# 評価・Checkpoint・TDD

## 評価原則

**確定**: Tokenizerが異なるモデル間ではtoken-level perplexityを直接比較しない。4k/8kの主比較指標は同一raw bytesに対するBits Per Byte (BPB)とする。

**提案（実装上の具体化）**: 同一原文集合と共通前処理を固定し、実際に予測したcanonical UTF-8 bytesをBPBの分母とする。本文NLLの総和を使い、特殊tokenの損失は分離する。文脈量、同一学習bytes／GPU時間、統計比較、Chat rubricの仕様は[評価・配布調査](14_evaluation_deployment_research.md)を参照する。

## Base model評価

必須metric:

- validation loss
- BPB
- tokenizerごとのperplexity（同一Tokenizer内の推移用）
- chars/token、bytes/token
- 日本語文字率
- byte fallback率
- repetition率
- EOS到達率と生成長分布
- 文字化け・不正Unicode率
- tokens/sec、VRAM、GPU utilization

評価corpusはtrainingとdocument単位で分離し、Tokenizer比較では全く同じraw textを使う。

## 固定生成suite

**提案**: Base向けに100〜500件をversion管理する。

- 文章completion
- 日常的な日本語文法
- 簡単な常識
- 短いQA
- 指示ではない自然文の続きを生成
- 固有名詞、数字、日付、句読点
- 短期context

temperatureやseedを固定したdeterministic setと、複数seedで分布を見るsampling setを分ける。

## Dialogue評価

SFT後は以下のcategoryを固定する。

- 挨拶
- 日常会話
- 感情応答
- 質問返し
- 話題継続
- 曖昧な発話
- 否定・訂正
- 2〜数ターン文脈
- 役割tokenの混同耐性

評価軸:

- 文法成立
- 入力との関連性
- 反復
- 自己矛盾
- 文脈維持
- 返答長
- EOS
- 事実性は参考値として分離

人手評価rubricと自動評価を分け、LLM judgeを使う場合はjudge名、prompt、versionを保存する。

## Checkpoint内容

**確定**: checkpointには以下を含める。

```text
model weights
optimizer state
scheduler state
global step / tokens seen
Python / NumPy / PyTorch / CUDA RNG state
dataloader shard and offset
model config
training config
git commit
tokenizer hash
dataset manifest hash
environment metadata
```

100 steps学習 → save → resumeしたrunと、停止せず200 steps学習したrunのloss・weightsが許容誤差内で一致することをテストする。

## TDD方針

**確定**: 最低限、以下を自動テストする。

### Model

- parameter countが9.5M〜10.1M
- tensor shapeとdtype
- tied embeddingの同一性
- causal maskが未来tokenを遮断
- Q/K/V head mappingがGQA仕様どおり
- forward/backwardでfinite lossとgradient

### Generation

- cached generationとnon-cached generationのlogits一致
- EOS停止
- greedy generationのdeterminism

### Tokenizer

- round-trip
- byte fallback
- 特殊token atomicity
- 4k/8k report再現性

### Data

- shard boundaryを跨ぐbatch
- shard checksum
- resume時のtoken位置一致
- train/validation document重複の検知

### Training

- 小データ100件をmemorizeできる
- gradient accumulationと大batchの近似一致
- save/resume一致
- NaN/Inf検知

## 実験台帳

全runに一意なIDを付け、config、data hash、code commit、開始/終了時刻、tokens seen、最良metric、失敗理由を表へ残す。成功runだけでなく失敗runも削除せず、再実行条件を明確にする。
