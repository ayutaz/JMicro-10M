# JMicro-10M 設計・調査ノート

最終更新: 2026-10-04。現在地は[status](autonomous_status.md)、次回の実行値と条件は[直接10B計画](39_learning_scale_and_generation_plan.md)、全体の品質目標は[roadmap](15_project_roadmap.md)を参照する。

日本語Base追加評価は[計画・仕様v2.1](45_japanese_base_evaluation_v2.md)と[現在10Bの実測結果](46_japanese_base_evaluation_v2_results.md)。文法/常識/含意/容認度/読解・基本意味・長文反復・Codex内容診断を追加し、独立人手と品質合格は別に扱う。

評価後の提案は[データ・学習改善計画](47_post_evaluation_training_plan.md)。ユーザーが再開した段階1〜3の実行は[完結文配合の三条件100M比較](48_complete_text_10b_comparison.md)に記録する。追加500M〜1B/20Bは次回以降。

## 現在の要約

モデルは10,001,152 parameters、T4K / NoQK-Norm / AdamW / context1024。主要Web5Bと同じ親から各100M仕上げ比較まで完了。準備済みtrainは12,225,819,077 tokens、独立全corpus監査は未完了。Phase 0〜5・Phase 6準備は完了済み。

直接10Bの専用準備は完了（14関連tests、実CUDA全state保存再開、26 review checks）。本10B科学学習とCPU保存確認19項目、再開された同条件品質評価とCPU確認23項目も完了。BPB0.954018・固定反復53・Unicode0、固定EOS0の課題は残る。今回はreport/commitで停止する。

本文BPBは改善したが、自然停止・反復・意味品質は不足。短文20%は固定EOS13/80へ改善したが全400 raw Unicode2件で最終採用不合格。表示helperの採用をraw品質成功とは扱わない。独立人手blind/test、Chat、新重みの量子化品質は未検証。

学習はWSL2/RTX4090/Linux disk、Python3.12.7をuvから実行する。容量最大batch111と最速batch32（約694k tokens/s）を区別する。Tokenizer/モデルと学習前export、GPU学習器・評価・保存再開は実装済み。完成したBase/Chat・配布品質とは別である。

## 文書内のラベル

- **確定**: 合意した方針・凍結条件。
- **確認済み**: 保存した実装・測定・一次資料に証拠がある内容。
- **提案/要検証**: 将来の比較候補。実行済みや品質達成とは扱わない。

過去の調査・完了記録は当時の証拠。旧500M/2B/7.5B計画と指示は[保存履歴](autonomous_history_20261004.md)へ分離した。現在の指示はAGENTS.mdとstatusを正とする。[Windows/WSL引き継ぎ](windows_handoff.md)、[残りの作業](27_phase6_remaining_plan.md)、[checklist](10_next_steps.md)を入口にする。

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
27. [27_phase6_remaining_plan.md](27_phase6_remaining_plan.md) — 直接10Bの残る作業、EOS/UTF8後続候補、Chat・量子化・条件付き拡張
28. [28_phase6_performance.md](28_phase6_performance.md) — ③の実GPU高速化・backend実効確認・容量と厳密再開の比較
29. [29_phase6_performance_completion.md](29_phase6_performance_completion.md) — ③の採用速度・最大容量・厳密/cold再開・独立監査と停止記録
30. [30_phase6_readiness_execution.md](30_phase6_readiness_execution.md) — ④⑤の限定比較、CPU精度修復、正式検証・凍結設定・commitと停止記録


- [32_local_10b_corpus.md](32_local_10b_corpus.md) — 大規模corpus構築の履歴。現行量・利用確認と独立監査の範囲はstatusを正とする
- [35_base_5b_execution.md](35_base_5b_execution.md) — 主要5B学習の実行記録
- [36_base_5b_comparison.md](36_base_5b_comparison.md) — 主要5Bの固定評価比較
- [37_eos_repetition_utf8_improvement_plan.md](37_eos_repetition_utf8_improvement_plan.md) — EOS・反復・UTF8改善の事前計画
- [38_eos_5b_finish_results.md](38_eos_5b_finish_results.md) — Web/短文比較の結果と採用不合格
- [39_learning_scale_and_generation_plan.md](39_learning_scale_and_generation_plan.md) — 現行の直接10B・評価・報告と後続候補
- [40_base_10b_preparation.md](40_base_10b_preparation.md) — 完了した専用10B準備。科学学習の完了ではない
- [41_base_10b_training.md](41_base_10b_training.md) — 総10B学習・保存確認の完了時の記録、実測速度。品質比較は後続42へ
- [42_base_10b_quality_evaluation.md](42_base_10b_quality_evaluation.md) — 同条件dev/400品質比較、生成内容、元gateと未達課題
- [43_local_webui.md](43_local_webui.md) — 学習済み10BモデルのローカルUI、起動・停止と実操作確認
- [44_japanese_base_evaluation_audit.md](44_japanese_base_evaluation_audit.md) — 現行評価の不足、日本語Baseの追加benchmark/意味診断、v2実装案
運用文書: [最新状態](autonomous_status.md)、[復旧履歴](autonomous_history_20261003.md)、[Windows/WSL引継ぎ](windows_handoff.md)、[固定Hub復元](huggingface_handoff.md)、[自律runner](codex_automation.md)、[評価仕様](evaluation_protocol.md)。[data](../data/README.md)、[eval](../eval/README.md)、[reports](../reports/README.md)に各保存領域の手順を記載する。

実行時の仕様は[評価仕様](evaluation_protocol.md)と[Windows/WSL移行手順](windows_handoff.md)を参照する。データとTokenizerの[Hugging Face公開版の取得手順](huggingface_handoff.md)も利用できる。

## 追加調査の要点（2026-10-02）

未実装のまま残っていた技術判断を、一次資料と公式コードから補足した。最初は[追加調査の入口](11_technical_research_gaps.md)を読む。

- **提案**: QK-NormをQwen3式のhead次元RMSNormとして具体化すると、T8Kは9,772,800、T4Kは10,002,816 parametersとなる。旧概算との差はgainの共有方式による。
- **提案**: SentencePieceの正規化と構造tokenの挿入方式を固定し、本文中の役割表記と構造IDを区別する。
- **提案**: BPBに加え、同一原文bytesと同一GPU時間での比較条件を用意する。
- **提案**: 長期学習前にランダム重みでHF／GGUF互換性を確認する。FFN幅576／640ではK-quantの型fallbackを確認する。
- **確認済み**: llama.cppの一般的なSentencePiece変換経路と独自Unigramの分割方式は同一ではない。内蔵Tokenizerへの互換性を検証し、必要なら外部SentencePieceでIDを作る経路を使う。
- **現在の判断**: 4090速度はPhase 4、会話教師token量はPhase 2で実測済み。Phase 5の候補選定は完了。雑談品質・学習後の量子化品質と、拡張corpus/長期予算での優位性は未達・未実証。

追加調査は学習・推論実験を実施した結果ではない。既存の確定方針を維持し、実装候補と検証条件を追加している。

## 重要な注意

公開データの「商用利用可能」は、データセット配布ライセンスだけで最終判断しない。Common Crawl由来データでは、データベースライセンスと各Web文書の著作権は別問題である。公開・販売前に、採用した各source subsetの利用条件、帰属表示、ShareAlike条件、削除要求対応を再確認する。本書は法的助言ではない。

最終更新: 2026-10-04。外部資料の調査日は各文書へ残し、研究候補と実装・実測結果を区別する。
# 次回計画の段階1〜3実行

[完結文配合の三条件100M比較](48_complete_text_10b_comparison.md): 限定data/EOS確認、25M〜50M候補pool、同じfinal10Bからの三条件学習・評価。各500M〜1B/20Bは次回以降。
