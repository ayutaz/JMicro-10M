実行中（2026-10-06 JST）: 五項目stage4の量/学習比較をWSL RTX4090で永続起動。actual481317/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start10369108とWindowsworker33932をps/procで確認。凍結config SHA f4c32912b250e733bfd78e7d56f66f012484e32b4e4edb12fbca2b8c1e315fb8。500M教材側の実CUDA連続/再開全state一致に合格し、100,000,000教師を完了（valid/physical100,499,456、Web80,072,899/story19,927,101教師、step149.842秒）。終端5ad2b5e1…の実LR/有限state/教師/cursor/metricsを読み取り監査し、100M時点から同20M decay枝の実CUDA再開全state一致も成功。100M後の生成品質は未評価。reports/phase6/amount-learning-20261006にjob/log/full checkpoints/config/sourceを保持し、本流2B＋small1B/同20M枝×5/GPU7200秒を実行中。GPUjob中は元UI停止、終端で元10B UI復帰。全400内容確認/段階4結論、改善Base/Chat/量子化と全五目標は未完了。旧数値7失敗/品質基準維持、Pythonは全てWSL uv。前準備と凍結のverified local commit f96c7ab、pushなし。

進捗（2026-10-06 JST）: stage4の入れ子教材v2準備が完了。small100,000,157/491,872文書、large500,000,785/2,459,360文書、dev2,000,207tokensを保存。source/本文長/編集単位/EOS分布は厳密1:5、固定64内容は弱10で既定10以下に合格（独立人手・事実認証ではない）。全量のglobal near/site/author照合は未実施。CPU5tests成功、遅延doc shuffleは従来入力順序と一致し全epochコピーを省く。configs/phase6/amount_learning_comparison.jsonにfresh現13層・500M教材本流2B/100M教材本流1B・同20M decay×5＝科学3.1B、GPU7200秒を凍結。本流/枝の保存再開、完了更新metrics回復、未評価の旧節目を処理しても最新本流へ復帰する実装を用意。科学GPU未開始、次は永続launcher→実CUDA再開一致→量/学習比較と全400内容。元UI479695とHTTP元10B親SHA/学習10,000,007,168を確認。段階1〜3は比較完了・候補不採用、改善Base/Chat/量子化を含む全五目標は未完了。旧数値7失敗・品質基準を保持、PythonはWSL uv3.12.7、pushなし。

継続（2026-10-06 JST）: stage3の現13層対9/6層各300M/全160新内容/実state採否を完了、両新構成不採用、全五項目は未完了。stage4全文供給v1はWeblarge315,728,705/small63,145,741/dev1,600,197で400M不足、592.386秒で終了・不在。新v2 CPUactual480376/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start10234538とWindowsworker31260を実確認。閉じたmatched prefixのcopy・index/cursor/厳密1:5検証を完了し、冒頭4block内の原文完結段落を追加抽出中。reports/phase6/nested-material-20261006-v2/prepare-job.json/sourceとdata同名に永続保存、CPU600秒/8workers。100M/500M供給と固定64内容は未達、量/学習比較GPUはまだ開始しない。元10B UI479695/start10188024＋HTTP親SHA410f975d…/tokens10,000,007,168/busy=falseを復帰確認。次はv2実供給/固定64内容→同source/長さ/編集単位/EOSで量を分離する学習config/command→改善Base→Chat/量子化。Chat教師samplerだけCPU3tests済みで学習/品質達成ではない。旧数値7失敗/全品質基準/全目標維持、重複job禁止。

完了/継続（2026-10-06 JST）: stage3の同Wiki10M・fresh各300M構成比較と全160新内容/実state監査を完了。現13層/9層/6層は共通Web BPB2.103709/2.166975/2.221544、意味48.958/36.979/50.000%、JBLiMP69.789/66.767/67.976%、JCQA23.012/22.788/23.235%、EOS54/59/52、自動反復4/7/6、一貫性0/0/0、適切完結0/2/0、Unicode1/0/2（各80）。未見Wiki dev32 NLL3.197/3.207/3.114・4gram反復20/15/17で構成変更だけでは未解決。両新候補不採用、容量不足の確定でも10M不可能の証明でもない。現構成300M結果を再利用し新科学600M/valid physical605,093,888、実CUDA16更新/検証519816別、結果GPU975.858秒・占有976.383秒。各学習410.507/399.853秒、VRAM peak5,766,197,760/4,837,471,744bytes。actual475615終了・不在、元UI479695/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start10188024生存・HTTP親SHA410f975d…/10,000,007,168/busy=false確認。可搬architecture_comparison review/annotations/57text rawtar14,628,836bytesを保持。次はstage4 actual477999で同source/全長/EOSの入れ子100M/500M準備を継続、CPU600秒内の供給と固定64内容の合格を確認する。学習量分離/改善Base/Chat/量子化と全五項目は未完了。旧数値7失敗/品質基準維持。

実行中（2026-10-06 JST）: 五項目stage3の構成比較を実CUDAで開始。actual475615/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start10089814をps確認。config architecture_comparison.json SHA33876ad915db583e02b12f53fbd4602f050f4ac55b2907a841b43bd28d85eef3。9層256/FFN1040・10,011,392と6層384/FFN832・9,982,848を同Wiki10M/seed42/各300M教師/LR.002/warmup200でfresh比較し、現13層Wiki300Mは再学習せず再利用。9層の実CUDA連続/再開full state一致を確認、4000更新129,971,858教師/loss1.969088有限。GPU学習各600秒/全体3600秒。reports/phase6/architecture-comparison-20261006/job.json/metrics/checkpointsとlauncherを保持。元UIはGPUjob中停止、終端で元10Bを復帰。Wiki単独は本学習不採用、構成/容量を単独原因と断定しない。全160新内容確認と採否、stage4の実100M/500M供給・量分離、Base/Chat/量子化は未完了。全品質基準/旧数値7失敗維持、重複job禁止。

完了/継続（2026-10-06 JST）: 五項目stage2の同じfresh0重み・連続各300M教材比較と全160内容/実state監査が完了。従来v3対WikipediaはBPB1.637138/2.103709、意味46.354/48.958%、JBLiMP72.810/69.789%、JCQA24.665/23.012%、EOS18/54、自動反復7/4、一貫性9/0、適切完結9/0、Unicode0/1（各80）。両候補不採用。Wikipediaのみの説明文は日常prefixを辞典の定義に変え、一般分布と内容が退行した。Wikipedia自source train32 goldNLL1.602/top1.660は初期より改善するがdev32 NLL3.197/top1.447、反復20/32/EOS25で、内部汎化も未達。容量不足の確定ではない。科学600M/valid・physical604,766,208、実CUDA16更新/検証別、GPU1148.505秒、各学習457.474/456.315秒、peak VRAM6,149,073,408bytes。actual467992終了・不在、元UI472318/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start10063411とHTTP親SHA410f975d…/10,000,007,168/busy=false確認。可搬material_comparison各JSON/rawtarとLinux二終端・教材を保持。次は条件付きstage3最大2新10M構成を同じ教材・各300Mで比較、現13層300M結果は再学習せず再利用。Wiki単独を本学習へ採用しない。全五項目/Chat/量子化は未完了、旧数値7失敗/品質基準維持。

実行中（2026-10-06 JST）: 教材比較actual467992/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start9948069をpsで確認、reports/phase6/material-comparison-20261006/job.json/metrics/checkpointsへ永続保存。従来v3側CUDA連続/再開一致、各300Mの前半をfinite loss/gradientで学習中。元UIは停止、job終端で元10Bを復帰する。新しいWikipedia側の学習は前半評価後、全160内容確認/採否は未完了。次段階の条件付き2新構成のコマンドを実装し、CPU1testで初期重みと学習再開latestのdirectory分離を検証したが、構成GPU/config凍結は未実行。五項目目標を保持、Chat/量子化未達。重複jobを開始しない。

進捗（2026-10-06 JST）: Wikipedia selector第2版の未確認固定64は弱8で10以下の内容基準に合格。train10,000,117/dev500,109、原文/全64理由と旧弱17を保存。旧校正64記事除外、JSQuAD記事/固定prefix除外、local exact/family分割、独立全corpus near-duplicate監査は未完了。既存raw利用の準備45.210秒。関連CPU5tests成功。各300M比較をconfigs/phase6/material_comparison.jsonへ凍結。同じfresh0更新/emptyAdam/親SHA70d86a83…・model10,001,152・Tokenizer4096・batch32/context1024・LR.002/warmup200・連続90%stable/10%decay、旧v3対新Wikipedia。共通dev32は両trainのexact hashと非重複。GPU1800秒/各学習600秒、保存再開検証教師は別会計。次はscripts/run_material_comparison.ps1を永続起動し、実CUDA再開→各300M→全日本語/160内容と採否。五項目/Chat/量子化は未完了。

進捗（2026-10-06 JST）: Wikipediaのtrain10,000,065/83,559文書、dev500,240/4,198文書を準備したが固定64弱17で内容不合格、全原文/理由を保存し学習0。初回4file供給4,359,178の失敗と再利用証拠を保持。次は欠落した外国名欄・外部記事予告を全文除外するselector第2版を凍結し、確認済み64記事familyを校正用として除外。既存rawを再利用、必要な新fileだけ取得。品質基準10/64は変更せず、最大2内容改訂、供給拡張を品質改訂と混同しない。関連CPU4tests成功。LR段階は完了・両候補不採用、全五項目は未完了。次の未確認64で合格した場合に限り、同じfresh0更新重み・LRで従来v3対新教材を各300M連続学習（GPU1800秒）する。

進捗（2026-10-06 JST）: 五項目stage1の低LR比較を完了・内容/保存再開/全state/同教材順序監査成功。各追加200M科学400M、valid/physical402,980,864、実CUDA16更新/検証520252教師別、GPU897.626秒。低LR追加側BPB1.089878/一貫性4/適切8/EOS29/Unicode0、新規側BPB1.672706/3/5/23/1（各80）。再加熱より追加側BPB13.21%改善、新規側は4.19%悪化。両候補不採用。全160理由・固定train/dev履歴・43raw members30.9MBの可搬証拠はlr_recovery各file。actual446010終了・不在、元UI462134/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start9763615とHTTP親SHA410f975d…/10,000,007,168/busy=false確認。stage2ではWebv1弱33/64、全文Webv2はdaily96,088/3M供給不足、青空文庫+Webv1弱30/64、校正用work除外v2弱32/64を保存・いずれも学習0。新しいWikipedia説明文の10M準備へ移る。固定source revision/原文冒頭段落・article family分割・JSQuAD記事除外。全PythonはWSLuv、CPU8workers、ext4、必要な新fileのhashのみ。全目標未完了、stage3〜5/Chat/量子化は未着手。旧数値7失敗・全旧証拠と基準維持。文学記録のsource_previously_in_parent_training=falseは新source取得歴だけを示し、旧Webとの重複/親未見を保証しない。

進捗（2026-10-06 JST）: 五項目全体を継続中。stage1低LR比較actual446010/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start9673316、追加側200M終端評価完了、新規側追加200M学習中。教材v1はWSL CPU23.652秒でtrain10,000,048/dev500,048を準備したが固定64内容弱33で不合格・未学習。全64理由/原文を保存しv2を別版で準備する。v2は中途抽出ではなく2〜6完全文のoriginal EOS parent全文と冒頭照応/OCR/予告の除外、dailyは過去の行動で区分。CPU5tests成功。旧v1/旧教材/数値7失敗/基準を保持。全五項目未完了、stage2同量比較/条件付き構成/量分離/Base/Chat/量子化は未完了。永続jobの実identityを確認して重複起動しない。

最新完了（2026-10-06 JST）: 新目標の長期段階1〜3を実診断・教材再設計・条件付き各300M戦略比較と採否まで完了。教材v3 train10,000,208/73,260全文、dev500,319/3,690、固定64弱10。供給不足v1/内容不合格v2/新規warmup構築失敗とwrapper修復を保存。継続100M→300M BPB1.070892→1.255773/一貫性6→8/EOS31→31、fresh1.413020→1.605410/6→5/12→22、300M両Unicode1。全既存品質gate未達、両候補不採用。LR再加熱・過適応/忘却は次の仮説で未確定、10M容量やデータ増量の効果は断定しない。全320個別理由（非blind）/四日本語評価/actual教師LRfull state監査成功。科学600M/valid physical604,504,064、CUDA再開32更新1,040,748教師別。段階3GPU1396.456秒/診断76.895秒、CPU変更関連tests/完了監査成功。raw153members gzipと三凍結config、Linux元/100M/300M終端・教材を保持。completionはreports/phase6/strategy_scope_completion.json、結果/次案はdocs/15_project_roadmap.md末尾。全科学job終了・不在。元UI actual444875/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start9599628＋HTTP親SHA410f975d…/tokens10,000,007,168/busy=false確認。次案はLR/損失切り分け→教材改訂→条件付き10M構成→データ量と学習量分離、未開始。次案の構成計数10,011,392/9,982,848はCPUのみ。旧数値7失敗保持。verified local commit後に停止。長期段階4/Chat/20B/test/push/公開なし。以下は履歴。
WSLの最新run: reports/phase6/generation-transfer-20261006（名称はrun識別子、実行日時はjob参照）、curriculum-strategy-20261005-v3（両100M）、curriculum-strategy-300m-20261005（各追加200M）。教材/home/aihub_ubuntu/jmicro-data/phase6/curriculum-strategy-20261005-v3と元story/Web poolsも別途移す。終端100Mはcontinuation00308251/fresh00003075、300Mはcontinuation00314400/fresh00009224、いずれもoptimizer/scheduler/RNG/samplerを保存。raw可搬gzipに重みと巨大shardsは含めない。設定/実コードsnapshotを保ち、完了したrunnerを再起動しない。新PCはWindowsの最新local commitを正本にする。元UIはscripts/start_webui.ps1、後日はserver.jsonとactual identity/HTTPを再確認。今回の次の研究は提案であり未起動。
最新完了（2026-10-05 JST）: 契約75の準備・各100M比較・品質未達による拡大非実行まで完了、結果docs/79_narrative_diversity_results.md。公開原文10000/1,206,453準備tokens（物語9000/Web1000）、固定64内容弱10/64、CPU9tests成功。元同一10Bから従来自然1000対新原文10000を各Web80M/short20M教師で学習、日本語全評価/専用dev64/160個別内容完了。基本意味58.333→64.583%、BPB0.980130→0.984834、EOS30→7、反復31→27、一貫性6→3、適切完結6→2。候補不採用、50k/5Mへの拡大・追加500Mは未開始。科学200M/valid・physical200,966,144、CUDA再開8更新260,794別、GPU500.023秒。比較actual395310/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start9106956終了・不在。元UI395857/同boot/start9157480とHTTP親SHA410f975d…/10,000,007,168/busy=false確認。可搬narrative_diversity JSON/tests/raw gzipとLinuxrun/data/両optimizer込み終端保持。最初の準備失敗、非blind内容判定、source/長さ/EOS密度の交絡、結果72の数値7失敗も保存。次案docs/80_generation_transfer_plan.mdは正解対自由生成・64/256停止位置の診断から変更を一つ選ぶ計画で未開始。今回の範囲は完了、verified local commit後停止。新data/GPU/20B/Chat/test/pushなし。以下は履歴。

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
