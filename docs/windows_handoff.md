# Windows/WSL引き継ぎ

最新再開（2026-10-05 JST）: [計画52段階1〜4](52_story20_low_lr_execution.md)を実行中。20%低LR100Mと全文の原条件通過後、固定4train filesを59,963,449 tokensへ構築し、約1.667周の再利用を明記して各500M比較を起動した。引継ぎにはLinux`reports/phase6/story20-low-lr-10b-100m-20261005/`の全科学/全文rawと、`story20-low-lr-10b-500m-20261005/`の途中checkpoint/metrics/source/job、`~/jmicro-data/phase6/simple-stories-ja-budget-20261005/`の原source参照/shards/content-reviewを含める。hidden Windows33908 / actual Linux174280 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4498545。actual processを照合し、liveなら同じjobを追跡して二重起動しない。現在UIは科学GPU中だけ停止、launcher finallyで元final10Bへ復帰する。320内容診断・原gate条件付き全文・段階4判断/report/local commitが残る。以下の旧停止境界は履歴として保持する。

最終更新: 2026-10-05 JST。[現在地](autonomous_status.md)と[最新比較48](48_complete_text_10b_comparison.md)を最初に読む。改善計画段階1〜3の学習・評価を完了し、最終report/local commit・UI復帰で停止する。以下の旧milestone記録は履歴として保持する。以前の停止境界・process情報・移行履歴は[2026-10-04保存履歴](autonomous_history_20261004.md)、初期復旧は[2026-10-03履歴](autonomous_history_20261003.md)に残す。

最新の移行対象: Linux `reports/phase6/complete-text-10b-100m-20261004/`（三枝checkpoint/metrics/raw240内容採点/source、旧失敗`conditional-full/`、完了`conditional-full-r1/`全文/400/長文rawを含む）と`~/jmicro-data/phase6/simple-stories-ja-20261004/`（固定source metadata/二つのtrain parquet/25,000,067-token shards）。Windowsの最終review/result/completionと最新local commitも移す。Linux17951/19791/37818は終了、再実行しない。新物語は親BPB悪化上限を超え未採用、Base/Chat品質目標は未達。UIは元final10B SHA410f975d…へ復帰、復帰時Linux49746 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks1043870、HTTP応答確認済み。現在のUI identityは`reports/local/webui/server.json`とactual processを照合する。完了比較の再開commandを追加学習に流用しない。

さらに新しい計画49の実行は[50](50_story10_and_budget_execution.md)/[判断51](51_story10_judgment_and_next_proposal.md)。Linux`reports/phase6/story10-10b-100m-20261005/`と`story10-low-lr-10b-100m-20261005/`のcheckpoints/metrics/source/raw generation/全240 annotations/tests/job/result/reviewも引き継ぐ。両10%枝は一貫性差4/6で未採用、全文と500Mは条件により未実施、科学139467/140216は終了。完了runnerを再起動しない。最新復帰時UI140800 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks1468219、元final10BでHTTP応答。次案20%低LR100Mは未実行で、今回はreport/local commitで停止する。

追加した日本語Base評価v2.1は[実施計画](45_japanese_base_evaluation_v2.md)/[実測結果](46_japanese_base_evaluation_v2_results.md)と`reports/phase6/japanese_base_v2_review.json`を参照する。移行時はLinux `reports/phase6/japanese-base-v2-20261004/`のraw/source/cpu、`japanese-base-v2-20261004-r1/pilot`の修正版意味診断、`~/jmicro-data/evaluation-v2`の公開評価cache/manifestも保存する。完了runのGPU再実行は不要。UIは評価後に復帰済み。新規評価の一括入口は`scripts/run_japanese_evaluation.ps1`で、UIを停止・finally復帰する。

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
| 学習・比較 | 主要Web10B、同じ親から三条件各100M・一次/全文/長文評価完了。実験枝各総10.1B、新物語pool25M。Base/Chat品質は未達 |
| 次の行動 | 最終report/local commitで停止。500M/1B/20B/50B/Chatは新しい依頼まで開始しない |

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
