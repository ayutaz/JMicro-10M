# JMicro-10M 設計・調査ノート

このディレクトリは、日本語専用の約10Mパラメータ級Decoder-only Language Model `JMicro-10M` を、Tokenizerを含めてスクラッチ構築するための設計・調査記録である。

## 文書内のラベル

- **確定**: 会話でプロジェクト方針として合意した内容。
- **確認済み**: 添付config、本人の過去成果、または一次資料から確認した事実。
- **提案**: 現時点の推奨案。実測やA/Bテストで変更し得る。
- **要検証**: 会話中の調査で得たが、実装前に最新版・原典・ライセンスを再確認すべき内容。

## 現在の要約

- **確定**: 目標は「約10M parameters、日本語専用、短文生成と数ターンの雑談対話」。高度な推論や長文RAGではなく、狭い能力を高密度に持たせる。
- **確定**: Tokenizer、モデル重み、事前学習、Dialogue SFTまでスクラッチで構築する。
- **確定**: 現在のiMacで開発し、学習時に別のRTX 4090 24GB搭載Windows PCへ切り替える。ユーザー指定WSL 3.x上のLinuxで最大安定バッチを実測して学習する。8TBストレージを前提とする。
- **提案**: 本命はModern deep-thin Transformer。8k語彙版はhidden 256、12層、4Q/2KV GQA、SwiGLU、RoPE、RMSNorm、head間gain共有のQK-Norm、context 1024、tied embeddingで約9.77M。
- **提案**: 4k語彙版も同じ約10M予算で作り、BPBと日本語圧縮率で比較する。
- **確定**: 学習量は100M → 1B → 2B → 5B → 10B → 20B → 50B tokensの段階評価。50Bは20B時点で改善が続く場合のみ実施する。
- **確定**: Vast.aiは初期開発には使わず、後半の並列比較・スケーリング実験に限定する。

着手順と各フェーズの目的・ゴール・成果物・完了条件は[フェーズ別実行計画](15_project_roadmap.md)を参照する。まず再現可能な最小pipeline、10B Base、Chat、量子化ローカル実行までを完成させる。20Bの比較と条件付き50B、追加アーキテクチャ研究は後続系列として判断する。

**現在地**: iMac上のPhase 0〜3が完了。データpilot、[4k/8k Tokenizer](18_phase2_completion.md)、[両モデル・cache・HF/native GGUF・Q8/Q4候補](19_phase3_completion.md)を検証した。モデル重みはランダム初期化。Python/依存は`uv add`で管理し、実行は`uv run`。

**次の作業**: Phase 4でWindows/WSL＋RTX 4090へ切り替え、学習器・shard・保存再開・最大安定batchを検証する。GPU学習は未実施。最新の状態は[フェーズ別計画の全体表](15_project_roadmap.md#全体の順序)を参照する。

**別PCでの再開入口**: [Windows/WSL＋RTX 4090の再開手順](windows_handoff.md)。GitHubの取得からHub成果物の復元、uv環境、CUDA確認、実装順までを順に実行できる。

**進め方**: 完成までの時間短縮を優先する。Phase 3の最終検証一式は実装後24.62秒で、実装・修正を含む作業時間とは別。Phase 3の再実装を移行条件にせず、既存artifactの引継ぎから進める。実装時間とGPU計算時間を分け、Phase 4の実測から残り時間を更新する。[詳細](15_project_roadmap.md#高速に完成させる進め方)

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
20. [20_publication_review.md](20_publication_review.md) — 公開済みデータのライセンス・個人情報確認、Tokenizer内部のローカル情報除去

実行時の仕様は[評価仕様](evaluation_protocol.md)と[Windows/WSL移行手順](windows_handoff.md)を参照する。データとTokenizerの[Hugging Face公開版の取得手順](huggingface_handoff.md)も利用できる。

## 追加調査の要点（2026-10-02）

未実装のまま残っていた技術判断を、一次資料と公式コードから補足した。最初は[追加調査の入口](11_technical_research_gaps.md)を読む。

- **提案**: QK-NormをQwen3式のhead次元RMSNormとして具体化すると、T8Kは9,772,800、T4Kは10,002,816 parametersとなる。旧概算との差はgainの共有方式による。
- **提案**: SentencePieceの正規化と構造tokenの挿入方式を固定し、本文中の役割表記と構造IDを区別する。
- **提案**: BPBに加え、同一原文bytesと同一GPU時間での比較条件を用意する。
- **提案**: 長期学習前にランダム重みでHF／GGUF互換性を確認する。FFN幅576／640ではK-quantの型fallbackを確認する。
- **確認済み**: llama.cppの一般的なSentencePiece変換経路と独自Unigramの分割方式は同一ではない。内蔵Tokenizerへの互換性を検証し、必要なら外部SentencePieceでIDを作る経路を使う。
- **要検証**: 4090実速度、4k/8kの勝者、日本語会話データの教師token量、量子化後の品質は実測待ち。

追加調査は学習・推論実験を実施した結果ではない。既存の確定方針を維持し、実装候補と検証条件を追加している。

## 重要な注意

公開データの「商用利用可能」は、データセット配布ライセンスだけで最終判断しない。Common Crawl由来データでは、データベースライセンスと各Web文書の著作権は別問題である。公開・販売前に、採用した各source subsetの利用条件、帰属表示、ShareAlike条件、削除要求対応を再確認する。本書は法的助言ではない。

最終更新: 2026-10-02
