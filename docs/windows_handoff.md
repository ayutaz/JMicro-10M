# Windows/WSL引き継ぎ

最新・計画58段階1〜3完了・停止（2026-10-05 JST）: [結果60](60_dataset_expansion_results.md)。教材200,000,192tokens/新140,036,743、旧/新各追加1B、日本語192/331/1119・dev256・全160個別内容、一次35/最終20checks完了。常識は改善したがEOS34→25/一貫性15→9等で候補不採用、条件付き全文未開始。科学2,000,027,648/検証262,144別、GPU3129.607秒。actual239609は終了し、完成screenを追加学習として再起動しない。元UI actual359102/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks7216365/ready08:29:21.306388Z、HTTP親SHA410f975d…/tokens10,000,007,168/busy=false復帰確認。引継ぎはLinux `reports/phase6/dataset-expansion-1b-20261005/` の両終端・500M中間checkpoint/metrics/source/全評価raw/160annotations/review/judgment/completion/jobと、`~/jmicro-data/phase6/dataset-expansion-20261005/` の200M shards/manifest/ready/content-review/新source pin・README/receipt、旧60M source・元10B/既存run、Windows正本最新local commitを含む。Git/Hubだけでこのデータとweightsを復元できない。primary reviewは別v2でLR記録時点を厳密修正、凍結v1/科学source/品質gate不変。新source/長さ/EOS密度差・独立corpus監査/人手blind未完了を保持し、量だけの効果としない。新data/GPU/20B/50B/Chat/test/push/publicationは今回対象外。以下の実行中identityや旧停止は履歴。

最新・計画58段階1〜3実行中（2026-10-05 JST）: 教材200,000,192 tokens（旧59,963,449＋新公開TinyStories日本語訳140,036,743）準備、40全文レビューで弱例18開示、CPU5tests、config/schema/source凍結commit03346a7。平均長/EOS密度も変わるため量だけの比較ではない。hidden Windows21040/actual Linux239609/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6902884で旧/新各追加1Bを実行中。実CUDA保存再開25checks成功/検証262,144別、旧pool対照学習中。Linux `reports/phase6/dataset-expansion-1b-20261005/screen-job.json`・各枝metrics/latest/checkpointとWindows同run stdout/stderr/launchを追跡し、actual liveなら新起動しない。元UIはGPU中停止、wrapper finallyで元10Bへ復帰する。終了後、同じ日本語192/331/1119・dev256・全160内容と原採否条件、必要時だけ全文/400/長文、report/local commit/復帰確認まで必要。教材 `~/jmicro-data/phase6/dataset-expansion-20261005/` と新source pinned README/receipt/全raw、旧60M source・元10B/既存全runを移す。中断復旧コマンドは `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/run_dataset_expansion.ps1 -Mode screen`、actual process終端と有効checkpointを先に確認する。20B/50B/Chat/protected test/pushは対象外。以下の計画56停止は完了履歴。

計画56段階1〜3完了・停止（2026-10-05 JST）: matched教材各22,977,241tokens/253,119全文の各500M比較を完了。対照→追加選別はEOS39→44/反復16→17/一貫性11→11/適切完結14→15（各80）で不採用。段階2も省略せず旧59,963,449-token物語固定/一定LR0.0001で連続1Bを完了し、500M→1BはBPB0.982953243→0.981611241/EOS31→35/反復21→10/一貫性11→19/適切完結15→20。意味60.417→66.146%（対応95%+1.563〜+10.417pp）と複数指標は改善したが、一貫性95%下限0、EOS35<37、内容各27未達、Web BPB比+1.0335%で原採用条件未達。両条件付き全文は未開始。CPU10tests/実CUDA25・13/一次32・29/最終要求別31checks成功、全320内容保存。科学2,000,027,648/検証524,288別、一次GPU3331.359秒。元final10B UI actual237483/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6728695/ready07:08:04.599378Z、HTTP親SHA410f975d…/tokens10,000,007,168/busy=falseとactual process確認。科学234687/236557/教材234279は終了し再起動しない。結果と提案はdocs/57_matched_story_and_learning_budget_results.md、最終確認reports/phase6/matched_story_completion.json。11B checkpoint・両run全raw/metrics/source/annotationsをLinuxへ保存。追加学習の効果を否定せずBase/Chat未達、次の小規模条件保持教材診断/LR減衰/新data/GPU/20B/50B/Chat/protected test/pushは提案のみで未開始。local commitで今回停止し、以下は実行当時の履歴。


計画56段階1完了／段階2凍結: matched各22,977,241-token教材で各500,006,912追加tokens、実EOS教師Web846,893/story1,101,267を一致。GPU1659.584秒・科学1,000,013,824/検証262,144別。dev/日本語全完了・全160個別内容・CPU32evidencechecks成功。対照→候補BPB0.979944438→0.980233205、EOS39→44/反復16→17/一貫性11→11/適切完結14→15（各80）、対応95%−8.75〜+8.75ppで改善条件未達・不採用。条件付き全文は開始しない。次は旧採用59,963,449-token物語pool固定、元10Bから一定LR0.0001で追加連続1,000,013,824tokens、500M中間/1B終端を保存して両地点評価。段階1科学234687終了、元UI235943へ復帰確認済み。段階2config/schema/sourceを凍結したが新科学はまだ未開始。


計画56段階1〜3実行中（2026-10-05 JST）: 二組各22,977,241tokens/253,119全文、body平均88.7764（旧88.4621）、同じ長さ並び/BOS/EOS位置。CPU抽出11.146秒、random40各に弱例14/12を個別明記してbounded比較を受入。CPU10tests成功・凍結commit a8215aa。2026-10-05 06:09頃、hidden Windows34620/actual Linux234687/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6377461で教材二条件各500Mを開始。実CUDA25checks通過、対照学習中。Linux reports/phase6/matched-story-content-500m-20261005/screen-job.json と Windows同run screen.stdout.log/stderr.logを追跡。UIはGPU中停止/finally復帰。段階1未達でも段階2の固定教材・一定LR連続1B（500M中間/1B終端）は必要。全320内容と日本語評価・事前条件付き全文、判断/report/local commit/元UI復帰で停止。科学・一次結果は未確定、20B/Chat/test/pushは開始しない。


最新完了（2026-10-05 JST）: [計画54](54_complete_document_500m_execution.md)段階1〜4を[結果55](55_complete_document_500m_results.md)まで完了、新110M完結文500M条件は不採用、CPU一次22/最終51項目成功。条件付き全文は未開始。元final10B UI actual232991/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6169021/ready05:34:47Z、HTTP SHA410f975d…/tokens10,000,007,168/busy=false。科学232272/教材231819・231975は終了し再起動しない。Linux reports/phase6/complete-document-500m-20261005/のcheckpoint/metrics/source/全raw/80annotations/review/source-origin-diagnosis/judgment/completion/jobと、~/jmicro-data/phase6/complete-documents-20261005/のfirst4B job・継続job・110M shards/index/manifest/ready/random40/content-reviewを引継ぐ。Windowsのcomplete_document_*.json/実装/config/schema/最終report/local commitを保存して停止。次案は未実行で、新GPU/1B/20B/Chat/test/pushは自動開始しない。以下の旧現在地・identityは履歴。

最新完了（2026-10-05 JST）: [計画52段階1〜4](52_story20_low_lr_execution.md)の学習・評価・判断を完了し、[最終判断/次案53](53_story20_low_lr_judgment.md)・local commitで停止する。各500M/四地点一次/全320内容診断/条件付き全文・400・長文を実施、CPU37/全文30項目成功、候補は原比較条件を全通過した研究候補。品質目標は未達。科学174280/全文177987は完了・終了、旧runを再起動しない。元final10B UIがLinux231106 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4964393 / ready2026-10-05 02:14:01.602203Zで復帰し、actual processとHTTP SHA410f975d…/tokens10,000,007,168/busy=falseを確認した。引継ぎには100M run全raw、500M runの四checkpoint/全metrics/四地点raw/320annotations/primary reviewとfull全raw/source/job/result/review、`~/jmicro-data/phase6/simple-stories-ja-budget-20261005/`のsource/shards/content-reviewを含める。物語pool59,963,449 tokens/約1.667周使用。科学1,100,021,760/検証524,288別会計。次のデータ構成比較は提案のみで、今回未開始。要求別確認は`reports/phase6/story20_execution_completion.json`。以下の旧停止境界は履歴として保持する。

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
| 学習・比較 | 主要Web10B、100M配合/LR比較、計画52の20%低LR100Mと各500M・一次/全文/長文評価完了。500M枝各総10.5B、物語pool59.96M。Base/Chat品質は未達 |
| 次の行動 | 判断53・要求別確認・local commitを保存して停止。次の新pool/500Mデータ構成比較・各枝1B/20B/50B/Chatはユーザー再開まで開始しない |

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
