# Codex継続作業の現在地

計画49段階1のGPU比較を永続起動: 準備commit70304d6、14関連CPU tests成功、専用config/schema凍結。hidden Windows34152、actual Linux139467 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks1364277、開始2026-10-04 16:13:58Z。実CUDA保存再開後、物語10%の100M学習を実行中。run`reports/phase6/story10-10b-100m-20261005`、`screen-job.json`とWindows`screen.*.log`へ保存。GPU中のみUI停止、finallyで元final10Bへ戻す。80内容診断・採用判定→条件付き各500Mまたは低LR比較→最終判断/提案が残るためgoalはactive。actual processを確認し、同じjobを重複起動しない。

2026-10-05 JST・計画49段階1〜3を実行再開: ユーザー「3までを進めて判断をして提案をしてください」。[実行記録50](50_story10_and_budget_execution.md)へ条件を保存し、物語10%/100Mの専用runner・launcher・testsを準備中。既存25M poolと保存済みWeb/20%対照を再利用し、原gateは不変。採用条件を通る場合は各500M比較、未達なら一つの低LR同量比較→判断/提案/report/local commit・UI復帰で停止する。1B/20B/50B/Chat/test/pushは開始しない。現在科学GPU未開始、actual GPU processは既存UI49746のみ。過去完了runを再起動しない。

2026-10-05 JST・次回計画のみ: 前回結果を踏まえた[配合・学習量計画49](49_next_mixture_and_training_budget_plan.md)を作成。最初は同じfinal10B親・同じLRで新物語10%を100M学習し、保存済みWeb/20%結果と比較する提案。既存25M poolで足り、新source取得は不要。原採用条件を通る場合のみ、pool約60MとWeb/物語10%各500Mの同量比較を別予算で計画する。学習不足仮説と10B対20B案を残す。BPB悪化上限は緩めず、未採用20%枝を自動延長しない。今回は計画保存/local commitで停止、GPU学習/評価・新data取得/構築は未開始、既存UIを維持する。前回段階1〜3の完了commitは6d0ab0c。

2026-10-05 JST・段階1〜3完了: 限定data/EOS確認、SimpleStories-JA候補25,000,067 tokens、同じfinal10BからWeb/既存短文20%/新物語20%を各100,007,936 tokens学習し、一次240内容診断と事前条件付き全文/長文評価まで完了した。[最終報告48](48_complete_text_10b_comparison.md)、[全文/長文結果](../reports/phase6/complete_text_10b_full_result.json)、[要求別完了記録](../reports/phase6/complete_text_10b_comparison_completion.json)。一次35・全文43証拠checks、38関連tests・修復15 tests・実CUDA全state保存再開成功。新物語は固定EOS0→24/80、反復60→24/80、Codex一貫性2点0→10/80へ改善したが、全文BPB0.955765は元親0.954018より+0.001746で既存+0.001上限を超え、正式採用は見送る。理解改善の確証・独立人手品質合格・Base/Chat品質目標達成とはしない。GPU合計2,731.428秒、追加科学300,023,808 / 検証262,144 tokensは別会計。科学Linux17951、旧失敗19791、修復37818はいずれも終了。UIは元final10Bへ復帰しHTTP応答/busy=false、Linux49746 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks1043870を実確認。最終report/local commitで停止する。次の具体的行動は新しい依頼が来るまで追加学習を開始しないこと。500M/1B/20B/50B/Chat/test/pushは未開始。

以下は当時の進捗履歴。現行状態と停止境界は上記を正とする。

2026-10-05 JST: conditional読み込みを修復しr1を再開。初回Linux19791はWeb全文/400保存後の`read_json(str)`型エラーで終了、UI復帰を確認。旧job/source/config/rawを保持し、15CPU tests（Path回帰含む）成功。Web全文/400をhash・同条件・raw IDから確認して明示的に再利用、既消費GPU831.355秒を元3,000秒予算に含め、学習/評価仕様/gateを変更しない。新run`reports/phase6/complete-text-10b-100m-20261004/conditional-full-r1`、hidden Windows33788、Linux37818 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks930807のactual processを確認。現在Web長文中、Windows`full-r1.*.log`、終端job/resultが揃ってから`scripts/review_complete_text_full.py`を実行する。三条件学習/240内容診断は完了、goalは最終評価/report/commit/UI復帰が残るためactive。重複起動しない。

条件付き評価のWeb対照全文本文を完了: dev89,416文書 / 164,344,743 bytes、BPB0.948957324851、本文評価389.088秒。現在は同じ対照の固定400生成中、Linux19791は実在。新物語の全文/長文結果と最終CPU確認・報告・UI復帰が残るのでgoalは未完了。全240一次採点と各枝100Mは完了済みで再学習しない。保存result/長文を原IDから確認する`scripts/review_complete_text_full.py`を準備した。中断は同一conditional jobの保存済みstageを再利用し、completed primary job17951を再起動しない。

条件付き全文/長文評価を2026-10-04 14:43:42Zに永続起動した。hidden Windows34244、Linux19791 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks822481、actual process実在。Linux `reports/phase6/complete-text-10b-100m-20261004/conditional-full/job.json`、Windows`full.stdout.log`/`full.stderr.log`。現在Web全文本文を評価中、追加学習0、上限3,000秒。準備と一次比較結果はlocal commit7e3b6cdへ保存。終端を確認するまで重複起動しない。UIはこの評価中のみ停止しlauncher finallyで元final10Bへ復帰する。stage3は条件付き評価と完了報告/commitが残るため未完了。

一次比較完了・条件付き評価へ: 三条件GPU774.624秒で完了し、全240をCodex内容採点、35証拠checks成功。Web/既存短文/新物語のEOS0/3/24、反復60/55/24、raw失敗0、Codex一貫性2点0/1/10（各80）。新物語は適切完結9/80、関連性2点23/80で対照26/80より減少し、元品質目標未達。一次の事前gateを全て通ったため、新物語とWebのみ原全文dev/400と20prefix128/512へ進む。専用conditional runner/config/schemaと14CPU testsを準備した。追加学習0、予算3,000秒。GPU科学process17951は終了、UIは元final10BでHTTP応答確認済み。次は条件付き評価の実行→結果確認→report/local commit・UI復帰で停止する。

三条件の科学学習は各100,007,936 tokensを完了し、各枝総10,100,015,104 tokens/update308228の終端checkpointを保存した。学習時間はWeb159.169秒、既存短文148.389秒、新物語148.383秒。Linux17951は実在し、最後の新物語条件の一次評価中。WebのEOS0/反復60/文字破損0、既存短文のEOS3/反復55/文字破損0（各固定80、全文評価ではない）。新物語結果は未確定。終了後に240出力内容診断とCPU証拠確認、UI復帰・report/local commitで停止する。

段階3のGPU比較を2026-10-04 14:23:05Zに起動した。hidden Windows28068、Linux17951 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks698774。actual processを確認済み、現在は実CUDA保存再開gate中。runは`reports/phase6/complete-text-10b-100m-20261004`、Windowsログ`gpu.stdout.log`/`gpu.stderr.log`、Linux`job.json`と各枝checkpoint/metricsへ永続化。準備commit05b450d、UIを一時停止しlauncher finallyで復帰する。重複起動せず、このprocessを追跡する。比較後に内容240件を診断・証拠を確認し、report/local commitで停止する。

段階2完了・三条件GPU比較の起動準備: 新公開物語pool25,000,067 tokens / 276,369全文 / 108,582親familyを82.876秒で構築し、100例をCodex確認。合成語・弱い展開・未解決末尾などの残る例を[標本記録](../reports/phase6/complete_text_data_review.json)へ明記した。全例意味保証や独立人手認定ではなく、元gateを保持した実験用候補として採用。両Web候補は未採用のまま保存。38関連CPU tests成功、同じfinal10Bから各100,007,936 tokensのconfig/schemaを凍結。GPU科学学習はまだ未開始、既存UI482のみ実在。次はUIを一時停止し、実CUDA保存再開→三条件の学習/一次評価→内容240件採点→報告/local commitで停止する。

段階2の内容確認により学習前に方針を修正: Web r2も30,235,206 tokensまで232.351秒で準備したが、無作為100例に意味の崩れ・前文依存が残り未採用。初回とr2は保存。公開SimpleStories-JAの作者MIT表記・revision `d25370316dd77ec0ee4fd9db57bfe57075cf4b90`・train parquet hash/サイズを固定し、必要な25M tokensの物語全文を準備中（hidden Windows33712、`prepare-stories.*.log`）。Cは2〜8文/32〜128tokensとなり、旧短文との長さ一致は学習前に撤回してsource/長さ/EOS密度を含む配合全体の比較と明示した。[改訂条件48](48_complete_text_10b_comparison.md)。原モデル/学習量/LR/gateは不変、関連38 CPU tests成功。現在もGPU科学学習は未開始、UI維持。

段階1を完了し、[実行記録48](48_complete_text_10b_comparison.md)へ保存。Web/既存短文各100の限定抽出、EOS/BOS/shift四条件成功、本文special混入0、句読点末尾63/100と100/100。句読点だけでは前文依存・意味の崩れを除けない。初回候補30,230,920 tokensを215.570秒で構築したが、無作為100例の前文依存・説明予告を確認して学習前に選別を修正。旧候補は保持し、r2をWSL12CPU workersで構築中（Linux17005、hidden Windows33952、ログ`reports/phase6/complete-text-10b-100m-20261004/prepare-r2.*.log`）。新しい選別・分岐と既存EOS/尤度/契約/評価メモリの関連36 CPU tests成功。科学GPU学習はまだ未開始、UI継続。次は修正poolの100例確認→凍結→UI停止→新poolの実CUDA保存再開と三条件各100M。

実行再開（ユーザー「3まで進めてください」）: 計画の段階1〜3、限定data/EOS確認→25M〜50M完結文pool→同じfinal10BからWeb/既存短文20%/新完結文20%各100Mの実学習と比較を開始する。以前の計画のみの停止境界はこの範囲で更新。まず実装・既存train/poolと実processを確認中。現在UIのLinuxPID482は実在し、GPU学習processなし、Linux空き526GiB。GPU開始時のみUI停止・完了時復帰。段階4の500M〜1B、20B/50B、Chat、公開は開始せず、三条件の評価・報告・local commitで停止する。

計画補足（2026-10-04、質問「学習量が足りない可能性」）: **学習量不足は未棄却で、収束を証明していない。** [計画47](47_post_evaluation_training_plan.md)へ、各100Mは配合screenであり総10Bに対して約1%に留まること、安全なA/Cを同量500M〜1Bまで比較する別段階案と、Web10B対20Bの直接比較案を追記した。100Mで内容が改善しないことを増量無効の証明にしない。旧品質gateは保持し、延長は別予算・終了点を先に凍結する提案。今回もGPU/data作業は未開始、UIを維持し、計画補足のlocal commitで停止する。

最新依頼（2026-10-04）は追加評価に基づく次回計画と「データセット量を増やすべきか」の判断。[データ・学習改善計画](47_post_evaluation_training_plan.md)を保存した。推奨は意味の通る完結文poolをまず25M〜50M tokens準備し、同じfinal10B親からWeb100%/既存短文20%/新完結文20%を各100Mで比較する案。EOSだけでなく生成一貫性・適切な完結・反復・条件保持を測り、有望ならpool100M以上と追加500Mへ段階拡張する。新規source量と既存dataの再選別・学習tokensを分ける。元gateは保持し、数値・予算は次回凍結する提案。**今回は計画のみで、新data取得/構築・GPU推論/学習・suite変更は未開始。UIは維持し、local commitで停止する。**

最新の評価追加依頼（2026-10-04、棚卸し後の実装再開）を完了した。[実施計画](45_japanese_base_evaluation_v2.md)、[結果と制限](46_japanese_base_evaluation_v2_results.md)、[15 evidence checksの集計](../reports/phase6/japanese_base_v2_review.json)、[終了・UI復帰記録](../reports/phase6/japanese_base_v2_completion.json)。新しいnative scorer/実行入口・8 CPU testsを追加し、既存契約/評価メモリと合わせた21 tests成功。WSL/RTX4090で現在の10M/総10Bモデルを実測した。JBLiMP sample SLOR74.62%、JCommonsenseQA30.38%、独自意味dev59.38%。意味の両文脈正答23/96＝23.96%でrandom期待25%を超える証拠はない。JNLI/JCoLAはlabel prior・多数派対照を含めると判別力が弱く、Base品質合格にはしない。

保存済み80×2の全160をCodexで文法/関連性/一貫性各0/1/2採点。10Bは文法2点38/80、関連性2点25/80、一貫性2点0/80。独立人手blindは未実施で、元70%人手目標へ代入しない。追加greedy128/512は各20件で自然EOS0、char4-gram反復83.26%/95.76%。元の自然EOS9件の適切な内容完結はCodex診断1/9。JSQuAD事前固定dev100は独自EM0%、文字F1 12.69%、外部Wikipedia100本文51,362 bytesのBPB1.335143。詳細は結果文書を正とする。

GPU初回pilot7.505秒、本評価320.820秒、語彙family重複を直した意味診断192件のみのrevision1.686秒で完了。元のraw/source/configを保持し、cluster CIの問題重みとJNLI image groupingは保存値からCPU修正した。追加学習0、公式test未取得/未採点、旧v1/学習コード/重み不変。rawとsourceはLinux `reports/phase6/japanese-base-v2-20261004/{pilot,full,cpu}`、修正版意味診断は`reports/phase6/japanese-base-v2-20261004-r1/pilot`。評価jobは終了し、Web UIを http://127.0.0.1:7860 へ復帰した（LinuxPID482 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks275771、ready13:12Z）。終了記録を確認し、完了GPU runを再起動しない。**今回はlocal commitで停止する。追加学習・test・参照重み・JMMLUは開始しない。**

以下は直前の棚卸し・実行履歴。現行の評価追加状況は上記を正とする。

最新依頼（2026-10-04）は日本語Base評価の追加に向けた「まず現行評価と改善部分を洗い出す」。**コード・固定suite・保存結果の棚卸しと公開日本語評価の調査を完了し、[評価改善案](44_japanese_base_evaluation_audit.md)へまとめた。** [CPU inventory](../reports/phase6/base_eval_inventory_20261004.json): dev80のchecksは全件共通の説明文、保存400のhuman_scoresは全null、400出力は80入力×5条件。BPB/EOS/raw flagsは測定済みでも、文法・関連性・一貫性の定量採点と公開日本語benchmark成績は未実施。

P0は既存結果から内容採点/category/反復/CIを追加し、否定・数量・時刻等の基本意味診断を設計する。P1はJBLiMP（原論文SLORと独自尤度診断を区別）・JCommonsenseQA・JNLI・domain別本文予測。次はv2の取得version/template/score/split/予算と新規基準を凍結し、Base向け候補尤度scorerを実装する案。今回は実装・GPU新評価・追加学習・参照重み取得・test採点を開始していない。旧protocol/gate/checkpoints/結果は不変。Web UIは維持する。

直前の追加依頼（2026-10-04）は「現モデルを試すローカルWeb UIの作成・起動」。**実装・実モデルAPI・Edgeブラウザの生成/停止確認を完了し、WSL/RTX4090の推論サーバーを http://127.0.0.1:7860 で稼働したまま引き渡す。** 起動/停止は `scripts/start_webui.ps1` / `scripts/stop_webui.ps1`。[操作説明](43_local_webui.md)、[確認記録](../reports/phase6/local_webui_review.json)。追加学習0、既存checkpoint/評価結果は保持。後続のEOS/Chat/20B実験の停止境界は維持する。

Web UI稼働中は `~/jmicro-data/gpu.lock` を保持する。次のGPU jobを開始する前はUIを停止し、WSL `reports/local/webui/server.json` のactual PID/boot/start ticksを確認する。Windows側launcher/process/logは `reports/local/webui/`。GPU推論はBF16/math attention＋KV cache。関連11 CPU tests、実モデルseed再現、旧greedy64 ID一致、切断後のlock解放/再生成、ブラウザdesktop/mobile生成と停止を確認済み。

最終更新: 2026-10-04。**ユーザーが再開したstep3「10bの品質評価」を完了した。** 同条件の全文dev89,416文書・固定400生成、旧5B/最良Web5.1B比較、全固定80と自然停止9件の内容確認、CPU証拠確認23項目を完了。BPB0.954018 / 固定EOS0・反復53 / raw Unicode0。元増量gateは合格、Base/Chat品質目標は未達。report/local commitで停止する。[品質結果](42_base_10b_quality_evaluation.md)、[本学習の結果と速度](41_base_10b_training.md)。

専用 `scripts/compare_base_10b.py` / `.sh` と凍結 `configs/phase6/base_10b_comparison.json` を用意し、関連23 CPU tests成功。初回は過去EOS設定5件のschema欠落で既存契約tests2件が失敗したため、元configを変更せず厳密const schemaを追加して修復した。[修復記録](../reports/phase6/base_10b_comparison_schema_repair.json)。GPU空きと既存job終了を確認済み。評価GPU上限1,800秒。旧結果・学習source/checkpointsを保持し、追加学習や後続実験は開始しない。

評価jobは2026-10-04 11:56Z開始、12:09Zにcomplete。LinuxPID442 / boot0f175ee3-e772-41f7-8f7a-76387be1f2e4 / start_ticks14858、hidden WindowsPID31900は実process終了を確認済み。[起動記録](../reports/phase6/base_10b_comparison_launch.json)、[完了記録](../reports/phase6/base_10b_comparison_completion.json)。GPU時間786.881秒（全文376.052秒・生成409.008秒）、上限1,800秒以内。Linux `reports/phase6/base-10b-comparison-20261004/` にjob/log/文書別NLL/400生成/result/比較packet/sourceを保持する。完了済みの評価・旧学習launcherを再起動しない。

完了CPU reviewer `scripts/review_base_10b_comparison.py` を実際の保存結果と内容診断へ適用し、23項目成功。生成IDから全raw flags、全文BPB、元安全gate、旧reference hash、評価隔離、実process終了を確認した。[review](../reports/phase6/base_10b_comparison_review.json)、[全80と自然停止の内容診断](../reports/phase6/base_10b_content_review.json)。追加学習tokens0、旧結果はGPU再評価せず再利用。独立人手blind/test/Chat/量子化は未実施。

[現在の計画](39_learning_scale_and_generation_plan.md)、[10B準備結果](40_base_10b_preparation.md)、[原ロードマップと品質条件](15_project_roadmap.md)、[引き継ぎ](windows_handoff.md)。過去の実行中メモ・停止境界・7.5B案は[2026-10-04までの履歴](autonomous_history_20261004.md)へ移した。旧メモのPIDやコマンドを現在の起動指示にしない。

## 実際に完了したこと

| 対象 | 実状態と証拠 |
|---|---|
| モデル | T4K / NoQK-Norm / 10,001,152 parameters。規模は10Mのまま |
| データ | train12,225,819,077 tokens整備済み。[受け入れ記録](../reports/phase6/corpus_10b_ready_review.json)。構築時確認・raw再構築・実loader成功、独立全件auditはユーザー指定で未完了 |
| 主系列学習 | 総5,000,003,584 input tokens。[学習確認](../reports/phase6/base_5b_review.json)、[全文と生成比較](36_base_5b_comparison.md) |
| 仕上げ比較 | 同じ5B親からWeb/短文20%を各100,007,936 tokens、各累積5,100,011,520。別モデルの消費を合算しない。[結果](38_eos_5b_finish_results.md) |
| UTF8表示 | 共通helper実装済み。上限の未完成末尾だけを表示から保留し、raw失敗と停止理由は保持 |
| 10B準備 | 専用config/schema/launcher凍結。14tests、実CUDA16updates/524,288検証tokensの全state/history一致、保存証拠26項目成功。[準備確認](../reports/phase6/base_10b_preparation_review.json) |
| 10B本学習 | stable9,500,000,256＋decay500,006,912＝総10,000,007,168 tokens。追加科学5,249,990,656 tokens。[保存状態19checks成功](../reports/phase6/base_10b_training_review.json) |
| 10B品質評価 | 同条件dev/400・全固定80と自然停止9件の内容確認、CPU証拠確認23項目成功。[品質結果](42_base_10b_quality_evaluation.md) |
| 品質と後続 | Base/Chat品質未達。独立人手blind採点・test・Chat学習・新重みの量子化品質は未実施 |

## 現在の評価結果

同じ保護dev89,416文書/164,344,743本文bytesのBPB、固定dev80のgreedy64-token上限。BPBは小さいほど良い。

| モデル | 全文BPB | 固定自然EOS | 固定反復 | 全400 raw Unicode失敗 |
|---|---:|---:|---:|---:|
| 元2B | 0.982882 | 0/80 | 60/80 | 0/400 |
| 元5B | 0.964484 | 0/80 | 59/80 | 2/400 |
| Web仕上げ5.1B | 0.958092 | 0/80 | 57/80 | 0/400 |
| 短文仕上げ5.1B | 0.959011 | 13/80 | 51/80 | 2/400 |
| 新10B | 0.954018 | 0/80 | 53/80 | 0/400 |

短文の全400自然EOS129/反復103、Web13/121。短文の全文BPB悪化は対照比+0.095894%で許容内だが、raw Unicode2により最終採用gate不合格。1件は途中不正UTF8、1件はcap末尾切断。短文重みは診断用として保持する。Webの増量数値gateは合格、両モデルとも意味・数量・時刻・否定条件の誤りが残る。自然停止増加を正答率・実用品質の達成にしない。2B→5BにはLR曲線差もあり、全差を学習量だけの因果効果とは断定しない。

## 保存先と実行状態

コード/Git正本はWindows `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`、Linux実行コピーは `/home/aihub_ubuntu/src/japanese-tiny-llm-10m`。大容量データは `/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards`。固定Tokenizerは `artifacts/phase2/4096/tokenizer.model`。Pythonはuv管理3.12.7、WSL2/RTX4090/Torch2.14.1+cu130。

主要checkpointはLinux repo相対で次に保存されている。hashの正本は凍結configと各review。

- 長期継続用stable4.75B: `reports/phase6/base-5b-20261004/stable/checkpoint-00144959.pt`、SHA `916c4105ba7ab62597334a059cd34839d675fde29bb82b6fca6d30f889df6be5`。
- final5B: `reports/phase6/base-5b-20261004/decay/checkpoint-00152588.pt`。
- Web/短文5.1B: `reports/phase6/eos-5b-finish-100m-20261004/{web,short20}/checkpoint-00155640.pt`。
- 10B準備: `reports/phase6/base-10b-20261004/` のpreparation-job/preparation/cuda-resume-gate/environment/source/logとverification checkpoints。

10B準備jobはcomplete、検証GPU時間19.217秒。旧Linux459/Windows29620は終了履歴。科学jobは2026-10-04 09:36Z起動、11:43:52Zにcomplete。Windows30148、Linux427（boot86a59ddc-4594-4dfb-81df-a4f1439c52b0/start_ticks3212）は実process終了を確認済み。[launcher記録](../reports/phase6/base_10b_launch.json)は起動時の履歴、[完了記録](../reports/phase6/base_10b_training_completion.json)が現在の終端状態。runのjob/result/metrics/log/sourceと科学checkpoint163個を保持した。pushはしない。

新10Bの継続用stableは `reports/phase6/base-10b-20261004/stable/checkpoint-00289917.pt`、評価用finalは `reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt`。[実hashと容量](41_base_10b_training.md)を参照。両終端のmodel/Adam/scheduler/RNG/sampler/digest/counterと全科学metricsをCPUで確認した。

高速化はFlash＋compile reduce-overhead・BF16・fused AdamW・batch32で対応済み。今回の定常速度はstable695,339 / decay694,288 tokens/s。準備を含むGPU lock時間7,657.678秒（約2時間8分）で上限9,000秒以内。以前の最速reference比5.436倍、最大VRAMのbatch111はbatch32より遅く、data waitは既存測定0.55%。追加速度実験は未実施。

## 次に行うことと終了点

直前チャットの番号に揃える。前回step2の学習・保存確認は完了し、commit1344b4eで停止した。今回ユーザーはstep3の品質評価を再開した。評価・内容確認・報告とcommitで停止する。

1. **実行設定準備: 完了。** 専用設定と保存再開確認を再実行する必要はない。
2. **本学習と保存確認: 完了。** 保存stable4.75Bから9.5B stable＋15,259-update decayで総10,000,007,168/update305176へ到達。追加科学5,249,990,656 tokens、7.5B中間実験・追加収集なし。専用CPU reviewer19項目成功。
3. **同じ評価と内容比較: 完了。** 新10Bだけ全文dev/400を測り、旧5B/最良Web5.1Bを再利用した。全文BPBはWeb比−0.425169%、固定反復57→53、raw Unicode0。固定EOS0のまま、数量・時刻・否定・因果誤りと局所退行が残る。元増量gateは合格し、次の仕上げ候補として保持する。実用品質達成とはしない。
4. **報告・local commit・停止。** 原raw品質条件を保持し、改善と残る課題を明示する。EOS仕上げ/UTF8制約は別の後続候補で、現在未起動。

以下は中断復旧用のWSL repo内コマンド履歴。今回のrunは完了しているため再起動しない:

```bash
bash scripts/run_base_10b.sh --train
```

将来別のrunを起動する前はactual PID/boot/start ticksとGPU lockを確認する。科学学習GPU上限9,000秒、評価上限1,800秒はともに予算内で完了。次の具体的な候補は、ユーザーがEOS仕上げを再開した場合に保存final10B親の単一Web/短文20%各100M比較を整えること。元raw採用gateを保持し、20B/50B/Chat/UL/sweepへ自動移行しない。

## 前回の文書整理の検証（起動前の履歴）

[文書更新記録](../reports/phase6/documentation_refresh_20261004.json)に元13文書の完全保存、270内部リンク、凍結10B設定・学習source/lockの不変性、Windows/WSLの現行文書一致、科学run未開始を記録した。過去のreport6件はWindows正本に存在し、Linuxコピーに不足することも記録する。移行時はGit管理reportと大型raw evidenceの両方を引き継ぐ。文書整理当時はGPU学習・評価を実行せず、local commitで停止した。その後ユーザーがstep2を再開した。
