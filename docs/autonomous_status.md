# Codex継続作業の現在地

最終更新: 2026-10-03（日本時間）。実測の正本はreportとWSLのrun/data、milestoneは[roadmap](15_project_roadmap.md)。

## 実行中: 新しい12.23Bデータで2B学習

2026-10-04: ユーザーの「過剰な検証や照合はしなくていい」「学習に早く入りたい」に従い、独立監査の残りを停止。最後の進捗は29/32band、raw128files/全29,208,256records再構築は済み。構築時の全32band重複処理・全export往復検査と、[実train loaderの合格](../reports/phase6/corpus_10b_loader_ready.json)で[ローカル10B整備を完了](../reports/phase6/corpus_10b_ready_review.json)。train12,225,819,077 tokens/25,879,667文書、dev/testは別。loader49.147秒、batch2×1024・sampler再現一致。独立全件監査は未完了のまま明記し、`job.json`のInterruptedError/failedは[ユーザー指定の監査停止](../reports/phase6/corpus_10b_validation_policy.json)によるもの。構築済みmanifestと凍結sourceは変更せず、再監査・再exportしない。

ユーザーは2B学習を明示指定。[新しい学習config](../configs/phase6/base_2b_10b_data.json)と[実GPU開始記録](../reports/phase6/base_2b_10b_data_start.json)。同じ約10M/NoNormモデルをseed42で別runに初期化し、旧500M重みは保持する。stable57,984更新＋decay3,052更新、総2,000,027,648 tokens（batch丸め、減衰も2B総予算内）。BF16/Flash＋compile reduce-overhead、batch32/context1024、途中保存1000更新ごと。実950更新/31,129,600tokens、finite loss3.5481・grad、約709k tokens/sを確認済み。まだ品質改善とはしない。

実行先`/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-2b-10bdata-20261004/`。Windows hidden launcher28168、pipeline shell472、stable supervisor482/start_ticks2372467、worker487/start_ticks2372547、boot`0b330ec7-c11f-4bb3-be7c-cae9b868f4af`。正本は`supervisor.json`（operation移行後はPIDが変わる）。logはrun内`stable-2B-0.log`、全体は`reports/phase6/base_2b_10b_data_pipeline.log`。`scripts/run_base_2b_10b_data.sh`がstable→decay→既存protected dev/400生成評価を順に実行し、その後停止する。現在の実PIDを確認してから再開し、live時は重複起動しない。学習のみ約47〜48分＋既存評価約12分が目安、実測速度・保存で変動する。test/5B/10B/Chat/decoder比較は未起動。

以下はデータ整備・旧監査の経過記録。

2026-10-04 02:41 JST: [逐次near監査28/32band通過](../reports/phase6/corpus_10b_edges_audit_twenty_eight.json)。band0〜27の連続した完了logを確認。大group7,077件を含むband27は987.968秒（約16分28秒）で完了した。実PID1170053/boot/start_ticks1074573が記録と一致し、CPU時間が増加、完成export manifest SHAも不変。残り4band→全代表・全corpus/membership/split/token/index往復→terminal/PID終了→実train loaderを継続する。WSL空き619,283,476,480 bytes・RAM available約64GBを確認済みで拡張不要。全件合格・整備完了は未達、学習更新0。

2026-10-04 02:33 JST: [重複判定GPU化の実装・一次資料確認](../reports/phase6/corpus_10b_gpu_dedup_assessment.json)。現在は構築済みcorpusの独立監査で、27/32band完了、audit1170053のCPU時間が増加している。原処理はUTF-8文字5-gram集合の積/和をPythonで1組ずつ計算し、7,077件の大groupでは同一componentのskip前に最大25,038,426組。衝突のない整数IDへ変換し候補をGPUへまとめる方法は有力だが、変換・転送・精度境界・代表の一致・依存互換性を含むGPU実測は未実施。cuGraphの指定pair Jaccardは候補であり、このcorpusの速度保証とはしない。稼働中の凍結監査は継続し、GPU版への差し替え・再起動は行わない。将来比較は固定大group/実1M全32band、全候補・判定・代表一致、変換転送込み速度、限定pair probe180秒/採用目安2倍で閉じる。全件auditと実loaderは未完了、学習更新0。

2026-10-04 02:10 JST: [逐次near監査24/32band通過](../reports/phase6/corpus_10b_edges_audit_three_quarters.json)。band0〜23の連続した完了logを確認し、24段階はraw完了後7098.828秒（約118.3分、移行込み）。band23だけで967.156秒（約16.1分）かかり、band間の候補量・所要時間の差を実確認した。同じaudit1170053/boot/start_ticks1074573が実live、完成export manifest SHAは不変。24段階平均が残りも続く仮定のnear残は約39分だが、残り8bandも変動する。全代表・全corpus/membership/split/token/index往復・実loaderは別で未完了。全件合格とはしない。残り8bandを継続し、学習更新0。

2026-10-04 01:25 JST: [逐次near監査16/32band通過](../reports/phase6/corpus_10b_edges_audit_half.json)。band0〜15の連続した完了logを確認し、前半16段階はraw完了後4437.677秒（約74.0分、移行込み）。同じaudit1170053/boot/start_ticks1074573が実live、完成export manifest SHAは不変。前半平均が後半も続く仮定では残りnearは約1.23時間だが、後半の候補量は異なり、全代表・全corpus/membership/split/token/index照合と実loaderは別で未完了。途中結果を全件合格としない。後半16bandを継続し、学習更新0。

2026-10-04 00:50 JST: [逐次near監査8/32band通過](../reports/phase6/corpus_10b_edges_audit_quarter.json)。band0〜7の完了logが連続し、最初の8段階はraw完了後2344.360秒（約39.1分、移行込み）。同じaudit1170053/boot/start_ticks1074573が実live、完成export manifest SHAは不変。8段階平均が続く仮定で残りnear検証は約1.95時間だが、band候補量は変動し、後続の全代表・全membership/split/token/index往復と実loaderは別で未完了。全件合格とはしない。引き続き同じjobを監視し、学習更新0。

2026-10-04 00:30 JST: [序盤3bandの実測](../reports/phase6/corpus_10b_audit_early_timing.json)は374.910/208.675/515.511秒、平均366.366秒（約6.1分、最初はrawからの移行込み）。同じaudit1170053は実liveで、全32band中3個が完了。序盤平均が続くという仮定だけなら残りnear検証は約2.95時間だが、bandごとの候補量は異なり、後続の全token逐次再encode/byte/index/membership照合と実loaderの時間はまだ未測定。以前の全体残り3〜5時間という暫定値が上振れする可能性をユーザーへ説明した。24時間累積上限と全件受入条件を保持し、健康なjobを再起動しない。最終合格・整備完了は未達、学習更新0。

2026-10-04 00:18 JST: [逐次near重複監査の最初のband完了](../reports/phase6/corpus_10b_edges_audit_start.json)。全raw checkpoint後からband0完了まで374.910秒（約6分15秒、移行処理も含む）。全32band中1個の原逐次Jaccard検証を終え、同じaudit1170053/start_ticks1074573が実live。残り31band→全cluster/duplicate代表→全corpus/token/index往復→terminal/PID終了→実loaderは未完了。bandごとのgroup/candidate量が異なるため、この1個だけから全体速度や完了時刻を確定しない。原受入条件と完成exportを保持し、学習更新0。

2026-10-04 00:12 JST: [全128raw filesの独立再照合完了](../reports/phase6/corpus_10b_raw_audit_complete.json)。全29,208,256 records（raw29,009,357＋保護198,899）が取り込み完了件数と一致。原auditorのfull SQLite integrity_check、全raw hash/size、source payload/filter/protection、全signature、exact代表/eligibilityの比較を通過した。audit開始から3667.085秒には初期DB検査を含む。同じ1170053/boot/start_ticks1074573が実live、完成export manifest SHAは`856bf074...e0eb1`のまま。次は全32bandの逐次near検証・全代表→全membership/split/token往復→terminal/PID終了→実loader。これは途中の受入結果で、全件auditの合格・ローカル10B整備の完了とはしない。WSL空き619,283,693,568 bytes、RAM available約64GBで拡張不要。学習更新0。

2026-10-03 23:46 JST: [以前の大型成果物の保持確認](../reports/phase6/corpus_10b_prior_bulk_preserved.json)を実施。以前の固定reviewとconfigをWindows/WSL間で実hash照合してから、それらに記録された19 checkpoint（全stable/decay保存点とpilot）、旧pilot/expandedの両shard manifestと全train/dev/test stream/index/token byte table、保護用旧corpus、T4K Tokenizerの全37ファイル・9,058,888,985 bytesをWSLで再hashし完全一致。uint16 stream sizeも一致し、6.536秒で終了。[再現用checker](../reports/phase6/check_corpus_10b_prior_bulk.py)を保持。モデル読み込み・heldout採点・学習更新0。既存225小ファイルの保持確認を補う証拠で、新10Bの全件audit/実loaderの完了ではない。新audit1170053は引き続きliveで、全raw再構築を進める。

2026-10-03 23:37 JST: [初期DB検査通過・raw全件再構築へ移行](../reports/phase6/corpus_10b_raw_audit_progress.json)。同じaudit1170053/start_ticks1074573がlive。原auditorのfull SQLite integrity_checkがokを返し、保護198,899件と完了raw fileのsource/filter/payload/signature全比較を通過した位置で`audit_raw` checkpointが出た。観測は13/128files・3,136,181 records（保護を含む）、workers16。file00001→00006は約75.46秒/5files（約15.1秒/file）で、raw再構築の残りは同速度なら約30分。ただし後続32bands/全代表・全corpus/token列照合・実loaderは別で未完了、全件合格としない。次は全128files/29,208,256 recordsの再照合完了→全band検証→最終監査を継続する。

2026-10-03 23:21 JST: ユーザーの変換・保存高速化の質問に対し、[実train262,144文書/123,504,934 tokensの限定比較](../reports/phase6/corpus_10b_export_speed_probe.json)を実行。親で文書ごとにJSON生成する方式（16workers/batch128）と、worker側でJSON/tokenをまとめて返す方式（16workers/batch512）をABBA順で比較し、10.828/11.093秒→8.005/8.121秒、1.353/1.366倍。全本文/token/indexのSHA・文書/token/bytes件数が4回すべて一致、事前gate1.2倍を通過、180秒上限に対し42.136秒で終了。[再現用code](../reports/phase6/corpus_10b_export_speed_probe.py)を保持。基準は同じ出力を作るbuffered binary writerで、実export全体/全splitの速度や新pipelineの完成とは区別する。既定readonly SQLite接続はcache_size=-2000（約2MB）/mmap_size=0、page_size4096、page_count28,238,943。元auditの接続にもcache指定がなく、cache/mmap調整は別の実測候補（未採用・速度未測定）。live audit1170053は継続し、frozen code・完成export・全件監査基準を変更しない。完了見積りは現在暫定3〜5時間へ更新し、初期DB/後続全件照合速度が未確定で上振れし得ることをユーザーへ説明済み。

2026-10-03 23:10 JST: [全件監査v4の起動確認](../reports/phase6/corpus_10b_cached_audit_start.json)。元1106994は14:10:03 UTCにSIGINTによるterminal failedと累積9975.723秒を保存して実終了。watcherがjob-v3-retired.jsonを保持し、Linux1170053/同boot/start_ticks1074573の`bounded_feature_cache_audit_v4`を14:10:06 UTCに起動した。実/proc・旧PID消失・累積時間の完全引継ぎ・3 source snapshots全binding・完成export manifest SHA不変を確認。原逐次auditの全件checksを保持し、特徴量memoizationだけを検証済みcacheへ変更する。ログ`ten-billion/preparation-v4.log`、source`execution_v4_snapshot/`、出力`prepared-v2/`。WSL空き約581GiB。現在はauditの初期SQLite検査中、全件監査の合格と実loaderはまだ未完了。次はraw/signature→全32bands/代表→全membership/token列→terminal/PID終了→実loader→最終report/commit、学習前に停止する。以下の終了待機は解消済みの履歴。

2026-10-03 23:00 JST: [以前の225ファイル保持確認](../reports/phase6/corpus_10b_prior_files_preserved.json)。診断開始前の固定baseline SHA `241d5070...98ee`を確認し、Windowsの全225 source/config/evaluation/historical reportsの実hashが一致、missing/mismatch0。これは既存コード・小成果物の保持確認で、Linux bulk corpus/shards/checkpointや新10Bの全件auditの代用ではない。元1106994と終了待機watcher1169492は実/procでlive、cache auditへの移行はまだ終了待ち。

2026-10-03 22:54 JST: [終了の観測だけを再開](../reports/phase6/corpus_10b_handoff_resume.json)。元の5分timeout・送信済みSIGINT時刻・PID/boot/start ticks一致を必須に、シグナル再送0の常駐watcherを起動。Windows28320/Linux1169492の実identityを確認した。108GiB SQLiteの実読み取りが続くため、終了の観測は90分上限とし、元processの終了・terminal state・累積runtime保存を確認してからcache audit入口を起動する。元timeoutを別JSON、再開codeを別snapshotとして保持する。5 guard tests成功（実CLI branchでもSIGINT再送0/retired job保持を確認）。候補・全件audit・受入条件は変更しない。現在は元1106994の終了待ちで、監査完了/実loader確認は未達。

2026-10-03 22:52 JST: [監査引き継ぎ補助処理の待機上限](../reports/phase6/corpus_10b_handoff_timeout.json)。SIGINT後も元1106994が108GiB SQLiteの読み取り中で、5分の終了待機を超えたためwatcher1168675はterminal failedで終了し、replacementは起動していない。元PID/start ticks144729の実liveとCPU増加を確認、完成export/manifestは保持する。観測timeoutを元processの停止へ読み替えず、同じSIGINT/起動を反復しない。次は元processの実終了・terminal stateと累積runtimeを確認し、job-v3-retired.jsonを保存して`scripts/run_corpus_10b_cached_audit.sh`を直接起動する。全件audit・実loader・最終reportは未完了。外部操作を要するblockerではなく、既存processの終了待ち。

2026-10-03 22:46 JST: [export完成](../reports/phase6/corpus_10b_export_complete.json)。実train **12,225,819,077 stream tokens /25,879,667文書 /47,525,339,486 body bytes**。dev678,132,065 tokens/test679,399,996 tokensは別split。`prepared-v2/export-001/`とroot/shard manifestが完成し、target_met true、manifest件数・hash参照・全split uint16 byte sizes一致を確認。これはbuilder成果物で、独立全件auditと実loaderはまだ未完了。13:46:32 UTCにidentityを照合してv3へSIGINTを一度送信、元processはSQLite読み取り中のため終了待ち（実/procとCPU増加を確認）。終了と累積runtime保存後にwatcherがcache監査を起動する。5分以内に終了しない場合はwatcherが失敗記録を残すため、次は元processの実終了を待ち、完成exportを保持して監査入口へ移行する。元processがliveの間は再起動しない。完成後report/commitで学習前に停止する。

2026-10-03 22:35 JST: [監査引き継ぎwatcher](../reports/phase6/corpus_10b_handoff_watch.json)を常駐。Windows launcher28516、Linux1168675/同boot/start_ticks861194を実/procで確認、v3のexportは継続中。完成manifest・実train10B以上・shard件数一致・frozen source・元のPID/boot/start ticksとaudit stageを確認してから一度だけSIGINTを送り、終了と累積runtimeの保存を待つ。旧jobを別保存し、検証済みcache監査入口を起動する。90分の完成待機/5分の終了待機を超えたら失敗記録を残し、強制終了や自動再試行をしない。3 guard tests成功、liveで二重watcherのlock拒否も確認した。現在は完成export待ちで、引き継ぎ/全件auditの成功はまだ未確認。logは`ten-billion/audit-handoff.log`、statusは`prepared-v2/audit_handoff.json`。

最新観測（2026-10-03 22:31 JST）: 全32bandsのbuilder重複除去が完了し、同じv3 process1106994でexport中。[完了記録](../reports/phase6/corpus_10b_dedup_complete.json)で185,955,238候補組、707,772のband内検証済みspanning links、3808.713秒、groups/duplicates/result SHAを実成果物へ照合した（独立全件auditは未実施）。exportは約5.5分でtrain約3.37B tokens、約10.2M train tokens/s。変換残りは暫定15〜20分、独立全件監査・実loader・report/commitまで含む残りは暫定2〜4時間。後者は大規模audit速度が未実測のため確約しない。完成manifest/実train10B以上を確認後、検証済みcacheのaudit入口へ移行し、完成exportと累積実行予算を保持する。学習前に停止する。以下の途中観測は履歴として保持する。

最新の実行はexecution v3。元の取り込み・品質基準・独立逐次auditを保持し、後続LSHだけを8workersのband並列へ移行した。[実1M全32bands比較](../reports/phase6/corpus_10b_parallel_probe.json)で524,480候補coverage/全cluster/duplicate代表完全一致、30.004秒→9.135秒（3.285倍）。旧v2を実PID確認後にSIGINTで終了し、累積680.554秒・24files/5,630,035レコードのcheckpointを保持して再開した。元source snapshotとデータは保持し、追加実行codeを別snapshotへ保存する。

Windows launcher23824、Linux1106994/boot`0b330ec7-c11f-4bb3-be7c-cae9b868f4af`/start_ticks144729は同じidentityでlive。全128raw filesのcommitと29,208,256 records（raw29,009,357＋保護198,899）を確認し、2026-10-03 12:20 UTC（21:20 JST）にstage parallel_external_lshへ移行した。[取り込み完了と実process確認](../reports/phase6/corpus_10b_ingestion.json)で全file receipt hash binding・file row合計/最終ID/ingest件数・signature size14,954,627,072bytesが一致。v3 ingestion2691.384秒、旧24filesは再処理しない。eligible28,998,779件を全32bands/8workersで検証中。workers1109198/1109201〜1109207の実PID/start ticks/CPUを確認。data rootは`ten-billion/prepared-v2/`、ログ`preparation-v3.log`、再開入口`scripts/run_corpus_10b_parallel.sh`。[移行と実装](32_local_10b_corpus.md#並列lshへの検証済み移行)。WSL空き約682GiBで拡張不要。token化・全件監査・実10Bの利用確認は未完了。次は全band完了/代表hash→export実token数→元の全件逐次audit→実ローダー→report/commit、学習前に停止する。

最終の[実学習用ローダー利用確認](32_local_10b_corpus.md#学習用ローダーでの最終利用確認)も実装した。未変更のShard/BlockSamplerでtrain batch2/context1024を作り、mask/bytes/再生一致を検証する（モデル作成・学習更新0）。小fixture3tests成功、未完了job/失敗auditでは拒否する。実10Bの確認はpipeline全件監査とprocess終了後に実行する。CPUの小fixtureを実10Bの完成へ読み替えない。

取り込み途中の残り時間見積り（履歴、取り込みは現在完了）の[読み取り専用実測](../reports/phase6/corpus_10b_eta_probe.json): committed prefix13,111,597件、eligible12,908,957件のband0に3,722,286候補組、最大group2,491件。180秒上限で実測39.530秒、sort10.056秒。先頭3,000組だけの検証0.698秒は無作為sampleでも全件検証でもなく、全体の速度へ断定的に外挿しない。現在のfile実測から取り込み残約30分。後続の重複除去・export・独立全件監査を含む完成は暫定6〜12時間だが、大規模の候補/check比とaudit速度が未確定で上振れし得る。全32bandsの実測へ進んだら更新する。24時間は累積実行上限で、完成予告ではない。token化と監査は未完了、学習未起動。

Jaccardのunion集合生成を同値の集合要素数式へ置き換える[限定比較](../reports/phase6/corpus_10b_jaccard_probe.json)も実施。実1M・全32bandsの全524,480組のfloat score列SHAと全代表が一致し、29.481秒→20.087秒（1.468倍）。事前の採用条件1.5倍未達のため不採用とし、live v3・元の独立逐次auditは変更していない。180秒上限の比較は終了、同じ比較の反復・閾値緩和はしない。[再現用code](../reports/phase6/corpus_10b_jaccard_probe.py)を保持する。

2026-10-03 13:03 UTC観測で本処理は30/32bands完了、残り23/27の実CPU時間は増加。[残り3bandsの全候補数](../reports/phase6/corpus_10b_pending_bands.json)は23,719,429 / 26,963,689 / 12,711,887組、最大group6,566 / 7,077 / 4,410件で、元builder2048・audit4096のcacheを超える。読み取り専用の[cache限定比較](../reports/phase6/corpus_10b_feature_cache_probe.json)では各groupの固定32,920組のfloat score列SHAが一致し、2.836 / 2.899 / 2.676倍。全group retentionのcharged bytesは約356 / 399 / 234MBで2GiB以下。新しい8192 entries/2GiB上限cacheは2tests成功だが本処理では未使用。採用前の実1M/全32bands/全代表の一致はまだpending。次にこの全件prefix照合と独立auditの統合検証を行い、既存の進行を失わない時点でauditの特徴量再計算だけを減らす判断をする。元の候補・Jaccard・独立逐次audit基準・frozen source・24時間累積予算は維持する。

監査cacheの[実1M・全32bands照合](../reports/phase6/corpus_10b_feature_cache_integration.json)も完了。全524,480組のfloat score列SHA `059a54...f7a9`・全1Mのcluster/duplicate代表が一致。original27.987秒/cache28.595秒で小groupは約2%遅いが、前記の大group限定2.676〜2.899倍という採用条件2倍を満たす。原auditの特徴量decoratorだけを8192 entries/2GiB上限へ替え、全raw再構築・全候補逐次Jaccard・全token/byte往復・old heldout保護・破損棄却を保持する[adapter](../src/jmicro/cached_corpus_audit.py)を追加。fixtureで同じchecks/split countsと失敗後のdecorator復元を確認し、全107tests成功/skip/failure/error0（fork warning8）。実live排他lockで新CLIの重複起動拒否も確認。 新入口は[scripts/run_corpus_10b_cached_audit.sh](../scripts/run_corpus_10b_cached_audit.sh)で、出力manifest/実train10B以上・old source snapshots・両実比較・process終了が必須。元のingest/dedup/exportを再実行せず、累積24時間予算と別execution_v4_snapshotを保持する。現在の本処理はまだv3で31/32bands完了、新入口は未起動。次は残りband→exportの実10B確認まで既存jobを継続し、完成exportを保持して監査入口へ移行する。

### 取得・初回構築の記録（履歴）

2026-10-03のユーザー依頼で、2B計画を約10Bのローカルデータ整備へ更新し、実行を再開した。[保存先・取得上限・実装・監査・停止条件](32_local_10b_corpus.md)。全bulk dataをWSLの`~/jmicro-data/phase6/ten-billion/`へ置き、Windowsとの境界越しデータ処理を避ける。WSL空き835GiB/Windows約2.5TBを確認し、現時点でdisk拡張は不要。原corpus/shards/heldoutを保持し、学習は開始しない。

取得Windows launcher24348、Linux933704/boot`0b330ec7-c11f-4bb3-be7c-cae9b868f4af`/start_ticks21313。構築v2 launcher7876、Linux1105089/同boot/start_ticks75979。取得は128files・約34.6GBを609.1秒で完了し、job terminal completeと実process終了を確認した。[取得記録](../reports/phase6/corpus_10b_acquisition.json)。構築v2は実/proc照合でlive、stageはingest。保護用198,899レコードの登録が完了し、実raw取り込みへ進んだ。最初の3raw filesのcommit/再開checkpointを確認し、100万超のレコードを処理した。[処理中の記録](../reports/phase6/corpus_10b_progress.json)。WSL空きは約800GiBで拡張不要。完了した初期8filesはhash確認してhardlink再利用。実tokensは構築後に確定するため、まだ10B用意済みではない。

旧待機job1104732は取り込み開始前に終了確認し、checkpointのatomic保存を加えたprepared-v2へ移行。旧job/snapshotを保持し、取得jobはそのまま継続。新規config/取得runner/SQLite file再開・external-sort LSH・streaming shard export・全件再構築auditを追加。元のtrainer/evaluator/shards/expanded_data/configと歴史的reportは変更しない。全105tests成功（skip/failure/error0、fork関連warning6件）。小fixtureでは旧dev/testのexact/near保護、再開末尾復旧、元LSH候補一致、全token往復と破損棄却を確認した。今後は取得完了→実file速度/容量の確認→全体構築/監査→report/status/commit。goalは10Bの整備全体で、raw取得やcode完了だけでは達成としない。

## 以前の次回計画: 学習用データを2Bへ拡張する（10B依頼で更新）

2026-10-03のユーザー訂正を反映。次に取り組むのは、整備済みtrain756,087,912 stream tokensを、同じT4Kで測った合計2B以上へ拡張すること。5Bは後続の段階目標。公開元の総量は十分に大きく、現在の準備量が少ないのは初回500M開始用の取得範囲へ限定したため。[取得・構築・監査・停止条件](27_phase6_remaining_plan.md#次回の一区切り-学習用データを2bへ拡張する)を更新した。既存dev/test・評価suite・過去データを保持し、別config/outputで追加取得と統合重複除去を行う計画。構築時間/容量は開始前の実測で予算を定める。次回実行の完了は2Bデータの監査・報告・commitまでで、学習は別計画とする。

今回は計画訂正のみで、取得・構築・GPU推論・学習を起動していない。モデルは10,001,152パラメータ、学習済み系列の消費量525,008,896 tokens、準備済みtrain756,087,912 tokensは変わらない。データ量不足は検証する仮説で、原因確定・品質改善の結果ではない。decoder/短文mixture比較は保留し、以下の旧計画と監査は当時の記録として保持する。

## 以前の次回案: 生成方法の比較（現在は保留）

計画作成依頼に従い、[次回の一区切り](27_phase6_remaining_plan.md#保留した案-学習済み10mモデルの生成方法を比較する)と[条件/予算/終了条件](../reports/phase6/repetition_decoder_plan.json)を記録した。[計画の16項目照合](../reports/phase6/repetition_decoder_plan_audit.json)でhash/実reference件数/7files同期/234既存files保持/未起動を確認する（比較codeや品質の合格ではない）。モデルは約10Mパラメータのまま、500Mは約5億input tokensの学習milestoneを指す。次回は同じdecay後checkpoint（合計525,008,896 input tokens学習）で反復抑制1.0/1.1、dev80×greedy＋sampling3seeds、計640outputsを比較する。reference320の全IDsを既存結果へ照合してから効果を判定する。GPU推論累積15分上限、実装・検証・報告込み30〜60分の目安。比較runnerは未実装で、先に別CLIと永続/再開・元decoder再現の検証を行う。

反復を8件以上減らすこと、sampling/EOSを悪化させないこと、candidateのUnicode/role/empty0件を自動改善候補の目安とし、元のBase品質基準は保持する。固定20組のblind人手評価packetを準備し、独立人手採点がない場合は未実施/文法・関連性未確定を残す。全文BPBの再採点は不要。同じ重みの生成方法の比較を、学習データの原因確定やモデルサイズ増加へ読み替えない。次回もreport/status/commitで停止し、短文mixture学習や1Bへ自動移行しない。今回の依頼では推論・学習・data変更を開始していない。

## 最新の調査: 反復退行・EOS・データ構成の調査完了、停止

ユーザー指定の反復悪化調査を[事前計画](../reports/phase6/repetition_diagnosis_plan.json)に沿って完了した。[判断と全比較](../reports/phase6/repetition_diagnosis_review.md)、[数値・binding・20項目監査](../reports/phase6/repetition_diagnosis_review.json)、[既存225 files保持](../reports/phase6/repetition_preservation.json)、[終了・同期・停止の監査](../reports/phase6/repetition_completion_audit.json)。学習更新0、GPU推論249.75秒/900秒上限、全102 tests成功/skip0。1B・新data・新trainerの学習・次回案を開始していない。

同じ80greedy反復は旧100M48→stable131M69→328M70→stable500M70→decay66。旧→最終は24件新規・6件解消、stable→decayは4件新規・8件解消。拡張モデルは131Mから反復が多く、decayが全体悪化の発生源という結果ではない。EOS教師はstable1,061,096回/0.2127%、旧0.2151%とほぼ同じで、BOSだけのmaskと実sampler/countersが完全一致する。全文同一devのEOS平均NLL3.00827→2.53698、同じ256文書末尾のEOS argmax30→35と改善する一方、80短prefix直後のEOS argmaxは0、最終の平均確率0.00247%。

全文trainの平均body464→469tokens、固定2,048文書/512文字sampleのregex反復は両方42（主に記号）。長さやsample反復の増加を主因にできない。拡張trainはWeb/commercial_web100%、128tokens以下は0.8505%。短い完結文の教師分布とgreedyの候補集中を有力な仮説として残すが、データ・露出・token予算・batch・schedule/backendが同時に変わる旧新比較で原因を確定しない。8case×旧/最終の生成IDsは完全再現、短FP32 full/cacheの全16probeは元許容内。BF16にはargmax差が各1位置あり、精度の影響と全context/backend同値は未解決として保持する。

Linux raw evidenceは`reports/phase6/repetition-diagnosis-20261003/`。CPU511/GPU570、Windows launcher23056/3468は完了し、jobのPID/boot/start_ticks・source/plan hash・log・sample/trace/testsを保持する。次の行動は停止。次回案は同じ重みのdecoder対照（最大640outputs/GPU15分）、必要なら短文mixtureの各25M-token対照（別loader/trainer実装と再開gate必須）で、元の品質基準・凍結codeを維持する。量不足が主因とは結論せず、1Bへ自動延長しない。

資源についてはWSL側で実測確認した。学習は速度優先のbatch32/Flash/compile/BF16/fused AdamW、約695k tokens/s、driver peak約7.5GiB。最大容量batch111はVRAM97.64%でも約650k tokens/sと遅く、32を採用する。data wait約0.5%でCPU入力供給が主要制約という証拠はない。使用容量を100%にする方針ではなく、検証した範囲で最速を採用している。調査推論は逐次greedy中心で学習と資源使用条件が異なる。

## 最新の結果: 500M学習・評価完了

2026-10-03: 拡張trainの500M stable＋独立763更新decayと全文dev/400生成評価を完了。同一dev BPB 1.244126→1.022491、抑制greedy EOS 0/80→0/80、反復48/80→66/80。全99 tests成功。人手blind採点・test・Chat・新重みの量子化は未実施。1B前で停止。

ユーザー指定の計画1〜5を実施した。[学習・評価監査と比較](../reports/phase6/base_500m_review.json)、[全80 greedy生成例](../reports/phase6/base_500m_review.md)、[preflight](../reports/phase6/base_500m_preflight.json)、[99 tests](../reports/phase6/base_500m_tests.json)。本文一度採点・同一89,416文書/164,344,743 bytes・FP32 CE・windowを検証した。document paired改善95% CIは[0.221163593157386, 0.22214939473619974]。これはdev文書のsampling不確実性で、学習seed変動やデータ量だけの因果効果ではない。

[指定範囲の完了監査](../reports/phase6/base_500m_completion_audit.json)で起動条件・実stable/decay・全文dev/400生成・過去証拠保持・job終了・停止境界を11項目照合した。学習/比較の独立監査25項目も通過した。生成退行は品質未達の結果として保持し、技術検証の成功へ混同しない。

stableは15,259更新/500,006,912 input tokens、decayは追加763更新/25,001,984 tokens。全state checkpointを保持し、parent SHA不変・全更新の有限値・保存間隔を監査した。stable SHA `775b14be60b755153fcfa03633e8a3a489fcddc6508db69f759b5547df57fbbf`、decay SHA `0a64cfc3ac18d411d0d2144d9d9c8185e7010872baf5247612dd365bd619514e`。Linux出力は`reports/phase6/base-20261003/`、stable/decay/evaluateのsupervisor・log・source snapshot・全checkpoint・raw評価を保持する。元のstableから同じglobal305,176更新のまま継続できる。

Windows launcher16200 / Linux pipeline465と各GPU stageは終了。`supervisor-{stable,decay,evaluate}-500M.json`・pipeline stateを保持し、完了した500Mを再起動しない。初回の非login shell uv PATH不足はGPU起動前の失敗で、専用入口へuser uv PATHを設定して修復した。失敗log/stateを`reports/local/`へ保持する。比較用の旧small reportはWindows正本からLinuxへ同期し、元のdeep evidenceは変更していない。

生成はgreedy反復48/80→66/80、sampling反復6/240→11/240、Unicode0/400→1/400で退行した。sampling EOSは0/240→1/240で、greedy EOSは0/80のまま。Unicode1件は64-token上限でmulti-byte列が途中終了したものだが、凍結metricの失敗として残す。[Codexによる20件の内容点検](../reports/phase6/base_500m_content_review.json)でも意味のある続きを展開せず反復する例を確認した。これはblind人手採点ではない。

次の行動は停止。1Bへの単純拡大は現時点で推奨せず、EOS教師量・文書長と短文promptの違い・反復傾向・greedy/sampling差を既存artifactで点検し、対照/予算/終了条件を定義してから次の実験を提案する。生成品質の未達・人手評価未実施を保持する。今回の結果をBase v1/Chat完成や新学習重みのexport/量子化合格にしない。以下の未起動/再開待ちは以前の準備・計画作成時点の履歴である。

## 以前の準備・計画作成記録（履歴）

文書・計画の更新依頼に基づき、README/実装checklist/技術状況/引継ぎと[残りの計画](27_phase6_remaining_plan.md)を93c7d1dの検証結果へ揃えた。次回は500M stable→独立decay→全文dev/400生成評価から開始し、1B/2B/5B/10Bを段階判断する。必要なpaired CI・人手採点の集約は未統合として明記した。今回の更新では学習・実験を開始せず、凍結code/config/protocol・過去report/snapshotを保持する。

[文書更新の監査](../reports/phase6/documentation_refresh_readiness_20261003.json)で25文書のWSL同期、実CLIと凍結値の一致、内部リンク、247の既存fileの保持と本学習未起動を確認する。

## 方針と停止境界

最新の依頼は次回計画の作成。[次回の500M計画](27_phase6_remaining_plan.md#次回の一区切り-拡張データで500mを学習評価する)に、約90倍へ拡張済みのtrain、新規500M stable・独立decay・同じdevでの比較、終了成果物を記載した。次回は500M評価/report/commitで停止する計画を提案し、1B以降は後続段階とする。データ不足は未確定の仮説で、学習量やscheduleも変わる比較をデータ量だけの因果効果にしない。今回は文書だけを更新し、学習は未起動。

Pythonは3.12.7/uv管理、全実行は`uv run --frozen`。依存変更は`uv add`、復元は`uv sync --frozen`。GPU学習はWSL 2 / Ubuntu / RTX 4090。Git local identityは`yousan <ka1357amnbpdr@gmail.com>`、検証済み変更をcommitし、push/公開しない。

**Phase 0〜5とPhase 6①〜⑤の準備は検証済み。ユーザー指定の「1.生成/変換確認、2.本学習設定確定」を実施し、最終監査37 checksを通過し、`93c7d1d`へcommitして停止済み。500M以上の本学習は未開始で、次の再開指定を待つ。** [今回の比較と完了条件](30_phase6_readiness_execution.md)、[③完了記録](29_phase6_performance_completion.md)。

## ③の実測と採用

採用はT4K NoNorm / 10,001,152 parameters、Flash＋torch.compile reduce-overhead / fullgraph・static / deterministic、context 1024、batch 32・accumulation 1、FP32 parameters＋BF16、fused AdamW、WSD。入力32,768 tokens/update。3×200完了更新の定常中央値は**694,521 tokens/s**、最速reference/math batch 16（127,772）比**5.436倍**。

最速設定のsave/小sample評価込みpeakはallocated 5.73 GiB、reserved 6.59 GiB、driver 7.53 GiB。data wait 0.55%。測定条件の最大安定batchは**111、112 OOM**。111は3×200・厳密再開・保存/評価を通過し、driver peak 23.42/23.99 GiB（97.64%）、速度649,563 tokens/s。VRAM容量上限と最高速度を分け、運用候補はより速い32を採用する。allocator cap 94%、固定shapeの有限探索であり、任意設定の理論最高性能を保証しない。

9設定のstable 200 vs 100+100・decay 100 vs 50+50はmodel/optimizer/scheduler/RNG/sampler、token/bytes/digest、loss/LR履歴、親の不変性・元継続が完全一致。6最速/容量設定の各3×200確認も完了。**独立監査1286 checks全成功、採用設定の空compiler cache再開26 checks完全一致、全79 tests / skip・failure・error 0**。小sample評価は4 dev文書＋1 prompt×2 greedy outputs/各最大8 tokensで、全文品質評価ではない。

v3のunique raw metricsは10,005 completed updates / 414,298,112 input tokens、cold再開は追加100 updates / 3,276,800 input tokens。別々の性能runで、一つの長期Baseではない。未完了OOM更新、診断v1/v2をこの台帳へ含めない。

- [全結果](../reports/phase6/batch_performance_report.json)、[採用理由](../reports/phase6/batch_choice.md)、[速度・資源・token要約](../reports/phase6/performance_summary.json)。
- [独立監査](../reports/phase6/performance_completion_audit.json)、[cold再開](../reports/phase6/performance_cold_resume_report.json)、[79 tests](../reports/phase6/performance_tests.xml)、[文書・旧成果保持監査](../reports/phase6/performance_documentation_audit.json)。
- [v1/v2失敗保持](../reports/phase6/performance_failures.json)、[監査初回の生成output数誤判定](../reports/phase6/performance_audit_initial_failure.json)。backend別cacheと実compiled code/呼び出し検証を修正した。監査は既存APIの2 greedy outputsを正しく確認し、GPU条件を変更していない。

## 保存先と終了したjob

Windowsコード/Git正本は`C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`、Linux実行コピーは`/home/aihub_ubuntu/src/japanese-tiny-llm-10m`。Linuxの古いGit HEADだけで識別せず、snapshot/hashで照合する。

- v3: Linux `reports/phase6/performance-20261003-v3`、job terminal complete。Windows launcher 24452、Linux supervisor 426 / boot `37666cd9-cd78-41c1-a0cb-39c21d108047` / start ticks 78847は終了確認済み。
- cold再開: Linux `reports/phase6/performance-cold-resume-20261003`、terminal complete。Windows launcher 17308、Linux supervisor 620 / 同boot / start ticks 361156は終了確認済み。
- v1/v2はinvalidatedで診断snapshot/log/checkpointを保持し、launcher 18088/23060も終了。GPU compute processなし。完了したjobを再起動しない。
- raw metrics/requests/results/checkpoints/compiled code/snapshotは各runに保持。通常cacheはLinux `artifacts/compile-cache`、cold cacheはcold runの`empty-cache`。

## ①②と過去の成果を保持

①の固定FineWeb2 Edu Japaneseは8 files / 2,152,539,810 raw bytes。T4K train 1,604,292 docs / **756,087,912 unique stream tokens** / 2,946,200,160 body bytes、dev89,416/test89,485 docs。全raw/clusterとretained 1,783,193 docsのtoken/index/文字往復を独立監査済み。初期Web 100%、first500M約0.66回露出。巨大master全量の証拠ではない。rawは`~/jmicro-data/phase6/raw/`、corpus/shards/全監査は`~/jmicro-data/phase6/expanded-v2/`。

②のWSD stable/独立decay CLIとNoNorm/math batch 8の全state再開・分岐完全一致は73 GPU checks / 74 tests、独立55 checksで完了。12 checkpointsとsnapshotをLinux `reports/phase6/preparation-20261003/cuda/`へ保持。[①②完了記録](26_phase6_preparation_completion.md)。新sourceの通常resumeは旧checkpointを拒否する契約を維持し、旧sourceはsnapshotへ保持。旧73 reportsとuv.lockのbyte保持は総合監査で確認済み。

## 今回の④⑤: 検証済み・本学習前で停止

**固定の短/1024入力・元のcache分割・全12数値比較が成功し、本学習設定をversion2として再凍結した。** [変換結果](../reports/phase6/nonorm_export_parity_report.json)、[独立した実CLI/重み監査149 checks](../reports/phase6/readiness_export_audit.json)、[全90 tests / skip・failure・error 0](../reports/phase6/readiness_precision_tests.xml)。

採用したCPU推論profileは `cpu-f32-f64-accumulation-v1`。FP32の重み・activation・cache・logitsを維持し、Linear/attentionの積和、RMSNorm分散、softmaxの和をFP64で累積する。SiLU/default RoPEのtrigも精度を上げる。Torch/HFの通常実行とcacheは完全一致、native1024の最大差0.0000124574は固定atol1e-5＋rtol1e-4以内。成果物metadataから実推論CLIも同じprofileを適用し、対応しないstock runtimeを拒否する。runtimeはLinux `artifacts/runtime-stable-f32-v2`、archive/patch chain/binary/shared librariesをhashで照合する。CPU精度優先の経路で、stock FP32やCUDAの同精度を保証する結果ではない。

旧stock FP32の失敗、RoPE周波数だけを修復した失敗、CPU8設定とCUDA参照の失敗を保持する。第1層q_projからの誤差増幅を[159 stageで追跡](../reports/phase6/nonorm_cache_precision_trace.json)した。2つ目の修復案で累積精度を上げ、途中版の4要素の未達はtrig丸めの差を修復して解消した。[修復の採否と保持](../reports/phase6/nonorm_precision_repair_report.json)。許容値・入力・必要な比較・学習済み重みを変更して通過扱いにしていない。

GPU学習coreのmodel/shards/training/uv.lockとreadiness worker/evaluatorは変更していない。高速CUDA/BF16経路にはCPU profileを適用せず、LR比較・保存再開の実測を維持する。LR0.001/0.002/0.003は各2,000 stable＋独立100 decayで完了、固定dev256文書BPBは1.18776153/1.18404703/1.18739314。0.002を採用。新sourceのstable400/200+200・decay100/50+50は50 checks完全一致、cold200→400は25 checks完全一致、親全file不変・元継続も成功。[GPU独立106 checks](../reports/phase6/readiness_gpu_audit.json)。合計7,500 updates / 245,760,000 input tokensは複数の準備runの台帳で、本学習系列ではない。

400生成は360.684秒、Unicode0/400、greedy EOS0/80・反復48/80で品質未達。全文dev89,416文書 / 164,344,743 bytes / 42,003,934 body tokensを336.292秒で採点しBPB1.2441264716、scalar/batch差0.0000330177（事前許容0.001以内）。旧pilotの直接改善量や人手文法評価の合格にしない。新CPU profileのcontrollerは実argmaxからのEOS/EOT停止と3 backendのgreedy IDsを実CLIで検証し、合成停止fixtureをモデル品質へ数えない。

[本学習設定version2](../configs/phase6/base_frozen.json)はbatch32・accum1・context1024、32,768 input tokens/update、LR0.002、warmup200、seed42、Flash/compile reduce-overhead/fullgraph/static/deterministic、WSD global305,176更新（10B丸め）、各観測点5%独立decay・floor0.1。save1,000更新ごと・全checkpoint保持、推定347件/41,702,694,225 bytes、run上限100 GiB・最低空き200 GiB。[起動/復旧計画](../reports/phase6/base_launch_plan.json)。`launch_enabled=true`は技術gateの成立を示すが、今回は起動しない。先の起動不可設定は[version1](../configs/phase6/base_frozen_blocked_v1.json)と[実起動拒否証拠](../reports/phase6/base_launch_guard_report.json)へbyte保持した。

Linux deep evidenceは `reports/phase6/readiness-20261003/`、最終exportは同runの `export-stable-f32/`、source snapshot/logs/raw logits/weightsを保持する。GPU準備とCPU8設定のsupervisorはterminal complete、精度build/probe/正式検証/CLI/テストも終了。`93c7d1d`のcommit後にGPU compute processなし・Git cleanを確認した。完了したjobを再起動しない。

**次の行動は停止。ユーザーが再開した後に、凍結source/data/runtimeを照合し、既存process/checkpointを確認して500Mの新規Base学習から始める。** prepareが既定で、復旧は同じglobal予算のまま行う。500M/1B/2B/5B/10Bの段階評価、Chat trainer、mixture、Muon、学習後量子化品質は今回の範囲外・未実施として維持する。外部権限やdriver更新のblockerはない。

現在速度から500M約12分・10B約4時間は純学習の算術値。compile/startup/全文dev評価/400生成/保存/decay枝を含め、完成時刻の保証にしない。[予算](24_phase6_plan.md)。以前の状態は[Phase 5当時status](autonomous_status_phase5_20261003.md)と[復旧履歴](autonomous_history_20261003.md)に保持。
