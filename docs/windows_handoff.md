# Windows/WSL引き継ぎ

最終更新: 2026-10-04。[現在地](autonomous_status.md)と[直接10B計画](39_learning_scale_and_generation_plan.md)を最初に読む。以前の停止境界・process情報・移行履歴は[2026-10-04保存履歴](autonomous_history_20261004.md)、初期復旧は[2026-10-03履歴](autonomous_history_20261003.md)に残す。

## 引継ぎ先と現在地

| 項目 | 現在の内容 |
|---|---|
| コード・docs・lock正本 | Windows `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m` |
| Linux実行コピー | `/home/aihub_ubuntu/src/japanese-tiny-llm-10m` |
| Linux data | `/home/aihub_ubuntu/jmicro-data` |
| repository | [private GitHub](https://github.com/ayutaz/japanese-tiny-llm-10m)。移行時はWindowsの最新local commitも引き継ぐ。remoteだけを最新と仮定しない |
| 実測済み環境 | WSL package 3.0.1.0 / Ubuntu WSL 2 / RTX 4090 / Windows driver 616.92 |
| Python / PyTorch | uv Python 3.12.7 / PyTorch 2.14.1、CUDA 13.0 |
| モデル・データ | 10,001,152 parameters / 準備済みtrain12,225,819,077 tokens |
| 学習・比較 | 主要Web5B、各100M仕上げ比較完了。Base/Chat品質は未達 |
| 次の実験 | 直接10Bの準備完了（local commit `4c3fbaf`）、科学学習step2とCPU保存確認19項目は完了。同条件品質評価step3も完了（CPU保存確認23項目） |

現在のPCは復元・CUDA検証済み。setup、Tokenizer学習、完了済みGPU studyを再実行しない。ユーザー指定step2の総10B学習と保存結果確認は完了。再開されたstep3品質評価も完了した。[品質結果](42_base_10b_quality_evaluation.md)。今回はreport/local commitで停止する。[本学習結果と速度](41_base_10b_training.md)。

## 現モデルをローカルで試す

2026-10-04の追加依頼で、学習済みfinal10BのWeb UIを起動した。Windowsのブラウザから `http://127.0.0.1:7860`。再起動は `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/start_webui.ps1`、停止は `scripts/stop_webui.ps1`。WSL/RTX4090で推論し、稼働中はGPU lockを保持する。[操作・保存先](43_local_webui.md)。学習・後続実験は再開していない。

## 1. Windows側でWSLとGPUを確認

新規PCや環境変更時にPowerShellで `wsl --version`、`wsl -l -v`、`nvidia-smi` を確認する。WSL package 3.xとdistributionのWSL 2は別の値。Windows driverでWSL CUDAを利用し、WSLへLinux display driverを追加しない。現在の固定構成は実CUDA/BF16学習で動作確認済み。

新規PCの準備が必要な場合のみ `powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\setup_windows_wsl.ps1` を使う。既存treeを上書きせず、OS昇格・再起動・初回Linuxユーザー作成が必要ならその外部操作をblockerとして記録する。

## 2. Linux側でコードとuvを準備

新規PCではprivate repositoryの認証・取得後、Windowsの最新local変更を保持して引き継ぐ。Macのvenv/native binaryは移さない。project rootで不足する環境だけ復元する。

```sh
uv python install 3.12.7
uv sync --frozen --python 3.12.7 --extra hub --extra data --extra ml --extra export
git config --local user.name yousan
git config --local user.email ka1357amnbpdr@gmail.com
```

すべてのPythonは `uv run --frozen --extra hub --extra data --extra ml --extra export ...`。依存変更は `uv add`。system Python/pipへ切り替えず、固定依存にアクセスできなければblockerを記録する。

## 3. Hugging FaceからTokenizerとデータを復元

固定[公開pilot/Tokenizer](https://huggingface.co/datasets/japanese-data-analyze/japanese-tiny-llm-10m-artifacts)は約107MB、25 payload。commit `0b1042979bf32899e24da30790e3ae6b239013c3`、manifest SHA256 `8072bd218be26637a51c7c11540f1c8c636392c3b1a91f805a5e317e6ca55a09` を使う。新規PCで不足する場合のみ実行する。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/download_hub_artifacts.py
```

hash確認後に `artifacts/phase2/{4096,8192}/` と `data/phase1/processed/` へ復元する。内容が異なる既存fileは上書きしない。[詳細](huggingface_handoff.md)。Hubには学習重み・12.23B shards・大型checkpointは含まれない。

## 4. 契約とCUDA環境を確認

新規環境・runtime変更時に必要な環境gateと関連testsを新しい `reports/local/handoff/` 等へ保存する。既存の完了reportを上書きせず、CPU成功をGPU成功に数えない。current runtimeの変更がなければ完了済み全suite・GPU比較を再実行しない。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/experiment.py capture-environment --probe-torch --output reports/local/handoff/environment.json
```

最新10B準備は[14 CPU testsと実CUDA全state一致、26 review checks](40_base_10b_preparation.md)で確認済み。旧Phase 4/5/6準備の証拠は各完了記録を保持する。

## 5. 入力・run・checkpointを引き継ぐ

Linux dataの `phase6/ten-billion/prepared-v2/export-001/shards`、必要なraw、Tokenizer、以下のrunとsource snapshot/log/checkpointを別途コピーする。Git/Hubだけでは復元できない。

- `reports/phase6/base-5b-20261004/`: stable親 `stable/checkpoint-00144959.pt`（4,750,016,512 tokens）とfinal5B `decay/checkpoint-00152588.pt`。
- `reports/phase6/eos-5b-finish-100m-20261004/`: Web/short20の `checkpoint-00155640.pt`、raw生成・評価。
- `reports/phase6/base-10b-20261004/`: 準備検証と科学job完了。stable9.5B/final10Bの両checkpoint、metrics/source/log/resultを保持。[保存結果](41_base_10b_training.md)。
- `reports/phase6/base-10b-comparison-20261004/`: 完了した同条件品質評価の全文文書別NLL、400 raw生成、固定80比較packet、自然停止9件、job/result/log/sourceを保持。[品質結果](42_base_10b_quality_evaluation.md)。評価Linux442/Windows31900は終了済み。
- 過去Phase 0〜5とPhase 6準備のreport、weights、native runtimeは保持する。

checkpointはmodel/optimizer/scheduler/RNG/sampler位置/消費tokensを完了updateで保存する。通常resumeでschedule/config/source/dataを変更しない。4.75B親SHAと各重みSHAは[status](autonomous_status.md)および保存reportを参照する。

長GPU jobはhidden Windows supervisorとLinuxのactual PID/boot ID/start ticks/stage/logを保存し、`~/jmicro-data/gpu.lock`で排他する。10B準備のLinux PID459・Windows PID29620は終了済みの履歴で、現在のjobではない。起動前に実process・GPU一覧・既存runを確認し、有効checkpointから再開する。

## 6. 実装済みCLIと次回の再開

AdamW、WSD stable/decay、StableExtensionTrainer、EOS短文mixture、学習/BPB/生成、表示helperは実装済み。Chat trainerとUTF8制約decoderは未実装・未適用。新10B専用品質比較は実装・実行済みで、同条件dev/400と内容確認を完了。学習完了CPU reviewは実装し、実際の終端保存stateと全metricsの19項目を確認済み。準備reviewを科学完了に流用しない。

中断復旧用コマンド履歴（今回のrunは完了しているため再起動しない）:

```sh
bash scripts/run_base_10b.sh --train
```

引数なし/`--verify-only`は準備確認だけで、完了済みならGPU検証を繰り返さない。旧5BやPhase 5 launcherを新10Bのcommandとして起動しない。学習後、新10Bだけ全文dev/固定400で評価し、既存5B・Web5.1B結果を再利用する。今回はstep3評価も完了し報告・commitで停止する。後続実験は別の再開依頼で進める。[残りの手順](27_phase6_remaining_plan.md)

## 次の担当へ渡す文面

```text
AGENTS.md、docs/autonomous_status.md、docs/15_project_roadmap.md、docs/windows_handoff.md、docs/39_learning_scale_and_generation_plan.mdを読んでください。
主要Web5Bと追加各100M仕上げ比較、直接10Bの準備が完了しています。10B科学学習step2とCPU保存確認19項目は完了、同条件品質評価step3も完了しています。
現在の指定step3も完了です。BPB0.954018 / 固定EOS0・反復53 / raw Unicode0、元増量gate合格と品質未達を保持してください。完了runを再起動せず、後続EOS/UTF8/Chat/20Bは新しい実行依頼に従ってください。
完了済みGPU study、旧5B比較、Tokenizer学習、大型全corpus照合を繰り返さないでください。
Pythonはuv、Linux dataを使用してください。actual process/lock/checkpointを確認して二重起動を避け、失敗証拠と未達品質を保持してください。
Windows正本の最新local commitとLinuxのsource/hashを確認してください。自動pushはしないでください。
```

## この手順の検証範囲

記載環境は現在のPCで動作確認済み。10B準備の実CUDA16更新/524,288検証tokensは科学学習tokensとは別会計。独立全12.23B監査は未完了。10Bの同条件自動評価と内容診断は完了、独立人手blind/test、Chat、新重みの量子化品質は未検証。品質基準を緩めず、新規環境では必要な変更部分を検証する。
