# 調査要約

更新: 2026-10-14 JST。[現在の状態](autonomous_status.md)、[最新結果141](141_chat_lr_comparison_results.md)、[ロードマップ](15_project_roadmap.md)が現在の判断の正本。研究・教材準備・診断・生成評価・学習は停止中。 外部研究は当時の資料で、今回全件の外部再調査はしていない。

現参照はnative10,001,152、Tokenizer4096、NoQK-Norm/SwiGLU/context1024。元10B Baseと後続SFTを実行したが品質未達。Layer Sharingの固定比較は実施・不採用、ReLU²の固定比較は予算gate不成立で本比較未開始・終了。これらを単なる未実装の次案へ戻さない。

最新低LR候補は新DEV内容20/80・自己文脈5/24、CI下限−1.25ポイント、反復と文字失敗が残り不採用。SFT TRAIN適合やBPB改善だけでは内容・文脈の達成を示さない。Base単独原因・10M容量限界は未確定。技術採否と後続実績は[全体記録125](125_project_retrospective.md)で追える。

## 作成時点の資料・契約

## 初期調査と当時の結論

③の高速化も[完了](29_phase6_performance_completion.md)。固定長・PADなしcausal経路とbackend別compile cacheを実装し、Flash＋compile reduce-overhead / batch 32で694,521 tokens/s、最速reference比5.436倍を実測した。容量上限111より32が速く、厳密/cold再開を通過した32を長期候補にする。④⑤の400生成・全文dev採点、NoNorm CPU精度profileの全12変換比較・実CLI149 checksと長期LR/WSD凍結も完了し、`93c7d1d`へcommitした。生成品質は未達、本学習は未開始。[④⑤の証拠](30_phase6_readiness_execution.md)。

**提案**: v1の本命は、2024〜2026年の小型モデル研究で支持される要素を組み合わせたModern deep-thin Transformerとする。

採用候補:

- deep-thin構成
- Grouped Query Attention (GQA)
- RoPE
- RMSNorm + pre-normalization
- QK-Norm（初期対照。現在の選定候補は省略）
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
| QK-Norm | 対照を保存、現在の候補では省略 | T4Kの同一100M比較でNoNormがBPB・速度改善。ただしsampling Unicode退行とHF/GGUF adapter未実装を留保 |
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

**2026-10-03当時の決定**: Phase 5の4本の100M・補助評価・独立監査は完了。Phase 6①②の拡張corpus・WSD分岐/再開も完了し停止中。次回の再開指定後に採用構成の容量/高速化、生成/変換課題を確認して本学習予算を固定する。[残りの実行計画](27_phase6_remaining_plan.md)

**初期提案（2026-10-02の調査時点）**:

1. 最初はAdamWとSwiGLUで、原因を切り分けやすいbaselineを作る。
2. 100M-token規模で4k/8k、QK-Norm、learning rateを一要因ずつ比較する。AdamW成立後、必要ならMuon+AdamWを別LRで比較する。
3. 1Bで候補を2つ程度へ絞り、5Bで本命を1つ決める。
4. 10BでBase v1、20BでBase v2を評価する。
5. 能力が頭打ちでなければ50Bへ進む。
6. Base完成後にDialogue mid-trainingとSFTを行う。
7. teacher distillationはbaseline完成後の改善実験とする。
