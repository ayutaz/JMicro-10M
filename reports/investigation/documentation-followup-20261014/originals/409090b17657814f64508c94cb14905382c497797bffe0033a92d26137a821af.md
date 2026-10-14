# Phase 5完了: 小予算の学習検証と候補選定

2026-10-03、WSL 2 / Ubuntu / RTX 4090上でPhase 5を完了した。Python 3.12.7はuv管理。runは23 stageを終了し、最終独立監査が成功した。Phase 6本学習は開始せず、今回の境界で停止する。

## 目的・計画・完了条件の照合

目的は小予算で学習実装の問題を発見し、本学習へ渡す候補を最大2つ選ぶこと。[詳細計画](22_phase5_plan.md)と[凍結run plan](../reports/phase5/plan.json)に予算・条件を固定した。自然な雑談の完成はPhase 5の条件ではないが、将来の品質目標は維持する。

| 要件 | 実際の証拠 |
|---|---|
| 実装検証・厳密保存再開 | 全68 tests、failure/error/skip 0。T8K/T4K/文書overfit/NoQK-NormのCUDA連続200 vs 100+100でweights・optimizer・scheduler・RNG・sampler・loss・消費列が一致。[resume](../reports/phase5/resume_report.json)、[独立監査](../reports/phase5/independent_audit.json) |
| train 100件overfit | 6,000更新、NLL/token 0.012770、teacher accuracy 99.712%、16-token continuation exact 100%、末尾EOS argmax/実生成100%。全5 gate成功。[生report](../reports/phase5/overfit_report.json) |
| 別runの10M smoke・実際の保存再開 | 600更新で保存・再開し1,221更新 / 10,002,432 tokens。全更新・checkpoint有限、dev BPB 2.747870→1.416968。[training audit](../reports/phase5/smoke_training_audit.json)、[評価](../reports/phase5/smoke_evaluation_audit.json) |
| T4K/T8K、Norm、LRの100M比較 | 各12,208更新 / 100,007,936 tokens。全loss/gradient/weights/optimizer有限、初期dev BPBより改善。Norm/LRはarchitecture/config/消費digestの単一要因検証。[比較](../reports/phase5/tokenizer_model_comparison.json) |
| 共通bytes・短文・生成の公平な評価 | 同じdev 924文書 / 1,633,458 bytes、同じ32短文window、80固定Base dev×5条件で各400生成。IDからflagsを再計算。test/Chat suiteは未使用。[集約](../reports/phase5/evaluation_summary.json) |
| 補助bytes/time予算 | 実metricsから近い保存点を独立に再選択し、4 checkpointで全devと短文を採点。実tokens/更新/bytes/時間差を併記し、近似と明記。[補助証拠](../reports/phase5/evaluation_summary.json) |
| 候補configと採用・棄却理由 | T4K / NoQK-Norm / LR 0.002を1候補に選定。[configとcheckpoint hash](../reports/phase5/candidate_configs.json)、[判断の詳細](../reports/phase5/candidate_selection_review.md) |
| 品質基準の凍結・失敗保存・永続実行 | 100M前にtargets.statusをfrozenへ変更し数値を維持。失敗を保存して閾値を緩めず修復。job PID/boot/start ticks・snapshot・ログ・checkpointをWSLへ保持。[失敗](../reports/phase5/failed_attempts.json)、[停止確認](../reports/phase5/process_completion.json) |

## 比較結果と判断

BPBは小さい方が良い。全主比較は同一stream-token予算・seed 42。共通短文と全devは学習へ混ぜない。

| 構成 | dev BPB | 共通短文 BPB | 定常 tokens/s | 抑制greedy EOS / 80 | 反復 / 80 |
|---|---:|---:|---:|---:|---:|
| T8K / QK-Norm / LR 0.002 | 1.258861 | 1.650058 | 117,119 | 0 | 54 |
| T4K / QK-Norm / LR 0.002 | 1.231823 | 1.591386 | 111,693 | 0 | 53 |
| **T4K / NoQK-Norm / LR 0.002** | **1.221443** | **1.546589** | **121,139** | **0** | **54** |
| T4K / NoQK-Norm / LR 0.001 | 1.235002 | 1.618124 | 121,046 | 0 | 52 |

T8K−T4K NormのBPB差0.027038（95% CI 0.024808〜0.029387）、Norm−NoNorm差0.010379（0.008505〜0.012258）。低LRはNoNorm基準より0.013558悪化（0.011594〜0.015443）。選択候補は約10.001M parameters。候補checkpoint SHAは`e5583927efc5aa2041648bcae23f1b618b70f002be334c3581dea23472447d07`。

一方、近いbytes予算ではT8K BPB 1.200920 / T4K 1.203982、近い更新時間ではT8K 1.212407 / T4K 1.194784となった。近似のbytes差約2.47%・時間差約5.62%と、schedule位置・architecture寸法の差がある。語彙のみの因果比較や、4kの普遍的優位とは呼ばない。paired CIはdocument samplingの不確実性で、単一学習seedの変動を測った値ではない。

## 未達の品質と修復の記録

候補のgreedy EOSは0/80で、停止目標は未達。samplingではUnicode破綻2/240、EOS2/240、反復8/240。NormありT4Kのsampling Unicodeは0/240であり、NoNormの退行を明示する。HF/GGUFのNoNorm adapterは未実装。Base文法、Chat関連性/文脈、量子化品質は達成したと扱わず、Chat/test suiteも未実施。生成flagsは診断であり、文法等の全件blind人手採点ではない。[品質の詳しい限界](../reports/phase5/candidate_selection_review.md#生成品質と進行条件)

compile/defaultとeager/defaultは厳密resume不一致で棄却した。eager/mathで一致を確保した後、固定連結block overfitはtrain loss約0.002でも文書単独の再現2%となり不合格。train文書単位windowのsamplerへ修復し、同じ6,000更新上限・同じ閾値で再実行して合格した。元の失敗run/checkpointは保持した。smoke/100Mのblock samplerは維持した。

pilotのunique trainは18,022文書 / 32,774,150 body bytes、T8K 6.884M / T4K 8.398M stream tokens。100Mは約14.53 / 11.91倍のstream-token曝露であり、unique 100Mを取得した結果ではない。途中checkpointが終端より良いBPBになる点もあり、反復pilotの予算増加だけで改善すると保証しない。

## 実時間・容量・保存先

100M学習4本のworker実時間合計は約**57.57分**。smokeと4本の生成評価worker合計は約**29.07分**。修復runの23 stageは11:51:33〜13:27:24 JST、約95分51秒。resume、overfit、補助評価も別stageとして記録し、以前の実装・失敗修復時間はこの合計へ含めない。[実測予算](../reports/phase5/resource_budget.json)

修復runの永続成果物は8,733,349,784 apparent bytes（約8.13 GiB）、checkpoint 73 files。失敗runも別途保持する。Linux空きは約969.7GB。uv cache/venv等はこのrun容量に含めず、hardlink重複を除去した値でもない。学習はmath / batch 8でピークallocated VRAM約3.9〜4.5 GiB。最大VRAM活用・高速化完了ではなく、compile/defaultの高速測定は厳密resumeを通過していない。[速度と制約](../reports/phase5/performance_status.md)

全raw evidence・snapshot・metrics・checkpointの保存先はWSL `/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase5/run-20261003-docoverfit/`。shardsは`~/jmicro-data/shards/`。Windowsに小さいJSON/MD/XMLを保存し、指定Git identityでコミットする。大型checkpointのGit追加・push・公開は行わない。

独立監査の再実行はWSL checkoutで:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/audit_phase5.py --run reports/phase5/run-20261003-docoverfit --output reports/phase5
```

## 次回の境界

ユーザーがPhase 6を再開した場合、拡張train corpus、WSDのstable継続/decay評価分岐と保存再開、math/compile/batchの実容量・速度を検証し、実測予算を固定してから本学習を始める。100Mのcosine終了optimizerへ予算だけを足さず、選択した構成を次のcorpusで新規初期化する。NoNorm変換adapter、Unicode退行、反復・自発停止を引継ぎ事項とする。Muonは安定したAdamW比較で候補を選べたため、この段階では追加しなかった。今回のPhase 5は完了し、Phase 6前で停止する。
