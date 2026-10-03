# プロジェクト目的

現在地（2026-10-03）: [Phase 0〜5](23_phase5_completion.md)と[Phase 6①②](26_phase6_preparation_completion.md)と[③の高速化](29_phase6_performance_completion.md)が完了。100M比較からT4K / NoQK-Norm / LR 0.002を選定し、756M unique train stream tokens、WSD全state再開一致とFlash＋compile batch 32の694,521 tokens/sを確認して停止中（④以降・本学習未開始）。完成したBase/Chat、雑談品質、学習後の量子化・独立環境検証は未達。本書の成功条件を維持し、再開後は[③以降の実行計画](27_phase6_remaining_plan.md)と[段階評価](24_phase6_plan.md)に従う。

## ゴール

**確定**: `JMicro-10M` は、約10Mパラメータで日本語の短文生成と数ターンの自然な雑談対話を行うDecoder-only Language Modelである。既存モデルの量子化やfine-tuningではなく、以下を一つの再現可能なpipelineとして構築する。

1. 日本語コーパスの選別と記録
2. 日本語専用Tokenizerの学習
3. モデルconfigの設計とランダム初期化
4. Base modelのスクラッチ事前学習
5. Dialogue-oriented mid-training
6. Assistant応答部分だけを対象にしたSFT
7. 量子化・ローカル推論用artifactの作成

最終成果物は `JMicro-10M-Base` と `JMicro-10M-Chat` を分ける。Chatは別アーキテクチャではなく、Baseに会話形式を追加学習したcheckpointである。

## 想定ユースケース

**確定**:

- 挨拶、相づち、感情への短い応答
- 日常的な質問返しと話題継続
- 2〜数ターン程度の短い文脈維持
- 5〜10MB級に量子化可能なローカル対話モデル
- 「日本語対話能力が10M級でどこまで成立するか」の研究ベースライン

## 明示的に狙わないもの

**確定**:

- 高度な数学、コード生成、長いChain-of-Thought
- 世界知識の網羅や高い事実性
- 長文RAG、文書要約、32K級の長文脈
- 大型汎用モデルを単純に縮小した代替品

10Mでは容量が限られるため、「何でも少しできる」より「短い日本語対話を破綻しにくく行う」を優先する。

## 過去の355M級モデルとの関係

**会話で確認済み**: 本人は2024年にMistral系の日本語モデルをスクラッチ事前学習している。

- 約355M parameters級
- 独自のSentencePiece Unigram Tokenizer
- byte fallbackあり
- 日本語データを用いて約2B tokensを事前学習
- Mistralの設計を利用しつつ、configを独自に設定し、重みはrandom initialization
- 語彙50,257、入力EmbeddingとLM Headは非共有だったため、語彙関連だけで約102.9M parameters、全体の約29%を占めた

**位置付け**: 今回は「初めてLLMを作る」計画ではない。過去の355M級モデルを約35分の1へ縮小し、Tokenizer・parameter allocation・学習データの焦点を日本語短文対話向けに再設計する実験である。

| 観点 | 2024年モデル | JMicro-10M |
|---|---|---|
| Architecture | Mistral系 | Modern Llama-like Transformerを基準 |
| 規模 | 約355M | 約10M |
| Tokenizer | SP Unigram、約50k語彙 | SP Unigram、4k/8k比較 |
| Byte fallback | あり | あり |
| Embedding共有 | なし | あり |
| 学習量 | 約2B tokens | 100M〜50Bを段階評価 |
| 主目的 | 日本語Base LM | 短文対話Base + Chat |
| 実験の焦点 | pipeline成立 | 極小サイズでの能力密度とscaling |

## 成功条件

**提案**: 最初の成功条件は大型モデルとの一般性能比較ではなく、以下とする。

- 学習・resume・生成が再現可能である
- 4k/8k Tokenizerを同一validation bytes上のBPBで比較できる
- 10B-token checkpointで自然な日本語短文が一定割合で生成される
- SFT後、固定対話prompt群で入力に関連した短い応答ができる
- 反復、文字化け、EOS失敗、役割混同を定量記録できる
- BF16約20MB、INT8約10MB、INT4約5MBを目安に配布可能である

実行順序と各段階の目的・ゴールは[フェーズ別実行計画](15_project_roadmap.md)に具体化する。同計画の品質閾値は初期提案の数値を維持してPhase 5の100M結果を見る前に凍結済み。実証済みの性能とは区別し、結果を見て閾値を下げない。技術的完了、品質目標、実artifact容量の達成を別々に記録する。
