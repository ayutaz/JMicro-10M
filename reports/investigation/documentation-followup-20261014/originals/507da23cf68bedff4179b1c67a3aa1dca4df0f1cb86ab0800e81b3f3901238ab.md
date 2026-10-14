# 文書一覧

更新: 2026-10-14 JST。Base/Chat未完成・未採用。[最新Base結果144](144_base_document_balance_results.md)は文書長重み100M/全80/数値監査・条件分岐を終え不採用。[計画143](143_base_document_balance_plan.md)の不合格時の停止条件で閉鎖し、独立学習/fullDEV/封印TEST/採用は未実行。元Base TEST promptのCPU解析も訂正した。前回Chatは[141](141_chat_lr_comparison_results.md)、文書納品は[142](142_documentation_refresh.md)。

## 読む順序

1. [現在の状態](autonomous_status.md)：実績・採否・停止・現在の依頼。
2. [最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md)：品質・採否・資源・事故・未実施。
3. [ロードマップ](15_project_roadmap.md) / [チェックリスト](10_next_steps.md)：Phaseと正式完成までの不足。
4. [Windows/WSL引継ぎ](windows_handoff.md)：元UI・全state/data・欠損時の復元。
5. [Base復旧124](124_base_recovery_plan.md) / [今回比較143](143_base_document_balance_plan.md)：原品質・10M・合格/不合格の停止境界。
6. [全文書カタログ](document_catalog.md)：311既存文書と今回追加2文書の全件区分。

## 現行仕様と履歴

目的・構成・Tokenizer・データ・学習・環境・評価は[01](01_project_goal.md)〜[08](08_evaluation.md)。凍結評価基準は[評価契約](evaluation_protocol.md)、実績を探す入口は[実験検索](base_experiment_lookup.md)・[全体記録125](125_project_retrospective.md)。

日付付き計画・結果と[固定revision台帳](retrospective/README.md)は原文を維持する。途中の「学習中」「次は」「未実施」やPIDは現在の実行許可ではない。原採否と条件は各runのcompletion/configが正本。以前のmanifest/納品証拠は当時のGit revisionとsnapshotに対する証拠で、今回のliving文書更新へ書き換えない。

閉じたChat比較の順序は128/129→131/132→133/134/136→135/137/138→139/140/141。最新の再開・採否を以前の未実行案へ戻さない。Phase0〜3、全日付付き報告、固定台帳の証拠を保全する。

[全311文書の更新前byte/hash](../reports/investigation/documentation-refresh-20261014/baseline.json)・[今回更新142](142_documentation_refresh.md)から現在の更新と原文を追える。[data](../data/README.md)、[eval](../eval/README.md)、[reports](../reports/README.md)の入口も最新化した。

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
| [133_chat_generalization_followup_plan.md](133_chat_generalization_followup_plan.md) | 教材汎化・直接回答・訂正の事前計画。実行は134、最終不採用は136 |
| [134_chat_generalization_execution.md](134_chat_generalization_execution.md) | 教材改訂・同条件比較・条件付き回復・paddingの実行履歴 |
| [135_chat_problem_solution_plan.md](135_chat_problem_solution_plan.md) | 実行済み教材比較の条件と138を踏まえた次介入の未再開提案 |
| [136_chat_generalization_results.md](136_chat_generalization_results.md) | 全3,066内容判断・NLL7点・回復分岐・padding・完了監査と不採用結果 |
| [137_chat_semantic_diversity_execution.md](137_chat_semantic_diversity_execution.md) | 意味多様性教材のQA/凍結・学習・全評価・監査・納品の時点別履歴 |
| [138_chat_semantic_diversity_results.md](138_chat_semantic_diversity_results.md) | 意味多様性教材の全21評価・採否・NLL・分岐・完了と停止 |
| [139_chat_lr_comparison_plan.md](139_chat_lr_comparison_plan.md) | 同TRAINでpeak LRだけを変える1候補・全28評価・条件付き独立確認の契約 |
| [140_chat_lr_comparison_execution.md](140_chat_lr_comparison_execution.md) | 凍結・事故保存/訂正・CUDA gate・実学習・全評価の時点別記録 |
| [141_chat_lr_comparison_results.md](141_chat_lr_comparison_results.md) | 低LR同TRAIN比較の全28評価・不採用・分岐と科学監査/納品 |

| [142_documentation_refresh.md](142_documentation_refresh.md) | 全ドキュメントの棚卸し・現行説明更新・原証拠保全・検証 |
