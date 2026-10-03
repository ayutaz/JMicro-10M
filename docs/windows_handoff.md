# 別PCで続きを進める: Windows / WSL / RTX 4090

Phase 6①②完了（2026-10-03）: train 756,087,912 unique stream tokensの拡張shardとWSD stable/decay CLI・CUDA全state再開一致を検証。全corpus・shardの独立監査も完了。③以降の速度/batch探索・本学習は未開始。

最終更新: 2026-10-03。現在のPCは[Phase 4の実機検証](21_phase4_completion.md)と[Phase 5](23_phase5_completion.md)が完了し、Phase 6①②完了で停止中（③以降未開始）。復元済みPCでは環境整備・Tokenizer学習・完了済み測定を繰り返さず、[現在の状態](autonomous_status.md)と既存job/checkpointを確認する。今回の作業範囲は①②まで。③以降を開始しない。Base/Chat本学習は未開始。

## 引継ぎ先と現在地

| 項目 | 内容 |
|---|---|
| コード・docs・lockの正本 | Windows `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m` |
| Linux実行コピー | `/home/aihub_ubuntu/src/japanese-tiny-llm-10m` |
| GitHub | [private repository](https://github.com/ayutaz/japanese-tiny-llm-10m)。最近のPhase 5コミットと文書更新は未push |
| 公開pilot / Tokenizer | [固定Hub repository](https://huggingface.co/datasets/japanese-data-analyze/japanese-tiny-llm-10m-artifacts)、約107MB |
| Hub commit | `0b1042979bf32899e24da30790e3ae6b239013c3` |
| manifest SHA-256 | `8072bd218be26637a51c7c11540f1c8c636392c3b1a91f805a5e317e6ca55a09` |
| 実機環境 | WSL package 3.0.1.0 / Ubuntu WSL 2、RTX 4090、Windows driver 616.92 |
| Python / PyTorch | uv管理の3.12.7 / 2.14.1、CUDA 13.0 |
| 完了済み | Phase 0〜5。pilot/Tokenizer、モデル/export、GPU学習器、overfit/smoke、100M比較・候補選定 |
| 現在の境界 | ①②は全監査を完了し停止。実行中jobなし。候補T4K / NoQK-Norm / LR 0.002 |
| 未実施 | 長期Base本学習、Chat trainer、学習後の量子化品質 |

HubにはpilotとTokenizerがあり、モデル重み・shard・checkpointは含まない。Phase 4の小さい学習済み検証checkpointはLinuxの`reports/phase4/gates-20261003/`へ保存してある。新規PCへは必要なcheckpoint/logも別途引き継ぐ。旧driver/アクセス拒否の履歴は[復旧履歴](autonomous_history_20261003.md)へ分離した。

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

Linuxのsetup.log/environment、Windowsのwsl_setup reportに結果を保存する。既存環境は構築済みで、CUDA/BF16、入力付きprepare/verify、全64 tests / skip 0を確認した。

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

Phase 4のsuiteは64 tests / skip 0。artifact欠落によるskipを完了証拠にしない。CPU成功はCUDA学習・再開一致の代わりにならない。Linux/WSL、GPU/driver、cuda_available、BF16、Python/uv/lock/sourceをreportから確認する。`nvidia-smi`がPATHにない場合は`/usr/lib/wsl/lib/nvidia-smi`を確認する。

環境captureの`training_target.verified=false`は準備用ラベル。最終判定は[handoff report](../reports/phase4/handoff_report.json)と実GPU結果を使う。wheel変更が必要な新規環境ではuvでlockを更新し、新しい条件で検証する。現在の固定構成は動作済み。

## 5. 入力・run・checkpointを引き継ぐ

準備snapshotは`experiment.py prepare-run` / `verify-run`で記録できる。これはphase 0/kind preparationの記録で学習開始を意味しない。実学習は別の[training run schema](../schemas/training_run.schema.json)を使い、CLI引数・環境・PID・Git dirty・source snapshot・入力hash・statusをrun.jsonへ保存する。

checkpoint version 2は完了updateでmodel/optimizer/scheduler/Python・NumPy・torch・CUDA RNG/sampler positionとRNG/consumed tokens・教師tokens・body bytes/digest/config/data/source hashをatomic保存する。latest.jsonのSHAを確認し、partial metricsはcheckpoint境界へ戻して再開する。resumeはschedule/config/source/shardの変更を拒否する。LinuxコピーのGit HEADだけで実行コードを判断せず、snapshotとimplementation hashを照合する。

長時間GPU jobはhidden Windows wsl.exe supervisor、Linux job.jsonのPID/boot ID/start ticks/stage/logで保持した。GPUは`~/jmicro-data/gpu.lock`で排他。再開前にWindows/Linuxプロセス、GPU compute一覧、既存runを確認し、二重jobを起動しない。スリープ/再起動後は有効なcheckpointから再開し、会話終了だけで保存先を失わない。

## 6. 実装済みCLIと次回の再開

今回の①②は[準備完了記録](26_phase6_preparation_completion.md)と[独立監査](../reports/phase6/completion_audit.json)を正とする。WSL data rootの拡張corpusは756M unique train stream tokens、WSD stable/decayの実CUDA再開一致は成功済み。準備の中断復旧/読み取り再監査の実commandは完了記録に保存した。現在のjobは全終了しており、通常の次回作業は③の別測定からになる。

次回のPhase 6準備順・開始条件・未凍結項目は[詳細計画](24_phase6_plan.md)を参照する。現在はPhase 6①②完了で停止中（③以降未開始）。WSDの実CLIと凍結run configはまだ存在しないため、③の測定後に本学習の起動・再開commandを追加する。

`scripts/train.py`にbuild-shards/train/evaluateを実装済み。trainはCLI引数を使用し、baseline JSONを自動読込しない。AdamW＋warmup/cosine・WSD stable/decayは実装済み、Muon・Chat trainer・複数source mixtureは未実装。

以下のhelpは学習を起動せず確認できる:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py train --help
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py evaluate --help
```

下記200更新はCLI利用例で、overfit合格の証拠や本学習設定ではない。Phase 5の正式な予算・合格条件は[詳細計画](22_phase5_plan.md)へ固定済み。Phase 5 supervisorは終了済み。完了した比較を重複起動せず、Phase 6③以降の再開指定を待つ。文書単独の暗記検証には`--sampler document`を使用し、通常のsmoke/100Mはdefaultのblock samplerを使う。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py build-shards --tokenizer artifacts/phase2/8192/tokenizer.model --limit 100 --output "$HOME/jmicro-data/shards/t8k-overfit100"
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py train --model configs/models/t8k.json --shards "$HOME/jmicro-data/shards/t8k-overfit100" --output reports/phase5/overfit-example --phase 5 --device cuda --dtype bf16 --context 1024 --batch 2 --schedule-updates 200 --stop-after 100 --save-every 100
```

`--limit 100`は各splitの上限。dev/testをoverfit学習へ使わない。保存済みrunを再開する際は元の全引数・出力先を維持し、同じcommandへ`--resume /absolute/path/to/checkpoint.pt`と必要な`--stop-after`を追加する。`--schedule-updates`を途中で変えて予算を延長しない。

評価の形式（同じ入力にbindされた実在checkpointを指定）:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py evaluate --checkpoint /absolute/path/to/checkpoint.pt --shards "$HOME/jmicro-data/shards/t8k-overfit100" --tokenizer artifacts/phase2/8192/tokenizer.model --split dev --output reports/local/overfit-evaluation.json
```

eager最大安定batchはT8K 57 / T4K 64、測定点の最高速度はcompile batch 8。Flash-onlyはmask非対応で失敗、compiled最大容量は未探索。次回の比較ではcontext/backend/precision/batch/更新数を固定し、最大容量と最高速度を区別する。Phase 4測定をそのまま有用なモデル品質として扱わない。[予算と制約](../reports/phase4/resource_budget.md)

## 次の担当へ渡す文面

```text
AGENTS.md、docs/autonomous_status.md、docs/15_project_roadmap.md、docs/windows_handoff.md、docs/24_phase6_plan.mdを読んでください。
Phase 0〜5は完了。今回のPhase 5は完了し、Phase 6①②完了で停止中（③以降未開始）です。ユーザーの再開指定があるまで本学習を起動しないでください。
最新コードの正本はWindows workspaceで、最近のコミットは未pushです。Linux実行sourceはsnapshot/hashで確認してください。
固定公開Tokenizer/pilotは復元済み。Pythonは必ずuv run --frozen、依存変更はuv addを使ってください。
既存process/checkpointを確認し、docs/24_phase6_plan.mdとdocs/26_phase6_preparation_completion.mdに従って進め、同じjobを二重起動しないでください。
未達の品質目標を維持し、原データ再取得・Tokenizer再学習・Phase 3全作業・完了済みPhase 4測定を繰り返さないでください。
実測結果、失敗、次の作業をreport/statusへ保存し、指定Git名義で適度にコミットしてください。
```

## この手順の検証範囲

固定公開25 payload、Python/uv/WSL/GPU、CUDA/BF16、全64 tests、入力付きprepare/verify、両モデルの全state resume一致、BPB/dev生成、容量・速度・予算まで現在のPCで検証済み。新規PCや変更したruntimeでは必要な環境gateを改めて確認する。学習後のBase/Chat品質・quantizationは未検証。
