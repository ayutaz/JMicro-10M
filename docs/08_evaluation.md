# 評価・Checkpoint・検証

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

最新RDropはDEV256 BPB/Japanese診断と全80のraw/prefix/停止/反復/内容を確認して不採用。paired一貫性差+2/80、95%CI[0,.0625]は元+8/CI下限>0を満たさない。文法47/80・一貫性3/80等の絶対条件も未達。Codex非blind、独立人間blind未実施。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## 設計・手順の保存記録

以下は作成時点の仕様・調査・復元手順。途中の「最新」「次は」「未実施」やPIDはその時点の記録で、現在の状態は本ページ冒頭と148を参照する。外部サービス/依存の最新仕様は今回再照会していない。

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
