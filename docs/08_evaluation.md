# 評価・Checkpoint・TDD

最終更新: 2026-10-03。Base本文NLL/BPB・生成評価とcheckpoint再開は実装・実GPU検証済み。[評価契約report](../reports/phase4/base_evaluation_contract_report.json)。Phase 4〜5のpilot devは924文書 / 共通1,633,458 canonical bytesで、モデル評価でtestは未使用。Phase 5で100件overfit、10M smoke、4本の100M、4補助checkpoint、document paired bootstrapを実施し独立監査した。[実測証拠](23_phase5_completion.md)。Chat、rollout、文法等の全件blind人手採点は未実施。以下のmetric/TDDは要件一覧で、未実施metricを達成済みとしない。

Phase 6①の新devは89,416文書 / 164,344,743 body bytes、testは89,485文書。全splitの構造・本文/token往復を監査したが、testをモデル評価・選定へ使っていない。②のCUDA dev採点は4文書の状態保全確認で、新dev全文の品質評価ではない。新devのBPBをpilot BPBの数値差として比較せず、全文採点と固定400生成の時間を別計測する。[準備の証拠](26_phase6_preparation_completion.md)、[次の評価](27_phase6_remaining_plan.md)

## 評価原則

**確定**: Tokenizerが異なるモデル間ではtoken-level perplexityを直接比較しない。4k/8kの主比較指標は同一原文集合・共通前処理のcanonical UTF-8 bytesを分母にしたBits Per Byte (BPB)とする。

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

**固定済み**: Base/Chat各100件、各dev 80/test 20をversion管理する。Phase 4に続きPhase 5のsmoke/100MでもBase dev 80×5 decoding条件を各モデルで評価し、生成IDからflagsを独立照合した。testとChatは未使用。

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
sampler epoch / block cursor / RNG state
model config
training config
tokenizer hash
dataset manifest hash
implementation hashes
```

Git commit/dirty、環境、PID/boot ticks、source snapshotはcheckpointと対応したrun.json側へ記録する。checkpointには消費digest・教師token/body bytes・sampler RNG/epoch/block位置も保存する。version 2 checkpointは完了updateで一時file→fsync→replaceし、latest.jsonへSHA-256を記録する。config/schedule/source/shard変更はresume時に拒否する。

Phase 4ではT8K/T4Kとも連続200と100+100のtoken列/loss/weights/optimizer/scheduler/RNG/samplerが完全一致した。中断後の未保存metricsはcheckpoint境界へ戻して再開する。Phase 6②は採用NoNorm・拡張shard・CUDA/BF16/math・batch 8でWSD stable 200 vs 100+100、decay 100 vs 50+50と元枝の不変性/継続一致を全state完全一致で確認した。新batch/backendは再検証が必要。

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
