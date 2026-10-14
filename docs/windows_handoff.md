# Windows / WSL 引継ぎ

2026-10-15最新: scienceはWSL `reports/phase6/base-fim-pilot-20261015/`で実PID1343/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start64143474、Windows durable worker34484が稼働。[起動観測](../reports/phase6/fim-feasibility-20261015/science_launch_observation.json)の675更新/6352596教師は途中値。`configs/phase6/base_fim_pilot_20261015.json` SHAc514ac4a944e7ca5974879585d902f0276a7ab544bf4ad9f226d971f48a61198、10000更新/94160195教師、science2519秒/技術含む3600秒を凍結。新`run_base_fim_pilot.py`/`evaluate_base_fim_pilot.py`/`review_base_fim_pilot.py`と13 CPU checks、DEV-only open監視を接続。旧readerを使用しない。最初のlauncher35328はscience開始前に停止し原記録を保全。`run_base_fim_pilot_v2.ps1`は既知UIのGPU解放だけを最大15秒待つ運用修理で、科学source/条件/予算を変更していない。稼働中へ再launch/refreeze/source editしない。実job/heartbeat/lock/PIDを照合し、真に中断した場合のみ閉じた累積台帳・同binding・有効checkpointで復旧する。UIはこのGPU仕事中のみ停止し、launcherが終端で元10Bへ戻す。終了後は全80個別notesと終端state/全10000更新/対照元streamを監査してreviewする。独立学習/fullDEV/新TEST/採用はまだ実施していない。下は開始前の準備記録。

更新: 2026-10-15 JST。「4まで」で評価分離修理からBase最終判定までが明示再開。[修理147](147_evaluation_boundary_repair.md)の新DEV reader/生成/reviewとCPU21 checks・実DEV80入力監査を完了。新契約は`eval/isolated-base-dev-v1/base.dev.manifest.json` SHA6198b43df8f4cf389e9de74c038e2e93d18665413477b27359ab352a02f69fa7をpinする。後続fresh FIM prospective案と技術probeは下記。旧混在readerを新比較へ呼ばず、frozen過去source/結果を変更しない。科学学習/品質評価0・科学契約未凍結。起動前の実process/lock確認が必要で、過去PIDを現在保証にしない。

[最新readiness](../reports/phase6/fim-feasibility-20261015/protocol_readiness.json)と[prospective pilot](../reports/phase6/fim-feasibility-20261015/fresh_FIM_pilot_proposal.json)を正とする。`scripts/base_fim_sampler.py`/`base_fim_trainer.py`は新kindで元quota選択後のPSM、同Native weights/Adam/clock、独立augmentation RNGを保存。CPU16＋workflow9 checksと実10M zero/元source32×80の照合を完了。`scripts/probe_base_fim.py`と`configs/phase6/base_fim_probe_20261015.json` SHAa0743dc70df9f51b26191eb1173359c0d8a775d10e734f9810fc14092afca6f2の専用probeはcomplete/終了確認。40技術更新/383190教師、GPU9.153451952966861秒、全state4対2+2、80x1024/32 timingsがpassed、pilot予測2519秒は提案総上限3600秒以内。再実行しない。`verification_*.pt`とTRAIN input payloadはWSLのみ、science初期化やGitへ移さない。science永続runner/launcherと安全なDEV256/80評価・notes/reviewerは未実装、科学契約をまだ凍結・開始しない。元10B UIは実PID520/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start63915576とHTTPの元親/Tokenizer/10M/idleを確認して復帰した。旧Japanese `build_tasks`もsafe DEV readerではなく、今後のfixed diagnosticsへ無検査で呼ばない。

`scripts/audit_fim_compatibility.py` は新しい固定CPU診断で、FIM trainerではない。契約`configs/phase6/fim_CPU_feasibility_20261015.json`と[receipt](../reports/phase6/fim-feasibility-20261015/actual_TRAIN_serialization_audit.json)を保存済み。各genre8の計24 TRAIN文書・serializer20 CPU checks、原token/bytes/EOS保存、24/24がcontext1024内、ordinary marker35token/追加入力標本比26.2746%。完了診断を再実行しない。原TRAIN index/cache identityとTokenizerを再利用し、本文・dataset・重みをGitへexportしていない。GPU/科学学習/DEV/TEST0、成熟親100M FIMを選定していない。fresh比較の価値と実行契約は[選定メモ](../reports/phase6/fim-feasibility-20261015/selection_assessment.json)の未解決項目から判断する。

[最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md) / [次の計画145](145_post_rejection_next_plan.md) / [今回更新146](146_documentation_followup.md)。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。

## 最新Baseと最後の観測

同10M・元10B親・同accepted TRAIN/教師/seed/batch/optimizerで、文書長によるCE寄与だけを変更。実17,698更新・100,000,000教師、全80理由付き判断、共通DEV256/Japanese192/331/1119を確認した。新GPUは科学1,474.808693＋技術8.721357＝1,483.530050秒。技術47更新/273,521教師は品質/本学習へ加算しない。

最終候補はWSL `reports/phase6/base-document-balance-comparison-20261014/document_balance/checkpoint-00017698.pt`、SHA `d89caf23bd7d2d8d81f298cb6f1fcbfe5fbd581105f91be1c3cfc18cefc9f86b`。full state/sampler/metricsはWSL、Windowsはportable viewと40保存file。結果1901564/receipt fc1a3fcの保存確認済み。

最後のUI納品観測2026-10-14T07:30:16ZはPID338403/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start60473641、元親/Tokenizer/10M/idle一致。現在保証ではなく、今回はprocess/HTTP/GPUを再診断していない。

元Base TEST20 promptと元Chat TEST20行は別のCPU解析問題を保存した。学習・GPU TEST採点に使っていないこととCPU未解析は別。将来の有資格最終確認にはreader分離と新しい封印TESTが必要。今回data/TESTを開封・再処理しない。

## 正本と保存場所

| 項目 | 保存場所・記録された構成 |
|---|---|
| Git正本 | Windows `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`。最新local HEADを確認し、remoteが同じとは仮定しない |
| WSL実行コピー | `/home/aihub_ubuntu/src/japanese-tiny-llm-10m` |
| 大容量データ | `/home/aihub_ubuntu/jmicro-data`。Linux diskで処理・学習 |
| 固定環境 | WSL package3.0.1 / Ubuntu WSL2 / RTX4090 / 記録時driver616.92 / Python3.12.7 / PyTorch2.14.1+cu130 / BF16。今回のruntime再測定ではない |
| Tokenizer | `artifacts/phase2/4096/tokenizer.model`、SHA `a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318` |
| nativeモデル | 10,001,152 parameters、既存9.5M〜10.1M内。`src/jmicro/model.py` SHA `298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83` |
| 最新結果保存 | [今回保存一覧](../reports/phase7/chat-lr-20261014/final_archive.json)と[納品確認](../reports/phase7/chat-lr-20261014/final_delivery_checks.json)。最新local commitは `git log -1` |

現在の環境変更は不要。Windows driverがWSL CUDAにも関係し、WSLへLinux display driverを追加しない。文書更新だけのときにdriver更新、uv依存変更、data再構築や全benchmarkを開始しない。

## 前回Chatの閉じたrunと当時のUI

`reports/phase7/chat-lr-20261014/` は全28セット・6,132内容判断・NLL7点×2,634 target、S1全3state/実入力教師列/予算/採否を監査し不採用で閉鎖。結果commit89275a8と納品commit09f338eを確認した。独立確認の7分岐は候補なしで未実行・品質未確認。

元10B [WebUI](http://127.0.0.1:7860)の保存された科学観測2026-10-13T16:54:20ZはPID309447/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start55170810、HTTP親SHA `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`、Tokenizer/10M一致、busy=false、kernel lock一致・競合なし。現在の生存保証ではない。文書更新では再起動・生成・GPU実験を行わない。

UI操作や明示実行再開時だけ、`reports/local/webui/server.json` と実PID/boot/start、HTTP、kernel lockを照合する。稼働中なら重複起動しない。必要時のWindows操作:

```powershell
Invoke-RestMethod http://127.0.0.1:7860/api/model
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/start_webui.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/stop_webui.ps1
```

[操作43](43_local_webui.md)。次の研究は新しい明示再開と別契約から始め、終了済みの元比較や拒否paddingを再起動しない。

## 前回Chatと旧BaseのGit外保全

最新S1は `reports/phase7/chat-lr-20261014/S1/checkpoint-00003646.pt`、SHA `f7e8bb8b1569cb45ac399108455a66c5922f64d7898e8ab6b4931ba13c856018`。t1/t2/t3のmodel/Adam/scheduler/RNG/sampler/counters、metrics/job/resultを同directoryに保持。TRAINは前回semanticのaccepted教材を参照し、新DEV/固定NLLはdata rootの `phase7/chat-lr-20261014/`。Gitには重みとdataset実体を含めない。以下の旧系列も保全する。所在は原記録から案内し全重み・全corpusを今回再hashしない。

| 場所 | 保全する内容 |
|---|---|
| `reports/phase7/chat-semantic-diversity-20261013/S1/` | 前回意味教材の全3state。最終SHA `6ca25064fa4ccb6784a05fa5ade43bfdaa87aeb55f11458a233eaf32664fd2ea` |
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

<a id="6-実装済みcliと次回の再開"></a>

## 明示的な実行再開後の順序

1. Windows最新local HEADとAGENTS/status/ロードマップ/本書/結果141を読む。Base復旧なら124、他の比較は別の新契約を参照する。
2. 再開範囲と10M維持を確認する。文書更新だけならdata/GPU/診断/評価へ進まない。閉じた128/131/133/135/139を復旧対象にしない。
3. 新しい実験を実行する場合だけ、実process・GPU lock・job/result・対照stateと保存hashを確認する。観測timeoutだけで終了と決めず、同じhandleを再確認する。
4. 新比較はTRAIN版/未使用DEV/全必要回帰・専用contract/runnerを先に完成し、欠けたCLI・技術gate・全評価予算を解消してから実行。Base復旧なら124の次条件選定から始める。
5. 成立した既存証拠を条件一致時に再利用する。長期jobはPID/boot/start、累積GPU台帳、全state、実消費・保存再開を必須にし、frozen sourceを保全する。
6. 新規比較の結果を保存して一度報告・停止。不採用を追加周回/seed選別/閾値緩和で救済しない。有資格時だけ独立学習seed43、人間blind、fullDEV、最終suite、封印TESTへ進む。候補なしなら未実行・品質未確認で止める。量子化は別の再開判断。

本当に未完了の新jobを復旧する場合だけ、同じ凍結条件と累積予算でvalid checkpointから再開する。Base復旧は証拠を満たしたBaseで通知・停止。通常Chat完成、公開、有料cloud、他者連絡へ自動移行しない。

旧引継ぎの全文は[今回の履歴保存一覧](../reports/investigation/documentation_plan_refresh_20261013/baseline.json)と[20261008履歴](windows_handoff_history_20261008.md)へ保全した。原source/report/raw・Phase0〜3を変更していない。

<!-- Original heading aliases retained for historical incoming links. -->
<a id="git外で保全する重みと教材"></a>
<a id="閉じた最新runとui"></a>
