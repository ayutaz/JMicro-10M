# 調査要約

更新: 2026-10-03。外部研究は2026-10-02の調査記録で、全件の最新再調査ではない。Transformer/Tokenizer/exportとAdamW＋warmup/cosineのGPU経路は実装・検証済み。[Phase 4](21_phase4_completion.md)。QK-Normなし、Muon、WSD、Layer Sharing、hybridは未実装の候補。100M比較は主要因を一つずつ扱い、Muon比較はAdamW baseline成立後に必要性を判断する。

## 結論

**提案**: v1の本命は、2024〜2026年の小型モデル研究で支持される要素を組み合わせたModern deep-thin Transformerとする。

採用候補:

- deep-thin構成
- Grouped Query Attention (GQA)
- RoPE
- RMSNorm + pre-normalization
- QK-Norm
- SwiGLU
- tied input/output embedding
- biasなし、dropout 0を初期値
- context 1024、full causal attention

[MobileLLM](https://arxiv.org/abs/2402.14905) はsub-billionモデルでdeep-thin、embedding sharing、GQA、immediate block-wise sharingを検証している。[Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) はGQA、SwiGLU、RoPE、RMSNormに加えQK-Normを採用している。これらは10Mでの勝利を直接保証するものではないが、初期baselineとして根拠が強い。

## 採否一覧

| 技術 | v1 | 判断 |
|---|---|---|
| Deep-thin | 採用 | 小型モデルのparameter budgetを層へ回す |
| GQA 4Q/2KV | 採用 | attention parametersとKV cacheを削減 |
| RoPE | 採用 | learned absolute positionより現代的で実装例が多い |
| RMSNorm | 採用 | Llama/Qwen系の標準的な軽量構成 |
| QK-Norm | 採用候補 | parameter増が小さく、学習安定性を期待。100M-token runで有無を確認 |
| SwiGLU | 採用 | MobileLLM等で小型モデルへの有効性が報告される |
| ReLU² | 比較候補 | gate projectionを省けるが10M日本語での優位性は未確立 |
| tied embedding | 採用 | 10Mでは語彙層の比率が大きく、節約効果が大きい |
| Layer Sharing | v2比較 | parameter数を増やさずlogical depthを増やす |
| Mamba2 hybrid | 後半候補 | 長文効率は魅力だがcustom kernel/runtime依存が増える |
| LFM2風Conv + Attention | 後半候補 | CPU推論向けに魅力的だが公式scale studyは350M以上が中心 |
| MoE | 不採用 | 10Mでは複雑さに対する利益が不明確 |
| 長文local/global attention | 不採用 | context 1024ではv1の必要性が低い |

## Layer Sharing

**提案**: 通常版を完成後、12 unique layersを各2回適用する`JMicro-10M-LS`を作る。

```text
12 unique / 12 logical  -> JMicro-10M-T
12 unique / 24 logical  -> JMicro-10M-LS
```

parametersはほぼ同じでcomputeは約2倍になる。MobileLLMのblock sharingは有力な根拠だが、10M・日本語・context 1024では独自検証が必要である。

## Mamba2 / LFM2をv1にしない理由

[Mamba-2](https://arxiv.org/abs/2405.21060) は長いsequenceで効率的だが、今回のcontextは1024であり、CUDA/Tritonや専用kernelへの依存が増える。[Pebble-10M](https://huggingface.co/basically-ai/Pebble-10M) は6 Mamba2 + 2 Attention、約25B tokensという重要な10M級先行例だが、custom codeと`mamba-ssm`等が必要である。

[LFM2 Technical Report](https://arxiv.org/abs/2511.23404) はgated short convolutionと少数のGQA blockを組み合わせ、edge CPUを意識したhardware-in-the-loop探索を行っている。ただし公開scaleは350M以上が中心なので、10Mでの最適性は要検証である。

## 学習方法に関する結論

**提案**:

1. 最初はAdamWとSwiGLUで、原因を切り分けやすいbaselineを作る。
2. 100M-token規模で4k/8k、QK-Norm、learning rateを一要因ずつ比較する。AdamW成立後、必要ならMuon+AdamWを別LRで比較する。
3. 1Bで候補を2つ程度へ絞り、5Bで本命を1つ決める。
4. 10BでBase v1、20BでBase v2を評価する。
5. 能力が頭打ちでなければ50Bへ進む。
6. Base完成後にDialogue mid-trainingとSFTを行う。
7. teacher distillationはbaseline完成後の改善実験とする。
