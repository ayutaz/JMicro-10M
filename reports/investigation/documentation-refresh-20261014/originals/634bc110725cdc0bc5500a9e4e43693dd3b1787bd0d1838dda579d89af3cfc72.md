# 原文書の一覧

内容は作成当時の計画・結果。現在の指示はAGENTSとstatusを優先する。番号の欠番は未保存文書の存在を意味しない。

| 文書 | 表題 | bytes |
|---|---|---:|
| [docs/01_project_goal.md](../../docs/01_project_goal.md) | プロジェクト目的 | 4,608 |
| [docs/02_research_summary.md](../../docs/02_research_summary.md) | 調査要約 | 5,738 |
| [docs/03_architecture.md](../../docs/03_architecture.md) | アーキテクチャ設計 | 6,595 |
| [docs/04_tokenizer.md](../../docs/04_tokenizer.md) | Tokenizer設計 | 4,337 |
| [docs/05_dataset.md](../../docs/05_dataset.md) | データ設計 | 5,666 |
| [docs/06_training_plan.md](../../docs/06_training_plan.md) | 学習計画 | 9,445 |
| [docs/07_environment.md](../../docs/07_environment.md) | 実行環境とデータ配置 | 9,145 |
| [docs/08_evaluation.md](../../docs/08_evaluation.md) | 評価・Checkpoint・TDD | 6,128 |
| [docs/09_prior_art_and_baselines.md](../../docs/09_prior_art_and_baselines.md) | 先行例とベースライン | 5,522 |
| [docs/10_next_steps.md](../../docs/10_next_steps.md) | 現在のチェックリスト | 3,654 |
| [docs/116_base_gradient_accumulation_pilot_results.md](../../docs/116_base_gradient_accumulation_pilot_results.md) | 同stream勾配蓄積pilotの結果（2026-10-08） | 3,346 |
| [docs/117_base_residual_initialization_pilot.md](../../docs/117_base_residual_initialization_pilot.md) | Base初期化の短期比較（2026-10-08） | 4,634 |
| [docs/118_base_residual_initialization_results.md](../../docs/118_base_residual_initialization_results.md) | Base残差出力初期化の結果（2026-10-08） | 3,956 |
| [docs/119_base_teacher_decay_pilot.md](../../docs/119_base_teacher_decay_pilot.md) | 教師トークン数に合わせる重み減衰の比較 | 4,606 |
| [docs/11_technical_research_gaps.md](../../docs/11_technical_research_gaps.md) | 未解決の技術課題と追加調査 | 11,355 |
| [docs/120_base_teacher_decay_pilot_results.md](../../docs/120_base_teacher_decay_pilot_results.md) | 教師量正規化decayの短い比較結果 | 4,897 |
| [docs/121_base_teacher_decay_2b_continuation.md](../../docs/121_base_teacher_decay_2b_continuation.md) | 同じ減衰条件で累積2Bまで継続する | 4,921 |
| [docs/122_base_native_seed_confirmation_preparation.md](../../docs/122_base_native_seed_confirmation_preparation.md) | native学習方式の独立seed確認に向けたCPU準備 | 2,951 |
| [docs/123_base_teacher_decay_2b_results.md](../../docs/123_base_teacher_decay_2b_results.md) | 2B teacher-normalized weight-decay comparison: results and user pause | 6,906 |
| [docs/124_base_recovery_plan.md](../../docs/124_base_recovery_plan.md) | Base改善の今後の計画 | 12,847 |
| [docs/12_training_implementation_research.md](../../docs/12_training_implementation_research.md) | モデル実装・段階学習・実行環境の追加調査 | 15,577 |
| [docs/13_tokenizer_dialogue_data_research.md](../../docs/13_tokenizer_dialogue_data_research.md) | Tokenizer・日本語会話データ・SFTの追加調査 | 17,811 |
| [docs/14_evaluation_deployment_research.md](../../docs/14_evaluation_deployment_research.md) | 比較評価・量子化・ローカル推論の追加調査 | 16,701 |
| [docs/15_project_roadmap.md](../../docs/15_project_roadmap.md) | JMicro-10M フェーズ別実行計画 | 9,017 |
| [docs/16_phase0_completion.md](../../docs/16_phase0_completion.md) | Phase 0 完了記録 | 5,471 |
| [docs/17_phase1_completion.md](../../docs/17_phase1_completion.md) | Phase 1 完了記録 | 8,361 |
| [docs/18_phase2_completion.md](../../docs/18_phase2_completion.md) | Phase 2完了記録 | 5,070 |
| [docs/19_phase3_completion.md](../../docs/19_phase3_completion.md) | Phase 3完了記録 | 8,872 |
| [docs/20_publication_review.md](../../docs/20_publication_review.md) | Hugging Face公開前のライセンス・個人情報確認 | 7,180 |
| [docs/21_phase4_completion.md](../../docs/21_phase4_completion.md) | Phase 4完了: WSL・学習器・再開・4090実測 | 4,753 |
| [docs/22_phase5_plan.md](../../docs/22_phase5_plan.md) | Phase 5: 目的・ゴール・実行計画 | 8,672 |
| [docs/23_phase5_completion.md](../../docs/23_phase5_completion.md) | Phase 5完了: 小予算の学習検証と候補選定 | 7,678 |
| [docs/24_phase6_plan.md](../../docs/24_phase6_plan.md) | Phase 6 Base学習の現在地と進行条件 | 4,503 |
| [docs/25_phase6_preparation.md](../../docs/25_phase6_preparation.md) | Phase 6の①データ拡充・②長時間学習準備 | 4,141 |
| [docs/26_phase6_preparation_completion.md](../../docs/26_phase6_preparation_completion.md) | Phase 6①②の完了記録 | 6,254 |
| [docs/27_phase6_remaining_plan.md](../../docs/27_phase6_remaining_plan.md) | Phase 6以降に残る作業 | 3,289 |
| [docs/28_phase6_performance.md](../../docs/28_phase6_performance.md) | Phase 6③: 高速化と資源活用の実測 | 10,913 |
| [docs/29_phase6_performance_completion.md](../../docs/29_phase6_performance_completion.md) | Phase 6③ 高速化・資源活用の完了記録 | 5,643 |
| [docs/30_phase6_readiness_execution.md](../../docs/30_phase6_readiness_execution.md) | Phase 6④⑤: 生成・変換と本学習設定の確定 | 14,741 |
| [docs/32_local_10b_corpus.md](../../docs/32_local_10b_corpus.md) | ローカル10Bデータセットの整備 | 15,454 |
| [docs/35_base_5b_execution.md](../../docs/35_base_5b_execution.md) | 次計画1・2：10Mモデルを総5Bまで学習 | 3,931 |
| [docs/36_base_5b_comparison.md](../../docs/36_base_5b_comparison.md) | 5B学習済み10Mモデルの比較結果 | 4,997 |
| [docs/37_eos_repetition_utf8_improvement_plan.md](../../docs/37_eos_repetition_utf8_improvement_plan.md) | 5B後のEOS・反復・UTF8末尾改善：調査と次回計画 | 13,749 |
| [docs/38_eos_5b_finish_results.md](../../docs/38_eos_5b_finish_results.md) | EOS・反復・UTF8改善の1〜3：実行結果 | 8,009 |
| [docs/39_learning_scale_and_generation_plan.md](../../docs/39_learning_scale_and_generation_plan.md) | 学習量拡大とEOS 反復 UTF8改善の次回計画 | 13,977 |
| [docs/40_base_10b_preparation.md](../../docs/40_base_10b_preparation.md) | 直接10B学習の実行準備完了 | 5,191 |
| [docs/41_base_10b_training.md](../../docs/41_base_10b_training.md) | 直接10B学習の完了記録 | 4,884 |
| [docs/42_base_10b_quality_evaluation.md](../../docs/42_base_10b_quality_evaluation.md) | 10Bの同条件品質評価 | 6,727 |
| [docs/43_local_webui.md](../../docs/43_local_webui.md) | 学習済み10BモデルのローカルWeb UI | 3,827 |
| [docs/44_japanese_base_evaluation_audit.md](../../docs/44_japanese_base_evaluation_audit.md) | 日本語Baseモデル評価の棚卸しと改善案 | 15,399 |
| [docs/45_japanese_base_evaluation_v2.md](../../docs/45_japanese_base_evaluation_v2.md) | 日本語Base追加評価v2の実施計画 | 6,550 |
| [docs/46_japanese_base_evaluation_v2_results.md](../../docs/46_japanese_base_evaluation_v2_results.md) | 日本語Base評価v2.1の結果 | 9,038 |
| [docs/47_post_evaluation_training_plan.md](../../docs/47_post_evaluation_training_plan.md) | 追加評価後のデータ・学習改善計画 | 14,891 |
| [docs/48_complete_text_10b_comparison.md](../../docs/48_complete_text_10b_comparison.md) | 完結文配合の三条件100M比較 | 17,140 |
| [docs/49_next_mixture_and_training_budget_plan.md](../../docs/49_next_mixture_and_training_budget_plan.md) | 完結文比較後の配合・学習量計画 | 8,143 |
| [docs/50_story10_and_budget_execution.md](../../docs/50_story10_and_budget_execution.md) | 配合10%・学習量比較の実行 | 7,278 |
| [docs/51_story10_judgment_and_next_proposal.md](../../docs/51_story10_judgment_and_next_proposal.md) | 物語10%・低LR比較の判断と次の提案 | 8,223 |
| [docs/52_story20_low_lr_execution.md](../../docs/52_story20_low_lr_execution.md) | 物語20%・低学習率と学習量比較の実行計画 | 13,374 |
| [docs/53_story20_low_lr_judgment.md](../../docs/53_story20_low_lr_judgment.md) | 物語20%・低学習率と学習量比較の判断 | 18,319 |
| [docs/54_complete_document_500m_execution.md](../../docs/54_complete_document_500m_execution.md) | 完結文データ構成比較・実行計画 | 5,782 |
| [docs/55_complete_document_500m_results.md](../../docs/55_complete_document_500m_results.md) | 完結文データ構成・固定500M比較結果 | 9,449 |
| [docs/56_matched_story_and_learning_budget_plan.md](../../docs/56_matched_story_and_learning_budget_plan.md) | 教材内容と学習量の切り分け・段階1〜3実行計画 | 7,869 |
| [docs/57_matched_story_and_learning_budget_results.md](../../docs/57_matched_story_and_learning_budget_results.md) | 教材内容と学習量の比較結果 | 10,922 |
| [docs/58_dataset_expansion_proposal.md](../../docs/58_dataset_expansion_proposal.md) | 教材量を増やす次回比較案 | 5,154 |
| [docs/59_dataset_expansion_execution.md](../../docs/59_dataset_expansion_execution.md) | 教材200M・各1B比較の実行 | 8,023 |
| [docs/60_dataset_expansion_results.md](../../docs/60_dataset_expansion_results.md) | 短い物語教材60M→200M・同量追加1Bの比較結果 | 8,836 |
| [docs/61_condition_preservation_next_plan.md](../../docs/61_condition_preservation_next_plan.md) | 次回計画: 条件保持と教材品質を切り分ける | 10,279 |
| [docs/62_condition_preservation_execution.md](../../docs/62_condition_preservation_execution.md) | 条件保持・教材品質比較の実行記録 | 2,480 |
| [docs/63_condition_preservation_preparation_results.md](../../docs/63_condition_preservation_preparation_results.md) | 同source・長さ/EOS一致教材の準備結果 | 7,224 |
| [docs/64_condition_selector_v2_execution.md](../../docs/64_condition_selector_v2_execution.md) | 条件保持selector改修と各100M比較 | 4,937 |
| [docs/65_condition_selector_v2_preparation_results.md](../../docs/65_condition_selector_v2_preparation_results.md) | 条件保持selector v2の検証・教材準備結果 | 7,707 |
| [docs/66_condition_learning_diagnostic_plan.md](../../docs/66_condition_learning_diagnostic_plan.md) | 条件保持の学習可能性診断：実行契約 | 3,648 |
| [docs/67_condition_learning_diagnostic_results.md](../../docs/67_condition_learning_diagnostic_results.md) | 条件保持の小教材学習・拡張・総合評価結果 | 8,712 |
| [docs/68_packing_learning_execution.md](../../docs/68_packing_learning_execution.md) | 文書連結依存の三条件比較：実行契約 | 3,417 |
| [docs/69_packing_learning_results.md](../../docs/69_packing_learning_results.md) | 同じ教材の文書連結・順序変更・文書単位学習の結果 | 9,583 |
| [docs/70_root_cause_investigation_plan.md](../../docs/70_root_cause_investigation_plan.md) | 日本語Baseの停止・反復・意味保持を根本から切り分ける計画 | 16,716 |
| [docs/71_root_cause_diagnostic_execution.md](../../docs/71_root_cause_diagnostic_execution.md) | 根本原因診断の実行契約 | 3,021 |
| [docs/72_root_cause_diagnostic_results.md](../../docs/72_root_cause_diagnostic_results.md) | 根本原因診断の結果と次の修正計画 | 13,929 |
| [docs/73_natural_learning_execution.md](../../docs/73_natural_learning_execution.md) | 自然短文の学習診断から教材比較・条件付き拡大まで | 4,117 |
| [docs/74_natural_learning_results.md](../../docs/74_natural_learning_results.md) | 自然短文の記憶診断と同量教材比較の結果 | 10,660 |
| [docs/75_diverse_learning_execution.md](../../docs/75_diverse_learning_execution.md) | 多様な完結文の準備・同量比較・条件付き拡大 | 4,348 |
| [docs/76_diverse_preparation_repair.md](../../docs/76_diverse_preparation_repair.md) | 準備の失敗を保持した抽出修正 | 1,692 |
| [docs/77_narrative_diversity_execution.md](../../docs/77_narrative_diversity_execution.md) | 同じ三段階を満たすためのsource選択修正 | 2,423 |
| [docs/78_narrative_supply_execution.md](../../docs/78_narrative_supply_execution.md) | 実供給量を反映した準備の固定 | 1,537 |
| [docs/79_narrative_diversity_results.md](../../docs/79_narrative_diversity_results.md) | 多様な原文教材の同量比較結果 | 9,547 |
| [docs/80_generation_transfer_plan.md](../../docs/80_generation_transfer_plan.md) | 生成の逸脱・停止位置・教材適合性を切り分ける次の計画 | 9,515 |
| [docs/README.md](../../docs/README.md) | JMicro-10M 文書一覧 | 12,951 |
| [docs/agents_history_20261008.md](../../docs/agents_history_20261008.md) | Latest user instruction (2026-10-08 JST): PAUSED at the completed cumulative2B teacher-decay experiment and all80 evaluation. The user explicitly requested a sensible stopping point and current learning results. Await explicit user resumption; do not start further research/training, seed43, Chat/Dialogue/SFT, quantization or deployment. The fixed2B condition is rejected and closed; Base and the wider objective remain unfinished. Preserve checkpoints and leave the restored original local WebUI available. See docs/123_base_teacher_decay_2b_results.md and current status headers. Earlier continuation instructions below are historical and do not override this pause. On future resumption, retain the Base-only stop boundary unless the user changes it. | 54,176 |
| [docs/autonomous_history_20261003.md](../../docs/autonomous_history_20261003.md) | 2026-10-03 環境復旧・Phase 4実装の履歴 | 7,986 |
| [docs/autonomous_history_20261004.md](../../docs/autonomous_history_20261004.md) | 2026年10月4日までの計画と進捗記録 | 344,847 |
| [docs/autonomous_history_20261005.md](../../docs/autonomous_history_20261005.md) | 2026-10-05文書整理前の保存履歴 | 197,449 |
| [docs/autonomous_status.md](../../docs/autonomous_status.md) | 現在の状態 | 8,429 |
| [docs/autonomous_status_history_20261008.md](../../docs/autonomous_status_history_20261008.md) | ユーザー指示による一時停止（2026-10-08 JST）。「切りのいいところで止めて現状の学習の成果を教えてください」に従い、累積2,000,000,000教師・212095更新のteacher-normalized weight-decay比較と全80件個別内容評価を完了した区切りで停止。元native2B対照→候補はBPB1.106386→1.090316（約1.45%改善）だが、一貫性3→3、適切完結7→5、EOS20→23、自動反復27→27、Unicode失敗0→1（各80）。元絶対6条件は全未達、固定条件は不採用・閉鎖、Base未完成・未採用。独立学習seed43/fullDEV/protectedTEST/adoption未達、CPU seed準備を学習成果にしない。actual118881/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start8215874終了、Windows worker38176 exit0、追加GPU26060.094秒・pilot込27475.228秒、台帳closed。最終checkpointはWSL reports/phase6/base-teacher-decay-2b-20261008/latest.pt（SHA03ebf266…）に保存。terminal jobの周期heartbeat212080と最終result212095を混同しない。元10B UI120460/start10822295・HTTP親410f975d…/10000007168/busy=false復帰確認。成果・制約・再開状態はdocs/123_base_teacher_decay_2b_results.md、portable completion/全80notes/raw評価/active_jobを保存。次の行動はユーザーの明示的な再開指示を待つこと。追加研究/学習/seed43/Chat/SFT/量子化/自動pushなし。元ローカルUIは利用可能のまま。以下の「継続」「次は」は履歴であり、この停止指示を上書きしない。 | 824,111 |
| [docs/autonomous_status_phase5_20261003.md](../../docs/autonomous_status_phase5_20261003.md) | Codex継続作業の現在地 | 16,212 |
| [docs/base_ademamix_100m_results.md](../../docs/base_ademamix_100m_results.md) | AdEMAMixの100M教師tokens比較（2026-10-07） | 4,843 |
| [docs/base_experiment_lookup.md](../../docs/base_experiment_lookup.md) | Baseの実験結果を探す | 1,861 |
| [docs/base_headwise_gate_100m_results.md](../../docs/base_headwise_gate_100m_results.md) | headwise Attention出力ゲートの比較を終了し、不採用とした。品質基準を満たすBaseは未完成で、Chat・量子化・展開は開始していない。 | 4,336 |
| [docs/base_headwise_gate_plan.md](../../docs/base_headwise_gate_plan.md) | Baseのquery依存Attention出力ゲート比較 | 6,370 |
| [docs/base_output_mixture_100m_results.md](../../docs/base_output_mixture_100m_results.md) | MoC / MoS 同学習量比較の結果 | 4,454 |
| [docs/codex_automation.md](../../docs/codex_automation.md) | Codexによる環境整備・学習・改善の自動化 | 6,718 |
| [docs/evaluation_protocol.md](../../docs/evaluation_protocol.md) | 評価仕様 v1 | 11,003 |
| [docs/huggingface_handoff.md](../../docs/huggingface_handoff.md) | Hugging Face経由での成果物共有 | 5,785 |
| [docs/project_roadmap_history_20261008.md](../../docs/project_roadmap_history_20261008.md) | ユーザー指示による一時停止（2026-10-08 JST）。「切りのいいところで止めて現状の学習の成果を教えてください」に従い、累積2,000,000,000教師・212095更新のteacher-normalized weight-decay比較と全80件個別内容評価を完了した区切りで停止。元native2B対照→候補はBPB1.106386→1.090316（約1.45%改善）だが、一貫性3→3、適切完結7→5、EOS20→23、自動反復27→27、Unicode失敗0→1（各80）。元絶対6条件は全未達、固定条件は不採用・閉鎖、Base未完成・未採用。独立学習seed43/fullDEV/protectedTEST/adoption未達、CPU seed準備を学習成果にしない。actual118881/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start8215874終了、Windows worker38176 exit0、追加GPU26060.094秒・pilot込27475.228秒、台帳closed。最終checkpointはWSL reports/phase6/base-teacher-decay-2b-20261008/latest.pt（SHA03ebf266…）に保存。terminal jobの周期heartbeat212080と最終result212095を混同しない。元10B UI120460/start10822295・HTTP親410f975d…/10000007168/busy=false復帰確認。成果・制約・再開状態はdocs/123_base_teacher_decay_2b_results.md、portable completion/全80notes/raw評価/active_jobを保存。次の行動はユーザーの明示的な再開指示を待つこと。追加研究/学習/seed43/Chat/SFT/量子化/自動pushなし。元ローカルUIは利用可能のまま。以下の「継続」「次は」は履歴であり、この停止指示を上書きしない。 | 754,460 |
| [docs/windows_handoff.md](../../docs/windows_handoff.md) | Windows / WSL 引継ぎ | 7,914 |
| [docs/windows_handoff_history_20261008.md](../../docs/windows_handoff_history_20261008.md) | ユーザー指示による一時停止（2026-10-08 JST）。「切りのいいところで止めて現状の学習の成果を教えてください」に従い、累積2,000,000,000教師・212095更新のteacher-normalized weight-decay比較と全80件個別内容評価を完了した区切りで停止。元native2B対照→候補はBPB1.106386→1.090316（約1.45%改善）だが、一貫性3→3、適切完結7→5、EOS20→23、自動反復27→27、Unicode失敗0→1（各80）。元絶対6条件は全未達、固定条件は不採用・閉鎖、Base未完成・未採用。独立学習seed43/fullDEV/protectedTEST/adoption未達、CPU seed準備を学習成果にしない。actual118881/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start8215874終了、Windows worker38176 exit0、追加GPU26060.094秒・pilot込27475.228秒、台帳closed。最終checkpointはWSL reports/phase6/base-teacher-decay-2b-20261008/latest.pt（SHA03ebf266…）に保存。terminal jobの周期heartbeat212080と最終result212095を混同しない。元10B UI120460/start10822295・HTTP親410f975d…/10000007168/busy=false復帰確認。成果・制約・再開状態はdocs/123_base_teacher_decay_2b_results.md、portable completion/全80notes/raw評価/active_jobを保存。次の行動はユーザーの明示的な再開指示を待つこと。追加研究/学習/seed43/Chat/SFT/量子化/自動pushなし。元ローカルUIは利用可能のまま。以下の「継続」「次は」は履歴であり、この停止指示を上書きしない。 | 702,402 |
