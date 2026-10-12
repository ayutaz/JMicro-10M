# Windows / WSL 引継ぎ

2026-10-13 JST 計画更新: 最新の課題解決方法と計画を[計画135](135_chat_problem_solution_plan.md)に整理した。教材の汎化改善を第一比較、正しい履歴での改善後に誤履歴回復、paddingを別の効率比較とする。既存D1準備の小記録はTRAIN40,126 target・固定280sample問題0・CPU消費チェック合格を示すが、独立人間確認・新DEV・CUDA gate・学習・品質は未確認。今回の依頼では計画と記録のみを更新し、新しい教材生成・GPU実験・学習は開始しない。Base/Chat未完成・未採用、10Mと元の品質基準を維持する。

2026-10-12 最終状態: 計画131の段階0–5の学習・全評価・結果報告を終え、C0/C1とも不合格で閉鎖。各1,899,555 Assistant本文+EOT教師、全14suite・3,066内容判断、固定NLL7点を確認した。最終新DEVの文法・関連性同時2はC0 11/80、C1 15/80（必要56）、自己生成最終文脈2は4/24、2/24（必要15）。GPU累積70.794分/6時間上限。合格候補がなく保持/samplingは条件付き省略・品質未確認。Base/Chat未完成・未採用。元10B UIを復帰。追加実験は停止し、[結果132](132_chat_improvement_execution.md)と[次の未実行計画133](133_chat_generalization_followup_plan.md)を参照する。

[完了監査](../reports/phase7/chat-improvement-20261012/completion.json)。以下の調査・事前計画・過去実験の記述は各時点の履歴で、現在の開始指示ではない。

## 過去の計画と経緯

最新の対策計画: [131](131_chat_improvement_execution_plan.md)。段階0–5の第一比較は2条件・各約1.9M Assistant教師、教師量schedule、累積GPU6時間上限案、未使用DEVと旧回帰で原gate確認、報告停止。新しいcontract/runner/評価入口が必要で、旧3周runを再利用して起動しない。計画JSONは文書検証用で実行configではない。計画作成依頼では教材準備/GPU実行を再開していない。回復教材・padding・最終採用確認は別の後続段階。

最終更新: 2026-10-12 JST。**問題点と改善方法の調査130を完了。計画128の限定Chat-first診断は不合格終了、学習・GPU診断・教材準備は停止中、Base/Chat未採用。** [状態](autonomous_status.md)、[調査130](130_chat_failure_improvement_investigation.md)、[実行・結果129](129_chat_first_sft_execution.md)、[完了監査](../reports/phase7/chat-first-sft-20261010/completion.json)を先に読む。Base復旧を選ぶ場合の[計画124](124_base_recovery_plan.md)は未再開。

今回の調査は保存済み小reportの再集計・静的コード確認・公開一次資料調査のみ。[証拠](../reports/investigation/chat_improvement_20261012/README.md)。教材変更の同教師量比較を第一候補とし、履歴長でLR scheduleが変わる交絡を先に解消する。新教材/比較configは未作成。再集計は `pwsh -NoProfile -File scripts/analyze_chat_first_failures.ps1`。Python/GPU/教材走査は不要。今回変更したscriptはWindowsの報告分析用で、WSLの学習sourceを変更・同期しない。元UIの現在の生存は今回未確認。追加実行やpushの許可とは扱わない。

元WebUI10Bからfresh AdamWでSFTを3周、1,899,555 Assistant+EOT教師tokens・121,098応答・3,785更新まで実施した。元採用gateを変更せず専用診断入口を使用。1/2/3周の全stateはWSLの reports/phase7/chat-first-sft-20261010/ に保存し、親10B・Tokenizer・モデル構成は保全。Gitに重みや教材は入れない。config、job、metrics、training_audit、raw、全notes、paired比較、completionを保存する。

全4条件876応答を確認し、3周候補も内容17/80・最終文脈2/24・自生成停止51/59で事前基準未達。sampling・Base保持・候補とのローカル5会話は合格候補なしの条件により省略。実装した診断CLIはcompile確認だけでGPU未実行。保持・独立seed・人間blind・fullDEV/TESTは完了扱いにしない。追加実験・量子化・公開へ進まない。完了runを再起動しない。

元UIは終端に元10Bへ復帰し、HTTP親SHA・busy=falseと実processを確認した。保存済みPIDを将来の生存証拠にせず、reports/local/webui/server.json と実PID/boot/start・HTTPを再確認する。計画128の「入口未実装・学習0」は作成時点の履歴。

[調査127](127_rebuild_investigation.md)の公開資料は参照用で、モデルへ移植していない。今回の診断にGitHub push・外部公開は含まない。既存remote認証の401を同じ条件で再試行しない。
## 将来確認するためのモデル保存版

[JMicro-10M-research-archive](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive)へ主要3系列をpublic / gated=manualで保存済み。revision `853d52d2323653331b610249912fbe25615615fc`。native safetensors・共通Tokenizer・optimizer/scheduler/RNG等の数値状態・実装/設定/文書/評価metadataがある。データセットとsamplerは含めず、元checkpointの完全な代替ではない。[保存内容・uv読み込み手順126](126_model_archive.md)、[全公開fileのhash照合report](../reports/publication/model_archive_20261009.json)。

ユーザーの「データセットは残さなくてよい」は今回のアップロード対象から除く指定であり、既存のWSLデータを削除する指示とは扱わない。元のローカルdata/checkpointを削除・変更していない。

後続の「すべてpushして」は、残っていた全体記録125・詳細台帳・記録作成スクリプトとREADMEを既存GitHubへ保存する依頼。学習の再開ではない。全経緯は[125](125_project_retrospective.md)、元報告の指標・採否は[詳細台帳](retrospective/README.md)から参照する。

## 固定方針と実行範囲

10Mのサイズ維持がユーザーの優先条件。現在10,001,152 parameters、既存9.5M〜10.1Mの総parameter予算を保ち、大型化や大型モデル比較を復旧・改善の既定作業にしない。元の日本語Base品質基準を維持する。128のdirect SFTは実測batch32・config凍結・3周・matched全内容評価まで完了し、全候補不合格で終了。結果記録で停止し、Base復旧を選ぶ場合の124も保持する。

## 正本と保存場所

| 項目 | 保存場所・確認済み構成 |
|---|---|
| Git正本 | Windows `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`。最新local commitを引継ぎ、remoteが最新とは仮定しない |
| WSL実行コピー | `/home/aihub_ubuntu/src/japanese-tiny-llm-10m` |
| 大容量データ | `/home/aihub_ubuntu/jmicro-data`。Linux diskで処理・学習 |
| 確認済み環境 | WSL package3.0.1 / Ubuntu WSL2 / RTX4090 / Windows driver616.92 / Python3.12.7 / PyTorch2.14.1+cu130 / BF16 |
| Tokenizer | `artifacts/phase2/4096/tokenizer.model`、SHA256 `a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318` |
| モデル | 10,001,152 parameters。最新2B候補、staged参考系列、元10B UIは別の重み |

WindowsのNVIDIA driverがWSL CUDAにも関係する。WSLへLinux display driverを追加しない。現在の環境変更は不要で、新PC・runtime変更時に必要な範囲だけ再確認する。学習の停止中にdriver更新やdata再構築を開始しない。

## 完了jobとUI

最新scienceは `reports/phase6/base-teacher-decay-2b-20261008/`。PID118881 / boot `4052bfc5-3850-44e4-9123-d34a9e19f36e` / start_ticks8215874は終了し、Windows worker38176はexit0。累積2B教師・212095更新、全80レビュー済み、不採用・固定条件closed。追加GPU26,060.094秒、pilot込27,475.228秒、ledger closed。**完了runを再起動しない。**

元[WebUI](http://127.0.0.1:7860)は10,000,007,168学習tokensの元10B checkpointを配信。2026-10-09 JSTの文書更新時にPID120460 / start_ticks10822295、HTTP親SHA `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290` /busy=falseを再確認した。将来は `reports/local/webui/server.json` と実PID/boot/start、HTTPを再確認する。保存PIDだけで稼働を判定しない。

Windows正本でのUI操作:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/start_webui.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/stop_webui.ps1
Invoke-RestMethod http://127.0.0.1:7860/api/model
```

[UI操作43](43_local_webui.md)。既に起動済みなら重複起動しない。停止中もUIは利用可能のままにする。明示的に再開されたGPU実験が必要なときだけidle確認後に停止し、終端で元モデルへ復帰する。

## Git外で必ず保全するもの

以下はWSL repo相対、またはdata root相対。Git/公開Hubだけでは学習済み状態を復元できない。

| 場所 | 内容 |
|---|---|
| `reports/phase6/base-teacher-decay-2b-20261008/` | 最新のlatest.pt、optimizer/scheduler/RNG/sampler/counters、metrics、resume gate、job/result、評価raw |
| `reports/phase6/base-teacher-decay-pilot-20261008/` | 同条件94M親、元config/source/履歴 |
| `reports/phase6/base-parallel-residual-comparison-20261007/` | 元sequential2B対照と閉じたparallel比較、重み・原レビュー |
| `reports/phase6/base-10b-20261004/` | 元UIのstable/final、特に `decay/checkpoint-00305176.pt` と再開state |
| data: `phase6/textbook-mixture-20261006/large` | 最新accepted混合2Bのstream/index/manifest/ready/source |
| data: `phase6/expanded-v2/shards` | 独立DEVとmanifest。TRAINとは分離 |
| data: `phase6/ten-billion/prepared-v2/export-001/shards` | 元12.23B Webとsplit/source履歴 |
| `artifacts/phase2/{4096,8192}/`、必要な `data/phase1/processed/` | pinned Tokenizer/pilot |
| 全旧run/data | staged参考系列・旧11B比較・失敗/採用候補・全Phase0〜5の記録。下記履歴リストも参照 |

最新latest.pt SHA256は `03ebf266853541759054ee7100903fa175815adfcfc8e62e559ccdb1ce657442`。checkpointはGitに加えず、転送時は保存済みSHAへ照合する。移行しない通常文書更新で全重み・13GB index・全corpusを再走査しない。Gitには最新completion、全80notes、raw生成・小評価記録・終端stateを保存済み。

job.jsonの周期heartbeatは212080更新/1,999,868,016教師だが、最終result/train-result/checkpointは212095更新/正確に2B。runner resultのcontent_pendingはその後の[completion](../reports/phase6/base_teacher_decay_2b_completion.json)で解消済み。元記録を「修正」して履歴を失わない。

## 新PC・欠損時だけ行う復元

PowerShellで `wsl --version`、`wsl -l -v`、`nvidia-smi` を確認する。WSL package3.xとdistributionのWSL2は別の値。必要時のみ `scripts/setup_windows_wsl.ps1` を使い、昇格・再起動・初回Linuxユーザー作成が必要なら外部blockerを記録する。

Linux project rootで固定環境を復元する:

```sh
uv python install 3.12.7
uv sync --frozen --python 3.12.7 --extra hub --extra data --extra ml --extra export
git config --local user.name yousan
git config --local user.email ka1357amnbpdr@gmail.com
```

全Pythonは `uv run --frozen --extra hub --extra data --extra ml --extra export ...`。依存変更は `uv add`。system Python/pipへ切り替えない。Mac/別OSのvenv/native binaryはコピーしない。

固定公開pilot/Tokenizerはcommit `0b1042979bf32899e24da30790e3ae6b239013c3`、manifest SHA `8072bd218be26637a51c7c11540f1c8c636392c3b1a91f805a5e317e6ca55a09`。不足時のみ次を使い、hash確認後に復元する。[詳細](huggingface_handoff.md)。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/download_hub_artifacts.py
```

Hubには学習済み重み・12.23B shardsはない。環境変更時の証拠は新しい保存先へ記録し、既存Phaseの完了reportを上書きしない。必要時の環境取得:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/experiment.py capture-environment --probe-torch --output reports/local/handoff/environment.json
```

## 再開時の手順

1. 最新Windows local commitとAGENTS/status/roadmap/本書/計画128を読む。Base復旧を選ぶ場合は124も読む。
2. ユーザーが再開した範囲と10M維持の固定条件を確認する。文書更新だけならGPU/data/診断へ進まない。
3. 実process・GPU lock・job/result・有効checkpointを確認する。観測timeoutや残存lockだけで終了を決めない。
4. 最新teacher-decay pilot/2Bは完了・不採用なので復旧対象にしない。限定Chat診断を再開した場合は128の元10B親確認と専用入口の実装から始め、Base復旧を選んだ場合は124の次条件選定から始める。
5. 新実験は不足command/型付き証拠接続/関連checks/予算/configを先に完成する。長期jobは全state再開gate・永続identity/ledgerを必須とする。
6. native方式の独立seed/fullDEV/TEST接続は未完成。旧stable+20M形式へ偽装しない。128の限定診断以外の通常Chat完成と量子化は別の再開判断まで進めず、未採用Baseを採用済みへ偽装しない。

本当に未完了のjobを復旧する場合に限り、同じ凍結条件・累積予算でvalid checkpointから再開する。歴史的なrestart commandは現在の実行指示ではない。外部公開・有料cloud・他者連絡は別途許可が必要。自動pushなし。

更新前の全引継ぎ原文と旧runの詳細リストは[引継ぎ履歴20261008](windows_handoff_history_20261008.md)。実験記録やPhase0〜3を消さず保全する。
