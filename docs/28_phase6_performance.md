# Phase 6③: 高速化と資源活用の実測

更新: 2026-10-03。ユーザーがVRAM等の資源活用、torch.compile等の高速化を確認し、不足を対応するよう指定したため、③を再開する。①②の証拠・snapshotは保持し、今回は③の実装・測定・厳密再開とcommitまで。④生成/変換、⑤長期設定の凍結、500M以上の本学習は開始しない。

## 確認した不足と実装

旧候補はT4K NoNorm / math / batch 8、Phase 5定常約121,139 tokens/s、peak allocated約3.866 GiBで、24 GiB VRAMの最大活用ではない。旧compile/defaultとeager/defaultの再開失敗は[保持済み](../reports/phase5/failed_attempts.json)。新しい測定は採用NoNormと756M拡張train shard、context 1024、FP32 parameters/BF16、AdamW、WSDを使う。品質基準や完全一致の要求を下げない。

固定長block学習専用のcausal attention経路を追加した。CPUでPAD不在・sampler/contextを確認し、cache/paddingを使わない学習では`attn_mask=None, is_causal=True`とする。推論/cacheと文書padding学習は従来経路を保持する。これにより明示maskとGPU値によるPython分岐を学習forwardから除き、compileはfullgraph/static shapeで失敗を可視化する。CPUの参照logits・loss・全gradient・causality検証と不正interface拒否を追加した。全78 tests / skip・failure・error 0、既知の小fixture fork警告2件を保持。

実train CLIに`--training-fast-path`、`--compile-mode`、`--deterministic`を追加し、checkpointのspecへbindする。決定的カーネルの指定時はCUDA workspaceを設定し、backendを固定して実際の完全一致を検証する。source bindingを維持するため、旧checkpointを新sourceで通常resumeしない。①②の旧runtimeは各snapshotに保持し、新sourceは新規準備runで検証する。

## 一次資料の確認（2026-10-03）

固定PyTorch 2.14の[torch.compile API](https://docs.pytorch.org/docs/2.14/generated/torch.compile.html)を確認した。default、reduce-overhead、max-autotune-no-cudagraphs等のmodeがある。reduce-overheadはCUDA GraphsでPython overhead削減を狙うが、workspace cacheでメモリを増やす場合があり、適用や速度向上は保証されない。fullgraphはgraph break時に失敗させ、dynamic=Falseはshapeを固定する。今回はdefaultとreduce-overheadを実機比較し、未測定modeを高速化成功と記載しない。

[SDPA公式仕様](https://docs.pytorch.org/docs/2.14/generated/torch.nn.functional.scaled_dot_product_attention.html)では、backendによって数値が異なる場合があり、mathのBF16中間値はfloatで保持される。causal maskなし経路はsquareの未padding学習に限定し、cacheの非正方形queryへ流用しない。FlashAttentionを明示的に試し、非対応・非決定性は失敗として残す。[再現性の公式説明](https://docs.pytorch.org/docs/2.14/notes/randomness.html)では、決定的処理に速度の代償があり、version/platform間の完全再現は保証しない。本実験は同じWSL/GPU/version/backend内で全state完全一致を要求する。

## 初回測定で判明したcache問題と修正

初回v1のcompiled math/Flashは40更新のloss履歴と全model tensorsが完全一致し、共用Inductor cacheの全45 Python filesにFlash ATen演算がなかった。backend指定だけで実kernelを証明できないため、v1を採用証拠から除外し、snapshot/log/checkpointと検査結果を保持した。既存workerのterminal OOMを確認してsupervisorを終了し、GPU compute processなしを確認した。

上流の[SDPA backendがFX cache keyに含まれないissue](https://github.com/pytorch/pytorch/issues/185449)を確認した。本環境の原因推定と区別し、修正後の実演算で検証する。Trainerはbackend・dtype・deterministic別のInductor cache namespaceへ分離し、構築時にDynamoのin-memory cacheをresetする。cache rootは`JMICRO_COMPILE_CACHE_ROOT`、既存`TORCHINDUCTOR_CACHE_DIR`、既定`artifacts/compile-cache`の順。単一jobで一つのTrainerを使う。通常再開では同じnamespaceを再利用し、cold compileとcacheのある起動を別に記録する。

v2のdefault compiled Flashは実CUDA updateのATen Flash演算を通過し、約433k tokens/s / peak training約1.592 GiBを測った。一方、reduce-overheadのCUDA Graph replayでは内側のCPU ATen hookが省略され、CPU-only検査が誤って失敗した。v2も完了証拠から除外して保持し、実際の演算変更とは区別する。[失敗と根拠](../reports/phase6/performance_failures.json)。

v3は実CUDA updateのCPU ATen traceで、Flashなら`aten::_scaled_dot_product_flash_attention`、mathならFlash不在かつ`aten::bmm`を確認する。CUDA Graph replayで内側のhookが出ない場合は、そのworkerが出力したcompiled codeのbackend固有callとSHA、実際の`CompiledFxGraph`呼び出しを必須とする。検査時に実行したコードを保存し、cache directory内の別graphやkernel名の部分一致で代替しない。profileした更新時間は速度集計から除く。compiled Flash/reduce-overheadを追加し、batch 8の速さだけでFlashの容量・速度を除外せず、最速mathと最速Flash双方を探索する。再開失敗時は同じbackendの次候補を順に検証する。cache分離のtestを含む全79 tests / skip・failure・error 0を確認した。

## 比較・完了条件

凍結した[performance config](../configs/phase6/performance.json)と[schema](../schemas/configs/phase6/performance.schema.json)、実入口[scripts/phase6_performance.py](../scripts/phase6_performance.py)を使う。reference math、causal math、compiled math/default・reduce-overhead、causal flash、compiled flashをbatch 8で比較する。有限値を通過した既存reference・最速math・全体最速に容量探索を絞り、各variant最大16設定、batch上限256で倍増/中間値を測る。範囲内でOOM境界がなければ真の最大と呼ばない。

採用するbatch/backendごとにstable 200 vs 100+100、decay 100 vs 50+50のmodel/optimizer/scheduler/RNG/sampler・消費token/bytes/digest・loss/LR/gradient履歴完全一致、元stable filesの不変性と継続一致を確認する。その後、容量上限と最速batchをそれぞれ3×200完了更新・評価/save込みで確認する。allocated/reserved、driver VRAM・GPU使用率・電力の時系列、cold compile、定常tokens/s、p95更新時間、data wait、save/評価時間を保存する。評価はdev 4文書＋1 prompt/8 new tokensの容量確認で、全文品質評価ではない。

最終設定は完全一致と運用確認を通過したものから速度で選ぶ。最大VRAM使用量と最高速度を別に報告し、評価/saveの余裕を残す。本学習effective batch/LR/WSD数値予算の凍結は⑤として残す。CPU/data waitが制約なら実測に基づく対策を比較し、測定していないMFUや「全GPU能力を使い切った」との保証はしない。

採用候補には、[空のcompiler cacheからの再開検証](../scripts/verify_phase6_cold_resume.py)も追加する。study終了後、その設定のstable 100 checkpointを新runへ通常loadし、空のbackend別cacheで残る100更新を実行する。連続200の全state・後半loss/LR/token履歴完全一致と元run全filesの不変性を確認する。cacheが作成された後、cold trajectoryのcheckpointを保存する前に中断した場合は、warm cacheで代替せず新しい空outputで再検証する。

## v3の短い比較（採用判定前）

[7設定のraw結果への参照と実演算証拠](../reports/phase6/performance_initial_probes.json)。各batch 8/context 1024/40完了更新、同じ入力327,680 tokens、最初の8更新とprofile更新を速度集計から除いた。compile cacheがある起動の値で、fresh cold compileや最大batchの結果ではない。

| 設定 | 定常tokens/s | training peak GiB |
|---|---:|---:|
| reference/math | 120,508 | 3.913 |
| causal/math | 111,869 | 3.913 |
| compile/math/default | 272,222 | 3.217 |
| compile/math/reduce-overhead | 284,281 | 3.154 |
| causal/Flash | 235,705 | 2.137 |
| compile/Flash/default | 473,743 | 1.592 |
| compile/Flash/reduce-overhead | 520,757 | 1.530 |

全7設定で有限値・保存/小sample評価・backend実効を確認した。最大速度比はreference比4.321倍だが、再開・容量・3×200を通過するまでは採用しない。[全79 tests](../reports/phase6/performance_tests.xml)、[文書・履歴保護の監査](../reports/phase6/performance_documentation_audit.json)、[live uv parent実行の確認](../reports/phase6/performance_launch_audit.json)を保存した。GPU使用率やdata waitの判定は最終confirmation時系列から行う。

## 永続実行と再開

WSL checkoutからの実command:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/phase6_performance.py --plan configs/phase6/performance.json --output reports/phase6/performance-20261003-v3
```

studyのterminal completeとprocess/GPUの終了確認後のみ:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/verify_phase6_cold_resume.py --study reports/phase6/performance-20261003-v3 --output reports/phase6/performance-cold-resume-20261003
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/audit_phase6_performance.py --study reports/phase6/performance-20261003-v3 --output reports/phase6/performance_completion_audit.json
```

Windows hidden launcherとLinux supervisorで保持し、`job.json`のPID/boot/start ticks・worker identity・stage/log/heartbeat/restart command、各runのmetrics/atomic checkpoint/SHA、source snapshotを保存する。GPU lockと既存compute processを確認して重複起動しない。同じcommandは完了したstudyを重複実行せず、同一source/configの完了probeを再利用する。中断したworkerは有効checkpointの境界へmetricsを戻して再開する。失敗・source/config変更は別outputへ分け、失敗を削除しない。

現在の実測結果は作業中で、まだ新しい高速化の成功や最大batchを宣言しない。最終reportはrun内の`batch_performance_report.json`、集約証拠と採用理由を完了後に保存する。
