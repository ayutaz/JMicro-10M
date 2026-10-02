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
- **確定**: 主学習環境は手元のRTX 4090 24GB搭載Windows PCとWSL。8TBストレージを前提とする。
- **提案**: 本命はModern deep-thin Transformer。8k語彙版はhidden 256、12層、4Q/2KV GQA、SwiGLU、RoPE、RMSNorm、QK-Norm、context 1024、tied embeddingで約9.78M。
- **提案**: 4k語彙版も同じ約10M予算で作り、BPBと日本語圧縮率で比較する。
- **確定**: 学習量は100M → 1B → 2B → 5B → 10B → 20B → 50B tokensの段階評価。50Bは20B時点で改善が続く場合のみ実施する。
- **確定**: Vast.aiは初期開発には使わず、後半の並列比較・スケーリング実験に限定する。

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
10. [10_next_steps.md](10_next_steps.md) — 実装順序と完了条件

## 重要な注意

公開データの「商用利用可能」は、データセット配布ライセンスだけで最終判断しない。Common Crawl由来データでは、データベースライセンスと各Web文書の著作権は別問題である。公開・販売前に、採用した各source subsetの利用条件、帰属表示、ShareAlike条件、削除要求対応を再確認する。本書は法的助言ではない。

最終更新: 2026-10-02
