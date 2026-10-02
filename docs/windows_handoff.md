# 別PCで続きを進める: Windows / WSL / RTX 4090

2026-10-02時点の再開手順。別PCでこの文書を最初に読み、上から順に環境と成果物を復元してPhase 4を進める。**Phase 0〜3は完了、本学習は未実施。次はRTX 4090で学習器・保存再開・最大安定バッチを検証する。** Windows実機のCUDA動作・速度はまだ測っていない。

## 引継ぎ先と現在地

| 項目 | 内容 |
|---|---|
| コード・docs・config・依存lock | [ayutaz/japanese-tiny-llm-10m](https://github.com/ayutaz/japanese-tiny-llm-10m)、private、`main` |
| Tokenizer・前処理済みpilot | [japanese-data-analyze/japanese-tiny-llm-10m-artifacts](https://huggingface.co/datasets/japanese-data-analyze/japanese-tiny-llm-10m-artifacts)、public、約107MB |
| Hub固定commit | `0b1042979bf32899e24da30790e3ae6b239013c3` |
| Hub manifest SHA-256 | `8072bd218be26637a51c7c11540f1c8c636392c3b1a91f805a5e317e6ca55a09` |
| Python・依存管理 | Python 3.12.7、`uv sync` / `uv run`、依存変更は`uv add` |
| 学習先 | Windows PC、RTX 4090 24GB、WSL上のLinux |
| 完了済み | データpilot、4k/8k Tokenizer、T4K/T8Kモデル、cache、CPU/HF/GGUF/量子化のランダム重み検証 |
| これから実装 | 学習器、uint16 shards・loader、checkpoint再開、BPB/生成評価runner、GPU速度測定 |

公開状態とfile一覧は[Hugging Face共有手順](huggingface_handoff.md)、詳細な順序と完了条件は[計画](15_project_roadmap.md#高速に完成させる進め方)を参照する。Hubから取得できるのはpilotとTokenizerであり、学習済みLLM・学習checkpoint・大規模shardsはまだ存在しない。

## 1. Windows側でWSLとGPUを確認

2026-10-02のユーザー指定により、WSLパッケージは**3.x**を採用する。公式latestを直接確認した時点の安定版は[3.0.1（2026-09-29公開）](https://github.com/microsoft/WSL/releases/tag/3.0.1)。従来の3.1指定を3.xへ更新し、実際に導入したversionを記録する。

このPCではWSL 2.6.1.0、RTX 4090 24,564 MiB、Windows NVIDIA driver 552.12を確認した。ただし、制限された実行環境ではdistribution一覧・状態が`E_ACCESSDENIED`、WSL更新が`WININET_E_CANNOT_CONNECT`、Hub/Python取得がsocketアクセス拒否となった。**更新・Linux起動・成果物復元は未完了**。実測は`reports/phase4/windows_preflight.json`を参照する。アクセス拒否をdistribution未導入と解釈しない。

通常のWindows PowerShellで、プロジェクトのrootから再開する:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\setup_windows_wsl.ps1
```

WSLを公式安定版へ更新して3.xを確認し、既存distributionを利用する。複数ある場合は`-Distribution Ubuntu-24.04`等で明示する。distributionがゼロの場合はUbuntu-24.04を導入し、Linuxユーザーの初回作成で停止する。作成後に同じcommandを再実行する。更新に管理者権限が必要と表示された場合は管理者PowerShellで更新する。更新チャネルが3.xをまだ配布しない場合は、[公式releaseのx64 MSI](https://github.com/microsoft/WSL/releases/tag/3.0.1)で更新してから再実行する。

Linux側では`setup_wsl_environment.sh`がWindowsの作業treeを`~/src/japanese-tiny-llm-10m`へコピーし、Python 3.12.7/uv、Hub成果物復元、依存、CUDA/BF16、skipなしテスト、入力付き準備runの順に進める。既存のLinuxコピーは上書きしない。Linuxコピーで再実行する場合:

```sh
cd ~/src/japanese-tiny-llm-10m
JMICRO_PROJECT_ROOT="$PWD" bash scripts/setup_wsl_environment.sh
```

`JMICRO_PROJECT_ROOT`で新しいLinux保存先も指定できる。Linuxの`reports/phase4/setup.log`と各report、Windowsの`reports/phase4/wsl_setup.json`に結果を残す。これらのスクリプトの構文とWindows確認モードを検証したが、Linux構築・GPU動作はまだ実機検証できていない。

固定`uv.lock`のLinux依存にはCUDA runtime 13.0.96、cuDNN-cu13が含まれる。[CUDA 13.xの最低driver条件は580以上](https://docs.nvidia.com/deploy/cuda-compatibility/minor-version-compatibility.html)で、観測した552.12は満たさない。Windows側でRTX 4090用の現行対応driverを[公式NVIDIA配布先](https://www.nvidia.com/Download/index.aspx)から更新する。スクリプトは成果物を先に復元し、driver条件未達ならGPU依存導入前に停止する。driver条件を満たすことと、実CUDA/BF16動作確認は別に記録する。

PowerShellで実行:

```powershell
wsl --version
wsl -l -v
nvidia-smi
```

「WSL 3.x」はWSLパッケージversionとして記録する。`wsl -l -v`のdistribution実行方式はWSL 2で確認する。この二つのversion表示を混同せず、実際の表示を記録する。[MicrosoftのWSL手順](https://learn.microsoft.com/en-us/windows/wsl/install)

WSL/Ubuntuが未導入の場合のみ、管理者PowerShellで以下を実行し、要求に従って再起動・Linuxユーザー作成を済ませる。既に使っているdistributionがあれば、その環境を確認して使用する。

```powershell
wsl --install -d Ubuntu
```

NVIDIA driverはWindows側に導入する。WSLにはLinux用のNVIDIA display driverを追加しない。[NVIDIAのWSL/CUDA手順](https://docs.nvidia.com/cuda/wsl-user-guide/index.html)

以降はUbuntu等の**WSL Linux shell**で実行する。プロジェクトとhot dataはまずLinux側のfilesystem（例: `~/src/`）へ置き、Windows側volumeとのI/O比較はPhase 4で行う。

## 2. Linux側でGitHubとuvを準備

以下のパッケージ導入例はUbuntu用。既に導入済みなら不要。

```sh
sudo apt update
sudo apt install -y git curl ca-certificates gh
```

private GitHub repositoryを読めるアカウントで、WSL側のGitHub CLIへログインする。Windows側のログイン状態がそのままLinux側にもあるとは仮定しない。

```sh
gh auth login --hostname github.com --git-protocol https --web
gh auth setup-git
mkdir -p ~/src
git clone https://github.com/ayutaz/japanese-tiny-llm-10m.git ~/src/japanese-tiny-llm-10m
cd ~/src/japanese-tiny-llm-10m
git status -sb
git rev-parse HEAD
```

既にclone済みなら、そのdirectoryでローカル変更を確認し、保存したうえで`git pull --ff-only`する。再開時のGit commitを環境reportに残す。

uvが未導入の場合のみ、Linux用の[公式インストール手順](https://docs.astral.sh/uv/getting-started/installation/)を実行する。

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

インストーラーが案内するPATH設定、またはshellの再起動後、project rootで実行:

```sh
uv --version
uv python install 3.12.7
uv sync --frozen --python 3.12.7 --extra hub --extra data --extra ml --extra export
```

Macの`.venv`は移さず、このPC用に作り直す。Python依存は`pip install`で追加せず、用途に応じて`uv add --optional ml ...`等で`pyproject.toml`と`uv.lock`を更新する。

## 3. Hugging FaceからTokenizerとデータを復元

同じproject rootで:

```sh
uv run --frozen --extra hub scripts/download_hub_artifacts.py
```

認証は不要。`configs/hub/artifacts.json`の固定commitから取得し、manifest SHAと全payloadのサイズ・SHA-256を検証してから復元する。新規cloneでの期待結果:

```json
{"status":"passed","verified_files":25,"restored_files":16,"revision":"0b1042979bf32899e24da30790e3ae6b239013c3"}
```

同じfileが配置済みなら`restored_files`は0になる。内容が違う既存fileは上書きせず停止する。その場合は差分のある旧artifactを別directoryへ退避し、公開版を新しい入力として復元する。取得cacheは`artifacts/hub-downloads/<commit>/`、復元先は次のとおり:

| 復元先 | 内容 |
|---|---|
| `artifacts/phase2/4096/` | 4k model/vocab、wrapper・special設定、metadataの5 files |
| `artifacts/phase2/8192/` | 8k model/vocab、wrapper・special設定、metadataの5 files |
| `data/phase1/processed/` | corpus、Parquet manifest、split manifest、Tokenizer sample、二つのreportの6 files |

本文22,998件のsplitはtrain 20,710 / dev 1,074 / test 1,214。Tokenizer sampleはtrainのみの2,444文書。Parquetは採否を含む取得23,000件を保持するので、学習入力は**採用corpusのtrain split**を使う。dev/testや`eval/`の固定suiteを学習に混ぜない。

recordの`kind`・`bucket`・`split`を保持し、Base本文と会話学習の選択を明示する。会話ではrole IDを構造として挿入し、SFTの教師はAssistant本文＋EOTに限定する。公開pilotを区別せず一種類の学習用textへ変換しない。[Tokenizer契約](04_tokenizer.md)と[学習計画](06_training_plan.md)を参照する。

公開modelはiMacのユーザーpathを含む`trainer_spec.model_prefix`だけを除去したコピーで、token ID契約は同じだが旧Phase 2 modelとbyte hashが異なる。公開manifest/training metadataのhashを正として記録する。旧ランダム重みHF/GGUFは旧model hashにbindされているため、公開コピーを使った再比較ではexportし直す。[公開前の確認と新hash](20_publication_review.md)

最初のCUDA確認にはMacのnative binary、Phase 3のランダム重み、raw archiveは不要。Tokenizer再学習・原データ再取得・CPU GGUF全比較を前提にせず、公開版で再開する。

## 4. CPU契約とCUDA環境を確認

```sh
uv run --frozen --extra data scripts/validate_phase0.py --output reports/phase4/phase0_validation.json
uv run --frozen --extra data --extra ml --extra export pytest -q -ra
uv run --frozen --extra data --extra ml --extra export scripts/experiment.py capture-environment --probe-torch --output reports/phase4/environment.json
```

引継ぎ時点のsuiteは48 tests・skip 0。Tokenizerがないとskipするテストがあるため、成功数だけでなくskip理由を確認する。CPUテスト成功はCUDAの学習・再開検証の代わりにはならない。

`reports/phase4/environment.json`で次を確認する:

- `platform.system`がLinux、`platform.is_wsl`がtrueで、Python・uv・Git commit・lock hashが記録されている。
- `nvidia_smi`にRTX 4090とdriver・メモリが記録されている。
- `torch_probe.cuda_available`と`bf16_supported`がtrue、`cuda_runtime`が記録されている。
- `wsl_observation`に実際のWSL version・distribution実行方式がある。取得できなければPowerShellの表示を別途残す。

`nvidia-smi`がLinux側PATHにない場合は`/usr/lib/wsl/lib/nvidia-smi`を確認し、必要ならそのdirectoryをPATHへ追加して環境を再記録する。`cuda_available=false`なら先にdriver/WSL/PyTorch wheelを確認する。固定lockのPyTorchと実機CUDA互換性はまだ未検証なので、wheel/indexの変更が必要なら[PyTorchの公式選択手順](https://pytorch.org/get-started/locally/)を参照し、uv管理の依存とlockを更新してから再記録する。CUDAを確認できない状態でGPU学習済みと扱わない。

`training_target.verified`は既存の環境captureではfalseを出す準備用ラベル。実際のprobe結果とPhase 4の検証reportを使い、probeだけで移行gate完了とはしない。

## 5. 入力付きの準備runを記録

まず本命T8K用の入力とコードをsnapshotに残す:

```sh
JMICRO_HANDOFF_RUN=$(uv run --frozen --extra data --extra ml scripts/experiment.py prepare-run --name phase4-handoff-t8k --output-root reports/phase4 --tokenizer-artifact artifacts/phase2/8192/tokenizer.model --dataset-manifest data/phase1/processed/dataset_manifest.parquet)
uv run --frozen --extra data --extra ml scripts/experiment.py verify-run "$JMICRO_HANDOFF_RUN"
```

表示されたrun directoryと`reports/phase4/experiments.jsonl`を保持する。既存CLIは準備runを`p0-...`、`phase: 0`、`kind: preparation`として記録する仕様であり、学習開始・Phase 4完了を意味しない。実学習runへのschema/ledger拡張は次の実装に含める。T4K比較では4096 modelを入力にした別runを記録する。

shard/checkpointの外部領域の候補を用意する:

```sh
export JMICRO_DATA_ROOT="$HOME/jmicro-data"
mkdir -p "$JMICRO_DATA_ROOT"
```

これは`configs/training/baseline.json`等にある環境変数名。**現時点では学習loaderが未実装で、download helperの復元先はproject root固定**。環境変数を設定しただけでdataが移動したり学習が始まったりはしない。Phase 4実装時にshard/checkpointのpathへ反映する。

## 6. この後に実装する順番

以下はこれから作る処理であり、現時点の実行commandはまだない。最初はT8Kで最小経路を成立させ、T4Kの比較へ広げる。

| 順番 | 作業 | 通過条件・残す証拠 |
|---|---|---|
| 1 | 公開pilotのtrainを`jmicro.tokenizer.Tokenizer`でencodeし、uint16 shard・document index・checksum・mmap loaderを実装 | token ID契約と文書/split境界が一致。消費位置を保存できる |
| 2 | 既存`jmicro.model`にAdamW、BF16 autocast、gradient accumulation、scheduler、checkpointを接続 | 小batchの実shardでfinite forward/backwardとoptimizer 1 stepが成立 |
| 3 | 本文NLL/BPBと固定Base生成suiteのrunner、保存再開を実装 | 本文を一度ずつ採点し、共通bytes分母・loss正規化・評価によるRNG干渉を検証 |
| 4 | 連続200 stepsと100 steps→保存→再開100 stepsを比較 | 消費token列が一致し、loss/weightsが同環境で許容誤差内。RNG、optimizer、scheduler、sampler状態を復元 |
| 5 | 最大安定batch、backend/compile、synthetic/実shard I/Oを測定 | 学習・評価・保存を含むVRAM、定常tokens/sec、data wait、保存時間を記録 |
| 6 | Phase 5の100件overfit、10M-token smokeへ進む | 学習→評価→生成→保存再開が一周。100MでT4K/T8K等を一要因ずつ比較 |

学習configは[baseline.json](../configs/training/baseline.json)、モデルは[t8k.json](../configs/models/t8k.json)・[t4k.json](../configs/models/t4k.json)、Tokenizer契約は[contract.json](../configs/tokenizer/contract.json)を参照する。LR等は候補値で、micro batch・effective batch・warmup・総stepsの未測定値は未確定のままになっている。

batchは8→16→32→64…と増やして境界の中間値も測る。初期動作確認の小batch後、本学習はユーザー方針の**最大安定batch**を使う。最大容量と最高tokens/secのbatchは両方記録し、micro batchとeffective batchを区別する。GPUの実測前に所要時間やbatchの確定値を置かない。

Phase 4では少なくとも`environment.json`、`handoff_report.json`、`resume_report.json`、`throughput_report.json`、`base_evaluation_contract_report.json`、`resource_budget.md`と復元可能checkpointを残す。環境・Phase 0確認report以外はこれから作る成果物。100M〜50Bの予算は`予定tokens / 定常tokens/sec + 評価・保存・比較の時間`で更新する。[Phase 4の全完了条件](15_project_roadmap.md#phase-4-学習器shard再開4090-benchmark)

## 次の担当へ渡す文面

別PCでprojectを開いた後、この文面で再開できる:

```text
このリポジトリの続きをWindows/WSL Linux＋RTX 4090 24GBで進めてください。
最初にREADME.md、docs/windows_handoff.md、docs/15_project_roadmap.md、docs/10_next_steps.mdを読んで現在地を確認してください。
Phase 0〜3は完了、本学習は未実施。次はPhase 4です。
コードはprivate GitHubのmain、Tokenizerとpilotはconfigs/hub/artifacts.jsonで固定したpublic Hugging Face commitから取得します。
公開Tokenizerはローカル保存先metadataだけを除去しているため旧artifactとbyte hashが違います。公開manifestのhashを記録してください。
Pythonはuv、依存変更はuv addを使ってください。
まず成果物の復元・skipのないテスト・CUDA/BF16確認・入力付き準備runを済ませてください。
次にT8Kでuint16 shard/loader、最小学習器、評価runner、保存再開を実装し、連続200 stepsと100+100 stepsを比較してください。
その後、実shardで最大安定batchと速度を測り、Phase 5のoverfit/10M smokeへ進めてください。
完成までの時間短縮を優先し、関係のない原データ再取得・Tokenizer再学習・Phase 3全検証は繰り返さないでください。
実際のGPU結果・未達事項・次の作業をreportとdocsに残してください。
```

## この手順の検証範囲

文書のコマンドoptionを既存CLIと照合し、Hubの固定commit/manifest hash、関連文書の内部fileリンク、config schema、uv lockを確認した。匿名取得済みの公開8k modelとParquet manifestを使い、iMacで実際に入力付き`prepare-run`→`verify-run`を実行して成功した。Windowsのインストール・CUDA・GPU学習・保存再開は移行先で実施する検証として残っている。
