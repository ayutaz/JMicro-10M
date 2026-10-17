# 調査要約

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

Tokenizer/model/学習/再開基盤は成立している一方、文法やEOSの改善は意味の一貫性改善を保証しない。ScaleGradは文法44→71・反復53→6でも一貫性7/80、BPB悪化で不採用。RDropも一貫性3/80で不採用。SFT141までの失敗を含め、Base単独原因や10M容量限界は確定していない。外部論文の以下の記述は当時の調査記録。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## 設計・手順の保存記録

以下は作成時点の仕様・調査・復元手順。途中の「最新」「次は」「未実施」やPIDはその時点の記録で、現在の状態は本ページ冒頭と148を参照する。外部サービス/依存の最新仕様は今回再照会していない。

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
