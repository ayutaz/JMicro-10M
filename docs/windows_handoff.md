# Windows/WSL引き継ぎ

最終更新: 2026-10-05 JST。最新完了は[結果60](60_dataset_expansion_results.md)、次回は[計画61・未実行](61_condition_preservation_next_plan.md)。現在の依頼は文書更新だけ。旧/新各追加1Bを含む計画58は完了し、不採用・条件付き全文未起動で停止した。完成runを追加学習として再起動しない。

## 現在の構成と確認先

| 項目 | 値・確認方法 |
|---|---|
| 正本 | Windows `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`。最新local commitを移し、remoteだけを最新と仮定しない |
| Linux実行コピー / data | `/home/aihub_ubuntu/src/japanese-tiny-llm-10m` / `/home/aihub_ubuntu/jmicro-data` |
| 既存実測環境 | WSL package3.0.1.0 / Ubuntu WSL2 / RTX4090 / Windows driver616.92 / uv Python3.12.7 / PyTorch2.14.1+cu130。新PCでは再確認する |
| モデル | 10,001,152 parameters。主系列/UIの学習量10,000,007,168tokens |
| 準備量 | Web12,225,819,077、短い物語200,000,192tokens |
| 最新比較 | 旧60M/新200M各追加1,000,013,824、各累積11,000,020,992tokens。科学2,000,027,648/検証262,144別 |
| 最新判断 | EOS34→25/一貫性15→9/適切完結20→19（各80）、候補不採用。常識は改善。Base/Chat未達 |
| 完了証拠 | Windows dataset_expansion各JSON、実験完了local commit `afad164`。最新の文書更新commitも引き継ぐ |

## 現モデルのUIとprocess

[UI](http://127.0.0.1:7860)は元final10Bを配信。今回読み取り確認したactual PID359102 / boot`53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe` / start_ticks7216365、HTTP親SHA`410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`/training_tokens10,000,007,168/busy=false。科学PID239609は終了。後日の現在値はLinux `reports/local/webui/server.json`とactual identity/HTTPを照合し、保存PIDだけで判断しない。

Windows rootで`powershell -NoProfile -ExecutionPolicy Bypass -File scripts/start_webui.ps1`、停止は`scripts/stop_webui.ps1`。[操作43](43_local_webui.md)。稼働UIはGPU lockを保持する。今回の文書更新では停止・重み変更をしていない。

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


## 5. データ・weights・runを移す

Git/Hubだけでは学習済みweightsと大容量dataを復元できない。Windows正本のコード/config/schema/docs/小さなreportsと、Linuxの以下を別途保存する。元のcheckpoint/source/raw/reportを保持し、旧版も削除しない。

| Linux上の保存先（repo相対またはdata下） | 引き継ぐ内容 |
|---|---|
| `artifacts/phase2/4096/`・`8192/`、必要な`data/phase1/processed/` | pinned Tokenizer/pilot。固定Hub復元後にhash確認 |
| `~/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards` | 12.23B Web trainとsplit/manifest、必要なraw/source履歴 |
| `reports/phase6/base-10b-20261004/` | stable9.5Bとfinal10B `decay/checkpoint-00305176.pt`、optimizer/scheduler/RNG/sampler/counters/source/metrics |
| `reports/phase6/base-10b-comparison-20261004/`・日本語追加評価run | 全文NLL/400生成・固定80・日本語raw/source/job/review |
| `reports/phase6/story20-low-lr-10b-500m-20261005/` | 採用された500M研究候補とWeb対照、全文/長文と全320内容。実用品質合格とはしない |
| `reports/phase6/dataset-expansion-1b-20261005/` | control/refined両11B終端と500M中間checkpoint、全metrics/source/評価raw/annotations/review/judgment/completion/job |
| `~/jmicro-data/phase6/dataset-expansion-20261005/` | 200M shards/manifest/ready/content-review、新source pin/README/receipt/raw。旧60M sourceも保持 |
| 過去Phase0〜5、5B/100M/500M/一定LR1B等の各runとdata | 既存成果物・失敗/採用証拠・凍結config/source/重み。旧履歴の移行リストも参照 |

最新の旧final SHA`fd10dc1b358327bdbd8d3d58118c2cb096fc53d02b036f070e453911edf2b82a`、新final SHA`7932c04d905c0903eee338f08da2b3c44f5bde8fffc8dae237381de1f15c9391`、pool manifest SHA`a33ad89783d7b9c2f65eadc96ceca06d19c1e397b0dc95852b148d408cec7b12`。移したpayloadを各保存manifest/hashへ照合する。全12.23Bの新たな独立監査を移行で完了したと扱わない。

## 6. 実行と復旧の扱い

現在はplan58完了、plan61は提案。`scripts/run_dataset_expansion.ps1 -Mode screen`と旧`run_base_10b.sh --train`は完了したrunの履歴で、新実験として起動しない。plan61用のrunner/configはまだない。再開された実行範囲で必要なCLI・schema・関連checksを実装してから起動する。

本当に未完了のjobを復旧する場合だけactual PID/boot/start ticks・GPU lock・job/result・有効checkpoint・凍結条件を確認する。観測timeoutや残存lockだけを終了と判断せず、通常resumeでsource/schedule/budgetを変えない。UI復帰はactual processとHTTPのparent SHA/tokens/busyを確認する。

## 次の担当へ渡す文面

```text
AGENTS.md、docs/autonomous_status.md、docs/15_project_roadmap.md、docs/windows_handoff.md、最新結果60と次回計画61を読んでください。
計画58段階1〜3は完了、不採用と条件付き全文未起動を保存し、元final10B UIへ戻しています。
今回の文書更新は新しい学習の再開指示ではありません。plan61は未実行の提案です。
保存証拠・current process/HTTP・最新local commitを確認し、完了run/Tokenizer/全量照合を再実行しないでください。
Pythonはuv管理3.12.7、学習はWSL/Linux disk。Base/Chat未達・source/長さ/EOS差・独立監査/人手blind未完了を保持してください。
新data/GPU/20B/50B/Chat/test/push/publicationは再開された明示範囲でだけ進めます。
```

過去の移行・現在地の原文は[2026-10-05履歴](autonomous_history_20261005.md)、以前は[2026-10-04](autonomous_history_20261004.md)・[2026-10-03](autonomous_history_20261003.md)。凍結reportを現在値へ書き換えない。
