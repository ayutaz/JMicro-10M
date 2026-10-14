# 実行管理・後続準備・その他 — 21/26

[分野一覧へ](07_operations.md) ／ [台帳入口](README.md)

<details>
<summary>reports/phase6/low_rank_base_v2_review.json — fixed_rank4_and_fresh_full_control_rejected</summary>

[原記録](../../reports/phase6/low_rank_base_v2_review.json) ／ SHA256: `863ec1ecc2baf411299e8b542b7fc4480f740ae178a0fbc2210cc80bc3827c01` ／ 11,955 bytes

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
<summary>reports/phase6/low_rank_base_v2_running.json — fixed_rank4_Base_running</summary>

[原記録](../../reports/phase6/low_rank_base_v2_running.json) ／ SHA256: `2b1e3ce81ae508851aa0627183691be0b51379bc44e52a9bd4d65e68ed144c71` ／ 2,350 bytes

| 原キー | 保存値 |
|---|---|
| status | "fixed_rank4_Base_running" |
| actual_scientific_teacher_tokens_per_arm | 91641755 |
| nominal_reference_teachers_per_arm | 100000000 |
| new_scientific_teacher_tokens | 26292249 |
| GPU_seconds | 57.70230251600151 |
| GPU_ceiling_seconds | 1800 |
| probe_ceiling_seconds | 240 |
| protected_test_used | false |
| Base_complete | false |
| Base_adopted | false |
| actual_job.status | "setup" |
| actual_job.GPU_elapsed_seconds | 57.70230251600151 |
| actual_job.completed_updates | 880 |
| actual_job.total_updates | 3068 |
| actual_job.actual_teachers | 26292249 |
| actual_job.loss | 2.489757537841797 |
| teacher_count_scope | "Current arm completed updates observed at heartbeat, not final total across both arms." |
| verification_GPU_seconds | 58.92843314999482 |
| remaining_science_GPU_ceiling_seconds | 1741.0715668500052 |
| estimated_GPU_seconds_with_margin | 1144.749499059093 |
| reporting_correction | "Original launch top-level GPU_seconds/new_scientific_teacher_tokens defaulted to0 despite actual_job containing positive live progress. Raw original record/archive retained; use this observed heartbeat, not those defaults." |

</details>

<details>
<summary>reports/phase6/low_rank_base_v2_running_portable.json — None</summary>

[原記録](../../reports/phase6/low_rank_base_v2_running_portable.json) ／ SHA256: `343d218c43d659431878bbf84e6504eb703bac8e7c60c6ade6ca39ddb4af197d` ／ 1,911 bytes

| 原キー | 保存値 |
|---|---|
| files.reports/phase6/low_rank_base_v2_running.json.bytes | 2350 |
| files.configs/phase6/low_rank_base_v2_comparison.json.bytes | 19756 |
| files.reports/phase6/low_rank_base_v2_proposal.json.bytes | 3174 |
| files.reports/phase6/low_rank_base_tests.xml.bytes | 818 |
| files.reports/phase6/low_rank_base_tests.xml.sha256 | "2bcbb25dd4caae60332c675759e6be648e61c984c1156f82bd24d0274201c58f" |
| files.scripts/record_low_rank_base_milestone.py.bytes | 8721 |
| files.scripts/low_rank_base_trainer.py.bytes | 9698 |
| files.scripts/run_low_rank_base_comparison.py.bytes | 23015 |
| files.scripts/run_low_rank_base_comparison.ps1.bytes | 3100 |
| files.tests/test_low_rank_base.py.bytes | 3982 |
| files.tests/test_low_rank_base.py.sha256 | "56b12c4446246876982062367db7d3394ddb89815d1a3bca48f5ca910b1afc8a" |
| files.reports/phase6/low-rank-base-comparison-v2-20261006/job.json.bytes | 604 |

</details>

<details>
<summary>reports/phase6/lr_recovery_annotations.json — None</summary>

[原記録](../../reports/phase6/lr_recovery_annotations.json) ／ SHA256: `ace57014deedf89ccd0f45af98f28ab57ea5372dd40db58a3d93ea5008833ac9` ／ 32,624 bytes

| 原キー | 保存値 |
|---|---|
| arms.continuation.notes_sha256 | "cf0e4eaf5563417bdbb94cda73b8b7f08c8b76966f1eb54f5c352f4ab8a81bad" |
| arms.fresh.notes_sha256 | "434d617360d3d208283bcf9fddd492e2166fbcf618c34bbd95cf44e22cb0072b" |

</details>

<details>
<summary>reports/phase6/lr_recovery_continuation_notes.json — None</summary>

[原記録](../../reports/phase6/lr_recovery_continuation_notes.json) ／ SHA256: `cf0e4eaf5563417bdbb94cda73b8b7f08c8b76966f1eb54f5c352f4ab8a81bad` ／ 9,711 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/lr_recovery_evidence_manifest.json — None</summary>

[原記録](../../reports/phase6/lr_recovery_evidence_manifest.json) ／ SHA256: `3bd5355d1fc05b4fcb85822090433f6a66f894aae904fc2cc44cea728e7c30e5` ／ 8,903 bytes

| 原キー | 保存値 |
|---|---|
| bytes | 30907230 |
| limitations | "No checkpoint tensors or large shards; they remain at bound WSL paths" |

</details>

<details>
<summary>reports/phase6/lr_recovery_fresh_notes.json — None</summary>

[原記録](../../reports/phase6/lr_recovery_fresh_notes.json) ／ SHA256: `434d617360d3d208283bcf9fddd492e2166fbcf618c34bbd95cf44e22cb0072b` ／ 9,909 bytes

| 原キー | 保存値 |
|---|---|

</details>

<details>
<summary>reports/phase6/lr_recovery_review.json — stage1_evidence_complete</summary>

[原記録](../../reports/phase6/lr_recovery_review.json) ／ SHA256: `3ce404eeab1b3448242b2a453d6a8776aa842939dcd697a2d2012f51d6f73ef1` ／ 6,176 bytes

| 原キー | 保存値 |
|---|---|
| status | "stage1_evidence_complete" |
| summaries.continuation.BPB | 1.0898779879735516 |
| summaries.continuation.reheat_BPB | 1.2557731792857416 |
| summaries.continuation.BPB_relative_improvement | 0.13210601567915936 |
| summaries.continuation.rates.eos | 29 |
| summaries.continuation.rates.repetition | 11 |
| summaries.continuation.rates.unicode_failure | 0 |
| summaries.continuation.rates.role_leak | 0 |
| summaries.continuation.rates.empty | 0 |
| summaries.continuation.coherent | 4 |
| summaries.continuation.appropriate | 8 |
| summaries.continuation.practical.coherence_at_least27 | false |
| summaries.continuation.practical.appropriate_at_least27 | false |
| summaries.continuation.practical.EOS_at_least37 | false |
| summaries.continuation.practical.repetition_at_most18 | true |
| summaries.continuation.relative.checks.coherence_gain_at_least8 | false |
| summaries.continuation.relative.checks.paired_CI_lower_above0 | false |
| summaries.continuation.relative.checks.EOS_nonworsening | false |
| summaries.continuation.relative.checks.repetition_nonworsening | false |
| summaries.continuation.relative.checks.no_empty_role_unicode | true |
| summaries.continuation.relative.checks.BPB_gate | true |
| summaries.continuation.relative.checks.appropriate_completion_not_punctuation | true |
| summaries.continuation.relative.passed | false |
| summaries.continuation.original_Web.EOS_at_least8_more | true |
| summaries.continuation.original_Web.repetition_no_worse | true |
| summaries.continuation.original_Web.no_empty_role_unicode | true |
| summaries.continuation.original_Web.BPB_degradation_at_most1percent | false |
| summaries.continuation.safety_interpretation | "No increase in raw failure counts; case IDs retained, this is not proof all failures were repaired" |
| summaries.continuation.adopted | false |
| summaries.continuation.scientific_teachers | 200000000 |
| summaries.continuation.valid_input_tokens | 201490432 |
| summaries.continuation.physical_tokens | 201490432 |
| summaries.continuation.seconds | 304.88568180300354 |
| summaries.continuation.peak_allocated_bytes | 6149073408 |
| summaries.continuation.additional_EOS_teachers.web | 0 |
| summaries.continuation.additional_EOS_teachers.short | 1476083 |
| summaries.fresh.BPB | 1.6727057829400582 |
| summaries.fresh.reheat_BPB | 1.6054100927035742 |
| summaries.fresh.BPB_relative_improvement | -0.04191806849996538 |
| summaries.fresh.rates.eos | 23 |
| summaries.fresh.rates.repetition | 5 |
| summaries.fresh.rates.unicode_failure | 1 |
| summaries.fresh.rates.role_leak | 0 |
| summaries.fresh.rates.empty | 0 |
| summaries.fresh.coherent | 3 |
| summaries.fresh.appropriate | 5 |
| summaries.fresh.practical.coherence_at_least27 | false |
| summaries.fresh.practical.appropriate_at_least27 | false |
| summaries.fresh.practical.EOS_at_least37 | false |
| summaries.fresh.practical.repetition_at_most18 | true |
| summaries.fresh.relative.checks.coherence_gain_at_least8 | false |
| summaries.fresh.relative.checks.paired_CI_lower_above0 | false |
| summaries.fresh.relative.checks.EOS_nonworsening | true |
| summaries.fresh.relative.checks.repetition_nonworsening | false |
| summaries.fresh.relative.checks.no_empty_role_unicode | false |
| summaries.fresh.relative.checks.BPB_gate | false |
| summaries.fresh.relative.checks.appropriate_completion_not_punctuation | true |
| summaries.fresh.relative.passed | false |
| summaries.fresh.original_Web.EOS_at_least8_more | true |
| summaries.fresh.original_Web.repetition_no_worse | true |
| summaries.fresh.original_Web.no_empty_role_unicode | false |
| summaries.fresh.original_Web.BPB_degradation_at_most1percent | false |
| summaries.fresh.safety_interpretation | "No increase in raw failure counts; case IDs retained, this is not proof all failures were repaired" |
| summaries.fresh.adopted | false |
| summaries.fresh.scientific_teachers | 200000000 |
| summaries.fresh.valid_input_tokens | 201490432 |
| summaries.fresh.physical_tokens | 201490432 |
| summaries.fresh.seconds | 309.767266572002 |
| summaries.fresh.peak_allocated_bytes | 6149073408 |
| summaries.fresh.additional_EOS_teachers.web | 0 |
| summaries.fresh.additional_EOS_teachers.short | 1476083 |
| history.original10B.train.body_bytes | 21784 |
| history.original10B.train.BPB | 0.978310706080928 |
| history.original10B.train.EOS | 0 |
| history.original10B.dev.body_bytes | 20359 |
| history.original10B.dev.BPB | 1.0167645169377029 |
| history.original10B.dev.EOS | 0 |
| history.continuation_100M.train.body_bytes | 21784 |
| history.continuation_100M.train.BPB | 0.7708863528891515 |
| history.continuation_100M.train.EOS | 9 |
| history.continuation_100M.dev.body_bytes | 20359 |
| history.continuation_100M.dev.BPB | 0.9071984768205261 |
| history.continuation_100M.dev.EOS | 6 |
| history.fresh_100M.train.body_bytes | 21784 |
| history.fresh_100M.train.BPB | 0.8407389683443256 |
| history.fresh_100M.train.EOS | 8 |
| history.fresh_100M.dev.body_bytes | 20359 |
| history.fresh_100M.dev.BPB | 1.0722381457805832 |
| history.fresh_100M.dev.EOS | 7 |
| history.continuation_reheat300M.train.body_bytes | 21784 |
| history.continuation_reheat300M.train.BPB | 0.6583054836664534 |
| history.continuation_reheat300M.train.EOS | 10 |
| history.continuation_reheat300M.dev.body_bytes | 20359 |
| history.continuation_reheat300M.dev.BPB | 1.0168595185443636 |
| history.continuation_reheat300M.dev.EOS | 7 |
| history.fresh_reheat300M.train.body_bytes | 21784 |
| history.fresh_reheat300M.train.BPB | 0.6449052823180954 |
| history.fresh_reheat300M.train.EOS | 8 |
| history.fresh_reheat300M.dev.body_bytes | 20359 |
| history.fresh_reheat300M.dev.BPB | 1.201234604538317 |
| history.fresh_reheat300M.dev.EOS | 7 |
| scientific_teacher_tokens | 400000000 |
| verification_teacher_tokens | 520252 |
| CUDA_verification_optimizer_updates | 16 |
| gpu_seconds | 897.625938814992 |
| decision | "Proceed to distinct-source material comparison; retain original accepted UI until unchanged quality gates pass" |
| interpretation | "Exact same teacher order/state fork, entire LR scale differs10x; not proof of reheat instant-only effect or best fresh-from-zero LR" |
| numerical_failures72_unchanged | true |
| requested_five_steps_complete | false |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/matched_story_amount_1B_notes.json — complete80</summary>

[原記録](../../reports/phase6/matched_story_amount_1B_notes.json) ／ SHA256: `2de7c6d8007bb058874a31f12d9ebdc6ef79582d124c50c3bd40a7c7c825a041` ／ 12,455 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete80" |

</details>

<details>
<summary>reports/phase6/matched_story_amount_500M_notes.json — complete80</summary>

[原記録](../../reports/phase6/matched_story_amount_500M_notes.json) ／ SHA256: `e691c003e1fad6c17762eb4df0f60f0026d5a9a2d08f8c24c221d90fed6c70d9` ／ 12,200 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete80" |

</details>

<details>
<summary>reports/phase6/matched_story_amount_result.json — complete_pending_content_review</summary>

[原記録](../../reports/phase6/matched_story_amount_result.json) ／ SHA256: `a4a9703d7a1be319baf610c403d5c3ce3e805476001184d3eb1159c7ad1a113e` ／ 2,075,339 bytes

| 原キー | 保存値 |
|---|---|
| status | "complete_pending_content_review" |
| binding.parent.update | 305176 |
| binding.parent.tokens_seen | 10000007168 |
| binding.source_sha256.scripts/run_story20_budget.py | "9e1874f15c93eec841020b5fb78714a08509c4f9df79d31b1724b42e3808ade4" |
| binding.source_sha256.scripts/run_story20_budget.ps1 | "7f31cc6120b00853e3850a20617ff9bdc8bc7eeec10a394214a0028dcc7bf28a" |
| binding.source_sha256.scripts/prepare_story20_budget.py | "29cd73a6e2b3ccefa0251a63a250c8cc490c5bdb71261e3a62c9c6f7c77fc1a1" |
| binding.source_sha256.scripts/prepare_story20_budget.ps1 | "bdc4d8fbcd2ea8fe4248a7fdea03feb2b1463af18d6bd528ab196a78e752094f" |
| binding.source_sha256.scripts/review_story20_budget.py | "19170c57d31edfaa64272888bcf8dae2618192bfe7a33e3b74f9a08cd55a72a3" |
| binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| arms.fixed20.status | "complete" |
| arms.fixed20.binding.parent.update | 305176 |
| arms.fixed20.binding.parent.tokens_seen | 10000007168 |
| arms.fixed20.binding.source_sha256.scripts/run_story20_budget.py | "9e1874f15c93eec841020b5fb78714a08509c4f9df79d31b1724b42e3808ade4" |
| arms.fixed20.binding.source_sha256.scripts/run_story20_budget.ps1 | "7f31cc6120b00853e3850a20617ff9bdc8bc7eeec10a394214a0028dcc7bf28a" |
| arms.fixed20.binding.source_sha256.scripts/prepare_story20_budget.py | "29cd73a6e2b3ccefa0251a63a250c8cc490c5bdb71261e3a62c9c6f7c77fc1a1" |
| arms.fixed20.binding.source_sha256.scripts/prepare_story20_budget.ps1 | "bdc4d8fbcd2ea8fe4248a7fdea03feb2b1463af18d6bd528ab196a78e752094f" |
| arms.fixed20.binding.source_sha256.scripts/review_story20_budget.py | "19170c57d31edfaa64272888bcf8dae2618192bfe7a33e3b74f9a08cd55a72a3" |
| arms.fixed20.binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| arms.fixed20.binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| arms.fixed20.binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| arms.fixed20.binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| arms.fixed20.binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| arms.fixed20.binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| arms.fixed20.binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| arms.fixed20.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story-constant-lr-1b-20261005/fixed20/checkpoint-00335694.pt" |
| arms.fixed20.checkpoint_sha256 | "f913eda164dc024365558a9500f24fc76033dda01ebb5e4711b6baaef300137c" |
| arms.fixed20.update | 335694 |
| arms.fixed20.tokens | 11000020992 |
| arms.fixed20.additional_input_tokens | 1000013824 |
| arms.fixed20.source_tokens.web | 800063488 |
| arms.fixed20.source_tokens.short | 199950336 |
| arms.fixed20.source_eos_teachers.web | 1693843 |
| arms.fixed20.source_eos_teachers.short | 2210250 |
| arms.fixed20.sampler.kind | "eos-pilot-mixture-v1" |
| arms.fixed20.sampler.position | 30518 |
| arms.fixed20.sampler.web.seed | 42 |
| arms.fixed20.sampler.web.epoch | 0 |
| arms.fixed20.sampler.web.position | 10546944 |
| arms.fixed20.sampler.web.context | 1024 |
| arms.fixed20.sampler.web.blocks | 11939276 |
| arms.fixed20.sampler.short.seed | 42 |
| arms.fixed20.sampler.short.epoch | 3 |
| arms.fixed20.sampler.short.position | 19590 |
| arms.fixed20.sampler.short.context | 1024 |
| arms.fixed20.sampler.short.blocks | 58558 |
| arms.fixed20.sampler.source_tokens.web | 800063488 |
| arms.fixed20.sampler.source_tokens.short | 199950336 |
| arms.fixed20.sampler.source_eos.web | 1693843 |
| arms.fixed20.sampler.source_eos.short | 2210250 |
| arms.fixed20.training_seconds | 1479.5903360869997 |
| arms.fixed20.checkpoint_role | "result" |
| arms.fixed20.pool.short_updates | 6102 |
| arms.fixed20.schedule.parent_update | 305176 |
| arms.fixed20.schedule.stable_updates | 30518 |
| arms.fixed20.schedule.decay_updates | 1 |
| checkpoints.constant500M.status | "complete" |
| checkpoints.constant500M.binding.plan_sha256 | "93e08f45eaf36fb6904ac8656605d593f66ee512ba5d4da25877b9ff08f3fcdb" |
| checkpoints.constant500M.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| checkpoints.constant500M.binding.parent.sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| checkpoints.constant500M.binding.parent.update | 305176 |
| checkpoints.constant500M.binding.parent.tokens_seen | 10000007168 |
| checkpoints.constant500M.binding.implementation.src/jmicro/model.py | "2861baaf1860174fc8f7ae5da23386ae39146b8a907077bce4958a4b6b315b3a" |
| checkpoints.constant500M.binding.implementation.src/jmicro/shards.py | "9544c5a0c385f817f93510eaae6375e8c044286822fd86e333d2f07123b63e4c" |
| checkpoints.constant500M.binding.implementation.src/jmicro/training.py | "d898b9ba7d15d7e24c497c5981f3fc090894833d08f202d44ef881d0bb6f5086" |
| checkpoints.constant500M.binding.implementation.uv.lock | "29821397f48485dfa3317319da5248cb260c3963b6db4aad18276ed3ab9ce298" |
| checkpoints.constant500M.binding.source_sha256.scripts/run_matched_story_study.py | "1ae7933b4708f31ea7b2f758ee89e3c42e9382d95b21c46f1c5441dddc82dd32" |
| checkpoints.constant500M.binding.source_sha256.scripts/run_matched_story_study.ps1 | "94f7eb53169e54076a777544c73663a21a1d3e45cd55562ac055a58d091742f1" |
| checkpoints.constant500M.binding.source_sha256.scripts/review_matched_story_study.py | "439c990c4d2781937573927df08bdaef860041c78fd05f0d6afde4458351f315" |
| checkpoints.constant500M.binding.source_sha256.scripts/prepare_matched_story_pools.py | "4d7bff7106aa834180f537fc613cf7c8773851deabbfa0a0f230d8eab0a27768" |
| checkpoints.constant500M.binding.source_sha256.src/jmicro/story_quality.py | "23955328391a9361a38ba6a5a15b61c1e6e88260ff8412327611b82c171635d7" |
| checkpoints.constant500M.binding.source_sha256.scripts/run_story20_budget.py | "9e1874f15c93eec841020b5fb78714a08509c4f9df79d31b1724b42e3808ade4" |
| checkpoints.constant500M.binding.source_sha256.scripts/run_story20_budget.ps1 | "7f31cc6120b00853e3850a20617ff9bdc8bc7eeec10a394214a0028dcc7bf28a" |
| checkpoints.constant500M.binding.source_sha256.scripts/prepare_story20_budget.py | "29cd73a6e2b3ccefa0251a63a250c8cc490c5bdb71261e3a62c9c6f7c77fc1a1" |
| checkpoints.constant500M.binding.source_sha256.scripts/prepare_story20_budget.ps1 | "bdc4d8fbcd2ea8fe4248a7fdea03feb2b1463af18d6bd528ab196a78e752094f" |
| checkpoints.constant500M.binding.source_sha256.scripts/review_story20_budget.py | "19170c57d31edfaa64272888bcf8dae2618192bfe7a33e3b74f9a08cd55a72a3" |
| checkpoints.constant500M.binding.source_sha256.scripts/run_story20_low_lr.py | "68e320a7d16b468b3eec37074ae53e3489c631de95b6206d1ab6f740f2a5efb2" |
| checkpoints.constant500M.binding.source_sha256.scripts/run_story20_low_lr.ps1 | "85beea6cdcd9f36aa51c19d5eb53b5f7700e256cdec1b7bff886d7d1239a807d" |
| checkpoints.constant500M.binding.source_sha256.scripts/run_story10_low_lr.py | "5f47de181085b44bb194cb5b7ac9549008a4ead715df8007c61be73e7f336647" |
| checkpoints.constant500M.binding.source_sha256.scripts/run_story10_low_lr.ps1 | "e14c1f44205c49db8611bad88865e8fa993a9a441ec403e04a7c82b9ab2ae85f" |
| checkpoints.constant500M.binding.source_sha256.scripts/run_story10_comparison.py | "3f693393992fd18bde70f9a7d4ec16a85169857183c4c9bc503064b9a11a56a0" |
| checkpoints.constant500M.binding.source_sha256.scripts/run_story10_comparison.ps1 | "f85ff6dbee30a45aa3143ac000a9db28d6ee6f17cf2424bde01babf863feb0ea" |
| checkpoints.constant500M.binding.source_sha256.scripts/run_complete_text_comparison.py | "9d91d1d6124e62e4f40f7a99762f948186602e95cc362be10bfe03297874d8f7" |
| checkpoints.constant500M.binding.source_sha256.scripts/run_complete_text_comparison.ps1 | "7fb1a82d9450daf7f6955d56093be61cf31c25dd479e23715372b1d8db345e5b" |
| checkpoints.constant500M.binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| checkpoints.constant500M.binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| checkpoints.constant500M.binding.source_sha256.scripts/inspect_complete_text_data.py | "bf18510673c0c4352df911df850e3f598f921977cc34d580aa3fc87e8e8df626" |
| checkpoints.constant500M.binding.source_sha256.scripts/prepare_story_text.py | "ecbd5d1a320d59a318b282026b36e4b7ad9284d897169f0c57e77f6dae5c90fa" |
| checkpoints.constant500M.binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| checkpoints.constant500M.binding.source_sha256.src/jmicro/low_lr_pilot.py | "dcb6a1374c64c2852086b57a50433720b1e6b60263d5581eb742c3a1864ff64e" |
| checkpoints.constant500M.binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| checkpoints.constant500M.binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| checkpoints.constant500M.binding.source_sha256.scripts/evaluate_japanese_base.py | "9cabf705a67181b6a45eb20c1a62b69335140f2465b24ac2066f05e51ee48d02" |
| checkpoints.constant500M.binding.source_sha256.src/jmicro/japanese_evaluation.py | "8693e2a54e63c1b085b617b207cc5db618ae80af1eb7cb54133ba8b254da6801" |
| checkpoints.constant500M.binding.source_sha256.src/jmicro/readiness.py | "69a92251f4a697b551b9c3cfef9e2b992e776e2047c0331f7c43ba2331d172ea" |
| checkpoints.constant500M.binding.source_sha256.src/jmicro/evaluation_memory.py | "ba22fb7ca7ddb6633a308c2b1a32a59147ecb38e568d9f838ab032300147c6b4" |
| checkpoints.constant500M.binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| checkpoints.constant500M.binding.source_sha256.scripts/evaluate_complete_text_full.py | "9be7d2c3dda500571f9f95215021054b48708585cead582325d63e5da289dc9b" |
| checkpoints.constant500M.binding.source_sha256.scripts/evaluate_complete_text_full.ps1 | "ecd8c8e7341192ae32551c3309f7d20db8ac294c318c6c5e7c97dc8b34b3b3a5" |
| checkpoints.constant500M.binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| checkpoints.constant500M.binding.source_sha256.scripts/compare_base_10b.py | "bacea1be511e08f4d005084ad309ff840bf0b32de1650c349392aaafbd218291" |
| checkpoints.constant500M.binding.source_sha256.scripts/compare_base_5b.py | "1cf535ca7e3de85cdf5d5cf3987148b68f24602e0b10bc26ce97bca6296b14c8" |
| checkpoints.constant500M.binding.peak_lr | 0.0001 |
| checkpoints.constant500M.binding.stage | "amount" |
| checkpoints.constant500M.binding.arm | "fixed20" |
| checkpoints.constant500M.binding.short_manifest_sha256 | "213e11ddad72763ca5d1cb08b7a2c2a98a65989fe03dc194465d9ec4beec0921" |
| checkpoints.constant500M.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story-constant-lr-1b-20261005/fixed20/checkpoint-00320435.pt" |
| checkpoints.constant500M.checkpoint_sha256 | "17cb40a158c51a52e93ff31ba492067fff9c9cbebaa784da167fe036da60aad0" |
| checkpoints.constant500M.update | 320435 |
| checkpoints.constant500M.tokens | 10500014080 |
| checkpoints.constant500M.additional_input_tokens | 500006912 |
| checkpoints.constant500M.source_tokens.web | 400031744 |
| checkpoints.constant500M.source_tokens.short | 99975168 |
| checkpoints.constant500M.source_eos_teachers.web | 846893 |
| checkpoints.constant500M.source_eos_teachers.short | 1105092 |
| checkpoints.constant500M.sampler.kind | "eos-pilot-mixture-v1" |
| checkpoints.constant500M.sampler.position | 15259 |
| checkpoints.constant500M.sampler.web.seed | 42 |
| checkpoints.constant500M.sampler.web.epoch | 0 |
| checkpoints.constant500M.sampler.web.position | 10156288 |
| checkpoints.constant500M.sampler.web.context | 1024 |
| checkpoints.constant500M.sampler.web.blocks | 11939276 |
| checkpoints.constant500M.sampler.short.seed | 42 |
| checkpoints.constant500M.sampler.short.epoch | 1 |
| checkpoints.constant500M.sampler.short.position | 39074 |
| checkpoints.constant500M.sampler.short.context | 1024 |
| checkpoints.constant500M.sampler.short.blocks | 58558 |
| checkpoints.constant500M.sampler.source_tokens.web | 400031744 |
| checkpoints.constant500M.sampler.source_tokens.short | 99975168 |
| checkpoints.constant500M.sampler.source_eos.web | 846893 |
| checkpoints.constant500M.sampler.source_eos.short | 1105092 |
| checkpoints.constant500M.training_seconds | 746.5285631559964 |
| checkpoints.constant500M.learning_rate_fork.parent_base_lrs | [0.002, 0.002] |
| checkpoints.constant500M.learning_rate_fork.parent_actual_lrs | [0.0002, 0.0002] |
| checkpoints.constant500M.learning_rate_fork.new_peak_lr | 0.0001 |
| checkpoints.constant500M.learning_rate_fork.moments_weights_RNG_cursors_preserved | true |
| checkpoints.constant500M.checkpoint_role | "midpoint500M" |
| checkpoints.constant500M.pool.pool | "/home/aihub_ubuntu/jmicro-data/phase6/simple-stories-ja-budget-20261005/shards" |
| checkpoints.constant500M.pool.manifest_sha256 | "213e11ddad72763ca5d1cb08b7a2c2a98a65989fe03dc194465d9ec4beec0921" |
| checkpoints.constant500M.pool.short_updates | 6102 |
| checkpoints.constant500M.schedule.parent_update | 305176 |
| checkpoints.constant500M.schedule.stable_updates | 30518 |
| checkpoints.constant500M.schedule.decay_updates | 1 |
| checkpoints.constant500M.completed_at | "2026-10-05T06:52:46.942357Z" |
| checkpoints.constant1B.status | "complete" |
| checkpoints.constant1B.binding.plan_sha256 | "93e08f45eaf36fb6904ac8656605d593f66ee512ba5d4da25877b9ff08f3fcdb" |
| checkpoints.constant1B.binding.parent.path | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt" |
| checkpoints.constant1B.binding.parent.sha256 | "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290" |
| checkpoints.constant1B.binding.parent.update | 305176 |
| checkpoints.constant1B.binding.parent.tokens_seen | 10000007168 |
| checkpoints.constant1B.binding.implementation.src/jmicro/model.py | "2861baaf1860174fc8f7ae5da23386ae39146b8a907077bce4958a4b6b315b3a" |
| checkpoints.constant1B.binding.implementation.src/jmicro/shards.py | "9544c5a0c385f817f93510eaae6375e8c044286822fd86e333d2f07123b63e4c" |
| checkpoints.constant1B.binding.implementation.src/jmicro/training.py | "d898b9ba7d15d7e24c497c5981f3fc090894833d08f202d44ef881d0bb6f5086" |
| checkpoints.constant1B.binding.implementation.uv.lock | "29821397f48485dfa3317319da5248cb260c3963b6db4aad18276ed3ab9ce298" |
| checkpoints.constant1B.binding.source_sha256.scripts/run_matched_story_study.py | "1ae7933b4708f31ea7b2f758ee89e3c42e9382d95b21c46f1c5441dddc82dd32" |
| checkpoints.constant1B.binding.source_sha256.scripts/run_matched_story_study.ps1 | "94f7eb53169e54076a777544c73663a21a1d3e45cd55562ac055a58d091742f1" |
| checkpoints.constant1B.binding.source_sha256.scripts/review_matched_story_study.py | "439c990c4d2781937573927df08bdaef860041c78fd05f0d6afde4458351f315" |
| checkpoints.constant1B.binding.source_sha256.scripts/prepare_matched_story_pools.py | "4d7bff7106aa834180f537fc613cf7c8773851deabbfa0a0f230d8eab0a27768" |
| checkpoints.constant1B.binding.source_sha256.src/jmicro/story_quality.py | "23955328391a9361a38ba6a5a15b61c1e6e88260ff8412327611b82c171635d7" |
| checkpoints.constant1B.binding.source_sha256.scripts/run_story20_budget.py | "9e1874f15c93eec841020b5fb78714a08509c4f9df79d31b1724b42e3808ade4" |
| checkpoints.constant1B.binding.source_sha256.scripts/run_story20_budget.ps1 | "7f31cc6120b00853e3850a20617ff9bdc8bc7eeec10a394214a0028dcc7bf28a" |
| checkpoints.constant1B.binding.source_sha256.scripts/prepare_story20_budget.py | "29cd73a6e2b3ccefa0251a63a250c8cc490c5bdb71261e3a62c9c6f7c77fc1a1" |
| checkpoints.constant1B.binding.source_sha256.scripts/prepare_story20_budget.ps1 | "bdc4d8fbcd2ea8fe4248a7fdea03feb2b1463af18d6bd528ab196a78e752094f" |
| checkpoints.constant1B.binding.source_sha256.scripts/review_story20_budget.py | "19170c57d31edfaa64272888bcf8dae2618192bfe7a33e3b74f9a08cd55a72a3" |
| checkpoints.constant1B.binding.source_sha256.scripts/run_story20_low_lr.py | "68e320a7d16b468b3eec37074ae53e3489c631de95b6206d1ab6f740f2a5efb2" |
| checkpoints.constant1B.binding.source_sha256.scripts/run_story20_low_lr.ps1 | "85beea6cdcd9f36aa51c19d5eb53b5f7700e256cdec1b7bff886d7d1239a807d" |
| checkpoints.constant1B.binding.source_sha256.scripts/run_story10_low_lr.py | "5f47de181085b44bb194cb5b7ac9549008a4ead715df8007c61be73e7f336647" |
| checkpoints.constant1B.binding.source_sha256.scripts/run_story10_low_lr.ps1 | "e14c1f44205c49db8611bad88865e8fa993a9a441ec403e04a7c82b9ab2ae85f" |
| checkpoints.constant1B.binding.source_sha256.scripts/run_story10_comparison.py | "3f693393992fd18bde70f9a7d4ec16a85169857183c4c9bc503064b9a11a56a0" |
| checkpoints.constant1B.binding.source_sha256.scripts/run_story10_comparison.ps1 | "f85ff6dbee30a45aa3143ac000a9db28d6ee6f17cf2424bde01babf863feb0ea" |
| checkpoints.constant1B.binding.source_sha256.scripts/run_complete_text_comparison.py | "9d91d1d6124e62e4f40f7a99762f948186602e95cc362be10bfe03297874d8f7" |
| checkpoints.constant1B.binding.source_sha256.scripts/run_complete_text_comparison.ps1 | "7fb1a82d9450daf7f6955d56093be61cf31c25dd479e23715372b1d8db345e5b" |
| checkpoints.constant1B.binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| checkpoints.constant1B.binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| checkpoints.constant1B.binding.source_sha256.scripts/inspect_complete_text_data.py | "bf18510673c0c4352df911df850e3f598f921977cc34d580aa3fc87e8e8df626" |
| checkpoints.constant1B.binding.source_sha256.scripts/prepare_story_text.py | "ecbd5d1a320d59a318b282026b36e4b7ad9284d897169f0c57e77f6dae5c90fa" |
| checkpoints.constant1B.binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| checkpoints.constant1B.binding.source_sha256.src/jmicro/low_lr_pilot.py | "dcb6a1374c64c2852086b57a50433720b1e6b60263d5581eb742c3a1864ff64e" |
| checkpoints.constant1B.binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| checkpoints.constant1B.binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| checkpoints.constant1B.binding.source_sha256.scripts/evaluate_japanese_base.py | "9cabf705a67181b6a45eb20c1a62b69335140f2465b24ac2066f05e51ee48d02" |
| checkpoints.constant1B.binding.source_sha256.src/jmicro/japanese_evaluation.py | "8693e2a54e63c1b085b617b207cc5db618ae80af1eb7cb54133ba8b254da6801" |
| checkpoints.constant1B.binding.source_sha256.src/jmicro/readiness.py | "69a92251f4a697b551b9c3cfef9e2b992e776e2047c0331f7c43ba2331d172ea" |
| checkpoints.constant1B.binding.source_sha256.src/jmicro/evaluation_memory.py | "ba22fb7ca7ddb6633a308c2b1a32a59147ecb38e568d9f838ab032300147c6b4" |
| checkpoints.constant1B.binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| checkpoints.constant1B.binding.source_sha256.scripts/evaluate_complete_text_full.py | "9be7d2c3dda500571f9f95215021054b48708585cead582325d63e5da289dc9b" |
| checkpoints.constant1B.binding.source_sha256.scripts/evaluate_complete_text_full.ps1 | "ecd8c8e7341192ae32551c3309f7d20db8ac294c318c6c5e7c97dc8b34b3b3a5" |
| checkpoints.constant1B.binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| checkpoints.constant1B.binding.source_sha256.scripts/compare_base_10b.py | "bacea1be511e08f4d005084ad309ff840bf0b32de1650c349392aaafbd218291" |
| checkpoints.constant1B.binding.source_sha256.scripts/compare_base_5b.py | "1cf535ca7e3de85cdf5d5cf3987148b68f24602e0b10bc26ce97bca6296b14c8" |
| checkpoints.constant1B.binding.peak_lr | 0.0001 |
| checkpoints.constant1B.binding.stage | "amount" |
| checkpoints.constant1B.binding.arm | "fixed20" |
| checkpoints.constant1B.binding.short_manifest_sha256 | "213e11ddad72763ca5d1cb08b7a2c2a98a65989fe03dc194465d9ec4beec0921" |
| checkpoints.constant1B.checkpoint | "/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/story-constant-lr-1b-20261005/fixed20/checkpoint-00335694.pt" |
| checkpoints.constant1B.checkpoint_sha256 | "f913eda164dc024365558a9500f24fc76033dda01ebb5e4711b6baaef300137c" |
| checkpoints.constant1B.update | 335694 |
| checkpoints.constant1B.tokens | 11000020992 |
| checkpoints.constant1B.additional_input_tokens | 1000013824 |
| checkpoints.constant1B.source_tokens.web | 800063488 |
| checkpoints.constant1B.source_tokens.short | 199950336 |
| checkpoints.constant1B.source_eos_teachers.web | 1693843 |
| checkpoints.constant1B.source_eos_teachers.short | 2210250 |
| checkpoints.constant1B.sampler.kind | "eos-pilot-mixture-v1" |
| checkpoints.constant1B.sampler.position | 30518 |
| checkpoints.constant1B.sampler.web.seed | 42 |
| checkpoints.constant1B.sampler.web.epoch | 0 |
| checkpoints.constant1B.sampler.web.position | 10546944 |
| checkpoints.constant1B.sampler.web.context | 1024 |
| checkpoints.constant1B.sampler.web.blocks | 11939276 |
| checkpoints.constant1B.sampler.short.seed | 42 |
| checkpoints.constant1B.sampler.short.epoch | 3 |
| checkpoints.constant1B.sampler.short.position | 19590 |
| checkpoints.constant1B.sampler.short.context | 1024 |
| checkpoints.constant1B.sampler.short.blocks | 58558 |
| checkpoints.constant1B.sampler.source_tokens.web | 800063488 |
| checkpoints.constant1B.sampler.source_tokens.short | 199950336 |
| checkpoints.constant1B.sampler.source_eos.web | 1693843 |
| checkpoints.constant1B.sampler.source_eos.short | 2210250 |
| checkpoints.constant1B.training_seconds | 1479.5903360869997 |
| checkpoints.constant1B.learning_rate_fork.parent_base_lrs | [0.002, 0.002] |
| checkpoints.constant1B.learning_rate_fork.parent_actual_lrs | [0.0002, 0.0002] |
| checkpoints.constant1B.learning_rate_fork.new_peak_lr | 0.0001 |
| checkpoints.constant1B.learning_rate_fork.moments_weights_RNG_cursors_preserved | true |
| checkpoints.constant1B.checkpoint_role | "result" |
| checkpoints.constant1B.pool.pool | "/home/aihub_ubuntu/jmicro-data/phase6/simple-stories-ja-budget-20261005/shards" |
| checkpoints.constant1B.pool.manifest_sha256 | "213e11ddad72763ca5d1cb08b7a2c2a98a65989fe03dc194465d9ec4beec0921" |
| checkpoints.constant1B.pool.short_updates | 6102 |
| checkpoints.constant1B.schedule.parent_update | 305176 |
| checkpoints.constant1B.schedule.stable_updates | 30518 |
| checkpoints.constant1B.schedule.decay_updates | 1 |
| checkpoints.constant1B.completed_at | "2026-10-05T07:05:00.004128Z" |
| evaluations.constant500M.binding.parent.update | 305176 |
| evaluations.constant500M.binding.parent.tokens_seen | 10000007168 |
| evaluations.constant500M.binding.source_sha256.scripts/run_story20_budget.py | "9e1874f15c93eec841020b5fb78714a08509c4f9df79d31b1724b42e3808ade4" |
| evaluations.constant500M.binding.source_sha256.scripts/run_story20_budget.ps1 | "7f31cc6120b00853e3850a20617ff9bdc8bc7eeec10a394214a0028dcc7bf28a" |
| evaluations.constant500M.binding.source_sha256.scripts/prepare_story20_budget.py | "29cd73a6e2b3ccefa0251a63a250c8cc490c5bdb71261e3a62c9c6f7c77fc1a1" |
| evaluations.constant500M.binding.source_sha256.scripts/prepare_story20_budget.ps1 | "bdc4d8fbcd2ea8fe4248a7fdea03feb2b1463af18d6bd528ab196a78e752094f" |
| evaluations.constant500M.binding.source_sha256.scripts/review_story20_budget.py | "19170c57d31edfaa64272888bcf8dae2618192bfe7a33e3b74f9a08cd55a72a3" |
| evaluations.constant500M.binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| evaluations.constant500M.binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| evaluations.constant500M.binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| evaluations.constant500M.binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| evaluations.constant500M.binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| evaluations.constant500M.binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| evaluations.constant500M.binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| evaluations.constant500M.checkpoint_sha256 | "17cb40a158c51a52e93ff31ba492067fff9c9cbebaa784da167fe036da60aad0" |
| evaluations.constant500M.body.documents | 256 |
| evaluations.constant500M.body.limit_documents | 256 |
| evaluations.constant500M.body.body_nll | 321625.83211517334 |
| evaluations.constant500M.body.eos_nll | 576.5564105734229 |
| evaluations.constant500M.body.body_bytes | 472055 |
| evaluations.constant500M.body.body_tokens | 122343 |
| evaluations.constant500M.body.bpb | 0.982953242766938 |
| evaluations.constant500M.body.seconds | 1.4376653749932302 |
| evaluations.constant500M.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.constant500M.generation.max_new_tokens | 64 |
| evaluations.constant500M.greedy_rates.eos | 31 |
| evaluations.constant500M.greedy_rates.repetition | 21 |
| evaluations.constant500M.greedy_rates.unicode_failure | 0 |
| evaluations.constant500M.greedy_rates.role_leak | 0 |
| evaluations.constant500M.greedy_rates.empty | 0 |
| evaluations.constant500M.diagnostics.semantics.primary.accuracy.point | 0.6041666666666666 |
| evaluations.constant500M.diagnostics.semantics.primary.accuracy.ci95 | [0.5625, 0.6458333333333334] |
| evaluations.constant500M.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.constant500M.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.constant500M.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.constant500M.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.constant500M.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.constant500M.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.semantics.primary.hard_accuracy | 0.6041666666666666 |
| evaluations.constant500M.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5729166666666666 |
| evaluations.constant500M.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.609375] |
| evaluations.constant500M.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.constant500M.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.constant500M.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.constant500M.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.constant500M.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.constant500M.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.constant500M.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5729166666666666 |
| evaluations.constant500M.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5724991854024112 |
| evaluations.constant500M.diagnostics.semantics.per_token_secondary.mcc | 0.14611900125320154 |
| evaluations.constant500M.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.constant500M.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.constant500M.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.constant500M.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.constant500M.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.constant500M.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.constant500M.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.constant500M.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.constant500M.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.constant500M.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.constant500M.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.constant500M.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.constant500M.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.constant500M.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.constant500M.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.constant500M.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.constant500M.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.constant500M.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.constant500M.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.constant500M.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.constant500M.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.constant500M.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.constant500M.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.constant500M.diagnostics.jblimp.primary.accuracy.point | 0.7824773413897281 |
| evaluations.constant500M.diagnostics.jblimp.primary.accuracy.ci95 | [0.7401812688821753, 0.824773413897281] |
| evaluations.constant500M.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.constant500M.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.constant500M.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.constant500M.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.constant500M.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jblimp.primary.hard_accuracy | 0.7824773413897281 |
| evaluations.constant500M.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7280966767371602 |
| evaluations.constant500M.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6827794561933535, 0.7764350453172205] |
| evaluations.constant500M.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.constant500M.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.constant500M.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.constant500M.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.constant500M.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.constant500M.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7280966767371602 |
| evaluations.constant500M.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42132867132867136 |
| evaluations.constant500M.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.constant500M.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.constant500M.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.constant500M.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.constant500M.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.constant500M.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.constant500M.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.constant500M.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.constant500M.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.constant500M.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.constant500M.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.constant500M.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.constant500M.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.constant500M.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.constant500M.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.constant500M.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.constant500M.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.constant500M.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.constant500M.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.constant500M.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.constant500M.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.constant500M.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.constant500M.diagnostics.jblimp.raw_pair_accuracy | 0.7734138972809668 |
| evaluations.constant500M.diagnostics.jcqa.primary.accuracy.point | 0.3360142984807864 |
| evaluations.constant500M.diagnostics.jcqa.primary.accuracy.ci95 | [0.30831099195710454, 0.36193029490616624] |
| evaluations.constant500M.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.constant500M.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.constant500M.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.constant500M.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.constant500M.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jcqa.primary.hard_accuracy | 0.3360142984807864 |
| evaluations.constant500M.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3100983020554066 |
| evaluations.constant500M.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28418230563002683, 0.3378016085790885] |
| evaluations.constant500M.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.constant500M.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.constant500M.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.constant500M.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.constant500M.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.constant500M.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3100983020554066 |
| evaluations.constant500M.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.30869487153873754 |
| evaluations.constant500M.diagnostics.jcqa.per_token_secondary.mcc | 0.13748503505359425 |
| evaluations.constant500M.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.constant500M.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.constant500M.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.constant500M.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.constant500M.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.constant500M.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.constant500M.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.constant500M.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.constant500M.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.constant500M.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.constant500M.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.constant500M.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant500M.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.constant500M.diagnostics.semantic_both_contexts.correct | 21 |
| evaluations.constant500M.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.constant500M.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.constant500M.protected_test_used | false |
| evaluations.constant1B.binding.parent.update | 305176 |
| evaluations.constant1B.binding.parent.tokens_seen | 10000007168 |
| evaluations.constant1B.binding.source_sha256.scripts/run_story20_budget.py | "9e1874f15c93eec841020b5fb78714a08509c4f9df79d31b1724b42e3808ade4" |
| evaluations.constant1B.binding.source_sha256.scripts/run_story20_budget.ps1 | "7f31cc6120b00853e3850a20617ff9bdc8bc7eeec10a394214a0028dcc7bf28a" |
| evaluations.constant1B.binding.source_sha256.scripts/prepare_story20_budget.py | "29cd73a6e2b3ccefa0251a63a250c8cc490c5bdb71261e3a62c9c6f7c77fc1a1" |
| evaluations.constant1B.binding.source_sha256.scripts/prepare_story20_budget.ps1 | "bdc4d8fbcd2ea8fe4248a7fdea03feb2b1463af18d6bd528ab196a78e752094f" |
| evaluations.constant1B.binding.source_sha256.scripts/review_story20_budget.py | "19170c57d31edfaa64272888bcf8dae2618192bfe7a33e3b74f9a08cd55a72a3" |
| evaluations.constant1B.binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| evaluations.constant1B.binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| evaluations.constant1B.binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| evaluations.constant1B.binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| evaluations.constant1B.binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| evaluations.constant1B.binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| evaluations.constant1B.binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| evaluations.constant1B.checkpoint_sha256 | "f913eda164dc024365558a9500f24fc76033dda01ebb5e4711b6baaef300137c" |
| evaluations.constant1B.body.documents | 256 |
| evaluations.constant1B.body.limit_documents | 256 |
| evaluations.constant1B.body.body_nll | 321186.7243242264 |
| evaluations.constant1B.body.eos_nll | 563.7038075700402 |
| evaluations.constant1B.body.body_bytes | 472055 |
| evaluations.constant1B.body.body_tokens | 122343 |
| evaluations.constant1B.body.bpb | 0.9816112410247366 |
| evaluations.constant1B.body.seconds | 1.43507926199527 |
| evaluations.constant1B.body.teacher_scope | "body exactly once; BOS/PAD excluded, EOS loss separate" |
| evaluations.constant1B.generation.max_new_tokens | 64 |
| evaluations.constant1B.greedy_rates.eos | 35 |
| evaluations.constant1B.greedy_rates.repetition | 10 |
| evaluations.constant1B.greedy_rates.unicode_failure | 0 |
| evaluations.constant1B.greedy_rates.role_leak | 0 |
| evaluations.constant1B.greedy_rates.empty | 0 |
| evaluations.constant1B.diagnostics.semantics.primary.accuracy.point | 0.6614583333333334 |
| evaluations.constant1B.diagnostics.semantics.primary.accuracy.ci95 | [0.6041666666666666, 0.71875] |
| evaluations.constant1B.diagnostics.semantics.primary.accuracy.units | 96 |
| evaluations.constant1B.diagnostics.semantics.primary.accuracy.examples | 192 |
| evaluations.constant1B.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| evaluations.constant1B.diagnostics.semantics.primary.accuracy.seed | 42 |
| evaluations.constant1B.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| evaluations.constant1B.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.semantics.primary.hard_accuracy | 0.6614583333333334 |
| evaluations.constant1B.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5833333333333334 |
| evaluations.constant1B.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.6302083333333334] |
| evaluations.constant1B.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| evaluations.constant1B.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| evaluations.constant1B.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.constant1B.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| evaluations.constant1B.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.constant1B.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.semantics.per_token_secondary.count | 192 |
| evaluations.constant1B.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5833333333333334 |
| evaluations.constant1B.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5829260345389378 |
| evaluations.constant1B.diagnostics.semantics.per_token_secondary.mcc | 0.16699314428937317 |
| evaluations.constant1B.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.constant1B.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| evaluations.constant1B.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| evaluations.constant1B.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| evaluations.constant1B.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| evaluations.constant1B.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.constant1B.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| evaluations.constant1B.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| evaluations.constant1B.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| evaluations.constant1B.diagnostics.semantics.train_majority_accuracy | 0.5 |
| evaluations.constant1B.diagnostics.semantics.categories.negation.seed | 42 |
| evaluations.constant1B.diagnostics.semantics.categories.negation.repetitions | 2000 |
| evaluations.constant1B.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.semantics.categories.quantity.seed | 42 |
| evaluations.constant1B.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| evaluations.constant1B.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.semantics.categories.time.seed | 42 |
| evaluations.constant1B.diagnostics.semantics.categories.time.repetitions | 2000 |
| evaluations.constant1B.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.semantics.categories.comparison.seed | 42 |
| evaluations.constant1B.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| evaluations.constant1B.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.semantics.categories.coreference.seed | 42 |
| evaluations.constant1B.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| evaluations.constant1B.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.semantics.categories.causality.seed | 42 |
| evaluations.constant1B.diagnostics.semantics.categories.causality.repetitions | 2000 |
| evaluations.constant1B.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.constant1B.diagnostics.jblimp.primary.accuracy.point | 0.7824773413897281 |
| evaluations.constant1B.diagnostics.jblimp.primary.accuracy.ci95 | [0.7401812688821753, 0.8277945619335347] |
| evaluations.constant1B.diagnostics.jblimp.primary.accuracy.units | 331 |
| evaluations.constant1B.diagnostics.jblimp.primary.accuracy.examples | 331 |
| evaluations.constant1B.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| evaluations.constant1B.diagnostics.jblimp.primary.accuracy.seed | 42 |
| evaluations.constant1B.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jblimp.primary.hard_accuracy | 0.7824773413897281 |
| evaluations.constant1B.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7220543806646526 |
| evaluations.constant1B.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6737160120845922, 0.770392749244713] |
| evaluations.constant1B.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| evaluations.constant1B.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| evaluations.constant1B.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.constant1B.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| evaluations.constant1B.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jblimp.per_token_secondary.count | 331 |
| evaluations.constant1B.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7220543806646526 |
| evaluations.constant1B.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4192982456140351 |
| evaluations.constant1B.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| evaluations.constant1B.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.constant1B.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| evaluations.constant1B.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| evaluations.constant1B.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| evaluations.constant1B.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| evaluations.constant1B.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.constant1B.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| evaluations.constant1B.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| evaluations.constant1B.diagnostics.jblimp.train_majority_accuracy | null |
| evaluations.constant1B.diagnostics.jblimp.categories.island effects.seed | 42 |
| evaluations.constant1B.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jblimp.categories.binding.seed | 42 |
| evaluations.constant1B.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jblimp.categories.argument structure.seed | 42 |
| evaluations.constant1B.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| evaluations.constant1B.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| evaluations.constant1B.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| evaluations.constant1B.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jblimp.categories.morphology.seed | 42 |
| evaluations.constant1B.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| evaluations.constant1B.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| evaluations.constant1B.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| evaluations.constant1B.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jblimp.categories.control/raising.seed | 42 |
| evaluations.constant1B.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.constant1B.diagnostics.jblimp.raw_pair_accuracy | 0.7794561933534743 |
| evaluations.constant1B.diagnostics.jcqa.primary.accuracy.point | 0.34226988382484363 |
| evaluations.constant1B.diagnostics.jcqa.primary.accuracy.ci95 | [0.3145665773011618, 0.36907953529937443] |
| evaluations.constant1B.diagnostics.jcqa.primary.accuracy.units | 1119 |
| evaluations.constant1B.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| evaluations.constant1B.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| evaluations.constant1B.diagnostics.jcqa.primary.accuracy.seed | 42 |
| evaluations.constant1B.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jcqa.primary.hard_accuracy | 0.34226988382484363 |
| evaluations.constant1B.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.32439678284182305 |
| evaluations.constant1B.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2984584450402145, 0.3512064343163539] |
| evaluations.constant1B.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| evaluations.constant1B.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| evaluations.constant1B.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| evaluations.constant1B.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| evaluations.constant1B.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jcqa.per_token_secondary.count | 1119 |
| evaluations.constant1B.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.32439678284182305 |
| evaluations.constant1B.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3228231773557967 |
| evaluations.constant1B.diagnostics.jcqa.per_token_secondary.mcc | 0.15519360763145368 |
| evaluations.constant1B.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| evaluations.constant1B.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| evaluations.constant1B.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| evaluations.constant1B.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| evaluations.constant1B.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| evaluations.constant1B.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| evaluations.constant1B.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| evaluations.constant1B.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| evaluations.constant1B.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| evaluations.constant1B.diagnostics.jcqa.categories.commonsense.seed | 42 |
| evaluations.constant1B.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| evaluations.constant1B.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| evaluations.constant1B.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| evaluations.constant1B.diagnostics.semantic_both_contexts.correct | 36 |
| evaluations.constant1B.memory.maximum_observed_allocated_bytes | 275218432 |
| evaluations.constant1B.memory.maximum_observed_reserved_bytes | 13289652224 |
| evaluations.constant1B.protected_test_used | false |
| scientific_tokens | 1000013824 |
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
| resume_gate.checks.update | true |
| resume_gate.checks.spec | true |
| resume_gate.checks.lineage | true |
| resume_gate.checks.identical_finite_constant_LR_history | true |
| resume_gate.binding.parent.update | 305176 |
| resume_gate.binding.parent.tokens_seen | 10000007168 |
| resume_gate.binding.source_sha256.scripts/run_story20_budget.py | "9e1874f15c93eec841020b5fb78714a08509c4f9df79d31b1724b42e3808ade4" |
| resume_gate.binding.source_sha256.scripts/run_story20_budget.ps1 | "7f31cc6120b00853e3850a20617ff9bdc8bc7eeec10a394214a0028dcc7bf28a" |
| resume_gate.binding.source_sha256.scripts/prepare_story20_budget.py | "29cd73a6e2b3ccefa0251a63a250c8cc490c5bdb71261e3a62c9c6f7c77fc1a1" |
| resume_gate.binding.source_sha256.scripts/prepare_story20_budget.ps1 | "bdc4d8fbcd2ea8fe4248a7fdea03feb2b1463af18d6bd528ab196a78e752094f" |
| resume_gate.binding.source_sha256.scripts/review_story20_budget.py | "19170c57d31edfaa64272888bcf8dae2618192bfe7a33e3b74f9a08cd55a72a3" |
| resume_gate.binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| resume_gate.binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| resume_gate.binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| resume_gate.binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| resume_gate.binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| resume_gate.binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| resume_gate.binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| resume_gate.input_tokens | 262144 |
| resume_gate.scope | "Actual constant-LR mixed-source CUDA continuous/resumed" |
| constant_resume_gate.passed | true |
| constant_resume_gate.checks.model | true |
| constant_resume_gate.checks.optimizer | true |
| constant_resume_gate.checks.scheduler | true |
| constant_resume_gate.checks.rng | true |
| constant_resume_gate.checks.sampler | true |
| constant_resume_gate.checks.tokens | true |
| constant_resume_gate.checks.supervised_tokens | true |
| constant_resume_gate.checks.body_bytes | true |
| constant_resume_gate.checks.token_digest | true |
| constant_resume_gate.checks.update | true |
| constant_resume_gate.checks.spec | true |
| constant_resume_gate.checks.lineage | true |
| constant_resume_gate.checks.identical_finite_constant_LR_history | true |
| constant_resume_gate.binding.parent.update | 305176 |
| constant_resume_gate.binding.parent.tokens_seen | 10000007168 |
| constant_resume_gate.binding.source_sha256.scripts/run_story20_budget.py | "9e1874f15c93eec841020b5fb78714a08509c4f9df79d31b1724b42e3808ade4" |
| constant_resume_gate.binding.source_sha256.scripts/run_story20_budget.ps1 | "7f31cc6120b00853e3850a20617ff9bdc8bc7eeec10a394214a0028dcc7bf28a" |
| constant_resume_gate.binding.source_sha256.scripts/prepare_story20_budget.py | "29cd73a6e2b3ccefa0251a63a250c8cc490c5bdb71261e3a62c9c6f7c77fc1a1" |
| constant_resume_gate.binding.source_sha256.scripts/prepare_story20_budget.ps1 | "bdc4d8fbcd2ea8fe4248a7fdea03feb2b1463af18d6bd528ab196a78e752094f" |
| constant_resume_gate.binding.source_sha256.scripts/review_story20_budget.py | "19170c57d31edfaa64272888bcf8dae2618192bfe7a33e3b74f9a08cd55a72a3" |
| constant_resume_gate.binding.source_sha256.src/jmicro/coherent_units.py | "7b0e8cef7726b652f7b88187749090ded2b05042ac4c5fe076c30b5f5e637459" |
| constant_resume_gate.binding.source_sha256.scripts/prepare_coherent_text.py | "d91f65d6c469690cbb2c01971bddfad73a4b0ae61211a277fa3d522e17901149" |
| constant_resume_gate.binding.source_sha256.src/jmicro/eos_pilot.py | "84b23a04455475b598056b8973a1cf89346aa3faf766e9162fef2ff7e17dbb08" |
| constant_resume_gate.binding.source_sha256.scripts/run_eos_short_pilot.py | "7a381414bdea5b24bbbbf7532f04db743cff948fa47f60e95f65019af2d3ec3d" |
| constant_resume_gate.binding.source_sha256.scripts/run_eos_complete_100m.py | "62232fd440efbe32d65f25a3fffe8ec9fd7d7a96c74db329ddc3cc3443871a9d" |
| constant_resume_gate.binding.source_sha256.src/jmicro/tokenizer.py | "4198fd626bab96f9a613083b8f6cd175992f217fabed6202f4e600d24c3ad056" |
| constant_resume_gate.binding.source_sha256.scripts/run_eos_5b_finish.py | "e37c2fd3a32441690d94aa3f0a903b3d2b944707881177824e65b29fc81826c4" |
| constant_resume_gate.input_tokens | 262144 |
| constant_resume_gate.scope | "Actual constant-LR mixed-source CUDA continuous/resumed" |
| selection.reason | "Content condition not adopted; retained accepted story59.96M" |
| protected_test_used | false |
| GPU_seconds | 1671.758407936999 |

</details>

<details>
<summary>reports/phase6/matched_story_amount_review.json — passed</summary>

[原記録](../../reports/phase6/matched_story_amount_review.json) ／ SHA256: `c30c497f130d16f84d01d42bfacf42ce028ca134f0e285ecce417b9e6ada022f` ／ 313,696 bytes

| 原キー | 保存値 |
|---|---|
| status | "passed" |
| checks.actual_job_complete_exited_budget | true |
| checks.frozen_binding_scientific_verification_scope | true |
| checks.actual_CUDA_continuous_resumed_exact | true |
| checks.fixed20_finite_checkpoint_full_resume_hash | true |
| checks.fixed20_actual_contiguous_finite_updates | true |
| checks.fixed20_final_counters_binding_digest | true |
| checks.fixed20_actual_LR_schedule | true |
| checks.fixed20_actual_source_routes_cursors | true |
| checks.constant_LR_all30518_updates | true |
| checks.actual500M_midpoint_same_continuous_lineage | true |
| checks.learning_before_all_evaluation | true |
| checks.constant500M_checkpoint_bound_raw80 | true |
| checks.constant500M_annotations_raw_hash | true |
| checks.constant500M_all80_individual_notes | true |
| checks.constant500M_appropriate_completion_actual_EOS | true |
| checks.constant500M_common256_actual_NLL_BPB | true |
| checks.constant500M_raw_rates_recomputed | true |
| checks.constant500M_Japanese_complete_RNG_isolated | true |
| checks.constant1B_checkpoint_bound_raw80 | true |
| checks.constant1B_annotations_raw_hash | true |
| checks.constant1B_all80_individual_notes | true |
| checks.constant1B_appropriate_completion_actual_EOS | true |
| checks.constant1B_common256_actual_NLL_BPB | true |
| checks.constant1B_raw_rates_recomputed | true |
| checks.constant1B_Japanese_complete_RNG_isolated | true |
| checks.paired_fixed80_and_common_bytes_alignment | true |
| checks.paired_Japanese_IDs_semantics | true |
| checks.paired_Japanese_IDs_jblimp | true |
| checks.paired_Japanese_IDs_jcqa | true |
| summaries.constant500M.BPB | 0.982953242766938 |
| summaries.constant500M.rates.eos | 31 |
| summaries.constant500M.rates.repetition | 21 |
| summaries.constant500M.rates.unicode_failure | 0 |
| summaries.constant500M.rates.role_leak | 0 |
| summaries.constant500M.rates.empty | 0 |
| summaries.constant500M.content.grammar_score2 | 55 |
| summaries.constant500M.content.relevance_score2 | 27 |
| summaries.constant500M.content.coherence_score2 | 11 |
| summaries.constant500M.appropriate_EOS | 15 |
| summaries.constant500M.diagnostics.semantics.primary.accuracy.point | 0.6041666666666666 |
| summaries.constant500M.diagnostics.semantics.primary.accuracy.ci95 | [0.5625, 0.6458333333333334] |
| summaries.constant500M.diagnostics.semantics.primary.accuracy.units | 96 |
| summaries.constant500M.diagnostics.semantics.primary.accuracy.examples | 192 |
| summaries.constant500M.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| summaries.constant500M.diagnostics.semantics.primary.accuracy.seed | 42 |
| summaries.constant500M.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| summaries.constant500M.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.semantics.primary.hard_accuracy | 0.6041666666666666 |
| summaries.constant500M.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5729166666666666 |
| summaries.constant500M.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.609375] |
| summaries.constant500M.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| summaries.constant500M.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| summaries.constant500M.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.constant500M.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| summaries.constant500M.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.constant500M.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.semantics.per_token_secondary.count | 192 |
| summaries.constant500M.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5729166666666666 |
| summaries.constant500M.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5724991854024112 |
| summaries.constant500M.diagnostics.semantics.per_token_secondary.mcc | 0.14611900125320154 |
| summaries.constant500M.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.constant500M.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| summaries.constant500M.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| summaries.constant500M.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| summaries.constant500M.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| summaries.constant500M.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| summaries.constant500M.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| summaries.constant500M.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| summaries.constant500M.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| summaries.constant500M.diagnostics.semantics.train_majority_accuracy | 0.5 |
| summaries.constant500M.diagnostics.semantics.categories.negation.seed | 42 |
| summaries.constant500M.diagnostics.semantics.categories.negation.repetitions | 2000 |
| summaries.constant500M.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.semantics.categories.quantity.seed | 42 |
| summaries.constant500M.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| summaries.constant500M.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.semantics.categories.time.seed | 42 |
| summaries.constant500M.diagnostics.semantics.categories.time.repetitions | 2000 |
| summaries.constant500M.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.semantics.categories.comparison.seed | 42 |
| summaries.constant500M.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| summaries.constant500M.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.semantics.categories.coreference.seed | 42 |
| summaries.constant500M.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| summaries.constant500M.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.semantics.categories.causality.seed | 42 |
| summaries.constant500M.diagnostics.semantics.categories.causality.repetitions | 2000 |
| summaries.constant500M.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.constant500M.diagnostics.jblimp.primary.accuracy.point | 0.7824773413897281 |
| summaries.constant500M.diagnostics.jblimp.primary.accuracy.ci95 | [0.7401812688821753, 0.824773413897281] |
| summaries.constant500M.diagnostics.jblimp.primary.accuracy.units | 331 |
| summaries.constant500M.diagnostics.jblimp.primary.accuracy.examples | 331 |
| summaries.constant500M.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| summaries.constant500M.diagnostics.jblimp.primary.accuracy.seed | 42 |
| summaries.constant500M.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| summaries.constant500M.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jblimp.primary.hard_accuracy | 0.7824773413897281 |
| summaries.constant500M.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7280966767371602 |
| summaries.constant500M.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6827794561933535, 0.7764350453172205] |
| summaries.constant500M.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| summaries.constant500M.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| summaries.constant500M.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.constant500M.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| summaries.constant500M.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.constant500M.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jblimp.per_token_secondary.count | 331 |
| summaries.constant500M.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7280966767371602 |
| summaries.constant500M.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.42132867132867136 |
| summaries.constant500M.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| summaries.constant500M.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.constant500M.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| summaries.constant500M.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| summaries.constant500M.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| summaries.constant500M.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| summaries.constant500M.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| summaries.constant500M.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| summaries.constant500M.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| summaries.constant500M.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| summaries.constant500M.diagnostics.jblimp.train_majority_accuracy | null |
| summaries.constant500M.diagnostics.jblimp.categories.island effects.seed | 42 |
| summaries.constant500M.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| summaries.constant500M.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jblimp.categories.binding.seed | 42 |
| summaries.constant500M.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| summaries.constant500M.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jblimp.categories.argument structure.seed | 42 |
| summaries.constant500M.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| summaries.constant500M.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| summaries.constant500M.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| summaries.constant500M.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| summaries.constant500M.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| summaries.constant500M.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| summaries.constant500M.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| summaries.constant500M.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jblimp.categories.morphology.seed | 42 |
| summaries.constant500M.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| summaries.constant500M.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| summaries.constant500M.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| summaries.constant500M.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| summaries.constant500M.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| summaries.constant500M.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| summaries.constant500M.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| summaries.constant500M.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jblimp.categories.control/raising.seed | 42 |
| summaries.constant500M.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| summaries.constant500M.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.constant500M.diagnostics.jblimp.raw_pair_accuracy | 0.7734138972809668 |
| summaries.constant500M.diagnostics.jcqa.primary.accuracy.point | 0.3360142984807864 |
| summaries.constant500M.diagnostics.jcqa.primary.accuracy.ci95 | [0.30831099195710454, 0.36193029490616624] |
| summaries.constant500M.diagnostics.jcqa.primary.accuracy.units | 1119 |
| summaries.constant500M.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| summaries.constant500M.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| summaries.constant500M.diagnostics.jcqa.primary.accuracy.seed | 42 |
| summaries.constant500M.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| summaries.constant500M.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jcqa.primary.hard_accuracy | 0.3360142984807864 |
| summaries.constant500M.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.3100983020554066 |
| summaries.constant500M.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.28418230563002683, 0.3378016085790885] |
| summaries.constant500M.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| summaries.constant500M.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| summaries.constant500M.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.constant500M.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| summaries.constant500M.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.constant500M.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jcqa.per_token_secondary.count | 1119 |
| summaries.constant500M.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.3100983020554066 |
| summaries.constant500M.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.30869487153873754 |
| summaries.constant500M.diagnostics.jcqa.per_token_secondary.mcc | 0.13748503505359425 |
| summaries.constant500M.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.constant500M.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| summaries.constant500M.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| summaries.constant500M.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| summaries.constant500M.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| summaries.constant500M.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| summaries.constant500M.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| summaries.constant500M.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| summaries.constant500M.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| summaries.constant500M.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| summaries.constant500M.diagnostics.jcqa.categories.commonsense.seed | 42 |
| summaries.constant500M.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| summaries.constant500M.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant500M.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.constant500M.diagnostics.semantic_both_contexts.correct | 21 |
| summaries.constant1B.BPB | 0.9816112410247366 |
| summaries.constant1B.rates.eos | 35 |
| summaries.constant1B.rates.repetition | 10 |
| summaries.constant1B.rates.unicode_failure | 0 |
| summaries.constant1B.rates.role_leak | 0 |
| summaries.constant1B.rates.empty | 0 |
| summaries.constant1B.content.grammar_score2 | 56 |
| summaries.constant1B.content.relevance_score2 | 32 |
| summaries.constant1B.content.coherence_score2 | 19 |
| summaries.constant1B.appropriate_EOS | 20 |
| summaries.constant1B.diagnostics.semantics.primary.accuracy.point | 0.6614583333333334 |
| summaries.constant1B.diagnostics.semantics.primary.accuracy.ci95 | [0.6041666666666666, 0.71875] |
| summaries.constant1B.diagnostics.semantics.primary.accuracy.units | 96 |
| summaries.constant1B.diagnostics.semantics.primary.accuracy.examples | 192 |
| summaries.constant1B.diagnostics.semantics.primary.accuracy.unit | "family/prompt" |
| summaries.constant1B.diagnostics.semantics.primary.accuracy.seed | 42 |
| summaries.constant1B.diagnostics.semantics.primary.accuracy.repetitions | 2000 |
| summaries.constant1B.diagnostics.semantics.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.semantics.primary.hard_accuracy | 0.6614583333333334 |
| summaries.constant1B.diagnostics.semantics.per_token_secondary.accuracy.point | 0.5833333333333334 |
| summaries.constant1B.diagnostics.semantics.per_token_secondary.accuracy.ci95 | [0.5416666666666666, 0.6302083333333334] |
| summaries.constant1B.diagnostics.semantics.per_token_secondary.accuracy.units | 96 |
| summaries.constant1B.diagnostics.semantics.per_token_secondary.accuracy.examples | 192 |
| summaries.constant1B.diagnostics.semantics.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.constant1B.diagnostics.semantics.per_token_secondary.accuracy.seed | 42 |
| summaries.constant1B.diagnostics.semantics.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.constant1B.diagnostics.semantics.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.semantics.per_token_secondary.count | 192 |
| summaries.constant1B.diagnostics.semantics.per_token_secondary.hard_accuracy | 0.5833333333333334 |
| summaries.constant1B.diagnostics.semantics.per_token_secondary.macro_f1 | 0.5829260345389378 |
| summaries.constant1B.diagnostics.semantics.per_token_secondary.mcc | 0.16699314428937317 |
| summaries.constant1B.diagnostics.semantics.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.constant1B.diagnostics.semantics.unigram_control.accuracy.point | 0.5 |
| summaries.constant1B.diagnostics.semantics.unigram_control.accuracy.ci95 | [0.5, 0.5] |
| summaries.constant1B.diagnostics.semantics.unigram_control.accuracy.units | 96 |
| summaries.constant1B.diagnostics.semantics.unigram_control.accuracy.examples | 192 |
| summaries.constant1B.diagnostics.semantics.unigram_control.accuracy.unit | "family/prompt" |
| summaries.constant1B.diagnostics.semantics.unigram_control.accuracy.seed | 42 |
| summaries.constant1B.diagnostics.semantics.unigram_control.accuracy.repetitions | 2000 |
| summaries.constant1B.diagnostics.semantics.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.semantics.unigram_control.hard_accuracy | 0.5 |
| summaries.constant1B.diagnostics.semantics.train_majority_accuracy | 0.5 |
| summaries.constant1B.diagnostics.semantics.categories.negation.seed | 42 |
| summaries.constant1B.diagnostics.semantics.categories.negation.repetitions | 2000 |
| summaries.constant1B.diagnostics.semantics.categories.negation.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.semantics.categories.quantity.seed | 42 |
| summaries.constant1B.diagnostics.semantics.categories.quantity.repetitions | 2000 |
| summaries.constant1B.diagnostics.semantics.categories.quantity.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.semantics.categories.time.seed | 42 |
| summaries.constant1B.diagnostics.semantics.categories.time.repetitions | 2000 |
| summaries.constant1B.diagnostics.semantics.categories.time.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.semantics.categories.comparison.seed | 42 |
| summaries.constant1B.diagnostics.semantics.categories.comparison.repetitions | 2000 |
| summaries.constant1B.diagnostics.semantics.categories.comparison.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.semantics.categories.coreference.seed | 42 |
| summaries.constant1B.diagnostics.semantics.categories.coreference.repetitions | 2000 |
| summaries.constant1B.diagnostics.semantics.categories.coreference.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.semantics.categories.causality.seed | 42 |
| summaries.constant1B.diagnostics.semantics.categories.causality.repetitions | 2000 |
| summaries.constant1B.diagnostics.semantics.categories.causality.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.semantics.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.constant1B.diagnostics.jblimp.primary.accuracy.point | 0.7824773413897281 |
| summaries.constant1B.diagnostics.jblimp.primary.accuracy.ci95 | [0.7401812688821753, 0.8277945619335347] |
| summaries.constant1B.diagnostics.jblimp.primary.accuracy.units | 331 |
| summaries.constant1B.diagnostics.jblimp.primary.accuracy.examples | 331 |
| summaries.constant1B.diagnostics.jblimp.primary.accuracy.unit | "family/prompt" |
| summaries.constant1B.diagnostics.jblimp.primary.accuracy.seed | 42 |
| summaries.constant1B.diagnostics.jblimp.primary.accuracy.repetitions | 2000 |
| summaries.constant1B.diagnostics.jblimp.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jblimp.primary.hard_accuracy | 0.7824773413897281 |
| summaries.constant1B.diagnostics.jblimp.per_token_secondary.accuracy.point | 0.7220543806646526 |
| summaries.constant1B.diagnostics.jblimp.per_token_secondary.accuracy.ci95 | [0.6737160120845922, 0.770392749244713] |
| summaries.constant1B.diagnostics.jblimp.per_token_secondary.accuracy.units | 331 |
| summaries.constant1B.diagnostics.jblimp.per_token_secondary.accuracy.examples | 331 |
| summaries.constant1B.diagnostics.jblimp.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.constant1B.diagnostics.jblimp.per_token_secondary.accuracy.seed | 42 |
| summaries.constant1B.diagnostics.jblimp.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.constant1B.diagnostics.jblimp.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jblimp.per_token_secondary.count | 331 |
| summaries.constant1B.diagnostics.jblimp.per_token_secondary.hard_accuracy | 0.7220543806646526 |
| summaries.constant1B.diagnostics.jblimp.per_token_secondary.macro_f1 | 0.4192982456140351 |
| summaries.constant1B.diagnostics.jblimp.per_token_secondary.mcc | 0.0 |
| summaries.constant1B.diagnostics.jblimp.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.constant1B.diagnostics.jblimp.unigram_control.accuracy.point | 0.40483383685800606 |
| summaries.constant1B.diagnostics.jblimp.unigram_control.accuracy.ci95 | [0.3564954682779456, 0.45468277945619334] |
| summaries.constant1B.diagnostics.jblimp.unigram_control.accuracy.units | 331 |
| summaries.constant1B.diagnostics.jblimp.unigram_control.accuracy.examples | 331 |
| summaries.constant1B.diagnostics.jblimp.unigram_control.accuracy.unit | "family/prompt" |
| summaries.constant1B.diagnostics.jblimp.unigram_control.accuracy.seed | 42 |
| summaries.constant1B.diagnostics.jblimp.unigram_control.accuracy.repetitions | 2000 |
| summaries.constant1B.diagnostics.jblimp.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jblimp.unigram_control.hard_accuracy | 0.4773413897280967 |
| summaries.constant1B.diagnostics.jblimp.train_majority_accuracy | null |
| summaries.constant1B.diagnostics.jblimp.categories.island effects.seed | 42 |
| summaries.constant1B.diagnostics.jblimp.categories.island effects.repetitions | 2000 |
| summaries.constant1B.diagnostics.jblimp.categories.island effects.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jblimp.categories.binding.seed | 42 |
| summaries.constant1B.diagnostics.jblimp.categories.binding.repetitions | 2000 |
| summaries.constant1B.diagnostics.jblimp.categories.binding.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jblimp.categories.argument structure.seed | 42 |
| summaries.constant1B.diagnostics.jblimp.categories.argument structure.repetitions | 2000 |
| summaries.constant1B.diagnostics.jblimp.categories.argument structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jblimp.categories.ellipsis.seed | 42 |
| summaries.constant1B.diagnostics.jblimp.categories.ellipsis.repetitions | 2000 |
| summaries.constant1B.diagnostics.jblimp.categories.ellipsis.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jblimp.categories.verbal agreement.seed | 42 |
| summaries.constant1B.diagnostics.jblimp.categories.verbal agreement.repetitions | 2000 |
| summaries.constant1B.diagnostics.jblimp.categories.verbal agreement.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jblimp.categories.filler-gap.seed | 42 |
| summaries.constant1B.diagnostics.jblimp.categories.filler-gap.repetitions | 2000 |
| summaries.constant1B.diagnostics.jblimp.categories.filler-gap.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jblimp.categories.morphology.seed | 42 |
| summaries.constant1B.diagnostics.jblimp.categories.morphology.repetitions | 2000 |
| summaries.constant1B.diagnostics.jblimp.categories.morphology.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jblimp.categories.nominal structure.seed | 42 |
| summaries.constant1B.diagnostics.jblimp.categories.nominal structure.repetitions | 2000 |
| summaries.constant1B.diagnostics.jblimp.categories.nominal structure.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jblimp.categories.quantifiers.seed | 42 |
| summaries.constant1B.diagnostics.jblimp.categories.quantifiers.repetitions | 2000 |
| summaries.constant1B.diagnostics.jblimp.categories.quantifiers.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jblimp.categories.NPI licensing.seed | 42 |
| summaries.constant1B.diagnostics.jblimp.categories.NPI licensing.repetitions | 2000 |
| summaries.constant1B.diagnostics.jblimp.categories.NPI licensing.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jblimp.categories.control/raising.seed | 42 |
| summaries.constant1B.diagnostics.jblimp.categories.control/raising.repetitions | 2000 |
| summaries.constant1B.diagnostics.jblimp.categories.control/raising.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jblimp.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.constant1B.diagnostics.jblimp.raw_pair_accuracy | 0.7794561933534743 |
| summaries.constant1B.diagnostics.jcqa.primary.accuracy.point | 0.34226988382484363 |
| summaries.constant1B.diagnostics.jcqa.primary.accuracy.ci95 | [0.3145665773011618, 0.36907953529937443] |
| summaries.constant1B.diagnostics.jcqa.primary.accuracy.units | 1119 |
| summaries.constant1B.diagnostics.jcqa.primary.accuracy.examples | 1119 |
| summaries.constant1B.diagnostics.jcqa.primary.accuracy.unit | "family/prompt" |
| summaries.constant1B.diagnostics.jcqa.primary.accuracy.seed | 42 |
| summaries.constant1B.diagnostics.jcqa.primary.accuracy.repetitions | 2000 |
| summaries.constant1B.diagnostics.jcqa.primary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jcqa.primary.hard_accuracy | 0.34226988382484363 |
| summaries.constant1B.diagnostics.jcqa.per_token_secondary.accuracy.point | 0.32439678284182305 |
| summaries.constant1B.diagnostics.jcqa.per_token_secondary.accuracy.ci95 | [0.2984584450402145, 0.3512064343163539] |
| summaries.constant1B.diagnostics.jcqa.per_token_secondary.accuracy.units | 1119 |
| summaries.constant1B.diagnostics.jcqa.per_token_secondary.accuracy.examples | 1119 |
| summaries.constant1B.diagnostics.jcqa.per_token_secondary.accuracy.unit | "family/prompt" |
| summaries.constant1B.diagnostics.jcqa.per_token_secondary.accuracy.seed | 42 |
| summaries.constant1B.diagnostics.jcqa.per_token_secondary.accuracy.repetitions | 2000 |
| summaries.constant1B.diagnostics.jcqa.per_token_secondary.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jcqa.per_token_secondary.count | 1119 |
| summaries.constant1B.diagnostics.jcqa.per_token_secondary.hard_accuracy | 0.32439678284182305 |
| summaries.constant1B.diagnostics.jcqa.per_token_secondary.macro_f1 | 0.3228231773557967 |
| summaries.constant1B.diagnostics.jcqa.per_token_secondary.mcc | 0.15519360763145368 |
| summaries.constant1B.diagnostics.jcqa.per_token_secondary.confusion_ties | "first maximum; accuracy CI uses fractional credit" |
| summaries.constant1B.diagnostics.jcqa.unigram_control.accuracy.point | 0.17247542448614836 |
| summaries.constant1B.diagnostics.jcqa.unigram_control.accuracy.ci95 | [0.15102770330652368, 0.193923145665773] |
| summaries.constant1B.diagnostics.jcqa.unigram_control.accuracy.units | 1119 |
| summaries.constant1B.diagnostics.jcqa.unigram_control.accuracy.examples | 1119 |
| summaries.constant1B.diagnostics.jcqa.unigram_control.accuracy.unit | "family/prompt" |
| summaries.constant1B.diagnostics.jcqa.unigram_control.accuracy.seed | 42 |
| summaries.constant1B.diagnostics.jcqa.unigram_control.accuracy.repetitions | 2000 |
| summaries.constant1B.diagnostics.jcqa.unigram_control.accuracy.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jcqa.unigram_control.hard_accuracy | 0.17247542448614836 |
| summaries.constant1B.diagnostics.jcqa.train_majority_accuracy | 0.21179624664879357 |
| summaries.constant1B.diagnostics.jcqa.categories.commonsense.seed | 42 |
| summaries.constant1B.diagnostics.jcqa.categories.commonsense.repetitions | 2000 |
| summaries.constant1B.diagnostics.jcqa.categories.commonsense.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| summaries.constant1B.diagnostics.jcqa.limitations | "single model training seed; dev diagnostic, no practical-quality acceptance" |
| summaries.constant1B.diagnostics.semantic_both_contexts.correct | 36 |
| quality_comparison.checks.coherence_gain_at_least8 | true |
| quality_comparison.checks.paired_CI_lower_above0 | false |
| quality_comparison.checks.EOS_nonworsening | true |
| quality_comparison.checks.repetition_nonworsening | true |
| quality_comparison.checks.no_empty_role_unicode | true |
| quality_comparison.checks.BPB_gate | true |
| quality_comparison.checks.appropriate_completion_not_punctuation | true |
| quality_comparison.passed | false |
| practical.coherence_at_least27 | false |
| practical.appropriate_at_least27 | false |
| practical.EOS_at_least37 | false |
| practical.repetition_at_most18 | true |
| original_Web_gates.EOS_at_least8_more | true |
| original_Web_gates.repetition_no_worse | true |
| original_Web_gates.no_empty_role_unicode | true |
| original_Web_gates.BPB_degradation_at_most1percent | false |
| paired_diagnostics.semantics.point | 0.057291666666666664 |
| paired_diagnostics.semantics.ci95 | [0.015625, 0.10416666666666667] |
| paired_diagnostics.semantics.units | 96 |
| paired_diagnostics.semantics.examples | 192 |
| paired_diagnostics.semantics.unit | "family/prompt" |
| paired_diagnostics.semantics.seed | 42 |
| paired_diagnostics.semantics.repetitions | 2000 |
| paired_diagnostics.semantics.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics.jblimp.point | 0.0 |
| paired_diagnostics.jblimp.ci95 | [-0.027190332326283987, 0.02416918429003021] |
| paired_diagnostics.jblimp.units | 331 |
| paired_diagnostics.jblimp.examples | 331 |
| paired_diagnostics.jblimp.unit | "family/prompt" |
| paired_diagnostics.jblimp.seed | 42 |
| paired_diagnostics.jblimp.repetitions | 2000 |
| paired_diagnostics.jblimp.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| paired_diagnostics.jcqa.point | 0.006255585344057194 |
| paired_diagnostics.jcqa.ci95 | [-0.00804289544235925, 0.021447721179624665] |
| paired_diagnostics.jcqa.units | 1119 |
| paired_diagnostics.jcqa.examples | 1119 |
| paired_diagnostics.jcqa.unit | "family/prompt" |
| paired_diagnostics.jcqa.seed | 42 |
| paired_diagnostics.jcqa.repetitions | 2000 |
| paired_diagnostics.jcqa.note | "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI" |
| eligible_for_full | false |
| checked_at | "2026-10-05T07:10:01.000193Z" |
| protected_test_used | false |

</details>

<details>
<summary>reports/phase6/matched_story_categories.json — both_studies_complete</summary>

[原記録](../../reports/phase6/matched_story_categories.json) ／ SHA256: `9e653dd72b2c7ab0db8f42e264cf78bf3ee14414d998948f642b05af881cf4d4` ／ 12,125 bytes

| 原キー | 保存値 |
|---|---|
| status | "both_studies_complete" |
| stage2.constant1B.generation.grammar.relevance2 | 6 |
| stage2.constant1B.generation.grammar.coherence2 | 2 |
| stage2.constant1B.generation.grammar.count | 8 |
| stage2.constant1B.generation.grammar.naturalEOS | 4 |
| stage2.constant1B.generation.grammar.appropriate | 3 |
| stage2.constant1B.generation.short_story.relevance2 | 3 |
| stage2.constant1B.generation.short_story.coherence2 | 2 |
| stage2.constant1B.generation.short_story.naturalEOS | 6 |
| stage2.constant1B.generation.short_story.appropriate | 3 |
| stage2.constant1B.generation.local_context.relevance2 | 1 |
| stage2.constant1B.generation.local_context.coherence2 | 0 |
| stage2.constant1B.generation.local_context.naturalEOS | 5 |
| stage2.constant1B.generation.local_context.appropriate | 1 |
| stage2.constant1B.generation.common_sense.relevance2 | 3 |
| stage2.constant1B.generation.common_sense.coherence2 | 3 |
| stage2.constant1B.generation.common_sense.naturalEOS | 4 |
| stage2.constant1B.generation.common_sense.appropriate | 3 |
| stage2.constant1B.generation.conversation.relevance2 | 1 |
| stage2.constant1B.generation.conversation.coherence2 | 1 |
| stage2.constant1B.generation.conversation.naturalEOS | 4 |
| stage2.constant1B.generation.conversation.appropriate | 2 |
| stage2.constant1B.generation.punctuation.relevance2 | 4 |
| stage2.constant1B.generation.punctuation.coherence2 | 3 |
| stage2.constant1B.generation.punctuation.naturalEOS | 4 |
| stage2.constant1B.generation.punctuation.appropriate | 3 |
| stage2.constant1B.generation.daily.relevance2 | 6 |
| stage2.constant1B.generation.daily.coherence2 | 3 |
| stage2.constant1B.generation.daily.naturalEOS | 1 |
| stage2.constant1B.generation.daily.appropriate | 1 |
| stage2.constant1B.generation.proper_names.relevance2 | 3 |
| stage2.constant1B.generation.proper_names.coherence2 | 1 |
| stage2.constant1B.generation.proper_names.naturalEOS | 2 |
| stage2.constant1B.generation.proper_names.appropriate | 1 |
| stage2.constant1B.generation.numbers.relevance2 | 0 |
| stage2.constant1B.generation.numbers.coherence2 | 0 |
| stage2.constant1B.generation.numbers.naturalEOS | 2 |
| stage2.constant1B.generation.numbers.appropriate | 0 |
| stage2.constant1B.generation.description.relevance2 | 5 |
| stage2.constant1B.generation.description.coherence2 | 4 |
| stage2.constant1B.generation.description.naturalEOS | 3 |
| stage2.constant1B.generation.description.appropriate | 3 |
| stage2.constant1B.semantic.causality.accuracy | 0.84375 |
| stage2.constant1B.semantic.time.accuracy | 0.4375 |
| stage2.constant1B.semantic.quantity.accuracy | 0.625 |
| stage2.constant1B.semantic.negation.accuracy | 1.0 |
| stage2.constant1B.semantic.coreference.accuracy | 0.5625 |
| stage2.constant1B.semantic.comparison.accuracy | 0.5 |
| stage2.constant500M.generation.grammar.relevance2 | 3 |
| stage2.constant500M.generation.grammar.coherence2 | 0 |
| stage2.constant500M.generation.grammar.count | 8 |
| stage2.constant500M.generation.grammar.naturalEOS | 4 |
| stage2.constant500M.generation.grammar.appropriate | 1 |
| stage2.constant500M.generation.short_story.relevance2 | 2 |
| stage2.constant500M.generation.short_story.coherence2 | 1 |
| stage2.constant500M.generation.short_story.naturalEOS | 4 |
| stage2.constant500M.generation.short_story.appropriate | 2 |
| stage2.constant500M.generation.local_context.relevance2 | 0 |
| stage2.constant500M.generation.local_context.coherence2 | 0 |
| stage2.constant500M.generation.local_context.naturalEOS | 2 |
| stage2.constant500M.generation.local_context.appropriate | 0 |
| stage2.constant500M.generation.common_sense.relevance2 | 1 |
| stage2.constant500M.generation.common_sense.coherence2 | 0 |
| stage2.constant500M.generation.common_sense.naturalEOS | 2 |
| stage2.constant500M.generation.common_sense.appropriate | 0 |
| stage2.constant500M.generation.conversation.relevance2 | 4 |
| stage2.constant500M.generation.conversation.coherence2 | 3 |
| stage2.constant500M.generation.conversation.naturalEOS | 7 |
| stage2.constant500M.generation.conversation.appropriate | 4 |
| stage2.constant500M.generation.punctuation.relevance2 | 2 |
| stage2.constant500M.generation.punctuation.coherence2 | 2 |
| stage2.constant500M.generation.punctuation.naturalEOS | 3 |
| stage2.constant500M.generation.punctuation.appropriate | 3 |
| stage2.constant500M.generation.daily.relevance2 | 6 |
| stage2.constant500M.generation.daily.coherence2 | 1 |
| stage2.constant500M.generation.daily.naturalEOS | 1 |
| stage2.constant500M.generation.daily.appropriate | 1 |
| stage2.constant500M.generation.proper_names.relevance2 | 5 |
| stage2.constant500M.generation.proper_names.coherence2 | 1 |
| stage2.constant500M.generation.proper_names.naturalEOS | 3 |
| stage2.constant500M.generation.proper_names.appropriate | 1 |
| stage2.constant500M.generation.numbers.relevance2 | 0 |
| stage2.constant500M.generation.numbers.coherence2 | 0 |
| stage2.constant500M.generation.numbers.naturalEOS | 1 |
| stage2.constant500M.generation.numbers.appropriate | 0 |
| stage2.constant500M.generation.description.relevance2 | 4 |
| stage2.constant500M.generation.description.coherence2 | 3 |
| stage2.constant500M.generation.description.naturalEOS | 4 |
| stage2.constant500M.generation.description.appropriate | 3 |
| stage2.constant500M.semantic.causality.accuracy | 0.5 |
| stage2.constant500M.semantic.time.accuracy | 0.5 |
| stage2.constant500M.semantic.quantity.accuracy | 0.53125 |
| stage2.constant500M.semantic.negation.accuracy | 1.0 |
| stage2.constant500M.semantic.coreference.accuracy | 0.59375 |
| stage2.constant500M.semantic.comparison.accuracy | 0.5 |
| stage1.control.generation.numbers.appropriate | 0 |
| stage1.control.generation.numbers.coherence2 | 0 |
| stage1.control.generation.numbers.naturalEOS | 1 |
| stage1.control.generation.numbers.relevance2 | 0 |
| stage1.control.generation.daily.appropriate | 2 |
| stage1.control.generation.daily.coherence2 | 2 |
| stage1.control.generation.daily.naturalEOS | 4 |
| stage1.control.generation.daily.relevance2 | 4 |
| stage1.control.generation.short_story.appropriate | 1 |
| stage1.control.generation.short_story.coherence2 | 1 |
| stage1.control.generation.short_story.naturalEOS | 6 |
| stage1.control.generation.short_story.relevance2 | 2 |
| stage1.control.generation.proper_names.appropriate | 1 |
| stage1.control.generation.proper_names.coherence2 | 1 |
| stage1.control.generation.proper_names.naturalEOS | 3 |
| stage1.control.generation.proper_names.relevance2 | 3 |
| stage1.control.generation.local_context.appropriate | 0 |
| stage1.control.generation.local_context.coherence2 | 0 |
| stage1.control.generation.local_context.naturalEOS | 6 |
| stage1.control.generation.local_context.relevance2 | 0 |
| stage1.control.generation.conversation.appropriate | 3 |
| stage1.control.generation.conversation.coherence2 | 3 |
| stage1.control.generation.conversation.naturalEOS | 6 |
| stage1.control.generation.conversation.relevance2 | 3 |
| stage1.control.generation.punctuation.appropriate | 3 |
| stage1.control.generation.punctuation.coherence2 | 2 |
| stage1.control.generation.punctuation.naturalEOS | 3 |
| stage1.control.generation.punctuation.relevance2 | 3 |
| stage1.control.generation.grammar.count | 8 |
| stage1.control.generation.grammar.appropriate | 1 |
| stage1.control.generation.grammar.coherence2 | 0 |
| stage1.control.generation.grammar.naturalEOS | 4 |
| stage1.control.generation.grammar.relevance2 | 5 |
| stage1.control.generation.description.appropriate | 3 |
| stage1.control.generation.description.coherence2 | 2 |
| stage1.control.generation.description.naturalEOS | 4 |
| stage1.control.generation.description.relevance2 | 4 |
| stage1.control.generation.common_sense.appropriate | 0 |
| stage1.control.generation.common_sense.coherence2 | 0 |
| stage1.control.generation.common_sense.naturalEOS | 2 |
| stage1.control.generation.common_sense.relevance2 | 1 |
| stage1.control.semantic.time.accuracy | 0.5 |
| stage1.control.semantic.quantity.accuracy | 0.5 |
| stage1.control.semantic.comparison.accuracy | 0.5 |
| stage1.control.semantic.causality.accuracy | 0.78125 |
| stage1.control.semantic.negation.accuracy | 1.0 |
| stage1.control.semantic.coreference.accuracy | 0.625 |
| stage1.refined.generation.numbers.appropriate | 0 |
| stage1.refined.generation.numbers.coherence2 | 0 |
| stage1.refined.generation.numbers.naturalEOS | 1 |
| stage1.refined.generation.numbers.relevance2 | 0 |
| stage1.refined.generation.daily.appropriate | 4 |
| stage1.refined.generation.daily.coherence2 | 3 |
| stage1.refined.generation.daily.naturalEOS | 6 |
| stage1.refined.generation.daily.relevance2 | 6 |
| stage1.refined.generation.short_story.appropriate | 2 |
| stage1.refined.generation.short_story.coherence2 | 1 |
| stage1.refined.generation.short_story.naturalEOS | 5 |
| stage1.refined.generation.short_story.relevance2 | 3 |
| stage1.refined.generation.proper_names.appropriate | 1 |
| stage1.refined.generation.proper_names.coherence2 | 1 |
| stage1.refined.generation.proper_names.naturalEOS | 3 |
| stage1.refined.generation.proper_names.relevance2 | 4 |
| stage1.refined.generation.local_context.appropriate | 0 |
| stage1.refined.generation.local_context.coherence2 | 0 |
| stage1.refined.generation.local_context.naturalEOS | 7 |
| stage1.refined.generation.local_context.relevance2 | 0 |
| stage1.refined.generation.conversation.appropriate | 1 |
| stage1.refined.generation.conversation.coherence2 | 1 |
| stage1.refined.generation.conversation.naturalEOS | 4 |
| stage1.refined.generation.conversation.relevance2 | 1 |
| stage1.refined.generation.punctuation.appropriate | 2 |
| stage1.refined.generation.punctuation.coherence2 | 1 |
| stage1.refined.generation.punctuation.naturalEOS | 3 |
| stage1.refined.generation.punctuation.relevance2 | 2 |
| stage1.refined.generation.grammar.count | 8 |
| stage1.refined.generation.grammar.appropriate | 2 |
| stage1.refined.generation.grammar.coherence2 | 0 |
| stage1.refined.generation.grammar.naturalEOS | 6 |
| stage1.refined.generation.grammar.relevance2 | 3 |
| stage1.refined.generation.description.appropriate | 3 |
| stage1.refined.generation.description.coherence2 | 4 |
| stage1.refined.generation.description.naturalEOS | 5 |
| stage1.refined.generation.description.relevance2 | 3 |
| stage1.refined.generation.common_sense.appropriate | 0 |
| stage1.refined.generation.common_sense.coherence2 | 0 |
| stage1.refined.generation.common_sense.naturalEOS | 4 |
| stage1.refined.generation.common_sense.relevance2 | 1 |
| stage1.refined.semantic.time.accuracy | 0.5 |
| stage1.refined.semantic.quantity.accuracy | 0.5 |
| stage1.refined.semantic.comparison.accuracy | 0.5 |
| stage1.refined.semantic.causality.accuracy | 0.65625 |
| stage1.refined.semantic.negation.accuracy | 1.0 |
| stage1.refined.semantic.coreference.accuracy | 0.625 |
| interpretation | "Descriptive fixed dev breakdown; no new gate or independent validation." |

</details>
