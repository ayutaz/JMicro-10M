最初8.15M対100Mのread-only比較を実完了（2026-10-06 JST）: 最新ユーザー境界は品質・独立seed/full dev/protected test/採用を満たすBaseを完了して通知・停止。Chat/Dialogue/SFT/量子化には進まない。actual562158/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14551757はcomplete・実ps不在、GPU88.782514秒（450秒上限）、新学習/optimizer0。同じ元Web保持100M軌跡の最初250更新8,150,782教師と終端を比較したため、独立学習や追加教材として重複計上しない。固定byte256/472055bytes・全日本語・全80greedy/max64・bridge128/旧retention128・固定train full/body/EOS CEを完了。新80を全件個別に読み、同id/prefix/raw/stopの既存peer2件だけ同じ評点・根拠を再利用したnonblind採点。独立人間評価ではない。

8.15M→100M: BPB .991492→.990936、一貫性2=6→12/80、適切13→26、EOS25→34、反復31→21、文法2=68→72、関連2=75→68、Unicode failure両方1。意味66.667→59.896%、JBLiMP74.622→75.529%、JCQA34.674→35.567%。早い点の採用基準は未達で、早期停止による今回の改善は支持されない。単一のnested軌跡・一貫性差early-final=-6/pairedCI[-.1625,.0125]なので、量一般の因果や有意な終端優位、能力上限を証明したとはしない。短文source train CE/EOSは終端でさらに改善、Web train CEはほぼ同じ。一方local bridge両極正解は39→57/128、未見構造1→2/64に留まる。生成器共通のlocal probeと低いtrain EOS損失だけでは自然文の汎化・自由EOS品質を証明できない。relative/absolute/歴史Web1%の元条件は維持、不採用・Base未完了、最終seed/full/test未実施。残CPの都合のよい走査・自動学習延長・PCGrad・品質緩和をしない。

compare-result SHA cf11fcd265a6096584f4f67ce45eaadda919d3b6a62b49ba24566df009e62297、raw SHA付き全80notes/review/completionを保存。terminal215text/8,484,555bytes、gzip1,746,936/SHA c219a8322f98fe2409befd3c2a8f046c2317a71bff5bc8c11fb367784305a57c、全Windows entry/archive raw SHA一致。元10B UI563107/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14561114の実ps・HTTP親SHA410f975d…/10,000,007,168/busy=falseを確認。science GPU job0。completion reports/phase6/early_exposure_comparison_completion.json。次は既存bridge/retentionの各case尤度を使い語彙・未見構造とgold EOS/誤候補marginの失敗を追加GPU/学習なしで区別し、その証拠に基づく有限比較を事前定義する。旧数値7失敗・全品質条件を維持、PythonはWSL uv3.12.7、local commitのみ・pushなし。以下は過去の履歴。

保存済み最初8.15M対100Mのread-only比較を実装・起動（2026-10-06 JST）: 前turnfa37d9bはUTF8/paired256/source勾配の実診断を完了したprogress。最新ユーザー境界のBaseのみを継続し、Chat/Dialogue/SFT/量子化なし。early_exposure_comparison_proposal.jsonで結果を見る前に選んだ最初の250保存update305426/8,150,782教師/8,192,000input/CP f6ba0fd4…を実preflightで確認。元100M軌跡内の早い時点と終端を比較し、新学習・optimizer update0、教材増量も行わない。追加量の重複を独立した新100Mへ数えない。

run/review_early_exposure_comparison.pyと永続PS launcherを実装。元10B親/実CP lineage・actualLR.0002/元Web cursor/同source・250historyとの一致、元byte256/472055bytes・日本語192/331/1119・80greedy/max64、同128bridge/旧128retentionを維持する。100M結果・notesは正確cacheとして再利用しGPU再評価しない。固定4source×4batch×8×1024のtrain input/教師SHAを勾配診断と一致させ、full/body/EOS CEのみread-onlyで測る。学習/後段/保存点変更の拒否と不均一body/EOS分母を含むCPU2tests/1.09秒・PS構文/actual preflight成功。旧凍結trainer/evaluator/採否条件を変更しない。

Windowsworker35628/actual562158/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14551757の実psとjobを確認しWSL uv3.12.7で評価開始。science config SHA83ee2dfc699d6f2e8e8f7572b0625d7dad8987ebae2f205a2b4e805ecc664dde、新GPU累積450秒上限、stage generation80へ進行。run reports/phase6/early-exposure-comparison-20261006、restart scripts/run_early_exposure_comparison.ps1 -Worker。実live/complete jobの重複起動を拒否し、section/個別case結果を再開可能に保存する。科学中元10B UI停止、wrapper finallyで復帰。準備133text/2128479bytes、gzip654957/SHA8c508d77fe32b0036a69d9ed26849dd8ee998ac98f60d9a0d9a3d471248a46bb、全Windows entry/archive raw SHA一致。

次は同jobの全評価/損失終端→新80を全件個別に読んで同id/prefix/text/stopの既存peer評点だけ再利用→元relative/absolute/歴史Web1%採否→可搬証拠/local commit。最初の保存点の品質は未判定、Base未完了・最終seed/full/test未実施。失敗なら採用せず、残checkpointの都合のよい走査/自動学習延長/勾配補正/品質条件緩和をしない。旧数値7失敗/全品質条件保持、local commitのみ・pushなし。以下は過去の履歴。

末尾・paired dev・source勾配診断を実完了（2026-10-06 JST）: 最新境界はBaseだけの学習/評価/採用を完了して通知・停止、Chat/Dialogue/SFT/量子化なし。前turn73cf116は元Web保持100M・全80を完了して不採用まで進めたprogress。本turnもBase未完了を保持し、既存評価だけのCPU診断を0.053秒で完了（新GPU/学習0）。元Web保持のbase-070の末尾は「楓」のUTF8 e6a5がtoken上限64で切れたもの、内部不正byte0、他2重みも80/80 valid。既存text_display/WebUIはこのcap-tailを非表示にしraw failureを保持する処理が既にあり、新Tokenizer/文字変換・過去Unicode採点の消去は不要。同256文/472055bytesのうち234文でBPB改善、全4文長quartileでも改善、pooled差-.03536746。gold EOS NLLは全quartileでselected-Webより悪化、親より改善。BPB保持と自由生成を混同しない。

既存Japanese96反転familyの両正答（各16）はselected-Web→original-Web保持で否定16→16/比較1→0/照応0→0/数量0→6/時刻2→0/因果11→1。条件理解の弱さは末尾表示問題ではない。root結果はbase_retention_endpoint_diagnostic.json、固定raw IDs/bytesと全256paired NLL/bytes・全96familyを保存、保護testなし。

単一read-only勾配比較を原論文Gradient Surgery for Multi-Task Learning（https://papers.nips.cc/paper/2020/hash/3fe78a8acf5fda99de95303940a2420c-Abstract.html）に照らして事前定義。fixed seed2026100641、train4source×4batches×8×1024を両実parent10B/retention100Mへ同一入力し、fullCE/EOS CEからbody gradientを分解。元AdamWのmoments・bias correction・clip1・decay groupを使う仮想75/5/10/10方向の一次損失変化も算出、optimizerは作成/更新しない。分解と実CPU AdamW2group更新との一致/非破壊・UTF8/byte分母を含む4tests/2.03秒、PS構文/preflight成功。actual560871/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14495919は実終了・complete、GPU3.338秒<120、全weights unchanged/no parameter grads/RNG restored。fullCE採点259570/EOS2574は学習教師0と別会計。

両重みとも事前cosine<=-.05が3/4batch以上、またはAdamW一次損失上昇3/4以上のmarkerは未達。parentのWeb-vs-conditionで1/4だけ負、それ以外0、仮想AdamW上昇は全source0/4。従ってPCGrad/勾配補正は導入しない。小さいtrain assayでcurvatureや実finite-step害を測っておらず、全学習で衝突がない証明にも使わない。固定batch平均conditional fullCEは3.124300→.206272、EOS CE6.801157→.00014084で、教材の完結位置へのfitは強い一方、既存自由生成EOS34/一貫性12（各80）は未達。この差から学習量に伴う一般化の低下を次の一比較で調べる。

28text/1709698bytes、gzip266072bytes/SHA2ce3fc94a45c60c1e4cee7e064400a1afcffff976cdc7cf3d4bb1ba066ad3b7d、全Windows entry/archive raw SHA一致。base_source_diagnostics_completion.json・evidence_manifest.jsonが終端記録。元10B UI560936/同boot/start14496749の実ps/HTTP親410f975d…/10,000,007,168/busy=falseへ復帰、科学GPUjob0。新学習/最終seed/full/test/採用0、旧数値7失敗・全品質条件保持、PythonはWSL uv3.12.7、local commitのみ・pushなし。

次はearly_exposure_comparison_proposal.json。既存100M軌跡の最初の保存250updates/update305426/8,150,782教師・8,192,000input/CP SHA f6ba0fd4e7a24699f5c01d304f1e178b31bf40cbbe7d4eac960da82085fc6a14を実CPU inventoryで固定、100M終端との比較。候補の結果を見る前に最初の保存点と決め、残checkpointを都合よく走査しない。新学習0、新GPU上限450秒で同byte256/日本語/80個別内容・同128bridge/旧128retentionと同fixed train full/body/EOS CEをread-onlyで測る案。元relative/absolute/Web1%を保ち、失敗なら候補不採用、基準緩和/自動延長/新template・ratio・weight sweepなし。新evaluator/reviewerは未実装・GPU未開始、まず実装/関連check/preflightしてから起動する。inventoryの初回one-offはsrc import path不足で失敗し、src/scriptsを明示して修正、fallback PythonやGPU更新なし。以下は過去の履歴。

元Web保持100M・全80・元採否を完了、Base品質未達（2026-10-06 JST）: 最新ユーザー境界は品質・独立学習seed・full dev・protected test・採用までBaseのみ、実完了を通知して停止。Chat/Dialogue/SFT/量子化なし。actual556494/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14397590はcomplete・実ps不在。元10B-input親410f975d…から元Web75M＋同story5M/ordinary10M/relation10Mの科学100,000,000教師/100,532,224入力/3068updatesを実完了。学習159.041秒、科学GPU251.837秒＋検証16.540秒=268.377秒<900。CUDA全32保存再開/history/finite checksに合格した40検証更新/1,304,156教師は科学別。元Adam/LR.0002/weight1・実Web親cursor73421blocks分継続、短source3の最終cursor/教師/EOS/input/bytes/focusは完了対照と全一致。途中heartbeat99,765,470ではなく完了checkpoint100Mが正。

同byte256/472055bytes・日本語192/331/1119・全80を個別読解し同id/prefix/text/stopの旧1件だけ評点・理由再利用。非blind Codex判断で独立人間なし。selected-Web relation→original-Web保持はBPB1.026304→.990936、文法2=68→72/関連2=73→68/一貫性2=9→12/適切27→26/EOS48→34/自動反復20→21/Unicode0→1（各80）、role/empty0。意味64.063→59.896%、JBLiMP76.435→75.529%、JCQA35.210→35.567%。一貫性+3/paired95%CI[-.0625,.1375]で事前+8/CI条件未達、絶対一貫性27・適切27・EOS37・反復18以下と歴史Web1%/無Unicode条件も未達。候補不採用・Base未完了、seed/full/test未実施。BPB保持は改善したが文章品質の問題を解決したとはしない。

同128bridgeのsumLL両条件正答は76→57/128、語彙57→55/64・新文型19→2/64。旧128retentionは64→60/128、語彙46→42・旧構造18→18。原10B親と対照は正確cached結果を再利用し追加GPU/教師0。共有generator局所probeは独立自然文品質でなく、旧構造は学習recipeと重なる。Web材料/順序/長さ/EOS分布が同時に変わり、EOSだけや教材量だけの唯一原因を証明しない。

終端/採否はoriginal_web_retention_comparison_completion.json・review.json。275text/13,396,430bytes、gzip2,924,494bytes/SHA49bab30b94dbc641dae02648f3891f5cd0b7fa82e2764b8fb8931dfc66af1c26、全Windows entry/archive raw SHA一致。full model/Adam等はnative original_web/training/checkpoint-00308244.pt/SHAf54ea3fc23086de65bc00cd3f3f3a88f697a543a48c76647a4a66341ab3b2eb0へ保持。元10B UI557554の実ps・boot/startとHTTP親410f975d…/10,000,007,168/busy=falseへ復帰、科学GPUjob0。identity one-offの最初はscripts import path不足で失敗したがpathを明示して修正、新GPU/source/評価改変なし。

次はbase_retention_endpoint_diagnostic_proposal.jsonの単一CPU30秒/新GPU0/教師0診断。既存生成ID/bytesから1件の置換文字が末尾未完UTF8か内部破損かを調べ、同256文のpaired byte-weighted BPBを固定文長quartileで分解、既存Japanese192反転familyの失敗を再集計する。raw採点は変更せず、末尾表示修正をモデル一貫性の改善へ数えない。案は未実装/未開始、根拠から次の修正/比較を一つ定義する。Chat/量子化・自動長期延長・template/weight/ratio総当たり・基準緩和/pushなし。旧数値7失敗/全品質条件保持、PythonはWSL uv3.12.7。以下は過去の履歴。

元Web保持比較を準備・実CUDA検証完了、本学習中（2026-10-06 JST）: 最新ユーザー指示どおり、品質・独立学習seed・full dev・protected test・採用までBaseのみ進め、実完了を知らせて停止する。Chat/Dialogue/SFT/量子化は開始しない。元Web対選別WebのCPU診断はactual555746/CPU3.406秒で完了、新GPU/教師0。固定256 blocksのEOS/教師は元573/261571=.2191%、選別2312/259832=.8898%（約4.061倍）。sampling単位が異なりEOS間長さはblock端でcensored。全320生成とaccepted教材の連続24-token body spanはparent/Web0、curriculum/relation各2/80のみ、いずれも既存一貫性2。全文コピー/漏洩やEOSの唯一原因を証明しない。13GBindex再parse/global照合なし。診断8text/864957bytes、gzip68652bytes/SHAfa9c0aecade9f42f867f47a2e3dbd3ef16d60fa25aca1fdd7c6928aa6b0548ae、全Windows raw SHA一致。

単一次条件をoriginal_web_retention_comparison_proposal.jsonへ固定。元10B-input親410f975d…/actualLR.0002・元Adam/RNG/同shapeから100M、Web75Mを元12.225B shards＋実親BlockSampler cursorへ戻し、story5M/ordinary10M/relation10Mは同fresh42/同教師列を維持する。完了mature relation100Mを対照として再利用し再学習/再評価しない。Web材料/順序/長さ/EOS分布が同時に変わり純粋なEOS因果ではない。新trainer/runner/durable launcher/全80reviewerを実装、元3短sourceの入力・教師・最終cursor同一とCPU全state保存再開を含む4tests/1.65秒・PS構文成功。旧凍結sourceを変更しない。

probe actual556073/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14394437は実終了・complete、CUDA連続4対2+2の全32state/history/finite checksと32timingに合格。40検証更新の教師はprobe結果へ科学別保存、GPU16.540秒。実step.112410秒、100M予測学習348.371秒、30%余裕＋dev300秒＋局所128s50秒で802.882秒、probe込み819.423秒<900を確認して凍結。science config SHA5d7d10c7d5ed14a14da372cade700eb429601bd4413967a669400d3507209de3、probe SHA8e95a0ff31740789a61fc73d533d64931b35d6cf3e944137fe041abd8458e600。準備127text/1536940bytes、gzip473888/SHA85dc03a790b4381a08cb942cb1cfc8d587f2e727a1ca1e9303b33a3029f96763、全Windows raw SHA一致。

Windowsworker35384/actual556494/同boot/start14397590を実ps確認しWSL uv Python3.12.7で本学習開始、GPU91%/VRAM7705MiBを確認。run reports/phase6/original-web-retention-comparison-20261006、restart scripts/run_original_web_retention_comparison.ps1 -Mode Train -Worker。更新済みmodel/Adam/scheduler/RNG/Web実cursor/短source全cursor/会計/digestを250updatesごと永続保存、重複live jobは拒否。元10B UIは科学中停止しwrapper finallyで復帰。旧相対一貫性+8/pairedCIと絶対/歴史Web1%条件を維持、Base未採用・seed/full/test未実施。次は実100M終端→同byte256/472055bytes・日本語192/331/1119・80全文個別判断＋新128bridge/旧128retention→元採否→可搬証拠/local commit。合格候補だけ最終Base検証へ進む。自動長期延長/weight・template・ratio総当たり/品質基準緩和/pushなし。以下は過去の履歴。

元10B-input親からの同100M×3比較・全320内容を完了、不採用・Base未完了（2026-10-06 JST）: 最新ユーザー境界は品質・独立学習seed・full dev・protectedtest・採用までBaseのみ、実完了を知らせて停止する。Chat/Dialogue/SFT/量子化は開始しない。前turn4c1c9a2で実装/CPU7tests/実CUDA3arm各全32state/history/finite checksを保存。actual547862/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14186019はcomplete・実ps不在。Web/curriculum/relation各100,000,000教師、入力100,892,672/101,023,744/101,023,744、学習152.052/151.924/151.686秒、科学計300M。実GPU780.330＋検証32.739=813.069秒<2400、検証120updates/3,894,822教師は科学別。親model/Adam/RNG・actualLR.0002/weight1・同shapeを保ち、zero sourceの教師/入力/EOS/bytes/focus0と全completed-update state/accounting/元3source auditを終端reviewで確認した。途中heartbeat99,923,211でなく完了checkpoint100Mを各armの正とし、終了jobを再開しない。

parent read-only＋3armの同256/472055bytes・日本語192/331/1119・各原80/全320を個別読解しraw SHA付きnotesを保存。exact id/prefix/text/stopの旧/peer notesはparent0/Web3/curriculum5/relation23件を評点と理由ごと保持。非blind Codex判定、独立人間なし。parent/Web/curriculum/relationのBPB=.985891/1.019270/1.026259/1.026304、文法2=48/49/65/68、関連2=67/70/73/73、一貫性2=0/9/11/9、適切完結0/30/34/27、EOS0/45/47/48、自動反復53/30/24/20（各80）、Unicode/role/empty全0。Web-onlyでもEOSは改善し、条件教材だけの効果とはしない。意味59.375/58.333/56.250/64.063%、JBLiMP74.622/76.133/75.227/76.435%、JCQA30.384/31.814/34.718/35.210%。

事前primaryのcurriculum-vs-Webは一貫性+2/paired95%CI[-.075,.125]、relation-vs-Webは0/CI[-.1,.1]でともに相対改善未達。secondary relation-vs-curriculumは-2/CI[-.0875,.0375]。絶対一貫性27/反復18以下と歴史Web BPB.971570の1%保持条件を満たさず全候補不採用。EOS・文法・選択式や局所probeの改善だけでBaseを採用しない。独立seed/full dev/protectedtestは合格候補が出るまで未実施、Base未完了。

新relation128橋渡し（共有generator）sumLL両条件正答はparent23/Web21/curriculum9/relation76、語彙15/13/9/57・新文型8/8/0/19（各64）。旧128retentionは22/21/74/64、語彙15/16/51/46・旧構造7/5/23/18。旧構造はrelation recipeと重なり、新held-out一般化とは呼ばない。追加GPU/教師0の固定dev96反転familyの両正答（各16）はparent→Web→curriculum→relationで否定16→7→0→16、比較0→1→0→1、照応2→5→0→0、数量5→3→3→0、時刻0→0→1→2、因果0→2→13→11。成熟親は元々否定16/16で、relation16を新たに獲得した能力と呼ばない。条件切替に伴う保持の低下と局所転移を分け、旧2B親との比較は教材/順序も違う記述に留める。

終端はmature_base_condition_comparison_completion.json・review.json、追加CPU集計はmature_base_condition_pair_analysis.json。442files/34,493,393bytes、gzip7,343,113bytes/SHAbc05ddecc1422c7f8595cead67de97e8272ea8b228689f82922964612b70a0c8、全Windows entry/archive raw SHA一致確認、full optimizer checkpointはnativeのみ保持。元10B UI549723/同boot/start14264544の実psとHTTP親SHA410f975d…/10,000,007,168/busy=falseへ復帰を確認、科学GPUjob0。peer notes再利用をpostprocessingへ追加して同一文のrubric driftを防いだが、凍結科学sourceは変更していない。

次はmature_base_distribution_diagnostic_proposal.jsonの単一CPU30秒/新GPU0/学習0診断。元親Webと選別Webの固定sample token blocksでEOS/長さ/教師分布を比較し、全320生成IDとaccepted条件train文の連続24-token span一致を集計する。compact cacheを再利用し13GBindex再parse/global照合なし。共通定型句の一致を全文コピー/漏洩/因果の証明にはせず、元材料と現在材料の違い・保持低下の仮説を調べる。案は未実装/未開始、CPU診断の根拠から一つの保持/生成比較を事前定義してからGPUを使い、これ以上のtemplate/weight/ratio総当たり・自動長期延長・品質基準緩和はしない。旧数値7失敗/全品質基準保持、PythonはWSL uv3.12.7、local commitのみ・pushなし。以下は過去の履歴。

元10B-input Baseからの3条件比較を実装・実CUDA検証完了、本学習中（2026-10-06 JST）: 最新ユーザー指示を保持し、品質・独立学習seed・full dev・protectedtest・採用までBaseだけを進め、実完了を知らせて停止する。Chat/Dialogue/SFT/量子化は開始しない。既存4streamは全quota正を要求するため、過去の凍結trainerを変えずmature_condition_trainer.pyにzero-capable sampler/fullstate forkを追加。Web-onlyのゼロsourceはstream自体を作らず教師/EOS/入力/bytes/focusを0に保持する。Web末尾masked padding入力を実会計し、継続4対2+2で全state/Adam/RNG/履歴一致、source改変拒否などCPU7tests/1.71秒・PS構文/actual parent preflight成功。

実CUDA probe actual547502/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14181067はcomplete・終了。Web/curriculum/relation各全32state/history/finite checksと各32timingに合格、検証120updates/教師はprobe結果のverification_teacher_tokensへ別保存、実GPU32.739秒。stepはWeb.051386/curriculum.050850/relation.048386秒、各100Mの予測学習162.590/160.546/152.766秒。学習30%余裕＋parent/3評価1200秒＋局所bridge/retention100秒で科学1918.673秒、probe込み1951.412秒<2400を確認して凍結。science config SHA9ffffb298af3f4a404c1d2c63eda044ff9036772680ba0f5d77048cf45f123fb、probe SHA7c2cc1daa986cbe9b4862f40b5cd120cfcf04945dcc288f8ef8ec229dffae077。これら検証重みは科学に使わない。

Windowsworker32956/actual547862/同boot/start14186019を実psとjobで確認、本流Web約42.878M/100M教師・有限loss2.719893で進行。RTX4090 GPU90%/VRAM7703MiBを実確認、WSL native diskとuv Python3.12.7。親は元10B-input checkpoint410f975d…（教師9,978,838,479/入力10,000,007,168/actualLR.0002）、同model/Adam/RNG・constantLR/weight1で各100M、合計科学300M。accepted curriculum2048/relation684表現変更と元2B pool/compact cacheを再利用し新教材0・13GBindex再parse/global重複検証なし。completed updateごとのmodel/Adam/scheduler/RNG/source cursor/全教師・入力・bytes/digestsを250updatesごと保存し、job.jsonの実PID/boot/start/log/checkpointを再開前に確認する。restartはscripts/run_mature_base_condition_comparison.ps1 -Mode Train -Worker、実live/complete jobを重複起動しない。初期status setupでもstageと教師増加を確認して稼働を判断する。

all320 reviewerと固定byte256/472055bytes・日本語192/331/1119・parent read-only＋3arm評価・bridge128/旧128retentionを先に実装。事前primaryはcurriculum-vs-Webとrelation-vs-Web、relation-vs-curriculumはsecondary。旧相対/絶対/歴史Web1%条件を保持し、旧2B親との違いを純粋な学習量の因果へ代入しない。本科学終端/全320個別内容/採否はまだ未完了、Base未採用・独立seed/full/test未実施。127files/2,434,835bytesの準備のみarchive696,201bytes/SHA0a08bfd940917a4f9c887fd4a6e5a1f3f20fb15e6bc727a03376f925b5948b3aを保存、Windows archive SHAと76 copied evidence entryのraw SHA一致確認、checkpoint tensorsはnativeのみ。mature_base_condition_preparation.json・preparation_manifest.json・active_job.jsonが可搬記録。科学中UI停止、wrapper finallyで元10B UIへ復帰する。

次は同jobの各100M/parent+3dev終端確認→全320 raw-bound notes（exact旧文だけ評点/理由再利用）→review_mature_base_condition_comparison.pyで事前採否→portable終端/commit。合格候補だけ独立seed/full dev/protectedtest/採用へ進み、Base実完了を知らせて停止する。旧数値7失敗/全品質基準維持、local commitのみ・pushなし。以下は過去の履歴。

否定・比較の言語橋渡し同100M・全80完了、Base品質未達（2026-10-06 JST）: 前turnはf4a5de6で生成条件文同100Mを完了。本turnは準備/実GPU gate/永続launchを207c985へ保存し、actual542850/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14044573の同100Mを完了・実ps不在。科学100,000,000教師/101,023,744入力/3083更新、学習152.454秒、GPU236.899＋検証12.121=249.020秒<900。検証40updates/1,297,767教師は科学別。元Adam/scheduler/RNG/sampler/counters・LR.0002/weight1・元3教師列一致・全32CUDA state/history/finite checks成功。heartbeat99,923,211は途中値で完了checkpoint100Mを正とし、終了jobは再開しない。

同byte256/472055bytes・日本語192/331/1119・新80全文を個別読解し、同id/prefix/text/stopの旧19件の評点と理由を保持。非blind Codex判定で独立人間なし。生成curriculum→relationはBPB1.130250→1.130382、文法60→60/関連68→68/一貫性14→10/適切27→21/EOS45→35/反復17→21（各80）、Unicode/role/empty0。意味53.125→60.417%、JBLiMP78.852→78.550%、JCQA28.686→29.535%。一貫性差-4/paired95%CI[-.125,.025]、相対・絶対一貫性27/完結27/EOS37/反復18以下と元Web1%条件未達。候補不採用・Base未完了。選択式改善だけで自然な続きを生成できたとしない。

新relation128反転family×parent/control/newのsumLL両条件正答7→29→50/128。control→newの語彙holdout11→32/64、文型holdout18→18/64で未知文型の両正答数は増えない。旧128retentionはcontrol63→new45/128、control/parentはcached scoreを厳密bindingで再利用。旧caseの構造holdoutは新recipeで学習する表現との重なりがあり、新たな構造一般化の証明には使わない。追加GPU/教師0の元dev96反転family再集計はcontrol→newで否定0→12/比較0→0/照応1→1/数量1→3/時刻1→1/因果9→6（各16）。否定の改善と一般の文脈保持・生成品質を区別する。

終端/採否はreports/phase6/condition_relation_comparison_completion.json・review.json。265text/16,226,705bytes、gzip3,287,540bytes/SHA3c34a34182648d8aa030032f84c2ca8ccb08f7ffbc46411d8d6c39e78df9f7e1、全entry/archive raw SHA一致。full optimizer等はnative relation/training/checkpoint-00065249.pt/SHA3be130e6e99ea0e1dc366615409a1ff8e9741ab623ea61a5580b952a81ac319aへ保持。元10B UI543802/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14068785のps/boot/start・HTTP親SHA410f975d…/10,000,007,168tokens/busy=falseを確認。現在科学GPUjob0。

追加GPU0/CPU0.292秒の実parent inventoryで、今の2B教材親は2.037B input/2.020B教師/actualLR.0002、元Web10B親は10,000,007,168 input/9,978,838,479教師/actualLR.0002・同10M形状/fullstateを確認。歴史Web保持参照BPB0.971570のcheckpointは10.500B input/10.478B教師/actualLR.00001で別物、EOS0/反復62と文章生成の弱さも保持する。初回はevaluationにcheckpoint pathがあると誤認しKeyErrorとなったが、実training resultから対応pathを引き、評価SHAと実CP SHAを一致確認して修正。fallback CP/新GPU/品質改変なし。このinventoryはcheckpoint会計で新品質や因果の証明ではない。

次の単一study案はmature_base_condition_comparison_proposal.json。これ以上のtemplate/weight総当たりをせず、元10B-input親から同actualLR.0002/元Adam・RNG/同shapeで各100MのWeb-only・現curriculum・relationを比較する。科学計300M、accepted source/compact cache/旧ID・事実を再利用、新教材・Tokenizer準備なし。parentのread-only同評価も合わせ原80各/全320・byte・日本語と元relative/absolute/Web1%を測る。curriculum/relation間は元3教師列同一、Web-onlyは25MをWebへ戻すmixture対照と明記。過去2B親との違いは学習量とデータ/順序も違い、単純な量の因果とはしない。

案は未実装/未凍結/新GPU0。関連CPU/parent source compatibility→各実CUDA連続4対2+2/finite/32timing/save→30%余裕/4評価・probe込み新GPU2400秒以内へ凍結→各100M/all320/事前比較/元採否→証拠/commit、という完了条件。古い2B timingを10B親の実測へ代用しない。元10B親のEOS/自由生成品質は既存正確cacheがなければ一度だけ測り、未確認の強さを前提にしない。独立seed/full dev/protectedtest/採用は合格候補が出るまで未実施、Base実完了を知らせて停止する。Chat/Dialogue/SFT/量子化なし、旧数値7失敗/全品質基準保持、PythonはWSL uv3.12.7・local commitのみ・pushなし。以下の実行中記録は履歴で、今回完了を優先する。

否定・比較の言語橋渡し教材を準備・全64採否、同100Mを実学習中（2026-10-06 JST）: 前turnは同100M/all80/採否をf4a5de6に保存したprogress。本turnも最新境界のBaseのみ継続、Chat/Dialogue/SFT/量子化なし。accepted V2の元2048文/1024family/24構造/事実・正解・IDを保ち、否定の自然な述語と長短の関係文684文だけ置換した。残4種類1364文の全文はbyte exact。比較では二本の数値長を無名の組で保持し、数値を人へ直接割り当てず長短の関係を読む条件にした。長さ/EOS密度/語彙も変わる教材置換で唯一原因や容量限界の証明ではない。公開corpus追加0、old128はretentionとして保持し新recipeの構造holdoutと呼び直さない。

actual541694/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14018983はCPU0.382秒で完了・ps不在。body85,350tokens/330,943bytes、serialized89,446/fullCE87,398/EOS2048/focus12,302、manifest SHA154f13da4a817aaa21586fba2cd335faea7c79358be410e73166f5d0052bf936。固定first64全文を個別読解し、同全文42件は旧notesを保持、変更22件を新全文で判定。weak0/未解決文法0でaccepted。新128は否定64/比較64、語彙holdout64/文型holdout64を学習前分離し同candidate bytes/IDsを保持。4CPU source tests1.16秒・4trainer/budget/transfer/scope tests2.09秒/PS構文成功。元3streamの同100M教師列SHA・数/EOS/bodybytesをCPU6.479秒で一度再生し全一致、元compact cacheを再利用し13GB再scan/global照合なし。

actual542467は実CUDA連続4対2+2の全32state/history/finite checks一致、32連続timingもfirst4 trajectory一致。検証40updates/1,297,767教師は科学別、重みは捨てる。実GPU12.121秒、steady0.049021秒/32443.781教師、3083更新/保存warmup込み学習155.003秒。30%余裕/原評価300秒/新3重みprobeとretention50秒込み科学551.503秒、検証込み563.625秒<900を確認して凍結。scienceconfig SHA248651b0c7a25b3ab9950fce40f0e40a57b21a386201cf47c87eef4717911fac、probe SHA cbb902115f79963ffb1e68c5fd6babb68cde76957adf0f779280dc23143ed07d。

Windows33484/actual542850/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14044573を実ps確認、科学約42M/100M教師/loss2.457045有限・GPU89%/VRAM7705MiBで進行。元2B+20M親/Adam・RNG/LR.0002/weight1/元3教師列/同100Mを保持し完成生成control100M/全80を厳密bindingで再利用する。新科学100Mと比較計200Mを分け、普通Web75M/story5M/通常10M/条件10M。completed updateのmodel/Adam/scheduler/RNG/sampler/教師/入力/履歴・checkpoint250をWSL永続保存。restartはcondition_relation_active_job.jsonのscripts/run_condition_relation_comparison.ps1 -Mode Train -Worker。live/complete jobを重複起動しない。

準備完了/可搬証拠はcondition_relation_language_preparation_completion.json・preparation_manifest.json。28files/13,463,630bytes、gzip1,770,578bytes/SHA4a768f9037cc458fe43ad0dae9e031642a7136c65b14be14b511e6a391f23fcb、全entry/archive raw SHA一致確認。dataset arraysは含めfull optimizer tensorsは含めない。これは教材準備の証拠で今回の科学100M・文章品質はまだ未完了。元10B UIは科学中停止しfinallyで元親SHA410f975d…へ復帰する。

次は同job終端・新dev256/472055bytes・日本語192/331/1119・新80全内容、parent/control/new各新128とnew重み旧128保持を実評価し、cached control/parent retentionを再評価しない。元relative/absolute/originalWeb1%条件を維持、独立人手なしの生成probeをBase採用へ代入しない。originalWeb参照BPB0.971570は同256の実DocID/token/bytes一致を確認した歴史10B armで、100Mの等予算対照とは別の最終保持条件として残す。合格Base候補だけ独立学習seed/full dev/protectedtest/採用へ進め、実完了を知らせて停止する。旧数値7失敗/全品質基準保持、PythonはWSL uv3.12.7、local commitのみ・pushなし。以下の記録は当時の履歴。

生成条件教材の同100M比較・全80内容完了、Base品質未達（2026-10-06 JST）: 最新ユーザー境界はBaseのみ、実品質/独立学習seed/full dev/protectedtest/採用を満たした時点で知らせて停止する。Chat/Dialogue/SFT/量子化を開始しない。actual538399/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13931364はcomplete・実ps不在。accepted V2生成2048文を同2B+20M親/元Adam・RNG/LR.0002/weight1から100,000,000教師/101,023,744入力/3083更新、学習152.968秒で完了。自然2048の100M/全80を厳密bindingで対照再利用、新科学100Mと比較計200Mを分ける。実GPU236.227＋検証13.409=249.636秒<900、実CUDA全32state/history/finite checks・元3教師列/数/EOS/bodybytes一致・関連CPU4tests2.74秒成功。heartbeat99,914,563でなく完了checkpointの100Mを正とし、終了jobを再開しない。

同byte256/472055bytes・日本語192/331/1119・新80全文を個別読解、同id/prefix/text/stopの旧11件は評点と理由を保持。非blind Codex判定、独立人間なし。自然対生成はBPB1.136866→1.130250、文法62→60/関連74→68/一貫性12→14/適切30→27/EOS42→45/反復20→17（各80）、Unicode/role/empty0。意味50.521→53.125%、JBLiMP78.550→78.852%、JCQA29.803→28.686%。一貫性差+2/paired95%CI[-.05,.1]、相対+8/下限正と絶対一貫性27、元Web BPB1%条件を満たさず候補不採用・Base未完了。EOSと反復の改善だけでBaseを採用しない。

同generator128反転family×3重み/1536requests完了、sumLL両条件正答はparent5→自然7→生成63/128、語彙holdout4→4→43/64・構造holdout1→3→20/64。これは局所条件転移の改善で独立自然文品質の証明ではなく、構造holdoutはAND/OR・値域も同時に違う。追加GPU/教師0の元dev96反転family再集計は自然→生成で否定0→0/比較0→0/照応0→1/数量2→1/時刻1→1/因果1→9（各16）。因果の改善を否定・比較や総合文脈保持の改善へ代入しない。

終端/採否はreports/phase6/condition_transfer_comparison_completion.json・review.json。219text/13,217,315bytes、gzip2,929,870bytes/SHAfb38c31a81c18ab83d4a66a44ccb8f55beb7fd2964ecb2b53f8dbce31656ea77、全entry/archive raw SHA一致確認。full optimizer checkpointはnative curriculum/training/checkpoint-00065249.pt/SHAbe7121f6a0b1e60bbf6e7b254ce4b7b4debb1b658cb572874eb791b526a57a2eへ保持。元10B UI538886/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13955495の実ps/boot/startとHTTP元SHA410f975d…/10,000,007,168tokens/busy=falseへ復帰を確認、現在科学GPUjob0。

次の単一比較案はreports/phase6/condition_relation_language_proposal.json。記録された動作の言い直し/数値長さ比較から、否定の自然な述語と長短の関係文への言語橋渡しを仮説とし、生成2048の否定・比較表現だけを変更する。残4種類全文/元3stream/同親・Adam/LR/weight1/同100Mを保持して完成生成100M対照を再利用する。局所状態/反転正解を保ち、dev文/名前/templateは学習に流用しない。CPU240秒/固定64全内容・未解決文法を拒否→新実CUDA再開/finite/timingと検証込み900秒へ凍結→新100M/元80・byte・日本語/旧128保持＋新128→元quality/Web採否、という完了条件。案は未実装/未準備/未凍結/新GPU0。長さ/EOS/語彙変化を含む教材置換で単一構文因果や唯一原因/10M容量限界の証明としない。

無根拠の長期延長/weight・比率総当たり・巨大index再scan・基準緩和をしない。合格Base候補のみ独立seed/full dev/保護test/採用へ進め、実完了を知らせ停止する。旧数値7失敗/全品質基準を保持、PythonはWSL uv3.12.7、意味あるlocal commitのみ・pushなし。以下の実行中記録は当時の履歴で、今回の完了記録を優先する。

生成条件文2048対自然原文2048の同100M比較を実GPU学習中（2026-10-06 JST）: 前turnはaccepted V2教材/全64/元教師列/776c644を保存したprogress。本turnは実行・永続PS・raw-bound reviewerを接続し、CPUfullstate連続4対2+2/転移family/実測予算/後段拒否4tests2.74秒とPS構文成功。元自然2048の100M/全80/日本語を厳密binding確認して再利用、対照GPUの再学習/再評価はしない。
actual537993/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13926269は終了・ps不在、実CUDA連続4対2+2の全32state/history/有限値checks一致。32連続timingのfirst4 trajectoryも一致、検証40updates/1,297,661教師は科学別で重みを捨てる。検証GPU13.409秒、steady .053744秒/32441.156教師・3083更新、保存/warmup込み学習169.536秒見込み。30%余裕/元dev評価300秒/3重み×128転移40秒込み560.397秒、検証込み573.806秒が900秒以内であることを確認して凍結した。
scienceconfig SHAca4422521d43a59a287de954a5f9bef58edc66f60a1df32313d6abdf7154015b、probe SHAa57cfaa1ab789f7639c39d280eb809b69971793539c9c550a7002fb53b8fa8f2。Windows33572/actual538399/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13931364を実ps確認、新約78.50M/100M教師/loss2.397426有限で継続、GPU90%/VRAM7703MiBを観測。completed-updateの元Adam/scheduler/RNG/sampler/counters/latest/checkpoint250/logをWSLへ永続保存。native run condition-transfer-comparison-20261006、正確なrestartはcondition_transfer_active_job.jsonのscripts/run_condition_transfer_comparison.ps1 -Mode Train -Worker。live/complete jobを重複起動しない。元10B UIはjob中停止しfinallyで復帰する。
同親2B+20M/Adam・RNG継承/LR.0002/weight1/full body+EOS・各Web75M/story5M/通常10M/条件10M・同100Mを固定。新科学100M＋既存対照100Mを区別する。短いローカル教材への置換でEOS密度/長さ/語彙分布も変わるため量だけの因果としない。新dev256/472055bytes・日本語192/331/1119・生成全80と、parent/natural/curriculumの同128generator probe全1536requestsはこれから。新全80は個別読解し、同id/prefix/text/stopは旧評点を保持、元relative/absolute/originalWeb条件を監査する。追加GPU0の旧dev反転family再集計も別sourceSHA付きobserverを用意した。
Base未完了/未採用、Chat/Dialogue/SFT/量子化は開始しない。合格候補のみ独立学習seed/full dev/protectedtest/採用へ進め、実完了を知らせて停止する。旧数値7失敗/全品質基準維持、PythonはWSL uv3.12.7、意味あるlocal commitのみ・pushなし。以下は当時の履歴。

条件文教材の実準備・固定64採否完了（2026-10-06 JST）: 前turnは両100M/全160/採否を389d73cに保存したprogress。本turnはBaseのみを継続し、同100Mの次比較用にローカル生成2048文/1024対family/24構造/6種類と、別128family（語彙holdout64/構造holdout64）を実準備した。公開datasetの新取得や2B原corpusの増量とはしない。既存Tokenizerを保持、PythonはすべてWSL uv3.12.7。GPU学習・検証は本turn0、Chat/量子化0。
初回CPU536045は0.276秒/240秒上限で終了・ps不在、本文82,127tokens/320,314bytesを準備。固定first64全文を個別読解し、negation-2の「その内容は、人物は…」という不自然な接続2文を記録した。元weak<=10自体は2で通るが、proposalが明示する未解決文法不良の除外条件を満たさずGPU教材には不採用。元V1原文・全notes・manifest・arrays・実sourceを保存、都合のよいpilot再抽選はしない。
観測した接続だけを「その記録によると、」へ修正する一改訂V2を実CPU536581/0.344秒で準備し終了・ps不在。影響はtrain86文のみで、元の人物/値/条件/答え/ID/選択順・128probeの事実と候補・seedを実比較で全保持、固定64のIDも同じ。変更2文を新全文で読み、同じ全文62件の評点を保持、弱0/文法不良0で受け入れた。関連V1 CPU4tests0.90秒、V2 CPU5tests1.04秒（6状態のliteral結果、24構造/分離・実codec/共通target/焦点byte、実stream再開、元V1との一修正だけ/labels改変拒否）とPS構文成功。初版testが受け取ったを加えたしか認めなかったassertion失敗XMLも保存し、書式ごとの正しいliteralへ修正した。学習や採用基準を緩めていない。
V2本文82,213tokens/321,088bytes、serialized86,309/fullCE84,261/EOS2048/focus12,302、元original corpusへの追加0。manifest SHAb5b9c44830b6910a9e247bd44f72a54224038dc1712b92b6d3465c80b58bd311、native data /home/aihub_ubuntu/jmicro-data/phase6/condition-transfer-curriculum-20261006-v2。actual tokenizer IDs/bodybytesを保持する生成専用CurriculumTrainViewを用意し、元原文用loaderのprovenanceやfrozen sourceは変更しない。literal旧dev80/192のcontextが教材にないことを限定CPU確認、protectedtestを開かず学習へ使わない。語彙/構造probeは同generatorの限定転移指標であり独立の自然文品質証明ではない。
prepare_condition_transfer_inputs.pyを実CPU6.372秒/30秒上限で実行し、100M予定streamを再生。前の自然2048対照と元Web/story/通常教材の全教師ID列SHA・教師数・EOS数・bodybytesが全一致、元compact cacheを使い13GB index再scanなし。新条件文の短さ/EOS密度/学習露出・row interleavingは異なり、この一比較をsource教材置換として扱う。新serialized量を100M学習量や公開corpusの新規量へ足さない。
終端/採否はcondition_source_transfer_preparation_completion.json、全内容はcondition_source_transfer_{v1,v2}_content_review.json。V1失敗とV2 accepted data arrays/元generator/全notes/tests/教師auditを51file/24,721,903bytesの可搬archiveへ保存。archive3,401,611bytes/SHA347a9d6b065db1760fd8352caf673357b9a302afe6a68888e4250804088f1d5c、全entry/archive rawSHA一致確認。元10B UI532868の実psとHTTP親SHA410f975d…/10,000,007,168tokens/busy=falseを保持、科学GPUjob0。
次は未実装のrun_condition_transfer_comparison.py/ps1とraw-bound reviewerを接続する。accepted V2対immutable自然2048/100M対照再利用、同親2B+20M/Adam・RNG/LR.0002/weight1/普通3教師列・同100M、CPUfullstate→実CUDA連続4対2+2/有限値/timing/save→probe込み900秒以内へ凍結して新100M/全80・元dev・3重み×128probeを実評価する。新科学config/実CUDA/新学習/品質は未達であり、教材準備やCPU fixtureをGPU・Base完成としない。元relative/absolute/Web基準、旧数値7失敗を保持、合格Base候補だけ独立seed/full dev/protectedtest/採用へ進め、実完了をユーザーへ知らせ停止する。Chat/Dialogue/SFT/量子化は開始しない。意味あるlocal commitのみ・pushなし。

条件教材512対2048の同100M比較完了・Base未達（2026-10-06 JST）: Baseのみ継続。actual532172/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13744085はcomplete・実ps不在、両100,000,000教師/100,859,904入力/3078更新をfullstateで監査した。科学計200M・新original corpus0、実GPU453.001秒＋検証21.030秒=474.031秒<1200。各CUDA連続4対2+2の全32checksと関連CPU5tests/2.17秒成功、普通3streamの教師ID/数/EOS/bodybytes一致。scienceのheartbeat99,436,065は途中観測で、終端100Mはcheckpointを正とする。両完成checkpoint・元Adam/scheduler/RNG/sampler/countersはWSL保持、終了jobを再開しない。
同byte256/472055bytes・日本語192/331/1119・生成全160を個別nonblind読解、同id/prefix/text/stopの旧評点はsmall17/large9件で保持した。512→2048はBPB1.133285→1.136866、文法56→62/関連59→74/一貫性13→12/適切31→30/EOS42→42/反復25→20（各80）、Unicode/role/empty0。意味52.083→50.521%、JBLiMP78.248→78.550%、JCQA29.893→29.803%。一貫性差-1/paired95%CI[-.1,.075]、元relative・absolute・originalWeb1% BPBの全条件未達。旧25M比も一貫性51215→13/204816→12で改善条件を満たさない。独立人間採点なし、旧25M末尾quota maskの違いを保ち同trajectory prefixや独立再現としない。
拡張2048側の元全文履歴source128で両結末選好7→90、旧64/新64のtargetNLL1.504358/1.578169→.627247/.657038へ改善したが、未知文の一貫性は改善しない。512側の既知旧64は51→63、未学習側の新64は3のまま。既定mean-token感度分析では2048両104/128、条件文だけprimary55/128。元結末は排他的hard negativeの認証がなく、これを真偽正答率へ置換しない。追加GPU/教師0の同dev96反転family再集計は両100Mで否定0/16・比較0/16、否定全16同候補のまま。単純な学習不足だけで未知文の問題を説明できず転移への対処が必要という所見であり、attention故障や10M容量限界の証明ではない。
reports/phase6/condition_source_learning_completion.json・review.jsonとcondition_source_learning_condition_pair_analysis.jsonへ終端/採否を保存。253text/23,732,258bytes、archive5,126,351bytes/SHA4f12e340b332d5de05ab4cff7861cb89d483954f4c79da83c200bb3dc33b70a9、全可搬entry/archive rawSHA一致確認。元10B UI532868/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13789884・実ps/GPU一覧/HTTP親SHA410f975d…/10,000,007,168tokens/busy=falseへ復帰。科学GPUjob0。
次の単一比較案はcondition_source_transfer_proposal.json。自然原文2048の100Mを厳密binding確認後に対照再利用し、新2048の短く独立した条件文教材を同100M/同親/元Adam・LR.0002/weight1/普通3streamで比較する。局所状態と算術・時刻・順序から結果を定義し、少なくとも24構造/6種類を語彙・値・順序と組み合わせる。旧64familyの記憶実験の反復やrenameだけの一般化主張を避け、新128の語彙・構造holdoutを事前分離する。eval文/テンプレートをtrainへ流用せず、合成ローカル教材を新公開corpusと呼ばない。source置換では長さ/EOS密度等も変わることを明記して量だけの因果としない。
この案は未実装/未準備/未凍結/新GPU0。まずCPU240秒の永続準備/固定first64全文・旧weak<=10採否→実CUDA再開/finite/timing/保存→probe込み900秒以内へ凍結→新100M/全80/元dev/新128→元品質採否という完了条件。意味ある学習へ進むため、13GB再scan・global照合・無根拠の長期延長やweight/比率総当たりはしない。失敗時に採用条件を緩めない。
Base未完了/未採用、独立学習seed/full dev/protectedtestは合格候補が出るまで未実施。合格候補だけ最終確認・採用へ進め、Baseの実完了をユーザーへ知らせ停止する。Chat/Dialogue/SFT/量子化は開始しない。旧数値7失敗と全品質基準維持、PythonはWSL uv3.12.7、local commitのみ・pushなし。以下の実行中記録は過去の履歴。

条件教材512対2048の同100M比較を実学習中（2026-10-06 JST）: 前goal turnは更新0 source選好/fit/exposure診断・34f5b25を完成したprogress。本turnは同100M両armのrunner/永続PS/reviewerを実装し、旧25M source/data/result/notes/configと旧診断sourceを変更せず元親から新学習計200Mを揃えた。新corpus0、既存compact cacheを使い13GB原index再scanなし。関連CPU5tests/2.17秒（両実trainerの連続4対2+2全state・wrong25M binding拒否、元3stream教師列、2評価/source128/saveを含む実測予算、原labelのみfit/弱subset、Base-only weight1）とCLI help/PS構文成功。
元3streamの実100M samplerをCPU9.889秒で両方再生し、全教師ID列SHA/教師数/EOS/bodybytesが一致、source subsetを再抽出しない。actual531809終了・ps不在、512/2048の実CUDA連続4対2+2は各全32checks一致、32連続timingはfirst4のtrajectoryも一致。検証80更新/2,599,760教師は科学別、検証重みを科学親へ使わない。GPU21.030秒、steady512 .049197/2048 .048646秒/更新、各3078updates見込み、学習見込み155.220/153.571秒。保存/warmup/30%余裕・2評価各300秒/source128計20秒込み1021.428秒、検証込み1042.458秒が新1200秒上限に収まることを確認して凍結。
科学config SHA c3f3b9d077a5a0c8f61ec16ff614488d5a6146e658141f771349d9e5e90d860e、probe SHA7570107ae0a45cb0bf7184264ce1d8744e06d590e81373f032fc7b017452d47b。Windows23392/actual532172/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13744085を実ps確認し永続稼働。small512は追加100,000,000教師/100,859,904入力/3078更新・実training152.387秒で終端65244/SHA83e63c29843482ede43f576c3026c1d3e5aabdca2baab64bbe26e80d38d34fc1を保存し、元dev/Japanese/生成へ進行。後半2048/両128source選好/新全160個別内容/品質採否はこれから。jobのstatus setupは初期label、完了checkpointとactual PID/heartbeat/stageで判断する。
同親2B+20M/元Adam・RNG/LR.0002/weight1/full body+EOS、各Web75M/story5M/通常10M/条件10Mを固定。科学1178.970秒＋probe21.030秒。completed updateの全optimizer/scheduler/RNG/sampler/counters/latest/metricsと正確なrestartはreports/phase6/condition_source_learning_active_job.json。actual不在かつ未完了の時だけscripts/run_condition_source_learning.ps1 -Mode Train -Worker、終わったjobやlive jobは再起動しない。元10B UIは科学job中停止し終端finallyで復帰。native disk空き217GiB確認、Windows側データ読み出しなし。
次は同job終端・元common-byte256/Japanese192・331・1119/新80各全160原文を個別判定し、同id/prefix/text/stopは元評点を保持、旧relative/absolute/original-Web全条件を監査する。旧25Mは別の学習量参照で新100M controlへ代用しない。source128で適合と条件選好を測るがhard-negative真偽や未知の品質へ置換しない。Base未採用/未完了、独立seed/full dev/protected test未実施。合格候補だけ最終Base検証→実完了報告で停止。Chat/Dialogue/SFT/量子化は開始しない。旧数値7失敗/全品質条件保持、PythonはWSL uv3.12.7、local commitのみ・pushなし。

条件ごとの元結末選好・学習文適合の実診断完了（2026-10-06 JST）: 前goal turnは同25M/全160/採否/732ca50を完成したprogress。本turnは固定旧64+新64trainと3実重みのread-only診断を実装・凍結・実GPU実行した。Baseのみ継続し、Chat/Dialogue/SFT/量子化は開始しない。actual529838/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13651414は完了・ps不在、GPU6.907秒・占有6.925秒<60、optimizer0/新科学教師0/新original corpus0。全文履歴/元の条件文だけ、128family×2branch×2元結末×2文脈×3重み=3072requestsを全保存・監査した。
元原文の両結末選好/128はparent2B/control512/large2048の順に、全文履歴4/54/7、条件文だけ10/32/15。全文履歴の同候補選択は82/57/96、元原文一致率35.156/64.453/42.969%。旧64だけの両選好は2/51/4、新64は2/3/3。token平均の感度分析でも旧64は4/56/8、新64は2/5/4で、単なる結末長の正規化だけで2048側の適合差は消えない。これは元文章にある続きの選好で、他の結末が意味的に不可能と認証した正答率ではない。条件文だけでは先行文脈と代名詞等の参照を除くため、attention因果・全文packingの一般的原因・10M容量限界の証明にしない。
元結末target NLLの旧64/new64はparent1.937802/2.059500、control512 0.504619/2.233557、large2048 1.504358/1.578169。対照は旧512側を強く適合させるが拡張側の旧/新はそこまで適合していない。条件source2.5M教師/元fullCE対象72,397・292,291から平均露出34.532・8.553回分を算出し、4倍教材に学習量を据え置いた条件の不足仮説を支持する局所所見とする。これは各docの正確なepochや唯一の原因、未知文の品質改善の保証ではない。CPU再集計のみで原巨大index/再学習/再評価はない。
元proposalの「native primary mean-token」という説明は実コードと異なったため、新凍結configでsum LLを既存native semanticsの主指標、mean-token/mean-byteを事前固定secondaryとして明記した。元proposal/sourceやBase採否基準を後から書き換えていない。元のprefix/outcomeを別encodeしてcommon target IDsとし全UTF8 bytesを保持、1024requests全部でjoint encodeと実際に一致（segmentation差0）。EOSの捏造/切捨て/評価文の学習混入なし。関連CPU4tests/0.926秒とPS構文成功、実CUDA重み不変/RNG復元/勾配なし/eval全3合格。first requestのbatch対single最大token NLL差は.036806/.061845/.049349として残し、旧数値7失敗の合格証拠へ置換しない。補助CPU集計コードの構文とportable manifest参照を修正し、実samplerが使ったnative data manifest SHAで成功、診断GPUの重複実行なし。
原結果/review/fit/実終了はreports/phase6/condition_source_ranking_{review,fit_analysis,completion}.json。212text/7,074,515bytes、archive1,239,660bytes/SHA5a965dca7b143cfd4a22580bd3440212b381920dad8ca778dc96cfad20149dab、全212可搬entry/archive raw SHA一致確認。原10B UI529910/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13652555とactual ps/boot/start/GPU process一覧、HTTP親SHA410f975d…/10,000,007,168tokens/busy=falseを確認。現在科学GPU job0、complete診断を再開しない。以下のlive/未実装は当時の履歴。
次はcondition_source_learning_100m_proposal.jsonを実装・検証する一度のmatched学習量比較。既存512/2048を同2B+20M親/継承Adam・RNG/LR0.0002・weight1・同shapeで各100M教師（新科学計200M、Web75M/story5M/通常10M/条件10M各）まで学習する案。新教材変換なし・元compact cacheを再利用し、実連続/再開・有限値・元3stream教師列・実timing/保存/評価と検証込み新GPU1200秒以内へ先に凍結する。旧25M実39.853秒×8、30%余裕＋2評価300秒から概算1014.468秒で、これは未測定の本レシピ予算ではない。現時点で100Mコマンド/凍結/実学習は未開始。
旧25M結果は学習量違いの文脈として再利用し、新100M対照へ代用しない。旧25M終端quota maskと100M前半は完全同一と保証しないため、元親から両条件を新たに同100Mで揃える。条件10Mなら露出概算512件側138.127、2048件側34.212回分。source128の結末選好/元target適合、共通dev256・472055bytes/日本語192・331・1119/各80全160内容を両方測り、train適合だけでは採用しない。元relative/absolute/original-Web条件不変、不合格から自動200M/500M延長・weight/比率総当たりをしない。適合改善でも未知devが改善しなければ転移/教材形の失敗を残し、次の一仮説を選ぶ。
Base未完了/未採用、独立学習seed/full dev/保護test未実施、旧数値7失敗・全品質基準を保持。合格Base候補だけ最終seed/full dev/protectedtest/採用へ進め、実完了をユーザーへ知らせて停止する。Chat/量子化は再開指示を待つ。PythonはWSL uv3.12.7、意味のあるlocal commitのみ・pushなし。

条件教材512対2048の同25M比較・全160内容完了（2026-10-06 JST）: Baseのみ継続し、Chat/Dialogue/SFT/量子化は開始しない。actual527392とprobe527011は終了・ps不在、科学25,000,000教師/25,231,360入力/770更新、GPU113.426秒＋検証11.799秒=125.226秒<900。対照512側の既存25Mと全80評価を完全binding確認の上で再利用し、比較計50Mと新科学25Mを分ける。検証40更新/1,299,890教師は科学別。元3streamの実教師ID列/教師数/EOS/bodybytesのCPU一致、実CUDA連続4対2+2の全32state/history/finite checks、関連CPU4tests/1.661秒・PS構文成功。巨大index再scanなし。
512対2048: BPB1.143559→1.140149、文法54→59/関連43→50/一貫性15→16/適切完結27→27/EOS44→42/反復26→23（各80）、Unicode/role/empty0。意味52.604→54.167%、JBLiMP79.154→79.154%、JCQA29.848→29.044%。新80全文を個別に読みraw SHA付き理由を保存し、同じid/prefix/text/stopの20件は旧評点・理由を保持してrubric driftを避けた。非blind Codex採点で独立人間ではない。一貫性差+1/paired95%CI[-.075,.1]、旧relative/absolute/original-Web全条件未達、両候補不採用・Base未完了。4倍は条件教材の文書数512→2048で、元corpusの2Bを8Bへ増やした結果ではなく新original corpus0。文法・反復の小改善を総合品質合格にしない。
同じ意味dev192/96反転familyを追加GPU・教師0で再集計。large2048の両条件正答/16は否定0・比較0・照応0・数量3・時刻2・因果5（対照0/0/0/3/3/2）。否定は両重みとも同候補16/16、正しい方向へのmargin変化16/16だが順位は反転しない。注意機構不動・Tokenizer故障・10M容量限界の証明ではない。元の固定train pilot64+64の内容annotationもCPU0.153秒だけ再集計。旧/新の否定14/12・数量32/17・時刻10/5・比較53/46・因果24/24・entity47/24（複数label可）。これらは全512/2048やコーパスのカテゴリ量、単純二値operatorへの十分な供給を証明しない。
実終端と採否はreports/phase6/condition_diversity_comparison_completion.json・review.json、可搬manifestはcondition_diversity_comparison_evidence_manifest.json。93text/6,503,493bytes、archive1,604,972bytes/SHA7538e4b14eadafabee446d92e99ab436b75a81a7a2d59e1682e7f9c1481976f3、全可搬entry/archive SHA一致を確認。full optimizer等checkpointはnative large2048/training/checkpoint-00062936.pt/SHA712150e66851c4e85cbcc6d342af6c0352b95cb6b1558549d77294ebda50fb93。jobの最後teachers24,696,536は20更新毎heartbeatで、最終25Mは監査済みcompleted checkpoint/compare-resultを正とする。complete jobは再開しない。
元10B UI527808/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13568618・ps/GPU process一覧とHTTP元親SHA410f975d…/10,000,007,168tokens/busy=falseへ復帰確認。科学GPU jobは終了。以下の「実行中」は当時の履歴で、この完了記録を優先する。
次の具体的なBase作業はcondition_diversity_source_ranking_proposal.json。固定旧64+新64train原文の両条件/元結末を、同parent2B/control512/large2048の3重みと全文履歴prefix/元の条件文だけのprefixで比較するread-only診断を実装・検証・凍結する。optimizer0/新教師0/GPU60秒/CPU準備30秒、128familyを全保持し既知弱12は別表示、同candidate bytes/IDs、本文likelihood/元原文の結末選好/condition marginsを記録する。元の異なる結末は排他的なhard negativeの保証がなく、source-matchingを真偽正答へ置換しない。条件文だけでは省いた先行文脈や代名詞依存を明記。過去の単なるtarget NLL診断を反復せず、trainで結末を選び分けるかと未知devへの転移を区別する。未実装・未凍結・未開始を実成果としない。所見に基づく一要因・同教師の次比較だけを予算/元基準付きで先に凍結し、無根拠の増量・比率/weight総当たり・長期延長をしない。
Base品質を満たす候補だけ独立学習seed/full dev/保護test/採用確認へ進め、実完了をユーザーへ報告して停止する。Base未採用、独立seed/full dev/protected test未実施、旧数値7失敗/全品質基準を保持。Chatと量子化は再開指示を待つ。PythonはWSL uv3.12.7、意味のあるlocal commitのみ、pushなし。

条件教材512対2048の同25M比較を実学習中（2026-10-06 JST）: Baseのみ継続。前goal turnは更新0診断/2048供給/全64/元ID・mask準備/a3b73baを完了したprogress。本turnはrunner/永続PS/reviewerを接続し、既存512 control25M・評価・80notesをraw SHA/元source/parent/shape/LRで再利用する。新科学は2048側25M、比較計50Mを区別する。
関連CPU4tests1.67秒（拡張sourceの実連続4対2+2・wrong manifest拒否/元3stream教師列/実測budget・weight1とBase-only scope）とPS構文成功。初版fixtureが64語彙へ94等を入れた失敗XMLを保存し、fixture IDsを実語彙範囲へ修正した。学習コードや品質基準を緩和していない。元cacheを再利用し原13GB index再scanなし。両samplerだけを実CPU再生し、条件以外のWeb/story/通常教材の全教師ID列SHA・教師数・EOS数・body bytesが一致（CPU3.752秒/上限30、新科学/GPU0）。条件教材とrow interleavingは意図して異なる。
actual527011終了・ps不在、2048実CUDA連続4対2+2は全32state/history/finite/LR checks一致。32連続timingも初め4更新のtrajectory一致、検証40updates/1,299,890教師は科学別、検証weightsは科学親へ使わない。GPU11.799秒、steady0.049209s/update・32497.0625教師/update、770更新の学習予測40.001秒、warmup/save・1.3倍margin・単一新評価300秒込み352.001秒。検証含む363.801秒が900秒上限内であることを確認して凍結。
科学config SHA87b4ed4070fb92d5c97ffbb9563d20ad3d649414d81c11426cabe0540a7f80d0、probe SHA715b6dc9ea032608d72dddeebb11f85d0c0868565d69bdcc442179477819143a。Windows26404/actual527392/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13556768をps確認、追加8,448,645/25M教師・loss2.566590有限で継続。親2B+20M/元Adam・RNG/LR0.0002/weight1/元Web18.75M/story1.25M/通常2.5M/条件2.5Mを保持、元whole body+EOS教師を残す。科学上限888.201秒＋検証11.799秒。completed updateの全state/cursor/RNG/counters/latest/logとrestartはreports/phase6/condition_diversity_active_job.json。元10B UIは科学job中停止し終端に元親SHA410f975d…へ復帰する。
次は同job終端と同dev256/472055bytes・日本語192/331/1119・新80全文→旧80再利用と全160比較/旧relative・absolute・original-Web基準→可搬証拠/commit。新文章品質・全comparisonは未評価/未完了、Base未採用/未完了、protected test/独立seed/full dev未実施。Chat/Dialogue/SFT/量子化は開始しない。旧数値7失敗/全品質条件保持、PythonはWSL uv3.12.7、local commitのみ・pushなし。

Base学習文への適合診断完了・条件教材を4倍へ準備（2026-10-06 JST）: 前goal turnは実50M比較/全160採点/採否/20802d1を完了したprogress。本turnもBaseのみ継続し、Chat/Dialogue/SFT・量子化は開始しない。Base品質/独立seed/full dev/protected test/採用の実完了を報告して停止する。
512元原文の条件結果body/その他body/EOSを親2B/通常CE25M/weight4 25Mの同BOS原文token・mask/standalone/BF16 mathで実測。3CPU tests0.87秒（shift/右padding/EOS/focus/全量・raw coverage/read-only）、PS構文成功、config SHA1bbad30fbee91786c5e1c992930097b42c835663da8ea4235233291ff4a098afを凍結。actual524889/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13464040は終了・ps不在、1536 checkpoint-document全件完了。GPU4.703986秒/占有4.704372秒（上限60）、更新0/新教師0/新corpus0、重み不変/RNG復元/no gradients/eval mode全3で成功。第一文書のbatch対single NLL差0は局所測定で旧数値7失敗を代替しない。
各checkpoint共通のfocus18,956/その他52,929/EOS512 targetsを測定。親→通常→weight4のtoken平均NLLはfocus2.020925→0.542920→0.080601、その他2.132311→0.888265→0.819566、EOS0.038345→0.006877→0.006386。focus有効504文書は全てweight4が通常より低損失だが、既存heldout一貫性15→9/適切27→24は悪化した。条件streamは元72,397 CE targetsを2.5M教師で約34.53回相当学習している。これは元学習文への強い適合と転移未達を支持する局所証拠で、唯一の原因・容量限界・一般化の独立証明ではない。失敗候補を採用せずweight sweep/長期延長なし。
全raw target IDs/mask/NLLとgroup再集計・同対象/有限値・終端監査を完了。65text/14,042,315bytes、gzip3,681,803bytes/SHA3a1d0402b343536909580c76b7a1aad954747260b4273ad34294899c80ab22bbを可搬保存。reports/phase6/condition_trainfit_diagnostic_review.json及びcompletionへ証拠を保存。元10B UI524960/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13464953をps確認、HTTP親SHA410f975d…/10,000,007,168/busy=falseへ復帰。
次比較は重み1/同親・Adam/RNG/LR0.0002・同各25M・同Web18.75M/story1.25M/通常教材2.5M/条件教材2.5Mのまま条件教材512対2048だけを変える。元512は完全に残しV3 selectorを変えない。seed2026100654/CPU240秒・32M draws上限の永続CPU準備actual525076は終了・ps不在、2048を78.579秒/13,794,837drawsで供給、元cacheを再利用し13GB再scanなし。原文body290,243tokens（小71,885）、既存2Bに含まれる再選択で新corpus tokens0。独立family/近似重複/外部事実認証はなく、グローバル教材を2Bから増量した証拠とはしない。
追加分の固定first64全文/両元branchを個別nonblind読解、弱4/上限10で従来gate合格。同条件/因果段階ずれ・義務表現の誤分割・不明な第二結果を弱として記録し、医療金融等の過度な断定や韓国語混入は別にflagする。正しいhard negativeは認証しない、selector改訂/有利なpilot取り直しなし。関連nested-source CPU1test1.53秒、PS構文成功。実原文ID/byte-span masksをCPU0.685秒で準備し、旧512のtokens/focus/offsets/lengths/metadataの全5actual checks一致。2048 whole docs/serialized294,339/full CE292,291/focus76,614、旧8＋新4 weakはfocusのみ無効で通常body/EOS CE保持。manifest SHA cf0ac3efa0722d54aa1f6107770ca41b7843a0297d5e53b68f3cde6480901280、WSL data /home/aihub_ubuntu/jmicro-data/phase6/condition-diversity-positive-20261006、可搬data gzip506,985bytes/SHA45ff6aff967c787b956fe002f0ea6e687d75c30a64986406557cb6f5d332ac5b。
比較proposalはreports/phase6/condition_diversity_comparison_proposal.json。既存512 control25M/評価/80notesは親・source・shape・LR・通常3stream等のbinding確認後に再利用し、新科学は2048側25M（比較計50M）と分ける。GPU900秒上限案、新実CUDA連続4対2+2/fullstate及び連続timing・実測予算凍結→本25M→同byte256/80新文章/日本語192・331・1119/旧relative・absolute・original-Web基準、という完了条件。runner/reviewer接続・新比較GPUはまだ未実装/未開始。次はこの接続と検証から実比較へ進む。Base未完了/未採用、独立seed/full/testは合格候補が出るまで未実施。全品質基準/旧数値7失敗保持、PythonはWSL uv3.12.7、local commitのみ・pushなし。

条件結果の正例重み比較完了・Base品質未達（2026-10-06 JST）: ユーザー指定のBaseのみを継続し、品質/独立学習seed/full dev/保護test/採用を実達成した時点で報告して停止する。Chat・Dialogue/SFT・量子化は開始しない。
actual522579は終了・ps不在。同2B+20M親から同入力/元Adam/RNG/LR0.0002・各25M教師、通常CE対条件結果bodyのweight4を完了。両770更新/各25,231,360 input、教師quota/digest/focus654,588/元EOSと実fullstate再開の全32checks一致。科学50M教師は新教材量0、検証2,599,740教師は別会計。科学GPU224.401秒＋probe22.019秒＝246.420秒（上限1800秒）。重み付き損失分母は25M対26,963,764であり追加学習tokensへ足さない。
同dev256/122343bodytokens/472055bytes・日本語192/331/1119・生成全160を個別nonblind採点し、同一prefix/text/停止の既採点を再利用してrubricを保持（control6、positive4 28）。文法/関連/一貫性と数・時間誤りを分け、幻想や短い妥当な文を自動失敗にしない。独立人手評価なし。通常→weight4はBPB1.143559→1.145198、文法54→61/関連43→45/一貫性15→9/適切27→24/EOS44→47/反復26→22（各80）、Unicode・role・empty0。意味52.604→55.208%、JBLiMP79.154→78.550%、JCQA29.848→29.937%。一貫性差-6/paired95%CI[-.15,-.0125]はこの固定dev/一学習seed・非blind判定の結果で、独立再現や普遍的因果の証明ではない。既存relative/absolute/original-Web BPB条件未達、両候補不採用・Base未完了。EOSだけの改善を品質採用にしない。
保存済み192スコアの副分析は追加GPU0/学習0。因果のopposite-label両正解は通常2/16→weight4 6/16、照応0→1だが、否定と比較は両条件0/16、否定全16は同候補を選ぶ。文脈marginは変化しており注意機構不動/容量限界とは断定しない。生成の一貫性の代替合格指標にはしない。
raw SHA付きnotes/review/checkpoint会計と102text/10,047,232byte archive（gzip2,438,906byte、SHA4b688e945071ffd72b109527a00aaf6e75189a0911668256b29cd942e8fe72c8）を可搬保存し、full checkpointsはWSL保持。completionはreports/phase6/condition_positive_comparison_completion.json。元10B UI523067/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13401229をps確認、HTTP親SHA410f975d…/10,000,007,168/busy=falseへ復帰。jobの最終教師heartbeat24,696,377は途中値で、完了量は両checkpointの25,000,000を用いる。終了jobを重複起動しない。
次は既存512原文/元token・maskを固定して親/通常/weight4の正例body・その他body・EOS NLLを比較する更新0診断を実装する。GPU60秒上限、全512×3/同target/有限値/重み・RNG不変と全量会計の完了条件をproposalへ保存。まだ未実装・未起動。学習した結果へ適合してもheldoutへ転移しないのか、適合自体が不足したのかを分け、一要因の次改善を選ぶ。診断は一般化/容量の証明にせず、weight総当たり/失敗候補長期延長/13GB再scan/dev学習転用なし。独立seed/full dev/testは合格候補が出てから。旧数値7失敗/全品質基準保持、PythonはWSL uv3.12.7、local commitのみ・pushなし。

条件結果の正例重み比較を実行中（2026-10-06 JST）: 四stream sampler/fullstate trainer/永続PS worker/実行runner/全160 reviewerを実装。CPU連続4対途中2+2（通常/weight4）のmodel/Adam/scheduler/RNG/sampler/counter/digest一致、両条件input/teacher/focus同一と実model更新の相違を関連4tests/2.18秒で確認。実測budget/shape/teacher/weight/later-stage拒否2tests/0.84秒、CLI/PS構文成功。これはCPU component証拠と実CUDA証拠を分ける。
実GPU probe522157は終了しps不在。両実CUDA連続4対2+2の全32state/history/有限値checks合格、各32連続timingも先頭trajectory一致。検証80updates/2,599,740教師は科学別・weightsを科学親へ使わない。GPU22.019秒、通常0.051067s/update・weight4 0.048820s/update、教師32496.4375/update。各25M学習の予測41.635/39.832秒、保存・warmup・評価600秒・1.3倍margin込み705.907秒を1800秒枠内で確認。科学config SHA5af7b204dd45f1f7a19821572889e2fa7ccf70577c268518b412a381ddb64ec9、probe SHA42afea17e5141a3cc38243227fd7e7bf9efd0a4f904fe855d9be500d24c4b5d8を凍結、科学上限1777.981秒＋検証22.019秒。
Train worker35704/actual522579/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13378300を実psで確認。同2B+20M parent/元Adam/RNG/LR0.0002、同入力と各Web18.75M/story1.25M/通常教材2.5M/条件教材2.5M＝25M科学教師を、通常CE対正例weight4で実比較中。正例に元body tokenの続きだけを重くし、全body+EOS教師は残す。weighted massは損失分母として別保存し新教材量・追加教師数へ足さない。sampler/model/Adam/scheduler/RNG/全counter/digestはcompleted updateで保存。restart/ログ/経路はreports/phase6/condition_positive_active_job.json。元10B UIはGPUjob中停止し終端で元checkpointへ復帰する。
次は両25M終端と同byte dev256・日本語192/331/1119・生成80ずつ→全160raw-bound内容と旧relative/absolute/Web BPB条件→条件family順位の副分析→証拠保存/commit。全比較/採否・Base品質はまだ未完了。Base完成後に報告して停止し、Chat/量子化は開始しない。旧数値7失敗/元品質基準を保持、protected test未使用、新GPUjobを重複起動しない。全PythonはWSL uv3.12.7、local commitのみ・pushなし。
Base条件保持の教材準備完了・比較実装へ（2026-10-06 JST）: Baseのみ継続し、品質/独立学習seed/full dev/保護test/採用の完了を報告して停止する。Chat/量子化は延期。前turn0a36033は全96＋V1全48の内容確認・停止境界を実保存したprogressであり、GPU待機ではない。本turnも科学GPUjobなし、元10B UI519042のみpsで稼働を確認した。
実失敗に対応するV2はならでは/なぜなら/観点導入/増えるほど/宛先対してを区別し近い条件を選択。固定seed2026100652・既確認96+48除外・60秒/2M draws上限で512件を実CPU11.511秒/1,351,045 draws、227,484本文/既存29,737,479 body tokensから抽出した。固定64全原文・両branchを読み、弱15/上限10でpaired-target gate不合格・学習0を保存。弱いとは教材全体が壊れている意味ではなく、対象の二条件と具体的な異なる結果を抽出できていない意味。疑問のよいのか/多くの場合/のみならず、同条件の利点と制約、一般条件と詳細条件などを区別した。外部医療/法律/金融などの事実認証はなく、未認証の主張だけを理由にpair失敗とはしない。
二回目/最終の内容改訂V3はしかしだけの接続を除き明示的対比へ絞り、埋込疑問・頻度表現・ならずを追加除外。V2実測で一方/逆にが238/512だったことから4M draws・CPU60秒内の供給予算を定めた。seed2026100653、既確認96+48+64=208のdocID/本文SHA除外、既存cacheだけを利用。512件を実CPU22.972秒/2,739,635 drawsで供給。固定64の全本文・両結果を個別に読み、弱8/上限10で元gateに合格。全raw SHA付きnotes/reviewを保存。V3のIDはcopyによりcondition-v2 prefixが残るrun内IDで、必ずrun path/本文SHAで束縛する。二つの別原文結果を互いに誤答と認証せず、全corpus率・source family独立性・事実性を保証しない。V4自動rerollなし。
WSL ext4に512全原文を元trainから再tokenizeせずそのまま保存し、source char spanと元token byte overlapで条件結果の正例位置を記録。CPU0.392秒、body71,885tokens/311,199bytes、BOS/EOS込み72,909、full CE教師72,397、focus候補18,956。既知の弱8はfocusだけ無効とし原文の通常CEは両条件で残す。data path /home/aihub_ubuntu/jmicro-data/phase6/source-condition-positive-20261006、manifest SHA7ef3df21ec52541d32f4b6e17321cb35271a25ded13af913dab6c1aab5e866fc。これは既存2Bに含まれるtrainの再利用でnew prepared original tokens0、科学教師/GPU0、hard-negative labels0。EOS3は元文書末尾だけで保持しbranch末尾へ捏造しない。
正例CEの重み計算を別helperへ実装。通常weight1は既存sum CE/gradientと一致、weight4は元body+EOS全教師を保ち正例bodyだけ重くしてweighted massで正規化。weighted massを実学習tokensと混同せず、EOSはboostしない。V2/V3/byte mask/lossの関連CPU計10tests（0.89/1.56/1.32/1.26秒）成功。CPU componentはCUDA fullstate再開・速度・モデル品質の証拠ではない。
次のBase比較の定義はreports/phase6/condition_positive_comparison_proposal.json。同2B+20M parent SHA965a06dc…・Adam/RNG継承/LR0.0002から、同input/label/seed42/同teacher quotaで各25Mの通常CE対正例weight4だけを比較する。Web18.75M/story1.25M/通常教材2.5M/条件教材2.5M、batch32/context1024/Flash/BF16。元byte dev256/生成80ずつ/日本語192・331・1119、全160内容と既存relative/absolute/Web BPB条件、対比familyの順位変化は副指標。まず四stream sampler/fullstate trainer/永続runner/reviewerを実装→CPU連続再開→実CUDA4対2+2と連続timing→実測で予算凍結→両25M比較。検証含むGPU1800秒/初期probe120秒、実測が入るまではscience config未凍結・未開始。失敗を採用やBase完成に置換せず、weight/ratio総当たり・自動延長なし。元証拠/旧数値7失敗/全品質基準保持、全PythonはWSL uv3.12.7、local commitのみ・pushなし。
最新の実行範囲・Base改善調査（2026-10-06 JST）: ユーザーの「baseが終わったら教えてください。chatや量子化はまだ入らなくていいです」により、Baseの学習・評価・改善と証拠に基づく採用までを継続し、Base完了を報告して停止する。Chat/Dialogue mid-training/SFT/量子化/最終deploymentは開始しない。以下の過去の全五項目やPhase4停止境界より、この最新範囲を優先する。Baseは未完了・未採用であり、独立学習seed/full dev/保護testの最終確認も未実施。
固定train96本文の全内容を個別に読みraw SHA付きnonblind notes/content-reviewへ保存した。Web/物語/教材各32の文法2は29/31/32、独立本文2は27/29/31、具体的な条件→結果は23/31/24、二条件と異なる結果の明示は4/0/5。正常な記述文や幻想を条件不足だけで品質失敗にせず、外部事実認証・全corpus代表性・容量限界の証明はしていない。新prepared/学習/GPU0。
既存compact indexから原文を変えず二条件を抽出するV1を実CPU0.896秒・60000drawsで実行。10512教材本文/既存1382828body tokensを読み、供給は48/目標512、固定pilotも48/必要64で不足。全48原文と両branchを個別に読みobservations.tsv/content-reviewへ記録し、本文SHA・prefix/続きの元char spanをuv実行で確認。ならでは/なぜなら/増えれば増えるほどの誤分割、宛先の対しての誤判定、一般条件と詳細説明の混同がある。異なる続きでも両方正しい場合があり、誤答候補とは認定しない。V1は学習pool不採用、科学教師/GPU0・保護test未使用。関連CPU2tests/0.89秒成功。元resultと全旧失敗/品質条件を保持し、採用閾値は緩和しない。
次のBase作業は、これらの実失敗に対応する抽出処理一改訂（語彙的なら・理由導入・増えるほどの除外、近い具体的条件の選択、元span保持）と、新seed/既確認96+48除外・CPU上限60秒での供給確認。固定64の内容採否と一要因/同教師・実測GPU予算を確定してからBase比較を実行する。同じ失敗selectorの無根拠retry・比率総当たり・自動5B/10B・dev文言の学習転用はしない。科学GPUjobなし、元10B UI519042のpsとHTTP親SHA410f975d…/10,000,007,168/busy=false確認。全PythonはWSL uv3.12.7、local commitのみ・pushなし。
実CUDA合格/科学学習中（2026-10-06 JST）: actual494779をps確認、新75/20/5 mixed2B側の連続4対2+2CUDA/BF16保存再開は全19checks（重み/Adam/scheduler/RNG/3source sampler/counters/履歴/有限値等）一致、検証259,968教師は科学学習と別会計。実large-stable科学教師約18.7Mまで進みloss有限、update500のlatest checkpoint/fullstateを保存。直近step約65万inputtokens/秒・data_wait約1.7ms/GPUstep50ms、nvidia瞬時GPU89%/7709MiB、継続中の学習速度は品質証明ではない。Windows31344/Linux494779/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start11837034、run textbook-quantity-comparison-20261006、累積GPU4861秒/各1B+20M・残り二CUDAgate/同bytes日本語/全160を継続。latest_path/hashと再開はtextbook_quantity_active_job.json・nativejob、終了/中断をactual確認してから再開し重複しない、終端時元UIを復帰。Base/Chat未採用・全五目標active・旧数値7失敗/全品質基準不変、次はこの比較結果から改善Base→実Chat/人間最終test→量子化/UI、WSL uv/local commitのみ。

永続比較起動（2026-10-06 JST）: e7a4761で新75/20/5 mixed500,000,328対2,000,001,312/全64弱9受け入れ/両1B+各20M decay/GPU4861秒を凍結。Windows31344/Linux494779/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start11837034をactual psで確認しCPU preflight合格後に元UIを停止、run textbook-quantity-comparison-20261006でsmall/large index読込み中。GPU/科学学習は直近0として保持し、実CUDA保存再開/有限値三gateと実学習は未達。active identity/config/restart_commandはtextbook_quantity_active_job.json・native job.json、実プロセスを確認して重複しない。SIGTERM/予算では完成update checkpointを保持、終端時元UIを復帰。次は三実CUDA/両1B+20M/同byte日本語/全160内容→品質Base→実Dialogue/SFT対direct/retention・seed/人間test→量子化/実UI。全五目標はactive・Base/Chat未採用、旧数値7失敗/全品質基準不変、WSL uv/local commitのみ、pushなし。

教材採否/比較凍結（2026-10-06 JST）: 新75/20/5混合493920は280.672秒でcomplete/ps不在、small500,000,328/large2,000,001,312、Web375,000,002/教材100,000,084/物語25,000,242と厳密4倍/source-length-unit-EOS条件。新未確認64（24Web/24textbook/16story）を全原文で非blind評価、weak9で既存<=10に合格。宣伝/文法/前文依存/未説明区別/物語の矛盾を全raw-SHA notesへ保持。抽象文、匿名人物、軽微な誤記、比喩、source由来の未認証医療・法律・数値は理由と限界を明記し、代表的corpus率/独立人間/事実認証/モデル品質とはしない。別configs/phase6/textbook_quantity_comparison.jsonを実zero-update fresh13層10M・両1B+同20M decay・LR.002/warmup200・3source教師/EOS/fullstateと同dev bytes/日本語/全160で凍結。過去1B教師実速度から2.04B/throughput*1.3+900=GPU4861秒、検証教師別・三実CUDA連続4対2+2gate・UI停止前CPU preflight・永続job/再開を必須。実GPUはまだ0、次はverified local commit→永続学習起動→全日本語/160採否→改善Base/実Chat/人間test/量子化UI。全五目標・旧数値7失敗・全品質基準保持。

実測完了/混合準備継続（2026-10-06 JST）: textbook component493499は250.715秒でcomplete/ps不在、small100,000,084/large400,000,336/dev400,088、固定train9filesのみ取得/新hash確認（最大12、公式dev/testなし）。原文/source_id学年family/既読32除外/厳密4倍を保持し品質採用ではない。混合CPU永続Windows31780/Linux493920/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start11787515をactual ps確認、900秒で旧Webcache再利用+新textbook+source-storyの500M/2Bを組み合わせる。別三sourceindex/sampler/trainerを実装しWeb/story/textbook教師・EOS・tag mappingをfullstateに記録、履歴の二source trainerは変更しない。関連CPU2tests2.21秒で重み/Adam/scheduler/RNG/cursorの連続対再開・decay継承一致、別4tests0.88秒で同1B学習・正確4倍・raw内容・live preflight拒否を確認、CLI/PS成功。run_textbook_quantity_comparison.py/ps1と全160reviewを準備したが実CUDA/科学学習/config凍結は0。次は混合完成→未確認64弱<=10→同fresh10M/各1B+20Mを実測GPU枠で凍結/local commit→実CUDA保存再開/学習・全日本語/全160→品質Base/実Chat/最終人間test/量子化UI。全五目標・旧7数値失敗・品質基準保持、WSL uv/local commitのみ。

実行中/新教材準備（2026-10-06 JST）: e6b92bdでv3実2B準備完了/全64弱11不採用を保存。bfa61feの独立textbook100M/400M componentを永続Windows31880/Linux493499/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start11761563で起動し親と8workersのactual psを確認。最大固定train12files/新取得SHA/原文paragraph/provenance/source_id family/既読32除外/CPU1800秒を保持、途中進捗はtextbook_component_active_job.json・nativejobに記録。混合builder/reviewを追加しWeb75/textbook20/story5の500M/2B厳密4倍を予定。Webは旧不採用cacheの原文4groupを再利用し再tokenizeしない、既読64を含むgroupを除外、storyは受け入れ済みsource trainから再選別、全source canonical除外/長さunitEOS比を保持。新固定64は24Web/24textbook/16storyで非blind全内容、<=10基準不変、独立人間/代表的弱率/事実認証とはしない。関連CPU2/3testsと両PS構文/CLI成功。component実完了後に900秒の混合準備を起動し全64採否、合格時だけ3source教師/EOS会計を実装/実CUDA再開確認して両1B+20M比較。GPU学習0/Base・Chat未採用、旧数値7失敗と全五目標/基準を保持。

完了/教材不採用（2026-10-06 JST）: v3 CPU準備actual492108は1420.150秒でcomplete・ps不在、small500,000,264/large2,000,001,056と厳密4倍/source-length-unit-EOS条件を達成。全未確認64を原文で非blind評価し弱11で既存<=10基準を満たさず、GPU比較は凍結/起動しない。未回答の問い、前文依存、宣伝、崩れた文法、根拠のない教訓を全raw SHA付きnotes/reviewへ保持、判定の再分類/基準緩和なし。新教材案は同500M/2BでWeb75%・固定公開SyntheticTextbook-jp20%・物語5%、まずtextbook100M/400M厳密4倍componentをnative4kで準備し、既読32 familyを除外。最大固定train12files・CPU1800秒/8workers、実供給不足時はpartialを保持し学習しない。教材の事実/元Webとのglobal overlapは未検証として表示、旧Web/story dataは未採用キャッシュであり新全64の採否が必要。両1B+同20M比較→品質Base→実Chat/retention/seed・人間/test→量子化/実UIの全五目標は継続。元UI489906はps稼働確認、旧数値7失敗/全品質基準を保持、WSL uv/local commitのみ。

補助実測/継続（2026-10-06 JST）: 主v3準備492108の実稼働とWeb1.50B/small375.52Mまでの増加を確認、2B終端は未完了。固定SyntheticTextbook-jp/f928b35fde6732f7d981860d32a18ef451cd539e/Apache2のtrain-00000.parquet265,038,889bytesだけを実取得、SHA7e9a9276…一致後にuniform row1024/66,701を読む有限pilotを17.552秒で完了。公式validation/testと他15filesは取得せず、native4k平均body1167.301、適格train1016、当fileのserialized候補約46.060M/CI45.041–47.043Mを測るが、重複/既存Webとのoverlap/全source容量/新prepared/品質とはしない。first eligible unitの32 distinct source_id familyを全原文で非blind確認、弱3（説明予告/二分類の片方欠落/重要性導入だけ）。3/32は独立人間・代表的corpus率・固定64受け入れ・Webへのpaired優位ではなく、医療/技術/歴史/数値は未認証。textbook_supply_result/sample32_notes/reviewと全draw/source archiveへ保存、関連CPU1test1.10秒、GPU0/新prepared0/Base・Chat未採用。主v3教材は変えず未確認64の正式採否→同量各1B+20M/GPU実測枠→改善Base→実Chat/retention/全seed・人間/test→量子化/実UIを継続。旧数値診断はFP32でも自然文の反復が残る実証済みで同一GPU再診断は行わず、旧7失敗・全品質基準・全五目標を保持。WSL uv/local commitのみ、pushなし。

実行中/継続（2026-10-06 JST）: 72c3704で供給比較とv3を凍結し、CPU永続worker33884/actual492108/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start11587415と8workersをps確認、run larger-material-20261006-95web-v3で原文first32適格段落の500M/2B厳密4倍95/5準備を継続。actualと最新進捗はlarger_material_v3_active_job.json、CPU1800秒/8workers、未完了partialは学習不可・失敗時同一blind retryなし。元10B UI489906/HTTP親SHA410f975d…/tokens10,000,007,168/busy=false・ext4空319GBを確認。review_larger_material.pyとrun_larger_material_comparison.py/ps1、review_larger_material_comparison.pyを追加し、未確認64弱<=10/終了・raw notesを待って同fresh10M・両1B教師＋同20M decayを凍結する準備。実測旧1B速度から2.04B/throughput×1.3+900秒（上限7200）の累積GPU枠、UI停止前CPU preflight・各stableとequal-decay CUDA4対2+2、保存再開/全会計・同byte256/日本語192・331・1119/全160内容とpaired採否を保持。関連CPU9tests2.59秒/CLI help/PS構文成功、実GPU config/学習/生成0。1B screenは2B全量を使い切る証明ではなくgenre/EOS/epoch/blockと学習量を別表示、exact unique-token union/global audit未測定。Base/Chat未採用・旧数値7失敗と全品質基準・全五目標を保持。次はCPU準備終端→全64採否→同量学習と全160→改善Base→実mid/SFT対direct/retention/全seed→人間/最終test→量子化/実UI。WSL uv/local commitのみ、pushなし。

進捗/継続（2026-10-06 JST）: 旧2B CPU準備491375は462.849秒で協調SIGINT→exit130/failed・親/8workers不在を確認し、small Web118,808,156/large475,232,624のpartialと凍結sourceを保持。native token-uniform6000同draw供給比較は旧1unit約1.049B/CI.990–1.110B、all-first4約1.325B/CI1.258–1.395BでWeb1.9B未満。品質filterは保ち原文first32内の全適格段落を使う別版は約2.213B/CI2.137–2.292B、重複/除外/group損失前のgross推定でdistinct/準備完了/品質とはしない。旧first4無適格でも後段適格があるため継承parity assertionの初回失敗を一度修正し別run/原source保存。whole採用時は段落を重ねず全siblingsを同first-family splitへ、probe例familyは全pool/未確認64から除外。v3独立builder/launcherと関連7CPUtests1.36秒/PS構文を凍結、準備1800秒/8workers、500M/2B厳密4倍95/5の目標不変、GPU0/未起動。次はv3永続CPU準備→固定64弱<=10全内容→同fresh10M/両1B+同20M decayのconfigと実GPU予算→品質Base→mid/SFT対direct/retention/全seed→人間/最終test→量子化/実UI。供給probe全draw/sourceはlarger_web_supply_evidence.tar.gz、準備はlarger_material_v3_preparation.json。Base/Chat未採用・全五目標未完了・旧数値7失敗/旧全証拠/品質条件維持、WSL uv/local commit、pushなし。

最新完了（2026-10-05 JST）: 契約75の準備・各100M比較・品質未達による拡大非実行まで完了、結果docs/79_narrative_diversity_results.md。公開原文10000/1,206,453準備tokens（物語9000/Web1000）、固定64内容弱10/64、CPU9tests成功。元同一10Bから従来自然1000対新原文10000を各Web80M/short20M教師で学習、日本語全評価/専用dev64/160個別内容完了。基本意味58.333→64.583%、BPB0.980130→0.984834、EOS30→7、反復31→27、一貫性6→3、適切完結6→2。候補不採用、50k/5Mへの拡大・追加500Mは未開始。科学200M/valid・physical200,966,144、CUDA再開8更新260,794別、GPU500.023秒。比較actual395310/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start9106956終了・不在。元UI395857/同boot/start9157480とHTTP親SHA410f975d…/10,000,007,168/busy=false確認。可搬narrative_diversity JSON/tests/raw gzipとLinuxrun/data/両optimizer込み終端保持。最初の準備失敗、非blind内容判定、source/長さ/EOS密度の交絡、結果72の数値7失敗も保存。次案docs/80_generation_transfer_plan.mdは正解対自由生成・64/256停止位置の診断から変更を一つ選ぶ計画で未開始。今回の範囲は完了、verified local commit後停止。新data/GPU/20B/Chat/test/pushなし。以下は履歴。

最新完了（2026-10-05 JST）: 契約73を段階4の品質未達/拡大非実行分岐まで完了、結果74。Adam引継ぎ/初期化各8Mはtrain64/64 gold＋EOS成功、別名dev127/128・128/128（同32scene）。規則でinherit選択。元同一10Bの従来/自然各25M教師・全日本語/160個別内容を完了。一貫性0→7、適切完結0→8、EOS10→26、反復48→30、BPB0.982188→0.983213。候補改善はあるが全品質基準未達、増量9192/追加100Mは未使用、不採用。科学66M/valid66,334,768/physical89,325,568、CUDA再開16更新215,168教師別、GPU484.284秒、CPU4tests・実学習/評価/完了監査成功。両job完了・不在、元UI actual379377/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start8917553とHTTP親SHA/tokens/busy確認。可搬natural_learning各JSON/原文gzipとLinuxrun保持。次案は名前置換ではない多様な完結文と同量各100M比較で未開始。結果72数値7失敗は保持。verified local commit後停止、追加準備/学習/20B/Chat/test/pushなし。以下の実行中記載は当時の履歴。

進捗（2026-10-05 JST）: 契約73の段階2完了、両Adam各8M教師でtrain64/64完全再現＋EOS。inherit別名dev127/128、fresh128/128（同じ32sceneなので一般汎化ではない）。規則でinherit選択、新規重みC不要。科学16M、検証215168別、GPU186.757秒、終端full resume/教師会計/有限値/原文評価監査成功。段階3 compare actual378856/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start8887284が元10Bから従来/自然各25Mを実行中。全160個別内容と日本語評価後、全既存gate合格時のみ段階4追加100M。元UI一時停止、終端復帰。重複起動しない。

実行中（2026-10-05 JST）: ユーザーの「4まで進めてください」で契約73を再開。自然64全文3426tokens、自然train1000全文52791tokens、条件付き増量9192全文501559tokens、未学習128を固定。32日常sceneの因果/対象/完結と64実原文をCodex確認、CPU4tests成功。A/B Adam引継ぎ/fresh各8M教師、必要時新規初期化C8M。記憶gate合格後に元10Bから従来/自然混合各25M、全日本語と160内容評価、全品質gate合格時のみ追加100M/増量。GPU各段階600/1200/1200秒、検証教師別。actual job-diagnostic/compare/expandを確認して重複起動しない。元UIを一時停止し各job終端で復帰。結果72の数値7失敗は保持。全範囲の結果/採否/local commit後停止、20B/Chat/test/pushなし。

最新完了（2026-10-05 JST）: 契約71の三項目＝計画70内部0〜2を実診断、結果72。32 train入力・三実重み・BF16生成384/FP32生成96・教材128全文確認。元10BのFP32 full/causal CE・gradient同一、cache/独立HF許容内。ただしpadding1要素/BF16 logitの計7checks失敗を保持。FP32でもoriginal/mixedの自然16件loop/停止未達が残る。mixedの条件16は全greedy/samplingでgold+EOS完全再現、既存story枝は短物語8/8EOSで展開改善。EOS無効化だけでは説明できず、自然文の教材適合/汎化/loop分布を優先。品質未解決、学習0/optimizer更新0。GPU63.439708秒、CPU4tests成功。raw bundle/summary/全文理由/完了証拠はreports/phase6/root_cause_*、Linuxrunはroot-cause-20261005。両job完了・不在、元UI actual374638/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start8753669、HTTP元SHA410f975d…/10,000,007,168/busy=false確認。verified local commit後に停止。自然短文64のAdam引継ぎ/fresh各8M比較は提案で未開始。追加学習/20B/Chat/test/pushなし。以下の実行中/計画のみの記載は履歴。

実行中（2026-10-05 JST）: ユーザーの三項目の再開範囲は契約71（計画70内部段階0〜2）。実装整合性、EOS/反復確率、教材適合性を診断する。32 train入力・128全文・三checkpoint SHAを凍結、CPU4tests成功。GPU占有上限600秒、学習/optimizer更新0。自然文記憶や次の学習比較は範囲外。元UIを一時停止し、診断終端で元10B UIへ戻して結果・local commit後に停止。reports/phase6/root-cause-20261005/job.json のactual PID/boot/start/logを確認し、重複起動しない。

最新提案（2026-10-05 JST）: [根本調査計画70](70_root_cause_investigation_plan.md)。実装の経路差→EOS/反復の発生点→必要な自然文陽性対照→原因別小比較→条件付き同10M設計比較の順。既存証拠を再利用し、単純増量や再学習を結論にしない。今回は文献/source/保存結果の調査と計画のみ、実行は未開始。下記の結果69・元品質目標は維持する。

最新完了（2026-10-05 JST）: [実行68](68_packing_learning_execution.md)段階1〜3、[結果69](69_packing_learning_results.md)。同教材の連結/順序変更/文書単位を各25M教師で実学習しtrain75/100/100、新dev74/85/76。shuffleを選び元10BからWeb80M＋短文20Mの各100Mを比較、対照train71/dev54→候補99/76。ただし一般自由生成は両一貫性0/適切完結0、EOS2/2、反復65/53（各80）で候補不採用。新五終端の日本語/全400個別内容評価、旧dev参照、24CUDA再開625,842教師別会計、106終端証拠checks完了。科学275M教師。Base/Chat品質未達、Phase7へ移行せず、元10B UI復帰・verified local commitで停止。次の多様な自然短文教材比較は提案のみ。以下の歴史的記録・原Phase定義と品質条件を維持する。
最新（2026-10-05 JST）: [契約66](66_condition_learning_diagnostic_plan.md)の四段階を実行、[結果67](67_condition_learning_diagnostic_results.md)。両追加24,969,216tokensでtrain75/68・未見65/61、目標未達で条件付き100Mは未開始。文脈付きtrain100%と単独の差を実測。全日本語・160内容評価済み、EOS改善のみでは一貫性/BPB未達で両不採用。Base/Chat品質未達、元10B UIを復帰してverified local commitで停止。次の文書単位学習比較は提案のみ。以下のPhase定義・原品質条件と以前の結果を維持する。

# JMicro-10M フェーズ別実行計画

最新（2026-10-05 JST）: 結果63後の四項目は別train32でselector v2を改修/凍結し、同source各20M/未確認全80を診断。対照弱例12/候補14で両内容gate未達、準備失敗分岐の採否・報告・元10B UI確認まで完了して停止。新GPUなし。状態はdocs/autonomous_status.md、結果はdocs/65_condition_selector_v2_preparation_results.md。以下のPhase定義と元品質条件は維持する。

作成日: 2026-10-02。最終更新: 2026-10-05（10Bと各100M/500M比較・日本語評価の実状態へ更新）。根拠は[プロジェクト目的](01_project_goal.md)、[設計](03_architecture.md)、[技術調査](11_technical_research_gaps.md)、[Phase 0完了記録](16_phase0_completion.md)、[Phase 1完了記録](17_phase1_completion.md)。既存の**確定**方針から逆算した計画であり、将来の成果物名・未凍結の実行値は**提案**である。品質目標・評価契約はPhase 5で凍結済みで、結果を見て緩めない。

## 最終的に実現すること

約10Mパラメータの日本語専用モデルをランダム初期化から学習し、日本語短文生成と2〜数ターンの雑談をローカルで実行する。コーパス選別、独自Tokenizer、Base事前学習、Dialogue mid-training、Assistant-only SFT、量子化までを再現可能なpipelineとして残す。

最終成果物は次の三つに分ける。

1. `JMicro-10M-Base`: 日本語短文生成の基準モデルと評価結果。
2. `JMicro-10M-Chat`: 関連した短い返答、話題継続、文脈維持、停止を評価した会話モデル。
3. 再現・利用一式: 学習コード、config、Tokenizer、データmanifest、再開可能checkpoint、量子化artifact、ローカル実行手順、実験台帳。

目標規模は9.5M〜10.1M parameters、初期contextは1024 tokens。5〜10MB級は量子化配布の目標であり、Tokenizer等を含む実容量、推論メモリ、品質を測って達成を判断する。高度な推論・コード生成・長文RAGは今回の成功条件へ加えない。

## 現在地と計画の使い方

2026-10-05 JST: Phase0〜5と主要Web10B、追加教材/学習量比較は完了。最新は[selector v2準備結果65](65_condition_selector_v2_preparation_results.md)。同source各20Mの未確認40各で弱例12/40→14/40、両内容条件未達で準備失敗分岐を完了、新GPUなしで停止。最新科学学習は[結果60](60_dataset_expansion_results.md): 物語60M→200M・各追加1B、常識改善/一貫性EOS未達で不採用。Base/Chat未達、Phase7へ移行していない。

モデル10,001,152 parameters、Web準備12,225,819,077 tokens、物語準備200,000,192tokens。主系列とUIは10,000,007,168学習tokens、最新二枝は各11,000,020,992tokens。別枝の合計科学2,000,027,648と検証262,144を区別する。長さ/source/EOS密度差を保持し、量だけの効果や容量限界は未確定。

今回の範囲は[実行64](64_condition_selector_v2_execution.md)の四項目の準備失敗分岐まで完了した。別train32でv2を凍結し、各20,000,072-token教材・長さ全並び/BOS/EOS一致・未確認全80を診断した。条件未達で各100M/条件付き全文を起動しない。次回案は結果65。新たな小教材設計/data/GPU/20B/50B/Chat/test/pushは未開始。状態は[status](autonomous_status.md)、移行は[引継ぎ](windows_handoff.md)、確認は[checklist](10_next_steps.md)を正とする。

以下のPhase定義・品質目標は維持する。以前の現在地と次の実行案は[2026-10-05履歴](autonomous_history_20261005.md)、各実験の当時の計画は各番号の文書へ保持する。結果や提案を新jobの開始指示として扱わない。20B/50Bと有料cloud/公開は別範囲。

## 全体の順序

| Phase | 状態 | 実行環境 | 目的 | フェーズ終了時のゴール | 前提 |
|---:|---|---|---|---|---|
| 0 | 完了 | iMac | 成功条件と実験の契約を固める | 設定・記録・評価仕様を作成し検証済み | [完了記録](16_phase0_completion.md) |
| 1 | 完了 | iMac | 目的に合うデータを追跡可能にする | 小規模Base corpusと会話pilot、独立した評価splitを用意する | [完了記録](17_phase1_completion.md) |
| 2 | 完了・[証拠](18_phase2_completion.md) | iMac | 日本語を小語彙で安定して表現する | 同じsampleで学習した4k/8k Tokenizerが契約を満たす | 1のsample・split |
| 3 | 完了・[証拠](19_phase3_completion.md) | iMac / CPU | 10Mモデルと推論経路を成立させる | 正しいモデル・cache・HF/float GGUF経路を確認する | 2 |
| 4 | 完了・[実機証拠](21_phase4_completion.md) | Windows/WSL＋RTX 4090 | 長時間学習の再現性と実行可能性を確かめる | 保存再開・実shard学習・4090速度と予算を検証した | 1〜3 |
| 5 | 完了 | Windows/WSL・RTX 4090 | 小予算で有望な候補を選ぶ | overfit、10M smoke、100M比較から最大2候補を選ぶ | 4 |
| 6 | 主要10B・各100M/500M/1Bと200M教材比較完了、品質目標未達 | Windows/WSL・RTX 4090 | 日本語Baseの能力を段階的に伸ばす | 学習量・配合・生成/意味診断を比較し、Base品質を別判定する | 5、[準備証拠](30_phase6_readiness_execution.md)、[最新判断60](60_dataset_expansion_results.md)、[次案61](61_condition_preservation_next_plan.md) |
| 7 | 未着手 | Windows/WSL・RTX 4090 | Baseを短文雑談モデルへ仕上げる | mid-trainingとSFTの効果を分離し、Chat v1を評価する | 6、1の会話pilot |
| 8 | 未着手 | 学習PC・独立したローカル検証環境 | ローカルで使える成果物を完成させる | Base/Chatと量子化版を独立環境で実行・再現できる | 7、3のexport経路 |
| 9 | 未着手・50Bは条件付き | Windows/WSL・RTX 4090 | 追加学習に継続価値があるか検証する | 20B、条件付き50Bの効果と限界を報告する | 6、追加予算の見積もり |
| 10 | 未着手・後半研究 | ローカル中心、後半にVast.ai並列比較 | baselineを越える追加研究を行う | 共有・蒸留・hybrid・規模比較の採否を証拠で決める | 8、固定したbaseline |

Phase 0〜8を最初の完結した開発系列とする。Phase 9は20Bの評価と、改善継続時のみ50Bへ進む系列。Phase 10は後半研究であり、最初のChat完成を待たせない。

Phase 1の会話pilotは準備済みで、拡張と評価準備をBase学習と並行して進める。Phase 6で10B Baseが成立すればPhase 7へ進め、20B・50BをChat開始の前提にしない。単一4090ではGPU実験を順番に実施し、CPUでのデータ整理・評価準備を並行する。

**確定（実行場所）**: Phase 0〜3はiMacで実施し、Phase 4からWindows/WSL＋RTX 4090へ移行済み。Phase 4のNorm/default eager運用上限はT8K 57 / T4K 64。Phase 6③ではNoNormのreference/math最大45、compiled/math最大53、compiled Flash最大111を検証。最速はFlash＋compile reduce-overhead batch 32、694,521 tokens/sで、容量上限と最高速度を分ける。[高速化完了記録](29_phase6_performance_completion.md)、[移行成果物・確認条件](07_environment.md)

## 高速に完成させる進め方

**確定（優先方針）**: ユーザーは完成までの時間短縮を優先する。Windows/WSLへの切替とPhase 4は完了した。Phase 5の候補選定まで完了し、Phase 6①〜⑤、5Bと各100M比較、10B準備が完了。本10B科学学習・保存確認・同条件品質評価は完了し、Base/Chat品質目標は未達。Phase 3をGPUで最初からやり直すことは移行の前提にしない。

Phase 3の最終検証一式はM1 iMac上で24.62秒。これは実装後の検証時間で、コード作成・修正、Tokenizer学習、runtime初回build、docs更新を含まない。作業全体の約25分と区別し、GPUへの変更で実装時間まで短縮すると見積もらない。[実測report](../reports/phase3/export_parity_report.json)

Phase 4は以下の順で実施済み。新規環境への移行・実装変更時にもこの検証順を使う。すべてのPhase 4完了条件は維持する。

1. **移行・CUDA確認**: GitのコードとGit管理外のTokenizer/pilotを引き継ぎ、hash/ID一致、GPU/driver/PyTorch/BF16を確認する。Macのnative binaryや仮想環境はコピーしない。
2. **最小の学習経路**: 検証済みモデルを使い、AdamW/BF16、uint16 shard、本文NLL/BPB・生成評価、checkpointを実装する。まず小batchでfiniteな1 stepまで成立させる。
3. **保存再開の検証**: 同じ環境で連続200 stepsと100→保存→再開100 stepsを比較し、消費token列・loss・weightsを確認する。
4. **速度と最大batchの実測**: batchを倍増して境界を見つけ、中間値で最大安定値を測る。compile初回と定常速度、backend、syntheticと実shardのI/O、評価・保存時のVRAMも記録する。最大安定batchと最高速度のbatchは両方残す。

変更した箇所と関連gateを検証し、関係のないPhase 1取得・Tokenizer再学習・CPU GGUF全検証を繰り返さない。artifactを変更した場合、移行先で数値差が出た場合、学習済みモデルを配布する場合は対応する検証を再実行する。

最初のChat完成に必要なPhase 0〜8を優先し、20B/条件付き50B、Muon等の追加比較、hybrid、クラウド並列研究はbaseline成立後に進める。小探索では主要因を一つずつ比較し、総当たりを前提にしない。データは次の段階で使う量から準備し、master corpus全量取得を学習開始の条件にしない。

**時間見積もり**: 「学習開始まで1〜2日、初版Chatまで1〜3週間」は会話中の粗い仮見積もりで、確定scheduleへ採用しない。実装作業時間とGPU計算時間を別々に記録する。変更後の採用設定で検証済みのPhase 6③のtokens/secから`残りtokens / tokens/sec + 評価・保存・比較runの時間`を計算し、段階ごとに更新する。品質の修正が必要な場合は追加実験を別に見積もる。

## Phase 0: 成功条件・環境・実験管理

**状態**: 完了。詳細な実path・検証範囲は[完了記録](16_phase0_completion.md)と[完了監査](../reports/phase0/completion_audit.json)を参照する。以下は実施した内容で、Windowsの実機確認はPhase 4へ残す。

実施時点のhashとsnapshotは履歴として保存する。計画やREADMEの更新で現fileが変わった場合も、過去runのsnapshotと監査を上書きしない。Tokenizer/data入力のartifact hashは作成前のため`null`で、各フェーズの完成後に実fileを記録する。

**目的**: 学習できたことと、狙った短文対話が成立したことを区別して判定できるようにする。

**ゴール**: runを再構築できる記録形式と、結果を見る前に固定した評価仕様がある。

作業:

- リポジトリ骨格、依存version固定、run ID、artifact naming、seed管理、config schemaを作る。
- iMac側の環境を記録し、Windows/WSL用の依存設定と移行手順を用意する。WSL 3.xの実導入version、GPU、driver、OS、PyTorch/CUDA、ストレージの実機確認は切替時に行う。
- Base評価、Chat評価、tokenizer契約、数値誤差、停止ID、公開対象のデータbucketを仕様化する。
- Base completionとChat各100件の独自prompt suiteを作成し、各dev 80件・最終test 20件へ分けた。Chatは挨拶、感情応答、質問返し、訂正、2〜数ターンの文脈を含む。

**成果物（作成済み）**: [experiment schema](../schemas/experiment_schema.json)、[iMac環境記録](../reports/phase0/environment.json)、[評価仕様](evaluation_protocol.md)、[固定promptとsplit](../eval/README.md)、[実行入口](../scripts/experiment.py)、`pyproject.toml`・`uv.lock`・`.python-version`。

**完了条件**: 同じrun IDからcode commit、config、依存環境、データ/Tokenizer hashを特定できる。Chat rubric、BPB分母、generation設定、dev/testの用途が明記される。評価例を手で採点し、ルールの曖昧さを修正する。

**次へ進む判断**: iMac上の設計・データpilot・Tokenizer・CPU実装検証は進められる。4090の実機記録は移行時のgateとし、Phase 4のGPU検証と学習開始前に確認する。

## Phase 1: データの小規模pilotと評価split

**状態**: 完了。[実施結果・実path・限界](17_phase1_completion.md)、[全件検証](../reports/phase1/verification.json)、[再生成一致](../reports/phase1/reproducibility.json)を参照する。Phase 0の共通前処理を使い、[処理コード](../src/jmicro/data.py)と[実行入口](../scripts/prepare_phase1.py)を作成した。

**目的**: 日本語短文・雑談へ容量を使い、出所不明の混合や評価漏洩を避ける。

**ゴール**: 100M探索まで使う小規模corpusと、Chatに使える会話候補の実量・品質が分かる。

取得に使用したsource:

| source | 確認したrevision・条件 | pilotでの扱い |
|---|---|---|
| FineWeb2 Edu Japanese / `small_tokens_cleaned` | revision `180ca004c6a89b590daaad86cb062a07a5353c69`。配布READMEにODC-By v1.0とCommon Crawl利用条件を記載 | 小規模Web pilotに採用。READMEで先頭0〜9,999行と10,000〜19,999行の重複を告知しているため、先頭10,000行を避け、取得後にも重複を検査する |
| RealPersonaChat | revision `28d0b6b3865b29cabc26c230a2db37cdf315e937`。LICENSEはCC BY-SA 4.0 | 会話pilotに採用。Webとは別bucketで出所・条件を記録し、persona・人口統計metadataは学習入力へ含めない |

根拠: [FineWeb2 Edu Japaneseの固定revision README](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese/blob/180ca004c6a89b590daaad86cb062a07a5353c69/README.md)、[RealPersonaChatの固定revision LICENSE](https://github.com/nu-dialogue/real-persona-chat/blob/28d0b6b3865b29cabc26c230a2db37cdf315e937/LICENSE)。取得済みmetadata・形式確認用previewは`data/phase1/source_metadata/`に保存した（Git管理外）。調査metadataは処理入力へ流用せず、固定revision原fileを取得してpilotとsplitを作成した。証拠のURL・revision・取得file hashはsource台帳へ固定済み。

**実施した取得範囲**: [config](../configs/data/pilot.json)へschema、保存先、容量上限、選択方法を固定し、Web 20,000文書、会話3,000対話を取得した。採用はWeb 19,998文書、会話3,000対話、合計42,647,826 canonical UTF-8 bytes。取得数とfilter後の採用数を分け、unique量・反復回数・実際の学習tokensを別に報告する。100M tokensの探索に不足する場合は取得範囲の拡張または明示した反復で対応し、unique 100M tokensを取得済みとは扱わない。

実施項目:

1. source台帳とdocument/dialogue manifestのschemaを作り、source/subset/revision・利用条件・raw/canonical hash・cluster・splitを記録できるようにする。
2. 確認済みrevisionを台帳へ固定し、少量sampleの取得範囲・容量上限・保存先を決めて本文を取得する。viewer previewのrevisionと固定revisionを混同しない。巨大データ全量の取得は先行しない。
3. sampleを共通前処理、filter、dedupへ通し、train/dev/testを固定する。Phase 0の`eval/`はモデルの固定生成suiteであり、新しいcorpus splitとは別管理する。
4. trainだけからTokenizer学習sampleを選ぶ。4k/8kで同じdocument集合・順序・hashを使えるようにする。
5. 使用条件を満たす短文会話候補で1k〜10k対話のpilotを作り、件数・応答長・turn数・品質をreportする。教師tokensはPhase 2で実計数する。

作業:

- [データ設計](05_dataset.md)に従ってsource/subset/revision、利用条件、raw/canonical hash、品質、splitを持つmanifestを作る。未確認sourceは採用を保留する。
- FineWeb2 Edu Japanese等から小subsetを取り、弱い前処理、言語・品質filter、日本語向けexact/near/cross-dataset dedupをpilotする。
- duplicate cluster単位でtrain/dev/testを分離してからTokenizer学習sampleを選ぶ。
- 使用条件を満たす候補から1k〜10k対話のpilotを作る。speakerの向き、personaの扱い、tree復元、window化前のsplitを確認する。
- domain別bytes、短文比率、会話長、品質のsample目視を記録する。会話の定型挨拶を文書重複と同じ基準で一律削除しない。

**成果物（作成済み）**: `data/phase1/processed/`の`dataset_manifest.parquet`、`split_manifest.json`、`corpus.jsonl`、`tokenizer_sample.jsonl`。data/dialogue report・レビュー・検証・再生成比較は`reports/phase1/`。[詳細・checksum・再生成手順](17_phase1_completion.md)

**完了条件**: 任意の採用文書・対話をsourceとsplitへ追跡できる。既知重複とtrain/eval間の検出重複を除外し、未検出の限界も記録する。対話件数、unique bytes、応答文字数、turn数の分布が分かる。1024-token内に収まる割合と教師token数はPhase 2で計測・追記する。

**次へ進む判断**: 会話候補が不足する場合は独自会話例でmask/評価の開発を進めつつ候補を追加する。量の不足を、同じ少数対話を反復した見かけのtokensで解決したことにしない。

## Phase 2: 4k/8k Tokenizerと会話形式

**状態**: 完了。[実施結果・artifact・再現手順](18_phase2_completion.md)。同一sampleで全6coverage候補が合格し、両語彙で0.9995を採用。外部codecのgolden・全corpus round-tripと会話token量を実計数した。

**目的**: 小語彙でも日本語・記号を扱い、学習とローカル推論で同じID列を使う。

**ゴール**: 語彙4096/8192の二つのSentencePiece Unigram + byte fallback artifactと、共通の入出力契約がある。

作業:

- 同じtrain sampleでcoverage候補を比較し、必須文字・256 byte pieces・8特殊tokenを含む予算を確認する。
- 正規化、空白、改行、タブ、結合文字、顔文字、未知文字のgolden例を固定する。
- role/EOTを構造IDとして挿入し、本文中の同じ文字列表記と区別する。学習後の語彙追加を避ける。
- domain別chars/token、bytes/token、fallback率、context超過率と会話の総/教師tokensを測る。

**成果物**: 4k/8kの`tokenizer.model`、設定・sample hash、`special_tokens.json`、`tokenizer_contract_report.json`、`tokenizer_comparison.json`。

**完了条件**: piece数と特殊IDが期待値と一致し、golden例が定義したcanonical textへround-tripする。全byte piecesと異常入力を検証する。同じartifactでencode結果が再現でき、再学習時の一致範囲も記録される。

**次へ進む判断**: 圧縮率だけで勝者を決めず、両候補をPhase 5へ渡す。4kが予算内で成立しない場合はcoverage/前処理を再検討し、語彙数を黙って変更しない。[詳細仕様](13_tokenizer_dialogue_data_research.md)

## Phase 3: モデル・cache・学習前export

**状態**: 完了。[実施結果・artifact・再現手順](19_phase3_completion.md)。両モデルの実parameter数・forward/backward・1024までのcache、公式HF・native float GGUF、Q8/Q4の読込生成を検証。内蔵Tokenizerに不一致があるため外部SentencePiece経路を採用した。

**目的**: 10M予算と正しい因果生成を満たし、長期学習後に推論形式で詰まるのを防ぐ。

**ゴール**: T8K/T4Kがforward/backward・cache生成・保存読込でき、配布経路の計算とTokenizerを検証できる。

作業:

- RMSNorm、RoPE、GQA、head間gain共有QK-Norm、SwiGLU、tied embeddingを実装する。
- parameter count、未来参照遮断、GQA mapping、padding、finite gradientを検証する。
- prefill、1-token decode、chunk decode、長さの違うcacheで全系列logitsとの一致を検証する。
- ランダム重みをHF参照モデル、float GGUFへ写し、同じ入力IDsでlogits/cacheを比較する。
- 内蔵Tokenizerのgolden parityとEOT停止を検証する。不一致なら外部SentencePieceでencode/decodeする呼び出し経路を実装する。
- Q8/Q4候補で読込・生成、tensor別量子化型、FFN幅576/640でのfallbackと実容量を確認する。

**成果物**: T4K/T8K config、`model_contract_report.json`、`export_parity_report.json`、実行可能な推論入口。

**完了条件**: 提案仕様のQK-NormありでT8K=9,772,800、T4K=10,002,816 parameters。cache/因果性の検証が通り、floatの数値差が事前定義した許容値内。選んだ配布経路で学習時と同じTokenizer契約を再現できる。

**次へ進む判断**: 外部SentencePiece経路ならその依存も配布計画へ含める。汎用GGUF CLIへの互換性は別項目として記録する。ランダム重みの量子化成功は会話品質の成功を意味しない。[モデル仕様](12_training_implementation_research.md)、[export仕様](14_evaluation_deployment_research.md)

## Phase 4: 学習器・shard・再開・4090 benchmark

**状態**: 2026-10-03に完了。WSL 3.0.1.0 / Ubuntu WSL 2 / RTX 4090でCUDA/BF16確認と64 tests / skip 0、両モデルの200 vs 100+100完全一致、全dev・固定生成suite、最大batch・backend/compile・予算を実測・監査した。[完了記録と測定の制約](21_phase4_completion.md)を参照する。Phase 5も[完了](23_phase5_completion.md)し、Phase 6①〜⑤、5Bと各100M比較、10B準備が完了。本10B科学学習・保存確認・同条件品質評価は完了し、Base/Chat品質目標は未達。

**目的**: 長期runを失わず、実際の計算・ストレージ予算に収める。

**ゴール**: 実shardでの学習・中断再開が成立し、以降の実験時間を実測から見積もれる。

作業:

- `uint16` shard、document index、checksum、mmap loader、決定的shuffle/mixture samplerを作る。
- GPU実機検証の前にWindows PCのWSL 3.x/Linuxへ切り替え、同じcommit/config、Tokenizer、sample、hashを引き継いでCUDA動作を確認する。
- AdamW、FP32 parameter + BF16 autocastを基準にloss、gradient accumulation、schedulerを実装する。
- model/optimizer/scheduler/RNG、消費済みデータ位置、tokens/steps、全hashを保存する。optimizer更新境界で保存し、一時fileからのatomic renameを行う。
- Phase 0の準備run記録を基に、学習runの開始/完了/失敗、checkpoint、metricsのschemaと台帳を追加する。準備runの`tokens_seen=0`を学習結果として流用しない。
- Baseの本文NLL取得、window/strideの採点、BPBと生成suiteの実行を実装する。共通bytes・本文を一度だけ採点することを検証し、Phase 5の比較前に評価runnerを使えるようにする。
- 連続200 stepsと100 steps→保存→再開100 stepsを同一環境で比較する。
- T4K/T8Kのsynthetic/実shardでmicro batchを最大安定値まで増やし、compile、backend、data wait、peak VRAM、保存時間を測る。micro batchとeffective batchを区別する。

**成果物**: 実機`environment.json`、`handoff_report.json`、`resume_report.json`、`throughput_report.json`、`base_evaluation_contract_report.json`、`resource_budget.md`、復元可能checkpoint。

**完了条件**: Windows/WSLへ移行済みで、CUDA動作と引継ぎartifactの一致を確認する。再開前後の消費token列が一致し、loss/weightsが同一環境で許容誤差内。累積lossの正規化、shard境界、評価によるRNG干渉を検証済み。BPB runnerの本文一度採点・共通bytes分母と固定生成suiteの実行を確認する。compile初回と定常速度を分け、実shardで運用できる最大安定batchと速度が分かる。

**次へ進む判断**: `予定tokens / 実測tokens/sec + 評価・保存・停止・分岐の時間`で100M/1B/10B/20B/50Bを見積もる。raw、一時領域、4k/8k shards、checkpointの容量を合算する。予算外ならまずbatch/I/O/探索本数を調整し、実験条件を台帳へ記録する。

## Phase 5: overfit・10M smoke・100M比較

**状態**: 2026-10-03に完了。4本の100Mと補助予算を評価し、T4K / NoQK-Norm / LR 0.002を1候補に選定。全68 tests / skip 0、CUDA厳密resumeと独立監査が成功。品質の未達も[完了記録](23_phase5_completion.md)へ保存し、Phase 6①〜⑤、5Bと各100M比較、10B準備が完了。本10B科学学習・保存確認・同条件品質評価は完了し、Base/Chat品質目標は未達。

**目的**: 実装不備を小予算で見つけ、長期学習へ渡す候補を根拠で選ぶ。

**ゴール**: 100M時点で発散しない候補を最大2つ選べる。

作業:

- 小データ100件のoverfitでloss低下と学習例の再現を確認し、別runで10M-token smokeを行う。
- 100MでT4K/T8Kを比較する。次にQK-Norm有無、LR、必要ならMuon+AdamWを、一度に一つの主要因だけ変えて比較する。全組合せの総当たりは前提にしない。
- 同じvalidation文書のBPB、共通短文window、生成失敗、実時間、処理bytes、更新回数を保存する。
- 同一tokens、同一学習bytes、同一GPU時間の条件を区別する。補助比較は対応するcheckpointまたは別runで行い、条件が揃わない結果へ同じラベルを付けない。

**成果物**: `smoke_report.json`、`tokenizer_model_comparison.json`、候補config、`candidate_selection.md`。

**完了条件**: finite loss/gradient、保存再開、EOS生成の検証が通る。BPBの改善と失敗率の推移を比較でき、候補選定理由・棄却理由を記録する。100Mで自然な雑談が完成することは要求しない。

**次へ進む判断**: 候補がすべて発散・悪化する場合はデータ、mask、LR、batchを切り分けてPhase 2〜4へ戻る。BPB差が小さい場合は速度・fallback・生成失敗・推論互換性を含めて最大2候補を残す。

## Phase 6: 500M〜10B Base v1

**状態**: 主要Web10Bと同条件全文評価、日本語追加評価、100M/500M/1Bの配合・品質・学習量比較、短い物語pool200Mへの拡張と各1B比較を完了。最新の一次35/最終20evidencechecksは成功したが、Base/Chat品質は未達。旧研究候補の保存と最新候補の不採用を区別する。[最新結果60](60_dataset_expansion_results.md)、[次回案61](61_condition_preservation_next_plan.md)。最新学習速度は約676k〜683k tokens/s。原GPU基盤・再開・高速化の完了証拠を保持し再実行しない。

**目的**: 約10Mで日本語短文生成がどこまで成立するかを測り、Chatの土台を作る。

主系列10Bとその評価は完了済みで再起動しない。計画52の500M研究候補は元比較gateを通過したが実用品質未達、後続の教材内容/一定LR1B/200M教材比較は報告済み。最新結果は[60](60_dataset_expansion_results.md)。次回の一区切りは[提案61](61_condition_preservation_next_plan.md)の限定教材品質比較と採否・停止であり、文書更新では実行しない。

**ゴール**: 選定済み10M候補を直接10Bまで学習・評価し、10Bの`JMicro-10M-Base-v1`と固定評価を残す。

| 累積tokens | 目的・判断 | 残すもの |
|---:|---|---|
| 500M | 初期改善と反復悪化の確認 | checkpoint、BPB/生成/速度 |
| 1B | 日本語生成の立ち上がり、候補最大2つ | 比較表、候補更新理由 |
| 2B | 過去355M/約2B経験との観察点整理 | 規模・Tokenizer・データ差を明記した記録 |
| 5B | 本命1つの決定 | 選定reportと継続config |
| 10B | Base v1の固定評価 | weights、Tokenizer、model card、全評価 |

作業（500M〜10Bの学習・同条件評価は完了。品質未達は保持）:

- 既存12.23B trainを使う。50〜100B master候補全量の取得を先行せず、実量と目標を混同しない。
- 各段階に必要なshardsから用意し、未使用全量の処理を10B開始の前提にしない。
- BPB、短文品質、反復、EOS、Unicode、追加GPU時間を段階ごとに記録する。
- 固定mixtureのscaling系列を残す。目的に合わせたmixture変更は別条件として記録する。
- Phase 5でWSDを採用し、Phase 6②でstable/decayの実装・CUDA全state再開/分岐完全一致を確認済み。現在のbatch/backend/数値配分は[直接10B専用設定](../configs/phase6/base_10b.json)へ凍結済み。従来version2は保持する。継続stable枝と評価decay枝を区別して追加computeも計上する。StableExtensionTrainerの明示forkは実装・10B準備検証済み。20B/50Bには新しい予算・履歴・再開確認が必要で、通常resumeでは予算を変更しない。

**成果物**: 段階checkpoint、`base_scaling_report.json`、`base_v1_evaluation.md`、継続用checkpoint、master corpus manifest。

**完了条件**: 本命の10B checkpointを再構築・再開でき、固定suiteとheld-out corpusの結果がある。短文の文法・関連性と破綻例を人手で確認し、[品質目標](#品質目標と判断ルール)の達成/未達を明示する。過去モデルのartifactがない場合は直接比較を未実施と明記する。

**次へ進む判断**: Baseの日本語生成が成立すればPhase 7へ進む。成立しない場合は量だけを増やさず、日常短文mixture等の対照実験を行う。修正後も未達なら容量・データの限界として報告し、成功扱いにしない。

## Phase 7: Dialogue mid-trainingとAssistant-only SFT

**目的**: 流暢な続きを生成するBaseから、入力に関連した短い応答で会話を続けるChatへ移す。

**ゴール**: 文法・関連性・2〜数ターンの文脈・停止を評価した`JMicro-10M-Chat-v1`を作る。

作業:

- Phase 1の会話pilotを拡張し、sourceごとのunique対話/bytes/総tokens/Assistant教師tokens/反復回数を固定する。
- Dialogue mid-trainingのmixture、loss範囲、LR、pilot予算と拡張上限を開始前にconfigへ記録する。
- 主系列はBase→mid-training→SFT。小規模なBase→SFT対照を残し、mid-trainingの効果を分離する。
- role metadataからAssistant本文+EOTの教師maskを作る。shift、PAD、教師0件、長い対話の古い完了turn切り捨てを検証する。
- SFTの累積総系列10M→30M→100M tokensを候補とし、毎段階devで比較する。教師token数とunique量は別記録し、悪化時は100Mまで強制継続しない。
- Base、mid-training後、SFT後を同じ固定prompt/seedで比較する。greedyと複数seed sampling、人手rubricと自動失敗率を分ける。
- Phase 0の固定履歴suiteに加え、モデル生成を履歴へ戻す2〜数ターンのrolloutと自動失敗flagを実装する。モデル名を伏せた人手評価と評価者一致率を記録する。

**成果物**: 会話manifest、`assistant_mask_report.json`、各段階checkpoint、`chat_ablation_report.json`、`chat_v1_evaluation.md`。

**完了条件**: mask/停止の検証が通り、独立した対話splitで評価済み。採用checkpointがdev上で関連性・文脈を改善し、反復・役割混同・空応答・停止失敗・Base流暢性の退行を報告する。最後に未使用testで品質目標を判定する。

**次へ進む判断**: 最良checkpointを選びPhase 8へ。未達なら応答長/品質/mixture/LR/反復回数を一要因ずつ見直す。蒸留を使う場合はcorpus-only baselineと別系列にする。

## Phase 8: 量子化・ローカル実行・再現手順

**目的**: 学習結果を手元で使える形にし、容量と品質の実際のtradeoffを示す。

**ゴール**: Base/Chatのfloat版と採用量子化版を、学習環境以外でも手順から起動できる。

作業:

- 学習済み重みでPhase 3のHF/float GGUF parityとcache/停止を再実行する。
- Q8とQ4候補を比較し、tensor別実型、file容量、Tokenizer込み全artifact、RSS、cacheメモリを測る。
- 対象CPU/OS/threadsを明記し、load、初回token時間、prefill/decode、応答総時間のp50/p95を測る。context1024は生成分も含めて管理する。
- floatとの差をBPB、人手関連性/文脈、Unicode、反復、role/停止で確認する。
- model card、採用source一覧、帰属、既知の限界、hash、runtime commit、量子化設定、実行/再現コマンドを揃える。

**成果物**: Base/Chat artifacts、`quantization_report.json`、`local_inference_report.json`、`reproduction_guide.md`、配布manifest。

**完了条件**: 独立環境でBase completionと2〜数ターンのChatが動く。学習時と同じencode/decode、EOT/EOS停止が成立し、量子化の退行を品質条件内に収める。全容量・速度・必要依存を実測値として提示する。

**次へ進む判断**: Q4が品質を満たさなければQ8/混合精度も比較する。5〜10MB級へ収まらない場合はサイズ目標未達を明記し、形式/precisionの追加検証を残す。artifactを用意したことと品質・容量目標達成を区別する。外部公開・Hub uploadはこの文書作成では実行しない。

## Phase 9: 20Bと条件付き50Bのscaling

**目的**: 固定10Mモデルへ追加学習する価値と、容量/データ反復の限界を確認する。

**ゴール**: 10B対20Bの差を測ってBase v2を評価し、50Bへの進行/停止を根拠で決める。

作業:

- 実装済みstable予算延長forkについて新20Bの固定条件・履歴・全state検証を確認してから継続用checkpointで20Bへ進み、固定mixture・同じ評価条件で10Bと比較する。通常resumeで終端budgetを変更しない。
- document単位のpaired bootstrapでBPB差と95%信頼区間を記録し、短文品質、失敗率、uniqueデータ露出と追加GPU時間を併記する。
- 50Bは20Bでも改善継続があり、生成失敗が悪化せず、追加時間/ストレージが予算内の場合のみ進む。
- 新Baseが有望なら同じChat手順を適用してv1と比較し、Phase 8の学習済みexport/量子化評価も再実行する。

**成果物**: `base_v2_evaluation.md`、`scaling_extension_decision.md`、実施した場合の50B checkpointと限界report。

**完了条件**: 20Bの比較と50B Go/No-Goを記録する。50Bを実施した場合は評価まで完了する。実施しない判断にも改善量、信頼区間、失敗率、予算の証拠を付ける。

**次へ進む判断**: 小さい改善しか残らない/悪化する場合は停止し、データ適合性またはPhase 10の比較へ移る。decay済み評価枝とstable継続枝の履歴を混同しない。

## Phase 10: 追加研究とVast.ai並列比較

**目的**: 完成したTransformer baselineと比較して、能力密度・計算効率をさらに改善する。

**ゴール**: 変更ごとに同じ目的・評価条件で採用/棄却を判断できる。

優先順はLayer Sharing（12 unique/24 logical）、teacher応答テキスト蒸留、ReLU²、Mamba2+Attention、Conv+Attention、5M/10M/25M/50M/100M規模比較。各実験では「改善したいmetric、parameter/compute予算、同一条件、採用基準」を先に記録する。異なるTokenizer間のlogitsをindexで直接KL比較しない。

Vast.aiはローカルで検証済みの独立runを並列化する後半用途に限定する。利用時の価格で再見積もりし、既存方針の上限$1,000に対して実験別計算時間・storage・失敗時費用を計上する。この計画作成で課金jobを開始しない。

**成果物**: 追加研究proposal、対照run、`research_comparison.md`、費用/速度/品質の台帳。

**完了条件**: 実施した各変更をbaselineと比較し、採否・限界を記録する。採用案は再現性、Chat評価、export、量子化まで再検証する。候補全部の実施を最初のBase/Chat完成条件にはしない。

**次へ進む判断**: 品質または速度が事前の採用基準を満たす変更だけを次の比較へ進める。改善が不明確な変更は結果を保存して保留し、追加computeで得られる情報と費用から再実験の優先度を決める。

## 品質目標と判断ルール

技術的完了と能力目標を別に管理する。Phase 8までのartifact・検証が揃っても、以下が未達なら「目的を達成した」とは記載せず、未達metricと次の対照実験を残す。

以下の数値はPhase 5の100M候補の結果を見る前に、初期提案を維持して**凍結済み**。10Mで達成できると実証した値ではない。Phase 0でsuiteと採点例を定め、Phase 5のdev/pilot評価では未達もそのまま記録する。変更理由と旧値を記録し、最終testを見て閾値を下げない。量子化の退行幅はfloat dev評価後、量子化候補選定前に別途固定する。[凍結の記録](22_phase5_plan.md#公平な評価と候補選定)

| 目的 | 判定方法・初期目標 | 判定するフェーズ |
|---|---|---|
| 日本語短文生成 | Base completionの文法2/2が70%以上。文字/記号の破綻と反復も別集計 | 6 |
| 入力に関連する短い雑談 | Chatの文法・関連性が両方2/2の応答が70%以上。文字数分布も併記 | 7 |
| 2〜数ターンの文脈維持 | 2〜4ターンsuiteで直前の条件/訂正を保持し、文脈2/2が60%以上 | 7 |
| 会話の停止と役割 | 停止成功95%以上、空応答5%以下、役割漏出1%以下、Unicode破綻は固定suiteで0件 | 7・8 |
| 量子化して使える | 全artifact容量5〜10MB級を目標に、floatとのBPB/品質/失敗率差を報告。許容退行幅はfloat dev評価後、量子化候補選定前に固定 | 8 |
| 長期学習の継続価値 | BPB改善幅（10B BPB − 20B BPB）の95%信頼区間の下限が0を越え、生成失敗に重大退行がなく追加予算内なら50B候補 | 9 |

停止等の失敗率はgeneration抑制設定を併記し、ID列で測る。人手評価はモデル名を伏せ、文法/関連性/文脈を各0/1/2で採点する。率は分母とsample数を付け、全体だけでなくcategory別も報告する。関連性が伸びても反復が増える等の重大退行は採用判断へ反映する。

品質条件はdevで選定し、独立testで最終確認する。testで未達なら結果を報告し、次の改訂では新たな未使用testを用意する。[評価の詳細](14_evaluation_deployment_research.md)

## 横断して残す記録と最初の着手順

全runでcode commit、config、依存version、Tokenizer/data hash、seed、tokens seen、unique docs/bytes/tokens、更新数、micro/effective batch、wall time、失敗理由を残す。SFTでは総系列tokensとAssistant教師tokens、WSDでは分岐ごとの履歴を分ける。比較する条件を変えたら別run IDにする。

Phase 0〜4の骨格・データpilot・Tokenizer・両モデル/cache/export・Windows/WSL移行・学習器・評価・保存再開・実機速度は完了済み。Phase 5のoverfit/smoke・4本の100M比較・候補選定が完了し、Phase 6①〜⑤、5Bと各100M比較、10B準備が完了。本10B科学学習・保存確認・同条件品質評価は完了し、Base/Chat品質目標は未達。巨大コーパス全量取得、50B開始、追加hybridを先行しない。

具体的な着手checklistは[次の実装タスク](10_next_steps.md)、各技術判断の根拠と実測待ち項目は[追加調査](11_technical_research_gaps.md)を参照する。

## 2026-10-05追加: 長期の改善・完成計画

ユーザーの「もっと長期的な計画」に対する提案。今回は計画のみでデータ作成・GPU評価・学習は開始しない。契約75〜79の不採用判断と停止境界を維持する。次回の実行範囲を定めて再開する。本節は品質基準を変更する実験契約ではなく、Phase 6の未達からPhase 7・8、条件付きPhase 9・10までを接続する方針である。

### 出発点と到達点

現在は約10MパラメータのBaseを約10B入力tokens学習済みだが、自然な続き・反復・停止が未達。直近の各100M教師比較は意味評価58.333→64.583%に対し、一貫性6→3/80、適切完結6→2/80、EOS30→7/80だった。[結果79](79_narrative_diversity_results.md)の教材は量に加えてsource・長さ・EOS密度も変わり、これだけで「増量が無効」「容量不足」「精度全体が有意に悪化」とは結論できない。自然64文の記憶成功も、未見文への汎化を保証しない。[結果72](72_root_cause_diagnostic_results.md)の数値7失敗は未解決として残す。

最終目標は、**10Mを維持して、短い日本語を自然に完結できるBase、2〜4ターンの短い雑談ができるChat、量子化したローカル成果物**を作ること。汎用大規模LLM並みの知識や推論は完成条件に含めない。Base文法70%以上、Chat文法・関連性70%以上、文脈60%以上、停止95%以上等の既存目標を維持し、未達を完成と扱わない。全成果物5〜10MB級は目標であり、Tokenizer・runtimeを含む実測で確認する。

### 段階と判断条件

| 段階 | 目的・主な作業 | 完了条件・次の分岐 |
|---|---|---|
| 1. 根本原因の切り分け | 正解を与えた予測と自由生成を比較し、最初の意味逸脱、EOS順位、反復、64/256tokensの打切りを調べる。必要なlabel/mask/cache/数値経路を修正する | 有力仮説と対照条件を固定。[計画80](80_generation_transfer_plan.md)の診断後、EOS重み・文の長さ・教材内容のうち一つずつ比較する |
| 2. 日本語教材の再設計 | 日常の完結文、因果を持つ説明段落、良質な一般日本語を段階別に用意。引用・条件・否定・時系列・数・照応を含める | 内容確認、独立dev、実文書数・準備tokens・EOS密度を記録。小教材から広げられる供給を確認 |
| 3. 学習方法と構成の選定 | 現10Bからの追加学習と、良い教材で同じ10Mを最初から学習する方法を比較。必要時は同程度の10Mで深さ/幅/embedding配分を比較 | 未見文の生成・BPB・学習曲線・実時間から本学習候補を選ぶ。追加学習の失敗だけで容量限界を断定しない |
| 4. データ量と学習量の分離 | 教材量だけ変える比較と、同じ教材で学習量だけ増やす比較を行う | 独立教材の不足、繰返し学習の不足、品質/構成の問題のどれに投資するかを実測で決める |
| 5. 改善Baseの本学習 | 固定レシピで1B→2B→5B→10Bの節目を評価。効果に応じ良質な教材を2〜5B規模へ広げる | 生成品質とBPBの採用条件を満たすBaseを確定。伸びが止まれば同じレシピの増量を止める |
| 6. Chat化 | Base→SFTと、対話の中間学習→SFTを比較。Assistant本文＋EOTを教師にし、訂正/否定/2〜4ターンを評価 | Chat文法・関連性70%、文脈60%、停止95%等を達成。未達は原因別にBase/対話教材へ戻す |
| 7. 量子化とローカル利用 | float/HF/GGUFを照合しQ8/Q4を比較。WebUIに採用重みを接続しWindows側等でも確認 | 品質退行が事前の許容内、Unicode/停止正常、容量・RAM・応答時間を実測。再現手順と成果物を保存 |
| 8. 完成後の拡張 | 固定レシピの10B対20B、条件付き50B。必要時に蒸留や重み共有を別実験で検討 | 追加学習のBPB改善の信頼区間と生成品質・費用が既存条件を満たす場合だけ進む。20B/50Bは最初のChat完成の前提にしない |

### 比較の規模と研究の上限

**段階1:** 診断は学習0・GPU上限600秒案。原因別の学習比較は各条件100M body/EOS教師tokens、最大3組、計600Mまでを初期研究枠とする。1組ごとに結果を見て次の仮説を選び、全組を自動実行しない。100M比較の中間品質gate（一貫性・適切完結各27/80以上、EOS37/80以上、反復18/80以下等）は既存条件のまま。一つの失敗は次の仮説へ進む材料にするが、失敗した候補を採用したり、旧契約で条件付きだった追加500Mを開始したりしない。3組で改善根拠が出なければ同種のEOS微調整を終了し、段階2・3へ研究対象を変える。

**段階2:** 準備量はまず10〜50M、次に100M、500M、供給と効果が確認できたら2〜5Bを目安にする。2〜5Bは短物語だけの要求ではなく、一般日本語を含む教材全体の規模。既存Web約12.23Bと公開sourceを優先利用し、600B全量取得は行わない。SimpleStories-JAは合成教材であり、人手の自然文と区別する。文書数を名前置換で水増しせず、同じ物語系列・著者/sourceの漏れを分割時に扱う。新poolの必要な照合だけを行い、既存巨大コーパスの全面再照合は繰り返さない。固定sampleの内容確認は最大2回の選別改訂までとし、不合格ならsource/作り方を変更する。診断用に外していた引用・条件構文は長期教材全体から排除しない。

**段階3:** 追加学習対最初からの学習は各100M、根拠がある場合のみ各300Mへ伸ばす。過去10Bの履歴・optimizer・LRが異なるため、これは学習戦略の比較であり容量だけを検定する比較ではない。構成変更が必要なら追加候補は最大2つとし、現構成も含め同じ教材・新規初期化・同じ予算で比較する。現行4k Tokenizerと過去の8k比較を理由なくやり直さない。Tokenizer比較が必要なら共通byte BPBとtokens/bytes/GPU時間を併記する。候補選定と品質合格による採用は別に記録する。

**段階4:** 教材量の比較案は、source・長さ・EOS密度を揃えた入れ子の**100M対500M準備tokensを、各1B教師tokens学習**する二条件。学習量の比較案は、**同じ500M準備tokensで100M/500M/1B/2B教師tokens**の節目を測る。後者は同じ安定学習経路のcheckpointを再利用し、毎回最初から学習しない。教材量比較の500M側も条件が同じなら再利用する。この構成なら主経路は最大3B教師、評価用decay枝は例えば25M×4＝100Mを別会計とし、約3.1B以内の枠に収める。途中の正確な配分は実験前に固定する。

LRの違いを学習量の効果と取り違えないよう、共通の安定経路と同じ長さのdecay評価枝を分ける。準備tokens、実際に触れた文書/tokens、反復を含む教師tokens、valid入力tokens、physical tokensを別記し、概算のepoch数だけで比較しない。主要な比較点で全日本語評価と固定80件の内容評価を行い、間の進捗は小devで見る。結果の再採点や全suiteの不要な反復を避け、最終候補だけ別seedでも確認する。

**段階5:** 本学習前に採用レシピ・最大10B教師予算・評価点・退行/停滞による終了条件を固定する。1B/2B/5B/10Bは新経路の教師予算であり、現10Bから継続する場合は「親の約10B入力＋追加教師」を分けて表示する。研究として学習曲線を見ることと、品質合格として増量を承認することを混同しない。予算終了でも未達ならどの能力が伸びなかったかを報告し、データ・構成・目標の見直し案を出す。10M不可能と断定したり目標を無断で下げたりしない。

**段階6以降:** SFTの10M→30M→100Mは既存ロードマップ通り**総系列tokens**の候補節目で、Assistant教師tokensを別に計数する。Baseの自由生成が未達の状態でSFTだけで治る前提に進まない。量子化の退行上限はfloat devの後・候補選定前に固定する。外部公開、第三者への連絡、有料cloudは本計画の実行範囲に含めず別の指示に従う。参照用の大きい教師モデルを検討しても、学習対象の10Mは維持する。

### 評価・期間・見直し

BPB、意味/文法の選択式評価、自由生成の文法/関連性/一貫性/適切完結、EOS、反復、Unicodeを併用する。gold EOS尤度だけ改善しても自由生成が止まるとは限らない。64tokensの凍結評価は維持し、256tokensは打切りと本当の不停止を見分ける診断として別報告する。採点基準を先に固定し、可能ならモデル名を伏せた人手レビューを加える。これまでの非blind Codex評価を独立した人手評価とは記載しない。devで選定し、保護したtestは最終レシピ凍結後に一度使う。必要時は実験前に新しい未使用holdoutを確保する。

最初の研究サイクルは**4〜6週間を見直しの時間枠**とする案。前半に診断・教材・小規模の戦略比較、中盤に学習曲線とBase本学習、後半はBase合格時にChat/量子化へ進む。Base未達なら後半を教材/構成の再設計に使う。これは作業配分の提案であり品質達成や全Phase完成の納期ではない。各段階の予算到達時に得た証拠と残課題から次の範囲を決める。

直近100M教師の学習本体は約150〜163秒。現レシピの計画用速度を約0.60M教師tokens/秒と置くと、100M約3分、1B約28分、2B約56分、5B約2時間20分、10B約4時間40分が**学習本体だけ**の目安。評価・compile・保存・教材準備は別で、構成/長さ/batchが変われば再計測する。長期計画の不確実性は学習時間より良質な教材の供給・実装修正・内容評価に大きいため、それぞれに比較本数と完了条件を設ける。

### 計画の根拠と限界

[TinyStories](https://arxiv.org/abs/2305.07759)は小型モデルでも単純な英語物語で一貫した生成ができる例を示し、狭い教材から学ぶ方針の参考になる。ただし日本語10Mで本プロジェクトの目標が達成できる証拠ではない。[Chinchilla](https://arxiv.org/abs/2203.15556)の計算最適性の実験は70M〜16Bモデルを含む研究であり、10M日本語に「最低2〜5Bが必須」という閾値を与えない。教材量・学習量・構成を分けて測る方針はこれらを踏まえた本プロジェクトの提案である。

[非停止と復号の整合性の研究](https://aclanthology.org/2020.emnlp-main.448/)はgreedy等の復号で非停止が生じ得ることを示す。今回の原因を確定するものではなく、正解経路と自由生成、学習された停止と生成側の制限を分けて診断する根拠として用いる。

### 段階1〜3の再開と、300M後の次案（2026-10-05）

新しい実行目標「3までをより詳細の計画を立てて進めてください」は上記長期段階1〜3。詳細の凍結契約はdocs/80_generation_transfer_plan.md末尾、generation_transfer/curriculum_strategy/strategy_extension各configにある。昔の短期契約の不採用判断を変更しない。

段階1は学習0の実診断。新候補train32はgreedy64のEOS9から256のEOS28へ増え、上限による切断を一部確認。ただし公式Web dev32は両モデル256でもEOS0で、長さだけでは解決しなかった。段階2は短文供給不足v1と内容弱20/64のv2を保存し、v3で10,000,208準備tokens/73,260全文、dev500,319/3,690を確保。short1M/物語4M/Web5Mの組成、固定64の弱10/64。SimpleStories-JAは合成、残る擬人化/幻想/一部宣伝を限界として記録した。新pool内の局所family分割を既存全corpusの完全近重複保証とは呼ばない。

段階3の各100M実教師比較は、元10B追加対新規同10Mの学習戦略比較。BPB1.070892/1.413020、意味66.146/51.563%、EOS31/12、一貫性6/6、適切完結11/6（各80）。両候補の採用条件は未達。新教材dev32の学習前後に限れば、両条件でBPB・EOS・4gram再出現が改善し、事前の研究延長条件を満たした。Web補助devは親のtrain既知文書を含むので、公式未学習devの改善と区別する。

条件付き延長は各100MのAdam/RNG/文書shuffle cursorを引継ぎ、追加200Mで各累積300M。元peakへ戻す段階的reheatと追加区間90%stable/10%decay、warmupを再実行しない。これは連続300M学習とは異なる経路。全段階3のGPU上限1800秒と既存品質基準を維持し、両300Mの共通日本語と全160個別内容、採否・元UI復帰・local commitで今回停止する。100Mの準備tokensと反復を含む100M教師を混同しない。

**その後の計画は以下の提案であり未開始。**

1. 300Mの100M比をまず確認する。BPB/選択式だけ改善し、主体・時系列・否定・因果や自由生成が改善しなければ、同じ教材の大規模継続を優先しない。過去履歴/LRが異なるので、freshが弱いことを容量不足の証拠にしない。
2. 次の教材は幻想・擬人化・宣伝への残存偏りをsource/編集単位で減らし、日常の行動と結果、説明、数・否定・照応を保つ。現v3の受け入れ基準を事後に変更したり、失敗sampleを無限に抽き直したりせず、別source/別契約として作る。まず10〜50Mの供給・固定内容sampleを確認し、同じ総教師量で比較する。大量全面照合は行わない。
3. 良質な教材でgoldは学べるが未見生成が伸びない場合は、10M内の構成を比較する。現13層/幅256/FFN640（10,001,152）を対照に、9層/幅256/FFN1040（10,011,392）、6層/幅384/FFN832・heads6/KV3（9,982,848）を最大2候補とする。countsはCPU構築による計数だけで学習性能の証拠ではない。Tokenizer4096、GQA比2、head64、NoQKNorm、context1024、tied embeddingsを維持する。全条件を新規学習・同教材順序・同seed/teacher budget（案各300M）・同LR条件で比較し、構成ごとに安定batch/CUDA保存再開を確認。幅/深さ/embedding比が一緒に変わる候補の比較であり、単一要因の容量検定とは呼ばない。設定はreports/phase6/strategy_architecture_proposal.json、未起動。
4. 教材・学習戦略/構成に候補ができた段階で、段階4のデータ量と学習量を分ける比較へ進む。source/長さ/EOSを揃えた入れ子100M対500M準備tokensを各1B教師、同500M教材の100M/500M/1B/2B教師checkpointを比較する。100Mという数字が準備量か教師量かを全表で明示する。供給不足時は利用可能な規模へ実験契約を書き直し、未準備500Mを用意済みと扱わない。品質不合格候補を実用Baseへ採用しない。
5. 改善のあるレシピを選べたら1B→2B→5B→10B教師の本学習へ。Base品質を満たしてからChat/量子化に進む。20B/50B、test、公開、pushは今回の範囲外。

### 段階1〜3の実結果と、次の優先順位（2026-10-06 JST）

凍結契約80の長期段階1〜3は、根本診断・10M以上の教材pilot・各100Mから条件付き各300Mまでの戦略比較・採否・元UI復帰を完了。実装の完了と生成品質の達成は別で、両候補は不採用。上の「300M後の次案」の優先順位を、以下の実結果で更新する。新しい研究は未開始。

| 条件 | 準備教材tokens | 今回の累積本文/EOS教師 | 共通dev BPB↓ | 基本意味 | JBLiMP | JCQA | EOS/80 | 自動反復/80 | 一貫性/80 | 適切完結/80 | Unicode破綻/80 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 元10Bから追加・100M | 10,000,208 | 100,000,000 | 1.070892 | 66.146% | 75.227% | 32.350% | 31 | 13 | 6 | 11 | 0 |
| 同10M新規・100M | 10,000,208 | 100,000,000 | 1.413020 | 51.563% | 74.018% | 25.648% | 12 | 16 | 6 | 6 | 0 |
| 元10Bから追加・300M | 同上 | 300,000,000 | 1.255773 | 55.729% | 75.529% | 26.899% | 31 | 5 | 8 | 15 | 1 |
| 同10M新規・300M | 同上 | 300,000,000 | 1.605410 | 49.479% | 71.299% | 26.542% | 22 | 2 | 5 | 13 | 1 |

同じ教材を繰り返した学習量比較であり、データセット固有量を増やした比較ではない。追加側の親は10,000,007,168入力tokensで、新規側の親は0更新/入力/教師、両者の歴史・LR・Adamも異なる。300Mは100M終端から元peakへ戻した追加200Mの段階的reheatで、連続300Mとの同一性は主張しない。自動反復カウンターの減少を、すべての意味的反復の解消とは扱わない。

100M→300Mで訓練中の損失は下がる一方、公式dev BPBと基本意味が悪化した。教材への過適応、一般分布の忘却、LR再加熱の影響が次の仮説であり、これだけで原因を確定しない。新規側も300Mで改善Baseにはならず、学習量不足が完全に否定されたとも10Mが不可能とも言わない。両条件とも既存一貫性/適切完結27以上・EOS37以上・raw Unicode0・BPB等の採用基準を満たさない。

次回の具体的な順序:

1. **損失とLRの切り分け。** 既存metrics/100M・300M重みを使い、同じ小train/devのBPBと、同じprefixの生成を並べる。必要な新GPU測定は小sampleのみとし全suiteを無用に反復しない。追加検証案は同じ100M重み/Adam/RNG/順序から、今回のreheat枝に対して終端LRを上限とする低LR枝を各同量200M教師で比較する。今回のreheat結果は再学習せず再利用する。仮説は「LRを戻した影響か、同じ教材を反復する影響か」、変更はLRだけ。実行前にbudget/scheduleと改善・終了条件を別契約で凍結。trainだけ改善してdevが悪化する条件を長期レシピへ選ばない。
2. **教材改訂の同量比較。** 現v3の幻想/擬人化/宣伝や、主体・数・因果の弱い教材を、別source/編集単位の自然な日常完結文・説明へ置き換える。まず10〜50M準備tokensと局所分割・固定64内容を確認する。新規学習の対照と改訂を同じ教師量・LRで比べ、増量と品質変更を区別する。現v3の閾値や失敗sampleを事後変更しない。旧巨大corpus全面照合は繰り返さない。
3. **10M構成の比較（条件付き）。** 良質な教材でgoldの学習は機能するが未見生成が伸びない場合、上記現13層256と提案9層256/6層384を全条件fresh・同教材/seed/teacher budgetで比較する。最大2新候補、各300Mは予算案で未起動。CPUによるパラメータ計数を能力の証拠にしない。
4. **固有データ量と学習量の分離。** 有望な教材・学習設定ができれば、入れ子100M対500M準備tokensを各1B教師で比較。同500M教材を100M/500M/1B/2B教師の節目で評価する。安定経路と同量decay評価枝を実行前に固定してLRによる交絡を減らす。供給・効果が出た後に良質な準備量を2〜5Bへ広げる。
5. **改善Base→Chat→量子化。** 品質を満たすレシピで本学習を進め、採用Baseを確定してから対話学習と量子化へ進む。品質達成までの期日は未確定。今回の停止境界を越えて自動開始しない。

科学教師は合計600,000,000、valid/physical入力604,504,064、実CUDA再開32 optimizer updates/検証教師1,040,748は別会計。段階3GPU1396.456秒（上限1800秒）、診断76.895秒（上限600秒）。CPU変更関連tests、実CUDA再開、全四終端の教師/LR/保存state/共通bytes評価、320個別内容と完了監査は成功。内容判定は非blind Codexで、独立人手認証は未実施。結果72の数値7失敗は残している。

可搬証拠はreports/phase6/generation_transfer_review.json、curriculum_strategy_ready/content_v2/v3・review/annotations、strategy_extension_eligibility/review/annotations、strategy_scope_completion.json、strategy_scope_evidence.json.gz（153members/32,891,478bytes）。全rawのsource/metrics/gold/generation/失敗/理由を保存し、checkpoint/shards/corpusはWSLへ保持。モデル・dataの設定/hashは三つの凍結configへ結び付く。元10B UIのactual444875/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start9599628、HTTP親SHA410f975d…/10,000,007,168/busy=falseを確認。科学396752/426421、基準429834、延長441415は終了・不在。local commit後に停止し、段階4・新構成学習・Chat・20B/50B・test・push/公開は未開始。

### 実行再開契約: 提示した項目1〜5（2026-10-06 JST）

ユーザーの「5まで進めてください」で、直前の五項目全体を再開する。1)同じ100M出発でLR切り分け、2)10〜50M教材改訂の同量比較、3)必要時の10M内構成比較、4)入れ子100M/500Mの教材量と同教材100M〜2B教師の学習量比較、5)改善Base本学習1B/2B/5B/10Bから、採用Base→Chat→量子化/ローカル検証までが実行対象。昔の段階1〜3の停止は今回の再開で解除される。診断や準備だけ、候補不採用だけでこの目標を完了としない。

1は既存100M/300M履歴を再利用し、固定train32/dev32の学習前後を測る（新科学学習0/診断GPU300秒以内）。元各100M重み・Adam・RNG・教材順序から、100M終端LR以下をpeakとする追加200Mを各条件実行（教師400M、同じ90%stable/10%decay、warmupなし、各学習600/比較評価1800秒）。既存reheat枝は再学習しない。実CUDA保存再開、公式dev256/全日本語と固定各80内容を確認し、train/dev悪化とLRを切り分ける。候補の採用gateを変更せず、LR選定と実用Base採用は別に記録する。

2は現教材の幻想/擬人化/宣伝や主体・数・因果の弱い部分を改善する。現v3や古いreportの閾値・原文・判定を変更しない。新source/編集単位を別versionで準備し、10〜50M pilotの局所exact/family分割と固定64内容を確認する。一度のsource/selector比較は準備CPU600秒×最大2改訂、同量の各300M以下教師/GPU1800秒枠として凍結し、失敗なら次のsource/仮説へ有効に進む。trainだけ改善する条件は本学習へ採用しない。引用/条件/否定/時間/数/照応を保持し、自然文と合成の由来を表示する。

3は良い教材でgoldは学べるが未見文が弱い時に、現13層256・提案9層256/6層384の最大2新構成を、全条件fresh・同Tokenizer/教材/seed/教師量/スケジュールで比較する。各300M教師を初期上限、構成ごとに実CUDA安定batch・連続/再開を確認。GPU各600秒学習＋共通評価、全比較3600秒枠を実行前に固定。容量不足を先に断定しない。

4は新しい固有教材100M/500Mの供給を実確認してから、source/長さ/EOSを揃えた入れ子の各1B教師比較を行う。同500M教材の安定経路100M/500M/1B/2B節目に同量decay評価枝を使う。基準を見て学習量を決め、量が用意できない場合はsource供給を改善して進める。旧巨大コーパス全量再照合は行わない。全初期研究は主経路約3B＋評価枝約100Mの案で、正確な量・計測時間・停止条件は準備後にconfigへ凍結する。準備量、実露出、教師量、valid/physical、EOS/bytes/時間を別会計とする。

5は選定したレシピの安定経路1B/2B/5B/10Bを評価し、Baseの既存品質目標を満たすまで教材/設定/構成の有効な次の仮説へ戻る。未達を達成として報告しない。採用Base後にChatの10M/30M/100M総系列tokens（Assistant教師別）、Assistant本文＋EOT、2〜4ターン/訂正/否定/停止を学習・評価。float/HF/GGUF parity、Q8/Q4品質/容量/速度、実WebUIと再現手順を揃える。技術的成果物だけで全目標達成としない。

実行中は永続job/PID/boot/start/ログ/checkpointとstage ledgerを保存し、各有意なmilestoneでchecks/status/local commit。GPU占有時にUIを停止しjob終端で元の採用UIを復帰する。保護testは既存ロードマップの最終レシピ凍結後の用途だけで、日常の教材選別に使わない。20B/50B・外部公開・push・有料cloudは別の範囲で今回自動開始しない。独立した人間のblind評価は未実施と表示し、実際に取得していない人間評価を作らない。


### 五項目stage2の教材比較結果（2026-10-06 JST）

同じfresh0重みから、従来v3と固定64弱8のWikipedia説明文を各300M教師・LR.002/warmup200・連続90stable/10decayで比較した。科学600M、valid/physical604,766,208、GPU1148.505秒。各80のEOS18→54に対し、一貫性/適切完結9→0、共通Web BPB1.637138→2.103709、Unicode0→1。両候補不採用で全目標未完了。Wikipediaは本学習の単独レシピへ採用しない。内容確認と教師予測の改善は自然生成の合格を保証しなかった。自source dev32も反復20/32なので、条件付きstage3の2新構成で同教材・同LR・同300Mの内部汎化と一般生成を比較する。現構成のmatched300Mは再利用し、新科学は最大600M。sourceの不足と構成はまだ単独原因として確定していない。量比較時の教材は広い日本語と日常文を保持する必要がある。証拠reports/phase6/material_comparison_review.jsonとannotations/rawtar、実行config material_comparison.jsonを参照。

### 五項目stage3の構成比較結果（2026-10-06 JST）

同じWikipedia10M教材・Tokenizer4096・seed42・fresh各300M教師・LR.002/warmup200で最大2新構成を比較した。現13層の300M結果と80件の採点は再利用し、追加学習・再採点していない。

| 構成 | parameters | Web BPB↓ | 基本意味 | EOS/80 | 自動反復/80 | 一貫性2/80 | 適切完結/80 | Unicode破綻/80 | Wiki dev32 gold NLL↓ | Wiki dev32 4gram反復/32 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 現13層×256/FFN640 | 10,001,152 | 2.103709 | 48.958% | 54 | 4 | 0 | 0 | 1 | 3.197244 | 20 |
| 新9層×256/FFN1040 | 10,011,392 | 2.166975 | 36.979% | 59 | 7 | 0 | 2 | 0 | 3.206582 | 15 |
| 新6層×384/FFN832 | 9,982,848 | 2.221544 | 50.000% | 52 | 6 | 0 | 0 | 2 | 3.113850 | 17 |

両新候補は全既存採用条件を満たさず不採用。6層は教材内devの正解予測が少し良いが、一般生成の改善に移らなかった。9層の少数の完結は比喩や曖昧な選択の部分成功で、一貫性2の合格ではない。どの構成も日常prefixを百科事典の定義へ変え、意味的反復が残る。構成を変えれば解決するとは言えず、容量不足とも10M不可能とも断定しない。

新科学600,000,000教師、valid/physical605,093,888、実CUDA連続/再開16更新・検証519,816教師別。各学習410.507/399.853秒、結果GPU975.858秒・job占有976.383秒。batch32の実BF16 forward/backwardとfull state再開を確認し、新構成の最大batch/最高速度を網羅的に探索したとは主張しない。全160新内容理由・日本語診断・同byte評価・教師LR/stateを監査済み。可搬証拠architecture_comparison各JSONと57text rawtar、各重みとsource教材はWSLに保持。非blind Codex評価で独立人手レビューは未実施。元10B UIを復帰した。

次のstage4はWiki単独を採用せず、広いWebと物語の新しい入れ子100M/500M教材を実準備する。同source・本文長・EOS密度を厳密5倍に揃え、同教師量で量の効果を調べる。構成比較で明確な改善が得られなかったので、数量比較の研究対照には現13層を保持する案とし、教材準備・内容基準の確認後に学習configへ凍結する。これは現Baseの品質合格を意味しない。stage4学習と改善Base/Chat/量子化を完了するまで全五項目の目標を保持する。

### 五項目stage4の実準備と凍結条件（2026-10-06 JST）

入れ子v2の実準備は100,000,157対500,000,785 tokens、dev2,000,207。Web80%/物語20%のsource・本文長・EOS・原文全文/冒頭完結段落の編集単位を厳密1:5に揃えた。固定64内容は弱10で既定基準内。合格は学習比較への受け入れであり、自然文だけ/全事実認証/実用Base合格を意味しない。原文・各理由・旧v1供給失敗をnested_material各JSONに保持する。

amount_learning_comparison.jsonで同じfresh現13層・Tokenizer4096・seed42・context1024/batch32/BF16 Flash compiled・LRpeak.002/初200更新warmupを凍結。500M教材の安定経路を100M/500M/1B/2B教師で分岐し、100M教材は1B教師で分岐する。各分岐に同20M教師のcosine decay（最低peakの.1、warmup再実行なし）を適用して全日本語/固定80内容を評価する。主経路3B＋評価枝5×20M=100Mの科学3.1B、保存再開検証教師は別、GPU占有上限7200秒。まず500M側を実行して早い100M評価を得る。各節目から毎回新規学習せず、枝は主経路のAdam/RNG/cursorへ戻す。本流/枝とも完了更新だけ保存・計数する。学習秒数は完了step metricsの合計で、保存/評価等は総GPU占有に別記する。

準備量と反復を含む教師量、valid/physical入力、実source別教師/EOS、epoch/block cursorを別記する。全tokenの固有露出unionは独立計測していないため、準備全量を学習済み固有量と呼ばない。遅延doc shuffleは従来と同じ文書/ブロック順序を保持し、全epochを毎回連結せずmmapから必要部分だけ読む。CPU5testsは入力/epoch/再開/学習state/decay復帰/metrics回復の証拠、GPU学習や品質の証拠ではない。実CUDA gate成功後に本流を開始する。量/学習比較GPU、全400内容、改善Base/Chat/量子化はこの凍結時点では未完了。
### stage4の最初の100M評価（2026-10-06 JST、比較継続中）

500,000,785準備tokensの現13層fresh経路で、本流100,000,000教師（valid/physical100,499,456、step149.842秒）から同20,000,000教師decayを分岐。実CUDA連続/再開の全state・有限loss/gradient、安定経路の実LR/教師/保存cursorを確認。共通Web dev256 BPB1.231780、意味46.875%、JBLiMP78.248%、JCQA30.206%。全80の非blind Codex内容は文法2=32、関連2=16、一貫性2=9、適切完結13、EOS31、反復20、raw Unicode0。理由とraw生成のhashをamount_learning_large-100000000_notes/content_reviewへ保存。独立人手評価ではない。

この一点は実用基準未達でBase採用なし。別教材の旧モデルとの値の違いを量だけの効果と扱わず、同500M教材の500M/1B/2Bと入れ子100M教材の同1Bを固定条件のまま実行する。100M枝を終えたactual481317は最新安定stateを復帰して学習継続中。全五項目・段階4全400内容と採否は未完了で、生成品質達成を宣言しない。
### stage4の100M→500M評価（2026-10-06 JST、比較継続中）

同じ500,000,785準備tokensで学習量だけを増やし、各節目に同20M教師のdecayを適用。共通256文書・固定80prefix・日本語全評価と各80非blind理由を保持する。

| 安定経路の教師量 | 評価枝の追加教師 | BPB↓ | 意味 | JBLiMP | JCQA | 文法2/80 | 関連2/80 | 一貫性2/80 | 適切完結/80 | EOS/80 | 反復/80 | Unicode/80 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 100M | 20M | 1.231780 | 46.875% | 78.248% | 30.206% | 32 | 16 | 9 | 13 | 31 | 20 | 0 |
| 500M | 20M | 1.167477 | 44.792% | 75.529% | 34.763% | 30 | 18 | 9 | 14 | 26 | 30 | 0 |

500Mの本流はvalid/physical502,497,280、完了step747.268秒。BPB約5.22%改善も、自由生成の一貫性は横ばい、停止と反復は悪化。学習量の今回の二点だけでデータ増量の効果を否定せず、予定の同教材1B/2Bと入れ子100M対500Mの同1B比較を続ける。Base採用基準は未達。数字の正答は補助値で、数を明示しない自然な書名の継続を、それだけで数値矛盾や文法失敗と判定しない。全400内容のうち160を完了、残240は後続点の生成後に判定する。ChatのCPUトレーナー/コマンド3testsは準備の証拠だけで、GPU対話学習や品質達成とは記載しない。

### stage4の1B評価とChat評価実装準備（2026-10-06 JST、比較継続中）

同500,000,785準備tokensの安定経路1B教師から同20M decayを分岐し、全日本語・固定80のraw生成と個別理由を保存した。BPB1.152110、基本意味48.958%、JBLiMP79.456%、JCQA35.836%、文法2=36/関連2=26/一貫性2=14/適切完結22/EOS37/反復20/Unicode0（各80）。500M点の一貫性9/適切14/EOS26/反復30より改善したが、実用Baseの文法56・一貫性27・適切27・反復18以下などの既存条件は未達。EOSだけを満たして採用しない。これは同教材の学習量比較で、入れ子100M対500Mの同1B比較は未完了。amount_learning_large-1000000000_notes/content_reviewを保持し、全240内容済み・2Bとsmall1Bの残160は未判定。

Chatはevaluate_chat_sft.py/chat_evaluation.pyと永続run_chat_sft.ps1を用意。固定dev80の抑制あり生成・抑制なし役割control、自己生成したAssistant本文を履歴へ戻す24familyの2〜4ターン・59応答を分ける。EOT7は抑制せずEOS3とも区別、raw IDs/bytes/Unicode・空応答・役割漏出・上限・反復を保存し、正解Assistant履歴でown-historyを代用しない。固定historyを切る場合は成功にせず、文脈の採点単位は59独立例ではなく24familyとする。未使用testは選択・採点しない。CLI help/PowerShell構文とCPU7tests成功、GPU Chat学習・評価・文法/関連性/文脈の内容採点は0で未採用。次は科学比較の残点を終えて条件を選定し、品質を満たすBaseからmid-training/SFT比較・量子化/ローカル実行へ進む。

本学習へ同教材の経路を延長するため、extend_amount_learning_trainer.pyのExtendedCurveTrainerを別実装した。完了したstableの予算に未来の教師節目だけを追加する明示load_extensionで、既存重み/Adam/scheduler/RNG、genre/EOS、入力/教師/bytes/digest/epoch/block/updateを保持する。通常loadは予算変更を拒否し、LR・過去節目・教材・親SHA・sourceが変わる延長も拒否。CPU2testsでfull state保持、連続対分割再開、最初から同じ全節目を指定した長期対照とのoptimizer/入力軌跡一致を確認した。curve_extension_tests.xmlを保存。5B/10Bの実GPU延長・採用configは未開始で、段階4の同量比較と残160内容・採否が先。教材を増量する場合のsampler移行は別条件であり、この同教材延長の一致検証を代用しない。

run_improved_base.py/ps1を追加し、一段ずつ5Bまたは10Bの同教材stable延長→同20M decay→共通256本文/日本語全suite/固定80生成を永続実行するコマンドを用意した。先行jobの実終了、raw80/全内容とreview/annotations/result/親/sourceのbindingを確認し、既存の相対改善gateまたは絶対Base研究screenを満たす場合だけ研究継続を受け入れる。研究継続の選定はBase採用ではなく、本学習後の全80内容と既存品質条件は別途必要。未終了比較からconfigを固定しない。各段のGPU予算は実測完了step throughputから「残教師/throughput×1.3＋1800秒」で見積もり、stableとdecayの実CUDA連続4対2+2全state/history一致を本学習前に要求する。科学の追加stable・decay教師、累積教師、valid/physical、検証教師、GPU占有を分け、途中失敗は最後の完了更新checkpointから再開する。全80内容未判定で次の段へ自動進行しない。

CPU2testsでは未終了記録と、complete記録でも実際に生きているPID/boot/startの拒否・config未作成を確認。CLI help/PowerShell構文も成功。GPU予算延長のgate/学習/品質評価は未実行、configsの採用候補は未凍結。WSLから`uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_improved_base.py --config configs/phase6/<new-recipe>.json --freeze --source-run reports/phase6/<completed-run> --parent-point <stable-point> --reference-point <quality-control-point> --target-teachers 5000000000`で、実比較完了と採否後に固定する。Windowsの永続起動は`scripts/run_improved_base.ps1 -Config configs/phase6/<new-recipe>.json`、中断後は実processを確認して同コマンドに`-Worker`を付ける。PythonはWSL uvのみ、同4090の科学jobを重複起動しない。

### Chat pilotの実準備（2026-10-06 JST、Base品質待ち）

prepare_chat_pilot.pyで、固定public pilot manifest/corpus/split/4K Tokenizerのhashを確認し、既存RealPersonaChatのtrain2,688/dev150対話だけを再利用した。splitは元のwhole-dialogue/connected-familyを保持し、testは選択・tokenize・採点しない。全量near判定や再取得・Tokenizer再学習を繰り返していない。入力原文と役割、canonical hash、train/dev family非交差、全Assistantターゲットの一回ずつの本文＋EOT、current pairを切らないwindowを実データで確認した。CPU準備2.315秒で完了・actual484206終了不在、Chat GPU0。

| 準備した分割 | 対話 | 元本文tokens（発話を一度ずつ） | 元対話系列tokens（役割等込み） | SFT窓 | 窓系列tokens（履歴反復込み） | Assistant本文＋EOT教師 | 古い履歴を切った窓 |
|---|---:|---:|---:|---:|---:|---:|---:|
| train | 2,688 | 1,177,334 | 1,341,764 | 40,366 | 10,189,157 | 633,185 | 0 |
| dev | 150 | 65,216 | 74,386 | 2,250 | 560,873 | 35,054 | 0 |

これらは準備量で消費済み学習量ではない。SFTの10M/30M/100M総系列予算はAssistant教師10M/30M/100Mとは異なり、このtrain窓の一周では教師は系列の約6.2%。元対話を一度ずつ数えた量もglobal unique-token unionではない。原文の相づちや同じ発話、口語・誤字を維持し、役割の交互性と空でないAssistant本文を保持する。固定train4全文を読んだ診断では、自然な話題継続の一方、自己紹介、未導入のフィジー等の背景、歴史の未検証の一般化を確認した。事実性/指示応答/訂正能力の保証ではなく、4例だけでsourceやtestを再選別しない。独立人手評価なし。

Linuxのデータは`/home/aihub_ubuntu/jmicro-data/phase7/real-persona-pilot-20261006`（train/dev JSONL、manifest、sample4）、実job/reportは`reports/phase7/chat-pilot-20261006`。Windows可搬証拠はchat_pilot_preparation/prepare_job/sample4/content_notes各JSON。human source revision28d0b6b…/CC-BY-SA-4.0・帰属と元public pilotを保持する。shared speakersの非交差は保証しておらず、persona本文の追加復元はしない。次は量比較と改善Base品質を完了してからmid-training/SFT比較を凍結し、実CUDA安定batch/再開/対話評価を行う。

### stage4の2B評価（2026-10-06 JST、同1B教材量比較は継続中）

同500,000,785準備tokensで2,000,000,000教師の安定経路から同20,000,000教師decayを分岐し、全日本語/固定80のraw生成と内容理由を評価した。安定経路valid/physical2,009,956,352、更新61339、step2985.553秒。結果はBPB1.138590、意味48.438%、JBLiMP72.508%、JCQA34.048%、文法2=43、関連2=32、一貫性2=21、適切完結27、EOS40、反復21、Unicode0。1B比では生成の一貫性14→21・完結22→27・停止37→40とBPBは改善したが、反復20→21と選択式の一部は悪化した。既存Baseの文法56・一貫性27・反復18以下等を満たさず採用しない。

全320/400内容済み。残small1Bは同じ科学jobで学習中で、同100M対500M教材の同1B結果と全400内容の採否を先に確定する。教材量が増えた効果と同教材の学習量効果を混同しない。有望な研究延長の選定は元の相対gate/絶対screenで行い、実用Base採用とは区別する。非blind Codex判定で独立人手なし、raw-bound notes/content_reviewとWSL全checkpointを保持。5B/10B追加GPU・Chat学習・最終test・量子化は未実行で全五目標は未完了。

review_improved_base.pyは完了した同教材延長の新metric範囲と累積stable stateを区別し、親のoptimizer/RNG/cursor lineage、同20M decay、CUDA再開gate、科学/検証教師・valid/physical入力、固定80raw SHA付きnotes、日本語全suite/共通byte BPBを監査する。研究継続gate・絶対dev screen・元Web品質を別報告し、最終seed/full/test等の未実施項目を残してBase_adopted=falseを保持する。採点済みnotesを自動作成せず、`uv run --frozen --extra hub --extra data --extra ml --extra export scripts/review_improved_base.py --config configs/phase6/<completed-recipe>.json --notes reports/phase6/<raw-bound-80-notes>.json --archive`でレビュー・可搬text保存を行う。CPU6tests/CLI helpは実装準備の証拠で、追加5B/10B GPU品質の証拠ではない。

### Dialogue mid-trainingの実装・train窓確認（2026-10-06 JST、GPU0）

src/jmicro/dialogue_training.pyは主系列の会話全体（User/Assistant本文・役割・EOT）を教える窓と、Base再学習本文/EOSのdocument samplerを混ぜる。source別の総系列予算を固定し、最後の窓を途中で切らない上限context+1のovershoot、valid/physical入力、全教師とAssistant教師等を区別する。長い対話をcomplete pair境界で分割し、前のpair/systemは必要時にcontext-only maskへ戻し、各原文targetを一度ずつ教える。元の139対話の最終Userは原文の未返信として保持し、Assistantを作らない。Base重みのみを継ぎAdam/RNG/局所会計はfresh、Base履歴は別lineage。SFTのAssistant-only窓・maskは変更しない。

inspect_dialogue_midtraining.pyは固定train2688のみを点検し、全2688窓、系列1,341,764、input/教師1,339,076（User584515/Assistant592819/role80871/EOT80871）、capacity2,752,512を記録。全元発話targetを一度ずつ保つことを実sourceで確認、CPU0.910秒、GPU0。dev/testはwindow化しない。dialogue_midtraining_preparation.jsonを保存。sourceの自然な末尾Userを誤って偶数turn限定にした初版は修正し、raw文やsplitを変えない。

run_dialogue_midtraining.py/ps1は固定config、採用Baseの評価・全80理由・SHA、train/source・mixture、実CUDA/BF16の新masked batch測定を先に要求する。実CUDA4対2+2全state一致の後に系列予算まで学習し、250完了更新checkpointとmetric・PID/boot/start・累積GPU予算・source snapshotを保存する。未採用Baseから起動しないCPUtestを含む関連10tests/CLI help/PS構文成功。Base評価reviewのPath型読込も修正し関連6tests再成功。これは準備で、実CUDA batch probe専用コマンド、mid-training後のSFT接続と直接SFTとの同条件ablation/内容評価は未完了。Base品質と現在の量比較を先に確定する。

### stage4の完了と5B研究延長の凍結（2026-10-06 JST）

全5点・全400個別内容とactual state監査を完了。科学stable3B+decay100M=3.1B教師、actual CUDA24更新/検証782564教師別、GPU5190.079秒。actual481317終了・不在、元10B UIを復帰確認した。

| 準備教材tokens | stable教師 | 同decay教師 | BPB↓ | 文法2/80 | 一貫性2/80 | 適切完結/80 | EOS/80 | 反復/80 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 500,000,785 | 100M | 20M | 1.231780 | 32 | 9 | 13 | 31 | 20 |
| 同上 | 500M | 20M | 1.167477 | 30 | 9 | 14 | 26 | 30 |
| 同上 | 1B | 20M | 1.152110 | 36 | 14 | 22 | 37 | 20 |
| 同上 | 2B | 20M | 1.138590 | 43 | 21 | 27 | 40 | 21 |
| 100,000,157 | 1B | 20M | 1.159479 | 32 | 9 | 26 | 34 | 21 |

同1Bの100M→500M教材ではBPB・文法・一貫性は平均改善したが、coherence+5のpaired CI[-.0375,.1625]はゼロを含み、改善基準未達。適切完結26→22も悪化し、増量すれば全指標が良くなるとは言わない。同500Mの全隣接学習比較も既存gate未達。全Base採用条件は未達で、量不足や容量限界の単独確定ではない。全Unicode/role/emptyは0、非blind Codex判定で独立人手なし。

量比較のcompleted-source review/annotations/result/親hashを確認した上でconfigs/phase6/improved-base-5b-20261006.jsonを固定した。候補2Bはこの曲線の文法/一貫性/BPBが最良で、500M→2Bの広い区間ではcoherence+12/CI[.0375,.2625]、EOS26→40、反復30→21と全既存相対gateを満たす。ただしこの区間の採用は結果を見た後の探索的選定で、多重比較補正や独立confirmationではない。1B→2Bのcoherence+7/CIゼロ含有と反復20→21の失敗をそのまま保持し、研究継続とBase採用を分ける。improved_base_5b_selection.jsonへ全失敗も保存。

次は2Bのstable全stateから同500M教材を累積5Bへ明示延長（科学追加3B+同20M decay）、2Bを新比較の対照に固定し全日本語/80内容を判定する。実測step2B/2985.553秒を基にremaining3B/throughput×1.3+1800=7622秒のGPU上限を固定。stable-extension/decay各CUDA4対2+2 fullstate gateが本学習前に必要。5B/10Bは教材量ではなく累積教師量であり、教材2〜5B増量のsampler移行は別実装/別実験。10Bへ自動進行しない。5Bのdev screen合格でも最終seed/full/test等を実証するまでBase採用しない。Chat/量子化/実UIを含む全五目標は未完了。

5B研究延長を実GPU起動した。actual487071/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start10923679、Windowsworker33740、config SHA f48ac242…を実確認。stable-extensionのCUDA連続4対2+2は全state/history/finite一致、検証8更新260906教師/262144inputを科学量と別に保存。累積教師2,001,989,075/loss2.654842有限から5Bへ継続し、GPU90%/VRAM7704MiB。現在の測定はbatch32/context1024の既存条件で、新たな最大VRAM/batch探索を行った証拠ではない。5B本流の終端、同20M decayの実CUDA再開、全日本語/全80内容、2Bとの採否は未完了。improved_base_5b_stable_gate.jsonとLinuxrun/job/source/metrics/checkpointsを保持し、実process確認後にのみ同restart_commandを使う。元UIはjob終端で復帰する。

### 主mid-training→SFTの接続とmasked batch測定の準備（2026-10-06 JST、Chat GPU0）

SFT configは`route=direct-sft`または`midtraining-sft`。`parent`は直前の学習済みmodel parent、`adopted_Base`は元の採用Baseを指し、後者のraw80評価/全理由/SHA/品質基準をそのまま確認する。主系列では`mid_training.config/result`のSHAと実job終了、同Base/train/Tokenizer/source、実CUDA再開gate、系列予算の完了とcheckpointの全会計/lineageを確認し、mid-trained parentをBase_adoptedと再ラベルしない。AssistantTrainerはparent重みを継ぎSFT optimizer/RNG/局所会計をfreshへ戻し、root Base・mid-training親・その履歴を別保存。Base流暢性保持/Chat採否は後続の比較評価で判定し、接続できたことを品質証明にしない。

`probe_chat_batch.py/ps1 --config <frozen Phase7 probe recipe>`を用意。probe configは主trainingのBase/data/shape/予算に加えて`probe_kind=sft|mid-training`、`probe_source_sha256`、有限`candidate_batches`（最大12候補/各256以下）、warmup1〜20/measured4〜100更新、`probe_GPU_budget_seconds`（最大1800）、training outputとは別の`probe_output`を固定する。前段の採用Baseと実mid-training親を確認してからGPU lock下で各候補をfresh親から実測、教師tokens/秒中央値で選ぶ。系列/valid/physical throughput、allocated/reserved VRAM、OOMと完了更新教師を別報告し、probe重みを本学習の親へ使わない。候補範囲内の最大成功batchと速度最良batchを区別し、真の最大や全backend最適化を未測定で主張しない。

主mid/SFTは`batch_evidence`のSHA・実完了job・親・data binding・trainer・context/dtype/backend/compile等とselected batchを確認する。probeだけは`require_batch=False`で前段確認を行い、CLI本学習で測定証拠の要求を外せない。採用Base未達なのでまだprobe config/GPU測定は0。関連15CPUtestsは実CPU mid→SFT weights/fresh Adam/full resumeと、不正な親/live jobの拒否、選択ルールのプロトコルfixtureの証拠のみ。CLI help/PS構文も成功。

Tokenizer codec/Assistant sampler本体は変えず、採用Base確認後のTokenizeにinstance LRU100kを使い、probe/再開builderで同じ本文の再encodeを省く。固定実train2688の全40366窓で元binding d5676756…と一致し、CPU1.742秒/hit1258820/miss74810を記録した（sft_cached_binding_check.json）。元IDs/教師mask/split/原文を保持し、未使用testやモデル品質を評価しない。GPU速度の実測値ではない。次は現在の5B本学習と品質採否が先で、主mid-training/SFT対直接SFTの実GPU/同条件ablation/全内容採点は未完了。

### Chat全内容採点と同条件比較の実装準備（2026-10-06 JST、実Chat GPU0）

`review_chat_sft.py --evaluation reports/phase7/<completed-eval>/result.json --template reports/phase7/<new-notes>.json`で、実終了した評価jobとcheckpoint/source/suite/TokenizerのSHAを確認して未採点templateと実history付きitemsを生成する。既存notes/itemsは上書きしない。primary80、役割抑制なしcontrol80、自生成履歴24family/59応答の全219を対象とする。token IDsからraw bytes/text/terminal/役割/反復と実promptを再構築し、提供された正解Assistantをown-historyへ混ぜない。各応答の文法/関連性/文脈0・1・2と具体的理由が必要で、欠損・重複・未採点・boolean値・別raw SHAを拒否する。

採点後は同コマンドの`--notes <notes>`で`content_review.json`へ保存する。文法・関連性が同時に2のprimary応答70%以上（56/80）、own-history最終文脈2が60%以上（15/24）と既存の停止95%・空5%以下・役割1%以下・Unicode0・固定history保持を集計する。文脈の単位は59独立応答ではなく24family。先行turnの内容/機械失敗は隠さず別表示し、category別と応答文字数分布も保存する。dev screen合格はChat採用ではなく、Base流暢性・複数seed sampling・独立blind人間評価/一致率・条件固定後のtestは別の未達項目。Codex非blind判定を人間証拠として登録できない。

`review_chat_ablation.py --direct-config <recipe> --direct-evaluation <result> --direct-notes <notes> --main-config <recipe> --main-evaluation <result> --main-notes <notes> --output reports/phase7/<new>/chat_ablation_report.json`は、実終了したdirect-SFTとmid-training→SFT、既存Base採用証拠と完了mid親、実CUDA再開gate・checkpoint counters/lineageを確認する。同root Base、SFT seed/batch/context/LR/warmup/source/train/budget、実SFT窓・系列・教師・入力・EOTが同じ場合だけ比較し、候補側の追加mid-training系列/教師/physical/GPUは別会計する。総教師/GPUが同量の比較とは記載しない。固定protocolの80primary/24own-finalについてfamily-paired差とbootstrap CIを出すが、多重比較補正なしの記述的評価で独立confirmation・採用を宣言しない。Base対mid対SFTの保持評価は別途必要。

関連CPU16tests/2.07秒と両CLI helpに成功。raw改変/履歴混入/集計改変/採点欠損/他SHA/boolean、人間への誤ラベル、70%・60%の境界、未終了/live job、実SFT量やbatchの不一致を検証した。fixtureの採点はモデル品質の証拠ではなく、対話GPU学習と実内容採点は0。可搬準備は`reports/phase7/chat_content_review_preparation.json`/tests XML。5B本流actual487071は継続し、凍結Base sourceやTokenizerを変更していない。次は5B終端・同decay・全日本語/80内容からBase品質を決め、後続の実比較へ進む。

### Chat blind packetと評価者一致率の準備（2026-10-06 JST、実人間評価0）

`chat_blind_review.py prepare --evaluations <named path/SHA refs.json> --output reports/phase7/<new-packet>`は、実終了した複数の異なる学習済みChat checkpointの全219応答/モデルを検証して無作為に混ぜる。公開用`reviewer_packet.json`はopaque sample ID・実messages/checks/応答本文とrubricだけで、model/route/checkpoint/case名やprivate seedを含めない。対応表は別の`private_mapping.json`へ保存し、評価者には渡さない。未採点`reviewer_notes_template.json`を生成し、既存packetを上書きしない。外部送信/公開を行わない。

`chat_blind_review.py review --packet-directory <packet> --notes <human-A.json> <human-B.json> --output reports/phase7/<new-report>.json`は、packet/entry/evaluation/checkpoint SHAと元raw/historyを再照合し、人間の本人名・独立性・blindの宣言と全応答0/1/2/理由を要求する。Codex/AI・未採点・欠損/重複・boolean・別packet・改変表示・同一評価者の表記揺れを拒否。モデルごとに全内容のdev集計、評価者ペアごとに文法/関連性/文脈のexact agreement、3×3混同行列、unweighted Cohen kappaを保存する。全同値では期待一致率1のためkappa=nullと明記する。相関するturn/conditionの応答単位であり独立familyの信頼区間と扱わず、統計が本人性・正しさを認証するとも記載しない。人間の本人性は自己申告に基づき、外部認証や実人間評価を捏造しない。自動合意・有利な評価者選択・Chat採用は行わない。

関連CPU10tests（新3/既存7）1.20秒、CLI help成功。fixtureの人間ラベルはプロトコル入力で実人間ではない。実モデルpacket/人間提出/対話GPU学習は0、Base品質と実Chat比較待ち。`reports/phase7/chat_blind_review_preparation.json`とtests XMLに準備を記録し、独立人間評価未実施と全品質条件を保持する。

### Base/mid/SFTの同条件Chat評価と複数seed sampling準備（2026-10-06 JST、実CUDA評価0）

`evaluate_chat_stages.py --sft-config configs/phase7/<frozen-SFT>.json --stage base|mid-training|sft --decoding greedy|sampling --output reports/phase7/<new-run>`を用意。固定SFT recipeの採用root Baseとdata/source/実masked batchを確認し、Base controlにはroot、mid controlには実終了したmid親、SFTには実終了job/config/SHA/実CUDA4対2+2/full sampler/教師・系列・入力・physical/EOT/lineageが一致した終端を使う。未採用Base、未終了/live SFT、direct routeでのmid親、会計/shape/dataの不一致は拒否する。Base controlやmidをChat採用と扱わない。既存greedy seed42、BF16 math、64tokens、固定dev80と自生成履歴24family/59応答の条件を保持する。Base completionの流暢性保持は別suiteで後続確認する。

samplingは`--seeds 42 43 44 --temperature .8 --top-p .9 --top-k 50`を既定案とし、3〜5 distinct seedsに限定する。temperature/top-p/top-kは始動前のbindingに固定し、学習RNGと別のlocal Generatorを使う。各User入力のseedとown-historyのseed+turn-1をraw rowに記録し、EOT7/EOS3、ID/byte/Unicode・役割・反復・空・max lengthを保存、表示修復を加えない。greedyはsamplingで置き換えない。各seedでprimary80/control80/own59の全219を保持し、繰り返したseedを独立80/24 familyの水増しと扱わない。良いseedだけを選ばず全seed結果が必要で、一seedの比較はその範囲と明記する。

job/progress/recipe/source/各seed result/summaryとPID/boot/startを永続化する。累積GPU上限は最大1800秒、CLI argsを正確なrestart commandへ保存し、完了caseを再実行せず再開する。各seed leafの完了記録だけでなく親multi-seed jobの実終了・binding・identity・全体予算を要求する。各seedの`result.json`は既存`review_chat_sft.py`の全219 notesと`review_chat_ablation.py`、blind packetへ接続する。native IDs/実prompt/seed設定を再検証するが、機械集計だけで文法/関連性/文脈を採点しない。

Windowsの永続起動は`evaluate_chat_stages.ps1 -SftConfig configs/phase7/<recipe>.json -Stage <stage> -Decoding <mode> -Output reports/phase7/<new-run>`、実process確認後の再開は同args＋`-Worker`。CPU preflightをUI/GPU変更前に行い、job中は元UIを止め終端で戻す。実科学jobと重複起動しない。関連CPU23tests/2.26秒、CLI help/PS構文に成功。native CPU seed再現/別seed/RNG非消費/フィルタとEOT/全219 raw/own turn seed/未終了親と予算超過拒否/実CPU SFT会計を確認した。実CUDAのstage/sampling、実Chat学習と品質、人間提出は0。`reports/phase7/chat_stage_sampling_preparation.json`/tests XMLへ保存し、Base品質→実Chat→全seed・全内容・人間/最終test→量子化/実UIの全目標を維持する。

### 対話学習によるBase流暢性保持の準備（2026-10-06 JST、実retention CUDA0）

`run_chat_base_retention.py --sft-config configs/phase7/<recipe>.json --stage mid-training|sft --output reports/phase7/<new-retention>`は、採用root Baseの保存済み評価/内容notesを対照として再利用し、対照のGPU再評価を行わない。native reference configの同dev256のDocID/body tokens/bytes、manifest/Tokenizer/固定Base80/日本語sourceをCPU preflightで照合し、実終了したmid親/SFT終端とCUDA保存再開・全会計に結び付く重みを評価する。変更対象の旧sourceを編集せず、`run_complete_text_comparison.evaluate`を別process内で呼び、BF16 math/FP32 CEと同じ本文・EOS別損失、greedy64/全80、日本語192・331・1119を保存する。BaseはBOS/plain prefix・EOS3のみで止まり、Chat EOT7は役割漏出として保持する。Chat headerやEOT停止へ置き換えて保持に合格させない。

job/PID/boot/start/source/recipeとnative section別progressを保存し、上限1800秒の累積GPU予算内で再開する。正確なuv restart commandを記録し、Windowsは同名ps1の`-SftConfig ... -Stage ... -Output ...`（reference変更時は`-ReferenceConfig ...`）で永続化、actual確認後の再開は`-Worker`。UI/GPU変更前にCPU preflightを行い、他の科学jobを重複起動しない。

終了後は`review_chat_base_retention.py --run <run> --template reports/phase7/<new-notes>.json`で全80の未採点notesを作り、raw generation SHA・nonblind Codexの0/1/2/完結0/1/具体的理由を固定して`--notes <notes>`へ渡す。採用Base notesは再採点せず、対象の全80のみ判定する。byte-weightedの本文BPB差と文書paired bootstrap CI、固定familyごとの内容差、文法・関連性・一貫性・適切完結、EOS/反復/空/役割/Unicodeと日本語集計差を報告する。文書BPBの単純平均は使わず、同じbytesを分母とする。既存Base絶対基準と歴史的BPB1% guardを報告し、Base/Chatを自動採用したり判定基準を緩めたりしない。非blind内容比較や集計日本語差は独立人間確認/paired日本語有意差と扱わない。

関連CPU11tests/2.19秒、両CLI help/PS構文に成功。不均一bytesの重み、DocID/教師不足の拒否、一貫性・役割の退行と採用false維持、未終了/live評価の拒否を確認。実retention CUDA/全内容採点、Chat学習、人間提出は0。`reports/phase7/chat_base_retention_preparation.json`/tests XMLへ準備を保存し、現5Bの品質→実対話比較→retention/全seed・人間/最終test→量子化/実UIを継続する。

### 5B本学習の完了・採否と次の教材比較（2026-10-06 JST）

同500,000,785 prepared tokensを維持したstable5Bと20M decay、全256文書・日本語192/331/1119・固定80個別内容を完了。学習量と教材量を混同しない。

| 指標 | stable2B＋20M | stable5B＋20M |
|---|---:|---:|
| 本文BPB↓ | 1.138590 | 1.127218 |
| 基本意味 | 48.438% | 60.417% |
| JBLiMP | 72.508% | 77.039% |
| JCQA | 34.048% | 37.265% |
| 文法2/80 | 43 | 35 |
| 関連性2/80 | 32 | 31 |
| 一貫性2/80 | 21 | 15 |
| 適切完結/80 | 27 | 24 |
| EOS/80 | 40 | 34 |
| 自動反復/80 | 21 | 18 |
| Unicode/role/empty | 全0 | 全0 |

一貫性の差-6/paired CI[-.1875,.0375]。観測平均は低下したが独立seed/人間や有意な悪化の証明ではない。損失や選択式評価の改善を生成品質の合格に代えず、既存absolute基準（文法56・一貫性27・適切27・EOS37・反復18以下・失敗0）とrelative gate、歴史的Web BPB1% guardの未達を保持する。5Bは不採用、10Bへの自動延長なし、final-seed/full/test/Base採用/Chat/量子化は未達のまま五目標を続ける。

実5B stableの追加は3B教師、decay20M、検証16CUDA更新/521760教師は別会計。全state/RNG/sampler/history/有限値の二gateは合格し、終端full optimizer/LR/会計/親cursor・全80rawを監査した。GPU4681.791秒・占有4681.798秒、7622秒枠内。科学PID487071は終了・不在、元10B UI489906と実boot/start/HTTP親SHA・tokens・busy=falseを確認。`improved_base_5b_notes.json`、`improved-base-5b-20261006_review.json`/annotations、`improved_base_5b_completion.json`、31text/14,094,878byte archive/manifestに保存し、大型tensorとshardsはWSLへ保持。内容判定は非blind Codexで独立人間評価ではない。旧数値7失敗と旧全比較も保持する。

次の優先は同じ小poolの繰り返し追加ではなく、distinct教材の量・多様性を変える比較。manifestのみの`larger_material_supply_inventory.json`でWeb12,225,819,077/物語200,000,192 train tokensを確認した。80/20の2B教材には物語400M、5B教材には物語1Bが必要で、現在のtokenized sourceだけでは足りない。未処理のpinned TinyStories-JA train原文の供給を有限範囲で測り、必要時に追加sourceを準備する。source追加・mixture/長さ/EOSの変化は交絡として別表示し、同じ教師量を揃えた比較と採否・予算を開始前に凍結する。既存全量の再照合や重複を新量に数える処理は行わない。2B教材/新GPUはまだ未準備・未開始であり、Base品質→実Chat比較→人間/最終test→量子化/実UIの順を保持する。
### 新95/5 mixture内の500M対2B準備契約（2026-10-06 JST）

5Bの失敗はacc2669へ保存し、同じ枝を10Bへ延長しない。固定4train rawから2400のbyte位置を一様抽出し、含まれる行のnative選別tokens/行bytesを集計した供給probeはCPU0.345秒。約156.95M/95% bootstrap144.92–168.67Mに旧retained59.96Mを加えても約216.92Mで、story400Mを既存sourceから得る見込みは弱い。既使用/重複を含む推定であり、独立family品質、正確な未処理量、追加prepared量とはしない。32原文例は未採点、protected test・新取得・GPU0。cacheキーは内容hashではないため過去の完了hash確認/固定revision/sizeを再利用し全5.37GBを再scanしなかった。

次はWeb95%/物語5%を両方に使い、small500M（Web475M/story25M）とlarge2B（厳密4倍）を準備する。量だけの比較はこの新二条件間に限り、旧80/20との比較はmixture差として別に報告する。より広いWebを使い、物語のテンプレート偏りを減らす仮説でもあり、結果前に改善を断定しない。原文wholeまたは最初4段落のintact unit、長さ/4gram/末尾/主体の旧機械selectorと固定64弱<=10を保持し、受け入れ条件を緩めない。正確4倍のsource/body-length/unit-kind/EOSとsubsetを`FourGroups`で作る。devは同source95/5、train-family splitを保持し学習に使わない。global near/site/author auditは未実施のまま。

実装は`prepare_larger_material.py/ps1`と`src/jmicro/larger_material.py`、CPU1800秒/8workers/seed2026100621。実WSLに326GB余裕を確認した。関連7CPUtests/0.86秒・PS構文成功、全5目標の達成証拠とはしない。`reports/phase6/larger_material_preparation.json`へsource SHA・CPU予算・条件を凍結してから永続CPU jobを起動する。未完了partialはreadyにせず既存旧runを上書きしない。新学習はactual供給と固定64採否を待ち、同じfresh10M/各1B教師・同20M decay、LR/seed/batch/教師範囲とGPU予算を次のconfigへ別途凍結する（現時点は案）。その後もBase品質→主mid/SFT対direct/retention/全seed内容→人間/最終test→量子化/実UIを完了するまで目標はactive、Chat/量子化未開始。追加取得/push/paidcloudなし。

### 教材量比較の実行状態と反復目的の条件付き次案（2026-10-06 JST）

上の95/5は不採用の旧準備案。現在の実比較は新75% Web/20% SyntheticTextbook-jp/5% story、small500,000,328対large2,000,001,312 prepared tokens、各同1B stable教師＋同20M decay、同fresh10M/LR/seed。`configs/phase6/textbook_quantity_comparison.json`の凍結source/GPU4861秒枠を保持する。large側の全日本語/原80件内容は完了し、文法44/一貫性14/適切25/EOS43/反復19で既存Base基準未達。small側はactual494779で学習中、全160/量効果/延長採否は未確定。両条件の終端と全内容判定を待ち、相対改善または絶対screenを満たす場合だけ既存の段階的延長を使う。未達なら有効な次のBase仮説へ進み、全五目標を候補不採用で完了にしない。

次の反復仮説として、モデル自身がtrain prefixから生成した続きを負例にするsequence unlikelihoodを一次資料のsection5.2で確認した。[Welleck et al.](https://arxiv.org/html/1908.04319v2#S5.SS2)、[著者の実装説明](https://github.com/facebookresearch/unlikelihood_training)。英語大規模モデルの報告を日本語10Mの効果や意味保持の保証として扱わない。独立実装で旧CE/source/依存関係は変更しない。

`sequence_unlikelihood.py`はnative EOS3を残すcached greedy rollout、実生成履歴の微分可能scoring、後続反復4gramの全所属tokenを一度だけnegativeにするlossを実装。EOS/EOTと特殊0..7は負例にせず、gold continuation/dev/testは使わない。`sequence_objective_trainer.py`は同じ更新へCE+alpha*ULを統合、trainの完全なdocument headだけをprefixにする。control alpha0も同rollout/scoringを実行し、CE教師と生成body/EOS/negative/extra valid・physical/digestを別保存する。実CPU連続/再開の全state一致・alpha0対旧CE完全一致などcore10/統合4tests成功。CPU Adam親tensorの共有は新trainerのfullstate copyで修正し、初回失敗XMLも保持。実CUDA品質は未測定。

large保存80件ではこの研究用4gram候補が50件/1501位置あり、うち一貫性2は2件、候補なしでも一貫性<2が18件。候補は自然な反復も含み、旧自動反復19/80や採否基準を置換しない。反復目的だけで全意味崩れを直せるとは言わない。

条件付き案は両教材比較の実終端/全160後、延長/採用根拠が得られず反復が残る場合にのみ検討する。largeの完了1B+20M親を両条件に固定、同25M CE教師/継承Adam・RNG・cursor、peak LRは実親以下かつ0.0002以下で再加熱なし。CE対CE+sequence UL(alpha0/0.1)、4更新ごと最大8 train prefixes32token/最大64greedy continuation、同計算policy。全GPU比較1800秒を上限案とし、実CUDA速度/batchと連続4対2+2 gateの測定後にrecipeを凍結する。新永続paired runner/採否は689f74fで実装、sourceの実終端/採否・新probe/final recipeなしには起動できない。実GPU学習0。actual probeは各alphaの連続4対2+2計16検証更新を300秒枠で測り、完了証拠から同25M各条件と評価がprobe込み1800秒へ収まる場合だけ本比較recipeを凍結する。全日本語/同dev256/全新80件ずつと旧relative/absolute/original-Web基準で採否を残す。反復だけの改善や短い出力をBase採用にしない。詳細は`reports/phase6/sequence_unlikelihood_research_preparation.json`。

### 最新の実行確認と、ここからの計画（2026-10-06 JST）

新75/20/5教材の500M対2Bを各1B教師＋同20M decayで完了、全160内容と実学習証拠を保存した。一貫性11→14/80、EOS51→43/80、反復14→19/80で既存改善・採用条件未達。単純増量の改善も10M容量限界も確定しない。次の同25M CE対sequence ULの実CUDA保存再開は各24checks合格、16検証更新/520076教師・54.624秒。本比較recipeは時間見積り超過で未凍結、科学学習0。

連続速度測定はCE側16更新を保存後、metrics行をcheckpoint用finite_stateへ渡したためKeyError('model')で終了した。actual500028は不在。測定GPU21.623秒を既消費として保持し、CE最終checkpoint31411と全16行を保存した。両条件の測定完了・科学比較成功とは扱わない。元UIへの復帰ログあり。この確認では追加GPUを起動していない。

1. 測定の確認コードを修正する。凍結済み旧config/source/jobを保存し、修正後のversionと継承根拠を明示する。metricsの有限値とmodel/Adamの有限値を別に確認し、実保存CE16更新を再利用可能なら再学習せず、未測定CE_ULだけを続ける。54.624＋21.623秒を含め検証総300秒以内、全比較案1800秒に計上する。
2. 実測が予算内なら同じlarge1B＋20M親からCEのみ対CE＋sequence ULを各25M教師、計50Mで比較する。同じ教材・順序・Adam/RNG/cursor・LR方針を維持し、生成tokensと追加GPU時間は教師量と分ける。全日本語・共通byte BPB・固定80件ずつを一度評価する。反復だけでなく文法、関連性、一貫性、適切完結、EOS、Unicodeを既存条件で判定する。
3. 全条件を満たす改善があれば、そのレシピを必要な学習量へ拡張し、独立seed・full dev・凍結後testでBase採用を確認する。反復だけ改善なら意味逸脱の残存例を分析し、次の一仮説・対照・予算を固定する。未改善の同じ設定を10Bへ自動延長しない。
4. 品質Baseを得た後、直接SFT対対話中間学習→SFTを比較する。Assistant本文＋EOTを教師とし、2〜4ターン、訂正/否定、停止、Base能力保持、複数sampling seedを確認する。独立人手レビューは未実施として扱い、実評価者の結果をAIで代用しない。
5. 合格Chatのfloat/HF/GGUF、Q8/Q4で品質退行・停止・Unicode・容量・応答速度を実測し、採用重みをローカルWebUIへ接続、再現手順と成果物を保存する。

最終目標は10Mの自然な短い日本語Base、2〜4ターンのChat、量子化したローカル利用。1800秒は直近比較のGPU上限案であり全工程の納期ではない。WSL uvのみ、必要な確認を行い、既存巨大コーパスの全量再照合や過去評価の不要な反復を避ける。節目でverified local commit、pushなし。全五目標active、Base/Chat未採用、旧数値7失敗と品質基準を保持する。

測定修正と本比較の再開（2026-10-06 JST、2717458）: `continuous-timing-v2`で旧CE16更新を実fullstate/SHA確認して再学習せず再利用、CE_UL残16更新をCUDA実測完了。metricsとmodel/Adamの有限値を別に検証する8回帰testsと、予算/既存guardを含む13CPUtestsに合格。旧config/source/jobは不変で、実CUDAprobe16更新520076教師、連続測定32更新1039808教師、計48更新1559884検証教師は科学学習とは別。既消費GPU54.623992＋失敗21.622512＋v2 27.587662＝103.834166秒を全て計上、検証300秒以内。両16行を記録し、最初4更新のcompile/data warmupは会計に残して後12連続更新/全3rollout cycleの中央値を使用。CE通常0.098622/rollout1.252964秒、CE_UL0.068504/1.287814秒、教師32494/update、各770更新見込み。科学学習合計584.429秒×1.3＋評価480秒＝1239.757秒、検証込み1343.591秒で1800秒案以内。

`configs/phase6/sequence_objective_comparison.json`（SHA8b8de74892c885c1680cf2d7755074b9938809b66dae09f6e276ac446ff43d19）へ各25M教師を凍結、科学GPU上限1696.165834秒。旧実probeのsnapshot/config/job/gatesをSHA検証し、driverの予算処理/reviewer会計以外のtrainer/core/forward/評価源変更は拒否する。Windowsworker31224、actual501165/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start12291147をps確認して永続起動、nativejob/log/checkpointsは`reports/phase6/sequence-objective-comparison-20261006`。起動時setup・新科学学習0で、品質改善は未評価。重複プロセスを確認してから`scripts/run_sequence_objective_comparison.ps1 -Mode Train -Worker`で保存済み完了更新から再開する。次は両実25M終端・全日本語/全160内容と採否。Base/Chat未採用、全五目標継続。

採用候補の独立training seed/full dev/保護test→実mid-training/SFT対direct/retention/全sampling内容→実人間評価→HF/GGUF/Q8/Q4/実UIという全五目標の後続は維持する。準備/CPU検証はこの完了証拠ではない。

### 同25M CE対sequence ULの完了・採否と次の診断（2026-10-06 JST）

actual501165は終了・ps不在。large1B＋20M親から各25M教師、計50M科学教師を完了。両770更新/各25,231,360 valid・physical入力、同teacher/source/genre/EOS/cursor/token digestを実checkpointと全historyで確認した。継承Adam/scheduler/RNGと親cursor、再加熱なしLR、実CUDA再開各24checks、全日本語192/331/1119・共通dev256/122343 body tokens/472055 bytes、全160原文とSHA付き個別nonblind notesの監査が成功。科学GPU727.265864秒、検証48更新1559884教師/103.834166秒（失敗測定を含む）、合計831.100029秒で1800秒内。TensorはWSLに保持、81text/8,773,723bytesの可搬archive（gzip1,792,157bytes/SHA5b9fd1a2…）を保存した。

| 条件 | 追加CE教師 | BPB↓ | 意味 | JBLiMP | JCQA | 文法2/80 | 関連2/80 | 一貫性2/80 | 適切完結/80 | EOS/80 | 自動反復/80 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CE / alpha0 | 25M | 1.148111 | 52.604% | 79.456% | 31.635% | 39 | 39 | 12 | 22 | 42 | 18 |
| CE＋sequence UL / alpha0.1 | 25M | 1.245716 | 45.833% | 70.997% | 19.929% | 20 | 6 | 0 | 6 | 32 | 7 |

両条件Unicode/role/empty0。反復は減ったが一貫性差-12/95%CI[-.2375,-.075]、EOSとBPBも悪化し、既存relative/absolute/original-Webの全条件未達。alpha0.1候補は不採用、反復減少だけでBaseを採用しない。独立人手未実施、10M容量限界や教材増量一般の無効を証明したとはしない。旧10B UI502043/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start12369434とHTTP親SHA410f975d…/10,000,007,168tokens/busy=falseへ復帰を確認。詳細は`reports/phase6/sequence_objective_comparison_review.json`/`sequence_objective_comparison_completion.json`。

保存済み生成をCPUだけで調べると、研究用token4gramの候補行はCE49→UL67、候補位置1517→1178。これは旧自動反復18→7とは異なる定義であり、どちらも改善・採用基準へ置き換えない。学習内の生成1536件/192rollout/skip0は両条件同じpolicy、body50320→74404、負例位置17423→15118、生成EOS1137→1053で、負例生成量は教師量と別に保存した。token候補の減少・補助lossの減少と、未見の文章品質の改善は一致しなかった。

次の一手は**学習を伸ばす前の、trainのみ・optimizer更新0の勾配診断**。コマンドを実装してから、同じ固定train窓と完全な文書頭のprefixを使い、実親/CE終端/UL終端を比較する。GPU60秒上限を事前固定し、CEと補助lossの有限値、clip前勾配norm・cosine/層別比率、抑制special0/1/2/4/5/6/7への確率質量、負例token IDと復号片を記録する。alpha0/.01/.1の比率は同じ勾配から計算し、ここで新しい科学学習やモデル品質を主張しない。終了条件は3checkpoint/同train入力の全診断・実GPU時間・更新0・原重み不変・UI復帰の記録。dev/testの正解やprefixを学習へ入れず、巨大indexの再scanや全量重複照合を行わない。

仮説は補助勾配の強さ、生成時のspecial抑制と損失分布の差、token4gramが罰する日本語の単位・prefix条件の不適合。いずれも今回の比較だけでは原因として確定していない。[一次論文](https://arxiv.org/html/1908.04319v2)は本文で単語単位、付録でGPT-2のBPE実験も扱うため、BPE一般に無効とは解釈しない。診断後に根拠のある変更を一つ選び、次の対照・教師量・GPU予算と終了条件を凍結する。失敗したalpha0.1の長期延長、無根拠のalpha探索、未採用BaseからのChatは始めない。Base採用→独立seed/full/test→Chat/retention/人手→量子化/実UIの全五目標は継続し、旧数値7失敗と品質条件は維持する。

### 勾配診断完了と、次の比較から最終利用までの計画（2026-10-06 JST）

`diagnose_sequence_objective.py/ps1`を実装し、勾配幾何・係数計算・特殊token確率の6 CPU testsに合格。凍結config SHA20f17b2b…でactual503238はGPU25.557537秒/上限60秒で完了し、実processは不在。train先頭32768入力/32397 CE targetsと8文書頭prefixだけを3つの実checkpointに共通使用した。optimizer更新0/新科学教師0、全重みの完全一致とRNG復元を確認。13GB index再scanなし、dev/test未使用。元10B UI503513とHTTP親SHA410f975d…/busy=falseへの復帰を確認。結果・全24生成/負例ID・層別勾配・frozen sourceは`reports/phase6/sequence-objective-diagnostic-20261006`、完了記録は`reports/phase6/sequence_objective_diagnostic_completion.json`。

親のUL/CE勾配norm比20.174929、cosine0.023000。alpha0.1の重み付き比2.017493/合成勾配対CE cosine0.460516に対し、alpha0.01なら比0.201749/cosine0.980436。CE25M終端でもalpha0.1の比2.146628。これは反復補助更新でCE方向が大きく変わるという局所的な根拠で、全学習の唯一原因の証明ではない。UL25M終端の比は0.183336へ低下したが、先の独立dev品質は悪化済みであり、補助loss低下を成功としない。生成特殊tokenへの平均確率は親0.000001275/CE0.000001869/UL0.000016636、raw argmaxが禁止tokenの割合は全て0。この入力で特殊tokenへ確率を逃がす仮説は支持されない。負例は句読点・助詞・語断片も含むが、機能語を含むことだけで誤った罰と断定しない。

| 段階 | 目的・実行内容 | 完了条件 |
|---|---|---|
| 次の短期比較 | 同じlarge1B+20M親・教師25M・入力順・Adam/RNG/LRから、補助係数だけ0.1→0.01に変更。従来CE25Mは全recipe/source/data/評価一致を確認できる場合のみ既存証拠を再利用。新CUDA保存再開と速度を測り、予算を凍結してから起動 | 全80個別内容・共通byte BPB・日本語評価・既存相対/絶対条件で採否。未凍結・未開始で、改善保証なし |
| Base改善と学習量 | 短期比較が既存改善条件を満たす場合、必要な学習量を節目ごとに延長。データ量変更は同学習量の別比較に分離 | 文法・意味の一貫性・適切完結・EOS・反復・文字処理を同時に改善。失敗条件を10Bへ自動延長しない |
| Baseの確認 | 有望な全recipeを独立training seedで再現し、full devを評価。選択終了後に保護testを使用 | 既存採用条件に合格し、短い日本語の続きを安定して生成できる採用Baseを保存 |
| Chat | 採用Baseから直接SFT対対話中間学習→SFTを比較。Assistant本文＋EOT、自己生成履歴2〜4ターン、訂正/否定、複数sampling seed、Base能力保持を評価 | 停止・文脈・応答品質・retentionを満たす候補を得て、独立人間レビューと最終評価を完了 |
| ローカル利用 | float/HF/GGUF・Q8/Q4で品質と速度/容量を比較し、採用重みをWebUIへ接続 | 量子化後も停止・Unicode・内容品質を維持し、再現手順と実成果物を保存 |

短期比較が不合格なら、保存された失敗例と旧数値7失敗を基に、計算経路の不一致または負例単位の一仮説を選び、対照・上限・終了条件を先に固定する。データ増量も10M容量不足も一般結論にしない。目標達成日は現時点では見積もれず、直近比較の実測と採否ごとに次段階の時間を更新する。既存対照・教材・hash証拠を再利用し、不要な全量照合を避ける。PythonはWSL uv、意味のある節目でlocal commit、pushなし。Base/Chat未採用、全五目標は未達のまま保持する。

### 係数0.01の実比較完了と、教材の学習被覆を切り分ける次の研究（2026-10-06 JST）

`dfe67e1`で実CUDAの全state/history/有限値・旧CE入力順25checks、24検証更新779980教師、GPU47.458262秒を確認し、同親・25M教師/alpha0.01を凍結した。actual504808は科学770更新/25,231,360 valid・physical入力を完了し終了・ps不在。終端SHA f1a95ec6a95293c0fecc5c5033c68b0da5fffe38d760234876ae846a003f3a5d、累積1,045,000,000教師。旧CE25Mはsource/親/データ/最終sampler・token digest一致と既存全80notesを確認して再利用し、新科学25Mと比較計50Mを区別する。新学習step271.356074秒/評価込み366.194958秒、検証込み413.653220秒で新GPU1800秒枠内。13GB indexは実最初1passで照合とcompact化を行い、科学起動ではchecksum付き圧縮配列を再利用した。

| 同親・各25M教師の条件 | BPB↓ | 意味 | JBLiMP | JCQA | 文法2/80 | 関連2/80 | 一貫性2/80 | 適切完結/80 | EOS/80 | 自動反復/80 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 従来CE / 再利用 | 1.148111 | 52.604% | 79.456% | 31.635% | 39 | 39 | 12 | 22 | 42 | 18 |
| CE＋UL alpha0.1 / 先行結果 | 1.245716 | 45.833% | 70.997% | 19.929% | 20 | 6 | 0 | 6 | 32 | 7 |
| CE＋UL alpha0.01 / 今回 | 1.163730 | 57.292% | 73.716% | 26.988% | 29 | 13 | 7 | 10 | 28 | 32 |

全条件Unicode/role/empty0。今回の一貫性差-5/95%CI[-.1375,.0125]は悪化を統計的に確定するものではないが、既存relative/absolute/original-Web条件は不合格。alpha0.01も不採用、係数低下だけで解決したとはしない。全80を個別に読み、算数の誤りと文法、創作や別の自然な続きと意味破綻を区別して理由を保存した。自然な完結は庭の花、写真の思い出、手袋、翌年の取り組み、お菓子の共有、読み直し、無理せず朝を過ごす等にあるが、全体で必要水準へ届かない。独立人間未実施。生成1536/body63633/EOS980/負例23965/追加valid226370・physical290656/skip0を教師と別計数した。反復補助lossの減少や少ない局所勾配だけで未見生成の改善は保証されない。

結果は`sequence_objective_low_alpha_review.json`/`sequence_objective_low_alpha_completion.json`、全raw/notes・60text/6,710,697bytesはgzip1,268,979bytes/SHA38a839899499b546fcb153bfe5442dcfeccd4cf875b42ed89e7964cf0b718150で保存。元10B UI505376/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start12551048とHTTP親SHA410f975d…/busy=falseを確認。科学jobは終了し、追加alpha探索・失敗UL長期延長は行わない。

次の一仮説は**新75/20/5の2B準備教材に対する学習不足**。現large1B stableはepoch0/position984800/blocks1953126で、並べ替えたtoken blockの約50.4%を通過した状態。これは原文の独立固有量・全document学習済み率の証明ではなく、教師tokensと準備tokensも同じ分母ではない。過去の500M教材5Bは別mixture/反復数であり、この新2B教材の被覆を一周程度まで進める効果は未測定。

明示する新研究は旧large1B stable（checkpoint30775/SHA df5295b9e7cfce14dff6a77ce2a9675fbbf67e48639045c4bb721063dce27fbf）から、CEのみ・同pool/原入力順・LR/Adam/RNG/cursorを保ち累積2B教師へ進め、同20M decayを評価する案。比較対照は旧large1B＋20M decayの全日本語/80件を一致確認して再利用し、25M目的比較のCEやUL枝とは混同しない。原stable1Bの実学習1502.646秒を速度の起点に追加1B/同20Mを見積もり、新実CUDA stable/decay保存再開・実速度からGPU上限案2700秒を事前凍結する。コマンド/設定は未実装・未凍結、科学学習0。

既存の品質改善を前提とする自動延長コマンドは拒否条件を保持し、そのgateを変更・迂回して既存条件に合格したとは扱わない。この研究は学習被覆の仮説を明示して別契約/runner/reviewerで実装し、最終採否の一貫性対応+8/80・CI下限>0、文法56、一貫性/適切27、EOS37、反復18以下、Unicode/role/empty0、共通byte BPB/元Web条件を保持する。終了条件は実2B＋同20M・同入力/会計・日本語/全80・全品質採否・local commit/UI復帰。合格改善が得られた場合のみ次の5B等を測定予算付きで選び、独立training seed/full dev/protected testを経てBase採用する。Chat/retention/複数sampling/実人間評価→HF/GGUF/Q8/Q4/実WebUIという全五目標は維持し、今回の不採用や次案だけで目標を完了にしない。

### 2B学習被覆比較の速度実測とv2科学レシピ（2026-10-06 JST）

原CUDAのstable/decay22checksは完了。毎更新保存16stepを速度の起点にしたところ予測4520.080秒で旧2700秒案に収まらず、同親・原入力・学習状態を固定した64連続対64毎保存の診断を実施した。連続median49.303ms、毎保存median81.468ms、15終端stateとfirst16学習履歴一致。診断35.229秒/4,159,460検証教師、原probe60.141秒/1,039,730検証教師も全会計に残し、重みは科学に使わない。これは速度の証拠で品質改善ではない。

原凍結source/config/resultは不変で、別run_textbook_coverage_v2.py/ps1・review_textbook_coverage_v2.py・textbook_coverage_2b_v2.jsonを凍結。科学条件は同2B prepared・stable1B親からCEのみ累積2B・同20M decay、旧large1B+20Mの全80/日本語を対照に再利用。250update durable saveの実測費用とwarmupを含め、学習・保存1571.308秒、30%余裕と評価480・実2B decay検証60を加え2582.700秒、新検証込み2678.070秒見込み。v2の全GPU上限は明示3000秒、本job2904.630秒。16CPUtests/2.33秒、構文/科学preflight成功。まだ科学学習0、次は永続本学習・全80採否、既存品質基準やBase/Chat採用条件は変えない。改善なら独立seed/full/testへ、不合格なら失敗例に基づく一要因比較へ進む。全五目標を候補の完了だけで完了にしない。
### 2B学習被覆の実結果と、ここからの長期計画（2026-10-06 JST）

同prepared2,000,001,312 tokens・75/20/5教材を保持し、旧large1B stableからAdam/RNG/cursor/LRを継いで累積2B教師へ進め、両節目を同20M decay後に比較した。新科学1.02B教師、実jobGPU1661.575秒＋事前検証95.370＝1756.944秒。保存再開/会計/日本語/全80個別内容まで完了し、actual507801は終了・不在。主な結果は以下。比較対象は同素材の学習量であり、新しい教材量を増やした実験ではない。

| 同2B教材の学習条件 | BPB↓ | 文法2/80 | 一貫性2/80 | 適切完結/80 | EOS/80 | 自動反復/80 |
|---|---:|---:|---:|---:|---:|---:|
| 旧stable1B＋20M decay | 1.157868 | 44 | 14 | 25 | 43 | 19 |
| 今回stable2B＋20M decay | 1.146757 | 53 | 14 | 26 | 50 | 18 |

一貫性差0/95%CI[-.1,.1]。文法・停止・BPBの改善はあるが、意味のつながりを保つ生成は未解決。JCQA31.457→28.597%、JBLiMP79.154→77.946%も保持する。既存絶対基準は文法56/80、一貫性27/80、適切27/80、EOS37/80、反復18/80以下、Unicode/role/empty0。今回文法・一貫性・適切と原Web BPB guard等が不合格で、Base未採用。非blind Codex判定であり独立人間評価ではない。教材不足を全面否定せず、10M容量限界や5B/10B延長成功も断定しない。

証拠は [完了記録](../reports/phase6/textbook_coverage_2b_completion.json)、[採否](../reports/phase6/textbook_coverage_2b_review.json)、[全80理由](../reports/phase6/textbook_coverage_2b_notes.json)、[可搬manifest](../reports/phase6/textbook_coverage_2b_evidence_manifest.json)。archive104text/23,757,435bytes、gzip5,880,129bytes、SHA3f490852ae9c35083dba6bde3d0c720bd39934b6bc9fe91ad0c73117394757c6。full checkpointsはWSLに保持。元10B UI復帰済みで、今回の不採用候補へdefaultを変えない。

以降は提案で、新しい診断/学習は未実装・未凍結・未開始。順序と目的・終了条件を固定し、原因が支持されない比較を繰り返さない。

| 順序 | 目的と行うこと | その段階のゴール・次へ進む条件 |
|---|---|---|
| 1. 文脈依存の切り分け | 今回の広い2B教材・実1B+20M/2B+20M重みで、同じtrain書き出し/正解続きを、実際の前方連結文脈付きと単独BOSで測る。重みを更新しない。 | 凍結した全例×両文脈×両重みの正解続き/EOS確率とraw生成を保存し、差を特定する。GPU上限180秒、optimizer0、重み不変。結果・判断・UI復帰・local commitまでで終了。 |
| 2. 原因に対応する一要因比較 | 文脈差が支持されれば連結学習と文書境界を意識した学習を、同親・同教材・同教師予算で比較する。差が乏しければ、数字/主体/因果の失敗例から教材または条件学習の一仮説を選ぶ。 | 変更が未見の一貫性を改善し、停止/反復/BPBを退行させない証拠を得る。対照・教師量・GPU上限・採否を先に凍結する。改善しなければ同条件の長期延長をしない。 |
| 3. Baseを確定 | 有望な条件だけを実測予算内で学習し、独立した学習seed42/43、full dev400＋long40、最後に未使用の保護testで検証する。 | 既存品質基準を満たす再現可能な10M Baseと実checkpointを採用する。保護testはレシピ/seedを固定した後に開き、探索へ戻して使わない。 |
| 4. Chatを学習・比較 | 採用Baseから直接SFTとDialogue mid-training→SFTを比較。Assistant本文＋EOTを学習し、自生成履歴の会話、複数sampling、Base能力保持を測る。 | 関連した返答・文脈維持・停止の既存Chat基準と保持条件を満たす。実人間のblind評価/一致率まで確認し、採用Chatを決める。準備済みコマンドを実学習の成果と混同しない。 |
| 5. ローカル成果物を完成 | 採用Base/ChatをHF/GGUFへexportしQ8/Q4、実メモリ/速度/容量と品質差、ローカルWebUI、再開/再現手順を確認する。 | 実際に起動して使えるBase・Chat・量子化成果物と評価台帳を揃える。目標5〜10MBの達否も実容量で報告する。全成果物が揃った段階でいったん停止する。 |

直近診断では、旧stable1Bの次の固定train batchを既存compact indexから読み、両比較checkpointに共通の文書prefixを採る。最大first4×32入力から目標24例を事前選定する案で、供給不足なら実数/source内訳を明記し、良い結果が出るまで選び直さない。同じBOS/body prefixと同じ正解suffixで本文/EOS NLL・rank、最大64tokensのgreedy、EOS/反復/UTF8を測り、raw context/target/出力と実GPU時間を残す。dev/test原文を学習prefixへ使わず、optimizerを作らず、RNGを分離する。対象と手順は新コマンド実装時に凍結する。

この診断は局所的なtrain文脈差の測定であり、代表的なコーパス品質や因果を単独で証明しない。過去compact1000文書のpacking/shuffle/isolated比較は既に実施・不採用で、同じ比較を再実行しない。今回は広い教材を一周程度学習した後の実重みにおける未確認部分へ限定する。支持された場合にだけ、新しい同教師比較を設計する。旧数値7失敗も未解決記録として残す。

データ増量は引き続き選択肢とするが、独立した内容・多様性の不足が支持された時に行い、「新教材tokens」と「実学習教師tokens」を別計数する。単純に5B/10Bへ進める判断は今回の結果では行わない。独立seed/full dev/保護test/Chat実学習/実人間は現時点で0、全五目標未達。全体の完了日は原因修正の結果次第なので確約せず、各学習比較の予算は実測から都度更新する。13GB index再scanや全量重複照合、旧対照の再学習/再生成は必要な変更がない限り行わない。全PythonはWSL uv、意味のある節目でlocal commit、push/公開なし。

### 広い教材の文脈診断実測と、次の物語教師比率比較（2026-10-06 JST）

前節の最初の診断を実装・実行した。stable1Bの次の実32入力からWeb/教材/物語各8の完全なtrain文書prefixを固定し、前方文脈は切らず、1B+20M/2B+20M重みで連結文脈/単独BOSの全96条件を測った。CPU5tests/1.15秒、actual514599はGPU81.779秒で完了し不在。optimizer/科学教師0。全96のraw/同gold/停止/bytes/flagsを再構築し、全24原文と全96生成を読んだ理由を保存した。実人間ではなく非blind Codex観察、原固定dev80の採用点数へ混ぜない。

| 学習済み重み | 連結の本文NLL/token | 単独の本文NLL/token | gold EOS top1（連結/単独） | 自由生成EOS（連結/単独） | 自動反復（連結/単独） |
|---|---:|---:|---:|---:|---:|
| 1B＋20M | 1.980812 | 1.987586 | 22/24・22/24 | 12/24・15/24 | 2/24・0/24 |
| 2B＋20M | 2.015694 | 2.023371 | 22/24・22/24 | 13/24・17/24 | 4/24・2/24 |

同じ正解suffix本文2303tokensを採点、EOSは本文分母に含めず別表示。case平均の連結有利NLL差は0.010976/0.009563natsで、事前marker0.1nats＋正差60%以上のうち前者が未達。強い文脈依存を支持しない局所結果であり、因果や全train代表性の証明ではない。1B decayが直近に見た親次batchを2B重みは以前に見ており、このtrain局所NLLから学習量増加で全体が悪化したとは推論しない。全devの改善/原不採用は前節のまま保持する。

gold suffixがEOS込み64以内なのは9/24件。ここだけの自由生成EOSは1B連結7/単独7、2B連結7/単独8。goldが64より長い残15件の打切りをEOS学習失敗と同一視しない。逆に単独の両重みに改行だけで止まるempty1があり、EOSだけで内容成功としない。鳥が助けられる側から友達を助ける側へ変わる、目標の自己定義、同じ会社/産地の循環、2B連結の地震→温暖化の飛躍などは両文脈で残る。創作の自然な別継続やgold非一致だけを失敗にしない。原文の事実性認証も行っていない。

[診断完了](../reports/phase6/broad_context_diagnostic_completion.json)、[raw audit](../reports/phase6/broad_context_diagnostic_review.json)、[全24個別観察](../reports/phase6/broad_context_diagnostic_content_notes.json)を保存。archive119text/4,215,027bytes/gzip759,995bytes/SHA7c1c946573235b55b2c8da00d29faaf65f45b419d892c53c4e5ddfc7cd06ce1c。重み不変/gradientなし/eval/RNG復元は双方成功。元10B UI515252/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start12979742とHTTP親SHA/training_tokens/busy=falseを確認。文脈を足すだけで課題が解決したとはせず、旧compact packing/isolated比較を繰り返さない。

次は**同教材内の物語教師比率**の一仮説を調べる。短い日常/人物の条件を学ぶ頻度を上げる効果は仮説で、今回の局所観察だけで不足が証明されたとはしない。教材総量は同じ2,000,001,312 serialized tokens、目的関数はCEのみ。以下は新研究の準備で、学習コマンド未実装・scientific config未凍結・新GPU/学習0。

| 条件 | Web教師 | 教材教師 | 物語教師 | 追加教師計 |
|---|---:|---:|---:|---:|
| control75/20/5 | 75M | 20M | 5M | 100M |
| story20：60/20/20 | 60M | 20M | 20M | 100M |

両条件は実2B+20M親SHA965a06dc1537ed917de98c565d78ae76f19d99ad075f019067a4324a6cbd2249から同一model/Adam/RNGを継ぎ、実terminal LR0.0002を上げずconstantで学習する案。context1024/最速既測定batch32/accum1/BF16/Flash＋compile reduce-overheadを保持する。source別文書shuffleを新しく明示forkし、両条件で同seed/初期source順を揃える。旧mixed block cursorは親lineageに保持し、新samplingが旧cursorをそのまま継いだとは偽らない。新sampler/optimizer/RNG/genre教師/input/physicalは完了更新で保存する。

[供給と親の実確認](../reports/phase6/story_weight_comparison_preparation.json)はprepare_story_weight_comparison.pyによりCPU0.506秒で完了。既存checksum付きcompact indexを使い13GB再scanなし。物語はbody98,478,072＋EOS761,448＝99,239,520教師、Web1,487,009,972/教材397,058,104教師で両条件の供給を満たす。これは独立固有原文量やglobal重複監査ではなく、既存train poolの会計である。新たな取得・全量変換を学習の前提にしない。

次の具体的な作業は、同教師quotaのsource sampler/trainer/永続runner/reviewerを実装し、CPUでquota/EOS/文書境界と連続対再開を確認する。その後、両条件の実CUDA連続4対2+2/fullstate/有限値/実速度を上限120秒で確認。全GPU上限1800秒に検証・各100M・同日本語/生成評価を含めて収まる実測予測が得られた場合だけscientific configを凍結して本学習する。旧品質改善を前提とする自動延長コマンドは拒否条件を保持し、新研究契約に合格したと混同しない。

終了条件は両actual100M教師、同dev256/common-byte BPB・日本語192/331/1119・固定dev80各/全160 raw-bound内容・全原relative/absolute/original-Web採否、実終了PID、可搬証拠/UI復帰/local commit。既存2B+20M評価は親能力保持の参照として再利用し、新100Mのmatched controlへ置き換えない。合格候補だけを独立学習seed/full dev/保護test→実Dialogue/SFT/retention/複数sampling/人間→HF/GGUF/Q8/Q4/実UIへ接続する。不合格なら採用せず、根拠なしの比率総当たり/自動5B・10B延長を行わない。全五目標/旧数値7失敗/全品質基準を維持する。

### 物語教師比率比較の実装・実CUDA検証・本学習開始（2026-10-06 JST）

前節の未実装事項を実装した。source別文書shuffleと教師quota、完了更新ごとのfull-state保存/再開、永続jobと評価・全160内容review/archiveを用意。CPU4tests/2.147秒、両条件の実CUDA連続4対2+2は26checksずつ一致した。各32連続timingを含む検証80更新/2,599,809教師は科学から除外、実GPU22.202秒。科学config SHA e5ee42c4bc923632faa5b49eceb76f32e92c9d632bb7d2d292a88117f3938f04、同CE/terminal LR0.0002/親AdamとRNG/同material/各100M、batch32 context1024を凍結。実測training予測control163.984秒/story20 152.996秒、評価余裕込み1012.074秒、科学上限1777.798秒（検証を含め1800秒）。予測は完了や品質の証明ではない。

actual518044/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13077625を実ps確認。controlの100M教師終端checkpoint65244（SHA353cb231d07dfb9e42328ee0e3ad82ead4d1ad875a25559987e6bf2dd44e03f5）はinput100,859,904、共通親から追加100Mで同日本語/生成評価へ進行。科学両条件完了/全160内容採点/品質採否は未完了。jobの初期setup文字列だけで停止を判定しない。[実ジョブ引継ぎ](../reports/phase6/story_weight_active_job.json)とnative reports/phase6/story-weight-comparison-20261006の実PID・チェックポイント・stageを参照し、再開はactual process不在を確認後にscripts/run_story_weight_comparison.ps1 -Mode Train -Worker。

今の比較を完了し、全160を個別に確認して元の品質条件の採否を出す。合格時は独立学習seedとfull dev/保護test接続をこの新source recipeに対応させてから最終Base検証へ進む。準備済みコマンドだけで採用とせず、Base→実Chat比較/retention/複数sampling/人間→export/量子化/実UIの全目標を保持する。不合格時は採用せず原因に対応する次の一要因を選び、根拠のない比率総当たりや長期延長をしない。PythonはWSL uv、local commitのみ、元UIは科学終端で復帰する。
### 物語教師比率の実結果・条件への反応と次のtrain内容調査（2026-10-06 JST）

同じ2B教材と同じ2B+20M親で各100M教師を実学習し、両条件の共通byte256文書/日本語192・331・1119/固定80各・全160の個別内容評価を完了した。control終端65244/SHA353cb231d07dfb9e42328ee0e3ad82ead4d1ad875a25559987e6bf2dd44e03f5、story20終端65243/SHAce267d5dbb0df445896d7d9605e60313a2685e483d715bf23ef8223ff7412e4a。科学教師200M/input201,687,040、検証2,599,809教師は別、GPU453.735＋22.202＝475.936秒<1800。actual518044終了/ps不在と元10B UI519042/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start13123487・ps/HTTP元SHA・10,000,007,168tokens/busy=falseを確認した。

| 同追加100Mの条件 | BPB↓ | 文法2/80 | 関連2/80 | 一貫性2/80 | 適切完結/80 | EOS/80 | 反復/80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| control Web75/教材20/物語5 | 1.129921 | 67 | 49 | 11 | 27 | 45 | 16 |
| story20 Web60/教材20/物語20 | 1.135269 | 64 | 47 | 15 | 24 | 38 | 21 |

一貫性は+4、paired95%CI[-.0375,.1375]で事前+8/下限正の条件を満たさない。EOS・反復は悪化し相対比較不合格、両条件とも絶対一貫性27未達と元Web BPB1% guard不合格でBase未採用。story20は適切27/反復18以下も失敗。Unicode/role/empty0。非blind Codex判定で独立人間ではない。局所構文と事実/数の正答を分け、同じprefix/text/stopの既採点は再利用してrubricを揃えた。内容の短い自然な別継続や幻想表現をgold不一致だけで誤答にしない。

[採否](../reports/phase6/story_weight_comparison_review.json)、[全160理由と可搬manifest](../reports/phase6/story_weight_comparison_evidence_manifest.json)、[実終了/UI確認](../reports/phase6/story_weight_comparison_completion.json)を保存。90text/12,673,202bytes、gzip3,297,073bytes/SHA3ce500e5f09d421c821f0336dfea5a8070873f995a1ac6033dda8b457bae99a3。可搬90textとarchive SHAを確認し、optimizer等のfull checkpointsはWSL保持。比較終了は全五目標の完了ではなく、独立seed/full dev/保護test/実Chat/人間/量子化は未達。

保存済みの意味dev192を[条件反転family分析](../reports/phase6/story_weight_condition_pair_analysis.json)へ再集計した。追加GPU/教師0、CPU4tests/0.78秒。各categoryは16family×2条件、候補は共通でgoldだけ逆転する。単純な正答率50%を、条件を保持できた証拠にしない。

| category | control両条件正答/16 | story20両条件正答/16 | control同じ候補を選択/16 | story20同じ候補を選択/16 |
|---|---:|---:|---:|---:|
| 否定 | 0 | 0 | 16 | 16 |
| 数量 | 1 | 3 | 14 | 13 |
| 時刻 | 1 | 2 | 15 | 14 |
| 比較 | 0 | 0 | 15 | 15 |
| 照応 | 0 | 0 | 16 | 15 |
| 因果 | 12 | 10 | 4 | 6 |

否定は親2Bも同じ候補16/16、両条件正答0。一方、肯定/否定でmarginが正しい方向へ動くのは三重みとも16/16、中央値parent4.355/control4.630/story20 4.320nats。条件に反応しても順位は反転しない結果で、注意機構が完全に不動、Tokenizerが根本的に壊れている、10M容量限界という証明にはならない。得意な因果だけで総合点が上がることと、条件保持の弱さを分ける。margin診断を生成品質へ代入せず、採用閾値やprimary scoringを変えない。

次に[train本文96件の固定inspection](../reports/phase6/conditional-content-pilot-20261006/result.json)を準備した。Web/物語/教材各32、64〜512 body tokens、seed2026100643、最大50000 document draws/CPU30秒を先にコードで固定。実CPU0.451秒・関連2tests/0.88秒、checksum付きcompact index再利用、13GB再scan/全量変換なし。これは既存正規化train本文からの未確認sampleで新prepared0/学習0/GPU0。完全な元source bytesや独立source family/全corpus代表性/品質の証明ではなく、将来の学習poolにもまだ採用しない。

次の具体的な作業は全96本文を個別に読み、各文書の文法的完結、明示的な否定/数量/時間/比較/主体/因果条件、その条件と結末の接続を記録すること。条件を含まない正常な文書を弱いと自動判定しない。内容の失敗と条件例の供給不足を分け、必要な教材の形と一つの同教師比較を根拠から選ぶ。dev192の文言/固有名/テンプレートを学習へ転用せず、保護testは開かない。次の本学習は内容採否・対照/teacher予算・GPU実測上限・元品質条件を先に凍結する。比率総当たり、根拠なしの5B/10B、基準緩和はしない。

品質Baseを得た後の独立学習seed/full dev/保護test→実Dialogue mid-training/SFT対direct/retention/複数sampling/人間blind→HF/GGUF/Q8/Q4/実WebUIまでの全五目標を保持する。旧数値7失敗を消さず、PythonはWSL uv/local commitのみ、push/公開なし。