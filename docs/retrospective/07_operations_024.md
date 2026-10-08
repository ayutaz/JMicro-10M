# 実行管理・後続準備・その他 — 24/26

[分野一覧へ](07_operations.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/root_cause_summary.json — diagnostic_scope_complete_quality_unmet</summary>

[原記録](../../reports/phase6/root_cause_summary.json) ／ SHA256: `3a6d99e31360d310ba702ddfc95828ca27ecd11b2645b237c157a1366385d9b3` ／ 112,812 bytes

| 原キー | 保存値 |
|---|---|
| status | "diagnostic_scope_complete_quality_unmet" |
| models.original.training_tokens | 10000007168 |
| models.original.update | 305176 |
| models.original.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| models.original.checkpoint.sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| models.original.groups.web.teacher_eos_arithmetic_mean | 0.1452356082663755 |
| models.original.groups.web.teacher_eos_median_rank | 2.0 |
| models.original.groups.web.teacher_eos_top1 | 1 |
| models.original.groups.web.teacher_top1_mean | 0.423789482313616 |
| models.original.groups.web.fp32_teacher_eos_top1 | 1 |
| models.original.groups.web.bf16_full_cache_eos_rank_changes | 0 |
| models.original.groups.web.generation.greedy.eos | 0 |
| models.original.groups.web.generation.greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.original.groups.web.generation.sampling-42.eos | 0 |
| models.original.groups.web.generation.sampling-42.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.original.groups.web.generation.sampling-43.eos | 0 |
| models.original.groups.web.generation.sampling-43.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.original.groups.web.generation.sampling-44.eos | 1 |
| models.original.groups.web.generation.sampling-44.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.original.groups.web.fp32_greedy.eos | 0 |
| models.original.groups.web.fp32_greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.original.groups.story200m.teacher_eos_arithmetic_mean | 0.04269940895028412 |
| models.original.groups.story200m.teacher_eos_median_rank | 2.0 |
| models.original.groups.story200m.teacher_eos_top1 | 0 |
| models.original.groups.story200m.teacher_top1_mean | 0.4127546257793797 |
| models.original.groups.story200m.fp32_teacher_eos_top1 | 0 |
| models.original.groups.story200m.bf16_full_cache_eos_rank_changes | 0 |
| models.original.groups.story200m.generation.greedy.eos | 0 |
| models.original.groups.story200m.generation.greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.original.groups.story200m.generation.sampling-42.eos | 0 |
| models.original.groups.story200m.generation.sampling-42.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.original.groups.story200m.generation.sampling-43.eos | 0 |
| models.original.groups.story200m.generation.sampling-43.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.original.groups.story200m.generation.sampling-44.eos | 2 |
| models.original.groups.story200m.generation.sampling-44.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.original.groups.story200m.fp32_greedy.eos | 0 |
| models.original.groups.story200m.fp32_greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.original.groups.compact.teacher_eos_arithmetic_mean | 0.00490213098237291 |
| models.original.groups.compact.teacher_eos_median_rank | 34.0 |
| models.original.groups.compact.teacher_eos_top1 | 0 |
| models.original.groups.compact.teacher_top1_mean | 0.28212256493506493 |
| models.original.groups.compact.fp32_teacher_eos_top1 | 0 |
| models.original.groups.compact.bf16_full_cache_eos_rank_changes | 4 |
| models.original.groups.compact.generation.greedy.eos | 0 |
| models.original.groups.compact.generation.greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.original.groups.compact.generation.sampling-42.eos | 0 |
| models.original.groups.compact.generation.sampling-42.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.original.groups.compact.generation.sampling-43.eos | 1 |
| models.original.groups.compact.generation.sampling-43.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.original.groups.compact.generation.sampling-44.eos | 0 |
| models.original.groups.compact.generation.sampling-44.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.original.groups.compact.fp32_greedy.eos | 0 |
| models.original.groups.compact.fp32_greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.original.max_teacher_mean_nll_delta | 0.024790287017822266 |
| models.original.fp32_bf16_teacher_eos_top1_changes | 0 |
| models.mixed.training_tokens | 10100572160 |
| models.mixed.update | 308245 |
| models.mixed.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/packing-study-20261005/mixed-candidate/checkpoint-00308245.pt" |
| models.mixed.checkpoint.sha256 | "5d7df8eec30eaaf3799f2cc1c494c733747e0f0a98563941cef0cbd3353a9ab1" |
| models.mixed.groups.web.teacher_eos_arithmetic_mean | 0.13852185039468168 |
| models.mixed.groups.web.teacher_eos_median_rank | 2.0 |
| models.mixed.groups.web.teacher_eos_top1 | 0 |
| models.mixed.groups.web.teacher_top1_mean | 0.43243188158101525 |
| models.mixed.groups.web.fp32_teacher_eos_top1 | 0 |
| models.mixed.groups.web.bf16_full_cache_eos_rank_changes | 1 |
| models.mixed.groups.web.generation.greedy.eos | 0 |
| models.mixed.groups.web.generation.greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.mixed.groups.web.generation.sampling-42.eos | 0 |
| models.mixed.groups.web.generation.sampling-42.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.mixed.groups.web.generation.sampling-43.eos | 2 |
| models.mixed.groups.web.generation.sampling-43.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.mixed.groups.web.generation.sampling-44.eos | 1 |
| models.mixed.groups.web.generation.sampling-44.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.mixed.groups.web.fp32_greedy.eos | 0 |
| models.mixed.groups.web.fp32_greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.mixed.groups.story200m.teacher_eos_arithmetic_mean | 0.058214526157826185 |
| models.mixed.groups.story200m.teacher_eos_median_rank | 2.0 |
| models.mixed.groups.story200m.teacher_eos_top1 | 0 |
| models.mixed.groups.story200m.teacher_top1_mean | 0.40460576417126515 |
| models.mixed.groups.story200m.fp32_teacher_eos_top1 | 0 |
| models.mixed.groups.story200m.bf16_full_cache_eos_rank_changes | 0 |
| models.mixed.groups.story200m.generation.greedy.eos | 0 |
| models.mixed.groups.story200m.generation.greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.mixed.groups.story200m.generation.sampling-42.eos | 1 |
| models.mixed.groups.story200m.generation.sampling-42.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.mixed.groups.story200m.generation.sampling-43.eos | 0 |
| models.mixed.groups.story200m.generation.sampling-43.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.mixed.groups.story200m.generation.sampling-44.eos | 0 |
| models.mixed.groups.story200m.generation.sampling-44.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.mixed.groups.story200m.fp32_greedy.eos | 0 |
| models.mixed.groups.story200m.fp32_greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.mixed.groups.compact.teacher_eos_arithmetic_mean | 0.9998903460800648 |
| models.mixed.groups.compact.teacher_eos_median_rank | 1.0 |
| models.mixed.groups.compact.teacher_eos_top1 | 16 |
| models.mixed.groups.compact.teacher_top1_mean | 1.0 |
| models.mixed.groups.compact.fp32_teacher_eos_top1 | 16 |
| models.mixed.groups.compact.bf16_full_cache_eos_rank_changes | 0 |
| models.mixed.groups.compact.generation.greedy.eos | 16 |
| models.mixed.groups.compact.generation.greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.mixed.groups.compact.generation.sampling-42.eos | 16 |
| models.mixed.groups.compact.generation.sampling-42.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.mixed.groups.compact.generation.sampling-43.eos | 16 |
| models.mixed.groups.compact.generation.sampling-43.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.mixed.groups.compact.generation.sampling-44.eos | 16 |
| models.mixed.groups.compact.generation.sampling-44.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.mixed.groups.compact.fp32_greedy.eos | 16 |
| models.mixed.groups.compact.fp32_greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.mixed.max_teacher_mean_nll_delta | 0.007064342498779297 |
| models.mixed.fp32_bf16_teacher_eos_top1_changes | 0 |
| models.story.training_tokens | 10500014080 |
| models.story.update | 320435 |
| models.story.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story20-low-lr-10b-500m-20261005/coherent20/checkpoint-00320435.pt" |
| models.story.checkpoint.sha256 | "f336806bee562cf11fe29506f833deae45de228c4b8acb1b942c7df21c82daac" |
| models.story.groups.web.teacher_eos_arithmetic_mean | 0.16142011590818583 |
| models.story.groups.web.teacher_eos_median_rank | 2.0 |
| models.story.groups.web.teacher_eos_top1 | 2 |
| models.story.groups.web.teacher_top1_mean | 0.43962434189847555 |
| models.story.groups.web.fp32_teacher_eos_top1 | 2 |
| models.story.groups.web.bf16_full_cache_eos_rank_changes | 1 |
| models.story.groups.web.generation.greedy.eos | 0 |
| models.story.groups.web.generation.greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.story.groups.web.generation.sampling-42.eos | 0 |
| models.story.groups.web.generation.sampling-42.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.story.groups.web.generation.sampling-43.eos | 0 |
| models.story.groups.web.generation.sampling-43.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.story.groups.web.generation.sampling-44.eos | 2 |
| models.story.groups.web.generation.sampling-44.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.story.groups.web.fp32_greedy.eos | 0 |
| models.story.groups.web.fp32_greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.story.groups.story200m.teacher_eos_arithmetic_mean | 0.814004048705101 |
| models.story.groups.story200m.teacher_eos_median_rank | 1.0 |
| models.story.groups.story200m.teacher_eos_top1 | 8 |
| models.story.groups.story200m.teacher_top1_mean | 0.624786431990619 |
| models.story.groups.story200m.fp32_teacher_eos_top1 | 8 |
| models.story.groups.story200m.bf16_full_cache_eos_rank_changes | 0 |
| models.story.groups.story200m.generation.greedy.eos | 8 |
| models.story.groups.story200m.generation.greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.story.groups.story200m.generation.sampling-42.eos | 6 |
| models.story.groups.story200m.generation.sampling-42.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.story.groups.story200m.generation.sampling-43.eos | 7 |
| models.story.groups.story200m.generation.sampling-43.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.story.groups.story200m.generation.sampling-44.eos | 6 |
| models.story.groups.story200m.generation.sampling-44.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.story.groups.story200m.fp32_greedy.eos | 8 |
| models.story.groups.story200m.fp32_greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.story.groups.compact.teacher_eos_arithmetic_mean | 0.01987144787563011 |
| models.story.groups.compact.teacher_eos_median_rank | 15.0 |
| models.story.groups.compact.teacher_eos_top1 | 0 |
| models.story.groups.compact.teacher_top1_mean | 0.2577448593073593 |
| models.story.groups.compact.fp32_teacher_eos_top1 | 0 |
| models.story.groups.compact.bf16_full_cache_eos_rank_changes | 0 |
| models.story.groups.compact.generation.greedy.eos | 5 |
| models.story.groups.compact.generation.greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.story.groups.compact.generation.sampling-42.eos | 7 |
| models.story.groups.compact.generation.sampling-42.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.story.groups.compact.generation.sampling-43.eos | 5 |
| models.story.groups.compact.generation.sampling-43.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.story.groups.compact.generation.sampling-44.eos | 4 |
| models.story.groups.compact.generation.sampling-44.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.story.groups.compact.fp32_greedy.eos | 5 |
| models.story.groups.compact.fp32_greedy.interpretation | "4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate" |
| models.story.max_teacher_mean_nll_delta | 0.011888504028320312 |
| models.story.fp32_bf16_teacher_eos_top1_changes | 0 |
| numeric_failed_checks.all32_bf16_math_vs_fp32.passed | false |
| numeric_failed_checks.all32_bf16_math_vs_fp32.finite | true |
| numeric_failed_checks.all32_bf16_math_vs_fp32.max_abs | 0.35198307037353516 |
| numeric_failed_checks.all32_bf16_math_vs_fp32.mean_abs | 0.015557014383375645 |
| numeric_failed_checks.all32_bf16_math_vs_fp32.outside_tolerance | 36584 |
| numeric_failed_checks.all32_bf16_math_vs_fp32.elements | 8495104 |
| numeric_failed_checks.all32_bf16_math_vs_fp32.tolerance.atol | 0.05 |
| numeric_failed_checks.all32_bf16_math_vs_fp32.tolerance.rtol | 0.02 |
| numeric_failed_checks.all32_padding.passed | false |
| numeric_failed_checks.all32_padding.finite | true |
| numeric_failed_checks.all32_padding.max_abs | 2.956390380859375e-05 |
| numeric_failed_checks.all32_padding.mean_abs | 1.6373654716517194e-06 |
| numeric_failed_checks.all32_padding.outside_tolerance | 1 |
| numeric_failed_checks.all32_padding.elements | 8495104 |
| numeric_failed_checks.all32_padding.tolerance.atol | 1e-05 |
| numeric_failed_checks.all32_padding.tolerance.rtol | 0.0001 |
| numeric_failed_checks.64_bf16_vs_fp32.passed | false |
| numeric_failed_checks.64_bf16_vs_fp32.finite | true |
| numeric_failed_checks.64_bf16_vs_fp32.max_abs | 0.2564353942871094 |
| numeric_failed_checks.64_bf16_vs_fp32.mean_abs | 0.014915302395820618 |
| numeric_failed_checks.64_bf16_vs_fp32.outside_tolerance | 274 |
| numeric_failed_checks.64_bf16_vs_fp32.elements | 262144 |
| numeric_failed_checks.64_bf16_vs_fp32.tolerance.atol | 0.05 |
| numeric_failed_checks.64_bf16_vs_fp32.tolerance.rtol | 0.02 |
| numeric_failed_checks.64_bf16_flash_vs_math.passed | false |
| numeric_failed_checks.64_bf16_flash_vs_math.finite | true |
| numeric_failed_checks.64_bf16_flash_vs_math.max_abs | 0.125 |
| numeric_failed_checks.64_bf16_flash_vs_math.mean_abs | 0.013879144564270973 |
| numeric_failed_checks.64_bf16_flash_vs_math.outside_tolerance | 355 |
| numeric_failed_checks.64_bf16_flash_vs_math.elements | 262144 |
| numeric_failed_checks.64_bf16_flash_vs_math.tolerance.atol | 0.05 |
| numeric_failed_checks.64_bf16_flash_vs_math.tolerance.rtol | 0.02 |
| numeric_failed_checks.1024_bf16_vs_fp32.passed | false |
| numeric_failed_checks.1024_bf16_vs_fp32.finite | true |
| numeric_failed_checks.1024_bf16_vs_fp32.max_abs | 0.35196590423583984 |
| numeric_failed_checks.1024_bf16_vs_fp32.mean_abs | 0.015793826431035995 |
| numeric_failed_checks.1024_bf16_vs_fp32.outside_tolerance | 4599 |
| numeric_failed_checks.1024_bf16_vs_fp32.elements | 4194304 |
| numeric_failed_checks.1024_bf16_vs_fp32.tolerance.atol | 0.05 |
| numeric_failed_checks.1024_bf16_vs_fp32.tolerance.rtol | 0.02 |
| numeric_failed_checks.1024_bf16_flash_vs_math.passed | false |
| numeric_failed_checks.1024_bf16_flash_vs_math.finite | true |
| numeric_failed_checks.1024_bf16_flash_vs_math.max_abs | 0.1875 |
| numeric_failed_checks.1024_bf16_flash_vs_math.mean_abs | 0.012907428666949272 |
| numeric_failed_checks.1024_bf16_flash_vs_math.outside_tolerance | 1712 |
| numeric_failed_checks.1024_bf16_flash_vs_math.elements | 4194304 |
| numeric_failed_checks.1024_bf16_flash_vs_math.tolerance.atol | 0.05 |
| numeric_failed_checks.1024_bf16_flash_vs_math.tolerance.rtol | 0.02 |
| numeric_failed_checks.1024_compiled_flash_logits.passed | false |
| numeric_failed_checks.1024_compiled_flash_logits.finite | true |
| numeric_failed_checks.1024_compiled_flash_logits.max_abs | 0.28125 |
| numeric_failed_checks.1024_compiled_flash_logits.mean_abs | 0.015573541633784771 |
| numeric_failed_checks.1024_compiled_flash_logits.outside_tolerance | 7091 |
| numeric_failed_checks.1024_compiled_flash_logits.elements | 4194304 |
| numeric_failed_checks.1024_compiled_flash_logits.tolerance.atol | 0.05 |
| numeric_failed_checks.1024_compiled_flash_logits.tolerance.rtol | 0.02 |
| gpu_job_seconds | 63.43970772001194 |
| new_training_tokens | 0 |
| optimizer_updates | 0 |
| scope | "user-facing1-3 / plan70 internal0-2" |
| protected_test_used | false |
| limitations | ["train diagnostic, not held-out score", "Web gold tails above64 make EOS absence alone censored", "first exact token departure is not semantic failure", "BF16 raw tolerance failures remain failures; original/mixed FP32 has same EOS/repetition counts, story marker differs by one", "story source/length/quality not independent", "current candidate full Flash gradient/HF not repeated; original10B audited", "capacity/Adam/optimization not isolated; no new learning", "4gram marker also finds valid repeated phrases"] |

</details>

<details>
<summary>reports/phase6/story-weight-comparison-20261006/annotations.json — None</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/annotations.json) ／ SHA256: `4efdf3f43338f7917c0a8591fc559e027b54acd52cdafd8305d554dc93407e97` ／ 35,877 bytes

| 原キー | 保存値 |
|---|---|
| arms.control.notes_sha256 | "85cadffb1195ba32f3ab41e136f84003880a1813a366db2d2e9bf6f0dcf2545e" |
| arms.story20.notes_sha256 | "c887019c091fdbb829c2a0f43e3cec7e44877d072c8017918d0112971b170371" |

</details>

<details>
<summary>reports/phase6/story-weight-comparison-20261006/compare-result.json — both_actual100M_learning_evaluations_complete_pending_all160_content</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/compare-result.json) ／ SHA256: `bb612ef75a6671a88422816ca20e98559c7117c7d216f6c87af8cfb5dfe2d994` ／ 442,089 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story-weight-comparison-20261006/control/training/checkpoint-00065244.pt" |
| checkpoints.control.checkpoint_sha256 | "353cb231d07dfb9e42328ee0e3ad82ead4d1ad875a25559987e6bf2dd44e03f5" |
| checkpoints.control.binding.config_sha256 | "e5ee42c4bc923632faa5b49eceb76f32e92c9d632bb7d2d292a88117f3938f04" |
| checkpoints.control.binding.arm | "control" |
| checkpoints.control.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.control.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.control.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.control.binding.teacher_goals.web | 75000000 |
| checkpoints.control.binding.teacher_goals.textbook | 20000000 |
| checkpoints.control.binding.teacher_goals.story | 5000000 |
| checkpoints.control.binding.optimizer_policy | "inherit" |
| checkpoints.control.binding.peak_lr | 0.0002 |
| checkpoints.control.binding.loss | "CE body+EOS" |
| checkpoints.control.binding.study_kind | "same_material_story_teacher_weight" |
| checkpoints.control.binding.sampler_policy | "Explicit experimental fork into per-genre document shuffles, same initial seed/order in both arms. Preserve original sampler as parent lineage; do not claim the new mixture keeps its old mixed block cursor. Save new samplers at completed updates." |
| checkpoints.control.update | 65244 |
| checkpoints.control.tokens | 2137915392 |
| checkpoints.control.supervised_tokens | 2120000000 |
| checkpoints.control.additional_supervised_tokens | 100000000 |
| checkpoints.control.additional_input_tokens | 100859904 |
| checkpoints.control.source_teachers.web | 75000000 |
| checkpoints.control.source_teachers.story | 5000000 |
| checkpoints.control.source_teachers.textbook | 20000000 |
| checkpoints.control.source_eos.web | 656229 |
| checkpoints.control.source_eos.story | 38240 |
| checkpoints.control.source_eos.textbook | 148210 |
| checkpoints.control.source_input_tokens.web | 75672576 |
| checkpoints.control.source_input_tokens.story | 5039104 |
| checkpoints.control.source_input_tokens.textbook | 20148224 |
| checkpoints.control.training_seconds | 151.744421539217 |
| checkpoints.control.completed_at | "2026-10-06T00:48:50.371874Z" |
| checkpoints.story20.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story-weight-comparison-20261006/story20/training/checkpoint-00065243.pt" |
| checkpoints.story20.checkpoint_sha256 | "ce267d5dbb0df445896d7d9605e60313a2685e483d715bf23ef8223ff7412e4a" |
| checkpoints.story20.binding.config_sha256 | "e5ee42c4bc923632faa5b49eceb76f32e92c9d632bb7d2d292a88117f3938f04" |
| checkpoints.story20.binding.arm | "story20" |
| checkpoints.story20.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.story20.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.story20.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.story20.binding.teacher_goals.web | 60000000 |
| checkpoints.story20.binding.teacher_goals.textbook | 20000000 |
| checkpoints.story20.binding.teacher_goals.story | 20000000 |
| checkpoints.story20.binding.optimizer_policy | "inherit" |
| checkpoints.story20.binding.peak_lr | 0.0002 |
| checkpoints.story20.binding.loss | "CE body+EOS" |
| checkpoints.story20.binding.study_kind | "same_material_story_teacher_weight" |
| checkpoints.story20.binding.sampler_policy | "Explicit experimental fork into per-genre document shuffles, same initial seed/order in both arms. Preserve original sampler as parent lineage; do not claim the new mixture keeps its old mixed block cursor. Save new samplers at completed updates." |
| checkpoints.story20.update | 65243 |
| checkpoints.story20.tokens | 2137882624 |
| checkpoints.story20.supervised_tokens | 2120000000 |
| checkpoints.story20.additional_supervised_tokens | 100000000 |
| checkpoints.story20.additional_input_tokens | 100827136 |
| checkpoints.story20.source_teachers.web | 60000000 |
| checkpoints.story20.source_teachers.story | 20000000 |
| checkpoints.story20.source_teachers.textbook | 20000000 |
| checkpoints.story20.source_eos.web | 525373 |
| checkpoints.story20.source_eos.story | 153191 |
| checkpoints.story20.source_eos.textbook | 148210 |
| checkpoints.story20.source_input_tokens.web | 60525568 |
| checkpoints.story20.source_input_tokens.story | 20153344 |
| checkpoints.story20.source_input_tokens.textbook | 20148224 |
| checkpoints.story20.training_seconds | 151.20842607061786 |
| checkpoints.story20.completed_at | "2026-10-06T00:52:33.588755Z" |
| evaluations.control.binding.teacher_goals.web | 75000000 |
| evaluations.control.binding.teacher_goals.textbook | 20000000 |
| evaluations.control.binding.teacher_goals.story | 5000000 |
| evaluations.control.binding.loss | "CE body+EOS" |
| evaluations.control.binding.sampler_policy | "Explicit experimental fork into per-genre document shuffles, same initial seed/order in both arms. Preserve original sampler as parent lineage; do not claim the new mixture keeps its old mixed block cursor. Save new samplers at completed updates." |
| evaluations.control.checkpoint_sha256 | "353cb231d07dfb9e42328ee0e3ad82ead4d1ad875a25559987e6bf2dd44e03f5" |
| evaluations.control.body.documents | 256 |
| evaluations.control.body.limit_documents | 256 |
| evaluations.control.body.body_nll | 369714.328417778 |
| evaluations.control.body.eos_nll | 945.5319351702929 |
| evaluations.control.body.body_bytes | 472055 |
| evaluations.control.body.body_tokens | 122343 |
| evaluations.control.body.bpb | 1.1299213611844423 |
| evaluations.control.body.seconds | 1.4734444220084697 |
| evaluations.control.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.control.generation.max_new_tokens | 64 |
| evaluations.control.greedy_rates.eos | 45 |
| evaluations.control.greedy_rates.repetition | 16 |
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
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5625 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5260416666666666, 0.5989583333333334] |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5625 |
| evaluations.control.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5623100303951367 |
| evaluations.control.diagnostics.semantics.per_token_secondary.mcc | 0.12510864843424485 |
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
| evaluations.control.diagnostics.jblimp.primary.accuracy.point | 0.7915407854984894 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.ci95 | [0.7462235649546828, 0.8338368580060423] |
| evaluations.control.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.primary.hard_accuracy | 0.7915407854984894 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7462235649546828 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6978851963746223, 0.7945619335347432] |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7462235649546828 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4273356401384083 |
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
| evaluations.control.diagnostics.jblimp.raw_pair_accuracy | 0.797583081570997 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.point | 0.289544235924933 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.ci95 | [0.26362823949955316, 0.3154602323503128] |
| evaluations.control.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.primary.hard_accuracy | 0.289544235924933 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2761394101876676 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2511170688114388, 0.30205540661304736] |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2761394101876676 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2758430447944515 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.mcc | 0.09566094410218752 |
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
| evaluations.story20.binding.teacher_goals.web | 60000000 |
| evaluations.story20.binding.teacher_goals.textbook | 20000000 |
| evaluations.story20.binding.teacher_goals.story | 20000000 |
| evaluations.story20.binding.loss | "CE body+EOS" |
| evaluations.story20.binding.sampler_policy | "Explicit experimental fork into per-genre document shuffles, same initial seed/order in both arms. Preserve original sampler as parent lineage; do not claim the new mixture keeps its old mixed block cursor. Save new samplers at completed updates." |
| evaluations.story20.checkpoint_sha256 | "ce267d5dbb0df445896d7d9605e60313a2685e483d715bf23ef8223ff7412e4a" |
| evaluations.story20.body.documents | 256 |
| evaluations.story20.body.limit_documents | 256 |
| evaluations.story20.body.body_nll | 371464.0153236389 |
| evaluations.story20.body.eos_nll | 937.1099682152271 |
| evaluations.story20.body.body_bytes | 472055 |
| evaluations.story20.body.body_tokens | 122343 |
| evaluations.story20.body.bpb | 1.1352687563443153 |
| evaluations.story20.body.seconds | 1.2746439430047758 |
| evaluations.story20.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.story20.generation.max_new_tokens | 64 |
| evaluations.story20.greedy_rates.eos | 38 |
| evaluations.story20.greedy_rates.repetition | 21 |
| evaluations.story20.greedy_rates.unicode_failure | 0 |
| evaluations.story20.greedy_rates.role_leak | 0 |
| evaluations.story20.greedy_rates.empty | 0 |
| evaluations.story20.diagnostics.semantics.primary.accuracy.point | 0.5677083333333334 |
| evaluations.story20.diagnostics.semantics.primary.accuracy.ci95 | [0.53125, 0.609375] |
| evaluations.story20.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.story20.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.story20.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.story20.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.primary.hard_accuracy | 0.5677083333333334 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.accuracy.point | 0.578125 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5364583333333334, 0.6197916666666666] |
| evaluations.story20.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.578125 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5781135555977539 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.mcc | 0.15625847779496568 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.story20.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.story20.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.story20.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.story20.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.story20.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.story20.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.story20.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.story20.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.story20.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.story20.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.story20.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.story20.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.story20.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.story20.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.story20.diagnostics.jblimp.primary.accuracy.point | 0.7915407854984894 |
| evaluations.story20.diagnostics.jblimp.primary.accuracy.ci95 | [0.7462235649546828, 0.8338368580060423] |
| evaluations.story20.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.story20.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.story20.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.story20.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.primary.hard_accuracy | 0.7915407854984894 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7522658610271903 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7038519637462236, 0.7976586102719029] |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7522658610271903 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42931034482758623 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.story20.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.story20.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.story20.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.story20.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.story20.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.story20.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.story20.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.story20.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.story20.diagnostics.jblimp.raw_pair_accuracy | 0.8066465256797583 |
| evaluations.story20.diagnostics.jcqa.primary.accuracy.point | 0.2975871313672922 |
| evaluations.story20.diagnostics.jcqa.primary.accuracy.ci95 | [0.2716711349419124, 0.32439678284182305] |
| evaluations.story20.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.story20.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.story20.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.story20.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jcqa.primary.hard_accuracy | 0.2975871313672922 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2931188561215371 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.26720285969615726, 0.3199285075960679] |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2931188561215371 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.29246767346523195 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.mcc | 0.11684593804862778 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.story20.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.story20.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.story20.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.story20.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.story20.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.story20.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.story20.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.story20.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.story20.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.story20.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.story20.diagnostics.semantic_both_contexts.correct | 15 |
| evaluations.story20.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.story20.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.story20.protected_test_used | false |
| status | "both_actual100M_learning_evaluations_complete_pending_all160_content" |
| scientific_teacher_tokens | 200000000 |
| verification_teacher_tokens | 2599809 |
| verification_GPU_seconds | 22.201600583008258 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |
| GPU_seconds | 453.7347566630051 |

</details>

<details>
<summary>reports/phase6/story-weight-comparison-20261006/control-content-review.json — None</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/control-content-review.json) ／ SHA256: `13d9a10f9c95e8f515d8276f4c8b9b245238f3a5cb8c64f847e5e2cc16e631d0` ／ 729 bytes

| 原キー | 保存値 |
|---|---|
| BPB | 1.1299213611844423 |
| rates.eos | 45 |
| rates.repetition | 16 |
| rates.unicode_failure | 0 |
| rates.role_leak | 0 |
| rates.empty | 0 |
| grammar2 | 67 |
| relevance2 | 49 |
| coherent | 11 |
| appropriate | 27 |
| new_teacher_tokens | 100000000 |
| source_teacher_tokens.web | 75000000 |
| source_teacher_tokens.textbook | 20000000 |
| source_teacher_tokens.story | 5000000 |
| notes_sha256 | "85cadffb1195ba32f3ab41e136f84003880a1813a366db2d2e9bf6f0dcf2545e" |
| Base_adopted | false |

</details>

<details>
<summary>reports/phase6/story-weight-comparison-20261006/control/training/latest.json — None</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/control/training/latest.json) ／ SHA256: `0f273121a65f6de8dfafae32ba05d943b1a5d3a6773588764c5ed693e876d2af` ／ 277 bytes

| 原キー | 保存値 |
|---|---|
| update | 65244 |
| tokens_seen | 2137915392 |

</details>

<details>
<summary>reports/phase6/story-weight-comparison-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/job.json) ／ SHA256: `f5ff7470e00639b1d474672b1824856b303a93cba2822567655aa5c48bb914c2` ／ 820 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 453.7347566630051 |
| Base_adopted | false |
| protected_test_used | false |
| teachers | 99447827 |
| teacher_budget | 100000000 |
| source_teachers.web | 59668201 |
| source_teachers.story | 19889415 |
| source_teachers.textbook | 19890211 |
| loss | 2.405149221420288 |

</details>

<details>
<summary>reports/phase6/story-weight-comparison-20261006/probe/control/timing/latest.json — None</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/probe/control/timing/latest.json) ／ SHA256: `a62415055a873b63e2eb946e326d412426f4546e1db6c6c7459f14291e34aca6` ／ 272 bytes

| 原キー | 保存値 |
|---|---|
| update | 62198 |
| tokens_seen | 2038104064 |

</details>

<details>
<summary>reports/phase6/story-weight-comparison-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/probe/job.json) ／ SHA256: `41dec150e390d534cd9e603ceb748ed0caee56138f5a09795dfc1561d1938141` ／ 594 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 22.201600583008258 |
| Base_adopted | false |
| protected_test_used | false |
| completed_updates | 32 |

</details>

<details>
<summary>reports/phase6/story-weight-comparison-20261006/probe/result.json — actual_story_weight_resume_and_timing_complete</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/probe/result.json) ／ SHA256: `629cb337b9599a51fb53d587e1ff463d6df083602c4d3fc4b7d20dd0140b128a` ／ 97,158 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_story_weight_resume_and_timing_complete" |
| gates.control.passed | true |
| gates.control.checks.model | true |
| gates.control.checks.optimizer | true |
| gates.control.checks.scheduler | true |
| gates.control.checks.rng | true |
| gates.control.checks.sampler | true |
| gates.control.checks.lineage | true |
| gates.control.checks.tokens | true |
| gates.control.checks.supervised_tokens | true |
| gates.control.checks.body_bytes | true |
| gates.control.checks.token_digest | true |
| gates.control.checks.update | true |
| gates.control.checks.spec | true |
| gates.control.checks.model_config | true |
| gates.control.checks.pilot_binding | true |
| gates.control.checks.study_binding | true |
| gates.control.checks.history_loss | true |
| gates.control.checks.history_gradient_norm | true |
| gates.control.checks.history_lr | true |
| gates.control.checks.history_token_digest | true |
| gates.control.checks.history_source_teachers | true |
| gates.control.checks.history_source_eos | true |
| gates.control.checks.history_source_input_tokens | true |
| gates.control.checks.history_source_body_bytes | true |
| gates.control.checks.finite | true |
| gates.control.checks.no_reheat | true |
| gates.control.GPU_optimizer_updates | 8 |
| gates.control.verification_teacher_tokens | 259964 |
| gates.story20.passed | true |
| gates.story20.checks.model | true |
| gates.story20.checks.optimizer | true |
| gates.story20.checks.scheduler | true |
| gates.story20.checks.rng | true |
| gates.story20.checks.sampler | true |
| gates.story20.checks.lineage | true |
| gates.story20.checks.tokens | true |
| gates.story20.checks.supervised_tokens | true |
| gates.story20.checks.body_bytes | true |
| gates.story20.checks.token_digest | true |
| gates.story20.checks.update | true |
| gates.story20.checks.spec | true |
| gates.story20.checks.model_config | true |
| gates.story20.checks.pilot_binding | true |
| gates.story20.checks.study_binding | true |
| gates.story20.checks.history_loss | true |
| gates.story20.checks.history_gradient_norm | true |
| gates.story20.checks.history_lr | true |
| gates.story20.checks.history_token_digest | true |
| gates.story20.checks.history_source_teachers | true |
| gates.story20.checks.history_source_eos | true |
| gates.story20.checks.history_source_input_tokens | true |
| gates.story20.checks.history_source_body_bytes | true |
| gates.story20.checks.finite | true |
| gates.story20.checks.no_reheat | true |
| gates.story20.GPU_optimizer_updates | 8 |
| gates.story20.verification_teacher_tokens | 260016 |
| timings.control.verification_teacher_tokens | 1039839 |
| timings.control.terminal_save_seconds | 0.16648784899734892 |
| timings.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story-weight-comparison-20261006/probe/control/timing/checkpoint.pt" |
| timings.control.checkpoint_sha256 | "5be9afd6ea323d2aaf0df0a986215cd41458e711233561320b1a8b8f84c48fc6" |
| timings.story20.verification_teacher_tokens | 1039990 |
| timings.story20.terminal_save_seconds | 0.1708043239923427 |
| timings.story20.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story-weight-comparison-20261006/probe/story20/timing/checkpoint.pt" |
| timings.story20.checkpoint_sha256 | "aac27a77d7ea16463f0f700b1b20b266bf8da0f34b797c5c14c05cc78008aaf7" |
| scientific_teacher_tokens | 0 |
| passed | true |
| verification_teacher_tokens | 2599809 |
| GPU_optimizer_updates | 80 |
| GPU_seconds | 22.201600583008258 |

</details>

<details>
<summary>reports/phase6/story-weight-comparison-20261006/progress-result.json — None</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/progress-result.json) ／ SHA256: `b0448ed5c2189fe781f32247c4357965542a94ed8395fc2713758d280f47f8f8` ／ 441,624 bytes

| 原キー | 保存値 |
|---|---|
| checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story-weight-comparison-20261006/control/training/checkpoint-00065244.pt" |
| checkpoints.control.checkpoint_sha256 | "353cb231d07dfb9e42328ee0e3ad82ead4d1ad875a25559987e6bf2dd44e03f5" |
| checkpoints.control.binding.config_sha256 | "e5ee42c4bc923632faa5b49eceb76f32e92c9d632bb7d2d292a88117f3938f04" |
| checkpoints.control.binding.arm | "control" |
| checkpoints.control.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.control.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.control.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.control.binding.teacher_goals.web | 75000000 |
| checkpoints.control.binding.teacher_goals.textbook | 20000000 |
| checkpoints.control.binding.teacher_goals.story | 5000000 |
| checkpoints.control.binding.optimizer_policy | "inherit" |
| checkpoints.control.binding.peak_lr | 0.0002 |
| checkpoints.control.binding.loss | "CE body+EOS" |
| checkpoints.control.binding.study_kind | "same_material_story_teacher_weight" |
| checkpoints.control.binding.sampler_policy | "Explicit experimental fork into per-genre document shuffles, same initial seed/order in both arms. Preserve original sampler as parent lineage; do not claim the new mixture keeps its old mixed block cursor. Save new samplers at completed updates." |
| checkpoints.control.update | 65244 |
| checkpoints.control.tokens | 2137915392 |
| checkpoints.control.supervised_tokens | 2120000000 |
| checkpoints.control.additional_supervised_tokens | 100000000 |
| checkpoints.control.additional_input_tokens | 100859904 |
| checkpoints.control.source_teachers.web | 75000000 |
| checkpoints.control.source_teachers.story | 5000000 |
| checkpoints.control.source_teachers.textbook | 20000000 |
| checkpoints.control.source_eos.web | 656229 |
| checkpoints.control.source_eos.story | 38240 |
| checkpoints.control.source_eos.textbook | 148210 |
| checkpoints.control.source_input_tokens.web | 75672576 |
| checkpoints.control.source_input_tokens.story | 5039104 |
| checkpoints.control.source_input_tokens.textbook | 20148224 |
| checkpoints.control.training_seconds | 151.744421539217 |
| checkpoints.control.completed_at | "2026-10-06T00:48:50.371874Z" |
| checkpoints.story20.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story-weight-comparison-20261006/story20/training/checkpoint-00065243.pt" |
| checkpoints.story20.checkpoint_sha256 | "ce267d5dbb0df445896d7d9605e60313a2685e483d715bf23ef8223ff7412e4a" |
| checkpoints.story20.binding.config_sha256 | "e5ee42c4bc923632faa5b49eceb76f32e92c9d632bb7d2d292a88117f3938f04" |
| checkpoints.story20.binding.arm | "story20" |
| checkpoints.story20.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.story20.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.story20.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.story20.binding.teacher_goals.web | 60000000 |
| checkpoints.story20.binding.teacher_goals.textbook | 20000000 |
| checkpoints.story20.binding.teacher_goals.story | 20000000 |
| checkpoints.story20.binding.optimizer_policy | "inherit" |
| checkpoints.story20.binding.peak_lr | 0.0002 |
| checkpoints.story20.binding.loss | "CE body+EOS" |
| checkpoints.story20.binding.study_kind | "same_material_story_teacher_weight" |
| checkpoints.story20.binding.sampler_policy | "Explicit experimental fork into per-genre document shuffles, same initial seed/order in both arms. Preserve original sampler as parent lineage; do not claim the new mixture keeps its old mixed block cursor. Save new samplers at completed updates." |
| checkpoints.story20.update | 65243 |
| checkpoints.story20.tokens | 2137882624 |
| checkpoints.story20.supervised_tokens | 2120000000 |
| checkpoints.story20.additional_supervised_tokens | 100000000 |
| checkpoints.story20.additional_input_tokens | 100827136 |
| checkpoints.story20.source_teachers.web | 60000000 |
| checkpoints.story20.source_teachers.story | 20000000 |
| checkpoints.story20.source_teachers.textbook | 20000000 |
| checkpoints.story20.source_eos.web | 525373 |
| checkpoints.story20.source_eos.story | 153191 |
| checkpoints.story20.source_eos.textbook | 148210 |
| checkpoints.story20.source_input_tokens.web | 60525568 |
| checkpoints.story20.source_input_tokens.story | 20153344 |
| checkpoints.story20.source_input_tokens.textbook | 20148224 |
| checkpoints.story20.training_seconds | 151.20842607061786 |
| checkpoints.story20.completed_at | "2026-10-06T00:52:33.588755Z" |
| evaluations.control.binding.teacher_goals.web | 75000000 |
| evaluations.control.binding.teacher_goals.textbook | 20000000 |
| evaluations.control.binding.teacher_goals.story | 5000000 |
| evaluations.control.binding.loss | "CE body+EOS" |
| evaluations.control.binding.sampler_policy | "Explicit experimental fork into per-genre document shuffles, same initial seed/order in both arms. Preserve original sampler as parent lineage; do not claim the new mixture keeps its old mixed block cursor. Save new samplers at completed updates." |
| evaluations.control.checkpoint_sha256 | "353cb231d07dfb9e42328ee0e3ad82ead4d1ad875a25559987e6bf2dd44e03f5" |
| evaluations.control.body.documents | 256 |
| evaluations.control.body.limit_documents | 256 |
| evaluations.control.body.body_nll | 369714.328417778 |
| evaluations.control.body.eos_nll | 945.5319351702929 |
| evaluations.control.body.body_bytes | 472055 |
| evaluations.control.body.body_tokens | 122343 |
| evaluations.control.body.bpb | 1.1299213611844423 |
| evaluations.control.body.seconds | 1.4734444220084697 |
| evaluations.control.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.control.generation.max_new_tokens | 64 |
| evaluations.control.greedy_rates.eos | 45 |
| evaluations.control.greedy_rates.repetition | 16 |
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
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5625 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5260416666666666, 0.5989583333333334] |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.control.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5625 |
| evaluations.control.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5623100303951367 |
| evaluations.control.diagnostics.semantics.per_token_secondary.mcc | 0.12510864843424485 |
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
| evaluations.control.diagnostics.jblimp.primary.accuracy.point | 0.7915407854984894 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.ci95 | [0.7462235649546828, 0.8338368580060423] |
| evaluations.control.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.primary.hard_accuracy | 0.7915407854984894 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7462235649546828 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6978851963746223, 0.7945619335347432] |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7462235649546828 |
| evaluations.control.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4273356401384083 |
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
| evaluations.control.diagnostics.jblimp.raw_pair_accuracy | 0.797583081570997 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.point | 0.289544235924933 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.ci95 | [0.26362823949955316, 0.3154602323503128] |
| evaluations.control.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.primary.hard_accuracy | 0.289544235924933 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2761394101876676 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2511170688114388, 0.30205540661304736] |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.control.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2761394101876676 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.2758430447944515 |
| evaluations.control.diagnostics.jcqa.per_token_secondary.mcc | 0.09566094410218752 |
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
| evaluations.story20.binding.teacher_goals.web | 60000000 |
| evaluations.story20.binding.teacher_goals.textbook | 20000000 |
| evaluations.story20.binding.teacher_goals.story | 20000000 |
| evaluations.story20.binding.loss | "CE body+EOS" |
| evaluations.story20.binding.sampler_policy | "Explicit experimental fork into per-genre document shuffles, same initial seed/order in both arms. Preserve original sampler as parent lineage; do not claim the new mixture keeps its old mixed block cursor. Save new samplers at completed updates." |
| evaluations.story20.checkpoint_sha256 | "ce267d5dbb0df445896d7d9605e60313a2685e483d715bf23ef8223ff7412e4a" |
| evaluations.story20.body.documents | 256 |
| evaluations.story20.body.limit_documents | 256 |
| evaluations.story20.body.body_nll | 371464.0153236389 |
| evaluations.story20.body.eos_nll | 937.1099682152271 |
| evaluations.story20.body.body_bytes | 472055 |
| evaluations.story20.body.body_tokens | 122343 |
| evaluations.story20.body.bpb | 1.1352687563443153 |
| evaluations.story20.body.seconds | 1.2746439430047758 |
| evaluations.story20.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.story20.generation.max_new_tokens | 64 |
| evaluations.story20.greedy_rates.eos | 38 |
| evaluations.story20.greedy_rates.repetition | 21 |
| evaluations.story20.greedy_rates.unicode_failure | 0 |
| evaluations.story20.greedy_rates.role_leak | 0 |
| evaluations.story20.greedy_rates.empty | 0 |
| evaluations.story20.diagnostics.semantics.primary.accuracy.point | 0.5677083333333334 |
| evaluations.story20.diagnostics.semantics.primary.accuracy.ci95 | [0.53125, 0.609375] |
| evaluations.story20.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.story20.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.story20.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.story20.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.primary.hard_accuracy | 0.5677083333333334 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.accuracy.point | 0.578125 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5364583333333334, 0.6197916666666666] |
| evaluations.story20.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.578125 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5781135555977539 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.mcc | 0.15625847779496568 |
| evaluations.story20.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.story20.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.story20.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.story20.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.story20.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.story20.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.story20.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.story20.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.story20.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.story20.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.story20.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.story20.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.story20.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.story20.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.story20.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.story20.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.story20.diagnostics.jblimp.primary.accuracy.point | 0.7915407854984894 |
| evaluations.story20.diagnostics.jblimp.primary.accuracy.ci95 | [0.7462235649546828, 0.8338368580060423] |
| evaluations.story20.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.story20.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.story20.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.story20.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.primary.hard_accuracy | 0.7915407854984894 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7522658610271903 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.7038519637462236, 0.7976586102719029] |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7522658610271903 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42931034482758623 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.story20.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.story20.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.story20.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.story20.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.story20.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.story20.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.story20.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.story20.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.story20.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.story20.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.story20.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.story20.diagnostics.jblimp.raw_pair_accuracy | 0.8066465256797583 |
| evaluations.story20.diagnostics.jcqa.primary.accuracy.point | 0.2975871313672922 |
| evaluations.story20.diagnostics.jcqa.primary.accuracy.ci95 | [0.2716711349419124, 0.32439678284182305] |
| evaluations.story20.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.story20.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.story20.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.story20.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jcqa.primary.hard_accuracy | 0.2975871313672922 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.2931188561215371 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.26720285969615726, 0.3199285075960679] |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.2931188561215371 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.29246767346523195 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.mcc | 0.11684593804862778 |
| evaluations.story20.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.story20.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.story20.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.story20.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.story20.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.story20.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.story20.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.story20.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.story20.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.story20.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.story20.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.story20.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.story20.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.story20.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.story20.diagnostics.semantic_both_contexts.correct | 15 |
| evaluations.story20.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.story20.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.story20.protected_test_used | false |

</details>

<details>
<summary>reports/phase6/story-weight-comparison-20261006/review.json — same_material_story_weights_actual200M_all160_evidence_complete</summary>

[原記録](../../reports/phase6/story-weight-comparison-20261006/review.json) ／ SHA256: `58ba73470b4e9c00cc5ddd5be48b86ffdfc5bbf4218a1965a36b70d6e5aeaf06` ／ 3,943 bytes

| 原キー | 保存値 |
|---|---|
| status | "same_material_story_weights_actual200M_all160_evidence_complete" |
| summaries.control.BPB | 1.1299213611844423 |
| summaries.control.rates.eos | 45 |
| summaries.control.rates.repetition | 16 |
| summaries.control.rates.unicode_failure | 0 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 67 |
| summaries.control.relevance2 | 49 |
| summaries.control.coherent | 11 |
| summaries.control.appropriate | 27 |
| summaries.control.new_teacher_tokens | 100000000 |
| summaries.control.source_teacher_tokens.web | 75000000 |
| summaries.control.source_teacher_tokens.textbook | 20000000 |
| summaries.control.source_teacher_tokens.story | 5000000 |
| summaries.control.notes_sha256 | "85cadffb1195ba32f3ab41e136f84003880a1813a366db2d2e9bf6f0dcf2545e" |
| summaries.control.Base_adopted | false |
| summaries.story20.BPB | 1.1352687563443153 |
| summaries.story20.rates.eos | 38 |
| summaries.story20.rates.repetition | 21 |
| summaries.story20.rates.unicode_failure | 0 |
| summaries.story20.rates.role_leak | 0 |
| summaries.story20.rates.empty | 0 |
| summaries.story20.grammar2 | 64 |
| summaries.story20.relevance2 | 47 |
| summaries.story20.coherent | 15 |
| summaries.story20.appropriate | 24 |
| summaries.story20.new_teacher_tokens | 100000000 |
| summaries.story20.source_teacher_tokens.web | 60000000 |
| summaries.story20.source_teacher_tokens.textbook | 20000000 |
| summaries.story20.source_teacher_tokens.story | 20000000 |
| summaries.story20.notes_sha256 | "c887019c091fdbb829c2a0f43e3cec7e44877d072c8017918d0112971b170371" |
| summaries.story20.Base_adopted | false |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | false |
| quality_comparison.checks.repetition_nonworsening | false |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| absolute_dev_screen.control.grammar_at_least56 | true |
| absolute_dev_screen.control.coherence_at_least27 | false |
| absolute_dev_screen.control.appropriate_at_least27 | true |
| absolute_dev_screen.control.EOS_at_least37 | true |
| absolute_dev_screen.control.repetition_at_most18 | true |
| absolute_dev_screen.control.no_empty_role_unicode | true |
| absolute_dev_screen.story20.grammar_at_least56 | true |
| absolute_dev_screen.story20.coherence_at_least27 | false |
| absolute_dev_screen.story20.appropriate_at_least27 | false |
| absolute_dev_screen.story20.EOS_at_least37 | true |
| absolute_dev_screen.story20.repetition_at_most18 | false |
| absolute_dev_screen.story20.no_empty_role_unicode | true |
| original_Web.control.EOS_at_least8_more | true |
| original_Web.control.repetition_no_worse | true |
| original_Web.control.no_empty_role_unicode | true |
| original_Web.control.BPB_degradation_at_most1percent | false |
| original_Web.story20.EOS_at_least8_more | true |
| original_Web.story20.repetition_no_worse | true |
| original_Web.story20.no_empty_role_unicode | true |
| original_Web.story20.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation.control | false |
| eligible_for_final_Base_validation.story20 | false |
| new_scientific_teacher_tokens | 200000000 |
| verification_teacher_tokens | 2599809 |
| GPU_seconds | 453.7347566630051 |
| verification_GPU_seconds | 22.201600583008258 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |

</details>

<details>
<summary>reports/phase6/story_weight_active_job.json — complete_process_exited_both_candidates_rejected</summary>

[原記録](../../reports/phase6/story_weight_active_job.json) ／ SHA256: `9d7b57c46ed26e1e11ce467b539fe7212263c23de2334468d91c1adce1a5a531` ／ 5,717 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_process_exited_both_candidates_rejected" |
| initial_job_status_label | "complete" |
| scientific_config | "configs/phase6/story_weight_comparison.json" |
| actual_probe.GPU_seconds | 22.201600583008258 |
| actual_probe.verification_teacher_tokens | 2599809 |
| actual_probe.scientific_teacher_tokens | 0 |
| actual_probe.passed | true |
| scientific_progress.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story-weight-comparison-20261006/control/training/checkpoint-00065244.pt" |
| scientific_progress.control.checkpoint_sha256 | "353cb231d07dfb9e42328ee0e3ad82ead4d1ad875a25559987e6bf2dd44e03f5" |
| scientific_progress.control.binding.config_sha256 | "e5ee42c4bc923632faa5b49eceb76f32e92c9d632bb7d2d292a88117f3938f04" |
| scientific_progress.control.binding.arm | "control" |
| scientific_progress.control.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| scientific_progress.control.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| scientific_progress.control.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| scientific_progress.control.binding.teacher_goals.web | 75000000 |
| scientific_progress.control.binding.teacher_goals.textbook | 20000000 |
| scientific_progress.control.binding.teacher_goals.story | 5000000 |
| scientific_progress.control.binding.optimizer_policy | "inherit" |
| scientific_progress.control.binding.peak_lr | 0.0002 |
| scientific_progress.control.binding.loss | "CE body+EOS" |
| scientific_progress.control.binding.study_kind | "same_material_story_teacher_weight" |
| scientific_progress.control.binding.sampler_policy | "Explicit experimental fork into per-genre document shuffles, same initial seed/order in both arms. Preserve original sampler as parent lineage; do not claim the new mixture keeps its old mixed block cursor. Save new samplers at completed updates." |
| scientific_progress.control.update | 65244 |
| scientific_progress.control.tokens | 2137915392 |
| scientific_progress.control.supervised_tokens | 2120000000 |
| scientific_progress.control.additional_supervised_tokens | 100000000 |
| scientific_progress.control.additional_input_tokens | 100859904 |
| scientific_progress.control.source_teachers.web | 75000000 |
| scientific_progress.control.source_teachers.story | 5000000 |
| scientific_progress.control.source_teachers.textbook | 20000000 |
| scientific_progress.control.source_eos.web | 656229 |
| scientific_progress.control.source_eos.story | 38240 |
| scientific_progress.control.source_eos.textbook | 148210 |
| scientific_progress.control.source_input_tokens.web | 75672576 |
| scientific_progress.control.source_input_tokens.story | 5039104 |
| scientific_progress.control.source_input_tokens.textbook | 20148224 |
| scientific_progress.control.training_seconds | 151.744421539217 |
| scientific_progress.control.completed_at | "2026-10-06T00:48:50.371874Z" |
| scientific_progress.story20.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story-weight-comparison-20261006/story20/training/checkpoint-00065243.pt" |
| scientific_progress.story20.checkpoint_sha256 | "ce267d5dbb0df445896d7d9605e60313a2685e483d715bf23ef8223ff7412e4a" |
| scientific_progress.story20.binding.config_sha256 | "e5ee42c4bc923632faa5b49eceb76f32e92c9d632bb7d2d292a88117f3938f04" |
| scientific_progress.story20.binding.arm | "story20" |
| scientific_progress.story20.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| scientific_progress.story20.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| scientific_progress.story20.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| scientific_progress.story20.binding.teacher_goals.web | 60000000 |
| scientific_progress.story20.binding.teacher_goals.textbook | 20000000 |
| scientific_progress.story20.binding.teacher_goals.story | 20000000 |
| scientific_progress.story20.binding.optimizer_policy | "inherit" |
| scientific_progress.story20.binding.peak_lr | 0.0002 |
| scientific_progress.story20.binding.loss | "CE body+EOS" |
| scientific_progress.story20.binding.study_kind | "same_material_story_teacher_weight" |
| scientific_progress.story20.binding.sampler_policy | "Explicit experimental fork into per-genre document shuffles, same initial seed/order in both arms. Preserve original sampler as parent lineage; do not claim the new mixture keeps its old mixed block cursor. Save new samplers at completed updates." |
| scientific_progress.story20.update | 65243 |
| scientific_progress.story20.tokens | 2137882624 |
| scientific_progress.story20.supervised_tokens | 2120000000 |
| scientific_progress.story20.additional_supervised_tokens | 100000000 |
| scientific_progress.story20.additional_input_tokens | 100827136 |
| scientific_progress.story20.source_teachers.web | 60000000 |
| scientific_progress.story20.source_teachers.story | 20000000 |
| scientific_progress.story20.source_teachers.textbook | 20000000 |
| scientific_progress.story20.source_eos.web | 525373 |
| scientific_progress.story20.source_eos.story | 153191 |
| scientific_progress.story20.source_eos.textbook | 148210 |
| scientific_progress.story20.source_input_tokens.web | 60525568 |
| scientific_progress.story20.source_input_tokens.story | 20153344 |
| scientific_progress.story20.source_input_tokens.textbook | 20148224 |
| scientific_progress.story20.training_seconds | 151.20842607061786 |
| scientific_progress.story20.completed_at | "2026-10-06T00:52:33.588755Z" |
| checkpoint_tensors_retained_in_WSL | true |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |
| completion | "reports/phase6/story_weight_comparison_completion.json" |

</details>

<details>
<summary>reports/phase6/story_weight_comparison_completion.json — actual200M_all160_complete_both_Base_candidates_rejected</summary>

[原記録](../../reports/phase6/story_weight_comparison_completion.json) ／ SHA256: `f23df4d01e3ff631e1fc93d8aa3931af0b7f5e9d9118488110d2e093d289ad99` ／ 8,613 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual200M_all160_complete_both_Base_candidates_rejected" |
| actual_scientific_identity.process_exited_and_absent | true |
| actual_scientific_identity.start_ticks | "13077625" |
| actual_scientific_identity.boot_id | "53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe" |
| actual_scientific_identity.pid | 518044 |
| scientific_teacher_tokens | 200000000 |
| scientific_input_tokens | 201687040 |
| verification_teacher_tokens | 2599809 |
| verification_GPU_seconds | 22.201600583008258 |
| scientific_job_GPU_seconds | 453.7347566630051 |
| total_new_GPU_seconds | 475.93635724601336 |
| GPU_ceiling_seconds | 1800 |
| checkpoints.control.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story-weight-comparison-20261006/control/training/checkpoint-00065244.pt" |
| checkpoints.control.checkpoint_sha256 | "353cb231d07dfb9e42328ee0e3ad82ead4d1ad875a25559987e6bf2dd44e03f5" |
| checkpoints.control.binding.config_sha256 | "e5ee42c4bc923632faa5b49eceb76f32e92c9d632bb7d2d292a88117f3938f04" |
| checkpoints.control.binding.arm | "control" |
| checkpoints.control.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.control.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.control.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.control.binding.teacher_goals.web | 75000000 |
| checkpoints.control.binding.teacher_goals.textbook | 20000000 |
| checkpoints.control.binding.teacher_goals.story | 5000000 |
| checkpoints.control.binding.optimizer_policy | "inherit" |
| checkpoints.control.binding.peak_lr | 0.0002 |
| checkpoints.control.binding.loss | "CE body+EOS" |
| checkpoints.control.binding.study_kind | "same_material_story_teacher_weight" |
| checkpoints.control.binding.sampler_policy | "Explicit experimental fork into per-genre document shuffles, same initial seed/order in both arms. Preserve original sampler as parent lineage; do not claim the new mixture keeps its old mixed block cursor. Save new samplers at completed updates." |
| checkpoints.control.update | 65244 |
| checkpoints.control.tokens | 2137915392 |
| checkpoints.control.supervised_tokens | 2120000000 |
| checkpoints.control.additional_supervised_tokens | 100000000 |
| checkpoints.control.additional_input_tokens | 100859904 |
| checkpoints.control.source_teachers.web | 75000000 |
| checkpoints.control.source_teachers.story | 5000000 |
| checkpoints.control.source_teachers.textbook | 20000000 |
| checkpoints.control.source_eos.web | 656229 |
| checkpoints.control.source_eos.story | 38240 |
| checkpoints.control.source_eos.textbook | 148210 |
| checkpoints.control.source_input_tokens.web | 75672576 |
| checkpoints.control.source_input_tokens.story | 5039104 |
| checkpoints.control.source_input_tokens.textbook | 20148224 |
| checkpoints.control.training_seconds | 151.744421539217 |
| checkpoints.control.completed_at | "2026-10-06T00:48:50.371874Z" |
| checkpoints.story20.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story-weight-comparison-20261006/story20/training/checkpoint-00065243.pt" |
| checkpoints.story20.checkpoint_sha256 | "ce267d5dbb0df445896d7d9605e60313a2685e483d715bf23ef8223ff7412e4a" |
| checkpoints.story20.binding.config_sha256 | "e5ee42c4bc923632faa5b49eceb76f32e92c9d632bb7d2d292a88117f3938f04" |
| checkpoints.story20.binding.arm | "story20" |
| checkpoints.story20.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/textbook-coverage-2b-20261006/decay/checkpoint-00062166.pt" |
| checkpoints.story20.binding.parent.sha256 | "965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249" |
| checkpoints.story20.binding.short_manifest_sha256 | "8cde6396d433644bb93efa27eb862a33d04fec6c6ab1a54b9e03006f3573a133" |
| checkpoints.story20.binding.teacher_goals.web | 60000000 |
| checkpoints.story20.binding.teacher_goals.textbook | 20000000 |
| checkpoints.story20.binding.teacher_goals.story | 20000000 |
| checkpoints.story20.binding.optimizer_policy | "inherit" |
| checkpoints.story20.binding.peak_lr | 0.0002 |
| checkpoints.story20.binding.loss | "CE body+EOS" |
| checkpoints.story20.binding.study_kind | "same_material_story_teacher_weight" |
| checkpoints.story20.binding.sampler_policy | "Explicit experimental fork into per-genre document shuffles, same initial seed/order in both arms. Preserve original sampler as parent lineage; do not claim the new mixture keeps its old mixed block cursor. Save new samplers at completed updates." |
| checkpoints.story20.update | 65243 |
| checkpoints.story20.tokens | 2137882624 |
| checkpoints.story20.supervised_tokens | 2120000000 |
| checkpoints.story20.additional_supervised_tokens | 100000000 |
| checkpoints.story20.additional_input_tokens | 100827136 |
| checkpoints.story20.source_teachers.web | 60000000 |
| checkpoints.story20.source_teachers.story | 20000000 |
| checkpoints.story20.source_teachers.textbook | 20000000 |
| checkpoints.story20.source_eos.web | 525373 |
| checkpoints.story20.source_eos.story | 153191 |
| checkpoints.story20.source_eos.textbook | 148210 |
| checkpoints.story20.source_input_tokens.web | 60525568 |
| checkpoints.story20.source_input_tokens.story | 20153344 |
| checkpoints.story20.source_input_tokens.textbook | 20148224 |
| checkpoints.story20.training_seconds | 151.20842607061786 |
| checkpoints.story20.completed_at | "2026-10-06T00:52:33.588755Z" |
| summaries.control.BPB | 1.1299213611844423 |
| summaries.control.rates.eos | 45 |
| summaries.control.rates.repetition | 16 |
| summaries.control.rates.unicode_failure | 0 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 67 |
| summaries.control.relevance2 | 49 |
| summaries.control.coherent | 11 |
| summaries.control.appropriate | 27 |
| summaries.control.new_teacher_tokens | 100000000 |
| summaries.control.source_teacher_tokens.web | 75000000 |
| summaries.control.source_teacher_tokens.textbook | 20000000 |
| summaries.control.source_teacher_tokens.story | 5000000 |
| summaries.control.notes_sha256 | "85cadffb1195ba32f3ab41e136f84003880a1813a366db2d2e9bf6f0dcf2545e" |
| summaries.control.Base_adopted | false |
| summaries.story20.BPB | 1.1352687563443153 |
| summaries.story20.rates.eos | 38 |
| summaries.story20.rates.repetition | 21 |
| summaries.story20.rates.unicode_failure | 0 |
| summaries.story20.rates.role_leak | 0 |
| summaries.story20.rates.empty | 0 |
| summaries.story20.grammar2 | 64 |
| summaries.story20.relevance2 | 47 |
| summaries.story20.coherent | 15 |
| summaries.story20.appropriate | 24 |
| summaries.story20.new_teacher_tokens | 100000000 |
| summaries.story20.source_teacher_tokens.web | 60000000 |
| summaries.story20.source_teacher_tokens.textbook | 20000000 |
| summaries.story20.source_teacher_tokens.story | 20000000 |
| summaries.story20.notes_sha256 | "c887019c091fdbb829c2a0f43e3cec7e44877d072c8017918d0112971b170371" |
| summaries.story20.Base_adopted | false |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | false |
| quality_comparison.checks.repetition_nonworsening | false |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| portable_text_bytes | 12673202 |
| UI_restored.training_tokens | 10000007168 |
| UI_restored.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| condition_pair_analysis | "reports/phase6/story_weight_condition_pair_analysis.json" |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |

</details>

<details>
<summary>reports/phase6/story_weight_comparison_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/story_weight_comparison_evidence_manifest.json) ／ SHA256: `f8d03423bfe0c47e87f5cf689896398e84b934102f11416a53adc8d54d32f39e` ／ 19,912 bytes

| 原キー | 保存値 |
|---|---|
| uncompressed_bytes | 12673202 |
| archive.bytes | 3297073 |
| checkpoint_tensors_included | false |

</details>

<details>
<summary>reports/phase6/story_weight_comparison_review.json — same_material_story_weights_actual200M_all160_evidence_complete</summary>

[原記録](../../reports/phase6/story_weight_comparison_review.json) ／ SHA256: `58ba73470b4e9c00cc5ddd5be48b86ffdfc5bbf4218a1965a36b70d6e5aeaf06` ／ 3,943 bytes

| 原キー | 保存値 |
|---|---|
| status | "same_material_story_weights_actual200M_all160_evidence_complete" |
| summaries.control.BPB | 1.1299213611844423 |
| summaries.control.rates.eos | 45 |
| summaries.control.rates.repetition | 16 |
| summaries.control.rates.unicode_failure | 0 |
| summaries.control.rates.role_leak | 0 |
| summaries.control.rates.empty | 0 |
| summaries.control.grammar2 | 67 |
| summaries.control.relevance2 | 49 |
| summaries.control.coherent | 11 |
| summaries.control.appropriate | 27 |
| summaries.control.new_teacher_tokens | 100000000 |
| summaries.control.source_teacher_tokens.web | 75000000 |
| summaries.control.source_teacher_tokens.textbook | 20000000 |
| summaries.control.source_teacher_tokens.story | 5000000 |
| summaries.control.notes_sha256 | "85cadffb1195ba32f3ab41e136f84003880a1813a366db2d2e9bf6f0dcf2545e" |
| summaries.control.Base_adopted | false |
| summaries.story20.BPB | 1.1352687563443153 |
| summaries.story20.rates.eos | 38 |
| summaries.story20.rates.repetition | 21 |
| summaries.story20.rates.unicode_failure | 0 |
| summaries.story20.rates.role_leak | 0 |
| summaries.story20.rates.empty | 0 |
| summaries.story20.grammar2 | 64 |
| summaries.story20.relevance2 | 47 |
| summaries.story20.coherent | 15 |
| summaries.story20.appropriate | 24 |
| summaries.story20.new_teacher_tokens | 100000000 |
| summaries.story20.source_teacher_tokens.web | 60000000 |
| summaries.story20.source_teacher_tokens.textbook | 20000000 |
| summaries.story20.source_teacher_tokens.story | 20000000 |
| summaries.story20.notes_sha256 | "c887019c091fdbb829c2a0f43e3cec7e44877d072c8017918d0112971b170371" |
| summaries.story20.Base_adopted | false |
| quality_comparison.checks.coherence_gain_at_least8 | false |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | false |
| quality_comparison.checks.repetition_nonworsening | false |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| absolute_dev_screen.control.grammar_at_least56 | true |
| absolute_dev_screen.control.coherence_at_least27 | false |
| absolute_dev_screen.control.appropriate_at_least27 | true |
| absolute_dev_screen.control.EOS_at_least37 | true |
| absolute_dev_screen.control.repetition_at_most18 | true |
| absolute_dev_screen.control.no_empty_role_unicode | true |
| absolute_dev_screen.story20.grammar_at_least56 | true |
| absolute_dev_screen.story20.coherence_at_least27 | false |
| absolute_dev_screen.story20.appropriate_at_least27 | false |
| absolute_dev_screen.story20.EOS_at_least37 | true |
| absolute_dev_screen.story20.repetition_at_most18 | false |
| absolute_dev_screen.story20.no_empty_role_unicode | true |
| original_Web.control.EOS_at_least8_more | true |
| original_Web.control.repetition_no_worse | true |
| original_Web.control.no_empty_role_unicode | true |
| original_Web.control.BPB_degradation_at_most1percent | false |
| original_Web.story20.EOS_at_least8_more | true |
| original_Web.story20.repetition_no_worse | true |
| original_Web.story20.no_empty_role_unicode | true |
| original_Web.story20.BPB_degradation_at_most1percent | false |
| eligible_for_final_Base_validation.control | false |
| eligible_for_final_Base_validation.story20 | false |
| new_scientific_teacher_tokens | 200000000 |
| verification_teacher_tokens | 2599809 |
| GPU_seconds | 453.7347566630051 |
| verification_GPU_seconds | 22.201600583008258 |
| Base_adopted | false |
| Chat_adopted | false |
| protected_test_used | false |
| requested_five_steps_complete | false |

</details>

<details>
<summary>reports/phase6/story_weight_control_notes.json — None</summary>

[原記録](../../reports/phase6/story_weight_control_notes.json) ／ SHA256: `85cadffb1195ba32f3ab41e136f84003880a1813a366db2d2e9bf6f0dcf2545e` ／ 16,723 bytes

| 原キー | 保存値 |
|---|---|
| exact_same_output_prior_notes_reused | ["base-017", "base-051", "base-062", "base-066", "base-077", "base-082"] |

</details>

<details>
<summary>reports/phase6/strategy_extension_annotations.json — None</summary>

[原記録](../../reports/phase6/strategy_extension_annotations.json) ／ SHA256: `10209a5af9fc05c67effe9f8cd5de5b8de79c49fd32087e86197317538ad0f73` ／ 35,260 bytes

| 原キー | 保存値 |
|---|---|
| review_scope | "Codex read all160 canonical64-token generations and wrote individual reasons; frozen rubric retained" |

</details>

<details>
<summary>reports/phase6/strategy_extension_eligibility.json — None</summary>

[原記録](../../reports/phase6/strategy_extension_eligibility.json) ／ SHA256: `ddfd21123762920a2b3137f1b726209ecdb54ebeb793dd8192451cd967e99422` ／ 3,537 bytes

| 原キー | 保存値 |
|---|---|
| rule.auxiliary_BPB_relative_improvement_at_least | 0.01 |
| rule.auxiliary_EOS_gain_at_least | 4 |
| rule.repetition_nonworsening | true |
| rule.no_empty_or_unicode | true |
| rule.equal_budget_pair_requires_both_strategies_eligible | true |
| rule.max_total_strategy_GPU_seconds | 1800 |
| results.before_continuation.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| results.before_continuation.checkpoint.sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| results.before_continuation.checkpoint.update | 305176 |
| results.before_continuation.checkpoint.tokens_seen | 10000007168 |
| results.before_continuation.body_bytes | 20359 |
| results.before_continuation.body_NLL | 14348.360681672217 |
| results.before_continuation.BPB | 1.0167645169377029 |
| results.before_continuation.EOS | 0 |
| results.before_continuation.empty | 0 |
| results.before_fresh.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/curriculum-strategy-20261005-v3/initial-fresh.pt" |
| results.before_fresh.checkpoint.sha256 | "70d86a832f607faf4325992b5ec76d080a167b164efc78a6dc0b88133507ea85" |
| results.before_fresh.body_bytes | 20359 |
| results.before_fresh.body_NLL | 41800.81864118576 |
| results.before_fresh.BPB | 2.96212160512489 |
| results.before_fresh.EOS | 0 |
| results.before_fresh.empty | 0 |
| results.after_continuation.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/curriculum-strategy-20261005-v3/continuation/checkpoint-00308251.pt" |
| results.after_continuation.checkpoint.sha256 | "ff1fe9689e841753e7e88cd8f7df58cdcbf6e01fe3bd038efcf60d277b284ddb" |
| results.after_continuation.body_bytes | 20359 |
| results.after_continuation.body_NLL | 12802.188450171987 |
| results.after_continuation.BPB | 0.9071984768205261 |
| results.after_continuation.EOS | 6 |
| results.after_continuation.empty | 0 |
| results.after_fresh.checkpoint.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/curriculum-strategy-20261005-v3/fresh/checkpoint-00003075.pt" |
| results.after_fresh.checkpoint.sha256 | "0d514fbc6f5ec8a512d45f1e7acabefb8b60b2408724e803ce5896288f09bae8" |
| results.after_fresh.body_bytes | 20359 |
| results.after_fresh.body_NLL | 15131.192519034248 |
| results.after_fresh.BPB | 1.0722381457805832 |
| results.after_fresh.EOS | 7 |
| results.after_fresh.empty | 0 |
| eligibility.continuation.checks.BPB | true |
| eligibility.continuation.checks.EOS | true |
| eligibility.continuation.checks.repetition | true |
| eligibility.continuation.checks.no_empty_UTF8 | true |
| eligibility.continuation.eligible | true |
| eligibility.fresh.checks.BPB | true |
| eligibility.fresh.checks.EOS | true |
| eligibility.fresh.checks.repetition | true |
| eligibility.fresh.checks.no_empty_UTF8 | true |
| eligibility.fresh.eligible | true |
| equal300M_pair_eligible | true |
| scientific_teacher_tokens | 0 |
| GPU_seconds | 16.30984483199427 |
| interpretation | "Repetition here is raw repeated4gram presence, not independently judged semantic-loop rate; eligibility is research budget only" |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/strategy_extension_review.json — verified_learning_and_content_evidence</summary>

[原記録](../../reports/phase6/strategy_extension_review.json) ／ SHA256: `daa2f2e247958d3452f5a49d68403882870fabcbe6e74616916aece8f2309c88` ／ 7,513 bytes

| 原キー | 保存値 |
|---|---|
| status | "verified_learning_and_content_evidence" |
| summaries.continuation.BPB | 1.2557731792857416 |
| summaries.continuation.rates.eos | 31 |
| summaries.continuation.rates.repetition | 5 |
| summaries.continuation.rates.unicode_failure | 1 |
| summaries.continuation.rates.role_leak | 0 |
| summaries.continuation.rates.empty | 0 |
| summaries.continuation.Japanese.semantics.seed | 42 |
| summaries.continuation.Japanese.semantics.repetitions | 2000 |
| summaries.continuation.Japanese.semantics.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.continuation.Japanese.jblimp.seed | 42 |
| summaries.continuation.Japanese.jblimp.repetitions | 2000 |
| summaries.continuation.Japanese.jblimp.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.continuation.Japanese.jcqa.seed | 42 |
| summaries.continuation.Japanese.jcqa.repetitions | 2000 |
| summaries.continuation.Japanese.jcqa.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.continuation.grammar2 | 34 |
| summaries.continuation.relevance2 | 17 |
| summaries.continuation.coherent | 8 |
| summaries.continuation.appropriate | 15 |
| summaries.continuation.auxiliary.documents | 32 |
| summaries.continuation.auxiliary.EOS | 7 |
| summaries.continuation.auxiliary.teacher_NLL | 2.2789345787954574 |
| summaries.continuation.auxiliary.teacher_top1_fraction | 0.530294233275204 |
| summaries.continuation.additional_teacher_tokens | 200000000 |
| summaries.continuation.cumulative_teacher_tokens | 300000000 |
| summaries.continuation.valid_input_tokens | 201490432 |
| summaries.continuation.physical_tokens | 201490432 |
| summaries.continuation.seconds | 304.9521164320031 |
| summaries.continuation.peak_allocated_bytes | 6149073408 |
| summaries.continuation.EOS_teachers.web | 0 |
| summaries.continuation.EOS_teachers.short | 1476083 |
| summaries.fresh.BPB | 1.6054100927035742 |
| summaries.fresh.rates.eos | 22 |
| summaries.fresh.rates.repetition | 2 |
| summaries.fresh.rates.unicode_failure | 1 |
| summaries.fresh.rates.role_leak | 0 |
| summaries.fresh.rates.empty | 0 |
| summaries.fresh.Japanese.semantics.seed | 42 |
| summaries.fresh.Japanese.semantics.repetitions | 2000 |
| summaries.fresh.Japanese.semantics.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.fresh.Japanese.jblimp.seed | 42 |
| summaries.fresh.Japanese.jblimp.repetitions | 2000 |
| summaries.fresh.Japanese.jblimp.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.fresh.Japanese.jcqa.seed | 42 |
| summaries.fresh.Japanese.jcqa.repetitions | 2000 |
| summaries.fresh.Japanese.jcqa.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.fresh.grammar2 | 27 |
| summaries.fresh.relevance2 | 15 |
| summaries.fresh.coherent | 5 |
| summaries.fresh.appropriate | 13 |
| summaries.fresh.auxiliary.documents | 32 |
| summaries.fresh.auxiliary.EOS | 7 |
| summaries.fresh.auxiliary.teacher_NLL | 2.661717681731758 |
| summaries.fresh.auxiliary.teacher_top1_fraction | 0.4922780780060575 |
| summaries.fresh.additional_teacher_tokens | 200000000 |
| summaries.fresh.cumulative_teacher_tokens | 300000000 |
| summaries.fresh.valid_input_tokens | 201490432 |
| summaries.fresh.physical_tokens | 201490432 |
| summaries.fresh.seconds | 305.4485366970039 |
| summaries.fresh.peak_allocated_bytes | 6149073408 |
| summaries.fresh.EOS_teachers.web | 0 |
| summaries.fresh.EOS_teachers.short | 1476083 |
| gates.continuation.practical.coherence_at_least27 | false |
| gates.continuation.practical.appropriate_at_least27 | false |
| gates.continuation.practical.EOS_at_least37 | false |
| gates.continuation.practical.repetition_at_most18 | true |
| gates.continuation.relative_to100M.checks.coherence_gain_at_least8 | false |
| gates.continuation.relative_to100M.checks.paired_CI_lower_above0 | false |
| gates.continuation.relative_to100M.checks.EOS_nonworsening | true |
| gates.continuation.relative_to100M.checks.repetition_nonworsening | true |
| gates.continuation.relative_to100M.checks.no_empty_role_unicode | false |
| gates.continuation.relative_to100M.checks.BPB_gate | false |
| gates.continuation.relative_to100M.checks.appropriate_completion_not_punctuation | true |
| gates.continuation.relative_to100M.passed | false |
| gates.continuation.original_Web.EOS_at_least8_more | true |
| gates.continuation.original_Web.repetition_no_worse | true |
| gates.continuation.original_Web.no_empty_role_unicode | false |
| gates.continuation.original_Web.BPB_degradation_at_most1percent | false |
| gates.continuation.adopted | false |
| gates.fresh.practical.coherence_at_least27 | false |
| gates.fresh.practical.appropriate_at_least27 | false |
| gates.fresh.practical.EOS_at_least37 | false |
| gates.fresh.practical.repetition_at_most18 | true |
| gates.fresh.relative_to100M.checks.coherence_gain_at_least8 | false |
| gates.fresh.relative_to100M.checks.paired_CI_lower_above0 | false |
| gates.fresh.relative_to100M.checks.EOS_nonworsening | true |
| gates.fresh.relative_to100M.checks.repetition_nonworsening | true |
| gates.fresh.relative_to100M.checks.no_empty_role_unicode | false |
| gates.fresh.relative_to100M.checks.BPB_gate | false |
| gates.fresh.relative_to100M.checks.appropriate_completion_not_punctuation | true |
| gates.fresh.relative_to100M.passed | false |
| gates.fresh.original_Web.EOS_at_least8_more | true |
| gates.fresh.original_Web.repetition_no_worse | true |
| gates.fresh.original_Web.no_empty_role_unicode | false |
| gates.fresh.original_Web.BPB_degradation_at_most1percent | false |
| gates.fresh.adopted | false |
| between_strategies.checks.coherence_gain_at_least8 | false |
| between_strategies.checks.paired_CI_lower_above0 | false |
| between_strategies.checks.EOS_nonworsening | true |
| between_strategies.checks.repetition_nonworsening | false |
| between_strategies.checks.no_empty_role_unicode | false |
| between_strategies.checks.BPB_gate | true |
| between_strategies.checks.appropriate_completion_not_punctuation | true |
| between_strategies.passed | false |
| scientific_teacher_tokens | 400000000 |
| cumulative_scientific_teacher_tokens | 600000000 |
| verification_teacher_tokens | 520252 |
| gpu_seconds | 839.733485528006 |
| stage3_total_GPU_seconds | 1396.455665194997 |
| decision | "No more extension in this scope; retain original UI unless all unchanged adoption gates pass" |
| interpretation | "Learning strategy comparison with staged reheat, not capacity proof or uninterrupted300M; auxiliary Web may be parent-known; official dev remains separate" |
| numerical_failures72_unchanged | true |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/strategy_scope_completion.json — complete_requested_roadmap1_to3_quality_unmet</summary>

[原記録](../../reports/phase6/strategy_scope_completion.json) ／ SHA256: `d054bb9d203f4a5be46a5b1b02950a89194526e3162f82efc3ecf07a9e357eac` ／ 3,731 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_requested_roadmap1_to3_quality_unmet" |
| stage1.job.status | "complete" |
| stage1.job.gpu_elapsed_seconds | 76.8951607140043 |
| stage1.job.scientific_teacher_tokens | 0 |
| stage1.scientific_teacher_tokens | 0 |
| stage2.train_prepared_tokens | 10000208 |
| stage2.dev_prepared_tokens | 500319 |
| stage3.teacher_tokens_per_strategy | 300000000 |
| stage3.scientific_teacher_tokens | 600000000 |
| stage3.valid_input_tokens | 604504064 |
| stage3.physical_tokens | 604504064 |
| stage3.verification_teacher_tokens | 1040748 |
| stage3.CUDA_resume_optimizer_updates | 32 |
| stage3.gpu_seconds | 1396.455665194997 |
| UI.model.training_tokens | 10000007168 |
| UI.model.update | 305176 |
| UI.model.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| UI.model.checkpoint_sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| UI.model.tokenizer_sha256 | "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318" |
| tests.generation_transfer_tests.xml.tests | 2 |
| tests.generation_transfer_tests.xml.sha256 | "c72b80eb6b05a688fd3d740d2defac959ac4de3422d9d66c2b008a08590c3f77" |
| tests.curriculum_strategy_tests.xml.tests | 5 |
| tests.curriculum_strategy_tests.xml.sha256 | "7975b104d0fc25732fd6e31e7dc34480e04c69e24a8222d55df4ea9627afc53a" |
| tests.curriculum_strategy_bootstrap_tests.xml.tests | 1 |
| tests.curriculum_strategy_bootstrap_tests.xml.sha256 | "fa98e252886f306091fdd8a0bc8d5de2d6c4411343c49d1bf93d8faaa9d2eb8a" |
| tests.strategy_extension_tests.xml.tests | 1 |
| tests.strategy_extension_tests.xml.sha256 | "f8ea4743e1d40f21d1fbfc445038572a9482e3dd2006772a3899db31900297af" |
| archive.bytes | 32891478 |
| decision | "Both300M candidates rejected under unchanged gates; original10B UI retained; architecture experiment remains a proposal" |
| old_numerical_failures72_preserved | true |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/text_display_verification.json — passed_production_display_saved400</summary>

[原記録](../../reports/phase6/text_display_verification.json) ／ SHA256: `866ebb2f45c82fe6d60d2cd24f4ce0245ee5d315dfd6cbfc4497a2861a00e3d9` ／ 2,152 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed_production_display_saved400" |
| raw_unicode_failures_retained | 2 |
| new_GPU_inference | 0 |

</details>

<details>
<summary>reports/phase6/web-kl-EOS-component-20261006/job.json — complete</summary>

[原記録](../../reports/phase6/web-kl-EOS-component-20261006/job.json) ／ SHA256: `573a9a333b32804de08649b63711b2700e40d5cf15eea5adb659c93b12f7aa47` ／ 1,025 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| CPU_budget_seconds | 180 |
| GPU_seconds | 0 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| protected_test_used | false |
| source_sha256.scripts/diagnose_web_kl_eos_component.py | "56c0bd57f149dd5011983235c7c5f6b18184fac6116ec0a76a0e9a61c98ea844" |
| source_sha256.scripts/web_kl_eos_decomposition.py | "5b60964952db3b81e8b3394bb561057b7f80dcbac08d34a9971e8a5d2125215d" |
| source_sha256.tests/test_web_kl_eos_decomposition.py | "0ce9cda43ab877868d3624fd7d41975980bea67bc4245de39a2fcabd53e63c75" |
| CPU_elapsed_seconds | 9.291952833998948 |

</details>

<details>
<summary>reports/phase6/web-kl-EOS-component-20261006/result.json — actual_CPU16_train_window_EOS_component_diagnostic_complete</summary>

[原記録](../../reports/phase6/web-kl-EOS-component-20261006/result.json) ／ SHA256: `07432ad723d2e1be2267ccd3e1633de8a50ab99ea62beb2f29ca3ff9ec4a3e93` ／ 6,327 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_CPU16_train_window_EOS_component_diagnostic_complete" |
| source_sha256.scripts/diagnose_web_kl_eos_component.py | "56c0bd57f149dd5011983235c7c5f6b18184fac6116ec0a76a0e9a61c98ea844" |
| source_sha256.scripts/web_kl_eos_decomposition.py | "5b60964952db3b81e8b3394bb561057b7f80dcbac08d34a9971e8a5d2125215d" |
| source_sha256.tests/test_web_kl_eos_decomposition.py | "0ce9cda43ab877868d3624fd7d41975980bea67bc4245de39a2fcabd53e63c75" |
| physical_input_tokens | 16384 |
| results.staged_CE.EOS_mass_KL.mean | 0.013618256547452306 |
| results.staged_CE.EOS_mass_KL.quantiles | [4.2115160210351e-14, 2.729340676561054e-07, 2.639163267845803e-06, 2.5497295664734825e-05, 4.975801787216803] |
| results.staged_CE.weighted_conditional_non_EOS_KL.mean | 0.48952366029168776 |
| results.staged_CE.weighted_conditional_non_EOS_KL.quantiles | [5.682912973087056e-06, 0.12782112431816528, 0.3287723459273261, 0.6165211421617567, 11.65251701779297] |
| results.staged_CE.parent_EOS_probability.mean | 0.0018135968412875117 |
| results.staged_CE.parent_EOS_probability.quantiles | [2.4041046914342617e-10, 1.1226483897228767e-06, 6.03755568297929e-06, 4.191233322992931e-05, 0.8292607418661353] |
| results.staged_CE.student_EOS_probability.mean | 0.01081806552018662 |
| results.staged_CE.student_EOS_probability.quantiles | [4.9655418037711394e-11, 6.73503954095807e-07, 4.049319529414161e-06, 3.22185301764926e-05, 0.9959061727267919] |
| results.staged_CE.EOS_logit_KL_derivative.mean | 0.009004468678899109 |
| results.staged_CE.EOS_logit_KL_derivative.quantiles | [-0.36903349545447856, -5.270678813847222e-06, -1.3429745997044943e-07, 4.141424613453116e-06, 0.9524116588148166] |
| results.staged_CE.EOS_gradient_position_counts.positive | 7386 |
| results.staged_CE.EOS_gradient_position_counts.negative | 8934 |
| results.staged_CE.EOS_gradient_position_counts.zero | 0 |
| results.staged_CE_parent_KL.EOS_mass_KL.mean | 0.00021607731409352093 |
| results.staged_CE_parent_KL.EOS_mass_KL.quantiles | [3.997901703588955e-15, 6.239238547843307e-08, 5.168829092284908e-07, 4.09731398490194e-06, 0.14512986684224768] |
| results.staged_CE_parent_KL.weighted_conditional_non_EOS_KL.mean | 0.029941325537571166 |
| results.staged_CE_parent_KL.weighted_conditional_non_EOS_KL.quantiles | [7.106736125815322e-07, 0.007342089288851716, 0.018262281168301316, 0.03442683572083462, 2.7042919613320526] |
| results.staged_CE_parent_KL.parent_EOS_probability.mean | 0.0018135968412875117 |
| results.staged_CE_parent_KL.parent_EOS_probability.quantiles | [2.4041046914342617e-10, 1.1226483897228767e-06, 6.03755568297929e-06, 4.191233322992931e-05, 0.8292607418661353] |
| results.staged_CE_parent_KL.student_EOS_probability.mean | 0.0016391239363889502 |
| results.staged_CE_parent_KL.student_EOS_probability.quantiles | [3.191257087459707e-10, 1.711751111712247e-06, 9.295435808464713e-06, 6.018777125860324e-05, 0.7121796456430152] |
| results.staged_CE_parent_KL.EOS_logit_KL_derivative.mean | -0.0001744729048985614 |
| results.staged_CE_parent_KL.EOS_logit_KL_derivative.quantiles | [-0.18634314001451668, 7.17768339301587e-08, 1.314351969990275e-06, 1.0075728894734274e-05, 0.20511024322139357] |
| results.staged_CE_parent_KL.EOS_gradient_position_counts.positive | 13377 |
| results.staged_CE_parent_KL.EOS_gradient_position_counts.negative | 2943 |
| results.staged_CE_parent_KL.EOS_gradient_position_counts.zero | 0 |
| CPU_elapsed_seconds | 9.290633116994286 |
| GPU_seconds | 0 |
| optimizer_updates | 0 |
| scientific_teacher_tokens | 0 |
| newly_prepared_source_tokens | 0 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| limitations | "Small overlapping train-replay window, FP32 diagnostic and shared weights; an EOS-gradient sign does not prove unique cause of free generation failure or generalization. No teacher/coefficient/temperature/order/LR/source sweep is authorized by this diagnostic." |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-20261006/probe/initial-parent-preservation.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-20261006/probe/initial-parent-preservation.json) ／ SHA256: `7e3baba2df7953d4543f1aa8dfb9201879154985b785d86eb0d487734d738771` ／ 266 bytes

| 原キー | 保存値 |
|---|---|
| parent_sampler_lineage | true |
| frozen_teacher_weights | true |
| frozen_teacher_eval_no_grad | true |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-20261006/probe/job.json — failed</summary>

[原記録](../../reports/phase6/web-kl-comparison-20261006/probe/job.json) ／ SHA256: `67b16c75104cde6d815e64ebb2f526a37c1301b436e2a7606eb12e5212d6ce7d` ／ 1,345 bytes

| 原キー | 保存値 |
|---|---|
| status | "failed" |
| GPU_elapsed_seconds | 8.727055846014991 |
| Base_adopted | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v2-20261006/probe/initial-parent-preservation.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v2-20261006/probe/initial-parent-preservation.json) ／ SHA256: `7e3baba2df7953d4543f1aa8dfb9201879154985b785d86eb0d487734d738771` ／ 266 bytes

| 原キー | 保存値 |
|---|---|
| parent_sampler_lineage | true |
| frozen_teacher_weights | true |
| frozen_teacher_eval_no_grad | true |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v2-20261006/probe/job.json — complete</summary>

[原記録](../../reports/phase6/web-kl-comparison-v2-20261006/probe/job.json) ／ SHA256: `5790b2f5ab264c721055d231f964b00ffc1f8bd7ddd2132cfd1815dfad69e79e` ／ 590 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete" |
| GPU_elapsed_seconds | 30.86147491700831 |
| Base_adopted | false |
| protected_test_used | false |
| completed_updates | 32 |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v2-20261006/probe/result.json — actual_web_KL_resume_timing_complete</summary>

[原記録](../../reports/phase6/web-kl-comparison-v2-20261006/probe/result.json) ／ SHA256: `20faa844c3eb3482491025c4044986996187b2890414099896556172210a1e29` ／ 83,751 bytes

| 原キー | 保存値 |
|---|---|
| status | "actual_web_KL_resume_timing_complete" |
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
| gate.checks.history_reference_input_tokens | true |
| gate.checks.history_reference_soft_target_body_positions | true |
| gate.checks.history_reference_ignored_positions | true |
| gate.checks.history_reference_digest | true |
| gate.checks.history_combined_student_physical_input_tokens | true |
| gate.checks.finite | true |
| gate.checks.no_reheat | true |
| gate.GPU_optimizer_updates | 8 |
| gate.verification_teacher_tokens | 261602 |
| gate.verification_reference_input_tokens | 65536 |
| gate.verification_reference_soft_positions | 65276 |
| timing.verification_teacher_tokens | 1046365 |
| timing.terminal_save_seconds | 0.18151909299194813 |
| timing.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/web-kl-comparison-v2-20261006/probe/timing/checkpoint.pt" |
| timing.checkpoint_sha256 | "8184560d4180fa030f660d609580479433a0354b1a83cb2c2bd6626ab5e2baaa" |
| timing.reference_input_tokens | 262144 |
| verification_teacher_tokens | 1307967 |
| GPU_optimizer_updates | 40 |
| scientific_teacher_tokens | 0 |
| initial_parent_preservation.parent_sampler_lineage | true |
| initial_parent_preservation.frozen_teacher_weights | true |
| initial_parent_preservation.frozen_teacher_eval_no_grad | true |
| verification_reference_input_tokens | 327680 |
| verification_reference_soft_positions | 326339 |
| GPU_seconds | 30.86147491700831 |

</details>

<details>
<summary>reports/phase6/web-kl-comparison-v2-20261006/probe/timing/latest.json — None</summary>

[原記録](../../reports/phase6/web-kl-comparison-v2-20261006/probe/timing/latest.json) ／ SHA256: `61998e6685bd53836d9851eaf8c89e8b23587d5c74161ea5453117b26236e9ee` ／ 263 bytes

| 原キー | 保存値 |
|---|---|
| update | 320467 |
| tokens_seen | 10501062656 |

</details>
