# Codex継続作業の現在地

計画58段階2・新教材500M中間保存（2026-10-05 JST）: actual239609が新200M条件の追加500,006,912/総10,500,014,080/update320435を732.937秒で保存（2026-10-05T08:14:11.748544Z、SHA4e98847ed502ba86afeb137a9254558ed1f9446aa58d437139efb1b74a7ccd19を実ファイルと照合）。Web400,031,744/short99,975,168を対照と一致、EOS教師Web846,893/short578,635で短文EOS数は旧1,105,092の約52.36%。新sourceと長さ差の影響をそのまま保持する。実PID38分経過・stderr空で1Bへ継続中。対照1Bは完成、旧1B全30,518更新の実使用LRと保存後LRはv2 CPU照合で成功。新終端・両終端評価/160内容・採否・必要時全文・report/local commit/元UI復帰が残る。

計画58段階2・対照1B完了／新教材学習中（2026-10-05 JST）: actual239609が対照追加1,000,013,824/総11,000,020,992/update335694を1479.136秒で保存（2026-10-05T08:01:57.826188Z、SHA fd10dc1b358327bdbd8d3d58118c2cb096fc53d02b036f070e453911edf2b82aを実ファイルと照合）。Web800,063,488/short199,950,336、EOS教師Web1,693,843/short2,210,250。元final10Bから新200M条件へ同一jobで移り、actualPID稼働・stderr空を確認。metric.lrは使用した率、saved scheduler/optimizer.lrは次更新の率であり、旧CPU reviewerの照合に1更新ずれを発見。凍結した旧source/config/学習は変えず、別reviewer v2で使用率(step−1)と保存後率(step)を厳密照合し、実CPU scheduler境界と誤率拒否の2tests成功。品質gateは不変。新条件1B・両終端日本語/160内容・原gate判断・必要時全文/report/local commit/元UI復帰は未完了。

計画58段階2・対照500M中間保存（2026-10-05 JST）: actual239609が500,006,912追加/総10,500,014,080/update320435を745.994秒で保存。`control/checkpoint-00320435.pt` SHA c5658fc5891f30ebb007e58427d1453fcf9cb47687222411ae8078a0ff1344f3を実ファイルと照合成功。Web400,031,744/short99,975,168、EOS教師Web846,893/short1,105,092。07:50:05Z時点で15700更新へ続行、実psで同一PID/13分経過を確認しstderr空。科学ジョブは止めていない。段階3未完了、対照1B→新200M教材1B→両終端の日本語/全160内容・採否と条件付き全文、report/local commit/元UI復帰まで追跡する。観測用functionsセル2370は終了したがGPUジョブとは別プロセス。

計画58段階2開始（2026-10-05 JST）: 凍結commit03346a7。hidden Windows21040からwrapperを起動、actual Linux239609/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6902884を実psで確認。元UI停止、科学は新poolによる実CUDA保存再開を開始したところ。Linux reports/phase6/dataset-expansion-1b-20261005/screen-job.jsonとWindows同run stdout/stderr/launchを追跡し、再起動しない。旧60M/新200M各追加1Bの終端、日本語全診断・全160内容と採否、report/local commit/元UI復帰が未完了。

計画58段階1完了・段階2凍結（2026-10-05 JST）: 新pool200,000,192tokens/1,161,923全文（旧59,963,449＋新TinyStories日本語訳140,036,743）。元sourceの選別緩和やコピー増量ではなく、別公開trainを追加。準備145.021秒/1800秒、40全文の個別診断で弱例18を開示、CPU5tests成功。平均長88.462→170.129/EOS密度11.054→5.810で量だけの比較ではないとGPU前に具体化した。docs/59_dataset_expansion_execution.md・新config/schema/runner/reviewerを凍結。次は実CUDA stable/decay保存再開→旧/新各追加1B（同じ20%/stable29000・decay1518）→全日本語・160内容/原gate判断・必要時全文→report/local commit/元UI復帰で停止。科学はまだ未開始。Linux教材builder238695終了、元UI237483を保持。

計画58段階1〜3を再開（2026-10-05 JST）: ユーザーが「3まで進めてください」を指示。200M教材供給の実確認・必要分準備→旧/新各追加1Bの同条件学習→日本語/全160内容と原条件の採否判断、report/local commit/元UI復帰で停止する。actual process確認で科学学習なし、元UI237483稼働、WSL空き490GiB。新TinyStories日本語訳と合成教科書の公開train供給をpinして確認する。旧source現条件60M枯渇を避けるためだけのコピー・選別緩和はしない。新sourceの実量/長さ/EOS密度が変わる場合は開始前に比較条件を具体化して開示する。科学未開始、20B/Chat/protected test/pushは対象外。

教材増量の次回比較案（2026-10-05 JST）: ユーザーのデータセット増量提案を受け、既存Web12,225,819,077/物語59,963,449 tokensと供給枯渇の記録を確認。docs/58_dataset_expansion_proposal.mdに短い完結教材200M目標・旧60Mとの各追加1B/同じ20%配合/共通減衰比較を具体化した。別source・長さ・EOS密度が変われば量だけの効果とはしない。新200M供給の成立は未確認、取得・構築・GPUは未開始。結果57・原採用基準と完了ジョブは保持する。今回行った作業は次回案の保存のみで、計画56完了の停止状態と元10B UIを変更していない。次の具体作業案は未使用train供給を1,800秒以内で調査し、目標量・長さ/EOS密度・内容の成立を凍結すること。

計画56段階1〜3完了・停止（2026-10-05 JST）: matched教材各22,977,241tokens/253,119全文の各500M比較を完了。対照→追加選別はEOS39→44/反復16→17/一貫性11→11/適切完結14→15（各80）で不採用。段階2も省略せず旧59,963,449-token物語固定/一定LR0.0001で連続1Bを完了し、500M→1BはBPB0.982953243→0.981611241/EOS31→35/反復21→10/一貫性11→19/適切完結15→20。意味60.417→66.146%（対応95%+1.563〜+10.417pp）と複数指標は改善したが、一貫性95%下限0、EOS35<37、内容各27未達、Web BPB比+1.0335%で原採用条件未達。両条件付き全文は未開始。CPU10tests/実CUDA25・13/一次32・29/最終要求別31checks成功、全320内容保存。科学2,000,027,648/検証524,288別、一次GPU3331.359秒。元final10B UI actual237483/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6728695/ready07:08:04.599378Z、HTTP親SHA410f975d…/tokens10,000,007,168/busy=falseとactual process確認。科学234687/236557/教材234279は終了し再起動しない。結果と提案はdocs/57_matched_story_and_learning_budget_results.md、最終確認reports/phase6/matched_story_completion.json。11B checkpoint・両run全raw/metrics/source/annotationsをLinuxへ保存。追加学習の効果を否定せずBase/Chat未達、次の小規模条件保持教材診断/LR減衰/新data/GPU/20B/50B/Chat/protected test/pushは提案のみで未開始。local commitで今回停止し、以下は実行当時の履歴。


計画56段階2・500M中間保存／連続1B学習中: actual236557が500,006,912追加/総10,500,014,080/update320435を746.529秒で中間保存（SHA 17cb40a158c51a52e93ff31ba492067fff9c9cbebaa784da167fe036da60aad0）。Web400031744/story99975168、EOS教師Web846893/story1105092、一定LR0.0001。評価を挟まず同じ学習を1Bまで続行中。500Mを新たな科学枝として重複計上しない。新一定LRの実CUDA13checks成功/検証262,144別。1B終端/両地点日本語・160内容/最終判断は未完了。


計画56段階2実行中: hidden Windows34216/actual Linux236557/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6560977。旧59,963,449-token物語を固定、一定LR0.0001/30518更新/科学1,000,013,824tokens、500M中間と1B終端を保存し1B後に両地点評価する。新一定LRの実CUDA保存再開を実行中、科学は未完了。Linux reports/phase6/story-constant-lr-1b-20261005/screen-job.json・fixed20/metrics.jsonl/latest.json と Windows同runログを追跡。段階1科学234687終了・32evidencechecks成功/内容改善未達、commit04acf40。段階2全160内容/必要時全文/最終判断/report/commit/UI復帰まで進め停止する。


計画56段階1完了／段階2凍結: matched各22,977,241-token教材で各500,006,912追加tokens、実EOS教師Web846,893/story1,101,267を一致。GPU1659.584秒・科学1,000,013,824/検証262,144別。dev/日本語全完了・全160個別内容・CPU32evidencechecks成功。対照→候補BPB0.979944438→0.980233205、EOS39→44/反復16→17/一貫性11→11/適切完結14→15（各80）、対応95%−8.75〜+8.75ppで改善条件未達・不採用。条件付き全文は開始しない。次は旧採用59,963,449-token物語pool固定、元10Bから一定LR0.0001で追加連続1,000,013,824tokens、500M中間/1B終端を保存して両地点評価。段階1科学234687終了、元UI235943へ復帰確認済み。段階2config/schema/sourceを凍結したが新科学はまだ未開始。


計画56段階1・対照500M学習完了／候補学習中: actual234687が対照500,006,912追加tokens/総10,500,014,080/update320435を745.075秒で終端保存（SHA d6d3009c23870ffcefba93afade16107840cc4eaa2d4a836f1960384b1dc0971）。Web400031744/story99975168、EOS教師Web846893/story1101267。同じ元final10Bから候補500Mへ移った。一次評価/全160内容/条件付き全文/段階2固定1B/最終判断は未完了。同じ実行を追跡し重複起動しない。


計画56段階1〜3実行中（2026-10-05 JST）: 二組各22,977,241tokens/253,119全文、body平均88.7764（旧88.4621）、同じ長さ並び/BOS/EOS位置。CPU抽出11.146秒、random40各に弱例14/12を個別明記してbounded比較を受入。CPU10tests成功・凍結commit a8215aa。2026-10-05 06:09頃、hidden Windows34620/actual Linux234687/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6377461で教材二条件各500Mを開始。実CUDA25checks通過、対照学習中。Linux reports/phase6/matched-story-content-500m-20261005/screen-job.json と Windows同run screen.stdout.log/stderr.logを追跡。UIはGPU中停止/finally復帰。段階1未達でも段階2の固定教材・一定LR連続1B（500M中間/1B終端）は必要。全320内容と日本語評価・事前条件付き全文、判断/report/local commit/元UI復帰で停止。科学・一次結果は未確定、20B/Chat/test/pushは開始しない。


新計画56段階1〜3をユーザーが再開許可: 量/長さ/EOS数を一致させた物語教材二組各500M→選択教材で一定LR連続1Bの500M/1B比較→日本語/内容診断と判断/report/commit/UI復帰で停止。教材候補未達でも学習量比較を省略せず旧採用poolを使う。1Bは今回範囲、20B/Chat/test/pushは開始しない。既存GPUjobなし・元UI232991のみ。実装/教材準備中、科学GPU未開始。

2026-10-05 JST・新計画54段階1〜4完了: train全文pool110,000,202 tokens（物語30M/Web80M）、一様ランダム40全文の弱例8を明記して受入、12CPUtests/実CUDA25save-resume/一次CPU22/最終要求別51項目成功。同じ元10Bから一条件500,006,912科学tokens（検証262,144別）、学習745.510秒・一次GPU853.678秒。BPB0.972888865/EOS17/反復31/一貫性9/適切完結8（各80）、日本語192/331/1119全完了・全80個別Codex診断。保存物語500MのEOS37/反復18/一貫性・完結19から悪化し、新改善条件未達で不採用、条件付き全文/400/長文は未開始。物語実比率20%→5.4531%、short EOS教師約111万→約61万で、増量だけの効果ではない。データ量・学習量不足を否定せず、次案は実物語比率/長さ/EOS密度を揃えた内容比較として報告55に保存（未実行）。科学232272/教材231819・231975は終了。元final10B UI actual232991/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6169021、HTTP親SHA410f975d…/tokens10,000,007,168/busy=falseとactual processを確認。報告/判断/要求別確認/local commitで停止。Base/Chat品質未達、1B/20B/50B/Chat/protected test/push/publicationは未開始。以下は当時の履歴で旧jobを再起動しない。

計画54・科学500M完了/一次評価中: actual232272がwhole20の追加500,006,912/総10,500,014,080/update320435を745.510秒で学習し終端を保存した。Web400,031,744/short99,975,168、EOS教師Web846,893/short607,745（旧物語short1,105,092より少ない）。同じjobがdev256/80生成/日本語192・331・1119を実行中。科学と検証262,144は別会計。80内容の個別採点・実CPUreview/条件付き全文・段階4採否/report/commit/UI復帰は未完了。重複学習や旧対照の再実行をしない。

計画54・段階2実行中: hidden Windows32072/actual Linux232272/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6083120、2026-10-05T05:20:28.697566Z起動。新110M教材を使う実CUDA exact save/resume25checks通過、検証262,144tokens別会計、whole20追加500Mの学習中。Linux reports/phase6/complete-document-500m-20261005/screen-job.json、Windows同run screen.stdout.log/screen.stderr.logとcheckpoint/latest.jsonを追跡。一次1800秒、必要時保存checkpointから同じ凍結条件で再開し、重複起動しない。UIはGPU中停止・wrapper finallyで元final10B復帰。一次評価/全80内容診断・条件付き全文・判断/報告/commit/停止は未完了。データと凍結実装のlocal commit aa53975。

計画54・段階1完了: 新pool110,000,202 tokens=story30,000,063/Web80,000,139、668,680全文、抽出累計73.340秒。最初4Bで量未達後、原条件を維持して未走査範囲だけ6.84Bまで継続し必要量で停止。一様ランダム40全文に弱例8を明記してbounded研究比較として受入、独立意味/事実/unique認証ではない。CPU12tests成功、実量/config/schema/source/対照を凍結。次に新データ実save/resumeと一条件500Mを1800秒以内で実行し一次評価・全80内容診断へ進む。旧対照の再学習なし。

2026-10-05 JST・新計画54の段階1〜4をユーザーが再開承認: 固定500Mで短文データ構成/準備量を改善する一条件を実行する。目標110M=低反復物語30M+短いWeb文書全文80M、trainのみ、CPU1800秒/Web最大4Bの必要分だけ抽出、無作為40全文を開始前確認。段階1教材builder/選別を実装し関連tests後に起動する。元UI231106のみ稼働、旧科学/evaluationは終了済み。保存Web/物語500M対照を再利用し、原条件を維持して採否/report/local commit/元UI復帰まで進め停止する。旧計画52の完了境界は履歴で新計画を阻まない。

2026-10-05 JST・計画52段階1〜4の実験/評価/判断完了: 20%低LR100Mと全文通過後の各500M・四地点一次・全320内容診断・500M全文/400/長文を完了した。500M一次CPU37/全文CPU30項目成功、候補は全文BPB0.948798235（親より−0.005220237、Web比+0.887930%）、固定EOS37/反復18/一貫性・適切完結19（各80）、全400 EOS179/反復36/Unicode・role・empty全0、長文128/512はEOS各12/20・文再出現各6・UTF-8失敗0で原条件を全通過。研究候補として採用するが文法38/80・停止37/80等のBase/Chat品質目標は未達。[最終判断/次案53](53_story20_low_lr_judgment.md)に同量500Mで短文教材構成/準備量を変える一条件を提案し、今回は実行しない。物語準備量59,963,449/消費99,975,168は約1.667周、科学計1,100,021,760/検証524,288別会計、GPU計6,007.147秒。実科学143237/174280・全文143904/177987・教材173735は完了して終了。元final10B UIがactual231106 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4964393 / ready02:14:01.602203Zで復帰し、HTTP SHA410f975d…/tokens10,000,007,168/busy=falseとactual processを確認した。判断JSON・要求別最終確認・local commitを保存して停止する。新pool/別500M/各枝1B/20B/50B/Chat/protected test/pushは未開始。以下の実行中・未完了記録は当時の履歴で、旧jobを再起動しない。

500M全文・Web側完了／候補側全文中: Web全文BPB0.940447718183、固定80 EOS0/反復62、全400 EOS10/反復128/Unicode・role・empty全0。長文128/512各20はEOS0/0、文再出現9/11、4gram反復0.839971/0.959310、raw失敗0。実source/hashとこの途中結果を`reports/phase6/story20_budget_full_progress.json`へ保存し、候補の合否はnullのままにした。actual177987が`coherent20-full`へ移り、起動約18分38秒で本文53,248/213,432 windows、stderr空、actual process存在を再確認。最終全文合否・段階4・UI復帰は未完了。320内容の対応変化も保存し、一貫性改善12/喪失2件、EOS新規18/喪失3件、適切完結率は実EOS中40.9%→51.4%。旧100Mに対する全品質の優位や意味能力改善は主張せず、結果を報告53へ追記した。同じ177987の完了を待ち、実CPU全文reviewと最終判断/報告/確認/local commit・元UI復帰まで進めて停止する。

500M全文の途中実測: Web対照の89,416文書/164,344,743本文bytes/42,003,934本文tokensを採点し、全文BPB0.940447718183を保存した。actual Linux177987のforward_callsが進み、生成評価を継続中（起動約8分21秒でactual process再確認、stderr空）。候補側・長文・原全文条件はまだ未確定。320採点のカテゴリ集計を`story20_content_categories.json`へ保存、物語一貫性は短い物語0→4/8、描写0→3/8、数字0→0/8。各8件の記述的集計で新gateではない。判断53に同量500Mで短文教材の構成/準備量を変える次案を準備し、今回のfull結果後に確定する。新pool/追加学習は未開始。最終確認runnerに別凍結full plan/source snapshotと具体的次案/report hashの確認を加え、uv構文確認済みだが最終実行はfullと段階4完成後に行う。次は同じ177987の完了→実CPU全文review→採否/報告/最終確認/local commit/UI復帰で停止する。

段階3・全320内容診断と一次review完了／500M全文・長文評価中: 全四条件80件ずつのrawを個別確認・採点し、実CPU37項目をすべて通過した。Web中間/終端の一貫性2点・適切完結は0/0、物語は9/19（各80）。物語の100M→500M差は+12.5pp、対応95%区間[+3.75,+21.25]。意味−1.042pp・常識−0.357ppはいずれも区間が0を含み、JBLiMP+3.021ppは[+0.302,+6.042]。終端の元一次条件を全通過したため、追加学習0の全文89,416/固定400/長文20prefix128・512を2026-10-05 01:41:50.837298Zに永続起動した。hidden Windows34068 / actual Linux177987 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4771336、actual process存在を確認。Linux`reports/phase6/story20-low-lr-10b-500m-20261005/full/full-job.json`とWindows同run`full.stdout.log`/`full.stderr.log`を追跡する。上限3,000秒、元親の保存結果を再利用。UIはこの評価中だけ停止し、finallyで元final10Bへ戻す。最終全文合否・段階4採否/次案/報告/local commitは未完了。同じ177987を追跡し、完了済み科学174280や旧100M全文を再起動しない。以下のpartial160/320等は履歴。

段階3・科学/一次GPU完了／内容160/320保存済み: 新しい二枝各500Mと四地点のdev256/greedy80/意味192/JBLiMP331/常識1119評価を終了した。GPU1,878.712秒、科学1,000,013,824/検証262,144は別会計、actual Linux174280は終了。Web中間→終端はBPB0.978642327→0.971570249/EOS0→0/反復55→62、物語は0.985129409→0.979911453/EOS22→37/反復29→18（各80、raw失敗全0）。物語意味63.021%→61.979%、JBLiMP75.529%→78.550%、常識33.870%→33.512%で一律の能力改善とはしない。Web160件を全文確認・個別採点し、二つの`story20_budget_annotations_web_*.json`へ保存、Linux`annotations.json`はpartial160/320。物語160件の個別内容診断・全320CPU review/原gate判定・条件付き全文/長文・段階4判断/次案/完成報告は未完了。元final10B UIはactual176353/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe、start ticksはserver.jsonと`story20_budget_result.json`の現在identityを参照、HTTP SHA410f975d…/tokens10,000,007,168/busy=falseを確認した。科学jobは再起動せず、残る内容診断から続ける。

段階3・二枝各500M学習完了／一次評価中: actual Linux174280が起動約25分3秒時点で`web-greedy80`へ移ったことを確認。物語枝は追加500,006,912/総10,500,014,080/update320435、Web400,031,744・short99,975,168、学習735.280秒、終端SHA f336806bee562cf11fe29506f833deae45de228c4b8acb1b942c7df21c82daac。保存short samplerはepoch1/position39074/blocks58558で、一周完了＋第二周の一部を実際に使用した。Web枝は747.396秒、二枝の科学計1,000,013,824で、一つのモデルの累積に足さない。各100M中間も保存済み。一次四条件のBPB/80生成/日本語診断→全320内容採点→原gate条件付き全文→段階4採否・次案・報告・local commit・元UI復帰が残る。新しい科学GPUを起動せず、同じjobの評価を追跡する。

段階3・Web500M学習完了／物語20%学習中: actual Linux174280が起動約13分5秒時点で`coherent20-train`400更新へ移ったことを確認、stderr空。Web枝は15259更新/追加500,006,912/総10,500,014,080/update320435を747.396秒で学習し、終端SHA d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4を保存した。物語枝は同じ元final10Bから別に学習中。中間/終端の一次評価・320内容診断・条件付き全文・段階4採否/次案は未完了。[判断53](53_story20_low_lr_judgment.md)は100M実測と残要件を保存した途中原稿。元UIはGPU中のみ停止し、finally復帰予定。科学174280の同じ実行を追跡し、重複起動しない。

段階3実行中・Web中間100M保存済み: actual Linux174280を起動約3分8秒時点で再確認した。実CUDA保存再開25checksすべて成功、検証262,144 tokensは科学会計と分離。Web枝は3300更新/追加108,134,400 tokensまで進み、100,007,936地点のupdate308228/総10,100,015,104 checkpointを保存した（SHA0813da0970485ec58d480f04f19b8dc92750421ce7086bef86232529f0626365）。GPU89%/VRAM7690MiB、stderr空。二枝の科学学習はまだ未完了、320内容診断/条件付き全文/段階4も未実施。新しい最終確認`scripts/review_story20_completion.py`は構文確認のみで、完了証拠としてまだ実行していない。job/metrics/latest/checkpointとactual identityを追跡し、同じrunを重複起動しない。README/roadmap/handoffに現52の再開状態を反映、local commit4f7260c。

段階3の各500M比較を永続起動: 準備commit742ec45、2026-10-05 00:56:22.906739Z、hidden Windows33908 / actual Linux174280 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4498545。actual process存在を確認した。Linux run`reports/phase6/story20-low-lr-10b-500m-20261005`の`screen-job.json`/arm metrics/checkpoint、Windows同run`screen.stdout.log`/`screen.stderr.log`を追跡する。CUDA実保存再開→二枝各500M→中間/終端の一次評価→全320内容診断→原gate条件付き全文/長文→段階4判断・report・local commit・元UI復帰で停止。起動済み同じjobを確認し、重複起動しない。

段階3・各500M条件凍結済み、起動前: 固定train4filesの構築は59,963,449 tokens/662,857文書で完了、source exhausted/120M目標未達を記録。99,975,168物語inputには約1.66727周を使う。40全文サンプルと14弱例、非ランダムsample・synthetic・広域重複未確認の限界を`reports/phase6/story20_budget_pool_content_review.json`へ保存し、限定比較として使用する。26関連CPU tests、凍結config/schema/probe成功。各500,006,912科学tokensと共通schedule中間100Mの実比較を開始し、320内容診断・原gate条件付き全文→段階4判断/report/local commit・元UI復帰で停止する。[現計画52](52_story20_low_lr_execution.md)。旧完了jobは再起動しない。

段階2合格・段階3データ準備中: 物語20%低LR100Mは全文BPB0.952080670、元親0.954018473より改善し、同LR Web0.945960821比+0.647%。固定EOS23/反復22、一貫性12/適切完結12（各80）、全400 EOS127/反復45/raw失敗0。長文128/512各20でEOS9/9、文再出現8/8、4gram反復0.474/0.586。GPU全文1,940.030秒、CPU原条件30checks全成功。実科学143237/評価143904終了、元UI復帰を確認。条件付き各500Mへ進むため、データ準備を2026-10-05 00:46:47Zに永続起動した。hidden Windows21332 / actual Linux173735 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4440874。`~/jmicro-data/phase6/simple-stories-ja-budget-20261005/job.json`とWindows`reports/phase6/story20-low-lr-10b-500m-20261005/prepare.*.log`を追跡。途中約45Mまで構築、500M config未凍結・科学GPU未開始。26関連CPU tests成功、元親/共通pool/共通schedule100M中間・500M終端/反復実数の実装を準備済み。次は実source量/40sample確認・必要epoch明記→config凍結・永続GPU起動→320内容診断/条件付き全文→段階4判断/report/commit・元UI復帰で停止。以下は準備/起動履歴で、現行状態は本段落を正とする。

段階1/一次内容診断完了、段階2全文/長文を永続起動: 物語20%・peak0.0001は100,007,936 tokens追加、学習159.277秒・一次GPU262.543秒。固定80でEOS23/反復22/raw失敗0、一貫性2点12/80・適切完結12、同LR Web対照は0/59/0。元mixtureと一貫性差8/paired下限>0を全通過し、全文/長文へ進む。新科学143237は終了、UI復帰確認後、hidden Windows30472 / actual Linux143904 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticksはfull launch記録を正とする、2026-10-05 00:11:52Zに段階2開始。追加学習0、GPU上限3,000秒、同LR Webと候補の未測定全文/400/長文だけ測る。原親BPB+0.001/全raw条件が通るまで500Mへ進まない。同一jobを追跡し、終了後のCPU確認→条件分岐→判断/report/commit・元UI復帰が残る。

物語20%・低LR100Mを永続起動: 準備commitca5dac0、20関連testsと実親/参照確認済み。hidden Windows30420、actual Linux143237 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4192785、開始2026-10-05 00:05:25Z。run`reports/phase6/story20-low-lr-10b-100m-20261005`へjob/source/metrics/checkpoint/rawを保存する。実CUDA保存再開→新条件100M/一次評価→80内容診断→事前条件付き全文/各500M→段階4判断/report/commit・元UI復帰で停止。同じactual jobを追跡し、重複起動しない。

2026-10-05 JST・段階1〜4を再開: ユーザー「4まで進めて」。[実行計画52](52_story20_low_lr_execution.md)に物語20%・低LR100M→有望時のみ全文/長文→全条件合格時のみ各500M→判断/次案/report/local commit・元UI復帰で停止の条件を保存した。保存済み同LR Web対照と25M poolを再利用し、原gateは不変。専用runner/config/schema凍結、20関連CPU tests成功、CPU実親finite/hash/元state・凍結参照確認済み、科学GPUは未開始。実process確認では既存UI140800のみ、旧科学job終了。次は準備commit後の永続起動。以下は過去の完了/起動履歴であり、現在の状態は本段落を正とする。

2026-10-05 JST・計画49段階1〜3完了: 通常LR物語10%100M→事前失敗時分岐の低LR Web/物語10%各100M→[判断と次案51](51_story10_judgment_and_next_proposal.md)を完了した。[実行50](50_story10_and_budget_execution.md)。通常LR10%はEOS17/反復40/一貫性4、低LR Webは0/59/0、低LR10%は16/36/6（各固定80）。両候補は事前一貫性差8件未達で未採用、全文/長文・500M/pool拡張の開始条件を満たさず未実施。常識5択の低LR配合対照差+3.038pp・95%区間+0.894〜+5.004は診断上の改善で、基本意味の対照差は負、幅広い理解能力・Base/Chat品質達成とはしない。科学300,023,808/検証524,288別会計、GPU775.522秒、CPU14/16 tests、実CUDA保存再開各25項目成功、追加全240出力内容診断済み。[要求別確認](../reports/phase6/story10_execution_completion.json)。科学139467/140216は終了。UIは元final10BでHTTP応答/busy=false、復帰時Linux140800 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks1468219。次案は20%・peak0.0001一条件100Mを保存済み同LR Web対照と比較する提案で、今回は開始しない。report/local commitで停止。500M/1B/20B/50B/Chat/test/push未実施、独立人手/全12.23B監査/広域混入確認は未実施のまま。

以下は今回の準備・起動履歴。最新状態と停止境界は上記を正とする。

低LRの同量比較を永続起動: 準備commitd3b762a、16関連CPU tests、peak0.0001/10%/Web対照各100Mの専用config/schemaを凍結。hidden Windows28816、actual Linux140216 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks1416619、開始2026-10-04 16:22:41Z。run`reports/phase6/story10-low-lr-10b-100m-20261005`とWindows`screen.*.log`へ永続保存。現在Web対照学習中、二枝評価と160内容診断→事前条件付き全文→段階3判断/次案が残る。UIはfinally復帰。科学140216のactual processを確認して同じjobを追跡、重複起動しない。

計画49段階1を完了し、段階2の低LR分岐へ: 物語10%/100MはGPU264.370秒、EOS17・反復40・raw0（固定80）。全80をCodex採点し、一貫性2点4/80で事前の対照差8件を満たさず未採用。元mixture条件は全通過だが内容条件を緩めない。全文/長文は未実施、500Mへ進めず、同じ親・10%・同量でpeak0.0001のWeb/物語各100M比較を一つ凍結した。[記録50](50_story10_and_budget_execution.md)。16関連CPU tests成功。先のLinux139467は終了、UIは元final10Bで復帰を確認。次は低LR二枝の科学200,015,872（検証262,144別）→160内容診断→条件付き全文→段階3判断/提案/report/local commit・UI復帰で停止。1B/20B/Chat/test/pushは開始しない。

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
