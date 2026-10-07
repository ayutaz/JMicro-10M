# アーキテクチャ設計

現在の実装はQK-Normあり/なしの両方をサポートする。[Phase 5](23_phase5_completion.md)でT4K / NoQK-Norm / LR 0.002を本学習候補に選定した。ReLU²とhybridは未実装の候補。Layer Sharingは13個のnative blockを各2回使うzero-gated方式を実装・実100M学習・全80評価済みで、[既存採否](../reports/phase6/gated_shared_comparison_review.json)では不採用。下の初期Layer Sharing案を未検証の一般候補と扱わない。[反復計算の重複調査](../reports/phase6/base_recurrent_compute_novelty_review.json)を参照。設定を変える場合はparameter予算・数値一致・GPU容量を別runで検証する。NoNormのHF/Llama・GGUF/Llama adapterは実装済み。[④⑤](30_phase6_readiness_execution.md)で学習済み重みの短/1024・full/cacheの全12比較をCPU精度profileで検証した。未修正stock FP32の失敗は保持する。

**実装状況（2026-10-03）**: T8K/T4Kを実装し、実parameter数9,772,800／10,002,816、因果性、padding/cache、HF/native float GGUFをCPUで検証済み。[Phase 3完了記録](19_phase3_completion.md)。Phase 4で両モデルのCUDA/BF16学習・再開・評価・容量を検証済み。Phase 5では同一token予算と近い時間予算の結果からT4K NoNormを選定した。近いbytes予算ではT8Kが僅かに良く、モデルfamilyと予算に依存した選択。Base/Chatの品質目標は未達で、以下の派生案は研究候補として残す。

## 現在の本学習候補: T4K / NoQK-Norm

語彙4,096、hidden 256、13層、FFN 640、4Q/2KV、head dim 64、SwiGLU、RMSNorm、RoPE、context 1024、tied embedding、biasなし、dropout 0。Q/K head NormをIdentityへ置き換え、gainは持たない。実parameter数 **10,001,152**。[実行configとcheckpoint hash](../reports/phase5/candidate_configs.json)

主比較のdev BPB 1.221443、共通短文BPB 1.546589。greedy EOS0/80、反復54/80、sampling Unicode2/240という未達がある。採用はPhase 6の比較候補であり、品質目標の達成とは区別する。CPU精度profileと外部SentencePieceの実CLI・変換契約は検証済みで、学習後量子化品質は未検証。[採否理由](../reports/phase5/candidate_selection_review.md)、[次の準備](24_phase6_plan.md)

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
