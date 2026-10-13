# Windows / WSL 引継ぎ

2026-10-14 現行: [結果141](141_chat_lr_comparison_results.md)で低LR候補を不合格・不採用と判定。全28セット・6,132判断・NLL7点、学習3,646更新/1,899,557教師、全state/予算と7条件分岐の科学監査は完了。独立確認は未実行・品質未確認。小report保存一覧final_archiveとWindows/WSL byte・ローカルcommitの納品確認final_delivery_checksをそろえて停止する。最終commitの照合まではgoal完了を宣言しない。追加GPU/新条件/教材準備は開始しない。最新科学監査2026-10-13T16:54:20Zで全job終端、元UI PID309447/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start55170810、HTTP親/Tokenizer/10M・busy=false・kernel lock一致。現在の生存は必要時に再照合し終了workerを再起動しない。候補全stateはWSL reports/phase7/chat-lr-20261014/S1、最終SHA f7e8bb8b1569cb45ac399108455a66c5922f64d7898e8ab6b4931ba13c856018。以下は途中と旧比較の引継ぎ履歴。

2026-10-14 明示再開: goal「3まで進めてください」は直前回答の介入1件選定→10M/原品質で比較→有望条件だけ独立確認を再開する。[計画139](139_chat_lr_comparison_plan.md)。SFTのpeak LR1e-4→3e-5だけを変更し、同TRAIN/同親/教師量、新DEV＋既知3回帰を登録する。Base/Chat未採用、旧135の完了と不採用を保持。以下の停止状態は今回再開前の履歴。

最新実績（2026-10-14 JST）: [139](139_chat_lr_comparison_plan.md)/[実行140](140_chat_lr_comparison_execution.md)でLR3e-5候補のCUDA25検証更新と全評価予測10,732.271秒/14,400秒が通過。本学習をdurable workerで開始し、15:43:54Zに実PID304617/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start54912399の生存と600更新/312,871教師を観測。全レビューは13/28セット・2,847/6,132判断・NLL1/7点。元親新DEVは全219理由付き判断を確認。最終採否・3段階の完了は未確認。準備時の元Chat TEST20行解析事故は保存・訂正済みで、有資格時は新しい封印Chat TESTが必要。

保存点監査追記: t1=1,215更新/633,206教師、t2=2,430更新/1,266,627教師の実入力/教師digest・LR列・全stateを確認して通過。15:57:11Zに同学習PID304617の実生存と2,500更新/1,303,091教師を観測。生成品質は未確認、t3/残15suite/NLL6点/採否・分岐・納品を継続する。

最終更新: 2026-10-13 JST。**最新の教材比較135は全6段階を完了し、138で不採用として閉鎖。Base/Chatは未完成・未採用。追加研究・準備・診断・評価・学習は停止する。** [状態](autonomous_status.md)、[最終結果138](138_chat_semantic_diversity_results.md)、[計画135](135_chat_problem_solution_plan.md)末尾を先に読む。旧runや今回の終了jobを再開手順に戻さない。

## 正本と保存場所

| 項目 | 保存場所・記録された構成 |
|---|---|
| Git正本 | Windows `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`。最新local HEADを確認し、remoteが同じとは仮定しない |
| WSL実行コピー | `/home/aihub_ubuntu/src/japanese-tiny-llm-10m` |
| 大容量データ | `/home/aihub_ubuntu/jmicro-data`。Linux diskで処理・学習 |
| 固定環境 | WSL package3.0.1 / Ubuntu WSL2 / RTX4090 / 記録時driver616.92 / Python3.12.7 / PyTorch2.14.1+cu130 / BF16。今回のruntime再測定ではない |
| Tokenizer | `artifacts/phase2/4096/tokenizer.model`、SHA `a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318` |
| nativeモデル | 10,001,152 parameters、既存9.5M〜10.1M内。`src/jmicro/model.py` SHA `298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83` |
| 最新結果保存 | [今回保存一覧](../reports/phase7/chat-semantic-diversity-20261013/final_archive.json)と[納品確認](../reports/phase7/chat-semantic-diversity-20261013/final_delivery_checks.json)。最新local commitは `git log -1` |

現在の環境変更は不要。Windows driverがWSL CUDAにも関係し、WSLへLinux display driverを追加しない。文書更新だけのときにdriver更新、uv依存変更、data再構築や全benchmarkを開始しない。

## 閉じた最新runとUI

`reports/phase7/chat-semantic-diversity-20261013/` は全21suite/4,599内容判断/固定NLL7点×2,554 target、S1全3state/実教師列、原採否・分岐・台帳の[科学監査](../reports/phase7/chat-semantic-diversity-20261013/completion.json)を完了した。S1は3,646更新/1,899,557教師、S0は最新D1の歴史stateで新学習0。両条件の内容/文脈は未達。保持/samplingは候補なしで未実行・品質未確認。追加学習・評価を起動しない。

元10B [WebUI](http://127.0.0.1:7860)は最終科学監査2026-10-13T09:44:20Zで実PID292581/boot `4052bfc5-3850-44e4-9123-d34a9e19f36e`/start_ticks52504723、HTTP親SHA `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`、Tokenizer/10M一致、busy=false、kernel GPU lock一致、競合jobなしを確認した。これは当時の観測で、将来の生存保証ではない。

UI操作や明示実行再開時だけ、`reports/local/webui/server.json` と実PID/boot/start、HTTP、kernel lockを照合する。稼働中なら重複起動しない。必要時のWindows操作:

```powershell
Invoke-RestMethod http://127.0.0.1:7860/api/model
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/start_webui.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/stop_webui.ps1
```

[操作43](43_local_webui.md)。次の研究は新しい明示再開と別契約から始め、終了済みの元比較や拒否paddingを再起動しない。

## Git外で保全する重みと教材

最新S1は `reports/phase7/chat-semantic-diversity-20261013/S1/checkpoint-00003646.pt`、SHA `6ca25064fa4ccb6784a05fa5ade43bfdaa87aeb55f11458a233eaf32664fd2ea`。同directoryに全3state/metrics/jobを保持し、data rootの `phase7/chat-semantic-diversity-20261013/` に教材・manifest・DEV・固定NLL targetを保持する。Gitには重みとdataset実体を含めない。以下の旧系列も保全する。以下はWSL repo相対、`data:` は大容量data root相対。今回は所在を原記録から案内し、全重み・全corpusの再hashは行わない。

| 場所 | 保全する内容 |
|---|---|
| `reports/phase7/chat-generalization-20261013/D1/` | `checkpoint-00003641.pt`、t1/t2、model/Adam/scheduler/RNG/sampler/counters、metrics/job/result。最新t3はSHA `aa84a1dc3fbbf1c264ebd9327ecc7183bf3d88c606e01bd0f82bb5351945aed6` |
| `reports/phase7/chat-generalization-20261013/padding/` | 固定/動的比較と連続/保存再開state、全数値差、失敗判定。main重みへ置換しない |
| `reports/phase7/chat-improvement-20261012/` | C0/C1の全3保存点、対照D0の再利用元、raw/notes/NLL/終端とsource |
| `reports/phase7/chat-first-sft-20261010/` | 最初のSFT3周の全state・raw・内容判断・不採用記録 |
| `data: phase7/chat-generalization-20261013/` | D1 TRAIN・manifest/sampler、未使用DEV・authored/固定NLL targetとhash |
| `data: phase7/chat-improvement-20261012/` | D0=旧C1 TRAIN、manifest/sampler・評価/教師根拠 |
| `reports/phase6/base-teacher-decay-2b-20261008/` | Base最新2Bの`latest.pt`、全state・metrics・raw。SHA `03ebf266853541759054ee7100903fa175815adfcfc8e62e559ccdb1ce657442` |
| `reports/phase6/base-teacher-decay-pilot-20261008/`、`base-parallel-residual-comparison-20261007/` | 閉じたBase pilot/対照・比較の歴史state/source/レビュー |
| `reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt` | 元UI10B親と再開state。SHA `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290` |
| `data: phase6/textbook-mixture-20261006/large` | accepted混合2Bのstream/index/manifest/ready/source |
| `data: phase6/expanded-v2/shards`、`phase6/ten-billion/prepared-v2/export-001/shards` | 独立DEV、元Web TRAIN12.23Bとsplit/source。全件独立corpus auditとは別 |
| `artifacts/phase2/{4096,8192}/`、全旧run/data | pinned Tokenizer/pilot、staged等の旧系列とPhase0〜5の全証拠 |

Gitに保存した小report/metadataと、WSLの重み・教材実体は別。datasetのarchive除外指定はローカル削除指示ではない。`job.json`の周期heartbeatと、最終result/checkpoint/completionの数値を混同せず、元履歴を上書きしない。

2026-10-09の[研究モデル保存版126](126_model_archive.md)は主要3系列・共通Tokenizer・数値学習状態等のpublic/manual gated保存。revision `853d52d2323653331b610249912fbe25615615fc`。データセットとsamplerを含まず、元checkpointの厳密再開代替ではない。後続Chat重みは公開していない。新しい公開やpushには別の明示指示が必要。

## 新PC・欠損時だけ行う復元

必要時だけ `wsl --version`、`wsl -l -v`、`nvidia-smi` を確認し、`scripts/setup_windows_wsl.ps1` を使用する。昇格・再起動・初回Linuxユーザー作成が必要なら外部blockerを記録する。WSL package3.xとdistributionのWSL2は別の値。

Linux project rootで固定環境を復元する:

```sh
uv python install 3.12.7
uv sync --frozen --python 3.12.7 --extra hub --extra data --extra ml --extra export
git config --local user.name yousan
git config --local user.email ka1357amnbpdr@gmail.com
```

全Pythonは `uv run --frozen --extra hub --extra data --extra ml --extra export ...`。依存変更は `uv add`、system Python/pipへ切り替えない。別OSのvenv/native binaryはコピーしない。

固定公開pilot/Tokenizerはcommit `0b1042979bf32899e24da30790e3ae6b239013c3`、manifest SHA `8072bd218be26637a51c7c11540f1c8c636392c3b1a91f805a5e317e6ca55a09`。不足時のみ取得してhashを照合する。[復元詳細](huggingface_handoff.md)。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/download_hub_artifacts.py
```

この固定bundleは学習済み重み/12.23B shardsのbackupではない。環境変更が必要な場合だけ新しい保存先へ証拠を記録し、旧Phase報告を上書きしない。

## 明示的な実行再開後の順序

1. Windows最新local HEADとAGENTS/status/ロードマップ/本書/結果136を読む。選んだ経路が教材比較なら135、Base復旧なら124を参照する。
2. 再開範囲と10M維持を確認する。文書更新だけならdata/GPU/診断/評価へ進まない。閉じた128/131/133を復旧対象にしない。
3. 新しい実験を実行する場合だけ、実process・GPU lock・job/result・対照stateと保存hashを確認する。観測timeoutだけで終了と決めず、同じhandleを再確認する。
4. 教材比較は新TRAIN版/未使用DEV/既知2回帰・専用contract/runnerを先に完成し、欠けたCLI・技術gate・全評価予算を解消してから実行。Base復旧なら124の次条件選定から始める。
5. 成立した既存証拠を条件一致時に再利用する。長期jobはPID/boot/start、累積GPU台帳、全state、実消費・保存再開を必須にし、frozen sourceを保全する。
6. 新規比較の結果を保存して一度報告・停止。不採用を追加周回/seed選別/閾値緩和で救済しない。独立学習seed43、人間blind、fullDEV、最終suite、protectedTEST、採用、量子化は別の再開判断。

本当に未完了の新jobを復旧する場合だけ、同じ凍結条件と累積予算でvalid checkpointから再開する。Base復旧は証拠を満たしたBaseで通知・停止。通常Chat完成、公開、有料cloud、他者連絡へ自動移行しない。

旧引継ぎの全文は[今回の履歴保存一覧](../reports/investigation/documentation_plan_refresh_20261013/baseline.json)と[20261008履歴](windows_handoff_history_20261008.md)へ保全した。原source/report/raw・Phase0〜3を変更していない。
