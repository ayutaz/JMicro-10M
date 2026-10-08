# 教材・供給・品質・量 — 7/14

[分野一覧へ](02_material.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/evaluation/authored_news/evaluation/semantics.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/evaluation/authored_news/evaluation/semantics.json) ／ SHA256: `bd6b2b5d822ac5b62caeda647660712284413523b5c4513c645227c7f2b91e6d` ／ 203,134 bytes

| 原キー | 保存値 |
|---|---|
| summary.primary.accuracy.point | 0.59375 |
| summary.primary.accuracy.ci95 | [0.5520833333333334, 0.640625] |
| summary.primary.accuracy.units | 96 |
| summary.primary.accuracy.examples | 192 |
| summary.primary.accuracy.unit | "family/prompt" |
| summary.primary.accuracy.seed | 42 |
| summary.primary.accuracy.repetitions | 2000 |
| summary.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.primary.hard_accuracy | 0.59375 |
| summary.per_token_secondary.accuracy.point | 0.5885416666666666 |
| summary.per_token_secondary.accuracy.ci95 | [0.546875, 0.6354166666666666] |
| summary.per_token_secondary.accuracy.units | 96 |
| summary.per_token_secondary.accuracy.examples | 192 |
| summary.per_token_secondary.accuracy.unit | "family/prompt" |
| summary.per_token_secondary.accuracy.seed | 42 |
| summary.per_token_secondary.accuracy.repetitions | 2000 |
| summary.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summary.per_token_secondary.count | 192 |
| summary.per_token_secondary.hard_accuracy | 0.5885416666666666 |
| summary.per_token_secondary.macro_f1 | 0.5884411884411884 |
| summary.per_token_secondary.mcc | 0.17716986318620467 |
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
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/job.json) ／ SHA256: `57126f7741ec8fd1b87b1ebd8c51c3d2a932ff1aa7dde21232094a2efaf44a35` ／ 791 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 115.1166807099944 |
| teachers | 25976793 |
| teacher_budget | 26428122 |
| loss | 2.35932993888855 |
| source_teachers.web | 1428122 |
| source_teachers.authored_news | 24548671 |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/probe/job.json) ／ SHA256: `4872375caddcacb3abe740de8dce68419378b0fde2e38cd7e2cd38c711563cd9` ／ 577 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 28.335452045983402 |
| completed_updates | 32 |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/probe/news_boundary_stress/latest.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/probe/news_boundary_stress/latest.json) ／ SHA256: `25992278edbfcd85bfa21278a215a6a1a34719e10a66dab4a86af209fb7e3d49` ／ 280 bytes

| 原キー | 保存値 |
|---|---|
| update | 322717 |
| tokens_seen | 10574790656 |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/probe/original_Web/latest.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/probe/original_Web/latest.json) ／ SHA256: `99f7115634d230d772347d9bdd4a5dab6f61112e9f9194cc7b6429edb9d18cd4` ／ 272 bytes

| 原キー | 保存値 |
|---|---|
| update | 322717 |
| tokens_seen | 10574790656 |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/probe/result.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/probe/result.json) ／ SHA256: `afcac92c83cbbeb951df0fb058bf7fbb3ff12e8ba5b5102b0302e1a29e25df7c` ／ 116,471 bytes

| 原キー | 保存値 |
|---|---|
| gates.original_Web.passed | true |
| gates.original_Web.checks.model | true |
| gates.original_Web.checks.optimizer | true |
| gates.original_Web.checks.scheduler | true |
| gates.original_Web.checks.rng | true |
| gates.original_Web.checks.sampler | true |
| gates.original_Web.checks.lineage | true |
| gates.original_Web.checks.tokens | true |
| gates.original_Web.checks.supervised_tokens | true |
| gates.original_Web.checks.body_bytes | true |
| gates.original_Web.checks.token_digest | true |
| gates.original_Web.checks.focus_token_digest | true |
| gates.original_Web.checks.focus_teacher_tokens | true |
| gates.original_Web.checks.weighted_teacher_mass | true |
| gates.original_Web.checks.update | true |
| gates.original_Web.checks.spec | true |
| gates.original_Web.checks.model_config | true |
| gates.original_Web.checks.pilot_binding | true |
| gates.original_Web.checks.study_binding | true |
| gates.original_Web.checks.history_update | true |
| gates.original_Web.checks.history_loss | true |
| gates.original_Web.checks.history_gradient_norm | true |
| gates.original_Web.checks.history_lr | true |
| gates.original_Web.checks.history_tokens_seen | true |
| gates.original_Web.checks.history_supervised_tokens | true |
| gates.original_Web.checks.history_body_bytes_seen | true |
| gates.original_Web.checks.history_token_digest | true |
| gates.original_Web.checks.history_focus_token_digest | true |
| gates.original_Web.checks.history_focus_teacher_tokens | true |
| gates.original_Web.checks.history_weighted_teacher_mass | true |
| gates.original_Web.checks.history_outcome_weight | true |
| gates.original_Web.checks.history_source_teachers | true |
| gates.original_Web.checks.history_source_eos | true |
| gates.original_Web.checks.history_source_input_tokens | true |
| gates.original_Web.checks.history_source_body_bytes | true |
| gates.original_Web.checks.history_source_focus_teachers | true |
| gates.original_Web.checks.history_valid_input_tokens | true |
| gates.original_Web.checks.history_physical_input_tokens | true |
| gates.original_Web.checks.history_additional_teacher_tokens | true |
| gates.original_Web.checks.finite | true |
| gates.original_Web.checks.fixed_inherited_LR | true |
| gates.original_Web.verification_teacher_tokens | 261592 |
| gates.original_Web.GPU_optimizer_updates | 8 |
| gates.news_boundary_stress.passed | true |
| gates.news_boundary_stress.checks.model | true |
| gates.news_boundary_stress.checks.optimizer | true |
| gates.news_boundary_stress.checks.scheduler | true |
| gates.news_boundary_stress.checks.rng | true |
| gates.news_boundary_stress.checks.sampler | true |
| gates.news_boundary_stress.checks.lineage | true |
| gates.news_boundary_stress.checks.tokens | true |
| gates.news_boundary_stress.checks.supervised_tokens | true |
| gates.news_boundary_stress.checks.body_bytes | true |
| gates.news_boundary_stress.checks.token_digest | true |
| gates.news_boundary_stress.checks.focus_token_digest | true |
| gates.news_boundary_stress.checks.focus_teacher_tokens | true |
| gates.news_boundary_stress.checks.weighted_teacher_mass | true |
| gates.news_boundary_stress.checks.update | true |
| gates.news_boundary_stress.checks.spec | true |
| gates.news_boundary_stress.checks.model_config | true |
| gates.news_boundary_stress.checks.pilot_binding | true |
| gates.news_boundary_stress.checks.study_binding | true |
| gates.news_boundary_stress.checks.history_update | true |
| gates.news_boundary_stress.checks.history_loss | true |
| gates.news_boundary_stress.checks.history_gradient_norm | true |
| gates.news_boundary_stress.checks.history_lr | true |
| gates.news_boundary_stress.checks.history_tokens_seen | true |
| gates.news_boundary_stress.checks.history_supervised_tokens | true |
| gates.news_boundary_stress.checks.history_body_bytes_seen | true |
| gates.news_boundary_stress.checks.history_token_digest | true |
| gates.news_boundary_stress.checks.history_focus_token_digest | true |
| gates.news_boundary_stress.checks.history_focus_teacher_tokens | true |
| gates.news_boundary_stress.checks.history_weighted_teacher_mass | true |
| gates.news_boundary_stress.checks.history_outcome_weight | true |
| gates.news_boundary_stress.checks.history_source_teachers | true |
| gates.news_boundary_stress.checks.history_source_eos | true |
| gates.news_boundary_stress.checks.history_source_input_tokens | true |
| gates.news_boundary_stress.checks.history_source_body_bytes | true |
| gates.news_boundary_stress.checks.history_source_focus_teachers | true |
| gates.news_boundary_stress.checks.history_valid_input_tokens | true |
| gates.news_boundary_stress.checks.history_physical_input_tokens | true |
| gates.news_boundary_stress.checks.history_additional_teacher_tokens | true |
| gates.news_boundary_stress.checks.finite | true |
| gates.news_boundary_stress.checks.fixed_inherited_LR | true |
| gates.news_boundary_stress.verification_teacher_tokens | 257698 |
| gates.news_boundary_stress.GPU_optimizer_updates | 8 |
| timings.original_Web.verification_teacher_tokens | 1046336 |
| timings.original_Web.terminal_save_seconds | 0.16470115300035104 |
| timings.original_Web.peak_VRAM_bytes | 6149106176 |
| timings.original_Web.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/livedoor-base-comparison-v2-20261006/probe/original_Web/timing.pt" |
| timings.original_Web.checkpoint.sha256 | "0d97866235203182359f581b6d01c2704c2f0713c258bcb1d4271409811fdb1a" |
| timings.news_boundary_stress.verification_teacher_tokens | 1037656 |
| timings.news_boundary_stress.terminal_save_seconds | 0.18173838697839528 |
| timings.news_boundary_stress.peak_VRAM_bytes | 6149106176 |
| timings.news_boundary_stress.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/livedoor-base-comparison-v2-20261006/probe/news_boundary_stress/timing.pt" |
| timings.news_boundary_stress.checkpoint.sha256 | "c47b241cee3e26b799ceee4faa4a967edf16b1eec485ebed27edb4d9b713e875" |
| passed | true |
| GPU_seconds | 28.335452045983402 |
| verification_teacher_tokens | 2603282 |
| verification_updates | 80 |
| scientific_teacher_tokens | 0 |
| measured_timing.source_timings.original_Web.steady_step_seconds | 0.13628264600993134 |
| measured_timing.source_timings.original_Web.teachers_per_update | 32697.833333333332 |
| measured_timing.source_timings.original_Web.warmup_seconds | 1.0855464238848072 |
| measured_timing.source_timings.original_Web.save_seconds | 0.16470115300035104 |
| measured_timing.source_timings.news_boundary_stress.steady_step_seconds | 0.0477208634983981 |
| measured_timing.source_timings.news_boundary_stress.teachers_per_update | 32457.125 |
| measured_timing.source_timings.news_boundary_stress.warmup_seconds | 1.4760750010318588 |
| measured_timing.source_timings.news_boundary_stress.save_seconds | 0.18173838697839528 |
| measured_timing.estimated_updates | 817 |
| measured_timing.steady_step_seconds | 0.13628264600993134 |
| measured_timing.warmup_seconds | 2.561621424916666 |
| measured_timing.save_seconds | 0.9086919348919764 |
| measured_timing.estimated_training_seconds | 114.81323514992255 |
| estimated_science_GPU_seconds | 449.2572056948993 |
| previous_failed_GPU_seconds | 1.419417480006814 |
| estimated_total_GPU_seconds | 479.0120752208895 |
| Base_complete | false |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/progress-result.json) ／ SHA256: `19bcb406f2a87955426624e39d0b3c31932f0a82410db1b1ec52fd9ff5a9f014` ／ 636,498 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.authored_news.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/livedoor-base-comparison-v2-20261006/authored_news/training/checkpoint-00323499.pt" |
| checkpoints.authored_news.checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |
| checkpoints.authored_news.binding.config_sha256 | "9e27df5b8ea2ba6aadb2e8fd1bc48f052a68b743ddd6f991a17ab89e64132d6e" |
| checkpoints.authored_news.binding.arm | "authored_news" |
| checkpoints.authored_news.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source-order-condition-comparison-v2-20261006/source_order/training/checkpoint-00322685.pt" |
| checkpoints.authored_news.binding.parent.sha256 | "1398ad1364d60e88382bca26e711e45b8b981275dc56d77fdae295674df297c7" |
| checkpoints.authored_news.binding.original_parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| checkpoints.authored_news.binding.original_parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| checkpoints.authored_news.binding.teacher_goals.web | 1428122 |
| checkpoints.authored_news.binding.teacher_goals.authored_news | 25000000 |
| checkpoints.authored_news.binding.study_kind | "authored_Japanese_news_vs_synthetic_native_Base100M_v1" |
| checkpoints.authored_news.binding.optimizer_policy | "inherit_native" |
| checkpoints.authored_news.binding.scientific | true |
| checkpoints.authored_news.update | 323499 |
| checkpoints.authored_news.tokens | 10600415232 |
| checkpoints.authored_news.supervised_tokens | 10577786961 |
| checkpoints.authored_news.additional_supervised_tokens | 26428122 |
| checkpoints.authored_news.additional_input_tokens | 26673152 |
| checkpoints.authored_news.source_teachers.web | 1428122 |
| checkpoints.authored_news.source_teachers.authored_news | 25000000 |
| checkpoints.authored_news.source_eos.web | 3064 |
| checkpoints.authored_news.source_eos.authored_news | 238510 |
| checkpoints.authored_news.source_input_tokens.web | 1434624 |
| checkpoints.authored_news.source_input_tokens.authored_news | 25238528 |
| checkpoints.authored_news.source_focus_teachers.web | 0 |
| checkpoints.authored_news.source_focus_teachers.authored_news | 0 |
| checkpoints.authored_news.focus_teacher_tokens | 0 |
| checkpoints.authored_news.focus_token_digest | "179baab1310e5fefbd4b7a09268deaadddd0308d06e996169063717ac048e9b1" |
| checkpoints.authored_news.weighted_teacher_mass | 26428122 |
| checkpoints.authored_news.outcome_weight | 1 |
| checkpoints.authored_news.training_seconds | 45.90560058527626 |
| checkpoints.authored_news.completed_at | "2026-10-06T14:29:11.203754Z" |
| checkpoints.authored_news.sampler.kind | "exact_staged_Web_then_authored_news_quota_v1" |
| checkpoints.authored_news.sampler.goals.web | 1428122 |
| checkpoints.authored_news.sampler.goals.authored_news | 25000000 |
| checkpoints.authored_news.sampler.source_order | ["web", "authored_news"] |
| checkpoints.authored_news.sampler.context | 1024 |
| checkpoints.authored_news.sampler.seed | 42 |
| checkpoints.authored_news.sampler.position | 814 |
| checkpoints.authored_news.sampler.source_teachers.web | 1428122 |
| checkpoints.authored_news.sampler.source_teachers.authored_news | 25000000 |
| checkpoints.authored_news.sampler.source_eos.web | 3064 |
| checkpoints.authored_news.sampler.source_eos.authored_news | 238510 |
| checkpoints.authored_news.sampler.source_tokens.web | 1434624 |
| checkpoints.authored_news.sampler.source_tokens.authored_news | 25238528 |
| checkpoints.authored_news.sampler.source_body_bytes.web | 5562565 |
| checkpoints.authored_news.sampler.source_body_bytes.authored_news | 92210860 |
| checkpoints.authored_news.sampler.source_focus_teachers.web | 0 |
| checkpoints.authored_news.sampler.source_focus_teachers.authored_news | 0 |
| checkpoints.authored_news.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| checkpoints.authored_news.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| checkpoints.authored_news.sampler.streams.web.sampler.seed | 42 |
| checkpoints.authored_news.sampler.streams.web.sampler.epoch | 0 |
| checkpoints.authored_news.sampler.streams.web.sampler.position | 10327321 |
| checkpoints.authored_news.sampler.streams.web.sampler.context | 1024 |
| checkpoints.authored_news.sampler.streams.web.sampler.blocks | 11939276 |
| checkpoints.authored_news.sampler.streams.authored_news.kind | "fresh_authored_news_contiguous_block_shuffle_v1" |
| checkpoints.authored_news.sampler.streams.authored_news.manifest_sha256 | "600d8e04e0ea266aef6d7180b6e95639f7260e910dc6a55b7a6ae7eeb7c38bfa" |
| checkpoints.authored_news.sampler.streams.authored_news.sampler.seed | 42 |
| checkpoints.authored_news.sampler.streams.authored_news.sampler.epoch | 47 |
| checkpoints.authored_news.sampler.streams.authored_news.sampler.position | 160 |
| checkpoints.authored_news.sampler.streams.authored_news.sampler.context | 1024 |
| checkpoints.authored_news.sampler.streams.authored_news.sampler.blocks | 521 |
| checkpoints.authored_news.source_body_bytes.web | 5562565 |
| checkpoints.authored_news.source_body_bytes.authored_news | 92210860 |
| checkpoints.authored_news.token_digest | "7a1d151a6be3cc79ca9143fa703e0ef02e89c203eb91b734e6418bce13ece3f9" |
| checkpoints.authored_news.model_config.schema_version | 1 |
| checkpoints.authored_news.model_config.architecture | "decoder_only_transformer" |
| checkpoints.authored_news.model_config.hidden_size | 256 |
| checkpoints.authored_news.model_config.num_attention_heads | 4 |
| checkpoints.authored_news.model_config.num_key_value_heads | 2 |
| checkpoints.authored_news.model_config.head_dim | 64 |
| checkpoints.authored_news.model_config.activation | "swiglu" |
| checkpoints.authored_news.model_config.norm | "rmsnorm" |
| checkpoints.authored_news.model_config.rms_norm_eps | 1e-06 |
| checkpoints.authored_news.model_config.qk_norm_type | "none" |
| checkpoints.authored_news.model_config.qk_norm_before_rope | true |
| checkpoints.authored_news.model_config.attention_scale | 0.125 |
| checkpoints.authored_news.model_config.rope_theta | 10000 |
| checkpoints.authored_news.model_config.rope_layout | "half_split" |
| checkpoints.authored_news.model_config.rotary_dim | 64 |
| checkpoints.authored_news.model_config.max_position_embeddings | 1024 |
| checkpoints.authored_news.model_config.tie_word_embeddings | true |
| checkpoints.authored_news.model_config.attention_bias | false |
| checkpoints.authored_news.model_config.mlp_bias | false |
| checkpoints.authored_news.model_config.dropout | 0.0 |
| checkpoints.authored_news.model_config.initializer_std | 0.02 |
| checkpoints.authored_news.model_config.norm_initial_gain | 1.0 |
| checkpoints.authored_news.model_config.status | "phase5_ablation" |
| checkpoints.authored_news.model_config.name | "JMicro-10M-T4K-NoQKNorm" |
| checkpoints.authored_news.model_config.vocab_size | 4096 |
| checkpoints.authored_news.model_config.num_hidden_layers | 13 |
| checkpoints.authored_news.model_config.intermediate_size | 640 |
| checkpoints.authored_news.model_config.expected_parameter_count | 10001152 |
| checkpoints.authored_news.unique_parameters | 10001152 |
| checkpoints.authored_news.reused_prefix_teacher_tokens | 73571878 |
| checkpoints.authored_news.total_teacher_tokens_from_original_parent | 100000000 |
| checkpoints.authored_news.pure_Web_continuation_matched_updates | 43 |
| evaluations.authored_news.binding.teacher_goals.web | 1428122 |
| evaluations.authored_news.binding.teacher_goals.authored_news | 25000000 |
| evaluations.authored_news.binding.scientific | true |
| evaluations.authored_news.checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |
| evaluations.authored_news.body.documents | 256 |
| evaluations.authored_news.body.limit_documents | 256 |
| evaluations.authored_news.body.body_nll | 334242.09346342087 |
| evaluations.authored_news.body.eos_nll | 314.84866300038993 |
| evaluations.authored_news.body.body_bytes | 472055 |
| evaluations.authored_news.body.body_tokens | 122343 |
| evaluations.authored_news.body.bpb | 1.0215110753959236 |
| evaluations.authored_news.body.seconds | 1.6565144920023158 |
| evaluations.authored_news.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.authored_news.generation.max_new_tokens | 64 |
| evaluations.authored_news.greedy_rates.eos | 49 |
| evaluations.authored_news.greedy_rates.repetition | 24 |
| evaluations.authored_news.greedy_rates.unicode_failure | 0 |
| evaluations.authored_news.greedy_rates.role_leak | 0 |
| evaluations.authored_news.greedy_rates.empty | 0 |
| evaluations.authored_news.diagnostics.semantics.primary.accuracy.point | 0.59375 |
| evaluations.authored_news.diagnostics.semantics.primary.accuracy.ci95 | [0.5520833333333334, 0.640625] |
| evaluations.authored_news.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.authored_news.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.authored_news.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.primary.hard_accuracy | 0.59375 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5885416666666666 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.546875, 0.6354166666666666] |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5885416666666666 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5884411884411884 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.mcc | 0.17716986318620467 |
| evaluations.authored_news.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.authored_news.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.authored_news.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.authored_news.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.authored_news.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.authored_news.diagnostics.jblimp.primary.accuracy.point | 0.770392749244713 |
| evaluations.authored_news.diagnostics.jblimp.primary.accuracy.ci95 | [0.7250755287009063, 0.8187311178247734] |
| evaluations.authored_news.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.authored_news.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.authored_news.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.primary.hard_accuracy | 0.770392749244713 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.716012084592145 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6676737160120846, 0.7673716012084593] |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.716012084592145 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.41725352112676056 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.authored_news.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.authored_news.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.authored_news.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.authored_news.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.authored_news.diagnostics.jblimp.raw_pair_accuracy | 0.7673716012084593 |
| evaluations.authored_news.diagnostics.jcqa.primary.accuracy.point | 0.37890974084003576 |
| evaluations.authored_news.diagnostics.jcqa.primary.accuracy.ci95 | [0.3512064343163539, 0.4075067024128686] |
| evaluations.authored_news.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.authored_news.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.authored_news.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jcqa.primary.hard_accuracy | 0.37890974084003576 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3418230563002681 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.31500223413762285, 0.36907953529937443] |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.34137622877569257 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.34100536204466153 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.mcc | 0.17689830849780755 |
| evaluations.authored_news.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.authored_news.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.authored_news.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.authored_news.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.authored_news.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.authored_news.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.authored_news.diagnostics.semantic_both_contexts.correct | 20 |
| evaluations.authored_news.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.authored_news.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.authored_news.protected_test_used | false |
| transfer.authored_news.checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |
| transfer.authored_news.checks.weights_unchanged | true |
| transfer.authored_news.checks.no_gradients | true |
| transfer.authored_news.checks.eval_mode | true |
| transfer.authored_news.checks.RNG_restored | true |
| transfer.authored_news.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5859375 |
| transfer.authored_news.summary.aggregate.sum_log_likelihood.all128.both_correct | 27 |
| transfer.authored_news.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.6328125 |
| transfer.authored_news.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 22 |
| transfer.authored_news.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| transfer.authored_news.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 5 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.61328125 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 30 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 97 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 105 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6796875 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 24 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 39 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 51 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.546875 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 6 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 58 |
| transfer.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 54 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.58203125 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 22 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 105 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.625 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 17 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 46 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 51 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 5 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 59 |
| transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 54 |
| transfer.authored_news.optimizer_updates | 0 |
| transfer.authored_news.scientific_teacher_tokens | 0 |
| transfer.authored_news.protected_test_used | false |
| transfer.authored_news.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| retention.authored_news.checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |
| retention.authored_news.checks.weights_unchanged | true |
| retention.authored_news.checks.no_gradients | true |
| retention.authored_news.checks.eval_mode | true |
| retention.authored_news.checks.RNG_restored | true |
| retention.authored_news.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5703125 |
| retention.authored_news.summary.aggregate.sum_log_likelihood.all128.both_correct | 24 |
| retention.authored_news.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.625 |
| retention.authored_news.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 17 |
| retention.authored_news.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.515625 |
| retention.authored_news.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 7 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.5625 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 19 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 106 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 78 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6015625 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 13 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 51 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 44 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 6 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 55 |
| retention.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 34 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.515625 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 10 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 112 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 80 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5703125 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 9 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 55 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 43 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4609375 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 1 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 57 |
| retention.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 37 |
| retention.authored_news.optimizer_updates | 0 |
| retention.authored_news.scientific_teacher_tokens | 0 |
| retention.authored_news.protected_test_used | false |
| retention.authored_news.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/review.json — news100M_all80_content_and_native_state_reviewed</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/review.json) ／ SHA256: `7ad97ea83c297481a0fd3127ff50704ec54fe5cf9bf364e724255e95f61d5cb3` ／ 4,291 bytes

| 原キー | 保存値 |
|---|---|
| status | "news100M_all80_content_and_native_state_reviewed" |
| summaries.authored_news.BPB | 1.0215110753959236 |
| summaries.authored_news.rates.eos | 49 |
| summaries.authored_news.rates.repetition | 24 |
| summaries.authored_news.rates.unicode_failure | 0 |
| summaries.authored_news.rates.role_leak | 0 |
| summaries.authored_news.rates.empty | 0 |
| summaries.authored_news.grammar2 | 45 |
| summaries.authored_news.relevance2 | 46 |
| summaries.authored_news.coherent | 17 |
| summaries.authored_news.appropriate | 18 |
| summaries.authored_news.notes_sha256 | "9f338300b1275a5bbdacef5c9082a26c2f7b0522cf497b2c3939354aa62e199b" |
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
| eligible_for_final_Base_validation | false |
| accounting.completed_updates | 814 |
| accounting.new_teacher_tokens | 26428122 |
| accounting.physical_input_positions | 26673152 |
| accounting.source_teachers.web | 1428122 |
| accounting.source_teachers.authored_news | 25000000 |
| accounting.source_EOS.web | 3064 |
| accounting.source_EOS.authored_news | 238510 |
| pure_Web_continuation_matched_updates | 43 |
| new_scientific_teacher_tokens | 26428122 |
| reused_prefix_teacher_tokens | 73571878 |
| total_teacher_tokens_from_original_parent | 100000000 |
| verification_teacher_tokens | 2603282 |
| new_total_GPU_seconds | 144.8715502359846 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| limitations | "Authored-news source/EOS/diversity replace synthetic post-Web25M; teacher counts match but inputs/updates do not. 523883 local body tokens, about47.265 repeated exposures, old Web overlap/global audit incomplete. One learned seed/nonblind repeated dev." |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0000.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0000.json) ／ SHA256: `7896f8c70efa1d216aec30ce2aed135f2f256ad0759c94a8e7ae3f9dd430945f` ／ 9,772 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0016.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0016.json) ／ SHA256: `1b4d4853268d73c14eae3f5075ac96a54c67156d2589d644510ffd803002e886` ／ 9,428 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0032.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0032.json) ／ SHA256: `3c01b21fb9b291c5a9199c06658e069ae7f7f4a6883502a85209646c37f78f5e` ／ 10,066 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0048.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0048.json) ／ SHA256: `2d20969683811c25ae2606c20e94196e7af8801681619a327a89d8bac9ee601b` ／ 9,351 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0064.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0064.json) ／ SHA256: `25a66ed05d5696160a0c4b24b1799b9dda693aa2b4de545621ef6344b9fe962d` ／ 10,126 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0080.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0080.json) ／ SHA256: `299863780a2221dc259d5d459ba7311517b06861714cde276839801faf8dbcee` ／ 9,550 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0096.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0096.json) ／ SHA256: `723497f14f76edb8b3dc6c911b81dcade405693e9bab8a29bf0166fc8afe70b6` ／ 9,644 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0112.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0112.json) ／ SHA256: `85a209c6488d7473db027380b53704f417ebb9e2d455a5b74f58f73c9771e617` ／ 9,989 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0128.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0128.json) ／ SHA256: `fe98c0dcfd18b8191b7df2153ec47fca2fd0d350326c1949bd810d484f3be78d` ／ 9,637 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0144.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0144.json) ／ SHA256: `26c82ab2d9b0cb638a022a00cb9ba2fe0032840a631026023be75acb12dfd4be` ／ 9,724 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0160.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0160.json) ／ SHA256: `87878a261640a0539dc11d3505525697a5c9033ba65218fb3770cbda5bd6641f` ／ 10,021 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0176.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0176.json) ／ SHA256: `c65b618919efe2c03392fadeb2da960322404db2f0a25cde2e537e55e6bb17fc` ／ 9,826 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0192.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0192.json) ／ SHA256: `df5b42b9fc010b00d984fd087f0aec44b7b7a20efc78da6edb7089fe14503899` ／ 9,734 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0208.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0208.json) ／ SHA256: `3eaf1c25d7396eb2bde730b525977ab098765140c56fa4deef5040e211edb3a4` ／ 9,469 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0224.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0224.json) ／ SHA256: `ba16e361b8775d5d76788699755dabcc05f1f0f36f45cf076a67c746a96e27d8` ／ 9,633 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0240.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0240.json) ／ SHA256: `2ea89d3334dedf2067e546796f558b3086c8cde6d28523fef043ff62ecebe092` ／ 9,440 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0256.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0256.json) ／ SHA256: `7994e2343e96be53e738ad628e829576223d01fa4f2f4126170eca80dbc201ce` ／ 9,420 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0272.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0272.json) ／ SHA256: `ce50423df512981d4a9aec6212db473ccaf1625e00ffdfd4b82f5590f59436b1` ／ 9,426 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0288.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0288.json) ／ SHA256: `57a4c9f74e1c241642f033b877863f62e997e87213665ac8f2f3f069b210c06a` ／ 9,414 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0304.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0304.json) ／ SHA256: `3652d50e3dcc4096e1b66678f01b4ff6048e721a03975c84a13c053056abf136` ／ 9,598 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0320.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0320.json) ／ SHA256: `6036a286dd4088d43d882465998ebd2fef1344073ded3cd004243b34e141f2d2` ／ 9,153 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0336.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0336.json) ／ SHA256: `4e916d1155c516ba3fc50ac5ac814bcaddbcd03feaab8956e5801dd49ce0b669` ／ 9,240 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0352.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0352.json) ／ SHA256: `56c35c730b4c948e4e7e012a0cc0931a162be71cb9831c6f2f46ce74d309a4ae` ／ 9,586 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0368.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0368.json) ／ SHA256: `f3e06179dde29aac0f6e0618a59c10b371071e2cd0792c5209b48b9a934688aa` ／ 9,331 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0384.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0384.json) ／ SHA256: `46a337b2ae6b7ad92a42e8321ca5445eaafd7262721a3408a45fcae13803eeae` ／ 9,655 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0400.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0400.json) ／ SHA256: `9cc97d9a0da324cb02e11a005513fbf814814be6b5c2055fe47f18495a0906dc` ／ 9,344 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0416.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0416.json) ／ SHA256: `075b1adbd0a96f38a5abd69925f2bff04ec013800b217da0bc1cabfee08453e0` ／ 9,683 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0432.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0432.json) ／ SHA256: `98ea6dad0a13566a6f4ffd7300c28179e7407219f2a62bb4ca605f50cd65b730` ／ 9,147 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0448.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0448.json) ／ SHA256: `f597569d02364abae658411cfefa5c1eb724957afea3ac929b70392eca86374e` ／ 9,402 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0464.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0464.json) ／ SHA256: `e4e82a35c574d2c1c4cd1e146e20b7dad74eabd7af4a596063174c25d8c4e848` ／ 9,240 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0480.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0480.json) ／ SHA256: `3c81f5f0e5c92e0fb148599d6f317fb6a2308c9972d8246820d9a88c47df94de` ／ 9,237 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0496.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/0496.json) ／ SHA256: `1aacfc36822a005854c207d17ddf869adf590726740a5ed6ba2c32921791424e` ／ 9,316 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/result.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/bridge/authored_news/result.json) ／ SHA256: `f69388fe56534132618d38184cf089ece1fa43f1fb2f385b090e958c958eaf15` ／ 186,495 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5859375 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 27 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.6328125 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 22 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 5 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.61328125 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 30 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 97 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 105 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6796875 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 24 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 39 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 51 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.546875 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 6 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 58 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 54 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.58203125 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 22 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 105 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.625 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 17 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 46 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 51 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 5 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 59 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 54 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0000.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0000.json) ／ SHA256: `b0cf82b0d1a71b99ea4a16004774220afb3afa4d46540c3a6b8eb93dc75028e3` ／ 7,865 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0016.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0016.json) ／ SHA256: `1c5cda7bb44d70e7940b28ee428dc091f734d524f327e6edee15b3b634216ac6` ／ 8,206 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0032.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0032.json) ／ SHA256: `9e6928e2472d62da3ca0d8f39706b211a7d160c9678e1f701a8948d0eca76027` ／ 6,887 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0048.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0048.json) ／ SHA256: `814bbc1a04afbf4c659471170d6e5000e681f3116597ad93c27cb924999f410c` ／ 8,071 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0064.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0064.json) ／ SHA256: `fd13d583abf67c79f08d75bf70fe2243e8368bb5635fe4e3231dc9b5fd4a62c9` ／ 8,365 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0080.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0080.json) ／ SHA256: `7f4e62acb2b86a57c49ea48dd529fac0e32b247b7a5dba725428cf44e11ef15e` ／ 6,972 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0096.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0096.json) ／ SHA256: `2054e88a4dc38e6a6666d5cfcc3f9a8c486426a27e5f977d3964db2dcf655d37` ／ 7,984 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0112.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0112.json) ／ SHA256: `c7b542ab97c95ed218cdc8d81e8e796167a85ffb68999c5d7d01e4a39e6ae430` ／ 8,130 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0128.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0128.json) ／ SHA256: `f3c650c2d436af79aee199401c42b9054abfb8c87d020a2eb9754c91fc5b356e` ／ 6,987 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0144.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0144.json) ／ SHA256: `137a8045502938b36972cb3286fc02b8735e48469a6f39d4d14ee655f00313b3` ／ 8,068 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0160.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0160.json) ／ SHA256: `3ae59ae3b5825823999f56ce3bc78e664f9f03bee5476164983b7f66cb8b8060` ／ 8,489 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0176.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0176.json) ／ SHA256: `f37b9da6f55a88d4e94bc5d0ba6b423ba5504dc6b13d05d248332665897bbee6` ／ 6,829 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0192.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0192.json) ／ SHA256: `10e5a59b635ab3370f96857bcc6eed37c41f8ac5b16a00b0bedd835b8466a37e` ／ 8,089 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0208.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0208.json) ／ SHA256: `1c66bbf5818035fbabcd469bb4d2b15dd7aa07cb4c6a2e746a57dcfcb70330bf` ／ 8,390 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0224.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0224.json) ／ SHA256: `52decdf2b67f93dcd51159f2922f4aee8cc6657a98c87d3ba2ca2c6540c50eee` ／ 6,992 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0240.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0240.json) ／ SHA256: `a955e210bd733a633e3cf7a62a9eac59aadafbaf66b037ea1ee9095a2f747936` ／ 8,238 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0256.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0256.json) ／ SHA256: `caf38bf5f8b4d405cdd654937c029480429ff5e574935e30ab49b0304c27d46d` ／ 8,142 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0272.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0272.json) ／ SHA256: `b8367d968c1f28822baae336f535c28ab92e0d8fd2ef3916abbf045c38305cba` ／ 8,286 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0288.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0288.json) ／ SHA256: `4dc707c4af1a015c5593ddbb17b567bcf565e2eb0e0d33134fdb597a321f219a` ／ 6,998 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0304.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0304.json) ／ SHA256: `d54488c382ff4ec89b5f307f7e2699e3ddf18f9728ef684eeb83ade3dac8fe70` ／ 8,061 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0320.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0320.json) ／ SHA256: `f73ef93298d13b4a054dbad08f31c27f7887b67ee7ab01946518e2f82814aea6` ／ 8,488 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0336.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0336.json) ／ SHA256: `2975bd976a333f5cf56b0c74f3da59e89fd5be03f8cd8cc16e79c068356063ad` ／ 7,004 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0352.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0352.json) ／ SHA256: `40f018fe8cec44d90f4de635d24ea4fee833262e7e5b3d6542d15b5996ead4d6` ／ 8,054 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0368.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0368.json) ／ SHA256: `3a6ee8c0271f09fbd2cdf61f44e78cd9b73a11e29fd6b33e1c5bdd456384fed2` ／ 8,046 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0384.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0384.json) ／ SHA256: `f2db1d4f476ee23408b5de93a8d8ca6e2351ec59a26f17a424b0b13326d6960d` ／ 6,908 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0400.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0400.json) ／ SHA256: `a54276261d0905e30b68c286ae5bb57a4cf17e5a13c9e03f1a24e9bd35e10a47` ／ 8,058 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0416.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0416.json) ／ SHA256: `11f2490e7a821819a193650669afbbaca1801c4888b720618c77c0b2ed5e03ac` ／ 8,045 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0432.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0432.json) ／ SHA256: `eaf467fbe197dc65a981e2f57e9b3618b693870d17b5e3af9c52c31d2ad95c2c` ／ 7,000 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0448.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0448.json) ／ SHA256: `894677ca5a2261df44e75c36c41fd6e8799b09cf959408e24feb56983c1c20dc` ／ 7,970 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0464.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0464.json) ／ SHA256: `43b2801a1362491d859ae1a9cee2e9dbe28b4df315d6f7d69ac8161437db5d71` ／ 8,219 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0480.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0480.json) ／ SHA256: `669d3586920f7e4d648b51c6195bbaff5996e39cffea02128c4e3a7ed64d2bb2` ／ 6,907 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0496.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/0496.json) ／ SHA256: `dcd2e1f3cd18e97c90ac7deff510f747b66a509e31d2932f2156593049e91b9c` ／ 7,991 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |

</details>

<details>
<summary>reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/result.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-comparison-v2-20261006/transfer/retention/authored_news/result.json) ／ SHA256: `16c1c629888c3869a6dbe186f8b0c6aa91cea22762518e6d4ed197f8d7d9620a` ／ 183,423 bytes

| 原キー | 保存値 |
|---|---|
| checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |
| checks.weights_unchanged | true |
| checks.no_gradients | true |
| checks.eval_mode | true |
| checks.RNG_restored | true |
| summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5703125 |
| summary.aggregate.sum_log_likelihood.all128.both_correct | 24 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.625 |
| summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 17 |
| summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.515625 |
| summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 7 |
| summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.5625 |
| summary.aggregate.mean_token_log_likelihood.all128.both_correct | 19 |
| summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 106 |
| summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 78 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6015625 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 13 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 51 |
| summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 44 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 6 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 55 |
| summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 34 |
| summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.515625 |
| summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 10 |
| summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 112 |
| summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 80 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5703125 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 9 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 55 |
| summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 43 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4609375 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 1 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 57 |
| summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 37 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |

</details>

<details>
<summary>reports/phase6/livedoor-base-probe-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-probe-launcher-20261006/launcher.json) ／ SHA256: `f5044959799d6f98e15087728b1322dbaf97bb884ec179e0e2f0f630ee12e928` ／ 106 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/livedoor-base-probe-launcher-20261006/result.json — failed</summary>

[原記録](../../reports/phase6/livedoor-base-probe-launcher-20261006/result.json) ／ SHA256: `a93e8fc136e20f617dcd6a28c6778f17c5ef6dcac25ca07cb6c2cb5bc154a6b3` ／ 176 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed" |

</details>

<details>
<summary>reports/phase6/livedoor-base-probe-launcher-v2-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-probe-launcher-v2-20261006/launcher.json) ／ SHA256: `b33381412a08070fec8c497b42ee89d1642d485cc2d2f4911d335b2145aa59fc` ／ 106 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/livedoor-base-probe-launcher-v2-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/livedoor-base-probe-launcher-v2-20261006/result.json) ／ SHA256: `aab9a169aa964345cd2065cd60a5d9fc31d824777b60d0899889c4dd10078413` ／ 178 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/livedoor-base-probe-preparation-initial-failure-20261006/failure.json — CPU_preparation_rejected</summary>

[原記録](../../reports/phase6/livedoor-base-probe-preparation-initial-failure-20261006/failure.json) ／ SHA256: `bc5d7556c6647d5aeb88c6ea6184ddd427bd8cb42ff91f60ba8a9b1581eefd43` ／ 376 bytes

| 原キー | 保存値 |
|---|---|
| status | "CPU_preparation_rejected" |
| GPU_seconds | 0 |

</details>

<details>
<summary>reports/phase6/livedoor-base-science-launcher-20261006/launcher.json — None</summary>

[原記録](../../reports/phase6/livedoor-base-science-launcher-20261006/launcher.json) ／ SHA256: `0d4d95db60a20fca34c3552cf7e890abd733b2c216cef98d9a66dc97c28243c3` ／ 97 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/livedoor-base-science-launcher-20261006/result.json — complete</summary>

[原記録](../../reports/phase6/livedoor-base-science-launcher-20261006/result.json) ／ SHA256: `891152e29f351d3ff2593ab9d17c92b4dbdc464abdd45e416d1a9b5445526425` ／ 178 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |

</details>

<details>
<summary>reports/phase6/livedoor-leads-20261006/content-review.json — fixed64_authored_news_content_reviewed</summary>

[原記録](../../reports/phase6/livedoor-leads-20261006/content-review.json) ／ SHA256: `0f4c15ea87f70e213152893a06350b1afcf4f04a2e38a44ac83d31e6e4a617d6` ／ 31,115 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed64_authored_news_content_reviewed" |
| documents | 64 |
| weak_documents | 8 |
| maximum_weak_documents | 10 |
| passed | true |
| quality_accepted | true |
| sample.path | "/home/aihub_ubuntu/jmicro-data/phase6/livedoor-leads-20261006/sample64.json" |
| sample.sha256 | "15bb8043577705292c4a20ccb0400b6847179794d0d9c1e0c6c4913def9fa82a" |
| notes.livedoor-4571636.weak | false |
| notes.livedoor-4571636.rationale | "転職希望の調査対象と割合を示し、新しい仕事への意欲という話題を一段落で説明する。" |
| notes.livedoor-4571636.canonical_sha256 | "edbeb40364c6a646acf83ac6bbdc3c4125a9b19e85eca798764ea663dacecb97" |
| notes.livedoor-4571636.original_article_sha256 | "8ce16cebaa2bffc8b2af3e3f4a6c884c048dca8ac0cec6acaeecbc18bcd77d55" |
| notes.livedoor-4571636.source_URL | "http://news.livedoor.com/article/detail/4571636/" |
| notes.livedoor-4669665.weak | false |
| notes.livedoor-4669665.rationale | "新しい球種が投手によって生まれたという短いニュース導入として主語と出来事が閉じる。" |
| notes.livedoor-4669665.canonical_sha256 | "6b001266bcfb88fb50d565012a8330c8cf0320d607deba6c2d8c640d0b5b565f" |
| notes.livedoor-4669665.original_article_sha256 | "f10841a9e5c5197db66f1d1307f8e934b96bb1a42de31dbe45f7dcc48bfbb336" |
| notes.livedoor-4669665.source_URL | "http://news.livedoor.com/article/detail/4669665/" |
| notes.livedoor-5934970.weak | false |
| notes.livedoor-5934970.rationale | "映画の公開と宣伝担当の活動を同じ作品に結び付けて説明する。軽微な表記揺れは弱判定にしない。" |
| notes.livedoor-5934970.canonical_sha256 | "96f1fcc5a1db10281454cb4e7ba8a8226b0e5801ca13998a44d8e3c0ac0e2643" |
| notes.livedoor-5934970.original_article_sha256 | "22f20dd2b3f84ede99090dd55112803a791f7a0fbe11f01952a2270ca5c986e7" |
| notes.livedoor-5934970.source_URL | "http://news.livedoor.com/article/detail/5934970/" |
| notes.livedoor-5936282.weak | false |
| notes.livedoor-5936282.rationale | "端末発売、販売会社、予約と店頭の様子を同じ発売ニュースとしてまとめる。" |
| notes.livedoor-5936282.canonical_sha256 | "4f27d60b29ba5c628ffdaa1546c2f8cb3a8b235d5d6678de1df7f529b1e0215b" |
| notes.livedoor-5936282.original_article_sha256 | "e37979724a079791ee44287e470dbb35596e01a1eb3394b4b574eceba1b581db" |
| notes.livedoor-5936282.source_URL | "http://news.livedoor.com/article/detail/5936282/" |
| notes.livedoor-5114008.weak | false |
| notes.livedoor-5114008.rationale | "選手の活動から過去の試合動画への関心へつながる人物紹介の導入。" |
| notes.livedoor-5114008.canonical_sha256 | "10211bf66977a98cb6238879251b8ae2cb06f58718fdf07c343c03e11392caec" |
| notes.livedoor-5114008.original_article_sha256 | "ed8985b96b04821ac75dcc2d2283b143d9a049c9beb05b0d4f07f0df964a4ca1" |
| notes.livedoor-5114008.source_URL | "http://news.livedoor.com/article/detail/5114008/" |
| notes.livedoor-5648783.weak | true |
| notes.livedoor-5648783.rationale | "スマホの着せ替えから中華店の冷やし中華へ話題が移り、原段落内では両者の関係を説明しない。" |
| notes.livedoor-5648783.canonical_sha256 | "1db59cac95a54b2e3f5c1606798abe303f55e1f9d540f342356e20b268c7e82e" |
| notes.livedoor-5648783.original_article_sha256 | "b5f406d1d80214d77b93afe7dfd9cb2c909115755e51406119cebf23c4593a30" |
| notes.livedoor-5648783.source_URL | "http://news.livedoor.com/article/detail/5648783/" |
| notes.livedoor-6773379.weak | false |
| notes.livedoor-6773379.rationale | "夏の旅行の予定と個人で計画したい人という話題を問いかけで閉じる導入。" |
| notes.livedoor-6773379.canonical_sha256 | "bde0b3aaa677f2cc9414c4b9c2793a1548dfbe6e290f3b7db5b02e9a2c41dfb6" |
| notes.livedoor-6773379.original_article_sha256 | "3c4a3e20ab6fd0f2c8e45b564aaec1d2ab894024e200f1f3255c11e89292ffbb" |
| notes.livedoor-6773379.source_URL | "http://news.livedoor.com/article/detail/6773379/" |
| notes.livedoor-6111186.weak | false |
| notes.livedoor-6111186.rationale | "スマホ利用者がビジネスマンから女性へ広がったという時間的な変化を説明する。" |
| notes.livedoor-6111186.canonical_sha256 | "eccfa127f36ee165246520412fe909eaba54cab9df51c7d82e24f1598f67cafe" |
| notes.livedoor-6111186.original_article_sha256 | "2154a8c8c9dd646cbc501ccf279a9bec14e9e57799aeea5ad9b022077cb8ee55" |
| notes.livedoor-6111186.source_URL | "http://news.livedoor.com/article/detail/6111186/" |
| notes.livedoor-6402950.weak | false |
| notes.livedoor-6402950.rationale | "市場情報を調べる従来の方法と、現在のサイトの対応範囲を対比している。" |
| notes.livedoor-6402950.canonical_sha256 | "c98dbc409cb3e5af14720d8e317bf4556ef525ef4412204a11e1060dfbed4d4f" |
| notes.livedoor-6402950.original_article_sha256 | "b3156e0e19d0b8834d07d04821780d43ed15c43633013944d619ce11c018948f" |
| notes.livedoor-6402950.source_URL | "http://news.livedoor.com/article/detail/6402950/" |
| notes.livedoor-5839953.weak | false |
| notes.livedoor-5839953.rationale | "映画の題名と、その題名につながる人物間の発言を紹介している。" |
| notes.livedoor-5839953.canonical_sha256 | "673b4921e9ff63b4470da9fb34ef5e36b394e9cfc26f9140416a38202e174487" |
| notes.livedoor-5839953.original_article_sha256 | "9d80b75b4e76ce5369aeddf9346253f07e34f98d1dac704600f1aa347d50d95d" |
| notes.livedoor-5839953.source_URL | "http://news.livedoor.com/article/detail/5839953/" |
| notes.livedoor-6478266.weak | false |
| notes.livedoor-6478266.rationale | "試写会の反応、前篇の成績、後篇の公開予定が同一作品に結び付く。" |
| notes.livedoor-6478266.canonical_sha256 | "fe9cf26405400ae65a7273a60df7bc548e39cb0999ad8097e6c3c4acfdc468a3" |
| notes.livedoor-6478266.original_article_sha256 | "2438999e3404636fb407fdb3f7f6d0012daf5ce9961684a6b6c8e00dc0f0ae35" |
| notes.livedoor-6478266.source_URL | "http://news.livedoor.com/article/detail/6478266/" |
| notes.livedoor-4958217.weak | false |
| notes.livedoor-4958217.rationale | "俳優二人の出身と共演を紹介し、取材の対象と話題まで明示する。" |
| notes.livedoor-4958217.canonical_sha256 | "ec51e55120fe2d3792d3a9322dc5011ec983f7a0b7268f41f3ce0129ba8cb31b" |
| notes.livedoor-4958217.original_article_sha256 | "0f298b2fb33c1748d4036f211e74591cca4bdb8af433e3ea3dcc492dcf48fbd1" |
| notes.livedoor-4958217.source_URL | "http://news.livedoor.com/article/detail/4958217/" |
| notes.livedoor-5045512.weak | false |
| notes.livedoor-5045512.rationale | "仕事帰りのゴルフ練習の移動負担から、継続しにくいという結論につながる。" |
| notes.livedoor-5045512.canonical_sha256 | "81168471c703a0fa2902f981c99ed501e93136fe0fe218c521a4cc7d95b3ed2c" |
| notes.livedoor-5045512.original_article_sha256 | "a5ddc01f130619a9e85e2a60b2fb2780f2308dfbdb6faf31747af1d01fb75334" |
| notes.livedoor-5045512.source_URL | "http://news.livedoor.com/article/detail/5045512/" |
| notes.livedoor-5806446.weak | true |
| notes.livedoor-5806446.rationale | "医学史や治療への有効性を広く無条件に肯定する宣伝的説明で、原段落に根拠や限定がない。" |
| notes.livedoor-5806446.canonical_sha256 | "097f51f52352278ac458e40870cd39ac177de4d5e2cad4e1099f07774394d402" |
| notes.livedoor-5806446.original_article_sha256 | "0328ee3c9d3a850a49044a02cf4c53aa8d5ec94a3d2db2341e0a7e5f611d77f4" |
| notes.livedoor-5806446.source_URL | "http://news.livedoor.com/article/detail/5806446/" |
| notes.livedoor-6123308.weak | false |
| notes.livedoor-6123308.rationale | "原作と映画の興行成績を示し、その作品の映像媒体発売という出来事を閉じる。" |
| notes.livedoor-6123308.canonical_sha256 | "c39696fac7e95a788c391ad68845b4b7bf62da32cdd329d4698c42918c9158f9" |
| notes.livedoor-6123308.original_article_sha256 | "76ec0e78c892100beedf4485b43c7c6164dae25f1a24d94c326b0e6ddbb9e926" |
| notes.livedoor-6123308.source_URL | "http://news.livedoor.com/article/detail/6123308/" |
| notes.livedoor-6426966.weak | false |
| notes.livedoor-6426966.rationale | "ブランド名を導入し、具体的な製品種別を列挙する短い説明として閉じる。" |
| notes.livedoor-6426966.canonical_sha256 | "b3162d8166aae97e0670310eef73b88ecbcc893b2f3be5cfef7d99cee7615720" |
| notes.livedoor-6426966.original_article_sha256 | "28a6058a68d4db925e541a0a1cd3e3b9ad307952606455bca852261cb8d2b71f" |
| notes.livedoor-6426966.source_URL | "http://news.livedoor.com/article/detail/6426966/" |
| notes.livedoor-6673821.weak | false |
| notes.livedoor-6673821.rationale | "企業キャンペーンと楽曲、出演とドラマ主題歌の関係を同じ発表にまとめる。" |
| notes.livedoor-6673821.canonical_sha256 | "453296e3dc0283ef52906ecc3ba0146ac92ca1352a17bfe660d8b49c2c43414a" |
| notes.livedoor-6673821.original_article_sha256 | "d828b77581b24a2826ff50f62d4cbd276bfa839eaf2eeb6a0b4cfbf8f773474b" |
| notes.livedoor-6673821.source_URL | "http://news.livedoor.com/article/detail/6673821/" |
| notes.livedoor-4497332.weak | false |
| notes.livedoor-4497332.rationale | "化粧品ブランドの過去のテーマと新商品発表を示す導入。続きの紹介予告自体は許す。" |
| notes.livedoor-4497332.canonical_sha256 | "ad02c0ed3047e5ac2868a15426dbd7c386b31d268adcb86ecac3d3176a9291bf" |
| notes.livedoor-4497332.original_article_sha256 | "b31225d943355cd62e798294e4776d7a5c6de4e1b659d4e36a8490966a6b13bd" |
| notes.livedoor-4497332.source_URL | "http://news.livedoor.com/article/detail/4497332/" |
| notes.livedoor-5546006.weak | false |
| notes.livedoor-5546006.rationale | "大会成績とコーチによる復調をつなぐ人物紹介の段落として読める。" |
| notes.livedoor-5546006.canonical_sha256 | "8ba30988e5c8a4ebad37b5dcf3224fd1c31428bce0b0aa47f05220ef6f2ae9bd" |
| notes.livedoor-5546006.original_article_sha256 | "83044653ebd518d5ad169818f0977efa9a404f967e91204d1b4c238d5bc6cb07" |
| notes.livedoor-5546006.source_URL | "http://news.livedoor.com/article/detail/5546006/" |
| notes.livedoor-6369052.weak | false |
| notes.livedoor-6369052.rationale | "番組内の出来事へのネット反応を伝える短いニュース導入。詳細はないが対象番組と話題は明示される。" |
| notes.livedoor-6369052.canonical_sha256 | "8ea327516a340b09151bd8ced4f8a27f06247ef5f7b0171020376753fe17ca52" |
| notes.livedoor-6369052.original_article_sha256 | "08619f15a42b89e4c9fed7b2f21f4a6ba535f13402218319832a567ff1144caf" |
| notes.livedoor-6369052.source_URL | "http://news.livedoor.com/article/detail/6369052/" |
| notes.livedoor-4972112.weak | true |
| notes.livedoor-4972112.rationale | "焼肉を好む話からこちらのお店という紹介へ終わり、原段落には店の名前や対象がない。" |
| notes.livedoor-4972112.canonical_sha256 | "4fa5ef2f2db91293ad5b64adf6f4335257af73141ec1926b22b47614566d8aaf" |
| notes.livedoor-4972112.original_article_sha256 | "f7c8ec8c115bb081906a74f8ead7cb0b85b4f41a5eb4a620632f38662a0eb8a0" |
| notes.livedoor-4972112.source_URL | "http://news.livedoor.com/article/detail/4972112/" |
| notes.livedoor-6121996.weak | false |
| notes.livedoor-6121996.rationale | "監督の就任先、公式ページの出典、背番号という情報を一つの就任ニュースに結び付ける。" |
| notes.livedoor-6121996.canonical_sha256 | "4cfa1b57dcfc5db78fae438b394752831d946133267b637cf6ed0725cf88d0b4" |
| notes.livedoor-6121996.original_article_sha256 | "2f2f9ff9c761fef15d706460e0e91aa4438a98bb22d0bbd410451f1893cf429d" |
| notes.livedoor-6121996.source_URL | "http://news.livedoor.com/article/detail/6121996/" |
| notes.livedoor-6502605.weak | false |
| notes.livedoor-6502605.rationale | "ドラマの評判とDVD発売、宣伝担当者の就任を同じ作品の情報としてまとめる。" |
| notes.livedoor-6502605.canonical_sha256 | "2d79cab963c8f46529d40d357e36166310ce9aff4f1c63da685c348ab18ed85b" |
| notes.livedoor-6502605.original_article_sha256 | "f9d4e9c860528890c0ecc9866331afa1b9db60fc2190721c0f010b0b606e79d2" |
| notes.livedoor-6502605.source_URL | "http://news.livedoor.com/article/detail/6502605/" |
| notes.livedoor-5333688.weak | false |
| notes.livedoor-5333688.rationale | "人物の活動と婚活を紹介し、取材した話題を明示する短い導入。" |
| notes.livedoor-5333688.canonical_sha256 | "533559d890f082cce16d4b8c58ee279fa6c3a7d4b56ad6add161d2d338516f10" |
| notes.livedoor-5333688.original_article_sha256 | "08a43c8d4225aeb7b3511bde603976d0b64ee5dab3aecdf58e9039b7b35cb5c9" |
| notes.livedoor-5333688.source_URL | "http://news.livedoor.com/article/detail/5333688/" |
| notes.livedoor-5534000.weak | false |
| notes.livedoor-5534000.rationale | "番組、対戦相手、インタビュー対象の選手を明示する一文の放送ニュース。" |
| notes.livedoor-5534000.canonical_sha256 | "4b902b8c91ef126e982cb7157999e26b1f0e0280a6c786c261ae54344959dcfe" |
| notes.livedoor-5534000.original_article_sha256 | "641bb35ab71607e6c3661bfd28a11fae66022bd6f1605666c4ce5cdb85be96f0" |
| notes.livedoor-5534000.source_URL | "http://news.livedoor.com/article/detail/5534000/" |
| notes.livedoor-5385396.weak | false |
| notes.livedoor-5385396.rationale | "年度末の忙しさと出会いの増加を対比し、対象読者への期待につなげる。" |
| notes.livedoor-5385396.canonical_sha256 | "60e9dc1779046e87068505961cc066d2856d1ba7a4a2a4f1c82f100a3b549d66" |
| notes.livedoor-5385396.original_article_sha256 | "585783e0e13c62ec4150344edae72e6f7494401b3281f61af5d006def1527f83" |
| notes.livedoor-5385396.source_URL | "http://news.livedoor.com/article/detail/5385396/" |
| notes.livedoor-6425811.weak | false |
| notes.livedoor-6425811.rationale | "小説から映画への関係、公開予定、先行イベントを同一作品の話題として説明する。" |
| notes.livedoor-6425811.canonical_sha256 | "0a19dbb1f23e9e741357f664321c41574f29d5f707d9ef23c952c93f5234752d" |
| notes.livedoor-6425811.original_article_sha256 | "6fb997fb8beb4e0885048b5101e059246614b7c5f396d965b7af00fe20272d7d" |
| notes.livedoor-6425811.source_URL | "http://news.livedoor.com/article/detail/6425811/" |
| notes.livedoor-6160931.weak | true |
| notes.livedoor-6160931.rationale | "冒頭の正月休みはゆっくりというにオススメの句で、対象人物を表す語が欠落している。" |
| notes.livedoor-6160931.canonical_sha256 | "605d8c149833f5cb44ef7c2cd72ec068a4a7415dd77d57da3f441fa9dc29ef34" |
| notes.livedoor-6160931.original_article_sha256 | "fac84143b421efba2338b465e91ff222c814d2dc3a2e8d0a944d1b77934f90bc" |
| notes.livedoor-6160931.source_URL | "http://news.livedoor.com/article/detail/6160931/" |
| notes.livedoor-6591348.weak | true |
| notes.livedoor-6591348.rationale | "冒頭の北朝鮮の武装勢力拿捕されたに必要な格関係が欠け、捕獲主体と船員の構文が崩れる。" |
| notes.livedoor-6591348.canonical_sha256 | "551c0933386c994dbe39ac19fe9598a600804cc778ab64f05a0e9b246f27e2a0" |
| notes.livedoor-6591348.original_article_sha256 | "4b5766787187eb0af17fb5191d7c4fa573f10b5f6f6a92df0c47cb56be93748a" |
| notes.livedoor-6591348.source_URL | "http://news.livedoor.com/article/detail/6591348/" |
| notes.livedoor-5698268.weak | false |
| notes.livedoor-5698268.rationale | "選手の移籍と直近の私生活の報道を人物紹介の話題としてまとめる。" |
| notes.livedoor-5698268.canonical_sha256 | "dbe7f18cae06cc24574e46782b641794682e633cf7f933823efdf41a6d4d586e" |
| notes.livedoor-5698268.original_article_sha256 | "2b944bbcdb23aeadc583f83cfb321df59910736ef408ea0eadb61833a09b6747" |
| notes.livedoor-5698268.source_URL | "http://news.livedoor.com/article/detail/5698268/" |
| notes.livedoor-6308686.weak | false |
| notes.livedoor-6308686.rationale | "大会結果、監督の発言とその意図を述べ、引用内容と説明が整合する。" |
| notes.livedoor-6308686.canonical_sha256 | "68d913c069d603c1085bdaf550dbb420f3e95af5805d1b9f83dee0cb4c148c62" |
| notes.livedoor-6308686.original_article_sha256 | "851ee08886b124ec0770e55893522678eb00ebb96168774d0ecfc8add3b660e3" |
| notes.livedoor-6308686.source_URL | "http://news.livedoor.com/article/detail/6308686/" |
| notes.livedoor-6738885.weak | false |
| notes.livedoor-6738885.rationale | "英語の小見出しに続き、番組が密着した選手と発表時点を明示する完結した導入。" |
| notes.livedoor-6738885.canonical_sha256 | "423cf2590c25e201683c13cdd4862dd1066a434949fc96d2700a8bfea29f9b44" |
| notes.livedoor-6738885.original_article_sha256 | "f9b6c90fe8ba9abcf19859243a8b97e17d82d923f97aa8d0277e907afaa45d94" |
| notes.livedoor-6738885.source_URL | "http://news.livedoor.com/article/detail/6738885/" |
| notes.livedoor-6361219.weak | false |
| notes.livedoor-6361219.rationale | "強盗事件と店員の対応へのネット反応を出典付きで報じる導入。方法の詳細を後段へ残すことは許す。" |
| notes.livedoor-6361219.canonical_sha256 | "2943b33b6a3f68c9bdeadf1a558444687ffb2a60c0a6daa3d9c1ac96b4247fcc" |
| notes.livedoor-6361219.original_article_sha256 | "74fa0c67a1e047c31831f18cc21748ff123208c7daa9fe3ad5207a555fd1425a" |
| notes.livedoor-6361219.source_URL | "http://news.livedoor.com/article/detail/6361219/" |
| notes.livedoor-6471962.weak | false |
| notes.livedoor-6471962.rationale | "国籍取得と代表選出から出場が不確実になる状況変化を短く述べる。" |
| notes.livedoor-6471962.canonical_sha256 | "bd2b669bc577022739d0d3cff3520697d8ac8772511dca15b730bdb27eda1f57" |
| notes.livedoor-6471962.original_article_sha256 | "87565b37b0132a138b449d8e960528c728deb8e47842432be90d74d01c196c81" |
| notes.livedoor-6471962.source_URL | "http://news.livedoor.com/article/detail/6471962/" |
| notes.livedoor-6511242.weak | false |
| notes.livedoor-6511242.rationale | "映画の舞台と主人公、制作担当、海外での公開予定を同じ作品に結び付ける。" |
| notes.livedoor-6511242.canonical_sha256 | "1ff754cebaf1d9b1e08b0d8635c75aff01a6c32eb67f9e69c9e4f703df663d58" |
| notes.livedoor-6511242.original_article_sha256 | "42adb20b6f44916ee4c3a5187c9c1620f44527d6edc81216336d69392c9f1c14" |
| notes.livedoor-6511242.source_URL | "http://news.livedoor.com/article/detail/6511242/" |
| notes.livedoor-6610486.weak | false |
| notes.livedoor-6610486.rationale | "レビュー募集の主体、対象製品、人数と参加者への特典が一段落で説明される。" |
| notes.livedoor-6610486.canonical_sha256 | "9fad085330be307e25e9b24b9f91325c94f2a3260ce0148cf85db32feac4bce6" |
| notes.livedoor-6610486.original_article_sha256 | "e8a19c679f7278a2e9427bf64f5d1954dcea676f369f5297d73e25241354afde" |
| notes.livedoor-6610486.source_URL | "http://news.livedoor.com/article/detail/6610486/" |
| notes.livedoor-6076425.weak | false |
| notes.livedoor-6076425.rationale | "会社と三つの部署という組織構成を短く明示する説明段落。" |
| notes.livedoor-6076425.canonical_sha256 | "5e884a979d3e949e5588df522168e54ab2b29078a9b6acc0518b16d4ece75865" |
| notes.livedoor-6076425.original_article_sha256 | "2a31ed12c92cb5dde1201160575edc28d651695293091c10b10b16a316a8b297" |
| notes.livedoor-6076425.source_URL | "http://news.livedoor.com/article/detail/6076425/" |
| notes.livedoor-6499995.weak | false |
| notes.livedoor-6499995.rationale | "作品の画像公開と関連コンテストという二つの発表を同一映画にまとめる。" |
| notes.livedoor-6499995.canonical_sha256 | "847a92f80a187d4309d36f9272747c9aa6923c891301d0f9043d88b4eebcfa75" |
| notes.livedoor-6499995.original_article_sha256 | "86f355392bd8d0da61a66e8350ae04127eb5aca2434d4d0ce030a981c09e484f" |
| notes.livedoor-6499995.source_URL | "http://news.livedoor.com/article/detail/6499995/" |
| notes.livedoor-5380699.weak | false |
| notes.livedoor-5380699.rationale | "友人関係を意識する季節から新しい概念の存在へつなぐ問いかけの導入として読める。" |
| notes.livedoor-5380699.canonical_sha256 | "7aa0e9aecfd22c4b39727fbd12a7db4753c1df218e8f06f8203978606d87afa7" |
| notes.livedoor-5380699.original_article_sha256 | "becd5df6ca0cbc355fa1e2885729af44ac2a7e8ff376b0a265292943ef54976b" |
| notes.livedoor-5380699.source_URL | "http://news.livedoor.com/article/detail/5380699/" |
| notes.livedoor-4491554.weak | true |
| notes.livedoor-4491554.rationale | "二人で美容を楽しむ話からサロンがこちらと結ぶが、原段落には参照する店や場所がない。" |
| notes.livedoor-4491554.canonical_sha256 | "70075dfbf6a4d1d5ef501b1758d86cd95662f0c76afd5f939e6392eabe36c66e" |
| notes.livedoor-4491554.original_article_sha256 | "8cdc7e9aa6b9082048276dd77522b65850e33069cfa22a0cef82773db9c7f40e" |
| notes.livedoor-4491554.source_URL | "http://news.livedoor.com/article/detail/4491554/" |
| notes.livedoor-6703420.weak | false |
| notes.livedoor-6703420.rationale | "芸人が注目された経緯と、新しい冠番組の配信予定を同じ人物に結び付ける。" |
| notes.livedoor-6703420.canonical_sha256 | "e69f999d5427cd19a7dc3d4d401df63846ac80f6fcbbad77eb0e1d1b8405f4a6" |
| notes.livedoor-6703420.original_article_sha256 | "bbb6896a6e6cd731d1afc57c2d7c17e0fa03fb1aa1ee9adb8fae529a7980ff82" |
| notes.livedoor-6703420.source_URL | "http://news.livedoor.com/article/detail/6703420/" |
| notes.livedoor-6662611.weak | false |
| notes.livedoor-6662611.rationale | "地図アプリ内の表記とネット反応を対象地名を明示して報じる。歴史報道の記述であり現在の立場の認定ではない。" |
| notes.livedoor-6662611.canonical_sha256 | "e14d1786e3db08edec8d0c43f550352e61ad014d5310c0ea27390f4b4caaecc5" |
| notes.livedoor-6662611.original_article_sha256 | "3e15e30ff3dcf65e1b462fe9de0713d2cf022997e4f8484a7f78c6b90c53e78d" |
| notes.livedoor-6662611.source_URL | "http://news.livedoor.com/article/detail/6662611/" |
| notes.livedoor-6511389.weak | false |
| notes.livedoor-6511389.rationale | "番組名と放送局、公式サイトの番組説明を示す短い紹介段落。" |
| notes.livedoor-6511389.canonical_sha256 | "74e7ad0d543c36a2f1d862ecbf870a532f6ed36376ab429857b4758a3ae7f22c" |
| notes.livedoor-6511389.original_article_sha256 | "d28dafd427e1a185a3ad31a7d006f2fa74a43e41adbe7a494d41c10708ac260d" |
| notes.livedoor-6511389.source_URL | "http://news.livedoor.com/article/detail/6511389/" |
| notes.livedoor-5240023.weak | false |
| notes.livedoor-5240023.rationale | "年始の買物への関心から調査対象と割合へつながる同じ話題の説明。" |
| notes.livedoor-5240023.canonical_sha256 | "8dd0ffe297d0f354b65c30d4194292317d1566dc7b66b68d8fa89726ff90d3bc" |
| notes.livedoor-5240023.original_article_sha256 | "8a9c0367c2f18b7ab200945ec79e56ed0a3ac9904b1f0061f2a334e18d68e851" |
| notes.livedoor-5240023.source_URL | "http://news.livedoor.com/article/detail/5240023/" |
| notes.livedoor-6465411.weak | false |
| notes.livedoor-6465411.rationale | "映画前後篇の舞台と主人公の関係を対比して説明する。テーマの予告だけを失敗にしない。" |
| notes.livedoor-6465411.canonical_sha256 | "311ef22e8d069f95c9715ac850cad4a2ca80b9443d2a57af41857753dbc26a98" |
| notes.livedoor-6465411.original_article_sha256 | "63d83b7719cf396165c9065240fe4399394fc19d1fc6b6e5d7f487e43096ee60" |
| notes.livedoor-6465411.source_URL | "http://news.livedoor.com/article/detail/6465411/" |
| notes.livedoor-5825813.weak | true |
| notes.livedoor-5825813.rationale | "調査の対象と方法は示すが、最後にランキング結果をご覧くださいと指し、原段落にその結果がない。" |
| notes.livedoor-5825813.canonical_sha256 | "7c4bff510c8824dc320a48ed3700b330b89770032110084491ae755516f65c4c" |
| notes.livedoor-5825813.original_article_sha256 | "82e626b39bc37076cd6d06e9555a5aa02d400b3d1a8277435c034c10477dd42c" |
| notes.livedoor-5825813.source_URL | "http://news.livedoor.com/article/detail/5825813/" |
| notes.livedoor-5738688.weak | false |
| notes.livedoor-5738688.rationale | "用語や芸能人の発言を紹介し、聞き取りの疑問と対象を明示する取材導入。" |
| notes.livedoor-5738688.canonical_sha256 | "493b19846ba7682bf56e017086b9904d4d047e114bbdf1fa0194770c04590186" |
| notes.livedoor-5738688.original_article_sha256 | "b0e83498654f64845398d8cb2ad0841203a357a7f60d6f24936044da46468e45" |
| notes.livedoor-5738688.source_URL | "http://news.livedoor.com/article/detail/5738688/" |
| notes.livedoor-6850409.weak | false |
| notes.livedoor-6850409.rationale | "地方イベントの場所と日程、共催先を同じ開催案内にまとめる。" |
| notes.livedoor-6850409.canonical_sha256 | "b94beaa781ad2097a2be7d4dd696d862911a20f85a9f80d4c3b56498868a85b2" |
| notes.livedoor-6850409.original_article_sha256 | "47c4e8ce4ed9327167fd1cd6615d5eb0a84fc1a274ce30371a5bdd95d411e224" |
| notes.livedoor-6850409.source_URL | "http://news.livedoor.com/article/detail/6850409/" |
| notes.livedoor-6484815.weak | false |
| notes.livedoor-6484815.rationale | "男女の役割への筆者の意見から、家父長制の説明と書籍への帰属へつなぐ。価値観や歴史主張の正しさは未認証。" |
| notes.livedoor-6484815.canonical_sha256 | "4256886f398532f1fd9bb22bfae7b0aabeaf6e14958bac6480961ca966aaffc3" |
| notes.livedoor-6484815.original_article_sha256 | "39b030187ea9c5d4606ed4ff0284395998e514ba6c240a7519f4a5b4997dcebf" |
| notes.livedoor-6484815.source_URL | "http://news.livedoor.com/article/detail/6484815/" |
| notes.livedoor-6808796.weak | false |
| notes.livedoor-6808796.rationale | "店舗開設、関連キャンペーンと別店舗の改装という同じ企業の発表を整理する。" |
| notes.livedoor-6808796.canonical_sha256 | "3a3c33edb9d887b4db5b093150a7cf86559a10f4d6aec371da805c836c937d73" |
| notes.livedoor-6808796.original_article_sha256 | "ae7ee8eee0d09710c5d08a506c8a0290fd809d7a476cdce03dbe7c0100f89939" |
| notes.livedoor-6808796.source_URL | "http://news.livedoor.com/article/detail/6808796/" |
| notes.livedoor-5976932.weak | false |
| notes.livedoor-5976932.rationale | "寒暖の変化から体調と空気中の病原体への関心につなぐ季節の導入。" |
| notes.livedoor-5976932.canonical_sha256 | "9d7b8c9b0c3de0812bfe1e8ea5fdb7d8325ea8b91eecb1acb365ea57cb61af5c" |
| notes.livedoor-5976932.original_article_sha256 | "e37c60b88bc1891c205f2bc6af1c9485c794ae6e6412832e455fed4f0754d090" |
| notes.livedoor-5976932.source_URL | "http://news.livedoor.com/article/detail/5976932/" |
| notes.livedoor-5959843.weak | false |
| notes.livedoor-5959843.rationale | "伝記を出典として人物の製品への発言を引用・帰属させる一段落。主張を独立に事実認定するものではない。" |
| notes.livedoor-5959843.canonical_sha256 | "4804c51e4e1211e558f892f989bb4ceebcc49f6b5a8165ea4c8122e7daaec5f1" |
| notes.livedoor-5959843.original_article_sha256 | "9acf3a029875c88eb69003345d34d980027af937bd5db7d87facb6b68182ff82" |
| notes.livedoor-5959843.source_URL | "http://news.livedoor.com/article/detail/5959843/" |
| notes.livedoor-6556361.weak | false |
| notes.livedoor-6556361.rationale | "情報が多く投稿を見落とす問題から、特定の友人の投稿表示という方法の話題へつなげる。" |
| notes.livedoor-6556361.canonical_sha256 | "ddc0c7dd4f33a491a0bad4e6c7b45141d474f934a644e94f698ddd161b93c27e" |
| notes.livedoor-6556361.original_article_sha256 | "864a61b4137bdad2ace5e1834bb2325d348f793ec5c49e69a4525b6a2c82dce5" |
| notes.livedoor-6556361.source_URL | "http://news.livedoor.com/article/detail/6556361/" |
| notes.livedoor-5507645.weak | false |
| notes.livedoor-5507645.rationale | "試合中の落球、判定とその後の試合結果を同じ場面のニュースとしてまとめる。" |
| notes.livedoor-5507645.canonical_sha256 | "f2f9592d9b6a18f15059eb1d1219209d9b8ffdec12445f5e7d24760442242f12" |
| notes.livedoor-5507645.original_article_sha256 | "7e855ce1ee157c42d7f47325b4518e3ecbc529acb7ac319e890c05196ff29223" |
| notes.livedoor-5507645.source_URL | "http://news.livedoor.com/article/detail/5507645/" |
| notes.livedoor-6407997.weak | false |
| notes.livedoor-6407997.rationale | "機器の用途を定義し、既存機器に部品を加える利用方法まで説明する。" |
| notes.livedoor-6407997.canonical_sha256 | "9f318733326581047bc7c7f61798c6551c2c41c8893ac23e9ab6fbd332e2c4c4" |
| notes.livedoor-6407997.original_article_sha256 | "2a98db6863bc87e762e474691dfc4bd1e7add500370caf2a2cd5c04704f89c08" |
| notes.livedoor-6407997.source_URL | "http://news.livedoor.com/article/detail/6407997/" |
| notes.livedoor-6617204.weak | true |
| notes.livedoor-6617204.rationale | "人気記事TOP5を届けると述べるが、原段落にその記事や順位がなく、参照先だけを残す。" |
| notes.livedoor-6617204.canonical_sha256 | "c9dab6e2cea6b423aceae012d83ce188244e9f99aab3e28b072ae0a15bb41be8" |
| notes.livedoor-6617204.original_article_sha256 | "b48297e6f088957c7c9be1734212bafd0c46c052624bfe6172d51d8a44e61e4b" |
| notes.livedoor-6617204.source_URL | "http://news.livedoor.com/article/detail/6617204/" |
| notes.livedoor-6472183.weak | false |
| notes.livedoor-6472183.rationale | "番組、ゲストと中断、その反応という出来事を一文にまとめる。" |
| notes.livedoor-6472183.canonical_sha256 | "fd841ca44167fd1f535691df8ff038bba09497ca0aa45549717987e2af051cac" |
| notes.livedoor-6472183.original_article_sha256 | "4e5b456fff6292c8ed04c32a643376883ff8bc9abacba61c5cb5c3fad346b55e" |
| notes.livedoor-6472183.source_URL | "http://news.livedoor.com/article/detail/6472183/" |
| notes.livedoor-5749645.weak | false |
| notes.livedoor-5749645.rationale | "悪天候下の参加者の行動から、目当ての製品と催しの背景を説明する。" |
| notes.livedoor-5749645.canonical_sha256 | "0acdd6835d3e0a0a308ebea051c0679f6ac0e0884c257030cf5f47c92b7f540a" |
| notes.livedoor-5749645.original_article_sha256 | "786d9585ee237d26fdb017c77b6cb03db8e80fed6ccdfb677affbfee0836b9e5" |
| notes.livedoor-5749645.source_URL | "http://news.livedoor.com/article/detail/5749645/" |
| notes.livedoor-6642155.weak | false |
| notes.livedoor-6642155.rationale | "複数の映画の順位と動員・収益を列挙し、筆者の期待へつなげる週次の概要。" |
| notes.livedoor-6642155.canonical_sha256 | "b7fc53c992b3820cfe35a62cacb20867493389392542617ad2a19034f05aeed8" |
| notes.livedoor-6642155.original_article_sha256 | "5a9e8f551139f944c8765b5fdca6270188c900f6375faf12195ed2c6c406fd5f" |
| notes.livedoor-6642155.source_URL | "http://news.livedoor.com/article/detail/6642155/" |
| notes.livedoor-6635481.weak | false |
| notes.livedoor-6635481.rationale | "総選挙の上位の話題から、注目されていた別メンバーの結果へ人物関係をつなげる。" |
| notes.livedoor-6635481.canonical_sha256 | "65f9ecd47d644536f7e42d2bec8e38f96cddf3dd2afe129ff009541c9bfc736d" |
| notes.livedoor-6635481.original_article_sha256 | "ee53a2beaeb11a8b5459c85f3ff72dbc29bbdd4ee23702379574342093db82f3" |
| notes.livedoor-6635481.source_URL | "http://news.livedoor.com/article/detail/6635481/" |
| notes.livedoor-5436089.weak | false |
| notes.livedoor-5436089.rationale | "災害に伴う大会の中止を具体的に列挙し、連続四大会というまとめへつなげる。" |
| notes.livedoor-5436089.canonical_sha256 | "48d00db91669c69b7b3855ba864d0bd76cb95c6d09595b4151a0425f9a8e8155" |
| notes.livedoor-5436089.original_article_sha256 | "12afd36173f2e0ddd611937280056dfd4ef8c8df610b6846d1f680d7b5c949b8" |
| notes.livedoor-5436089.source_URL | "http://news.livedoor.com/article/detail/5436089/" |
| notes.livedoor-6180278.weak | false |
| notes.livedoor-6180278.rationale | "映画の題材、監督と制作規模を紹介し、その作品の試写会とゲストを述べる。" |
| notes.livedoor-6180278.canonical_sha256 | "249de3947abaf580d240b26d7030924101d4b1b7e4b516671e5362edf94da3ff" |
| notes.livedoor-6180278.original_article_sha256 | "afbb7a19c64c61938e771adc4099dbca4ddd5958f788a708d579dfb2ed07e324" |
| notes.livedoor-6180278.source_URL | "http://news.livedoor.com/article/detail/6180278/" |
| notes.livedoor-6438462.weak | false |
| notes.livedoor-6438462.rationale | "同期サービスの目的を説明し、筆者周辺での利用状況への問いを明示する。" |
| notes.livedoor-6438462.canonical_sha256 | "7eca3d45874a3d8d5f8d709a7603a90685f99fa79b7a721252a63b102739ef85" |
| notes.livedoor-6438462.original_article_sha256 | "4880a705c171d529187fba1785786b3f0b77c84a49296ec1c973a2acc79c15a6" |
| notes.livedoor-6438462.source_URL | "http://news.livedoor.com/article/detail/6438462/" |
| notes.livedoor-5625252.weak | false |
| notes.livedoor-5625252.rationale | "RSS閲覧という話題と利用サービスを示す記事導入。前回への言及はあるが今回扱う対象は明示される。" |
| notes.livedoor-5625252.canonical_sha256 | "efffc4e413e3577b79e79559c44ab7cccb143b03da9a2b580eac66bd0894305d" |
| notes.livedoor-5625252.original_article_sha256 | "182516de59551ffd9acf11565cd6b17e25f60f7a7f7deee060f5dbbb41031abf" |
| notes.livedoor-5625252.source_URL | "http://news.livedoor.com/article/detail/5625252/" |
| prepared_train_documents | 5050 |
| prepared_body_tokens | 523883 |
| prepared_stream_tokens | 533983 |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 0 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| limitations | "Single nonblind fixed64 sample is a readiness screen, not all5050 paragraph audit or Base quality evidence. Advertisements, dated facts and introductory rather than full-article closure remain. Old Web overlap/global audit incomplete." |

</details>

<details>
<summary>reports/phase6/livedoor-leads-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/livedoor-leads-20261006/job.json) ／ SHA256: `c72716fe9bd1a8a9fd2b20b92ac4c463989628b89e601662fa3e11a2be09b706` ／ 800 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_seconds | 0 |
| seconds | 3.8352022010076325 |

</details>

<details>
<summary>reports/phase6/livedoor-leads-20261006/ready.json — prepared_pending_fixed64_content_review</summary>

[原記録](../../reports/phase6/livedoor-leads-20261006/ready.json) ／ SHA256: `9a14662182da7ad80c87f0ae95467a891ff2b4e8bdb7aeb1a64db4de75001ef4` ／ 5,344 bytes

| 原キー | 保存値 |
|---|---|
| status | "prepared_pending_fixed64_content_review" |
| download_seconds | 2.4841441260068677 |
| CPU_seconds | 1.3498220820038114 |
| GPU_seconds | 0 |
| counts.accepted_leads | 5050 |
| counts.test_articles_not_decoded | 376 |
| counts.token_length_rejected | 108 |
| category_accepted_counts.dokujo-tsushin | 611 |
| category_accepted_counts.it-life-hack | 694 |
| category_accepted_counts.kaden-channel | 625 |
| category_accepted_counts.livedoor-homme | 330 |
| category_accepted_counts.movie-enter | 707 |
| category_accepted_counts.peachy | 646 |
| category_accepted_counts.smax | 16 |
| category_accepted_counts.sports-watch | 774 |
| category_accepted_counts.topic-news | 647 |
| splits.train.tokens | 533983 |
| splits.train.documents | 5050 |
| splits.train.body_bytes | 1950770 |
| splits.dev.tokens | 0 |
| splits.dev.documents | 0 |
| splits.dev.body_bytes | 0 |
| splits.test.tokens | 0 |
| splits.test.documents | 0 |
| splits.test.body_bytes | 0 |
| splits.test.stream_sha256 | "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" |
| splits.test.index_sha256 | "37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570" |
| distinct_prepared_body_tokens | 523883 |
| EOS_per_supervised_token | 0.00954752303221769 |
| sample.path | "/home/aihub_ubuntu/jmicro-data/phase6/livedoor-leads-20261006/sample64.json" |
| sample.sha256 | "15bb8043577705292c4a20ccb0400b6847179794d0d9c1e0c6c4913def9fa82a" |
| protected_test_used | false |
| quality_accepted | false |
| Base_complete | false |
| limitations | "Natural dated news paragraphs are not verified facts or everyday fiction. Repeated epochs are learning, not more distinct data. Possible overlap with old Web and benchmark ancestry remains incompletely audited; no claim of corpus-independent novelty." |

</details>

<details>
<summary>reports/phase6/livedoor_base_comparison_completion.json — livedoor_base_comparison_completion</summary>

[原記録](../../reports/phase6/livedoor_base_comparison_completion.json) ／ SHA256: `1dfb188b73d55296c3fa4c621ecc9ab3c78a2740526d697b748d535221a29cf9` ／ 687,698 bytes

| 原キー | 保存値 |
|---|---|
| status | "livedoor_base_comparison_completion" |
| actual_job.status | "complete" |
| actual_job.GPU_elapsed_seconds | 115.1166807099944 |
| actual_job.teachers | 25976793 |
| actual_job.teacher_budget | 26428122 |
| actual_job.loss | 2.35932993888855 |
| actual_job.source_teachers.web | 1428122 |
| actual_job.source_teachers.authored_news | 24548671 |
| scientific_GPU_seconds | 115.1166807099944 |
| verification_GPU_seconds | 29.754869525990216 |
| verification_teacher_tokens | 2603282 |
| observed_new_teacher_tokens | 26428122 |
| reused_prefix_teacher_tokens | 73571878 |
| Base_complete | false |
| Base_adopted | false |
| protected_test_used | false |
| original_UI.HTTP.training_tokens | 10000007168 |
| original_UI.HTTP.update | 305176 |
| original_UI.HTTP.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| original_UI.HTTP.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| original_UI.HTTP.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| actual_result.checkpoints.authored_news.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/livedoor-base-comparison-v2-20261006/authored_news/training/checkpoint-00323499.pt" |
| actual_result.checkpoints.authored_news.checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |
| actual_result.checkpoints.authored_news.binding.config_sha256 | "9e27df5b8ea2ba6aadb2e8fd1bc48f052a68b743ddd6f991a17ab89e64132d6e" |
| actual_result.checkpoints.authored_news.binding.arm | "authored_news" |
| actual_result.checkpoints.authored_news.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/source-order-condition-comparison-v2-20261006/source_order/training/checkpoint-00322685.pt" |
| actual_result.checkpoints.authored_news.binding.parent.sha256 | "1398ad1364d60e88382bca26e711e45b8b981275dc56d77fdae295674df297c7" |
| actual_result.checkpoints.authored_news.binding.original_parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/web/checkpoint-00320435.pt" |
| actual_result.checkpoints.authored_news.binding.original_parent.sha256 | "d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4" |
| actual_result.checkpoints.authored_news.binding.teacher_goals.web | 1428122 |
| actual_result.checkpoints.authored_news.binding.teacher_goals.authored_news | 25000000 |
| actual_result.checkpoints.authored_news.binding.study_kind | "authored_Japanese_news_vs_synthetic_native_Base100M_v1" |
| actual_result.checkpoints.authored_news.binding.optimizer_policy | "inherit_native" |
| actual_result.checkpoints.authored_news.binding.scientific | true |
| actual_result.checkpoints.authored_news.update | 323499 |
| actual_result.checkpoints.authored_news.tokens | 10600415232 |
| actual_result.checkpoints.authored_news.supervised_tokens | 10577786961 |
| actual_result.checkpoints.authored_news.additional_supervised_tokens | 26428122 |
| actual_result.checkpoints.authored_news.additional_input_tokens | 26673152 |
| actual_result.checkpoints.authored_news.source_teachers.web | 1428122 |
| actual_result.checkpoints.authored_news.source_teachers.authored_news | 25000000 |
| actual_result.checkpoints.authored_news.source_eos.web | 3064 |
| actual_result.checkpoints.authored_news.source_eos.authored_news | 238510 |
| actual_result.checkpoints.authored_news.source_input_tokens.web | 1434624 |
| actual_result.checkpoints.authored_news.source_input_tokens.authored_news | 25238528 |
| actual_result.checkpoints.authored_news.source_focus_teachers.web | 0 |
| actual_result.checkpoints.authored_news.source_focus_teachers.authored_news | 0 |
| actual_result.checkpoints.authored_news.focus_teacher_tokens | 0 |
| actual_result.checkpoints.authored_news.focus_token_digest | "179baab1310e5fefbd4b7a09268deaadddd0308d06e996169063717ac048e9b1" |
| actual_result.checkpoints.authored_news.weighted_teacher_mass | 26428122 |
| actual_result.checkpoints.authored_news.outcome_weight | 1 |
| actual_result.checkpoints.authored_news.training_seconds | 45.90560058527626 |
| actual_result.checkpoints.authored_news.completed_at | "2026-10-06T14:29:11.203754Z" |
| actual_result.checkpoints.authored_news.sampler.kind | "exact_staged_Web_then_authored_news_quota_v1" |
| actual_result.checkpoints.authored_news.sampler.goals.web | 1428122 |
| actual_result.checkpoints.authored_news.sampler.goals.authored_news | 25000000 |
| actual_result.checkpoints.authored_news.sampler.source_order | ["web", "authored_news"] |
| actual_result.checkpoints.authored_news.sampler.context | 1024 |
| actual_result.checkpoints.authored_news.sampler.seed | 42 |
| actual_result.checkpoints.authored_news.sampler.position | 814 |
| actual_result.checkpoints.authored_news.sampler.source_teachers.web | 1428122 |
| actual_result.checkpoints.authored_news.sampler.source_teachers.authored_news | 25000000 |
| actual_result.checkpoints.authored_news.sampler.source_eos.web | 3064 |
| actual_result.checkpoints.authored_news.sampler.source_eos.authored_news | 238510 |
| actual_result.checkpoints.authored_news.sampler.source_tokens.web | 1434624 |
| actual_result.checkpoints.authored_news.sampler.source_tokens.authored_news | 25238528 |
| actual_result.checkpoints.authored_news.sampler.source_body_bytes.web | 5562565 |
| actual_result.checkpoints.authored_news.sampler.source_body_bytes.authored_news | 92210860 |
| actual_result.checkpoints.authored_news.sampler.source_focus_teachers.web | 0 |
| actual_result.checkpoints.authored_news.sampler.source_focus_teachers.authored_news | 0 |
| actual_result.checkpoints.authored_news.sampler.streams.web.kind | "actual-parent-Web-block-cursor-v1" |
| actual_result.checkpoints.authored_news.sampler.streams.web.manifest_sha256 | "2edfd35bf077cd1aa583713c01341c0db52f39adc5701f30ede0aacae840b2de" |
| actual_result.checkpoints.authored_news.sampler.streams.web.sampler.seed | 42 |
| actual_result.checkpoints.authored_news.sampler.streams.web.sampler.epoch | 0 |
| actual_result.checkpoints.authored_news.sampler.streams.web.sampler.position | 10327321 |
| actual_result.checkpoints.authored_news.sampler.streams.web.sampler.context | 1024 |
| actual_result.checkpoints.authored_news.sampler.streams.web.sampler.blocks | 11939276 |
| actual_result.checkpoints.authored_news.sampler.streams.authored_news.kind | "fresh_authored_news_contiguous_block_shuffle_v1" |
| actual_result.checkpoints.authored_news.sampler.streams.authored_news.manifest_sha256 | "600d8e04e0ea266aef6d7180b6e95639f7260e910dc6a55b7a6ae7eeb7c38bfa" |
| actual_result.checkpoints.authored_news.sampler.streams.authored_news.sampler.seed | 42 |
| actual_result.checkpoints.authored_news.sampler.streams.authored_news.sampler.epoch | 47 |
| actual_result.checkpoints.authored_news.sampler.streams.authored_news.sampler.position | 160 |
| actual_result.checkpoints.authored_news.sampler.streams.authored_news.sampler.context | 1024 |
| actual_result.checkpoints.authored_news.sampler.streams.authored_news.sampler.blocks | 521 |
| actual_result.checkpoints.authored_news.source_body_bytes.web | 5562565 |
| actual_result.checkpoints.authored_news.source_body_bytes.authored_news | 92210860 |
| actual_result.checkpoints.authored_news.token_digest | "7a1d151a6be3cc79ca9143fa703e0ef02e89c203eb91b734e6418bce13ece3f9" |
| actual_result.checkpoints.authored_news.model_config.schema_version | 1 |
| actual_result.checkpoints.authored_news.model_config.architecture | "decoder_only_transformer" |
| actual_result.checkpoints.authored_news.model_config.hidden_size | 256 |
| actual_result.checkpoints.authored_news.model_config.num_attention_heads | 4 |
| actual_result.checkpoints.authored_news.model_config.num_key_value_heads | 2 |
| actual_result.checkpoints.authored_news.model_config.head_dim | 64 |
| actual_result.checkpoints.authored_news.model_config.activation | "swiglu" |
| actual_result.checkpoints.authored_news.model_config.norm | "rmsnorm" |
| actual_result.checkpoints.authored_news.model_config.rms_norm_eps | 1e-06 |
| actual_result.checkpoints.authored_news.model_config.qk_norm_type | "none" |
| actual_result.checkpoints.authored_news.model_config.qk_norm_before_rope | true |
| actual_result.checkpoints.authored_news.model_config.attention_scale | 0.125 |
| actual_result.checkpoints.authored_news.model_config.rope_theta | 10000 |
| actual_result.checkpoints.authored_news.model_config.rope_layout | "half_split" |
| actual_result.checkpoints.authored_news.model_config.rotary_dim | 64 |
| actual_result.checkpoints.authored_news.model_config.max_position_embeddings | 1024 |
| actual_result.checkpoints.authored_news.model_config.tie_word_embeddings | true |
| actual_result.checkpoints.authored_news.model_config.attention_bias | false |
| actual_result.checkpoints.authored_news.model_config.mlp_bias | false |
| actual_result.checkpoints.authored_news.model_config.dropout | 0.0 |
| actual_result.checkpoints.authored_news.model_config.initializer_std | 0.02 |
| actual_result.checkpoints.authored_news.model_config.norm_initial_gain | 1.0 |
| actual_result.checkpoints.authored_news.model_config.status | "phase5_ablation" |
| actual_result.checkpoints.authored_news.model_config.name | "JMicro-10M-T4K-NoQKNorm" |
| actual_result.checkpoints.authored_news.model_config.vocab_size | 4096 |
| actual_result.checkpoints.authored_news.model_config.num_hidden_layers | 13 |
| actual_result.checkpoints.authored_news.model_config.intermediate_size | 640 |
| actual_result.checkpoints.authored_news.model_config.expected_parameter_count | 10001152 |
| actual_result.checkpoints.authored_news.unique_parameters | 10001152 |
| actual_result.checkpoints.authored_news.reused_prefix_teacher_tokens | 73571878 |
| actual_result.checkpoints.authored_news.total_teacher_tokens_from_original_parent | 100000000 |
| actual_result.checkpoints.authored_news.pure_Web_continuation_matched_updates | 43 |
| actual_result.evaluations.authored_news.binding.teacher_goals.web | 1428122 |
| actual_result.evaluations.authored_news.binding.teacher_goals.authored_news | 25000000 |
| actual_result.evaluations.authored_news.binding.scientific | true |
| actual_result.evaluations.authored_news.checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |
| actual_result.evaluations.authored_news.body.documents | 256 |
| actual_result.evaluations.authored_news.body.limit_documents | 256 |
| actual_result.evaluations.authored_news.body.body_nll | 334242.09346342087 |
| actual_result.evaluations.authored_news.body.eos_nll | 314.84866300038993 |
| actual_result.evaluations.authored_news.body.body_bytes | 472055 |
| actual_result.evaluations.authored_news.body.body_tokens | 122343 |
| actual_result.evaluations.authored_news.body.bpb | 1.0215110753959236 |
| actual_result.evaluations.authored_news.body.seconds | 1.6565144920023158 |
| actual_result.evaluations.authored_news.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| actual_result.evaluations.authored_news.generation.max_new_tokens | 64 |
| actual_result.evaluations.authored_news.greedy_rates.eos | 49 |
| actual_result.evaluations.authored_news.greedy_rates.repetition | 24 |
| actual_result.evaluations.authored_news.greedy_rates.unicode_failure | 0 |
| actual_result.evaluations.authored_news.greedy_rates.role_leak | 0 |
| actual_result.evaluations.authored_news.greedy_rates.empty | 0 |
| actual_result.evaluations.authored_news.diagnostics.semantics.primary.accuracy.point | 0.59375 |
| actual_result.evaluations.authored_news.diagnostics.semantics.primary.accuracy.ci95 | [0.5520833333333334, 0.640625] |
| actual_result.evaluations.authored_news.diagnostics.semantics.primary.accuracy.units | 96 |
| actual_result.evaluations.authored_news.diagnostics.semantics.primary.accuracy.examples | 192 |
| actual_result.evaluations.authored_news.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.authored_news.diagnostics.semantics.primary.accuracy.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.semantics.primary.hard_accuracy | 0.59375 |
| actual_result.evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5885416666666666 |
| actual_result.evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.546875, 0.6354166666666666] |
| actual_result.evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| actual_result.evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| actual_result.evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.semantics.per_token_secondary.count | 192 |
| actual_result.evaluations.authored_news.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5885416666666666 |
| actual_result.evaluations.authored_news.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5884411884411884 |
| actual_result.evaluations.authored_news.diagnostics.semantics.per_token_secondary.mcc | 0.17716986318620467 |
| actual_result.evaluations.authored_news.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| actual_result.evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| actual_result.evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| actual_result.evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| actual_result.evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| actual_result.evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| actual_result.evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| actual_result.evaluations.authored_news.diagnostics.semantics.train_majority_accuracy | 0.5 |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.negation.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.negation.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.quantity.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.time.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.time.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.comparison.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.coreference.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.causality.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.causality.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.primary.accuracy.point | 0.770392749244713 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.primary.accuracy.ci95 | [0.7250755287009063, 0.8187311178247734] |
| actual_result.evaluations.authored_news.diagnostics.jblimp.primary.accuracy.units | 331 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.primary.accuracy.examples | 331 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.primary.accuracy.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.primary.hard_accuracy | 0.770392749244713 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.716012084592145 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6676737160120846, 0.7673716012084593] |
| actual_result.evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.per_token_secondary.count | 331 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.716012084592145 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.41725352112676056 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| actual_result.evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.train_majority_accuracy | null |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.island effects.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.binding.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.argument structure.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.morphology.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.control/raising.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| actual_result.evaluations.authored_news.diagnostics.jblimp.raw_pair_accuracy | 0.7673716012084593 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.primary.accuracy.point | 0.37890974084003576 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.primary.accuracy.ci95 | [0.3512064343163539, 0.4075067024128686] |
| actual_result.evaluations.authored_news.diagnostics.jcqa.primary.accuracy.units | 1119 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.authored_news.diagnostics.jcqa.primary.accuracy.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jcqa.primary.hard_accuracy | 0.37890974084003576 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3418230563002681 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.31500223413762285, 0.36907953529937443] |
| actual_result.evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| actual_result.evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jcqa.per_token_secondary.count | 1119 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.34137622877569257 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.34100536204466153 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.per_token_secondary.mcc | 0.17689830849780755 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| actual_result.evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| actual_result.evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| actual_result.evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.categories.commonsense.seed | 42 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| actual_result.evaluations.authored_news.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| actual_result.evaluations.authored_news.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| actual_result.evaluations.authored_news.diagnostics.semantic_both_contexts.correct | 20 |
| actual_result.evaluations.authored_news.memory.maximum_observed_allocated_bytes | 275218432 |
| actual_result.evaluations.authored_news.memory.maximum_observed_reserved_bytes | 13289652224 |
| actual_result.evaluations.authored_news.protected_test_used | false |
| actual_result.transfer.authored_news.checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |
| actual_result.transfer.authored_news.checks.weights_unchanged | true |
| actual_result.transfer.authored_news.checks.no_gradients | true |
| actual_result.transfer.authored_news.checks.eval_mode | true |
| actual_result.transfer.authored_news.checks.RNG_restored | true |
| actual_result.transfer.authored_news.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5859375 |
| actual_result.transfer.authored_news.summary.aggregate.sum_log_likelihood.all128.both_correct | 27 |
| actual_result.transfer.authored_news.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.6328125 |
| actual_result.transfer.authored_news.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 22 |
| actual_result.transfer.authored_news.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| actual_result.transfer.authored_news.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 5 |
| actual_result.transfer.authored_news.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| actual_result.transfer.authored_news.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.61328125 |
| actual_result.transfer.authored_news.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 30 |
| actual_result.transfer.authored_news.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 97 |
| actual_result.transfer.authored_news.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 105 |
| actual_result.transfer.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| actual_result.transfer.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6796875 |
| actual_result.transfer.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 24 |
| actual_result.transfer.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 39 |
| actual_result.transfer.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 51 |
| actual_result.transfer.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| actual_result.transfer.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.546875 |
| actual_result.transfer.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 6 |
| actual_result.transfer.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 58 |
| actual_result.transfer.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 54 |
| actual_result.transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| actual_result.transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.58203125 |
| actual_result.transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 22 |
| actual_result.transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 105 |
| actual_result.transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 105 |
| actual_result.transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| actual_result.transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.625 |
| actual_result.transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 17 |
| actual_result.transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 46 |
| actual_result.transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 51 |
| actual_result.transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| actual_result.transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.5390625 |
| actual_result.transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 5 |
| actual_result.transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 59 |
| actual_result.transfer.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 54 |
| actual_result.transfer.authored_news.optimizer_updates | 0 |
| actual_result.transfer.authored_news.scientific_teacher_tokens | 0 |
| actual_result.transfer.authored_news.protected_test_used | false |
| actual_result.transfer.authored_news.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| actual_result.retention.authored_news.checkpoint_sha256 | "403f8155276c0566cd4e98c24ba1433d9412ed6973056adf35bfb8377bd4d375" |
| actual_result.retention.authored_news.checks.weights_unchanged | true |
| actual_result.retention.authored_news.checks.no_gradients | true |
| actual_result.retention.authored_news.checks.eval_mode | true |
| actual_result.retention.authored_news.checks.RNG_restored | true |
| actual_result.retention.authored_news.summary.aggregate.sum_log_likelihood.all128.accuracy | 0.5703125 |
| actual_result.retention.authored_news.summary.aggregate.sum_log_likelihood.all128.both_correct | 24 |
| actual_result.retention.authored_news.summary.aggregate.sum_log_likelihood.lexical_holdout.accuracy | 0.625 |
| actual_result.retention.authored_news.summary.aggregate.sum_log_likelihood.lexical_holdout.both_correct | 17 |
| actual_result.retention.authored_news.summary.aggregate.sum_log_likelihood.structural_holdout.accuracy | 0.515625 |
| actual_result.retention.authored_news.summary.aggregate.sum_log_likelihood.structural_holdout.both_correct | 7 |
| actual_result.retention.authored_news.summary.aggregate.mean_token_log_likelihood.all128.families | 128 |
| actual_result.retention.authored_news.summary.aggregate.mean_token_log_likelihood.all128.accuracy | 0.5625 |
| actual_result.retention.authored_news.summary.aggregate.mean_token_log_likelihood.all128.both_correct | 19 |
| actual_result.retention.authored_news.summary.aggregate.mean_token_log_likelihood.all128.same_unique_candidate | 106 |
| actual_result.retention.authored_news.summary.aggregate.mean_token_log_likelihood.all128.aligned_context_margin_shift | 78 |
| actual_result.retention.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.families | 64 |
| actual_result.retention.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.accuracy | 0.6015625 |
| actual_result.retention.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.both_correct | 13 |
| actual_result.retention.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.same_unique_candidate | 51 |
| actual_result.retention.authored_news.summary.aggregate.mean_token_log_likelihood.lexical_holdout.aligned_context_margin_shift | 44 |
| actual_result.retention.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.families | 64 |
| actual_result.retention.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.accuracy | 0.5234375 |
| actual_result.retention.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.both_correct | 6 |
| actual_result.retention.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.same_unique_candidate | 55 |
| actual_result.retention.authored_news.summary.aggregate.mean_token_log_likelihood.structural_holdout.aligned_context_margin_shift | 34 |
| actual_result.retention.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.families | 128 |
| actual_result.retention.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.accuracy | 0.515625 |
| actual_result.retention.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.both_correct | 10 |
| actual_result.retention.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.same_unique_candidate | 112 |
| actual_result.retention.authored_news.summary.aggregate.mean_byte_log_likelihood.all128.aligned_context_margin_shift | 80 |
| actual_result.retention.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.families | 64 |
| actual_result.retention.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.accuracy | 0.5703125 |
| actual_result.retention.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.both_correct | 9 |
| actual_result.retention.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.same_unique_candidate | 55 |
| actual_result.retention.authored_news.summary.aggregate.mean_byte_log_likelihood.lexical_holdout.aligned_context_margin_shift | 43 |
| actual_result.retention.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.families | 64 |
| actual_result.retention.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.accuracy | 0.4609375 |
| actual_result.retention.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.both_correct | 1 |
| actual_result.retention.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.same_unique_candidate | 57 |
| actual_result.retention.authored_news.summary.aggregate.mean_byte_log_likelihood.structural_holdout.aligned_context_margin_shift | 37 |
| actual_result.retention.authored_news.optimizer_updates | 0 |
| actual_result.retention.authored_news.scientific_teacher_tokens | 0 |
| actual_result.retention.authored_news.protected_test_used | false |
| actual_result.retention.authored_news.limitations | "Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement." |
| actual_result.status | "news100M_GPU_complete_pending_all80_content" |
| actual_result.GPU_seconds | 115.1166807099944 |
| actual_result.scientific_teacher_tokens | 26428122 |
| actual_result.reused_prefix_teacher_tokens | 73571878 |
| actual_result.total_teacher_tokens_from_original_parent | 100000000 |
| actual_result.exact_same_scientific_sources_as_control | false |
| actual_result.Base_complete | false |
| actual_result.Base_adopted | false |
| actual_result.protected_test_used | false |
| total_new_GPU_seconds | 144.8715502359846 |
| actual_review.status | "news100M_all80_content_and_native_state_reviewed" |
| actual_review.summaries.authored_news.BPB | 1.0215110753959236 |
| actual_review.summaries.authored_news.rates.eos | 49 |
| actual_review.summaries.authored_news.rates.repetition | 24 |
| actual_review.summaries.authored_news.rates.unicode_failure | 0 |
| actual_review.summaries.authored_news.rates.role_leak | 0 |
| actual_review.summaries.authored_news.rates.empty | 0 |
| actual_review.summaries.authored_news.grammar2 | 45 |
| actual_review.summaries.authored_news.relevance2 | 46 |
| actual_review.summaries.authored_news.coherent | 17 |
| actual_review.summaries.authored_news.appropriate | 18 |
| actual_review.summaries.authored_news.notes_sha256 | "9f338300b1275a5bbdacef5c9082a26c2f7b0522cf497b2c3939354aa62e199b" |
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
| actual_review.quality_comparison.checks.coherence_gain_at_least8 | false |
| actual_review.quality_comparison.checks.paired_CI_lower_above0 | false |
| actual_review.quality_comparison.checks.EOS_nonworsening | false |
| actual_review.quality_comparison.checks.repetition_nonworsening | false |
| actual_review.quality_comparison.checks.no_empty_role_unicode | true |
| actual_review.quality_comparison.checks.BPB_gate | true |
| actual_review.quality_comparison.checks.appropriate_completion_not_punctuation | true |
| actual_review.quality_comparison.passed | false |
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
| actual_review.accounting.completed_updates | 814 |
| actual_review.accounting.new_teacher_tokens | 26428122 |
| actual_review.accounting.physical_input_positions | 26673152 |
| actual_review.accounting.source_teachers.web | 1428122 |
| actual_review.accounting.source_teachers.authored_news | 25000000 |
| actual_review.accounting.source_EOS.web | 3064 |
| actual_review.accounting.source_EOS.authored_news | 238510 |
| actual_review.pure_Web_continuation_matched_updates | 43 |
| actual_review.new_scientific_teacher_tokens | 26428122 |
| actual_review.reused_prefix_teacher_tokens | 73571878 |
| actual_review.total_teacher_tokens_from_original_parent | 100000000 |
| actual_review.verification_teacher_tokens | 2603282 |
| actual_review.new_total_GPU_seconds | 144.8715502359846 |
| actual_review.Base_complete | false |
| actual_review.Base_adopted | false |
| actual_review.protected_test_used | false |
| actual_review.limitations | "Authored-news source/EOS/diversity replace synthetic post-Web25M; teacher counts match but inputs/updates do not. 523883 local body tokens, about47.265 repeated exposures, old Web overlap/global audit incomplete. One learned seed/nonblind repeated dev." |
| eligible_for_final_Base_validation | false |
| notes.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/livedoor-base-comparison-v2-20261006/content-notes.json" |
| notes.sha256 | "9f338300b1275a5bbdacef5c9082a26c2f7b0522cf497b2c3939354aa62e199b" |

</details>
