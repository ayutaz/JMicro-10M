# 文書一覧

2026-10-13 JST 計画更新: 最新の課題解決方法と計画を[計画135](135_chat_problem_solution_plan.md)に整理した。教材の汎化改善を第一比較、正しい履歴での改善後に誤履歴回復、paddingを別の効率比較とする。既存D1準備の小記録はTRAIN40,126 target・固定280sample問題0・CPU消費チェック合格を示すが、独立人間確認・新DEV・CUDA gate・学習・品質は未確認。今回の依頼では計画と記録のみを更新し、新しい教材生成・GPU実験・学習は開始しない。Base/Chat未完成・未採用、10Mと元の品質基準を維持する。

2026-10-12 最終状態: 計画131の段階0–5の学習・全評価・結果報告を終え、C0/C1とも不合格で閉鎖。各1,899,555 Assistant本文+EOT教師、全14suite・3,066内容判断、固定NLL7点を確認した。最終新DEVの文法・関連性同時2はC0 11/80、C1 15/80（必要56）、自己生成最終文脈2は4/24、2/24（必要15）。GPU累積70.794分/6時間上限。合格候補がなく保持/samplingは条件付き省略・品質未確認。Base/Chat未完成・未採用。元10B UIを復帰。追加実験は停止し、[結果132](132_chat_improvement_execution.md)と[次の未実行計画133](133_chat_generalization_followup_plan.md)を参照する。

[完了監査](../reports/phase7/chat-improvement-20261012/completion.json)。以下の調査・事前計画・過去実験の記述は各時点の履歴で、現在の開始指示ではない。

## 過去の計画と経緯

最新計画: [課題への対策と段階計画131](131_chat_improvement_execution_plan.md)。問題と対策、段階0–5、2条件・約1.9M教師/条件、GPU6時間案、新旧DEVの原gate、結果報告での停止と後続分岐を具体化しました。[計画作成時の静的確認](../reports/investigation/chat_improvement_plan_20261012/verification.json)。

2026-10-12最新調査: [Chat-first SFTの問題点と改善方法130](130_chat_failure_improvement_investigation.md)。保存済みの失敗・実装・公開研究を調べ、教材改善、自生成履歴回復、未使用評価の順で提案した。[再集計と出典](../reports/investigation/chat_improvement_20261012/README.md)。新しい学習・GPU診断・教材準備は未開始。

2026-10-10の実行完了記録: ユーザーの「5まで進めてください」に基づく[Chat-first計画128](128_chat_first_sft_plan.md)の限定実行を完了しました。1条件のSFT3周と全4条件876内容確認・paired比較まで実施し、全候補不合格で停止しています。[実行・結果129](129_chat_first_sft_execution.md)、[完了監査](../reports/phase7/chat-first-sft-20261010/completion.json)。Base/Chatは未完成・未採用。sampling/保持/手動5会話は合格候補なしの事前条件により省略しました。

10M維持（現10,001,152 parameters、9.5M〜10.1M予算）、元UI・Tokenizer・重み・旧証拠を保全します。追加学習、比較、量子化、公開は未再開。[調査127](127_rebuild_investigation.md)、[Base復旧計画124](124_base_recovery_plan.md)、[モデル保存126](126_model_archive.md)も保持します。
## 読む順序

最初に[最新結果132](132_chat_improvement_execution.md)と[次の未実行計画133](133_chat_generalization_followup_plan.md)を読む。以下の128/129/130/131は、その結果に至る経緯と事前登録。


最新の[Chat-first SFT計画128](128_chat_first_sft_plan.md): 親モデル、準備済み会話の正確な量、Assistant本文+EOT、専用診断入口、学習前後/自生成履歴/保持の評価、時間上限と停止。従来のBase-first順序に対する限定診断の計画で、Base/Chat採用とは区別します。

2026-10-10の[作り直す前の調査127](127_rebuild_investigation.md): 参考Akebonoの公開実装・評価、前回の失敗原因の確度、再利用する基盤と再構築順序。公開資料と既存結果の調査で、新しい学習や推論評価は行っていません。

経緯をまとめて読む場合は[調査・検証・学習の全体記録125](125_project_retrospective.md)から始め、数値・失敗・採否を調べる場合は[詳細台帳](retrospective/README.md)を参照してください。

1. [現在の状態](autonomous_status.md): 実際の成果、未達、停止境界、processと保存先。
2. [最新結果123](123_base_teacher_decay_2b_results.md): 同native2B比較、全80、BPB改善と文章品質未改善、採否。
3. [今後の計画124](124_base_recovery_plan.md): 再開後の目的・ゴール・進行/停止条件・予算。
4. [ロードマップ](15_project_roadmap.md): Phase0〜10の現在地と元品質条件。
5. [Windows/WSL引継ぎ](windows_handoff.md): uv、Git外の重み/data、元UI、復元と再開。
6. [チェックリスト](10_next_steps.md)、[評価契約](evaluation_protocol.md)、[実験の探し方](base_experiment_lookup.md)。

番号付き文書は原則として作成時点の計画・結果です。古い「次回」「未開始」「実行中」は現在の状態や新しい開始指示ではありません。最新の実状態はstatus、各runの採否は原completionを参照します。準備コード、CPU tests、学習終了、Base採用を区別します。

## 運用文書と履歴

- [作業ルール](../AGENTS.md)、[自律runner](codex_automation.md)、[固定pilot/Tokenizer復元](huggingface_handoff.md)。
- [旧状態の全原文](autonomous_status_history_20261008.md)、[旧ロードマップの全原文](project_roadmap_history_20261008.md)、[旧引継ぎの全原文](windows_handoff_history_20261008.md)、[旧AGENTSの全原文](agents_history_20261008.md)。
- [2026-10-05履歴](autonomous_history_20261005.md)、[2026-10-04履歴](autonomous_history_20261004.md)、[2026-10-03履歴](autonomous_history_20261003.md)。
- [data](../data/README.md)、[eval](../eval/README.md)、[reports](../reports/README.md)。

旧運用文書は今回の整理前のbytesをそのまま保存しています。凍結report/source/raw、Phase0〜3の証拠は変更していません。native seedの[準備122](122_base_native_seed_confirmation_preparation.md)はCPU準備のみで、候補の後続不採用は結果123を参照します。

## 番号付きの計画・結果

| 文書 | 作成時点の主題 |
|---|---|
| [01_project_goal.md](01_project_goal.md) | プロジェクト目的 |
| [02_research_summary.md](02_research_summary.md) | 調査要約 |
| [03_architecture.md](03_architecture.md) | アーキテクチャ設計 |
| [04_tokenizer.md](04_tokenizer.md) | Tokenizer設計 |
| [05_dataset.md](05_dataset.md) | データ設計 |
| [06_training_plan.md](06_training_plan.md) | 学習計画 |
| [07_environment.md](07_environment.md) | 実行環境とデータ配置 |
| [08_evaluation.md](08_evaluation.md) | 評価・Checkpoint・TDD |
| [09_prior_art_and_baselines.md](09_prior_art_and_baselines.md) | 先行例とベースライン |
| [10_next_steps.md](10_next_steps.md) | 現在のチェックリスト |
| [11_technical_research_gaps.md](11_technical_research_gaps.md) | 未解決の技術課題と追加調査 |
| [12_training_implementation_research.md](12_training_implementation_research.md) | モデル実装・段階学習・実行環境の追加調査 |
| [13_tokenizer_dialogue_data_research.md](13_tokenizer_dialogue_data_research.md) | Tokenizer・日本語会話データ・SFTの追加調査 |
| [14_evaluation_deployment_research.md](14_evaluation_deployment_research.md) | 比較評価・量子化・ローカル推論の追加調査 |
| [15_project_roadmap.md](15_project_roadmap.md) | JMicro-10M フェーズ別実行計画 |
| [16_phase0_completion.md](16_phase0_completion.md) | Phase 0 完了記録 |
| [17_phase1_completion.md](17_phase1_completion.md) | Phase 1 完了記録 |
| [18_phase2_completion.md](18_phase2_completion.md) | Phase 2完了記録 |
| [19_phase3_completion.md](19_phase3_completion.md) | Phase 3完了記録 |
| [20_publication_review.md](20_publication_review.md) | Hugging Face公開前のライセンス・個人情報確認 |
| [21_phase4_completion.md](21_phase4_completion.md) | Phase 4完了: WSL・学習器・再開・4090実測 |
| [22_phase5_plan.md](22_phase5_plan.md) | Phase 5: 目的・ゴール・実行計画 |
| [23_phase5_completion.md](23_phase5_completion.md) | Phase 5完了: 小予算の学習検証と候補選定 |
| [24_phase6_plan.md](24_phase6_plan.md) | Phase 6 Base学習の現在地と進行条件 |
| [25_phase6_preparation.md](25_phase6_preparation.md) | Phase 6の①データ拡充・②長時間学習準備 |
| [26_phase6_preparation_completion.md](26_phase6_preparation_completion.md) | Phase 6①②の完了記録 |
| [27_phase6_remaining_plan.md](27_phase6_remaining_plan.md) | Phase 6以降に残る作業 |
| [28_phase6_performance.md](28_phase6_performance.md) | Phase 6③: 高速化と資源活用の実測 |
| [29_phase6_performance_completion.md](29_phase6_performance_completion.md) | Phase 6③ 高速化・資源活用の完了記録 |
| [30_phase6_readiness_execution.md](30_phase6_readiness_execution.md) | Phase 6④⑤: 生成・変換と本学習設定の確定 |
| [32_local_10b_corpus.md](32_local_10b_corpus.md) | ローカル10Bデータセットの整備 |
| [35_base_5b_execution.md](35_base_5b_execution.md) | 次計画1・2：10Mモデルを総5Bまで学習 |
| [36_base_5b_comparison.md](36_base_5b_comparison.md) | 5B学習済み10Mモデルの比較結果 |
| [37_eos_repetition_utf8_improvement_plan.md](37_eos_repetition_utf8_improvement_plan.md) | 5B後のEOS・反復・UTF8末尾改善：調査と次回計画 |
| [38_eos_5b_finish_results.md](38_eos_5b_finish_results.md) | EOS・反復・UTF8改善の1〜3：実行結果 |
| [39_learning_scale_and_generation_plan.md](39_learning_scale_and_generation_plan.md) | 学習量拡大とEOS 反復 UTF8改善の次回計画 |
| [40_base_10b_preparation.md](40_base_10b_preparation.md) | 直接10B学習の実行準備完了 |
| [41_base_10b_training.md](41_base_10b_training.md) | 直接10B学習の完了記録 |
| [42_base_10b_quality_evaluation.md](42_base_10b_quality_evaluation.md) | 10Bの同条件品質評価 |
| [43_local_webui.md](43_local_webui.md) | 学習済み10BモデルのローカルWeb UI |
| [44_japanese_base_evaluation_audit.md](44_japanese_base_evaluation_audit.md) | 日本語Baseモデル評価の棚卸しと改善案 |
| [45_japanese_base_evaluation_v2.md](45_japanese_base_evaluation_v2.md) | 日本語Base追加評価v2の実施計画 |
| [46_japanese_base_evaluation_v2_results.md](46_japanese_base_evaluation_v2_results.md) | 日本語Base評価v2.1の結果 |
| [47_post_evaluation_training_plan.md](47_post_evaluation_training_plan.md) | 追加評価後のデータ・学習改善計画 |
| [48_complete_text_10b_comparison.md](48_complete_text_10b_comparison.md) | 完結文配合の三条件100M比較 |
| [49_next_mixture_and_training_budget_plan.md](49_next_mixture_and_training_budget_plan.md) | 完結文比較後の配合・学習量計画 |
| [50_story10_and_budget_execution.md](50_story10_and_budget_execution.md) | 配合10%・学習量比較の実行 |
| [51_story10_judgment_and_next_proposal.md](51_story10_judgment_and_next_proposal.md) | 物語10%・低LR比較の判断と次の提案 |
| [52_story20_low_lr_execution.md](52_story20_low_lr_execution.md) | 物語20%・低学習率と学習量比較の実行計画 |
| [53_story20_low_lr_judgment.md](53_story20_low_lr_judgment.md) | 物語20%・低学習率と学習量比較の判断 |
| [54_complete_document_500m_execution.md](54_complete_document_500m_execution.md) | 完結文データ構成比較・実行計画 |
| [55_complete_document_500m_results.md](55_complete_document_500m_results.md) | 完結文データ構成・固定500M比較結果 |
| [56_matched_story_and_learning_budget_plan.md](56_matched_story_and_learning_budget_plan.md) | 教材内容と学習量の切り分け・段階1〜3実行計画 |
| [57_matched_story_and_learning_budget_results.md](57_matched_story_and_learning_budget_results.md) | 教材内容と学習量の比較結果 |
| [58_dataset_expansion_proposal.md](58_dataset_expansion_proposal.md) | 教材量を増やす次回比較案 |
| [59_dataset_expansion_execution.md](59_dataset_expansion_execution.md) | 教材200M・各1B比較の実行 |
| [60_dataset_expansion_results.md](60_dataset_expansion_results.md) | 短い物語教材60M→200M・同量追加1Bの比較結果 |
| [61_condition_preservation_next_plan.md](61_condition_preservation_next_plan.md) | 次回計画: 条件保持と教材品質を切り分ける |
| [62_condition_preservation_execution.md](62_condition_preservation_execution.md) | 条件保持・教材品質比較の実行記録 |
| [63_condition_preservation_preparation_results.md](63_condition_preservation_preparation_results.md) | 同source・長さ/EOS一致教材の準備結果 |
| [64_condition_selector_v2_execution.md](64_condition_selector_v2_execution.md) | 条件保持selector改修と各100M比較 |
| [65_condition_selector_v2_preparation_results.md](65_condition_selector_v2_preparation_results.md) | 条件保持selector v2の検証・教材準備結果 |
| [66_condition_learning_diagnostic_plan.md](66_condition_learning_diagnostic_plan.md) | 条件保持の学習可能性診断：実行契約 |
| [67_condition_learning_diagnostic_results.md](67_condition_learning_diagnostic_results.md) | 条件保持の小教材学習・拡張・総合評価結果 |
| [68_packing_learning_execution.md](68_packing_learning_execution.md) | 文書連結依存の三条件比較：実行契約 |
| [69_packing_learning_results.md](69_packing_learning_results.md) | 同じ教材の文書連結・順序変更・文書単位学習の結果 |
| [70_root_cause_investigation_plan.md](70_root_cause_investigation_plan.md) | 日本語Baseの停止・反復・意味保持を根本から切り分ける計画 |
| [71_root_cause_diagnostic_execution.md](71_root_cause_diagnostic_execution.md) | 根本原因診断の実行契約 |
| [72_root_cause_diagnostic_results.md](72_root_cause_diagnostic_results.md) | 根本原因診断の結果と次の修正計画 |
| [73_natural_learning_execution.md](73_natural_learning_execution.md) | 自然短文の学習診断から教材比較・条件付き拡大まで |
| [74_natural_learning_results.md](74_natural_learning_results.md) | 自然短文の記憶診断と同量教材比較の結果 |
| [75_diverse_learning_execution.md](75_diverse_learning_execution.md) | 多様な完結文の準備・同量比較・条件付き拡大 |
| [76_diverse_preparation_repair.md](76_diverse_preparation_repair.md) | 準備の失敗を保持した抽出修正 |
| [77_narrative_diversity_execution.md](77_narrative_diversity_execution.md) | 同じ三段階を満たすためのsource選択修正 |
| [78_narrative_supply_execution.md](78_narrative_supply_execution.md) | 実供給量を反映した準備の固定 |
| [79_narrative_diversity_results.md](79_narrative_diversity_results.md) | 多様な原文教材の同量比較結果 |
| [80_generation_transfer_plan.md](80_generation_transfer_plan.md) | 生成の逸脱・停止位置・教材適合性を切り分ける次の計画 |
| [116_base_gradient_accumulation_pilot_results.md](116_base_gradient_accumulation_pilot_results.md) | 同stream勾配蓄積pilotの結果（2026-10-08） |
| [117_base_residual_initialization_pilot.md](117_base_residual_initialization_pilot.md) | Base初期化の短期比較（2026-10-08） |
| [118_base_residual_initialization_results.md](118_base_residual_initialization_results.md) | Base残差出力初期化の結果（2026-10-08） |
| [119_base_teacher_decay_pilot.md](119_base_teacher_decay_pilot.md) | 教師トークン数に合わせる重み減衰の比較 |
| [120_base_teacher_decay_pilot_results.md](120_base_teacher_decay_pilot_results.md) | 教師量正規化decayの短い比較結果 |
| [121_base_teacher_decay_2b_continuation.md](121_base_teacher_decay_2b_continuation.md) | 同じ減衰条件で累積2Bまで継続する |
| [122_base_native_seed_confirmation_preparation.md](122_base_native_seed_confirmation_preparation.md) | native学習方式の独立seed確認に向けたCPU準備 |
| [123_base_teacher_decay_2b_results.md](123_base_teacher_decay_2b_results.md) | 2B teacher-normalized weight-decay comparison: results and user pause |
| [124_base_recovery_plan.md](124_base_recovery_plan.md) | Base改善の今後の計画 |
| [125_project_retrospective.md](125_project_retrospective.md) | 調査・検証・学習・失敗・未達・保存先の全体記録と詳細台帳 |
| [126_model_archive.md](126_model_archive.md) | データセットを含めない主要3系列のHugging Face保存・手動承認・読み込み手順 |
| [127_rebuild_investigation.md](127_rebuild_investigation.md) | 作り直す前のAkebono比較・前回の原因分析・再利用方針 |
| [128_chat_first_sft_plan.md](128_chat_first_sft_plan.md) | 元10B Baseから小規模な直接SFTで会話を先に検証する計画 |
| [129_chat_first_sft_execution.md](129_chat_first_sft_execution.md) | 明示再開後の保全・SFT入口・CUDA gate・学習/会話評価の実行記録 |
| [130_chat_failure_improvement_investigation.md](130_chat_failure_improvement_investigation.md) | SFT後の失敗・実装・教材・一次研究から整理した改善の優先順位と比較案 |
| [131_chat_improvement_execution_plan.md](131_chat_improvement_execution_plan.md) | 課題ごとの対策、教材2条件比較、教師量学習契約、新旧評価・停止・後続段階 |
| [132_chat_improvement_execution.md](132_chat_improvement_execution.md) | 教材2条件・全学習/評価・不採用結果と完了監査 |
| [133_chat_generalization_followup_plan.md](133_chat_generalization_followup_plan.md) | 比較132を受けた教材汎化・直接回答・訂正の改善計画。未実行 |
