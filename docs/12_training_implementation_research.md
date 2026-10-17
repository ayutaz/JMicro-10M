# モデル実装・段階学習・実行環境の追加調査

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

RDropの通常lossは最大48×1024二重graphでOOM、解析VJP/CPU一括target runtimeは全数値・再開・cache照合に合格。その当時は旧累積予算で科学を閉鎖したが、新資源契約で初めて科学25Mを実施し品質不合格だった。技術合格・旧費用閉鎖・今回品質拒否を区別し、閉じたprobeを再実行しない。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## 設計・手順の保存記録

以下は作成時点の仕様・調査・復元手順。途中の「最新」「次は」「未実施」やPIDはその時点の記録で、現在の状態は本ページ冒頭と148を参照する。外部サービス/依存の最新仕様は今回再照会していない。

## 1. QK-Normの仕様を固定する

**確認済み**: TransformersのQwen3実装は、Q/Kの各headの最後の`head_dim`軸へRMSNormを適用し、その後RoPEを適用する。Q用・K用それぞれのgainは`head_dim`個で、同じ種類のhead間で共有する。attention scaleは`1/sqrt(head_dim)`。単位長へL2正規化する別形式とは区別が必要。[Qwen3公式実装](https://github.com/huggingface/transformers/blob/main/src/transformers/models/qwen3/modeling_qwen3.py)

**提案**: 初期実装は次の順序とし、QK-Normなし版は当該処理だけを省略する。

```text
hidden -> pre-RMSNorm -> Q/K/V projection
       -> reshape [B, heads, T, 64]
       -> QとKだけhead次元RMSNorm
       -> Q/KへRoPE（絶対token位置を使用）
       -> cache更新 -> causal GQA -> output projection
       -> residual -> pre-RMSNorm -> SwiGLU -> residual
```

設定に`qk_norm_type: rms_head_shared`、`rms_norm_eps`、`rope_theta`、RoPEの回転layout、`attention_scale`を記録する。初期候補はeps `1e-6`、theta `10000`、全64次元回転、scale `0.125`。これらは小型日本語モデルでの優位性を確認した値ではない。Norm統計とRoPE周波数計算はFP32を候補にし、出力を演算dtypeへ戻す。

### parameter countの再計算

**設計からの計算**: hidden `h=256`、head dim `d=64`、Q heads 4、KV heads 2、FFN幅`f`、層数`L`、語彙`V`、biasなしの場合。

```text
Embedding（共有） = V*h
Attention/block = h*(4d + 2d + 2d) + (4d)*h = 196,608
SwiGLU/block = 3*h*f
Norm/block = 2*h + 2*d = 640
Final Norm = h
N = V*h + L*(196,608 + 3*h*f + 640) + h
```

| 構成 | QK-Normなし | head間gain共有のQK-Normあり | 初期設計の旧概算 |
|---|---:|---:|---:|
| T8K: V=8192,L=12,f=576 | 9,771,264 | 9,772,800 | 9,775,872 |
| T4K: V=4096,L=13,f=640 | 10,001,152 | 10,002,816 | 10,006,144 |

既存概算はQ/K gainが合計384個/blockなら一致する。これはheadごとに別gainを持つ場合の個数で、Qwen3式の128個/blockとは異なる。規模への影響は小さいが、export互換性とテストの期待値に影響する。最終値は実装後に共有parameterを重複計数せず検証する。

## 2. KV cacheとcausal mask

**確認済み**: PyTorch SDPAのboolean maskは`True`が参照許可。非正方形の`is_causal=True`は左上整列であり、GQAにもhead数等の制約がある。使えるbackendはversion・入力形状・dtypeに依存する。[SDPA公式仕様](https://docs.pytorch.org/docs/2.14/generated/torch.nn.functional.scaled_dot_product_attention.html)

**提案**: maskを以下の3ケースに分ける。

| 場面 | Query／Key長 | mask仕様 |
|---|---|---|
| 学習・paddingなしprefill | T／T | `is_causal=True` |
| 1-token decode・有効cacheのみ | 1／past+1 | 全keyが過去または現在なので`is_causal=False` |
| cacheへのchunk追加 | q／past+q | `key_position <= past_length + query_index`を明示、`is_causal=False` |

paddingを含むbatchでは有効keyの条件も追加する。未使用cache領域を参照許可しない。たとえばpast=5、q=2なら、最初のqueryが参照できるのはkey 0〜5、次は0〜6。`tril(2,7)`とは一致しない。

cache内にはQK-Norm・RoPE後のKと、Vを保持する案とする。既存cacheにRoPEを再適用しない。prefillとdecodeで同じ絶対位置を使い、1024超過時はv1では会話履歴を切り詰めて再prefillする。位置外挿の性能は保証しない。

必須検証は全系列forwardとの各位置logits一致、1-token／複数tokenのcache更新、未来token変更が過去logitsへ影響しないこと、paddingとcache長が異なるbatch。まずFP32 math backendで正しさを確認し、その後BF16と高速backendを確認する。

## 3. 初期化・optimizer・precision

**確認済み**: Qwen3のconfigには初期化幅とNorm eps等があり、未指定の既定値へ依存しない設計が必要。Muonの公式実装はhidden行列を対象とし、embedding、output、gain、biasにはAdamWを使う。[Qwen3 config](https://github.com/huggingface/transformers/blob/main/src/transformers/models/qwen3/configuration_qwen3.py)、[Muon](https://github.com/KellerJordan/Muon)

**提案**:

- 全重みはランダム初期化。Linear／Embeddingのnormal std `0.02`、Norm gain `1`を最初の比較基準とし、初期化方式をconfigへ保存する。
- まずAdamWのみ。LR `1e-3/2e-3/3e-3`は候補で、batch・更新回数とセットで調整する。betas `(0.9,0.95)`、eps `1e-8`、weight decay `0.1`、clip norm `1.0`を探索の初期値とする。
- weight decayはLinear行列に適用し、Normには適用しない。共有Embeddingへのdecay有無は明示する。共有Embeddingをoptimizerへ2回登録しない。
- FP32 parameter／optimizer stateを保持し、CUDA autocast BF16でforwardを計算する案をbaselineにする。BF16 parameterへ直接更新する設計は別実験。
- AMP時のCrossEntropy等のdtype挙動を採用versionで確認する。独自lossで全logitsをFP32へ変換すると一時メモリが増える点も測る。[PyTorch AMP仕様](https://docs.pytorch.org/docs/2.14/amp.html)
- AdamWの`fused=True`は対応環境で速度比較する。[AdamW公式仕様](https://docs.pytorch.org/docs/main/generated/torch.optim.AdamW.html)

MuonのLRをAdamWと同じ数値で比較しない。Muonと補助AdamWは別LRを持ち、実装commit、矩形行列のscale規則、Newton–Schulz反復数、各parameter groupを記録する。同じtokensと同じ壁時計時間の両面で比較する。

## 4. tokensだけでなくoptimizer更新回数を管理する

**設計からの計算**: effective batchが262,144 tokensなら、100M-token runは約381.5更新しかない。1M-token warmupは約3.8更新になる。小探索で大きなbatchを使うと、LR／Norm比較の結果が少ない更新回数に支配され得る。

**現在の実測**: Phase 5はeager/math・micro batch 8・effective 8,192 tokens/updateで12,208更新を固定した。小探索の更新数確保と厳密resumeのための設定で、最大VRAM活用ではない。③でmath/compiled-math/Flashの最大容量・再開一致・速度を別測定し、Flash＋compile batch 32（32,768 input tokens/update）を採用した。独立1286 checks・cold再開26 checksも通過。長期のLR0.002/WSD global305,176更新・各観測点5%独立decayを⑤で[version2](../configs/phase6/base_frozen.json)へ凍結済み。

**当初の提案**: GPUを埋めるmicro batchと、統計的なeffective batchを分ける。100M探索ではeffective batch 16,384／32,768／65,536 tokens等を候補にし、約6,104／3,052／1,526更新を確保する。メモリと速度測定後に一つへ固定して主要因を比較する。warmupはtokensとstepsの両方で記録する。

SFTでは有効なAssistant教師token数がbatchごとに違う。gradient accumulation時はmicro batchごとの平均lossを単純平均せず、全micro batchの教師tokenに対するloss総和／教師token総数へ正規化する。

## 5. 終点を延長できる学習率

**確認済み**: cosineは総学習step数を必要とする。WSDはwarmupと安定区間を進め、必要な予算でdecay枝を作る方式として研究されている。2026年のWSqDは安定区間を逆平方根型へ変更する候補だが、10M日本語での検証ではない。[WSD研究](https://arxiv.org/abs/2410.05192)、[WSqD研究](https://arxiv.org/abs/2607.10959)

**提案**:

- 100M探索は終点固定のwarmup＋cosineを使い、設定を揃える。
- 長期系列はPhase 5でWSD採用を決定し、Phase 6②でstable/decay実装とCUDA全state完全一致を検証済み。凍結した準備configは200更新/100追加更新で、本学習の数値配分はversion2へ凍結済み。継続用のstable checkpointと、評価用のdecay済みcheckpointを別artifactにする。以下の9B+1B等は当初の例で、実行configではない。[①②完了証拠](26_phase6_preparation_completion.md)、[本学習以降の計画](27_phase6_remaining_plan.md)
- 10B評価枝を作るなら、たとえば9Bで分岐し1Bをdecay。継続枝も9Bから10Bへ進める。20B評価枝は19Bで同様に分岐する。decay 10%は初期案で、最適値ではない。
- 評価枝の追加計算も累積GPU時間へ計上し、`tokens_seen`は各枝の履歴に対する値として扱う。
- decay済み10Bから20Bへ継続する場合は、LR再上昇を含む別の実験条件とし、stable枝からの継続と混同しない。

「100Mごとにcosineをゼロまで落として再起動」を、連続50B学習と同じscaling曲線として扱わない。Stage Bのmixture変更もscalingと分離し、10B／20Bの固定mixture比較を少なくとも一系列残す。

## 6. 10Mでもlogitsは大きい

**設計からの計算**: T8K、B=64、T=1024で全logits `[64,1024,8192]`をBF16保存すると1GiB、FP32なら2GiB。backward、一時buffer、12層分のactivationは別に必要。weight tyingは保存parameterを減らすが、全語彙へのoutput projectionの計算は残る。

**提案**: 最初は通常CrossEntropyで正しさを確認する。profilingでhead／lossが制約と分かってから、LM headとCrossEntropyをtoken単位で分割する実装やfused lossを検討する。logits生成後の分割だけでは元の1GiBを削減できないため、projection前のhiddenを分割する。変更後はlossとgradientの一致を確認する。

## 7. 4090 benchmarkと時間見積もり

**確認済み**: PyTorchのbenchmarkはwarmupとCUDA同期の重要性を説明する。WSLのCUDAはWSL 2環境を対象とし、Windows側driverを利用する。WSL内へLinux GPU driverを別途インストールしない。[PyTorch benchmark](https://docs.pytorch.org/tutorials/recipes/recipes/benchmark.html)、[NVIDIA WSL guide](https://docs.nvidia.com/cuda/wsl-user-guide/)

**提案**: 「WSLパッケージversionが3.x」等と、distributionがWSL 1／2のどちらかを区別する。PowerShellの`wsl --version`と`wsl -l -v`、Linux側のOS、driver、PyTorch、CUDA runtime、BF16可否を記録する。調査環境のMacから学習機の性能を推定しない。

benchmarkはT4K／T8Kそれぞれで、micro batch 8→16→32→64…、eager／compile、実際のSDPA backend、fused AdamWの有無を段階比較する。最初はsynthetic token、次に実shardを使用し、forward＋loss＋backward＋optimizer stepを計測する。

compile初回時間、steady-state中央値／p95、最大allocated／reserved VRAM、data wait、実処理tokens/sec、有効教師tokens/secを保存する。MFUは`6N`だけの近似か、attention・output headまで含む推定かを明記する。

以下は**単純な算術例であり4090の実測値ではない**。処理時間は`tokens / 実測tokens_per_second`。評価・保存・停止・decay枝は別加算する。

| 仮の速度 | 1B | 10B | 20B | 50B |
|---:|---:|---:|---:|---:|
| 20k tokens/sec | 0.58日 | 5.79日 | 11.57日 | 28.94日 |
| 50k | 0.23日 | 2.31日 | 4.63日 | 11.57日 |
| 100k | 0.12日 | 1.16日 | 2.31日 | 5.79日 |
| 200k | 0.06日 | 0.58日 | 1.16日 | 2.89日 |

## 8. 再開時の一致を成立させる

**確認済み**: PyTorchはrelease、platform、CPU／GPUが異なる条件で完全再現を保証しない。deterministic algorithmには速度とのtradeoffがある。[再現性の公式説明](https://docs.pytorch.org/docs/2.14/notes/randomness.html)

**提案**: 必須要件を「同一hardware・依存version・backend・configでの中断再開一致」とする。portableなbitwise一致は要求しない。

追加保存項目は、source mixture samplerのRNG、shard順、epoch、document／token offset、完了済みoptimizer update数、loss正規化に必要なtoken counters。workerが先読みした位置ではなく、学習へ実際に渡し終えた位置を保存する。

v1は`num_workers=0`と決定的なmmap読み込みから始める。遅い場合だけworker／prefetchを導入し、導入後もtoken列一致を確認する。checkpointはoptimizer更新完了点で保存し、勾配蓄積途中の保存はv1では行わない。保存は一時file→checksum確認→同一filesystemでrenameとする。

再開検証では評価がtraining RNGへ影響しないことも確認する。strict検証はFP32・決定的backend、performance検証はBF16・高速backendで許容誤差を事前定義する。単に「近いloss」だけでtoken位置のずれを見逃さない。

## 9. 過学習とデータ反復

**確認済み**: Chinchillaは計算予算下でのmodel／data配分の研究であり、固定10Mモデルを50Bまで学習したときの最適点を直接示すものではない。データ制約下の研究でも、反復tokenと新規tokenの価値を分けている。[Chinchilla](https://arxiv.org/abs/2203.15556)、[データ制約下のscaling](https://arxiv.org/abs/2305.16264)

**提案**: 10Mの50B学習は容量固定の実験として扱う。unique docs／bytes／tokens、総tokens seen、source別反復回数を保存する。validation BPB改善の信頼区間、会話失敗率、追加GPU時間を合わせて20B以降を判断する。論文の「数epochなら有効」を、日本語雑談SFTの100M反復へそのまま適用しない。

現在の`--branch-from`はstableからdecayを作る入口で、stable終端budgetを延長するforkは未実装。通常resumeでの予算変更は拒否する。20B/50Bへの継続には明示forkの履歴と全state検証を追加する。[実装上の残り](27_phase6_remaining_plan.md)

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="当時の資料保存手順"></a>
