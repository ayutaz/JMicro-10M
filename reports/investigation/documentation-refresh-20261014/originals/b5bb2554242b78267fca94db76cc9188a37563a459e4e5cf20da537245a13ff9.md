# 実行管理・後続準備・その他 — 7/26

[分野一覧へ](07_operations.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/progress-result.json) ／ SHA256: `591940fcfd27ed7b659411bc11ec3cf0f61fcc7f4bf4a9046c6deee3db30a59e` ／ 1,947,575 bytes

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
| checkpoints.context_outcome_ranking.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/context-outcome-ranking-comparison-20261006/context_outcome_ranking/training/checkpoint-00323503.pt" |
| checkpoints.context_outcome_ranking.checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |
| checkpoints.context_outcome_ranking.binding.config_sha256 | "8de26074f0701ec1894fc239430179eaaa3e8096f5828359083da12377ef01b4" |
| checkpoints.context_outcome_ranking.binding.arm | "context_outcome_ranking" |
| checkpoints.context_outcome_ranking.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.context_outcome_ranking.binding.parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.context_outcome_ranking.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.context_outcome_ranking.binding.teacher_goals.web | 75000000 |
| checkpoints.context_outcome_ranking.binding.teacher_goals.story | 5000000 |
| checkpoints.context_outcome_ranking.binding.teacher_goals.ordinary_textbook | 10000000 |
| checkpoints.context_outcome_ranking.binding.teacher_goals.conditional_textbook | 10000000 |
| checkpoints.context_outcome_ranking.binding.optimizer_policy | "inherit" |
| checkpoints.context_outcome_ranking.binding.peak_lr | 1e-05 |
| checkpoints.context_outcome_ranking.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| checkpoints.context_outcome_ranking.binding.study_kind | "historical_parent_staged_CE_conditional_Web_KL_train_outcome_ranking_100M" |
| checkpoints.context_outcome_ranking.binding.sampler_policy | "Same inherited100M CE and conditional parent Web KL windows; separate TRAIN opposite-context ranking cursor/labels/exposures, no reheat/reset/new corpus." |
| checkpoints.context_outcome_ranking.binding.outcome_weight | 1 |
| checkpoints.context_outcome_ranking.binding.ranking_policy.kind | "train_opposite_context_non_EOS_outcome_ranking_v1" |
| checkpoints.context_outcome_ranking.binding.ranking_policy.coefficient | 1.0 |
| checkpoints.context_outcome_ranking.binding.ranking_policy.temperature | 1.0 |
| checkpoints.context_outcome_ranking.binding.ranking_policy.families_per_update | 2 |
| checkpoints.context_outcome_ranking.binding.ranking_policy.candidate_rows_per_family | 4 |
| checkpoints.context_outcome_ranking.binding.ranking_policy.context | 256 |
| checkpoints.context_outcome_ranking.binding.ranking_policy.row_order | "For each family: branch0-candidate0,branch0-candidate1,branch1-candidate0,branch1-candidate1; gold candidate equals branch." |
| checkpoints.context_outcome_ranking.binding.ranking_policy.scores | "Mean token log probability of complete candidate body, excluding EOS3 from vocabulary normalization; prefix and padding labels ignored." |
| checkpoints.context_outcome_ranking.binding.ranking_policy.objective | "Mean softplus(foil_score-gold_score) over both context poles of all selected families." |
| checkpoints.context_outcome_ranking.binding.ranking_policy.supervision | "Relational choice labels and positive/foil scored positions are separate from ordinary CE teachers and parent-KL soft target positions." |
| checkpoints.context_outcome_ranking.binding.ranking_policy.input_source | "Only already accepted1024 TRAIN families/2048 positive records; other opposite-state outcome is the foil. No dev/probe/test labels." |
| checkpoints.context_outcome_ranking.binding.ranking_policy.sampler | "Independent local seed42 permutation over all train families, cyclic epochs with seed+epoch; no filtering or global RNG consumption." |
| checkpoints.context_outcome_ranking.binding.ranking_inputs.path | "/home/aihub_ubuntu/jmicro-data/phase6/context-outcome-ranking-20261006/manifest.json" |
| checkpoints.context_outcome_ranking.binding.ranking_inputs.sha256 | "0b394e1d8ba9fc836001620a9c6b6035aebbe246a1aa3d52b87c15eb1a1edb58" |
| checkpoints.context_outcome_ranking.binding.KL_policy.kind | "frozen-parent-Web-body-conditional-non-EOS-KL-v1" |
| checkpoints.context_outcome_ranking.binding.KL_policy.direction | "parent_to_student" |
| checkpoints.context_outcome_ranking.binding.KL_policy.temperature | 1.0 |
| checkpoints.context_outcome_ranking.binding.KL_policy.coefficient | 1.0 |
| checkpoints.context_outcome_ranking.binding.KL_policy.every_completed_update | 1 |
| checkpoints.context_outcome_ranking.binding.KL_policy.reference_context | 1024 |
| checkpoints.context_outcome_ranking.binding.KL_policy.reference_batch | 8 |
| checkpoints.context_outcome_ranking.binding.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding target positions. Remove EOS3 from student conditional vocabulary; preserve parent non-EOS mass weight and all remaining vocabulary IDs." |
| checkpoints.context_outcome_ranking.binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| checkpoints.context_outcome_ranking.binding.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| checkpoints.context_outcome_ranking.binding.KL_policy.objective_component | "Full parent-to-student KL minus Bernoulli EOS-mass KL; exact weighted conditional non-EOS component only." |
| checkpoints.context_outcome_ranking.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.context_outcome_ranking.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.context_outcome_ranking.binding.positive_manifest_sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.context_outcome_ranking.binding.original_web.path | "/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards" |
| checkpoints.context_outcome_ranking.binding.original_web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.context_outcome_ranking.update | 323503 |
| checkpoints.context_outcome_ranking.tokens | 10600546304 |
| checkpoints.context_outcome_ranking.supervised_tokens | 10577786961 |
| checkpoints.context_outcome_ranking.additional_supervised_tokens | 100000000 |
| checkpoints.context_outcome_ranking.additional_input_tokens | 100532224 |
| checkpoints.context_outcome_ranking.source_teachers.web | 75000000 |
| checkpoints.context_outcome_ranking.source_teachers.story | 5000000 |
| checkpoints.context_outcome_ranking.source_teachers.ordinary_textbook | 10000000 |
| checkpoints.context_outcome_ranking.source_teachers.conditional_textbook | 10000000 |
| checkpoints.context_outcome_ranking.source_eos.web | 159170 |
| checkpoints.context_outcome_ranking.source_eos.story | 38240 |
| checkpoints.context_outcome_ranking.source_eos.ordinary_textbook | 74183 |
| checkpoints.context_outcome_ranking.source_eos.conditional_textbook | 234328 |
| checkpoints.context_outcome_ranking.source_input_tokens.web | 75183104 |
| checkpoints.context_outcome_ranking.source_input_tokens.story | 5039104 |
| checkpoints.context_outcome_ranking.source_input_tokens.ordinary_textbook | 10075136 |
| checkpoints.context_outcome_ranking.source_input_tokens.conditional_textbook | 10234880 |
| checkpoints.context_outcome_ranking.source_focus_teachers.web | 0 |
| checkpoints.context_outcome_ranking.source_focus_teachers.story | 0 |
| checkpoints.context_outcome_ranking.source_focus_teachers.ordinary_textbook | 0 |
| checkpoints.context_outcome_ranking.source_focus_teachers.conditional_textbook | 1407427 |
| checkpoints.context_outcome_ranking.focus_teacher_tokens | 1407427 |
| checkpoints.context_outcome_ranking.focus_token_digest | "afdd9ed988079f0c64ee887fe759d7668843c235c046dfd4ffd80df6e97e6dac" |
| checkpoints.context_outcome_ranking.weighted_teacher_mass | 100000000 |
| checkpoints.context_outcome_ranking.outcome_weight | 1 |
| checkpoints.context_outcome_ranking.training_seconds | 441.0778062947211 |
| checkpoints.context_outcome_ranking.completed_at | "2026-10-06T08:28:04.933673Z" |
| checkpoints.context_outcome_ranking.reference_non_EOS_teacher_probability_mass | 24981892.629882812 |
| checkpoints.context_outcome_ranking.reference_replay.kind | "frozen-parent-Web-body-conditional-non-EOS-KL-v1" |
| checkpoints.context_outcome_ranking.reference_replay.batch | 8 |
| checkpoints.context_outcome_ranking.reference_replay.context | 1024 |
| checkpoints.context_outcome_ranking.reference_replay.initial_cursor.seed | 42 |
| checkpoints.context_outcome_ranking.reference_replay.initial_cursor.epoch | 0 |
| checkpoints.context_outcome_ranking.reference_replay.initial_cursor.position | 10253920 |
| checkpoints.context_outcome_ranking.reference_replay.initial_cursor.context | 1024 |
| checkpoints.context_outcome_ranking.reference_replay.initial_cursor.blocks | 11939276 |
| checkpoints.context_outcome_ranking.reference_replay.stream.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoints.context_outcome_ranking.reference_replay.stream.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.context_outcome_ranking.reference_replay.stream.sampler.seed | 42 |
| checkpoints.context_outcome_ranking.reference_replay.stream.sampler.epoch | 0 |
| checkpoints.context_outcome_ranking.reference_replay.stream.sampler.position | 10278464 |
| checkpoints.context_outcome_ranking.reference_replay.stream.sampler.context | 1024 |
| checkpoints.context_outcome_ranking.reference_replay.stream.sampler.blocks | 11939276 |
| checkpoints.context_outcome_ranking.reference_replay.updates | 3068 |
| checkpoints.context_outcome_ranking.reference_replay.physical_input_tokens | 25133056 |
| checkpoints.context_outcome_ranking.reference_replay.body_positions | 25026383 |
| checkpoints.context_outcome_ranking.reference_replay.ignored_positions | 106673 |
| checkpoints.context_outcome_ranking.reference_replay.digest | "f5b042150492ace80a1f27edc2f0a70678a80b6fcc4a6b709a061fffc8792f37" |
| checkpoints.context_outcome_ranking.reference_teacher_weight_digest | "bd397b489d1cdf26e74942cb5553d959ef3f597a6d2c6df2d158f15837c1f5ca" |
| checkpoints.context_outcome_ranking.reference_input_tokens | 25133056 |
| checkpoints.context_outcome_ranking.reference_soft_target_body_positions | 25026383 |
| checkpoints.context_outcome_ranking.main_and_Web_reference_physical_input_tokens | 125665280 |
| checkpoints.context_outcome_ranking.combined_student_physical_input_tokens | 131948544 |
| checkpoints.context_outcome_ranking.combined_student_valid_input_tokens | 126688260 |
| checkpoints.context_outcome_ranking.ranking_policy.kind | "train_opposite_context_non_EOS_outcome_ranking_v1" |
| checkpoints.context_outcome_ranking.ranking_policy.coefficient | 1.0 |
| checkpoints.context_outcome_ranking.ranking_policy.temperature | 1.0 |
| checkpoints.context_outcome_ranking.ranking_policy.families_per_update | 2 |
| checkpoints.context_outcome_ranking.ranking_policy.candidate_rows_per_family | 4 |
| checkpoints.context_outcome_ranking.ranking_policy.context | 256 |
| checkpoints.context_outcome_ranking.ranking_policy.row_order | "For each family: branch0-candidate0,branch0-candidate1,branch1-candidate0,branch1-candidate1; gold candidate equals branch." |
| checkpoints.context_outcome_ranking.ranking_policy.scores | "Mean token log probability of complete candidate body, excluding EOS3 from vocabulary normalization; prefix and padding labels ignored." |
| checkpoints.context_outcome_ranking.ranking_policy.objective | "Mean softplus(foil_score-gold_score) over both context poles of all selected families." |
| checkpoints.context_outcome_ranking.ranking_policy.supervision | "Relational choice labels and positive/foil scored positions are separate from ordinary CE teachers and parent-KL soft target positions." |
| checkpoints.context_outcome_ranking.ranking_policy.input_source | "Only already accepted1024 TRAIN families/2048 positive records; other opposite-state outcome is the foil. No dev/probe/test labels." |
| checkpoints.context_outcome_ranking.ranking_policy.sampler | "Independent local seed42 permutation over all train families, cyclic epochs with seed+epoch; no filtering or global RNG consumption." |
| checkpoints.context_outcome_ranking.ranking_input_binding.manifest_sha256 | "0b394e1d8ba9fc836001620a9c6b6035aebbe246a1aa3d52b87c15eb1a1edb58" |
| checkpoints.context_outcome_ranking.ranking_input_binding.train_manifest.path | "/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006/manifest.json" |
| checkpoints.context_outcome_ranking.ranking_input_binding.train_manifest.sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.context_outcome_ranking.ranking_input_binding.train_source.path | "/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006/train-source.json" |
| checkpoints.context_outcome_ranking.ranking_input_binding.train_source.sha256 | "89fa2aea6fddece74246e447859ec8a90155a76c166912fe1985cff962fd1f48" |
| checkpoints.context_outcome_ranking.ranking_input_binding.arrays_sha256 | "1f85f6a33e686327333568f03aa5e40eccf727362837dd6a29bb3375b672be82" |
| checkpoints.context_outcome_ranking.ranking_input_binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| checkpoints.context_outcome_ranking.ranking_input_binding.family_ids_sha256 | "8372b048071d942401fffd0bd2875e644e1633d9b30e6893b753572390eb6218" |
| checkpoints.context_outcome_ranking.ranking_sampler.kind | "train_family_outcome_ranking_sampler_v1" |
| checkpoints.context_outcome_ranking.ranking_sampler.binding.manifest_sha256 | "0b394e1d8ba9fc836001620a9c6b6035aebbe246a1aa3d52b87c15eb1a1edb58" |
| checkpoints.context_outcome_ranking.ranking_sampler.binding.train_manifest.path | "/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006/manifest.json" |
| checkpoints.context_outcome_ranking.ranking_sampler.binding.train_manifest.sha256 | "154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936" |
| checkpoints.context_outcome_ranking.ranking_sampler.binding.train_source.path | "/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006/train-source.json" |
| checkpoints.context_outcome_ranking.ranking_sampler.binding.train_source.sha256 | "89fa2aea6fddece74246e447859ec8a90155a76c166912fe1985cff962fd1f48" |
| checkpoints.context_outcome_ranking.ranking_sampler.binding.arrays_sha256 | "1f85f6a33e686327333568f03aa5e40eccf727362837dd6a29bb3375b672be82" |
| checkpoints.context_outcome_ranking.ranking_sampler.binding.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| checkpoints.context_outcome_ranking.ranking_sampler.binding.family_ids_sha256 | "8372b048071d942401fffd0bd2875e644e1633d9b30e6893b753572390eb6218" |
| checkpoints.context_outcome_ranking.ranking_sampler.seed | 42 |
| checkpoints.context_outcome_ranking.ranking_sampler.families_per_update | 2 |
| checkpoints.context_outcome_ranking.ranking_sampler.context | 256 |
| checkpoints.context_outcome_ranking.ranking_sampler.epoch | 5 |
| checkpoints.context_outcome_ranking.ranking_sampler.position | 1016 |
| checkpoints.context_outcome_ranking.ranking_sampler.updates | 3068 |
| checkpoints.context_outcome_ranking.ranking_sampler.families_seen | 6136 |
| checkpoints.context_outcome_ranking.ranking_sampler.relational_choice_labels | 12272 |
| checkpoints.context_outcome_ranking.ranking_sampler.valid_input_tokens | 1022980 |
| checkpoints.context_outcome_ranking.ranking_sampler.physical_input_positions | 6283264 |
| checkpoints.context_outcome_ranking.ranking_sampler.gold_body_scored_positions | 73725 |
| checkpoints.context_outcome_ranking.ranking_sampler.foil_body_scored_positions | 73725 |
| checkpoints.context_outcome_ranking.ranking_sampler.gold_body_scored_bytes | 315047 |
| checkpoints.context_outcome_ranking.ranking_sampler.foil_body_scored_bytes | 315047 |
| checkpoints.context_outcome_ranking.ranking_sampler.digest | "f5fda5bbab96066a63a036f6f33fd98998a0f043c83503b6cd07fd0a0ed23cbe" |
| checkpoints.context_outcome_ranking.ranking_exposure.updates | 3068 |
| checkpoints.context_outcome_ranking.ranking_exposure.families_seen | 6136 |
| checkpoints.context_outcome_ranking.ranking_exposure.relational_choice_labels | 12272 |
| checkpoints.context_outcome_ranking.ranking_exposure.valid_input_tokens | 1022980 |
| checkpoints.context_outcome_ranking.ranking_exposure.physical_input_positions | 6283264 |
| checkpoints.context_outcome_ranking.ranking_exposure.gold_body_scored_positions | 73725 |
| checkpoints.context_outcome_ranking.ranking_exposure.foil_body_scored_positions | 73725 |
| checkpoints.context_outcome_ranking.ranking_exposure.gold_body_scored_bytes | 315047 |
| checkpoints.context_outcome_ranking.ranking_exposure.foil_body_scored_bytes | 315047 |
| checkpoints.context_outcome_ranking.KL_policy.kind | "frozen-parent-Web-body-conditional-non-EOS-KL-v1" |
| checkpoints.context_outcome_ranking.KL_policy.direction | "parent_to_student" |
| checkpoints.context_outcome_ranking.KL_policy.temperature | 1.0 |
| checkpoints.context_outcome_ranking.KL_policy.coefficient | 1.0 |
| checkpoints.context_outcome_ranking.KL_policy.every_completed_update | 1 |
| checkpoints.context_outcome_ranking.KL_policy.reference_context | 1024 |
| checkpoints.context_outcome_ranking.KL_policy.reference_batch | 8 |
| checkpoints.context_outcome_ranking.KL_policy.masked_targets | "labels&gt;=8; ignore EOS/BOS/role/padding target positions. Remove EOS3 from student conditional vocabulary; preserve parent non-EOS mass weight and all remaining vocabulary IDs." |
| checkpoints.context_outcome_ranking.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| checkpoints.context_outcome_ranking.KL_policy.replay_policy | "separate fork of actual historical parent Web cursor; train only, overlaps first75M primary Web, never dev/test" |
| checkpoints.context_outcome_ranking.KL_policy.objective_component | "Full parent-to-student KL minus Bernoulli EOS-mass KL; exact weighted conditional non-EOS component only." |
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
| evaluations.context_outcome_ranking.binding.teacher_goals.web | 75000000 |
| evaluations.context_outcome_ranking.binding.teacher_goals.story | 5000000 |
| evaluations.context_outcome_ranking.binding.teacher_goals.ordinary_textbook | 10000000 |
| evaluations.context_outcome_ranking.binding.teacher_goals.conditional_textbook | 10000000 |
| evaluations.context_outcome_ranking.binding.loss | "ordinary original body+EOS CE, outcome weight1" |
| evaluations.context_outcome_ranking.binding.sampler_policy | "Same inherited100M CE and conditional parent Web KL windows; separate TRAIN opposite-context ranking cursor/labels/exposures, no reheat/reset/new corpus." |
| evaluations.context_outcome_ranking.binding.ranking_policy.families_per_update | 2 |
| evaluations.context_outcome_ranking.binding.ranking_policy.sampler | "Independent local seed42 permutation over all train families, cyclic epochs with seed+epoch; no filtering or global RNG consumption." |
| evaluations.context_outcome_ranking.binding.KL_policy.every_completed_update | 1 |
| evaluations.context_outcome_ranking.binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| evaluations.context_outcome_ranking.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| evaluations.context_outcome_ranking.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| evaluations.context_outcome_ranking.checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |
| evaluations.context_outcome_ranking.body.documents | 256 |
| evaluations.context_outcome_ranking.body.limit_documents | 256 |
| evaluations.context_outcome_ranking.body.body_nll | 323411.1250305176 |
| evaluations.context_outcome_ranking.body.eos_nll | 517.7313129939139 |
| evaluations.context_outcome_ranking.body.body_bytes | 472055 |
| evaluations.context_outcome_ranking.body.body_tokens | 122343 |
| evaluations.context_outcome_ranking.body.bpb | 0.9884094570544709 |
| evaluations.context_outcome_ranking.body.seconds | 1.2839610580122098 |
| evaluations.context_outcome_ranking.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.context_outcome_ranking.generation.max_new_tokens | 64 |
| evaluations.context_outcome_ranking.greedy_rates.eos | 41 |
| evaluations.context_outcome_ranking.greedy_rates.repetition | 21 |
| evaluations.context_outcome_ranking.greedy_rates.unicode_failure | 0 |
| evaluations.context_outcome_ranking.greedy_rates.role_leak | 0 |
| evaluations.context_outcome_ranking.greedy_rates.empty | 0 |
| evaluations.context_outcome_ranking.diagnostics.semantics.primary.accuracy.point | 0.59375 |
| evaluations.context_outcome_ranking.diagnostics.semantics.primary.accuracy.ci95 | [0.546875, 0.640625] |
| evaluations.context_outcome_ranking.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.context_outcome_ranking.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.context_outcome_ranking.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.context_outcome_ranking.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.semantics.primary.hard_accuracy | 0.59375 |
| evaluations.context_outcome_ranking.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5885416666666666 |
| evaluations.context_outcome_ranking.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.6354166666666666] |
| evaluations.context_outcome_ranking.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.context_outcome_ranking.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.context_outcome_ranking.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.context_outcome_ranking.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.context_outcome_ranking.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5885416666666666 |
| evaluations.context_outcome_ranking.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5882624392627378 |
| evaluations.context_outcome_ranking.diagnostics.semantics.per_token_secondary.mcc | 0.17732400774015752 |
| evaluations.context_outcome_ranking.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.context_outcome_ranking.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.context_outcome_ranking.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.context_outcome_ranking.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.context_outcome_ranking.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.context_outcome_ranking.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.context_outcome_ranking.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.context_outcome_ranking.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.primary.accuracy.point | 0.7522658610271903 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.primary.accuracy.ci95 | [0.7069486404833837, 0.797583081570997] |
| evaluations.context_outcome_ranking.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.primary.hard_accuracy | 0.7522658610271903 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7220543806646526 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6737160120845922, 0.770392749244713] |
| evaluations.context_outcome_ranking.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7220543806646526 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4192982456140351 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.context_outcome_ranking.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.context_outcome_ranking.diagnostics.jblimp.raw_pair_accuracy | 0.7673716012084593 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.primary.accuracy.point | 0.33958891867739055 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.primary.accuracy.ci95 | [0.3118856121537087, 0.3672922252010724] |
| evaluations.context_outcome_ranking.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.context_outcome_ranking.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jcqa.primary.hard_accuracy | 0.33958891867739055 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.32082216264521896 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2931188561215371, 0.3485254691689008] |
| evaluations.context_outcome_ranking.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.context_outcome_ranking.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.32082216264521896 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3202529966325722 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.per_token_secondary.mcc | 0.15168655619820284 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.context_outcome_ranking.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.context_outcome_ranking.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.context_outcome_ranking.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.context_outcome_ranking.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.context_outcome_ranking.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.context_outcome_ranking.diagnostics.semantic_both_contexts.correct | 21 |
| evaluations.context_outcome_ranking.memory.maximum_observed_allocated_bytes | 348777472 |
| evaluations.context_outcome_ranking.memory.maximum_observed_reserved_bytes | 12694061056 |
| evaluations.context_outcome_ranking.protected_test_used | false |
| mechanism_cached.checkpoints.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/eos-decoupled-web-kl-comparison-20261006/eos_decoupled_web_kl/training/checkpoint-00323503.pt" |
| mechanism_cached.checkpoints.checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |
| mechanism_cached.checkpoints.binding.config_sha256 | "1d31739438ffcd2e2ef93c725e16b0ed23d0fec6417ece5f2268766e88881017" |
| mechanism_cached.checkpoints.binding.arm | "eos_decoupled_web_kl" |
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
| mechanism_cached.checkpoints.binding.study_kind | "historical_parent_staged_CE_frozen_Web_conditional_non_EOS_KL_100M" |
| mechanism_cached.checkpoints.binding.sampler_policy | "Same historical fullstate/actualLR.00001/main staged100M streams as cached control, plus separately counted frozen-parent Web body KL replay. Main and reference cursors separate; no reheat/reset/new corpus." |
| mechanism_cached.checkpoints.binding.outcome_weight | 1 |
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
| mechanism_cached.checkpoints.training_seconds | 287.5748953077127 |
| mechanism_cached.checkpoints.completed_at | "2026-10-06T07:25:26.363788Z" |
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
| mechanism_cached.checkpoints.combined_student_physical_input_tokens | 125665280 |
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
| mechanism_cached.evaluations.binding.sampler_policy | "Same historical fullstate/actualLR.00001/main staged100M streams as cached control, plus separately counted frozen-parent Web body KL replay. Main and reference cursors separate; no reheat/reset/new corpus." |
| mechanism_cached.evaluations.binding.KL_policy.every_completed_update | 1 |
| mechanism_cached.evaluations.binding.KL_policy.reference_teacher | "immutable actual historical10.5B parent, no optimizer/gradients" |
| mechanism_cached.evaluations.binding.reference_teacher.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| mechanism_cached.evaluations.binding.reference_teacher.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| mechanism_cached.evaluations.checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |
| mechanism_cached.evaluations.body.documents | 256 |
| mechanism_cached.evaluations.body.limit_documents | 256 |
| mechanism_cached.evaluations.body.body_nll | 321651.43452215195 |
| mechanism_cached.evaluations.body.eos_nll | 513.1300341412425 |
| mechanism_cached.evaluations.body.body_bytes | 472055 |
| mechanism_cached.evaluations.body.body_tokens | 122343 |
| mechanism_cached.evaluations.body.bpb | 0.9830314888729699 |
| mechanism_cached.evaluations.body.seconds | 1.4468623629945796 |
| mechanism_cached.evaluations.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| mechanism_cached.evaluations.generation.max_new_tokens | 64 |
| mechanism_cached.evaluations.greedy_rates.eos | 44 |
| mechanism_cached.evaluations.greedy_rates.repetition | 20 |
| mechanism_cached.evaluations.greedy_rates.unicode_failure | 0 |
| mechanism_cached.evaluations.greedy_rates.role_leak | 0 |
| mechanism_cached.evaluations.greedy_rates.empty | 0 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.point | 0.5729166666666666 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.ci95 | [0.5260416666666666, 0.6197916666666666] |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.units | 96 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.examples | 192 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.primary.hard_accuracy | 0.5729166666666666 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5520833333333334 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5104166666666666, 0.59375] |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.count | 192 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5520833333333334 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5508649766075508 |
| mechanism_cached.evaluations.diagnostics.semantics.per_token_secondary.mcc | 0.10473644811127698 |
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
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.point | 0.743202416918429 |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.ci95 | [0.6978851963746223, 0.7885196374622356] |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.units | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.examples | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.primary.hard_accuracy | 0.743202416918429 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7190332326283988 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6706948640483383, 0.7673716012084593] |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.count | 331 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7190332326283988 |
| mechanism_cached.evaluations.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4182776801405975 |
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
| mechanism_cached.evaluations.diagnostics.jblimp.raw_pair_accuracy | 0.7583081570996979 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.point | 0.33958891867739055 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.ci95 | [0.3127792672028597, 0.36642091152815] |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.units | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jcqa.primary.hard_accuracy | 0.33958891867739055 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3100983020554066 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28239499553172476, 0.3360142984807864] |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.count | 1119 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3100983020554066 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.30903529199025803 |
| mechanism_cached.evaluations.diagnostics.jcqa.per_token_secondary.mcc | 0.13825571947644602 |
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
| mechanism_cached.evaluations.diagnostics.semantic_both_contexts.correct | 19 |
| mechanism_cached.evaluations.memory.maximum_observed_allocated_bytes | 315223040 |
| mechanism_cached.evaluations.memory.maximum_observed_reserved_bytes | 13046382592 |
| mechanism_cached.evaluations.protected_test_used | false |
| mechanism_cached.transfer.checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |
| mechanism_cached.transfer.checks.weights_unchanged | true |
| mechanism_cached.transfer.checks.no_gradients | true |
| mechanism_cached.transfer.checks.eval_mode | true |
| mechanism_cached.transfer.checks.RNG_restored | true |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.6953125 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.all128.both_correct | 54 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 42 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5625 |
| mechanism_cached.transfer.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 12 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.6875 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 54 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 68 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 98 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.828125 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 42 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 22 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.546875 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 12 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 46 |
| mechanism_cached.transfer.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.71484375 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 59 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 65 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 98 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.859375 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 46 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 18 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 63 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5703125 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 13 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 47 |
| mechanism_cached.transfer.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 35 |
| mechanism_cached.transfer.optimizer_updates | 0 |
| mechanism_cached.transfer.scientific_teacher_tokens | 0 |
| mechanism_cached.transfer.protected_test_used | false |
| mechanism_cached.transfer.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| mechanism_cached.retention.checkpoint_sha256 | "a27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213" |
| mechanism_cached.retention.checks.weights_unchanged | true |
| mechanism_cached.retention.checks.no_gradients | true |
| mechanism_cached.retention.checks.eval_mode | true |
| mechanism_cached.retention.checks.RNG_restored | true |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.60546875 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.all128.both_correct | 33 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.6875 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 27 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| mechanism_cached.retention.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 6 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.625 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 37 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 86 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 103 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6953125 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 28 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 33 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5546875 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 9 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 53 |
| mechanism_cached.retention.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.61328125 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 34 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 89 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 103 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.703125 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 28 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 34 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 54 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 6 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 55 |
| mechanism_cached.retention.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 49 |
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
| transfer.context_outcome_ranking.checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |
| transfer.context_outcome_ranking.checks.weights_unchanged | true |
| transfer.context_outcome_ranking.checks.no_gradients | true |
| transfer.context_outcome_ranking.checks.eval_mode | true |
| transfer.context_outcome_ranking.checks.RNG_restored | true |
| transfer.context_outcome_ranking.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.7578125 |
| transfer.context_outcome_ranking.summary.aggregate.sum_log_likelihood.all128.both_correct | 86 |
| transfer.context_outcome_ranking.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| transfer.context_outcome_ranking.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 63 |
| transfer.context_outcome_ranking.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| transfer.context_outcome_ranking.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 23 |
| transfer.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.7578125 |
| transfer.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 86 |
| transfer.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 22 |
| transfer.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 102 |
| transfer.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| transfer.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 63 |
| transfer.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 1 |
| transfer.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| transfer.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 23 |
| transfer.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 21 |
| transfer.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 38 |
| transfer.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.7578125 |
| transfer.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 86 |
| transfer.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 22 |
| transfer.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 102 |
| transfer.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| transfer.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 63 |
| transfer.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 1 |
| transfer.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| transfer.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 23 |
| transfer.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 21 |
| transfer.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 38 |
| transfer.context_outcome_ranking.optimizer_updates | 0 |
| transfer.context_outcome_ranking.scientific_teacher_tokens | 0 |
| transfer.context_outcome_ranking.protected_test_used | false |
| transfer.context_outcome_ranking.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
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
| retention.context_outcome_ranking.checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |
| retention.context_outcome_ranking.checks.weights_unchanged | true |
| retention.context_outcome_ranking.checks.no_gradients | true |
| retention.context_outcome_ranking.checks.eval_mode | true |
| retention.context_outcome_ranking.checks.RNG_restored | true |
| retention.context_outcome_ranking.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.78125 |
| retention.context_outcome_ranking.summary.aggregate.sum_log_likelihood.all128.both_correct | 80 |
| retention.context_outcome_ranking.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.9140625 |
| retention.context_outcome_ranking.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 53 |
| retention.context_outcome_ranking.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.6484375 |
| retention.context_outcome_ranking.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 27 |
| retention.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.7734375 |
| retention.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 80 |
| retention.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 38 |
| retention.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 105 |
| retention.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.9140625 |
| retention.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 53 |
| retention.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 11 |
| retention.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.6328125 |
| retention.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 27 |
| retention.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 27 |
| retention.context_outcome_ranking.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| retention.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.78125 |
| retention.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 80 |
| retention.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 40 |
| retention.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| retention.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.9140625 |
| retention.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 53 |
| retention.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 11 |
| retention.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6484375 |
| retention.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 27 |
| retention.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 29 |
| retention.context_outcome_ranking.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| retention.context_outcome_ranking.optimizer_updates | 0 |
| retention.context_outcome_ranking.scientific_teacher_tokens | 0 |
| retention.context_outcome_ranking.protected_test_used | false |
| retention.context_outcome_ranking.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/review.json — web_KL_CE100M_all80_and_cached_stagedCE100M_reviewed</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/review.json) ／ SHA256: `16698e66626d9229f83cad7a600990d7d8b1692091178266c12c3db5de7f17bc` ／ 15,282 bytes

| 原キー | 保存値 |
|---|---|
| status | "web_KL_CE100M_all80_and_cached_stagedCE100M_reviewed" |
| mechanism_comparison.checks.coherence_gain_at_least8 | false |
| mechanism_comparison.checks.paired_CI_lower_above0 | false |
| mechanism_comparison.checks.EOS_nonworsening | false |
| mechanism_comparison.checks.repetition_nonworsening | false |
| mechanism_comparison.checks.no_empty_role_unicode | true |
| mechanism_comparison.checks.BPB_gate | true |
| mechanism_comparison.checks.appropriate_completion_not_punctuation | true |
| mechanism_comparison.passed | false |
| mechanism_summary.BPB | 0.9830314888729699 |
| mechanism_summary.rates.eos | 44 |
| mechanism_summary.rates.repetition | 20 |
| mechanism_summary.rates.unicode_failure | 0 |
| mechanism_summary.rates.role_leak | 0 |
| mechanism_summary.rates.empty | 0 |
| mechanism_summary.grammar2 | 58 |
| mechanism_summary.relevance2 | 49 |
| mechanism_summary.coherent | 11 |
| mechanism_summary.appropriate | 28 |
| mechanism_summary.notes_sha256 | "5be5a2e6914ff8ad35c089462b657298a91daec7deca6080acba86de13c55ba2" |
| mechanism_summary.additional_teacher_tokens | 100000000 |
| previous_related_study_GPU_seconds | 1173.5953914780694 |
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
| summaries.context_outcome_ranking.BPB | 0.9884094570544709 |
| summaries.context_outcome_ranking.rates.eos | 41 |
| summaries.context_outcome_ranking.rates.repetition | 21 |
| summaries.context_outcome_ranking.rates.unicode_failure | 0 |
| summaries.context_outcome_ranking.rates.role_leak | 0 |
| summaries.context_outcome_ranking.rates.empty | 0 |
| summaries.context_outcome_ranking.grammar2 | 37 |
| summaries.context_outcome_ranking.relevance2 | 41 |
| summaries.context_outcome_ranking.coherent | 2 |
| summaries.context_outcome_ranking.appropriate | 22 |
| summaries.context_outcome_ranking.notes_sha256 | "e03024c23b3a5e2fb5e27ce6490db590e8eab6ef0d9c2942a1df785acbea8d76" |
| summaries.context_outcome_ranking.additional_teacher_tokens | 100000000 |
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
| transfer_aggregates.context_outcome_ranking.sum_log_likelihood.all128.accuracy | 0.7578125 |
| transfer_aggregates.context_outcome_ranking.sum_log_likelihood.all128.both_correct | 86 |
| transfer_aggregates.context_outcome_ranking.sum_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| transfer_aggregates.context_outcome_ranking.sum_log_likelihood.lexical_holdout.both_correct | 63 |
| transfer_aggregates.context_outcome_ranking.sum_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| transfer_aggregates.context_outcome_ranking.sum_log_likelihood.structural_holdout.both_correct | 23 |
| transfer_aggregates.context_outcome_ranking.mean_token_log_likelihood.all128.families | 128 |
| transfer_aggregates.context_outcome_ranking.mean_token_log_likelihood.all128.accuracy | 0.7578125 |
| transfer_aggregates.context_outcome_ranking.mean_token_log_likelihood.all128.both_correct | 86 |
| transfer_aggregates.context_outcome_ranking.mean_token_log_likelihood.all128.same_unique_candidate | 22 |
| transfer_aggregates.context_outcome_ranking.mean_token_log_likelihood.all128.aligned_context_margin_shift | 102 |
| transfer_aggregates.context_outcome_ranking.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.context_outcome_ranking.mean_token_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| transfer_aggregates.context_outcome_ranking.mean_token_log_likelihood.lexical_holdout.both_correct | 63 |
| transfer_aggregates.context_outcome_ranking.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 1 |
| transfer_aggregates.context_outcome_ranking.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.context_outcome_ranking.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.context_outcome_ranking.mean_token_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| transfer_aggregates.context_outcome_ranking.mean_token_log_likelihood.structural_holdout.both_correct | 23 |
| transfer_aggregates.context_outcome_ranking.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 21 |
| transfer_aggregates.context_outcome_ranking.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 38 |
| transfer_aggregates.context_outcome_ranking.mean_byte_log_likelihood.all128.families | 128 |
| transfer_aggregates.context_outcome_ranking.mean_byte_log_likelihood.all128.accuracy | 0.7578125 |
| transfer_aggregates.context_outcome_ranking.mean_byte_log_likelihood.all128.both_correct | 86 |
| transfer_aggregates.context_outcome_ranking.mean_byte_log_likelihood.all128.same_unique_candidate | 22 |
| transfer_aggregates.context_outcome_ranking.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 102 |
| transfer_aggregates.context_outcome_ranking.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer_aggregates.context_outcome_ranking.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| transfer_aggregates.context_outcome_ranking.mean_byte_log_likelihood.lexical_holdout.both_correct | 63 |
| transfer_aggregates.context_outcome_ranking.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 1 |
| transfer_aggregates.context_outcome_ranking.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| transfer_aggregates.context_outcome_ranking.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer_aggregates.context_outcome_ranking.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| transfer_aggregates.context_outcome_ranking.mean_byte_log_likelihood.structural_holdout.both_correct | 23 |
| transfer_aggregates.context_outcome_ranking.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 21 |
| transfer_aggregates.context_outcome_ranking.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 38 |
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
| retention_aggregates.context_outcome_ranking.sum_log_likelihood.all128.accuracy | 0.78125 |
| retention_aggregates.context_outcome_ranking.sum_log_likelihood.all128.both_correct | 80 |
| retention_aggregates.context_outcome_ranking.sum_log_likelihood.lexical_holdout.accuracy | 0.9140625 |
| retention_aggregates.context_outcome_ranking.sum_log_likelihood.lexical_holdout.both_correct | 53 |
| retention_aggregates.context_outcome_ranking.sum_log_likelihood.structural_holdout.accuracy | 0.6484375 |
| retention_aggregates.context_outcome_ranking.sum_log_likelihood.structural_holdout.both_correct | 27 |
| retention_aggregates.context_outcome_ranking.mean_token_log_likelihood.all128.families | 128 |
| retention_aggregates.context_outcome_ranking.mean_token_log_likelihood.all128.accuracy | 0.7734375 |
| retention_aggregates.context_outcome_ranking.mean_token_log_likelihood.all128.both_correct | 80 |
| retention_aggregates.context_outcome_ranking.mean_token_log_likelihood.all128.same_unique_candidate | 38 |
| retention_aggregates.context_outcome_ranking.mean_token_log_likelihood.all128.aligned_context_margin_shift | 105 |
| retention_aggregates.context_outcome_ranking.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.context_outcome_ranking.mean_token_log_likelihood.lexical_holdout.accuracy | 0.9140625 |
| retention_aggregates.context_outcome_ranking.mean_token_log_likelihood.lexical_holdout.both_correct | 53 |
| retention_aggregates.context_outcome_ranking.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 11 |
| retention_aggregates.context_outcome_ranking.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention_aggregates.context_outcome_ranking.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.context_outcome_ranking.mean_token_log_likelihood.structural_holdout.accuracy | 0.6328125 |
| retention_aggregates.context_outcome_ranking.mean_token_log_likelihood.structural_holdout.both_correct | 27 |
| retention_aggregates.context_outcome_ranking.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 27 |
| retention_aggregates.context_outcome_ranking.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| retention_aggregates.context_outcome_ranking.mean_byte_log_likelihood.all128.families | 128 |
| retention_aggregates.context_outcome_ranking.mean_byte_log_likelihood.all128.accuracy | 0.78125 |
| retention_aggregates.context_outcome_ranking.mean_byte_log_likelihood.all128.both_correct | 80 |
| retention_aggregates.context_outcome_ranking.mean_byte_log_likelihood.all128.same_unique_candidate | 40 |
| retention_aggregates.context_outcome_ranking.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| retention_aggregates.context_outcome_ranking.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention_aggregates.context_outcome_ranking.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.9140625 |
| retention_aggregates.context_outcome_ranking.mean_byte_log_likelihood.lexical_holdout.both_correct | 53 |
| retention_aggregates.context_outcome_ranking.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 11 |
| retention_aggregates.context_outcome_ranking.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 58 |
| retention_aggregates.context_outcome_ranking.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention_aggregates.context_outcome_ranking.mean_byte_log_likelihood.structural_holdout.accuracy | 0.6484375 |
| retention_aggregates.context_outcome_ranking.mean_byte_log_likelihood.structural_holdout.both_correct | 27 |
| retention_aggregates.context_outcome_ranking.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 29 |
| retention_aggregates.context_outcome_ranking.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 47 |
| verification_ranking_exposure.updates | 40 |
| verification_ranking_exposure.families_seen | 80 |
| verification_ranking_exposure.relational_choice_labels | 160 |
| verification_ranking_exposure.valid_input_tokens | 13376 |
| verification_ranking_exposure.physical_input_positions | 81920 |
| verification_ranking_exposure.gold_body_scored_positions | 933 |
| verification_ranking_exposure.foil_body_scored_positions | 933 |
| verification_ranking_exposure.gold_body_scored_bytes | 4022 |
| verification_ranking_exposure.foil_body_scored_bytes | 4022 |
| new_scientific_teacher_tokens | 100000000 |
| reused_control_teacher_tokens | 100000000 |
| verification_teacher_tokens | 1307967 |
| GPU_seconds | 529.8342619489995 |
| verification_reference_non_EOS_teacher_probability_mass | 325778.16796875 |
| verification_reference_input_tokens | 327680 |
| verification_reference_soft_positions | 326339 |
| verification_GPU_seconds | 31.40799105199403 |
| prior_probe_GPU_seconds | 0.0 |
| Base_adopted | false |
| protected_test_used | false |
| limitations | "One100M mainCE with same parent/Adam/scheduler/RNG/LR/source quotas/order and same conditional parent Web KL windows. Extra TRAIN opposite-context ranking pairs/foil/gold body exposures and relational labels are separate, not equal input/supervision/time to control. No new corpus. Shared-generator local probes/nonblind repeated dev/one learned seed; independent seed/full dev/protected test/adoption pending." |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0000.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0000.json) ／ SHA256: `ea5a9ced5c7e7858657da468fe5fce4f31ebda2d279dcbabd627cec8d80f94d9` ／ 9,894 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0016.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0016.json) ／ SHA256: `4e199dbff3896feb3c60528452d921428bb3955d73e57cdbbdee3bcf3282a755` ／ 9,533 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0032.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0032.json) ／ SHA256: `cd7040e419a210444f42dc8520a0a4d0739f24bab2bc923b199eae4d81958d0e` ／ 10,174 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0048.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0048.json) ／ SHA256: `2ca90022122e8769437c4b5b97c2f70b31dd8e405c578e679ddf026236d16cc2` ／ 9,456 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0064.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0064.json) ／ SHA256: `f22269ab3221bdb92a7e98d5b0eac929e5ced0a1ad960e42bade5c3c2a7bd8cf` ／ 10,276 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0080.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0080.json) ／ SHA256: `2221e066d7da3032b71bff6bb7d87e9f45d641b9a9e649b5df2708fe01901e8a` ／ 9,646 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0096.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0096.json) ／ SHA256: `cc5b688f50f46f64157caa64c57f2ea35dde57bba649a48a802d58494f080d1a` ／ 9,741 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0112.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0112.json) ／ SHA256: `dfdad8484ce65f6c134fe828e5de7c626785cb3d4dd2fa1e84e8c6f29920d711` ／ 10,083 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0128.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0128.json) ／ SHA256: `9256724799134f2396c218f8e1cf0694bfcb2f92158f5d15f8e6bd6e597ad470` ／ 9,791 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0144.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0144.json) ／ SHA256: `dfab1f7e5012cda891a083842a142c14b4b5866903e468389c7226ee0acc0447` ／ 9,822 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0160.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0160.json) ／ SHA256: `560b3a7e30ad2a7cf3622ecf715f990015bda762ab733cce7cadd3b38cd38266` ／ 10,080 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0176.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0176.json) ／ SHA256: `766777892a5849379026f82ed8d13d354df67933fc86ce3206505ac45a777677` ／ 9,895 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0192.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0192.json) ／ SHA256: `41629abcac9bca68f4089595e92a9a642509bbf0ab778abe4a1cbabcb825977a` ／ 9,839 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0208.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0208.json) ／ SHA256: `26e206d5f33683a490b7771a322b0e1a585f4c039f0800891e8152f1f62b8efe` ／ 9,555 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0224.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0224.json) ／ SHA256: `db97150f796f48f8896d4a6340f05cd4f2f224e66187d6c4a0f9352b83203248` ／ 9,743 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0240.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0240.json) ／ SHA256: `7b27d4affed01eed6cdba6c6add5fe4051deb3025506e0189faeea919c82708c` ／ 9,546 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0256.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0256.json) ／ SHA256: `b0009bcab4aa1ca47797ea11e8430ef56aca6bc596312637a216494f932a6fa1` ／ 9,585 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0272.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0272.json) ／ SHA256: `f54f5327e75e61710acf55f19d5aaddf0dbc53b4f2a49aa18152a4c7fb7ec86f` ／ 9,547 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0288.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0288.json) ／ SHA256: `ac67b6923bde9c5e07dc55c0259ba023449b1530ac3b4e8182024bca5d6e957e` ／ 9,572 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0304.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0304.json) ／ SHA256: `f3cc9e4f1886f5b66b1ec41626d5e2e9bc29d39d9ecbe54a8e432aec55dd3bde` ／ 9,743 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0320.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0320.json) ／ SHA256: `ba76545c00d42885a2201a56785bfdf10adc116b2d3d142264658db48a0f303a` ／ 9,291 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0336.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0336.json) ／ SHA256: `1739110cc840628de7d18892d5269f9bbaedef900cf6f9517da2497349f9d2b1` ／ 9,385 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0352.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0352.json) ／ SHA256: `020e294ce2ef40f6589b0e127e577d6168733d0ece780492cfda84449cbc893f` ／ 9,733 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0368.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0368.json) ／ SHA256: `64c3b49223f11cc1f89cf9f16b697db8c1334ebfe8ca23195e7211f002baf348` ／ 9,505 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0384.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0384.json) ／ SHA256: `02c7901b6c412ad8d03fdf3148b9d394dd2ac4d6aacfafab8791fe3dfe264a99` ／ 9,819 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0400.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0400.json) ／ SHA256: `475b35a659015517ddad7c91b8299a219a33264706a28d4810f9c429ef3ace99` ／ 9,495 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0416.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0416.json) ／ SHA256: `8001c9f22bff1d82add8082615dcca0a8f63b9e43da0987ed710074f2892a84c` ／ 9,848 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0432.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0432.json) ／ SHA256: `d4d4b46a7be3dff50f9523644aa6127ba60a2b67f13038ba3c684fb9ff17a29d` ／ 9,302 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0448.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0448.json) ／ SHA256: `ddc333940754aff30be36273cee26d27b45ea4bcc67531a69e2645091a75be6b` ／ 9,520 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0464.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0464.json) ／ SHA256: `32dcfa05e3b3ba815c79f1cdaeee710f4d1be3a233d874ef6d32aae8afce82bd` ／ 9,351 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0480.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0480.json) ／ SHA256: `258b681426e867833a4ec41caebc0569f29d85aca86e726e3556e29bbef0bb61` ／ 9,393 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0496.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/0496.json) ／ SHA256: `5a17f4a340f6be1ff90be2812f480cbc316cd38dc60fbe371b93e8c70af61eed` ／ 9,428 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/result.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/bridge/context_outcome_ranking/result.json) ／ SHA256: `3ce822213215000ec66eb06810c681578584fdf5a0313f547b8b8bcab2980e06` ／ 185,412 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.7578125 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 86 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 63 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 23 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.7578125 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 86 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 22 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 102 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 63 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 1 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 23 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 21 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 38 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.7578125 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 86 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 22 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 102 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.9921875 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 63 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 1 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 23 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 21 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 38 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0000.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0000.json) ／ SHA256: `f3ce3247d21ba1b4ecd937202b1e4c1841d9fea6bc5381a885f42ea2014bb4cd` ／ 7,922 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0016.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0016.json) ／ SHA256: `a79962e42ef69b9e5dddb446d0c3bdfe6f8c737737c987567e2d0f254c6575bc` ／ 8,260 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0032.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0032.json) ／ SHA256: `e452542b95b1669701e466684237a148be8206060f92be6831f28b21196c953f` ／ 6,938 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0048.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0048.json) ／ SHA256: `b62c847ed12a45d318d5395fe40c106f69f7d0995aa627a6624a4d59751ef379` ／ 8,100 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0064.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0064.json) ／ SHA256: `c00d84492cbe70573de3da554ace3f13eab40cb405aa4827072c09eddce646b7` ／ 8,452 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0080.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0080.json) ／ SHA256: `727ca20353876d68a3f57f7abd0ca37bdfc3ad48de956297835c002eadf3889f` ／ 7,037 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0096.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0096.json) ／ SHA256: `6db109c38a0451ead6f0b15762c5c0cfe7b2a2012131972ecf700086070ea91d` ／ 8,014 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0112.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0112.json) ／ SHA256: `789b0ada16dbdd664b0329818197add04db394b5f8f72b5acf1077c1f91a3424` ／ 8,188 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0128.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0128.json) ／ SHA256: `8c3ba038ab812049c4d59536087a007a38a48997ee4ea76c592bc4b750f35f31` ／ 7,045 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0144.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0144.json) ／ SHA256: `d14421ba7ad0531e7eddda450f7867acff1e1ee88702c0942c4469d720ba0274` ／ 8,119 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0160.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0160.json) ／ SHA256: `b1a930a249d7e4d0eaf803908a6e397ead7ac40a6cf5f33706d0b266f1b1ef21` ／ 8,548 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0176.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0176.json) ／ SHA256: `2073ce06c2b026960b575d238b42af83475a8add448d347940006dcf25c677c2` ／ 6,873 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0192.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0192.json) ／ SHA256: `7bc09572eecd95bebc19bf6fed40a7429b415190860a844f09c276574708448d` ／ 8,115 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0208.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0208.json) ／ SHA256: `bfc54b78a98e66be9da6d30fe3291e75e35da7af6e3ee51ce67b66805371fa34` ／ 8,455 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0224.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0224.json) ／ SHA256: `b6edc429c9d5783e59e2df9b443ec1c5e171dde6b7ba3573b2fe14c233db07ea` ／ 7,036 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0240.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0240.json) ／ SHA256: `473f3397734acc9e50fb8857bcb7d50d911a00b767e02bce176edd0faa011eb4` ／ 8,263 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0256.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0256.json) ／ SHA256: `ea142e06597e72598cd8a504c02db010a78570ecf2bdb36dff107cc6742d010b` ／ 8,214 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0272.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0272.json) ／ SHA256: `57d21fc724e3db0b88f98c555bd1fe88f1d22edfbfce36e0de8b8e592a5bc496` ／ 8,383 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0288.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0288.json) ／ SHA256: `98741e041b1c7ca05d7d2b331142e1e1ba89d363c361648dfe1fde2d03e9c2c2` ／ 7,057 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0304.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0304.json) ／ SHA256: `b0791a8b4d9ce2f13f0f60dd570a538acdd8d987bf6d598cfb8a817a0a24e21b` ／ 8,118 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0320.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0320.json) ／ SHA256: `104bbb038fd72513c4175d217749a58833f019237c6f45b07d331811ab546190` ／ 8,550 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0336.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0336.json) ／ SHA256: `c93c85369bcc8ec18ca8b4a5c6ccddc770f6a4cf38401f6062150e8fa922fc8a` ／ 7,061 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0352.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0352.json) ／ SHA256: `9522c94d42bd939439e792fb623ce82c3789e7b7a7b92d3cab432a2bd7fe5dd8` ／ 8,121 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0368.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0368.json) ／ SHA256: `c9dbcc4ee20b9a4e72f966b9678287a12402df7410c5fb30ca689de1dc39ec5c` ／ 8,133 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0384.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0384.json) ／ SHA256: `9c9a0705b324885ab825a5102b218b4be202df6c75df4a920aeb0f575155e54e` ／ 6,966 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0400.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0400.json) ／ SHA256: `0d559cef0b6a58e3bcfe1a0a22914b9ea753ba8de8a3cf99ad263e0c129de355` ／ 8,106 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0416.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0416.json) ／ SHA256: `6310270be065a42cf01d08c08e81d3c0f205f741ad63b5b46f6c0c31a3f35843` ／ 8,147 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0432.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0432.json) ／ SHA256: `af805d394b12c47071f8530752d701428a867e5a4dcbfc7eee4c179d8a0b069b` ／ 7,054 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0448.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0448.json) ／ SHA256: `e284ffaf057f25afb3624c841b7a3684539e62e8211906f43a2bdf8ba9e1fc38` ／ 8,044 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0464.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0464.json) ／ SHA256: `dd04cbe08239d7b9c98ec2c25813b6e4e547b0c0b5bd4b34bc61f468f65ac7be` ／ 8,298 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0480.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0480.json) ／ SHA256: `6012d82737f1d7e9d6964841d29f0ced419730c1033d30ae18d629865d101916` ／ 6,968 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>

<details>
<summary>reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0496.json — None</summary>

[原記録](../../reports/phase6/context-outcome-ranking-comparison-20261006/transfer/retention/context_outcome_ranking/0496.json) ／ SHA256: `686c4439b3f2c3c9d90ef14d02402b24899a99f723de3163f2de8f8f216780fe` ／ 8,050 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "c95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c" |

</details>
