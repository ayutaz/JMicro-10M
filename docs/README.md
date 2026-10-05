# JMicro-10M 文書一覧

最終更新: 2026-10-05 JST。現在地は[status](autonomous_status.md)、最新完了は[結果60](60_dataset_expansion_results.md)、次回案は[計画61](61_condition_preservation_next_plan.md)。文書更新の依頼で、新data/GPUを開始していない。Phase0〜5と10B/追加比較は完了、Base/Chat品質未達。

## 読む順序

1. [status](autonomous_status.md): 実量、最新比較、採否、processと停止境界。
2. [roadmap](15_project_roadmap.md): 全体の目的・各Phase・元品質条件。
3. [結果60](60_dataset_expansion_results.md): 200M教材/各1Bの結果と解釈の限界。
4. [計画61](61_condition_preservation_next_plan.md)と[checklist](10_next_steps.md): 次回の目的・準備条件・同量予算・判断/停止。
5. [引継ぎ](windows_handoff.md): WSL/uv、Git管理外のweights/data、完成runの扱い。

主系列/UIは10,000,007,168学習tokens、最新比較枝は各11,000,020,992。モデルは10,001,152 parameters。Web準備12,225,819,077、短い物語準備200,000,192tokens。最新新条件は常識改善と生成/停止未達を分けて不採用。source/長さ/EOS密度も変わるので量だけの効果ではない。

文書のラベルは「確定/確認済み/提案・未実行」を区別する。凍結report/source/rawは当時の証拠として保存し、過去の進捗を現在の指示にしない。

## 文書一覧

1. [01_project_goal.md](01_project_goal.md) — 目的、成功条件、過去モデルとの位置付け
2. [02_research_summary.md](02_research_summary.md) — 調査結果と採否の要約
3. [03_architecture.md](03_architecture.md) — モデル仕様、パラメータ予算、派生案
4. [04_tokenizer.md](04_tokenizer.md) — 4k/8k Tokenizer、特殊token、正規化
5. [05_dataset.md](05_dataset.md) — データ候補、ライセンス、50〜100B master corpus
6. [06_training_plan.md](06_training_plan.md) — 段階学習、SFT、Vast.ai方針
7. [07_environment.md](07_environment.md) — RTX 4090、WSL、8TB、shard配置
8. [08_evaluation.md](08_evaluation.md) — 評価、checkpoint、TDD、再現性
9. [09_prior_art_and_baselines.md](09_prior_art_and_baselines.md) — 25M/100M configと100M以下の公開モデル
10. [10_next_steps.md](10_next_steps.md) — フェーズ別計画に対応した実装checklist
11. [11_technical_research_gaps.md](11_technical_research_gaps.md) — 追加調査の入口、未解決課題、優先順位、検証gate
12. [12_training_implementation_research.md](12_training_implementation_research.md) — QK-Norm仕様、cache、parameter再計算、段階学習、4090 benchmark
13. [13_tokenizer_dialogue_data_research.md](13_tokenizer_dialogue_data_research.md) — 正規化、特殊token、4k語彙予算、会話データ候補、SFT、蒸留
14. [14_evaluation_deployment_research.md](14_evaluation_deployment_research.md) — BPBの実装、公平な比較、雑談評価、GGUF、量子化、CPU推論
15. [15_project_roadmap.md](15_project_roadmap.md) — 目標から逆算したフェーズ別計画、目的・ゴール・成果物・完了条件・進行判断
16. [16_phase0_completion.md](16_phase0_completion.md) — Phase 0の実施結果、要求ごとの証拠、検証範囲、次の着手
17. [17_phase1_completion.md](17_phase1_completion.md) — 実データpilot、manifest・split、会話品質、Tokenizer sample、再生成・完了監査
18. [18_phase2_completion.md](18_phase2_completion.md) — Tokenizer学習・入出力・会話tokensの実測
19. [19_phase3_completion.md](19_phase3_completion.md) — モデル/cache/HF/native GGUF/量子化の実測
20. [20_publication_review.md](20_publication_review.md) — 当時の公開前確認、ローカル情報除去
21. [21_phase4_completion.md](21_phase4_completion.md) — WSL/CUDA・学習器・保存再開・評価・容量・速度の実機証拠
22. [22_phase5_plan.md](22_phase5_plan.md) — Phase 5の目的・条件・予算・scheduler判断
23. [23_phase5_completion.md](23_phase5_completion.md) — overfit/smoke/100M比較・候補選定・品質未達・独立監査
24. [24_phase6_plan.md](24_phase6_plan.md) — 実学習5B・仕上げ結果と直接10Bの現在地・予算
25. [25_phase6_preparation.md](25_phase6_preparation.md) — ①②の事前の目的、凍結条件と停止境界
26. [26_phase6_preparation_completion.md](26_phase6_preparation_completion.md) — ①②の実量、全corpus/CUDA監査、保存先、実CLI
27. [27_phase6_remaining_plan.md](27_phase6_remaining_plan.md) — 最新比較後の残作業、教材品質提案61、Chat・量子化・条件付き拡張
28. [28_phase6_performance.md](28_phase6_performance.md) — ③の実GPU高速化・backend実効確認・容量と厳密再開の比較
29. [29_phase6_performance_completion.md](29_phase6_performance_completion.md) — ③の採用速度・最大容量・厳密/cold再開・独立監査と停止記録
30. [30_phase6_readiness_execution.md](30_phase6_readiness_execution.md) — ④⑤の限定比較、CPU精度修復、正式検証・凍結設定・commitと停止記録


- [32_local_10b_corpus.md](32_local_10b_corpus.md) — 大規模corpus構築の履歴。現行量・利用確認と独立監査の範囲はstatusを正とする
- [35_base_5b_execution.md](35_base_5b_execution.md) — 主要5B学習の実行記録
- [36_base_5b_comparison.md](36_base_5b_comparison.md) — 主要5Bの固定評価比較
- [37_eos_repetition_utf8_improvement_plan.md](37_eos_repetition_utf8_improvement_plan.md) — EOS・反復・UTF8改善の事前計画
- [38_eos_5b_finish_results.md](38_eos_5b_finish_results.md) — Web/短文比較の結果と採用不合格
- [39_learning_scale_and_generation_plan.md](39_learning_scale_and_generation_plan.md) — 当時の直接10B・評価・報告案（完了履歴）
- [40_base_10b_preparation.md](40_base_10b_preparation.md) — 完了した専用10B準備。科学学習の完了ではない
- [41_base_10b_training.md](41_base_10b_training.md) — 総10B学習・保存確認の完了時の記録、実測速度。品質比較は後続42へ
- [42_base_10b_quality_evaluation.md](42_base_10b_quality_evaluation.md) — 同条件dev/400品質比較、生成内容、元gateと未達課題
- [43_local_webui.md](43_local_webui.md) — 学習済み10BモデルのローカルUI、起動・停止と実操作確認
- [44_japanese_base_evaluation_audit.md](44_japanese_base_evaluation_audit.md) — 現行評価の不足、日本語Baseの追加benchmark/意味診断、v2実装案
運用文書: [最新状態](autonomous_status.md)、[復旧履歴](autonomous_history_20261003.md)、[Windows/WSL引継ぎ](windows_handoff.md)、[固定Hub復元](huggingface_handoff.md)、[自律runner](codex_automation.md)、[評価仕様](evaluation_protocol.md)。[data](../data/README.md)、[eval](../eval/README.md)、[reports](../reports/README.md)に各保存領域の手順を記載する。

実行時の仕様は[評価仕様](evaluation_protocol.md)と[Windows/WSL移行手順](windows_handoff.md)を参照する。データとTokenizerの[Hugging Face公開版の取得手順](huggingface_handoff.md)も利用できる。


## 日本語評価と追加比較の履歴

| 文書 | 位置付け |
|---|---|
| [45 日本語評価v2.1](45_japanese_base_evaluation_v2.md) / [46 実測結果](46_japanese_base_evaluation_v2_results.md) | 日本語Base評価の仕様と元10B実測 |
| [47 改善計画](47_post_evaluation_training_plan.md) / [48 完結文比較](48_complete_text_10b_comparison.md) | 当時の提案と三条件100Mの完了結果 |
| [49 配合計画](49_next_mixture_and_training_budget_plan.md) / [50 実行](50_story10_and_budget_execution.md) / [51 判断](51_story10_judgment_and_next_proposal.md) | 10%/低LR追加比較の完了結果・当時の次案 |
| [52 20%低LR実行](52_story20_low_lr_execution.md) / [53 判断](53_story20_low_lr_judgment.md) | 100M/500M・条件付き全文、研究候補採用と実用品質未達 |
| [54 全文pool計画](54_complete_document_500m_execution.md) / [55 結果](55_complete_document_500m_results.md) | 110M教材・500M比較、不採用 |
| [56 教材/学習量計画](56_matched_story_and_learning_budget_plan.md) / [57 結果](57_matched_story_and_learning_budget_results.md) | matched教材と固定教材一定LR1B、採用未達 |
| [58 増量案](58_dataset_expansion_proposal.md) / [59 実行](59_dataset_expansion_execution.md) / [60 結果](60_dataset_expansion_results.md) | 最新完了。物語60M→200M・各1B、不採用 |
| [61 次回案](61_condition_preservation_next_plan.md) | 保存失敗診断・同source品質/長さ/EOSをそろえた比較。未実行 |

過去の番号付き計画にある「次回」「未開始」は記載当時の状態。現在の実行範囲はAGENTS.mdとstatusを正とする。詳細な原文は[2026-10-05履歴](autonomous_history_20261005.md)へ保持する。
