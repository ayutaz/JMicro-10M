最新完了（2026-10-05 JST）: 契約73を段階4の品質未達/拡大非実行分岐まで完了、結果74。Adam引継ぎ/初期化各8Mはtrain64/64 gold＋EOS成功、別名dev127/128・128/128（同32scene）。規則でinherit選択。元同一10Bの従来/自然各25M教師・全日本語/160個別内容を完了。一貫性0→7、適切完結0→8、EOS10→26、反復48→30、BPB0.982188→0.983213。候補改善はあるが全品質基準未達、増量9192/追加100Mは未使用、不採用。科学66M/valid66,334,768/physical89,325,568、CUDA再開16更新215,168教師別、GPU484.284秒、CPU4tests・実学習/評価/完了監査成功。両job完了・不在、元UI actual379377/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start8917553とHTTP親SHA/tokens/busy確認。可搬natural_learning各JSON/原文gzipとLinuxrun保持。次案は名前置換ではない多様な完結文と同量各100M比較で未開始。結果72数値7失敗は保持。verified local commit後停止、追加準備/学習/20B/Chat/test/pushなし。以下の実行中記載は当時の履歴。

進捗（2026-10-05 JST）: 契約73の段階2完了、両Adam各8M教師でtrain64/64完全再現＋EOS。inherit別名dev127/128、fresh128/128（同じ32sceneなので一般汎化ではない）。規則でinherit選択、新規重みC不要。科学16M、検証215168別、GPU186.757秒、終端full resume/教師会計/有限値/原文評価監査成功。段階3 compare actual378856/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start8887284が元10Bから従来/自然各25Mを実行中。全160個別内容と日本語評価後、全既存gate合格時のみ段階4追加100M。元UI一時停止、終端復帰。重複起動しない。

実行中（2026-10-05 JST）: ユーザーの「4まで進めてください」で契約73を再開。自然64全文3426tokens、自然train1000全文52791tokens、条件付き増量9192全文501559tokens、未学習128を固定。32日常sceneの因果/対象/完結と64実原文をCodex確認、CPU4tests成功。A/B Adam引継ぎ/fresh各8M教師、必要時新規初期化C8M。記憶gate合格後に元10Bから従来/自然混合各25M、全日本語と160内容評価、全品質gate合格時のみ追加100M/増量。GPU各段階600/1200/1200秒、検証教師別。actual job-diagnostic/compare/expandを確認して重複起動しない。元UIを一時停止し各job終端で復帰。結果72の数値7失敗は保持。全範囲の結果/採否/local commit後停止、20B/Chat/test/pushなし。

最新完了（2026-10-05 JST）: 契約71の三項目＝計画70内部0〜2を実診断、結果72。32 train入力・三実重み・BF16生成384/FP32生成96・教材128全文確認。元10BのFP32 full/causal CE・gradient同一、cache/独立HF許容内。ただしpadding1要素/BF16 logitの計7checks失敗を保持。FP32でもoriginal/mixedの自然16件loop/停止未達が残る。mixedの条件16は全greedy/samplingでgold+EOS完全再現、既存story枝は短物語8/8EOSで展開改善。EOS無効化だけでは説明できず、自然文の教材適合/汎化/loop分布を優先。品質未解決、学習0/optimizer更新0。GPU63.439708秒、CPU4tests成功。raw bundle/summary/全文理由/完了証拠はreports/phase6/root_cause_*、Linuxrunはroot-cause-20261005。両job完了・不在、元UI actual374638/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start8753669、HTTP元SHA410f975d…/10,000,007,168/busy=false確認。verified local commit後に停止。自然短文64のAdam引継ぎ/fresh各8M比較は提案で未開始。追加学習/20B/Chat/test/pushなし。以下の実行中/計画のみの記載は履歴。

実行中（2026-10-05 JST）: ユーザーの三項目の再開範囲は契約71（計画70内部段階0〜2）。実装整合性、EOS/反復確率、教材適合性を診断する。32 train入力・128全文・三checkpoint SHAを凍結、CPU4tests成功。GPU占有上限600秒、学習/optimizer更新0。自然文記憶や次の学習比較は範囲外。元UIを一時停止し、診断終端で元10B UIへ戻して結果・local commit後に停止。reports/phase6/root-cause-20261005/job.json のactual PID/boot/start/logを確認し、重複起動しない。

最新計画（2026-10-05 JST）: docs/70_root_cause_investigation_plan.md、reports/phase6/root_cause_plan_research.json。read-onlyの証拠/source/一次文献調査と計画作成、追加学習/新GPU評価/data準備0。原checkpoint/Tokenizer/学習コード/旧reportsを保持。次に実行する案は計画70の段階0〜2（小sampleで実経路と生成確率を切り分ける）で未開始。計画のGPU上限/教師量は未測定の提案、実行前に別契約へ固定する。元UIを止めていない。下記の最新実学習69と保存先は不変。

最新完了（2026-10-05 JST）: [結果69](69_packing_learning_results.md)、契約68段階1〜3。三条件各25M body/EOS教師、選択shuffleとfixedの元10B Web80M＋短文20M各100M。五学習終端/五日本語評価/400raw-bound個別理由/旧dev参照/採否を保存、一般品質未達で候補不採用、元UIを復帰して停止。科学275M教師・valid277,092,898・physical311,066,624、検証625,842別。GPU占有1080.897秒。Windows可搬証拠はpacking_study各JSON/tests.xml、凍結開始e1d340bと最終verified local commitを引き継ぐ。自動pushなし。

Linux reports/phase6/packing-study-20261005 にjob/source/config/resume-gate/selection/五枝のoptimizer込み終端・metrics/条件train-dev全行/日本語raw/annotations/previous-dev/review/judgment/completionと評価参照名の修正証拠。五checkpointは fixed00305954、shuffle00305953、isolated00306976、mixed両00308245。元data condition-learning-20261005-v2/compact（再利用）、参照dev/train100コピーはpacking-study-20261005。大型fileはGit外で別途移す。完成runを再起動せず、後日の実identityを確認する。

元10B UIはactual370009/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start8580412、親SHA410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290・学習10,000,007,168tokens・busy=falseを完了監査で照合。科学367596/368468と旧dev評価は終了・不在。今後はserver.json＋/proc boot/start＋HTTPを再確認する。次の自然短文教材案は未開始。以下の旧記録は当時の履歴。
最新（2026-10-05 JST）: [結果67](67_condition_learning_diagnostic_results.md)が直近の実学習。固定小教材1000/拡張5000全文、準備55,273/280,724tokensから両24,969,216学習tokens、両update305938/10,024,976,384tokens。科学49,938,432・検証262,144別。train75/68・未見65/61で条件付き100M未開始。元packed文脈の正答100%対単独72/95・65/96で文脈依存を実測。両dev256/日本語診断/全160個別内容採点完了、不採用。元10B UI actual365612/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start7955441・HTTP親SHA/tokens/busy確認。verified local commitで停止。

Linux実行 reports/phase6/condition-learning-20261005 にjob/二終端checkpoint/metrics/resume/日本語raw/条件train-dev全行/全160annotations/review/probe/completion。教材 /home/aihub_ubuntu/jmicro-data/phase6/condition-learning-20261005-v2。これらの大型fileはGit外なので別途引き継ぐ。最初の未使用教材と失敗testsはpreparation-v1として保持。次回は実job/UI identityとfrozen configを確認し、終了runを再起動しない。以下の結果65と旧UI identityの記述は以前の引き継ぎ履歴。

# Windows/WSL引き継ぎ

最終更新: 2026-10-05 JST。最新完了は[結果65](65_condition_selector_v2_preparation_results.md)。別train32でselector v2を凍結、両20,000,072-token教材と未確認各40を用意したが弱例12/14で両内容gateが未達。準備失敗分岐の報告・採否・元UI確認まで完了して停止。新100M/全文は未起動。結果60/63と全旧証拠を保持。完成runを再起動しない。

## 現在の構成と確認先

| 項目 | 値・確認方法 |
|---|---|
| 正本 | Windows `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`。最新local commitを移し、remoteだけを最新と仮定しない |
| Linux実行コピー / data | `/home/aihub_ubuntu/src/japanese-tiny-llm-10m` / `/home/aihub_ubuntu/jmicro-data` |
| 既存実測環境 | WSL package3.0.1.0 / Ubuntu WSL2 / RTX4090 / Windows driver616.92 / uv Python3.12.7 / PyTorch2.14.1+cu130。新PCでは再確認する |
| モデル | 10,001,152 parameters。主系列/UIの学習量10,000,007,168tokens |
| 準備量 | Web12,225,819,077、短い物語200,000,192tokens |
| 最新科学比較 | 旧60M/新200M各追加1,000,013,824、各累積11,000,020,992tokens。科学2,000,027,648/検証262,144別 |
| 最新準備・判断 | 同source各20,000,072tokens/71,268全文、長さ/BOS/EOS一致、弱例12/40→14/40。候補改善と上限の両条件未達、学習なし。Base/Chat未達 |
| 完了証拠 | Windows condition_v2各JSON/全32開発と全80受け入れ、CPU5tests/101準備証拠/13終了checks。v2凍結3273e77と最新local commitを引き継ぐ |

## 現モデルのUIとprocess

[UI](http://127.0.0.1:7860)は元final10Bを配信。今回読み取り確認したactual PID359102 / boot`53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe` / start_ticks7216365、HTTP親SHA`410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`/training_tokens10,000,007,168/busy=false。科学PID239609は終了。後日の現在値はLinux `reports/local/webui/server.json`とactual identity/HTTPを照合し、保存PIDだけで判断しない。

Windows rootで`powershell -NoProfile -ExecutionPolicy Bypass -File scripts/start_webui.ps1`、停止は`scripts/stop_webui.ps1`。[操作43](43_local_webui.md)。稼働UIはGPU lockを保持する。今回の教材準備ではUIを停止せず、完了確認でactual identityとHTTPを照合した。

今回のLinux教材は `/home/aihub_ubuntu/jmicro-data/phase6/condition-v2-20261005/`、実行証拠は `reports/phase6/condition-v2-100m-20261005/`。両20M stream/index/manifest/sampleと凍結selector/builder、calibration/ready/jobを別途移す。既存200Mのsubsetで新取得量へ足さない。100mという名前は学習した証拠ではない。portable review/judgment/completionはGitに保存し、shardsは含めない。旧condition-preservation両20Mと全旧証拠も保持する。

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
