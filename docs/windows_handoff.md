# 別PCで続きを進める: Windows / WSL / RTX 4090

次回は[学習済み10Mモデルの生成方法の比較](27_phase6_remaining_plan.md#次回の一区切り-学習済み10mモデルの生成方法を比較する)。[比較条件](../reports/phase6/repetition_decoder_plan.json)は計画のみで、専用比較CLIは未実装。ユーザーが実行を再開した後に別CLIの実装/元decoder再現を検証し、同じ重みで計640outputsを測りreport/commitで停止する。約500Mは学習tokensのmilestoneで、モデルサイズは約10Mパラメータ。今回GPU jobや学習を開始していない。

500M後の[反復/EOS/data調査](../reports/phase6/repetition_diagnosis_review.md)も完了し停止。追加学習/1Bは未開始。Linux `reports/phase6/repetition-diagnosis-20261003/`のsample・trace・log・job identity・testsを既存runとともに引き継ぐ。次回案のdecoder/mixture比較は未起動で、完了した500Mや診断jobを再実行しない。[最新状態](autonomous_status.md)。

2026-10-03: 拡張trainの500M stable＋独立763更新decayと全文dev/400生成評価を完了。同一dev BPB 1.244126→1.022491、抑制greedy EOS 0/80→0/80、反復48/80→66/80。全99 tests成功。人手blind採点・test・Chat・新重みの量子化は未実施。1B前で停止。 [最新状態](autonomous_status.md)。以下の初回復元・準備完了記録は履歴として保持する。

Phase 6①②③完了（2026-10-03）。④生成/変換と⑤本学習設定の確定もユーザー指定の範囲で検証済み。[今回の固定計画](30_phase6_readiness_execution.md)と[実状態](autonomous_status.md)を参照する。④⑤は`93c7d1d`へcommitして停止済みで、500M以上の本学習は開始しない。

最終更新: 2026-10-03。[Phase 4](21_phase4_completion.md)、[Phase 5](23_phase5_completion.md)、Phase 6①〜⑤の準備は完了。復元済みPCでは環境整備・Tokenizer学習・完了済み測定を繰り返さず、[現在の状態](autonomous_status.md)と既存job/checkpointを確認する。④⑤の限定比較と起動設定凍結も93c7d1dへcommitして終了した。Base/Chat本学習は未開始で、文書更新を学習再開の指定として扱わない。

## 引継ぎ先と現在地

| 項目 | 内容 |
|---|---|
| コード・docs・lockの正本 | Windows `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m` |
| Linux実行コピー | `/home/aihub_ubuntu/src/japanese-tiny-llm-10m` |
| GitHub | [private repository](https://github.com/ayutaz/japanese-tiny-llm-10m)。Phase 5・Phase 6①〜⑤と文書更新のコミットは未push |
| 公開pilot / Tokenizer | [固定Hub repository](https://huggingface.co/datasets/japanese-data-analyze/japanese-tiny-llm-10m-artifacts)、約107MB |
| Hub commit | `0b1042979bf32899e24da30790e3ae6b239013c3` |
| manifest SHA-256 | `8072bd218be26637a51c7c11540f1c8c636392c3b1a91f805a5e317e6ca55a09` |
| 実機環境 | WSL package 3.0.1.0 / Ubuntu WSL 2、RTX 4090、Windows driver 616.92 |
| Python / PyTorch | uv管理の3.12.7 / 2.14.1、CUDA 13.0 |
| 完了済み | Phase 0〜5とPhase 6①〜⑤の準備。pilot/Tokenizer、モデル/export、GPU学習器、100M候補選定、756M拡張corpus、WSD全state再開/分岐完全一致 |
| 現在の境界 | ③の証拠はa7d26e1へcommit済み。④⑤も93c7d1dで完了し、400生成/dev全文・NoNorm CPU変換精度、LR3候補・新source再開を検証済み。長期LR0.002と予算はversion2へ凍結済み、全12変換比較・実CLI149 checks・90 tests成功。本学習は開始しない。 |
| 未実施 | 長期Base本学習、Chat trainer、学習後の量子化品質 |

HubにはpilotとTokenizerがあり、モデル重み・shard・checkpointは含まない。Phase 4の検証checkpointはLinuxの`reports/phase4/gates-20261003/`、Phase 5は`reports/phase5/run-20261003-docoverfit/`、Phase 6準備の12 checkpointsは`reports/phase6/preparation-20261003/cuda/`へ保存してある。拡張raw/corpus/shardsは`~/jmicro-data/phase6/{raw,expanded-v2}/`で、Hub bundleには含まれない。新規PCへは必要なcheckpoint/logも別途引き継ぐ。旧driver/アクセス拒否の履歴は[復旧履歴](autonomous_history_20261003.md)へ分離した。

## 1. Windows側でWSLとGPUを確認

PowerShellの読み取り確認:

```powershell
wsl --version
wsl -l -v
nvidia-smi
```

WSL packageの3.xとdistributionの実行方式WSL 2は別に記録する。[MicrosoftのWSL手順](https://learn.microsoft.com/en-us/windows/wsl/install)。NVIDIA driverはWindows側へ導入し、WSLへLinux display driverを追加しない。[NVIDIAのWSL手順](https://docs.nvidia.com/cuda/wsl-user-guide/index.html)

現在の616.92で固定CUDA 13の動作を実測済み。以前の552.12は解消したblockerで、現PCに更新操作は不要。新規PCでdriver条件を満たさない場合は[公式配布先](https://www.nvidia.com/Download/index.aspx)から更新し、driver表示だけでなくCUDA/BF16も確認する。[CUDAの互換条件](https://docs.nvidia.com/deploy/cuda-compatibility/minor-version-compatibility.html)

新規PCの環境準備が必要な場合のみ、Windows project rootから実行:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\setup_windows_wsl.ps1
```

既存distributionを使い、ゼロの場合は導入・初回Linuxユーザー作成が必要。OS昇格/再起動を要求されたらその外部操作で停止する。既存のLinuxコピーはsetupで上書きしない。復元済みの現在のPCではsetupを再実行する必要はない。Linux内からのsetup再実行は以下（WSL Linux shell）:

```sh
cd ~/src/japanese-tiny-llm-10m
JMICRO_PROJECT_ROOT="$PWD" bash scripts/setup_wsl_environment.sh
```

Linuxのsetup.log/environment、Windowsのwsl_setup reportに結果を保存する。既存環境は構築済みで、CUDA/BF16、入力付きprepare/verify、Phase 4の全64 tests / skip 0を確認した。Phase 6①②は74 tests・73 GPU checks、最新③は79 tests・独立1286 checks・cold再開26 checks成功（全skip 0）。

## 2. Linux側でコードとuvを準備

新規PCでコードがない場合のみprivate repositoryを取得する。GitHub認証はLinux側でも確認する。clone先へWindowsの最新コミットを引き継ぐまで、GitHub mainだけを最新と仮定しない。既存treeの変更は保存し、resetや強制上書きをしない。

```sh
gh auth login --hostname github.com --git-protocol https --web
gh auth setup-git
mkdir -p ~/src
git clone https://github.com/ayutaz/japanese-tiny-llm-10m.git ~/src/japanese-tiny-llm-10m
cd ~/src/japanese-tiny-llm-10m
git status -sb
git rev-parse HEAD
```

uv未導入なら[公式導入手順](https://docs.astral.sh/uv/getting-started/installation/)を使い、案内されたPATHを有効にする。project rootで:

```sh
uv python install 3.12.7
uv sync --frozen --python 3.12.7 --extra hub --extra data --extra ml --extra export
git config --local user.name yousan
git config --local user.email ka1357amnbpdr@gmail.com
```

Macのvenv/native binaryは移さない。すべてのPython実行は必要なextra付き`uv run --frozen`、依存変更は`uv add`。system Pythonやpipへ切り替えない。固定Python/依存が取得できなければ正確なblockerを記録する。

## 3. Hugging FaceからTokenizerとデータを復元

新規PCで不足する場合のみ、project rootで:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/download_hub_artifacts.py
```

匿名で全25 payloadとmanifestを検証してから16 filesを配置する。配置済みならrestored_filesは0。内容が違う既存fileは上書きせず停止する。取得cacheは`artifacts/hub-downloads/<commit>/`。

| 復元先 | 内容 |
|---|---|
| `artifacts/phase2/4096/`、`8192/` | model/vocab、special IDs、wrapper、metadata、各5 files |
| `data/phase1/processed/` | corpus、Parquet manifest、split、sample、二つのreport、計6 files |

採用corpusは22,998件、全source合計splitはtrain 20,710 / dev 1,074 / test 1,214。Phase 4 BaseではWebのみを選び、train 18,022 / dev 924 / test 1,052に分離。会話/sharealikeと固定evalはBaseへ混ぜない。SFTはAssistant本文＋EOTを教師対象にするが、Chat trainerは未実装。

公開Tokenizerは旧Mac版の保存先metadataだけを除去したためbyte hashが異なる。公開manifestのhashを使い、checkpoint/shardへbindする。旧ランダム重みexportを公開版と再比較する場合のみexportを作り直す。初回CUDA確認のためにTokenizer再学習・原データ再取得・Phase 3全作業を繰り返さない。[hashと取得の詳細](huggingface_handoff.md)

## 4. 契約とCUDA環境を確認

新規環境での検証は既存reportを上書きせず別directoryへ保存する:

```sh
mkdir -p reports/local/handoff
uv run --frozen --extra hub --extra data --extra ml --extra export pytest -q -ra
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/experiment.py capture-environment --probe-torch --output reports/local/handoff/environment.json
```

Phase 4のsuiteは64 tests / skip 0、Phase 5は68、Phase 6①②完了時は74 tests / skip 0。[保存した結果](../reports/phase6/tests.xml)。artifact欠落によるskipを完了証拠にしない。CPU成功はCUDA学習・再開一致の代わりにならない。Linux/WSL、GPU/driver、cuda_available、BF16、Python/uv/lock/sourceをreportから確認する。`nvidia-smi`がPATHにない場合は`/usr/lib/wsl/lib/nvidia-smi`を確認する。

環境captureの`training_target.verified=false`は準備用ラベル。最終判定は[handoff report](../reports/phase4/handoff_report.json)と実GPU結果を使う。wheel変更が必要な新規環境ではuvでlockを更新し、新しい条件で検証する。現在の固定構成は動作済み。

## 5. 入力・run・checkpointを引き継ぐ

準備snapshotは`experiment.py prepare-run` / `verify-run`で記録できる。これはphase 0/kind preparationの記録で学習開始を意味しない。実学習は別の[training run schema](../schemas/training_run.schema.json)を使い、CLI引数・環境・PID・Git dirty・source snapshot・入力hash・statusをrun.jsonへ保存する。

checkpoint version 2は完了updateでmodel/optimizer/scheduler/Python・NumPy・torch・CUDA RNG/sampler positionとRNG/consumed tokens・教師tokens・body bytes/digest/config/data/source hashをatomic保存する。latest.jsonのSHAを確認し、partial metricsはcheckpoint境界へ戻して再開する。resumeはschedule/config/source/shardの変更を拒否する。LinuxコピーのGit HEADだけで実行コードを判断せず、snapshotとimplementation hashを照合する。

長時間GPU jobはhidden Windows wsl.exe supervisor、Linux job.jsonのPID/boot ID/start ticks/stage/logで保持した。GPUは`~/jmicro-data/gpu.lock`で排他。再開前にWindows/Linuxプロセス、GPU compute一覧、既存runを確認し、二重jobを起動しない。スリープ/再起動後は有効なcheckpointから再開し、会話終了だけで保存先を失わない。

## 6. 実装済みCLIと次回の再開

今回の①②は[準備完了記録](26_phase6_preparation_completion.md)と[独立監査](../reports/phase6/completion_audit.json)を正とする。WSL data rootの拡張corpusは756M unique train stream tokens、WSD stable/decayの実CUDA再開一致は成功済み。準備の中断復旧/読み取り再監査の実commandは完了記録に保存した。①②のjobは終了済み。③の別studyとcold再開も終了済み。[完了記録](29_phase6_performance_completion.md)に採用設定・監査・job identityを保存した。

開始条件は[Phase 6 gate](24_phase6_plan.md)と[今回の固定比較](30_phase6_readiness_execution.md)を参照する。④⑤の400生成/全文dev・3 LR比較・厳密/cold再開は終了し、[本設定](../configs/phase6/base_frozen.json)と[起動/復旧CLI](../reports/phase6/base_launch_plan.json)を保存した。長系列の固定数値gateはCPU精度profileで元の全12比較が成功し、実CLI監査149 checks・全90 testsが成功。version2は`launch_enabled=true`だが今回は本学習前で停止する。旧false設定と実起動拒否証拠は保持。完了した準備jobを再起動しない。Phase 4のNorm/pilot/cosine benchmarkをNoNorm/拡張shard/WSDの証拠へ流用しない。

`scripts/train.py`にbuild-shards/train/evaluateを実装済み。trainはCLI引数を使用し、baseline JSONを自動読込しない。AdamW＋warmup/cosine・WSD stable/decayは実装済み、Muon・Chat trainer・複数source mixtureは未実装。

以下のhelpは学習を起動せず確認できる:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py train --help
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py evaluate --help
```

下記200更新はCLI利用例で、overfit合格の証拠や本学習設定ではない。Phase 5の正式な予算・合格条件は[詳細計画](22_phase5_plan.md)へ固定済み。Phase 5 supervisorは終了済み。完了したPhase 5比較と③のstudyを重複起動しない。本学習は再開指定を待つ。文書単独の暗記検証には`--sampler document`を使用し、通常のsmoke/100Mはdefaultのblock samplerを使う。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py build-shards --tokenizer artifacts/phase2/8192/tokenizer.model --limit 100 --output "$HOME/jmicro-data/shards/t8k-overfit100"
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py train --model configs/models/t8k.json --shards "$HOME/jmicro-data/shards/t8k-overfit100" --output reports/phase5/overfit-example --phase 5 --device cuda --dtype bf16 --context 1024 --batch 2 --schedule-updates 200 --stop-after 100 --save-every 100
```

`--limit 100`は各splitの上限。dev/testをoverfit学習へ使わない。保存済みrunを再開する際は元の全引数・出力先を維持し、同じcommandへ`--resume /absolute/path/to/checkpoint.pt`と必要な`--stop-after`を追加する。`--schedule-updates`を途中で変えて予算を延長しない。

評価の形式（同じ入力にbindされた実在checkpointを指定）:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py evaluate --checkpoint /absolute/path/to/checkpoint.pt --shards "$HOME/jmicro-data/shards/t8k-overfit100" --tokenizer artifacts/phase2/8192/tokenizer.model --split dev --output reports/local/overfit-evaluation.json
```

Phase 4 Norm/defaultのeager最大安定batchはT8K 57 / T4K 64、測定点の最高速度はcompile/default batch 8。Phase 5でdefault/compile-defaultは厳密resumeに失敗し、現候補はeager/math batch 8を採用した。③では学習専用causal経路・cache分離を修正し、NoNorm/math最大45、compiled/math最大53、compiled Flash最大111を実測・厳密再開検証した。最速はFlash/compile reduce-overhead batch 32=694,521 tokens/s。最大容量と最高速度を区別する。[③の完了](29_phase6_performance_completion.md)。Phase 4測定をそのまま有用なモデル品質として扱わない。[予算と制約](../reports/phase4/resource_budget.md)

## 次の担当へ渡す文面

```text
AGENTS.md、docs/autonomous_status.md、docs/15_project_roadmap.md、docs/windows_handoff.md、docs/24_phase6_plan.mdを読んでください。
Phase 0〜5とPhase 6①〜⑤の準備は完了しています。③の証拠はa7d26e1へcommit済みです。④⑤のCPU精度profile・実CLI・長期設定も93c7d1dでcommit済みです。本学習の再開指定まで停止し、完了したGPU studyを再実行しないでください。残る作業はdocs/27_phase6_remaining_plan.mdを参照してください。ユーザーの再開指定があるまで本学習を起動しないでください。
最新コードの正本はWindows workspaceで、最近のコミットは未pushです。Linux実行sourceはsnapshot/hashで確認してください。
固定公開Tokenizer/pilotは復元済み。Pythonは必ずuv run --frozen、依存変更はuv addを使ってください。
既存process/checkpointを確認し、docs/24_phase6_plan.mdとdocs/26_phase6_preparation_completion.mdに従って進め、同じjobを二重起動しないでください。
未達の品質目標を維持し、原データ再取得・Tokenizer再学習・Phase 3全作業・完了済みPhase 4測定を繰り返さないでください。
実測結果、失敗、次の作業をreport/statusへ保存し、指定Git名義で適度にコミットしてください。
```

## この手順の検証範囲

固定公開25 payload、Python/uv/WSL/GPU、CUDA/BF16、Phase 4の全64 testsと両モデルの再開/容量/速度、Phase 5の100M候補選定、Phase 6①②の全74 tests・73 GPU checksと拡張corpus全監査を現在のPCで確認済み。③の採用NoNormの容量・compiled/math/Flash速度・厳密/cold再開は検証済み（独立1286 checks、cold26 checks、79 tests）。長期予算はversion2へ凍結済み、CPU精度profileの全12比較・実CLI149 checks・全90 tests成功。新規PCや変更したruntimeでは必要な環境gateを改めて確認する。学習後のBase/Chat品質・quantizationは未検証。
