# JMicro-10M 設計・調査ノート

Phase 6①②③完了（2026-10-03）: train 756,087,912 unique stream tokensの拡張shardとWSD stable/decay CLI・CUDA全state再開一致を検証。全corpus・shardの独立監査も完了。③の速度/batch・厳密再開・cold再開も完了。④以降と本学習は未開始。

このディレクトリは、日本語専用の約10Mパラメータ級Decoder-only Language Model `JMicro-10M` を、Tokenizerを含めてスクラッチ構築するための設計・調査記録である。

## 文書内のラベル

- **確定**: 会話でプロジェクト方針として合意した内容。
- **確認済み**: 添付config、本人の過去成果、または一次資料から確認した事実。
- **提案**: 現時点の推奨案。実測やA/Bテストで変更し得る。
- **要検証**: 会話中の調査で得たが、実装前に最新版・原典・ライセンスを再確認すべき内容。

## 現在の要約

- **確定**: 目標は「約10M parameters、日本語専用、短文生成と数ターンの雑談対話」。高度な推論や長文RAGではなく、狭い能力を高密度に持たせる。
- **確定**: Tokenizer、モデル重み、事前学習、Dialogue SFTまでスクラッチで構築する。
- **確定**: Phase 0〜3はiMac、Phase 4はWindows/WSL＋RTX 4090で完了。WSL package 3.0.1.0 / Ubuntu WSL 2を使用。Phase 4のNorm/default最大安定batchはeager T8K 57 / T4K 64。③でNoNorm/math最大batch 45、compiled/math最大53、Flash/compile最大111を確認。最速はFlash/compile batch 32、694,521 tokens/s。約8TBはユーザー計画で、Phase 6①②完了時のLinux空き実測は950,875,688,960 bytes（約950.9GB / 885.6GiB）。
- **選定済み（Phase 5の小予算比較）**: 本学習候補はT4K / NoQK-Norm / LR 0.002。hidden 256、13層、FFN 640、4Q/2KV GQA、SwiGLU、RoPE、RMSNorm、context 1024、tied embeddingで10,001,152 parameters。停止・反復・sampling UnicodeとNoNorm変換は未達・未対応。
- **実測済み**: 4k/8kの100M比較と近似bytes/time比較は完了。同一tokenと近い時間ではT4Kが有望、近いbytesではT8Kが僅かに良く、語彙の普遍的な優劣は断定しない。
- **確定**: 学習量は100M比較 → 500M → 1B → 2B → 5B → 10B → 20B → 50B tokensの段階評価。50Bは20B時点で改善が続く場合のみ実施する。
- **確定**: Vast.aiは初期開発には使わず、後半の並列比較・スケーリング実験に限定する。

着手順と各フェーズの目的・ゴール・成果物・完了条件は[フェーズ別実行計画](15_project_roadmap.md)を参照する。まず再現可能な最小pipeline、10B Base、Chat、量子化ローカル実行までを完成させる。20Bの比較と条件付き50B、追加アーキテクチャ研究は後続系列として判断する。

**完了範囲**: [4k/8k Tokenizer](18_phase2_completion.md)、[両モデル/cache/学習前export](19_phase3_completion.md)、GPU学習器・評価・再開・速度を検証済み。Phase 3重みはランダム初期化、Phase 4には小さい学習済み検証checkpointがある。Python 3.12.7、実行は`uv run --frozen`、依存変更は`uv add`。

**現在地**: [Phase 4の実GPU検証](21_phase4_completion.md)と[Phase 5の候補選定](23_phase5_completion.md)が完了し、Phase 6①②③完了で停止中（本学習未開始）。Base/Chatの本学習・能力目標は未達。①②は756M unique train stream tokensとWSD stable/decayのCUDA完全一致、全74 tests / skip 0、73 GPU checksを確認した。[完了証拠](26_phase6_preparation_completion.md)。最新の状態は[継続記録](autonomous_status.md)、③以降は[残りの実行計画](27_phase6_remaining_plan.md)を参照する。

**別PCでの再開入口**: [Windows/WSL＋RTX 4090の再開手順](windows_handoff.md)。GitHubの取得からHub成果物の復元、uv環境、CUDA確認、実装順までを順に実行できる。

**進め方**: 完成までの時間短縮を優先する。Phase 3の最終検証一式は実装後24.62秒で、実装・修正を含む作業時間とは別。Phase 3の再実装を移行条件にせず、既存artifactの引継ぎから進める。実装時間とGPU計算時間を分け、Phase 6③の実測694,521 tokens/sから純学習予算を更新済み。全文評価・保存・枝・調整を別計上し、完成時刻とは区別する。[詳細](15_project_roadmap.md#高速に完成させる進め方)

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
24. [24_phase6_plan.md](24_phase6_plan.md) — gateの完了/未着手、500M〜10B段階評価・予算
25. [25_phase6_preparation.md](25_phase6_preparation.md) — ①②の事前の目的、凍結条件と停止境界
26. [26_phase6_preparation_completion.md](26_phase6_preparation_completion.md) — ①②の実量、全corpus/CUDA監査、保存先、実CLI
27. [27_phase6_remaining_plan.md](27_phase6_remaining_plan.md) — ③の採用結果、再開後の④生成/変換、⑤設定凍結、本学習と完了条件
28. [28_phase6_performance.md](28_phase6_performance.md) — ③の実GPU高速化・backend実効確認・容量と厳密再開の比較
29. [29_phase6_performance_completion.md](29_phase6_performance_completion.md) — ③の採用速度・最大容量・厳密/cold再開・独立監査と停止記録

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

最終更新: 2026-10-03。外部資料の調査日は各文書へ残し、研究候補と実装・実測結果を区別する。
