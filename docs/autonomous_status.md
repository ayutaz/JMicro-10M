# 現在の状態

2026-10-15次比較の構造CPU準備: [明示proposal](../reports/phase6/cross-gqa-map-preparation-20261015/proposal.json)を実装前に保存し、別KV groupのQ/K mapを現在groupのVへ適用して元mapからtanh係数で差し引くvariantを選定した。元native source/NoQKNorm/Q4-KV2/13L/hidden256/FFN640は保存し、追加は各層4scalar、10,001,152→10,001,204（元9.5M〜10.1M内）。係数0で既存重み/O射影を変更しない。同KV内だけの混合がo_projへ吸収される案は除外し、全元head出力0でもcross-map-on-current-Vが非零になる反例をCPU確認。旧query-headwise output gateやMHA再配分の救済ではない。論文の独立paired Q/K・head norm・lambda初期化とは異なる独自variantで、注意noise/GQAが原因との診断や日本語10M改善の証拠ではない。

[CPU preparation](../reports/phase6/cross-gqa-map-preparation-20261015/CPU_preparation.json): model18 checks（独立行列式/初期logit・重み・RNG/符号係数gradient/因果性/active padded-chunk cache/strict state/export拒否）とtrainer12 checks passed。static-zeroの旧CE各更新既存weights/名前対応Adam状態・schedule/RNG/全sampler exact、有効時の原stream保持/係数更新、6対3+save+3全typed state/history exact、壊れたstateの変更前拒否、Adam中断後save/retry禁止と正常復旧を確認。元CE stepをそのまま再利用し、追加教師/aux loss0、二つのmapのquery-head位置を教師と別会計にした。

[実元親CPU parity](../reports/phase6/cross-gqa-map-preparation-20261015/actual_parent_CPU_parity.json)は元10B親と既存technical token spansだけで、全元weights/全logit/cache/RNGの差0、実count10,001,204を確認（CPU0.301962秒/30内）。親の既検証SHAに固定size/mtimeを照合して再利用し、新しい全重みhash照合とは呼ばない。新TRAIN/DEV/TEST・Tokenizer・実GPU/科学学習・重み保存0。完了assayを再実行しない。次は専用owned CUDA gate/永続science CLI/architecture差分を明示した対照・隔離評価・reviewerを実装し、180秒technicalと総4800秒提案内の実測後だけ科学契約を凍結する。GPU比較は未開始。独立fresh全pipeline/fullDEV/全440/新TEST/採用と4項目goalは未達。

2026-10-15最新終端: **TRAIN sentence-copy確率減衰100Mは不採用で閉鎖**。[completion](../reports/phase6/pseudo-repetition-science-20261015/completion.json) / [全80採否](../reports/phase6/pseudo-repetition-science-20261015/review.json) / [個別notes](../reports/phase6/pseudo-repetition-science-20261015/notes.json)。実17,698更新・正確100M main教師・141,584合成row/51,736,185確率比較。凍結reviewerで全更新historyとtyped model/Adam/scheduler/RNG/sampler/counters、原CE対照の全stream/digest/教師/EOS/bytes/main physical一致を確認した。文法44→53、一貫性2→2、適切完結2→3、EOS19→22、反復45→31（各80）、BPB0.9984871625→0.9996794278、一貫性差95%CI[0,0]。元絶対・相対・strong・historical保持は未達。反復の減少をBase完成としない。

全80をprefix/rawと個別理由付きで読みCodex非blindと記録。literal「á」を含む出力は既知CE0→候補12件で、notesに語句の崩れを保存した。全12件はvalid UTF8であり、既存raw Unicode failure0を改変せず、後付け文字数の観察を採否基準へ追加していない。科学GPU2544.969800秒＋技術12.190336秒＝2557.160137秒、科学4746/総4800内。実PID41491不存在・Windows worker33100終了・ledger closedを確認。元10B UIはPID44053/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start65703471とHTTP元親/Tokenizer/10M/idleへ復帰を再確認。最終checkpoint SHA896cc0a596db2ad4fa7c0ed1c35b8dd30713a3f75cfe55dc150c2ca86394421b、全weights/Adam/RNG/sampler/metricsはWSLのみ。7つの小metadata/raw/notesをWindowsへ同hash保存。既存reviewerの終端数値監査を重複実行する別assayは追加していない。

固定decay/係数/copy数/文境界/親/seed/decoder/予算の救済・再launch・延長をしない。次は別の根拠ある同10M比較を1件選定する。独立fresh全pipeline学習/fullDEV/全440内容/新封印TEST/採用は候補資格なしで未実施。4項目goalはactive/未達で、比較閉鎖を全目標完了へ縮めない。Chat/SFT・量子化・大型化・公開は範囲外。以下の学習中記述は当時の観測。

2026-10-15最新実job: **TRAIN sentence-copy確率減衰100M科学比較が稼働中**。[起動観測](../reports/phase6/pseudo-repetition-preparation-20261015/science_launch_observation.json)でWSL PID41491/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start65448557、Windows worker33100、GPU lock同ownerを確認。300更新/1694544教師/47.330852秒は途中値。[科学契約](../configs/phase6/pseudo_repetition_science_20261015.json) SHA3e27ed16d31764fa2e3242c6205994688f3676a43f13f712c1b040c08ec10d43は同native10,001,152/元10B親/元TRAIN/48/42/main CE100M、aux0.1・前copy確率0.5倍のdetach目標を固定。科学4746秒、技術12.190336秒を含む総4800秒。専用永続runner/reviewer、既存safe DEV256/80/Japanese evaluatorを接続し、13 CPU workflow checksを完了。500更新checkpoint/20更新heartbeat、原CEと合成比較位置を別会計にする。

直前の[owned CUDA gate](../reports/phase6/pseudo-repetition-probe-20261015/completion.json)はPID41063終了・44技術更新/255177 main位置、全state/全historyの6対3+save+3 exact、finite CE48x1024/aux8x512 backward、最大10755451392bytes・stress optimizer0/weights不変。実32timingsから科学4746秒を見積もった。native trainer14 CPU checksでaux無効時の旧CE各更新weights/Adam/schedule/RNG/全sampler一致、有効時の原stream維持/nonzero native語彙gradient/実全state resume/壊れたstateの変更前拒否/Adam中断後save禁止と正常復旧を確認。最初のWindows worker38084はGPU/UI停止前にGet-FileHash未検出で終了、原ログを保存。後の独立照会では検出でき原因未確定。別v2 operational launcherで同PowerShell7を明示し、凍結技術条件・予算を変更せず一回のCUDA gateを実施。元10B UIはPID41135/start65436367へ復帰確認後、今はscience中のみ停止。

次は同実processを観測し、100M終端の原CE対照全state/stream/教師/EOS/bytes/main physicalと全80個別内容を確認する。再launch/refreeze/source editをしない。signal中断だけvalid checkpoint/closed remaining ledgerで同条件resumeする。候補資格はまだなく、独立fresh全pipeline/fullDEV/全440/新封印TEST/採用は未達、4項目goalはactive/未完了。以下の「trainer/probe/science未実装」は準備時の履歴。

2026-10-15次比較のCPU準備: [prospective案](../reports/phase6/pseudo-repetition-preparation-20261015/proposal.json)はTRAIN文の合成全句反復に対して、同tokenの直前copy確率の0.5倍をdetachした正の目標へ合わせるDITTO系variant。旧4-gram rollout ULのzero-target/生成負例とは実原sourceで区別し、低すぎる反復確率を上げる勾配も確認。元10B親/native10,001,152/原CE100M/48/42/fresh AdamW1e-5を維持、aux coefficient0.1、既存TRAINのjoint-body tokensと句読点のbyte境界で最初の適格文を4〜16copy/512入力へ構成する。追加params/RNG/教材exportなし。論文の英語750M・交互更新を再現したとは呼ばず、日本語10Mの改善や原因を実証していない。

pure14 CPU checks passed（独立確率式/前copyのstopgradient/低確率への正勾配/飽和1000でclampなしの有限補正/元byte-boundary/未変更/不正pair拒否）。[一回限りCPU feasibility](../reports/phase6/pseudo-repetition-preparation-20261015/CPU_feasibility.json)は元32x48 TRAIN draw、256適格row/32 active batch/94405比較位置/最大512入力、CPU2.702730秒/30内、元rows/全material state不変。readはTRAIN/Tokenizerの5種類だけ、モデル/optimizer/GPU/DEV/TEST/newdataset0。完了auditを再実行しない。次は専用native trainerとdisabled CE equality/実全state resume CPU checks、その後owned CUDA180秒以内と総4800秒提案内の実測。永続science CLI・隔離評価・採否・凍結科学契約は未完成、科学学習0。独立学習/fullDEV/新TEST/採用と4項目goalは未達。

2026-10-15最新終端: **context likelihood100Mは不採用で閉鎖**。[completion](../reports/phase6/context-likelihood-science-20261015/completion.json) / [全80採否](../reports/phase6/context-likelihood-science-20261015/review.json) / [数値監査](../reports/phase6/context-likelihood-science-20261015/numeric_completion_audit.json)。実17,698更新・正確100M main教師、351,786 aux pair、原CE対照との全sampler/digest/scheduler/教師/EOS/bytes/main physical一致、全更新history/FIFO/model/Adam/RNGを確認。文法44→51、一貫性2→1、適切完結2→1、EOS19→22、反復45→50（各80）、BPB0.9984871625→0.9985244324、一貫性差95%CI[-.0375,0]。元絶対・相対・strong・historical保持を満たさない。全80をprefix/rawと個別理由付きで読み、Codex非blind・独立人間blind未実施と記録した。

科学GPU2410.335961秒＋技術9.415508秒＝2419.751470秒、科学3656/総4800秒内。実PID6927不存在・Windows worker20024終了・閉じたledgerを確認。元10B UIはPID38043/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start65165302とHTTP元親/Tokenizer/10M/idleへ復帰を再確認。checkpoint SHAca2e9e607af618682767b38d48ae55d3164f778d981bed4c773b473b2c57c0b6と全数値state/FIFO/metricsはWSL保全。Gitへは8つの小metadata/raw評価/notesだけを同hashで保存し、教材・weightsは移していない。以下の稼働記録は当時の観測。

固定条件の延長・係数/親/seed/decoder救済をしない。次は別の根拠ある同10M比較を1件選定する。独立fresh全pipeline学習/fullDEV/全440内容/新封印TEST/採用は候補資格なしで未実施。4項目goalはactive/未達、比較閉鎖を完了へ縮めない。Chat/SFT・量子化・大型化・公開は範囲外。

2026-10-15別CPU準備: [isolated DEV400/long40 adapter](../reports/phase6/isolated-continuations-preparation-20261015/completion.json)を実装。元DEV80からcase-majorの5 modes（greedy suppressed/unsuppressed、sampling42/43/44・T.8/top-p.9・64tokens）とcategory先頭2ずつ20prefix×128/512を計画し、元6-ID suppressionを保持。pilotの追加EOT7 suppressionへ無断統一せず、資格後の固定80 raw一致条件を維持。planner8/generator4 CPU checksで旧400/long40のfixture全出力一致、training RNG不変、壊れたTEST fixture非読取り、UNK/raw Unicode/role失敗保持、overflow/期限/非finite拒否を確認。実元codec前検査は440requests・最長prefix+BOS28token、readはDEV manifest/cases/Tokenizer3種類のみ。実model生成/GPU/品質評価/new data/TEST0、fullDEV永続runner/独立学習/全440内容/採用は未達。稼働中scienceのfrozen sources/条件へ接続・変更していない。同実PID6927/start64923858は7820更新/44246925教師/1085.746035秒で生存確認、100M終端と全80内容review待ち。

2026-10-15稼働中の保存証拠: [checkpoint2000 CPU監査](../reports/phase6/context-likelihood-preparation-20261015/checkpoint2000_CPU_audit.json)で実11297746 main教師/39483 aux pair/4060772 repeated likelihood positions、FIFO128/75741 committed anchorsを確認。同更新の保存済みCE対照と全original sampler・digest・scheduler・教師/EOS/bytes/main physicalが一致、全model/Adam/RNG/clock/FIFOと2000行metrics prefixが整合。CPU1.295629秒、追加GPU/学習/Corpus/DEV/TEST/品質評価0。新read-only auditorは稼働中frozen sourcesを変更しない。最新の同実PID6927/start64923858観測は4180更新/23632643教師/592.001431秒、running・stderr失敗なし。監査prefixと途中値は100M完了・品質合格ではない。次は同processを観測し、終端の全state/対照照合・隔離評価・全80内容採否へ進む。4項目goal未達、独立学習/fullDEV/新TEST/採用は資格前のまま。

2026-10-15最新: **context likelihood100M科学比較が稼働中**。[実起動観測](../reports/phase6/context-likelihood-preparation-20261015/science_launch_observation.json)でWSL PID6927/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start64923858、Windows worker20024とGPU lock同ownerを確認。840更新/4744814 main教師/120.778148秒は途中値。[科学契約](../configs/phase6/context_likelihood_science_20261015.json) SHA241ca76dd11a86f7113040dbf4afaec1eb42c11e5a7f925c9006dc6a2c9dcdcfは元10B親/同native10,001,152/元TRAIN・48・42・CE100M、専用学習/FIFO保存/安全DEV256・80/Japanese/採否CLI、13 CPU workflow checksを凍結。科学上限3656秒、技術9.415508を含む総4800秒、500更新checkpoint/20更新heartbeat。終端で元CE対照の全sampler/digest/実schedule/教師・EOS・bytes・main physicalを照合し、全80を個別reviewする。途中値や補助marginを品質合格にしない。元UIはこのGPU job中だけ停止、終端でlauncherが元10Bへ復帰。実process/同jobを観測し再launch/refreeze/source editしない。独立学習/fullDEV/全440/新TEST/採用は資格なしで未達、4項目goalはactive/未達。

直前の[owned CUDA検証](../reports/phase6/context-likelihood-probe-20261015/result.json)はPID6198終了を確認、実44技術更新/255177 main positions、連続6対3+3のmodel/Adam/scheduler/RNG/全sampler/FIFO/history exact一致。CE48x1024/24576 gold、aux96x512/47616 likelihood positionsは有限forward/backward・optimizer0・weights不変、最大11849772032bytes（約11.0GiB）で90%resident allowance内。技術GPU9.415508秒/180内、実32timingsから100M科学見積り3656秒。geometry stressは既存accepted token spansであり新文書/品質証拠ではない。元UIは一度PID6270/start64820221へ復帰しHTTP元親/Tokenizer/10M/idleを確認した後、今回scienceのため停止。新CLI/quality policyは元基準を維持（matched BPB非悪化、strong1%とhistorical Webを別判定）。cached160内容のsafe reader互換をCPU確認し、元混在reader/TESTを開かない。下の「科学未凍結/0」は準備時の記録。

2026-10-15最新: [次の比較案](../reports/phase6/context-likelihood-preparation-20261015/proposal.json)を選定しCPU準備を完了。新機構は同じ元suffixを、元prefixと「同genre/同prefix token数/別family・body・prefix・suffix」の既に通常学習された文脈の下でnative語彙尤度を比較するもの。旧natural InfoNCEの別々の隠れ表現や、固定template outcome ranking/親Web KLとは異なり、suffix-only priorと位置数のcueをそろえる。FIFO128はAdam成功後だけ更新、trainable params追加0/native10,001,152を維持。元10B親/accepted TRAIN/通常CE100M・batch48・seed42・fresh AdamW LR1e-5 WD.1/constantを対照と合わせるprospective案で、科学契約とGPU予算は未凍結。

[一回限りCPU feasibility](../reports/phase6/context-likelihood-preparation-20261015/CPU_feasibility.json)は32x48元TRAIN drawから551 pair/31 active batch、元rows/全material state不変、CPU2.827315秒/30内、read5種類のTRAIN/Tokenizerのみ。新教材/DEV/TEST/実model/GPU/学習0。pure機構12＋実CPU fixture trainer11 checks passed。補助無効時は実旧CEの初期/各更新model・Adam・scheduler・training RNG・全samplerと一致、有効時は原CE stream維持/nonzero語彙gradient、連続6対3+save+3のFIFO含む全state/history一致、壊れたstateの変更前拒否、中断後save/retry拒否と正常復旧を確認。通常CEの完全なbody+EOS<=512 rowだけauxに使い、長文/端数は元CEを全保持する。FIFOのCPU commitはfeasibility simulationで学習証拠ではない。次は専用owned CUDA180秒以内のfinite/resume/48x1024/aux stress/32 timingsと累積4800秒提案内の見積り、その後だけ新科学runner/evaluator/reviewerと契約を凍結する。旧FIM/InfoNCE/ranking条件は閉鎖のまま、seed43/fullDEV/全440/新TEST/採用は候補資格なしで未達。4項目goalを準備完了へ縮めない。

2026-10-15最新CPU準備: `src/jmicro/isolated_japanese_scoring.py`のsafe fixed-diagnostic adapterを実装。[回帰照合](../reports/phase6/isolated-japanese-scoring-20261015/CPU_regression.json)は隔離済みinputsのsemantics192/JBLiMP331/JCQA1119、計1642例/6641選択肢について元token境界・保存済み2M TRAIN unigram・raw sum/SLOR/secondary/credit/tiesを全件exact確認。CPU16 checks passed（実旧scorerとのfixture全row/summary一致、5許可fileだけの実adapterfixture、壊れたTEST fixture非読取り、期限切れ/欠落choice/不正counts/非finite拒否）。実回帰CPU0.165426秒、9種類の既知診断/元Tokenizer/保存countsをreadし、TRAIN token stream/混在suite/TEST/モデル推論/GPU/学習/新dataset0。元countsを再作成せず旧式の採点規則を維持した。現時点で科学recipe未選定、有資格Base/独立学習/fullDEV/新封印TEST/採用は未達。adapterはcheckpoint資格や永続runnerを代替せず、次の別凍結比較へ接続する準備まで。次は既存失敗から別の根拠ある介入を選定する。4項目goalはactive/未達。

2026-10-15の次案調査: [TRAIN索引の境界監査](../reports/phase6/sampling-boundary-20261015/sampling_audit.json)は新しい固定256 byte drawsとCPU11 checksを完了。実frozen samplerは包含行をskipして次行を選ぶため、正確には対象行自身ではなく直前行の索引byte数による重み（先頭/第2行/EOFの例外あり）。256/256で次行、source横断0。条件内分布差の有限標本近似はWeb0.00531、textbook0.02021、story0.000408（storyは7drawのみ）。CPU0.161030秒、openは既存TRAIN manifest/ready/indexの3種類だけ、token stream/モデル/DEV/TEST/GPU/学習0。過去の同selector pairingと結果は保持。原因や大きな生成改善の根拠にはならず、この小さなpolicy mismatchだけを理由に科学学習を開始しない。次は本比較用fixed Japanese diagnosticsのsafe scorer接続を整備し、別の根拠ある比較選定を継続。独立学習/fullDEV/新TEST/採用は未達、4項目goalを完了にしない。

更新: 2026-10-15 JST。文書更新は結果32b8f58/receipt d44b8a0で完了し、ユーザーが目標を解除。その後「4まで進めてください」で直前の4項目（評価分離修理→新同10M比較→合格候補の独立学習/全文DEV→新封印TEST/採用）が明示再開された。Base/Chatは未完成・未採用。Chat/SFT・量子化・大型化・公開は範囲外。

**最新終端: fresh FIM pilotは不採用で閉鎖。** [completion](../reports/phase6/base-fim-pilot-20261015/completion.json) / [全80採否](../reports/phase6/base-fim-pilot-20261015/review.json)で実10000更新・正確94160195教師、同native初期化/元抽出/quota/EOS/bytes/full sampler/original stream digest/actual schedule、DEV256と全80個別raw-bound notesを確認。対照→候補は文法28→31、一貫性2→2、適切完結3→2、EOS13→14、反復49→51（各80）。BPB1.2902028921801718→1.2924141763731125、一貫性差0/95%CI[-.0375,.0375]でpilot screen未達。Unicode/role/empty/FIM marker漏出0。科学GPU1527.822099743993＋技術9.153451952966861＝1536.9755516969599秒、科学2519/総3600内。評価openはDEV manifest/casesとDEV shard4ファイルの6種類のみ。実PID1343は終了、元UI実PID3223/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start64296679とHTTP元親/Tokenizer/10M/idleへ復帰を確認。最終checkpoint SHA5328bca46dbbbd88b1756c3cf7d177c0539c72a25c76ba66caadb9bd1dc7034d、全weights/Adam/RNG/sampler/metricsはWSL保全。再launch/延長/FIM率・marker・span・horizon・seed・decoder救済をしない。独立学習/fullDEV/新TEST/採用0、4項目目標未達のままactive。次は別の根拠ある比較選定で、閉鎖を目標完了に読み替えない。以下の稼働記述は当時の観測。

[終端10000 CPU監査](../reports/phase6/fim-feasibility-20261015/checkpoint10000_CPU_audit.json)も完了。旧auditorは演算順の違いで5更新のLRに4.3368e-19差を出したが、[診断](../reports/phase6/fim-feasibility-20261015/LR_audit_expression_diagnosis.json)で実native scheduleと全10000ログの差0を確認。phaseを先に計算する正しい順へauditorのみ修理し、exact比較を緩めず全state/metrics auditを通した。科学sources/学習結果は変更していない。Codex非blind/既知DEV・未成熟fresh1seedの1条件で、FIM一般や10M容量限界の証明ではない。

稼働中の別CPU作業: [2000更新checkpoint監査](../reports/phase6/fim-feasibility-20261015/checkpoint2000_CPU_audit.json)で18836429教師・全更新実LR・FIM会計・finite native/Adam/clockの整合を確認。追加学習/GPU/品質評価0。将来のfixed diagnosticsは[入力export](../reports/phase6/fim-feasibility-20261015/Japanese_diagnostic_export.json)で保存済みDEV-only記録からsemantics192/JBLiMP331/JCQA1119の入力/選択肢/元gold labelのみを投影し、新reader13 CPU checks passed。予測・scores・creditを移さず、混在suite/TEST/元corpusを開かない。payloadはWSL data rootのみ、manifest SHA06fcf2c18f086ee57c4f615e5ae765f568024912148bf94be891b1581e7edadd。既知診断の隔離であり未知DEV/封印TEST/品質改善の証拠ではない。JBLiMPは既知public固定benchmarkのproject DEV-roleで、新しい排他的DEV splitを発見したとは記載しない。稼働中FIMのfrozen sources/条件/評価へ接続・変更していない。

**最新: fresh FIM pilotの科学学習が稼働中。** [起動観測](../reports/phase6/fim-feasibility-20261015/science_launch_observation.json)で実WSL PID1343/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start64143474、GPU lock/Windows worker34484を確認。観測675更新/6352596教師は途中値で完了値ではない。[凍結科学契約](../configs/phase6/base_fim_pilot_20261015.json) SHA c514ac4a944e7ca5974879585d902f0276a7ab544bf4ad9f226d971f48a61198はfresh native42/batch80/元2B schedule/TRAIN、10000更新/正確94160195教師、科学GPU2519秒/技術含む総上限3600秒。永続CLI・DEV256/隔離greedy80評価・notes/reviewerと13 CPU checksを完成。Python open監視でDEV評価allowlistを守り、旧混在Base/Japanese readerを呼ばない。初回Windows worker35328はUI停止直後のGPU解放待ち不足で科学開始前に安全停止し、原ログを保存。別v2 launcherが既知UI PIDだけ最大15秒待ち、凍結science sources/条件/予算を変更せず開始した。元UIは学習中だけ停止、終端でlauncherが元10Bを復帰する。現在の生存は再観測する。品質評価/全80内容review/資格/独立学習/fullDEV/新TEST/採用は未達。下の「科学0/未凍結」は開始前の履歴。

最新は[fresh FIM pilotの準備](../reports/phase6/fim-feasibility-20261015/protocol_readiness.json)。同native10M・元TRAIN・batch80/seed42/元2B schedule、既存fresh対照の10000更新/94160195教師を使う1条件を[prospective案](../reports/phase6/fim-feasibility-20261015/fresh_FIM_pilot_proposal.json)として選定。元抽出/quota maskの後に文書内PSMを適用し、marker labelsを-100、body+EOS<=512のcomplete unit以外は元ARの全窓を維持する。trainer/sampler16 CPU checks、probe workflow9 checks、実10M zero weights/Adam/schedule/training RNGと各2560行の元抽出・material RNG一致を確認。[専用CUDA結果](../reports/phase6/base-fim-probe-20261015/result.json)は40技術更新/383190教師、4対2+2全state/history一致、80x1024/32 timings、GPU9.153451952966861秒。pilot予測2519秒は提案総上限3600秒以内。**科学学習/品質評価0、科学契約未凍結**。永続science CLI・隔離DEV256/80評価・notes/reviewerがまだ必要。元UIは実PID520/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start63915576、HTTP元親/Tokenizer/10M/idleへ復帰確認。記録時の観測で、次起動前に再確認する。元model/frozen sources/閉じたrecipeは変更していない。

下の24文書監査と未選定メモは、このprospective選定前の証拠。CPU/CUDA準備を品質改善・独立学習・fullDEV・新TEST・採用に読み替えない。旧Japanese `build_tasks`もsemantic全行解析後のDEV filterと全manifest source hash読みがあるため、新しい安全なDEV経路へそのまま呼ばない。新TEST内容の確認は行っていない。[参考モデルの公開metadata](../reports/phase6/fim-feasibility-20261015/reference_model_metadata.json)はrevision74b3a173…でカードの会話3/40・長会話0/12を確認し、今回のBase基準達成例と扱わない。外部weights/Tokenizerの取得・実行・学習素材の移入なし。

次案調査で[FIMの固定24 TRAIN CPU監査](../reports/phase6/fim-feasibility-20261015/actual_TRAIN_serialization_audit.json)を完了。新serializerのCPU20 checks passed、既存accepted TRAINから各genre8文書を固定抽出し、元token/bytesとEOS identityを保存、全24がcontext1024内。原4096 codecでordinary markerは計35token、標本の元教師位置に対する追加入力26.2746%。新教材作成・元本文export・実model生成・科学学習・GPU・DEV/TEST読取り0。literal markerは原論文special sentinelと異なり、EOSは復元middleの終端になる。[選定メモ](../reports/phase6/fim-feasibility-20261015/selection_assessment.json)で成熟親100M FIMの自動開始を見送り、fresh比較の通常Baseへの転移根拠、marker教師/mask、長文処理、対照、horizonと実測予算を未確定として残す。新科学recipeは未選定で、独立学習/全文DEV/新TEST/採用も未達。CPU実装可能性を品質改善や全目標完了に読み替えない。

[評価分離修理147](147_evaluation_boundary_repair.md)でDEV専用manifest/readerと新生成/review境界を実装。CPU21 checks passed、既に保存したDEV80から入力のみをexportし実read-setを3ファイルに限定した。元混在suite/TESTは開いていない。生成答えの教材化0・実モデル評価/GPU0・品質改善の証拠0。旧frozen sources/事故/全結果は保全。次は既存証拠から新介入と対照/予算/必要CLIを定義し、隔離済み経路で比較する。独立学習/全文DEV/TESTは候補資格が成立してから。

[最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md) / [次の計画145](145_post_rejection_next_plan.md) / [今回更新146](146_documentation_followup.md)。

前の「6まで」は未達でblockedとなり、ユーザーが解除。その後の文書/計画目標は完了し、現在は別の「4まで」の再開目標。以前のblocked countや再開質問を新目標へ引き継がない。

最新の[文書長重み比較144](144_base_document_balance_results.md)は17,698更新・正確100M教師・全80理由付き内容・共通DEV256/Japanese192/331/1119・全state/元文書重み/対照全samplerとdigestを確認して**不採用で閉鎖**。文法44→23、一貫性2→1、適切完結2→2、EOS19→20、反復45→50（各80）。BPB0.998487→1.000710、一貫性差CI−3.75〜0ポイントで原品質・保持未達。

CPU21 checks、有限192 TRAIN診断、実CUDA47技術更新/273,521教師は別証拠。新GPUは科学1,474.808693＋技術8.721357＝1,483.530050秒、科学上限3,855/技術込み上限4,800以内。[数値監査](../reports/phase6/base-document-balance-comparison-20261014/numeric_completion_audit.json)、[全採否](../reports/phase6/base_document_balance_comparison_review.json)、[閉鎖・条件分岐](../reports/phase6/base_document_balance_comparison_completion.json)。

本比較延長・fresh独立学習seed43・fullDEV/400＋40・封印TEST・採用は有資格候補なしで未実行・passed=false・品質未確認。6段階すべての実施、Base完成とは記載しない。計画143/124の不合格時の報告停止条件でこの1比較を終了。追加の研究・学習を自動起動しない。

元Base TEST20 promptも既存greedy80がDEV抽出前にCPU構文解析していたことを確認。学習・GPU TEST採点0、TEST shard未開封だが、元TEST promptを未参照とは呼べない。[問題と訂正](../reports/phase6/base-document-balance-comparison-20261014/original_TEST_prompt_exposure.json)。将来の有資格Base最終確認は別artifactのDEV/TEST readerと新しい封印TESTが必要。今回は候補なしで代替TEST未準備・未採点。

科学PID337424/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start60325743は終了。元10B UIはPID338403/start60473641で復帰、HTTP元親/Tokenizer/10M/idleを確認。最新Base候補はWSL `reports/phase6/base-document-balance-comparison-20261014/document_balance/checkpoint-00017698.pt`、SHA `d89caf23bd7d2d8d81f298cb6f1fcbfe5fbd581105f91be1c3cfc18cefc9f86b`。重み・全sampler・全metricsはWSL保全。結果commit1901564/receipt fc1a3fc、93Git内容・40保全file・232local linksの納品照合は完了。元UI確認は当時の観測で現在保証ではない。

## 前回Chatの完了結果

[低学習率比較141](141_chat_lr_comparison_results.md)で、計画139の介入選定・同10M比較・有資格候補だけの独立確認への分岐を完了し、候補S1を不採用で閉鎖した。元10B親、同accepted TRAIN/Tokenizer/seed42/教師量/schedule/paddingでpeak LR1e-4→3e-5を比較。S0は138のS1の歴史state、新学習0。

| 項目 | 実際の証拠 |
|---|---|
| 固定参照 | native10,001,152 parameters、Tokenizer4096、context1024。9.5M〜10.1Mを維持 |
| 教材 | TRAIN41,529 target、660,109教師/周。280sample QAを再利用。新教材・新QA0 |
| S1学習 | 3,646更新・1,899,557 Assistant本文+EOT教師、許容内超過2。全3state・全update入力/label digest確認 |
| 全評価 | 28セット・6,132理由付き内容判断・共通NLL7点×2,634 target。既知12セット2,628判断は出典付き再利用 |
| 技術確認 | CUDA probe9＋連続/保存再開16の25検証更新。品質や本学習へ数えない |
| 資源 | 新GPU2,658.673158秒/33,600秒。過去の学習やCPUレビュー時間と別 |
| 保存 | 結果commit89275a8、納品commit09f338eの360ファイル保存・Git内容を確認。push/公開なし |

| 最終セット | S0内容 /80 | S1内容 /80 | S0自己文脈 /24 | S1自己文脈 /24 |
|---|---:|---:|---:|---:|
| 新DEV | 13 | 20 | 3 | 5 |
| 138 DEV | 19 | 18 | 3 | 5 |
| 133 DEV | 21 | 19 | 6 | 5 |
| 元旧DEV | 11 | 15 | 1 | 1 |

原条件は全セット内容56/80以上、自己生成文脈15/24以上など。新内容差+8.75ポイント、95%CI −1.25〜+18.75も改善条件未達。反復非退行・停止の条件も不成立、新自己生成Unicode失敗1を保存。低LRでDEV NLLが対照より低くても品質合格ではない。

[科学監査](../reports/phase7/chat-lr-20261014/completion.json)、[採否](../reports/phase7/chat-lr-20261014/selection.json)、[納品記録](../reports/phase7/chat-lr-20261014/final_delivery_checks.json)。

## 完了したことと未確認

前の「3まで進めてください」は比較・採否・条件分岐・報告・保全・ローカル納品まで完了した。Base保持、sampling、fresh学習seed43、人間blind、fullDEV、封印TEST、採用の7分岐は候補なしで未実行・passed=false・品質未確認。独立確認を実行した、モデルが完成したとは記載しない。

判断はCodex非blind、QAは標本、対照は歴史state。独立corpus監査・正式Base/Chat採用も未確認。Base単独原因・10M容量限界は確定していない。

元Chat TEST20行を準備時にCPU構文解析した事故を[141](141_chat_lr_comparison_results.md)へ保存。学習・GPU評価への使用0だが、未参照の主張は取り消した。将来の有資格Chat最終確認には新たな封印TESTが必要。元Base TESTは事故では解析していない。

## 次の判断と停止境界

[比較143/結果144](144_base_document_balance_results.md)は不採用で閉鎖。今回の文書・計画・保存検証を完了して通知する。次の研究の順序と終了範囲は計画145を正とし、再開は別の明示指示。原品質・10M・独立確認を維持し、閉じた条件の係数/seed/親/予算延長で救済しない。Chat・量子化・公開へ自動移行しない。Base/Chatと全体projectは未完成。

## UI・保存先・履歴

最後の納品観測2026-10-14T07:30:16Zは元10B UI PID338403/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start60473641、元親/Tokenizer/10M/idleを確認。現在の生存保証ではない。文書更新では再診断・再起動していない。

前回Chat S1はWSL `reports/phase7/chat-lr-20261014/S1/checkpoint-00003646.pt`、SHA `f7e8bb8b1569cb45ac399108455a66c5922f64d7898e8ab6b4931ba13c856018`。重み・samplerを含む全state・教材はWSL、Git正本はWindows。[引継ぎ](windows_handoff.md)。

Base結果[123](123_base_teacher_decay_2b_results.md)、教材汎化[136](136_chat_generalization_results.md)、意味多様性[138](138_chat_semantic_diversity_results.md)、最新LR[141](141_chat_lr_comparison_results.md)は別runの閉鎖済み証拠。元UI10B・別staged約10.6B・teacher-decay2B・後続SFTの学習量を合算しない。

[公開保存版126](126_model_archive.md)は2026-10-09の主要3系列保存で、dataset/samplerを除外。後続Chat重みは公開していない。当時のpush許可は当時の納品に限る。

旧運用全文と全311文書のhashは[更新前baseline](../reports/investigation/documentation-refresh-20261014/baseline.json)に保全。[全体125](125_project_retrospective.md)と[固定台帳](retrospective/README.md)は当時のrevisionを保持する。
