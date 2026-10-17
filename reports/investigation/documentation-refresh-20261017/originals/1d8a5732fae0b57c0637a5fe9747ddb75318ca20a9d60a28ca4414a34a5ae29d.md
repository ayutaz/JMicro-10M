# 評価・Checkpoint・検証

更新: 2026-10-14 JST。現在の依頼は全現行文書の最新化と今後の計画作成。Base/Chatは未完成・未採用。研究・教材準備・診断・生成評価・GPU学習は再開していない。

[最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md) / [次の計画145](145_post_rejection_next_plan.md) / [今回更新146](146_documentation_followup.md)。

最新Baseは全80のprefix/全文をCodex非blindで理由付き採点。文法23、一貫性1、適切完結2、EOS20、反復50（各80）で不採用。原DEV絶対・相対CI・strong/cached/historical保持を維持。Chat141の28セット/6,132判断/NLL7点は別の評価契約。全文DEVとDEV256、独立学習と生成seed、人間blindとCodex判断、TEST CPU解析とGPU採点を区別する。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

元Base TEST20 promptと元Chat TEST20行は別のCPU解析問題を保存した。学習・GPU TEST採点に使っていないこととCPU未解析は別。将来の有資格最終確認にはreader分離と新しい封印TESTが必要。今回data/TESTを開封・再処理しない。

次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。

## 作成時点の資料・契約

## 評価原則

③の高速化studyは4 dev文書＋1 prompt×2 greedy outputs/最大8 tokensの保存・容量確認を通過した。[③の完了](29_phase6_performance_completion.md)。独立1286 checks・cold再開26 checksは再現性の証拠で、④で全文dev BPB・固定400生成を測定し、⑤で固定dev256文書による3 LR比較を終えた。品質目標は未達のまま。CPU精度profileの変換12比較・実CLI/重み149 checks・全90 tests成功は実装契約の証拠で、文法・EOS到達の能力合格ではない。

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

## v1固定suiteの契約と当時の利用

**固定済み**: Base/Chat各100件、各dev 80/test 20をversion管理する。Phase 4に続きPhase 5のsmoke/100MでもBase dev 80×5 decoding条件を各モデルで評価し、生成IDからflagsを独立照合した。このPhase4〜5時点ではtestとChatは未使用だった。

- 文章completion
- 日常的な日本語文法
- 簡単な常識
- 短いQA
- 指示ではない自然文の続きを生成
- 固有名詞、数字、日付、句読点
- 短期context

temperatureやseedを固定したdeterministic setと、複数seedで分布を見るsampling setを分ける。

## Dialogue評価の観点

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
