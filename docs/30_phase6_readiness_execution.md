# Phase 6④⑤: 生成・変換と本学習設定の確定

開始: 2026-10-03。ユーザーの「2まで計画を立てて進めてください」は、直前の計画の1.生成・変換確認、2.本学習設定確定を実行する指定。Phase 6④⑤を進め、検証・commit後に停止する。500M以上のBase scaling、Chat学習、学習後の量子化品質・公開は開始しない。

## 固定した比較と完了条件

1. Phase 5採用NoNorm checkpointのSHA、公開T4K Tokenizer、固定Base dev 80 promptとprotocolをbindする。連続forwardと1-token/chunk cache、EOS=3停止を確認。greedy/抑制なし/sampling seeds42/43/44の400生成でEOS・反復・Unicodeの生成IDと原因を残す。必要な修正は最大2案、同じcheckpoint/prompt/seed/長さで対照する。強制停止hookはcontroller検証に限り、品質改善に数えない。
2. NoNormのHF/Llamaとnative float GGUF adapterを実装する。HFはhalf-split RoPE、GGUF LlamaはQ/K rowを公式変換と同じ順序へ変える。固定protocolのFP32 logits許容誤差、短系列/1024・prefill/cache・tied embedding・Tokenizer外部ID・本物の出力からのEOS停止を確認。既存Norm/Qwen3経路とPhase 0〜3 reportは保持する。
3. 新dev89,416文書・164,344,743 body bytesを全文採点し、新corpusのBPB基準と実時間を記録する。batch評価を追加する場合は既存scalarの全本文採点・EOS分離・padding/position契約との一致を検証する。testはモデル選定へ使わない。
4. ③のFlash＋compile reduce-overhead / batch32・context1024・32,768 input tokens/updateを長期候補とする。LRは0.001/0.002/0.003の一要因3候補に限定し、各2,000更新（65,536,000 input tokens）・同じseed/data/sample、warmup200、WSD stableを比較する。dev固定256文書のcommon-byte BPBと有限loss/gradient/optimizer、末尾lossを比較。各100追加decay更新を別runへ分けて評価し、親の不変性を確認。発散・非有限は停止し失敗保持。採用はdecay dev BPBが最良の安定候補、既知の品質未達は維持する。追加sweepは行わない。
5. 変更後sourceでstable400 vs200+200・decay100 vs50+50の全state・履歴完全一致、親不変性・元継続、採用設定のcold-cache再開200→400を新runで確認する。warmup200を越えるstable予算を使う。③の旧sourceチェックを新sourceの再開証拠へ流用しない。
6. 採用LR・batch・model/Tokenizer/data/source hash、warmup・WSD終端/枝予算・seed・保存/評価間隔・保持数・容量上限・起動/再開CLIとGPU排他/PID/boot/start ticks/log/heartbeatを固定する。stableは10Bのglobal更新数で凍結し、500M等の観測点はstop-afterで区切る。純学習・保存/全文評価/生成/decay枝/compileを別計上し、本学習は起動しない。

## 保存する証拠

全文評価の前に固定dev先頭32文書でscalarとbatchのBPB差が0.001以下であることを確認する。この許容値は実測前に固定する。両経路のCEはFP32へ変換してから加算し、過去のBF16加算reportは上書きせず、新しい評価基準として明示する。CPUで本文/EOSの全件採点・padding・状態不変性も検証する。

`reports/phase6/generation_diagnostics.json`、`nonorm_export_parity_report.json`、`readiness_stability_report.json`、`base_launch_plan.json`と`configs/phase6/base_frozen.json`、最終監査・status・採否を保存する。raw logs/checkpoints/export/source snapshotsはLinux `reports/phase6/readiness-20261003/`へ保持。長いGPU処理は永続supervisorとcheckpointで復旧する。各起動前に既存jobと実GPU compute一覧を確認し、重複起動しない。

Python3.12.7の全実行はuv run --frozen。依存変更が必要ならuv add、復元はuv sync --frozen。HF/GGUF変換の一次資料は固定[llama.cpp Llama converter](https://github.com/ggml-org/llama.cpp/blob/46ca246de9bb1c35269722a6240d37d9dfd79cad/conversion/llama.py)とローカル固定Transformersを照合する。③実測の69.5万tokens/sは見積もりの起点で、④⑤の実装・検証時間の保証ではない。

## 2026-10-03の途中結果

以下はCPU精度profile修復前の記録で、起動不可設定は[version1](../configs/phase6/base_frozen_blocked_v1.json)へ保持した。現在の採用と検証は末尾の「最終検証と停止」を参照する。

400生成は360.684秒で完了。greedy抑制あり/なし各80件のEOSは0、反復48、sampling3 seed合計240件の反復6、Unicode破綻0。品質目標は未達のまま。拡張dev89,416文書 / 164,344,743 bytes / 42,003,934 body tokensを336.292秒で全文採点し、BPB1.2441264716を得た。scalar/batchの32文書BPB差は0.0000330177で事前の0.001以内。旧pilotのBPBとは母集団・CEの加算精度が違うため、改善量にしない。

NoNorm HF/Llama・GGUF/Llamaの重み/外部codec/greedy IDs・本物のargmaxからのEOS/EOT停止は成立。全12数値比較を保存したところ、学習済み1024系列ではTorch自身のfull/cache比較も固定FP32許容値を超え、変換だけの問題とは断定できない。標準GGMLのRoPE逐次乗算の位置依存誤差を別runtime `artifacts/runtime-precise`で修正し、1024系列のnative最大差は0.000259から0.0000382へ減ったが、厳密比較は未合格。元runtime・archive・失敗report・probeを保持する。許容値・入力・必要な比較を削って通過扱いにしない。設定値は確定して保存するが、この数値gateをfalseとし、起動CLIが実行を拒否する。④⑤の総合完了とは扱わない。

`scripts/run_base.py`は保存した設定から単一のstable観測点、独立decay、全文dev/400生成の実CLIを準備する。実行時は全gate・GPU排他・PID/boot/start ticks・heartbeat・checkpoint SHA・source・容量を確認し、中断時は同一予算で再開する。prepareが既定で、freezeから学習は起動しない。`base_frozen.json`は`launch_enabled=false`で保存した。500M以上を開始していない。

追加の数値診断はCPUのMKL分岐AUTO/AUTO,STRICT/AVX2,STRICT/COMPATIBLE×threads1/2の**8設定に限定**する。各設定で同じcheckpoint・seed・短/1024入力・元の12比較とEOS/EOT fixturesを検査し、許容誤差・重み・必要な比較を変更しない。全8完了が調査終了条件で、失敗も保存し追加sweepしない。MKLのCNR指定は[Intel公式説明](https://www.intel.com/content/www/us/en/docs/onemkl/developer-guide-windows/2024-1/specifying-code-branches.html)を参照。実環境はi9-14900KSで、実測差を保存して分岐指定だけを成功証拠にしない。

8設定の比較は終了し、全gate成功の設定は0。追加の分岐/threads sweepは行わない。[全失敗と各数値](../reports/phase6/nonorm_cpu_precision_report.json)。次の修復では演算ごとのfull/cache差を追跡し、参照・推論の精度を改善して元の全比較を再検証する。

CPUに限定された差かを切り分けるため、同じ入力と既存native logitsを使うCUDA FP32/math SDPA・TF32 offの参照比較を**1回だけ**行う。短/1024の元の全12比較と同じ許容値を使う。全12の結果保存でこの診断は終了し、CPUの未合格を消さず、CUDA参照の成功だけでCPUも合格としない。

CUDA参照の診断も終了。短系列の6比較は成功し、1024ではHF/full・Torch/cache・HF/cache・native/prefill・native/cacheの5比較が未合格（nativeのcache/prefill間は成功）。したがってCPU専用の問題とは断定できない。[元の全12結果](../reports/phase6/nonorm_cuda_reference_report.json)。次は環境設定の追加探索ではなく、同じ1024入力の演算ごとに差を追跡し、数値精度を修復する。

演算追跡は同じ学習済みartifact・固定1024入力で、CPU FP32のfull1回とcache511+1+512を1回実行し、全Linear/RMSNorm/attention/block/MLP出力の差と最初に相違する演算を保存する。全stage保存がこの診断の終了条件。重み・許容値を変えず、追加の環境sweepは行わない。

## 数値精度の修復条件

RoPE周波数の修復に続く第2案は、実際のCPU推論でFP32の重み・activation・cache・logitsを維持し、Linearとattentionの積和、RMSNormの分散、softmaxの和をFP64で累積する精度profileである。SiLUとdefault RoPEのsin/cosもdoubleで計算しFP32の演算境界へ丸める。Torchと独立したHF/Llamaのforward/cacheに専用の演算を適用し、別native runtime `artifacts/runtime-stable-f32-v2`のCPU F32 kernelsを同じ数学的精度へ修復する。高速なCUDA/BF16学習経路には適用しない。重みやモデル構造を変更せず、未修正のstock FP32での失敗を保持する。

固定checkpoint・元の短/1024入力とcache分割・元の全12比較・atol=1e-5/rtol=1e-4を使う。判定だけにoracleを差し込まず、artifact manifest/GGUF metadataを読んだ実際の推論CLIでも同じprofileを使う。nativeのpatch chain、archive、実binary/shared librariesをhashで照合し、stock runtimeではprofile付きartifactの実行を拒否する。全12比較・disk reload・greedy IDs・本物のEOS/EOT argmax停止・padding/cache/重み不変性の検証が採用条件。追加の環境設定sweepは行わない。

第2案の途中版はTorch/HF/full/cacheが完全一致し、native1024の4要素が未合格だった。位置0〜1023×32周波数のsin/cosを調べるとfloat libmとdouble結果のFP32丸めに474/329箇所の1 ULP差があり、double libmとTorch doubleをFP32へ丸めた値は全箇所一致した。default RoPEのtrigも修復した試作では同じ全12比較が合格。正式な成果物/CLI・全テストを検証してから設定を再凍結する。途中失敗・原runtime・既存GPU測定を保持する。

LR0.001/0.002/0.003は各2,000 stable＋独立100 decayを完了、固定256文書BPBは1.18776153/1.18404703/1.18739314で0.002を採用。新sourceのstable400 vs200+200、decay100 vs50+50、cold200→400は全state/履歴完全一致。[結果](../reports/phase6/readiness_stability_report.json)、[独立106 checks](../reports/phase6/readiness_gpu_audit.json)。unique raw metricsは7,500 completed updates / 245,760,000 input tokensで、複数の準備runの合計、本学習系列ではない。

[本設定](../configs/phase6/base_frozen.json)はbatch32・accum1・context1024・32,768 input tokens/update、LR0.002、warmup200、seed42、Flash/compile reduce-overhead/fullgraph/static/deterministic、WSD stable総305,176更新（10,000,007,168 input tokens）。各観測点に5%の独立decay枝、最低LR比0.1、1,000更新ごとにsave・全checkpointを保持する。容量はcheckpoint推定347件 / 41,702,694,225 bytes、run上限100 GiB・最低空き200 GiB。実CLIと復旧は[起動計画](../reports/phase6/base_launch_plan.json)。変換gate falseのため起動不可。

実測693,666 tokens/sからstable10B約4.00時間、5段階decay合計約22.2分、全文dev/400生成を5回で約58.1分。保存・compile・filesystemの変動は別計上で、完成時刻を保証しない。保存は最終1件0.435秒、compile込み初回更新1.987秒の観測値で、cold compileの上限ではない。テストは[全86件 / skip・failure・error 0](../reports/phase6/readiness_tests.xml)。

## 最終検証と停止

[正式な学習済み変換検証](../reports/phase6/nonorm_export_parity_report.json)は元の全12数値比較と13契約checksが成功。Torch/HFのfull/cacheは完全一致、nativeのfull/cacheも完全一致、1024のnative対Torch最大差0.0000124574は固定の要素別許容誤差内。FP32パラメータとTokenizer ID、元の入力・cache分割を保持した。

[独立監査](../reports/phase6/readiness_export_audit.json)は149 checks成功。実119 GGUF tensorsの全要素と元の学習済み重みの対応を確認し、9回の実CLI（学習済みgreedy・EOS/EOT fixture×3 backend）でID一致と停止を確認。profile metadataから実CLIが同じCPU演算を使い、stock native runtimeを指定すると実行前に拒否する。base品質のEOS成功ではなくcontrollerの合成fixture証拠である。

[全90 tests](../reports/phase6/readiness_precision_tests.xml)はskip・error・failure 0。既存Norm経路を維持し、NoNorm CPU精度profileの1024/full/cache/HF disk reload、ragged padding、future mask、重み/tie不変性、training/autocast拒否、native実library hashの変更拒否も確認した。GPU学習core・readiness worker/evaluator・uv.lockは未変更で、既存の実CUDA比較・厳密/cold再開証拠を維持する。

[設定version2](../configs/phase6/base_frozen.json)は元のbatch32/LR0.002/WSD予算・容量に加え、採用した推論profile・native receipt・学習済み検証artifactをbindした。技術gateはすべてtrue。旧[起動不可version1](../configs/phase6/base_frozen_blocked_v1.json)とその実拒否証拠を保持する。prepare/復旧commandの検証までを終えて93c7d1dへcommit済み。500M以上の本学習は開始せず停止している。

GPU学習はWSL/RTX4090の高速BF16経路を維持する。CPU精度profileは重み/activation/cache/logitsのFP32境界とFP64累積を使うため、stock CPU kernelと速度が異なる。未修正stock HF/GGUFやCUDA FP32の厳密parity達成とは扱わない。生成品質・文法・EOS到達の未達は維持し、次回の新規Base学習で同じdev suiteを測る。

[総合監査](../reports/phase6/readiness_gate_audit.json)は6つの要求と停止条件を37 checksで照合し、[文書・成果物・履歴監査](../reports/phase6/readiness_package_audit.json)も成功。旧73 reportsとuv.lockのbyte保持、現在source/config/正式artifactのhash、実prepare（global305,176更新・stop15,259）、GPU process/終了job identity、本学習directory未作成を確認した。検証済み結果は93c7d1dへcommit済みで、本学習前で停止している。

WSL project rootでの読み取り監査とprepare（どちらもGPU本学習を起動しない）:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/audit_phase6_completion.py
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_base.py --config configs/phase6/base_frozen.json --target 500M --output reports/phase6/base-20261003
```
