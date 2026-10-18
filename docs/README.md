# 文書を読む順序

更新: 2026-10-18 JST。

最新SFTは実行・全件評価を完了し、候補は品質不採用です。Base 3系列と最新SFTの重みは申請不要で公開し、コードはApache-2.0になりました。

## まず読む文書

| 目的 | 主文書 |
|---|---|
| モデルを取得して試す | [プロジェクトREADME](../README.md) / [保存範囲](126_model_archive.md) |
| 現在の結果と公開 | [状態](autonomous_status.md) / [最新結果165](165_chat_two_attribute_diagnosis_results.md) / [公開166](166_public_models_and_oss.md) |
| 構成・Tokenizer・学習 | [モデル構成](03_architecture.md) / [データ](../data/README.md) |
| 評価の基準と限界 | [評価方法](evaluation_protocol.md) / [残課題](10_next_steps.md) |
| 環境・保存先・画面 | [引継ぎ](windows_handoff.md) / [WebUI](43_local_webui.md) |
| 過去の研究を探す | [総覧](125_project_retrospective.md) / [実験索引](base_experiment_lookup.md) / [全件カタログ](document_catalog.md) |

重複する設計・計画は主文書へ統合しました。旧入口はリンク互換性のため案内だけ残し、古い文書更新報告142/146/148は[更新記録167](167_current_state_and_documentation.md)へ統合・削除しています。日付付き実験結果、凍結契約、source snapshot、原文copy、第三者の帰属は保持しています。

## 番号付きの計画と結果

以下は現在の実行順ではありません。各文書の日付・対象・採否で読み、古い「実行中」「未公開」「次は」を現在の状態へ持ち込まないでください。

| 文書 | 内容 |
|---|---|
| [01_project_goal.md](01_project_goal.md) | プロジェクト目的 |
| [02_research_summary.md](02_research_summary.md) | 調査要約 |
| [03_architecture.md](03_architecture.md) | アーキテクチャ設計 |
| [04_tokenizer.md](04_tokenizer.md) | Tokenizer設計 |
| [05_dataset.md](05_dataset.md) | データ設計 |
| [06_training_plan.md](06_training_plan.md) | 学習計画 |
| [07_environment.md](07_environment.md) | 実行環境とデータ配置 |
| [08_evaluation.md](08_evaluation.md) | 評価・Checkpoint・検証 |
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
| [43_local_webui.md](43_local_webui.md) | 元10B BaseモデルのローカルWebUI |
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
| [125_project_retrospective.md](125_project_retrospective.md) | JMicro-10M 調査・検証・学習の全体記録 |
| [126_model_archive.md](126_model_archive.md) | 研究モデルのHugging Face保存 |
| [127_rebuild_investigation.md](127_rebuild_investigation.md) | 作り直す前の調査: Akebono-10M-chatとJMicro-10Mの比較 |
| [128_chat_first_sft_plan.md](128_chat_first_sft_plan.md) | 現在のBaseを直接SFTして会話を検証する計画 |
| [129_chat_first_sft_execution.md](129_chat_first_sft_execution.md) | Chat-first SFT診断の実行記録 |
| [130_chat_failure_improvement_investigation.md](130_chat_failure_improvement_investigation.md) | Chat-first SFTの問題点と改善方法の調査 |
| [131_chat_improvement_execution_plan.md](131_chat_improvement_execution_plan.md) | Chatの課題を解決するための段階計画 |
| [132_chat_improvement_execution.md](132_chat_improvement_execution.md) | 計画131・教材改善比較の実行記録 |
| [133_chat_generalization_followup_plan.md](133_chat_generalization_followup_plan.md) | Chat教材の汎化を改善する次の計画 |
| [134_chat_generalization_execution.md](134_chat_generalization_execution.md) | 教材汎化の改善比較・実行記録 |
| [135_chat_problem_solution_plan.md](135_chat_problem_solution_plan.md) | Chatの課題を解決する方法と次の判断 |
| [136_chat_generalization_results.md](136_chat_generalization_results.md) | 教材汎化・同条件比較・回復分岐・paddingの最終結果 |
| [137_chat_semantic_diversity_execution.md](137_chat_semantic_diversity_execution.md) | 意味構造を広げる教材比較・実行記録 |
| [138_chat_semantic_diversity_results.md](138_chat_semantic_diversity_results.md) | 意味構造を広げる教材比較の最終結果（138） |
| [139_chat_lr_comparison_plan.md](139_chat_lr_comparison_plan.md) | 次介入1件・低学習率SFT比較と条件付き独立確認 |
| [140_chat_lr_comparison_execution.md](140_chat_lr_comparison_execution.md) | 低学習率SFT比較・実行履歴 |
| [141_chat_lr_comparison_results.md](141_chat_lr_comparison_results.md) | 低学習率SFT比較の結果（141） |
| [143_base_document_balance_plan.md](143_base_document_balance_plan.md) | Base再開: 文書長による損失配分の比較 |
| [144_base_document_balance_results.md](144_base_document_balance_results.md) | 文書長による損失配分の比較結果 |
| [145_post_rejection_next_plan.md](145_post_rejection_next_plan.md) | 不採用結果を踏まえた次の計画 |
| [147_evaluation_boundary_repair.md](147_evaluation_boundary_repair.md) | Base再開: 評価入力の分離修理 |
| [149_chat_sft_next_plan.md](149_chat_sft_next_plan.md) | 次のSFT計画：実際の会話データの幅を広げる |
| [150_chat_natural_sft_results.md](150_chat_natural_sft_results.md) | 会話教材を広げた短文SFTの比較結果 |
| [151_answer_learning_execution_plan.md](151_answer_learning_execution_plan.md) | 回答学習を切り分ける次の5段階 |
| [152_answer_learning_diagnosis_results.md](152_answer_learning_diagnosis_results.md) | 回答学習の切り分け：参考比較・教材点検・少量診断 |
| [153_answer_curriculum_comparison.md](153_answer_curriculum_comparison.md) | 回答教材を補う1件の対照SFT：事前方針 |
| [154_curriculum_resource_replan.md](154_curriculum_resource_replan.md) | 主SFT前の時間計画の訂正 |
| [155_answer_curriculum_execution_status.md](155_answer_curriculum_execution_status.md) | 回答教材SFTの実行状況 |
| [156_answer_curriculum_results.md](156_answer_curriculum_results.md) | 回答教材を補ったSFTの比較結果 |
| [157_chat_quality_100_results.md](157_chat_quality_100_results.md) | 現行Chatの100ケース品質診断 |
| [158_chat_quality_investigation_and_next_plan.md](158_chat_quality_investigation_and_next_plan.md) | 短い日本語チャットの失敗原因と次の改善計画 |
| [159_chat_recovery_diagnosis_results.md](159_chat_recovery_diagnosis_results.md) | 対照モデルと履歴条件を変えたチャット診断 |
| [160_chat_input_structure_sft_comparison.md](160_chat_input_structure_sft_comparison.md) | 情報配置を変える教材による新しい対照SFT |
| [161_chat_input_structure_execution_status.md](161_chat_input_structure_execution_status.md) | 情報配置の対照SFTの実行状況 |
| [162_chat_input_structure_sft_results.md](162_chat_input_structure_sft_results.md) | 情報配置を変えた対照SFTの結果 |
| [163_chat_next_capability_diagnosis_plan.md](163_chat_next_capability_diagnosis_plan.md) | 今回の失敗から進める次の課題と計画 |
| [164_chat_two_attribute_diagnosis_execution.md](164_chat_two_attribute_diagnosis_execution.md) | 二つの最新情報を答える能力の診断 |
| [165_chat_two_attribute_diagnosis_results.md](165_chat_two_attribute_diagnosis_results.md) | 二つの情報を答える学習と転用の診断結果 |
| [166_public_models_and_oss.md](166_public_models_and_oss.md) | 公開モデルとOSSコードの保存先 |
| [167](167_current_state_and_documentation.md) | 全文書の更新・統合・削除の記録 |

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="今回の文書と計画"></a>
<a id="文書一覧"></a>
<a id="現行仕様と履歴"></a>
<a id="番号付きの計画結果"></a>
<a id="読む順序"></a>
