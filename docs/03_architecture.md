# アーキテクチャ設計

更新: 2026-10-14 JST。[現在の状態](autonomous_status.md)、[最新結果141](141_chat_lr_comparison_results.md)、[ロードマップ](15_project_roadmap.md)が現在の判断の正本。研究・教材準備・診断・生成評価・学習は停止中。

## 現在の固定参照

語彙4,096、hidden256、13層、FFN640、4Q/2KV、head dim64、SwiGLU、RMSNorm、RoPE、context1024、tied embedding、biasなし、dropout0、QK-Normなし。実parameter数10,001,152。`src/jmicro/model.py` SHA256は `298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83`。元10B・後続教材比較・最新139はこのnative参照を維持しており、品質は未採用。

QK-Norm有無、T8K/T4K、ReLU²、Layer Sharing等の実装・閉じた比較は下の当時の記録と[全体125](125_project_retrospective.md)を参照する。構成変更は9.5M〜10.1M内の別proposalと比較が必要。元frozen sourceは置き換えない。

HF/GGUFの初期変換確認は基盤の証拠で、現在のSFT重みの量子化品質・配布完成ではない。

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
