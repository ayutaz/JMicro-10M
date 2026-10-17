# アーキテクチャ設計

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

現参照はnative10,001,152 parameters。13層・hidden256・FFN640・4Q/2KV・head64・vocab4096・context1024・NoQKNorm/SwiGLU・tied embedding。最新RDropは学習時のみdropout/損失を追加し、推論構成・パラメータ数を変更していない。9層FFN1040および6層hidden384/FFN832の300M比較は既に不採用で、未検証案として再掲しない。9.5M〜10.1Mと原品質を維持する。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## 設計・手順の保存記録

以下は作成時点の仕様・調査・復元手順。途中の「最新」「次は」「未実施」やPIDはその時点の記録で、現在の状態は本ページ冒頭と148を参照する。外部サービス/依存の最新仕様は今回再照会していない。

## 作成時点の資料・契約

## 初期baseline: JMicro-10M-T8K

**提案**:

```yaml
architecture: decoder-only-transformer
vocab_size: 8192
hidden_size: 256
num_hidden_layers: 12
num_attention_heads: 4
num_key_value_heads: 2
head_dim: 64
intermediate_size: 576
activation: swiglu
norm: rmsnorm
qk_norm: true
position_embedding: rope
max_position_embeddings: 1024
attention: full-causal-gqa
tie_word_embeddings: true
attention_bias: false
mlp_bias: false
dropout: 0.0
```

QK-Normをhead間gain共有のhead次元RMSNormとする実装で、パラメータ数9,772,800（約9.77M）を確認した。旧概算9,775,872との差はQ/K gainの共有方式による。[追加調査の計算式](12_training_implementation_research.md)と[実測report](../reports/phase3/model_contract_report.json)を参照する。

| 部分 | 概算 |
|---|---:|
| tied token embedding | 2.10M |
| Attention × 12 | 約2.36M |
| SwiGLU FFN × 12 | 約5.31M |
| Norm等 | 微量 |
| 合計 | 約9.77M |

## 比較: JMicro-10M-T4K

**提案**:

```yaml
vocab_size: 4096
hidden_size: 256
num_hidden_layers: 13
num_attention_heads: 4
num_key_value_heads: 2
head_dim: 64
intermediate_size: 640
tie_word_embeddings: true
```

同じhead間gain共有のQK-Normなら設計上10,002,816 parameters（約10.00M）。旧概算10,006,144との差はNorm仕様による。4kで節約したembedding予算を1層追加と広いFFNへ再配分する。

| 項目 | T4K | T8K |
|---|---:|---:|
| Vocab | 4,096 | 8,192 |
| Hidden | 256 | 256 |
| Physical layers | 13 | 12 |
| FFN | 640 | 576 |
| Params | 約10.00M | 約9.77M |
| 日本語token圧縮 | 不利の可能性 | 有利の可能性 |
| Transformer容量 | やや多い | やや少ない |

勝者はparameter数やtoken-level perplexityではなく、同一validation bytesに対するBPB、chars/token、会話評価で決める。

## Attention

**確定**: contextはまず1024。短文対話を対象とするため、v1はfull causal attentionとする。

**提案**: 4 query heads / 2 KV heads、head_dim 64のGQAを使う。QK-Normを有効化した初期baselineを保持する。Phase 5のT4K A/BではNoNormを選定し、CUDA厳密resume・有限値・生成条件も照合した。

**提案（追加調査）**: QK-NormはQ/Kそれぞれのhead次元RMSNorm、head間gain共有、RoPEの前、attention scaleは`1/sqrt(64)`として具体化する。cache使用時のmask、RoPE位置、初期化の仕様は[モデル実装調査](12_training_implementation_research.md)、HF／GGUFと量子化の制約は[配布調査](14_evaluation_deployment_research.md)を参照する。CPUのHF/native float GGUF parityはPhase 3で実測済み、GPUのcompile BF16 parityはPhase 4で確認した。学習後のexportと量子化品質は未検証。

## FFN

**提案**: v1はSwiGLU。ReLU²は同一parameter budget・同一data orderの比較実験とし、baseline実装を複雑にしない。

## Layer Sharing版

**提案**: `JMicro-10M-LS` はT8Kの12個のunique blockを各2回適用し、24 logical layersにする。

- model parameters: 約9.8Mのまま
- embedding: T8Kと共有設計
- compute: おおむね2倍
- 比較条件: tokens seen、data order、optimizer、LR scheduleを揃える

## 後半候補

| 名称 | 構成案 | 目的 |
|---|---|---|
| JMicro-10M-M | 6 Mamba2 + 2 Attention、hidden約384、vocab 2k〜4k | Hybridのsequence効率検証 |
| JMicro-10M-C | gated short Conv主体 + 少数GQA | CPU推論速度検証 |

これらはTransformer baselineと評価pipelineが完成してから着手する。

## 実装上の不変条件

- parameter countは9.5M〜10.1Mに収める
- future tokenを参照しない
- cached/non-cached generationのlogitsが許容誤差内で一致する
- tied embeddingが実際に同一parameterを参照する
- padding tokenをloss対象から除外する
- configだけでモデルを完全再構築できる

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="現在の固定参照"></a>
