# JMicro-10M フェーズ別実行計画

2026-10-15ScaleGrad25Mは全件確認して不採用・閉鎖: reports/phase6/scalegrad-science-20261015/completion.json / review.json。正確25M/4420更新、全typed model/Adam/RNG/sampler状態・全履歴と既存nativeCE25Mの元stream/時計一致、全80 raw-bound個別notesを確認。対照→候補は文法44→71、一貫性1→7、適切完結3→9、EOS11→59、規定反復53→6、BPB0.9927168291→1.0194316807（2.691%悪化）。対応coherence差6/80・CI[.025,.1375]は元差8と絶対27に届かず、適切完結27・BPB保持・strong等も未達。表面反復フラグが減っても同義反復/矛盾/数量誤りが残り、EOSだけを成功としない。非blind Codexで独立人手評価ではない。科学517.844708秒＋全既消費3115.407930＝総3633.252637秒/元4800、技術累計169.245628/元180、残技術10.754372/総1166.747363秒。実450392/start68776772/同bootと元Windows worker39440/06:10:01.9998789Zは終了、元UI450807/start68828958/正しいidle HTTP/実FLOCKの復帰を再確認。Windows終了はPIDと開始時刻で判定し、継承共有handleのlogは観測bytesのsnapshotを保存。17小記録はWindows/WSL同hash、全weights/Adam/RNG/sampler/metricsはWSL保全。固定gamma/履歴/教師/親/seed/decoder/精度/形状/予約時間/予算の救済や旧job再実行なし。次のGPU比較は未選定・未凍結で、既存原結果から未回答仮説1件と残実測予算内の成立根拠が必要。Base本比較資格・独立fresh全pipeline seed43/fullDEV/全440/新封印TEST/採用と元4項目goalはactive/未達。

2026-10-15ScaleGrad25M科学学習を起動・実生存確認: reports/phase6/scalegrad-science-20261015/live_observation.json。実WSL450392/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start68776772、Windows worker39440、sole GPU peerと実kernel FLOCK owner同PID、全凍結source一致を確認。06:10:55Z観測で460更新/2,602,395教師/48.702058秒の途中値、品質未判定。元10B/fresh Adam、原25M/48/42/gamma.2、科学cap1406＋全既消費3115.407930を元総4800へ継承、500更新completed全state保存/20更新heartbeat。元UIはこの学習中のみ停止、同永続launcherが終端で元親へ復帰する。source/config/履歴定義を変更・再凍結・重複起動せず、同processの終端と元native25M全履歴/全stateの照合、隔離DEV/日本語/全80個別内容を判定する。真のsignal中断だけvalid completed checkpointと同残予算で復旧し、failed/completed条件の再launchやgamma/教師/decoder/予算の救済をしない。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用と元4項目goalはactive/未達、pilot完了もBase完成ではない。

2026-10-15ScaleGrad実機合格・25M科学契約を準備: reports/phase6/scalegrad-probe-20261015/completion.json。最大48x1024一回逆伝播/peak11,094,813,184bytes、native/既存25M零head対照の3更新元座標/Adam/RNG/stream一致、有効6対3+save3全state/historyと実6の元cache全7項目（最大1.8119812e-5）が合格。53技術更新/307311教師、GPU12.895588秒を全額継承し累計3115.407930秒（技術169.245628＋既科学2946.162302）。元全32計時の25M＋600秒予測1406秒を足して4521.407930秒で元4800以内。実449382/start68719537・Windows30248終了、元UI449444/start68721211/元idle HTTP/実FLOCKを復帰確認。専用科学runner/protocol/reviewer/永続launcherと35 CPU workflow checksを完成、configs/phase6/scalegrad_science_20261015.jsonを凍結・preflight済み（565bae138c130f103af4b07913304e15cf04e121748879df06b89d6517cb9b47）。既存nativeCE25Mの実型/全state/零headとAdam0を確認し、全履歴照合を必須化。本学習はまだ未開始、次は元10B/fresh Adamから新25Mをcap1406で実行し、隔離DEV256/全80内容/日本語と元全品質を判定。verification/対照endpointを初期化に使わず、旧条件やgamma/教師/精度/形状/decoder/予算を救済しない。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用と全4項目goalはactive/未達。

2026-10-15ScaleGrad専用GPU gateを凍結・起動前準備: reports/phase6/scalegrad-preparation-20261015/GPU_readiness.json。数学/学習器44＋scope34の78 CPU checks、元実10Mの119勾配証拠とsource/config/CPU receiptのpreflightが合格。専用probe/永続launcherを実装し、最大48x1024一回decoder逆伝播をAdam前に検証、native/既存25M零head対照3更新の元座標・Adam・RNG一致、有効6対3+save3全state/history、実6保存点から元cache全項目、全32計時で判断する。元UI実447775/start68603793/同boot・正しいidle HTTP/実FLOCK・唯一GPU peerを確認。現時点では新GPU/科学0、科学workflow/契約は未実装・未凍結。元累計3102.512341秒、元technical180の残り23.649960秒・総4800の残り1697.487659秒を保持し、25M＋600秒と全品質基準を救済変更しない。旧jobを再開せず、新型verification重みも科学初期化に使わない。独立fresh全pipeline/fullDEV/全440/新TEST/採用と4項目goalはactive/未達。

2026-10-15次案ScaleGrad型のCPU準備完了: reports/phase6/scalegrad-preparation-20261015/CPU_readiness.json。原notesの節/名詞/行為の循環を根拠に、原UL rollout/合成句確率減衰/一様confidence KL/label smoothing/二回RDropとの原source差を確認し、先行proposal後に固定gamma.2を選定。一次論文Eq4-6/公式commit b2685f9c8680e731316ca6149c1171fda7af5eadを確認、論文の困惑度悪化例と日本語10M未検証を記録。元同窓BODY入力prefix0..jだけの未出IDへlog(gamma)を足したhardCEを学習し、元CEは別metric・推論は元native。未来/別行/窓外履歴を使わず、公式flat target prefix/1e-8とは異なる明示variant、反復名詞やEOSへの影響も未解決。数学/独立全logit勾配/因果oracle25＋typed trainer19の44 CPU checks（disabled4全native/Adam/RNG/source一致、両6対3+save3全state/history一致、型/不正state/中断guard）が合格。元10M一回CPU2x64/0.374903秒でnative無効化の全119勾配が厳密一致max0、active全勾配有限かつ変更、元重み/CPU RNG不変・Adam0。既知128 body教師の新規85/既知43、親/既知technical payloadだけを読取、新corpus/DEV/TEST/GPU0。元model/Tokenizer/inference変更0、過去cache証拠を再利用し実学習6後cacheは次のown gateで確認。専用GPU probe/launcher/科学workflow/configはまだ未実装・未凍結、品質未確認。次は最大48x1024 FIRST、元学習/既存25M対照の実機一致、active6再開/実6cache/全32計時を実装する。累計3102.512341秒と残技術23.649960/総1697.487659秒、元25M＋評価保存600秒/全品質条件を保持し、旧条件再開やgamma/履歴/予算救済をしない。本比較資格・独立全pipeline seed43/fullDEV/全440/新封印TEST/採用と全4項目goalはactive/未達。

2026-10-15正解ラベルCPU一括転送の実機検証合格・科学学習前に予算で閉鎖: reports/phase6/rdrop-target-batch-probe-20261015/completion.json。最大48x1024二回グラフの有限逆伝播/peak22,573,591,552bytes、元native/既存25M対照3更新、元解析reference6との全数値状態/非時間履歴、両6保存点、保存再開、実6の元cache全7項目（最大1.8119812e-5）が合格。保存済み旧全32更新との非時間履歴も全件厳密一致。fresh CPU62 checksと既存数学/実native CPU証拠を利用し、59技術更新/341011教師、新GPU18.238786秒を全額継承。累計3102.512341秒（技術156.350040＋科学2946.162302）、新全32計時による固定25M＋600秒予測1757秒を足すと4859.512341秒で元4800秒を59.512341秒超え、科学/DEV/TEST0・品質未評価で別runtimeも閉鎖。48転送の単発cold profileは定常bottleneckや速度改善の根拠ではありません。残り元技術23.649960/総1697.487659秒、再計時/外れ値除外/教師・評価予約・精度・形状・親・seed・decoder・予算救済/旧job再開なし。実447710/start68601580とWindows31628終了、元UI447775/start68603793/元HTTP/実kernel FLOCKを復帰確認。全重み/Adam/RNG/samplerはWSL、小raw記録を同hash保全。次は既存原proposal/resultから未回答の同10M品質仮説を最大1件選び、根拠/対照/実測予算を事前定義する。無根拠なruntime最適化の連続実行はしない。本比較資格・独立fresh全pipeline seed43/fullDEV/全440/新封印TEST/採用と元4項目goalはactive/未達です。

2026-10-15正解ラベル一括転送の別runtimeを準備: reports/phase6/rdrop-target-batch-preparation-20261015/CPU_readiness.json。事前proposal後、元target列を-100で既存幅へCPU一括化し1回転送するhelperと専用typed trainerを作成。元ID packing/数式/係数/二回グラフ/精度/10,001,152/25M/評価予約600秒は保持。helper11＋trainer14の25 CPU checksで元解析trainer対両4更新の全数値/非時間履歴、両6対3+保存3、旧型load拒否/中断guardが合格。比較から除くのはkindとinput_runtimeラベルだけで、loss_runtime/重み/Adam/RNG/sampler/時計は比較。専用GPU scope37 checks、既存native数学/cache証拠を再利用し、新しい実10M CPU forwardは0。owned probe/launcher/configを凍結・preflight済み、新GPU/科学はまだ0。起動前元UI447017/start68566884/元HTTP/実FLOCK・唯一GPU peerを実確認。次は最大48x1024 FIRST、元学習/既存25M対照の実機一致、元解析reference6との全数値/履歴、再開/実6cache/全32計時で元180/4800予算を判定する。累計3084.273555秒を全額継承し、残技術41.888746/総1715.726445秒。旧条件/予測を再開せず品質改善は未確認、全4項目goalは未達。

2026-10-15入力転送の一回診断が完了・閉鎖: reports/phase6/rdrop-input-pack-profile-20261015/completion.json。保存6の厳密な次48窓（既存update7/6273教師/48x583）の抽出履歴・stream digest・source時計が一致。入力/正解/length/mask・CPU/CUDA RNG全6項目一致、モデル/forward/backward/Adam0。CPU profileで入力側_to_copy2（lengthとID）、正解側48を確認。同期込み単発計測は入力6.608ms/正解24.463msですが、計測負荷とcold影響を含み定常bottleneck/速度改善/科学予測には使いません。新GPU1.383377秒を全額継承し累計3084.273555秒（技術138.111254、残技術41.888746/総1715.726445）。実446962/start68566391とWindows31852は終了し、元UI447017/start68566884/元HTTP/実kernel FLOCKへ復帰確認。次は正解ラベルだけのCPU一括転送を別typed runtimeとして事前提案し、元全数値/履歴・再開/cacheと新全32計時を検証する。旧解析RDropは閉鎖のまま、全4項目goalと独立全pipeline/fullDEV/全440/新TEST/採用は未達。

2026-10-15入力転送の限定診断を準備: reports/phase6/rdrop-input-pack-preparation-20261015/CPU_readiness.json。元right_padは入力IDを既にCPUで一括化しており、未計測の候補は48行ごとのGPU正解ラベル生成/代入です。事前proposal、専用scope/launcher、25 CPU checksと元UI実446261/start68479313/HTTP/lockを確認。保存済み6更新目の厳密な次48窓（既存update7/6273教師/48x583）だけを一回、モデル/forward/backward/Adam0・最大5秒GPUでCPU演算profileする計画。現時点では新GPU/診断実行0、実バッチ復元も未実施。単発計測は定常bottleneck/速度向上/科学予測の証拠にしません。旧解析RDropの予算閉鎖と全3082.890178秒を保持し、独立fresh全pipeline/fullDEV/全440/新封印TEST/採用は未達です。

2026-10-15実機検証合格・科学学習前に予算で閉鎖: [解析勾配実装のGPU記録](../reports/phase6/rdrop-analytic-probe-20261015/completion.json)。最大48x1024の二回グラフ保持と有限な共同逆伝播が成功し、ピーク22,573,591,552bytes。元学習/既存25M対照の3更新一致、元実装との6更新の全数値状態/履歴の厳密一致、両6保存点、保存再開、実6の元cache全7項目（最大差1.8119812e-5）、全32計時まで確認しました。検証59更新/341011教師、追加18.341705秒を全額継承し累計3082.890178秒。しかし固定25M＋評価保存600秒の予測1754秒を足すと4836.890178秒となり、元4800秒を36.890178秒超えるため科学学習は開始しません。再計時・外れ値除外・評価予約削減・教師/形状/精度/親/seed/decoder/予算の救済や旧job再起動はしません。残り技術43.272123/総1717.109822秒、品質は未評価です。実446184/start68477053とWindows34056は終了し、元UI446261/start68479313/正しいidle HTTP/実kernel FLOCKの復帰を確認。次の別診断/比較はこの実測を根拠に範囲を事前定義し、単一の計測から定常速度や元予算の再予測を断定しません。本比較資格・独立fresh全pipeline/fullDEV/全440/新封印TEST/採用と元4項目goalはactive/未達です。以下は以前の記録です。

2026-10-15別実装のCPU検証: [R-Drop損失の保存量を減らす解析勾配実装](../reports/phase6/rdrop-analytic-preparation-20261015/CPU_readiness.json)を、前回の実測OOM箇所を根拠に事前提案してから実装しました。数式・係数・dropout・二回のdecoderグラフ・精度・形状・教師量は保持し、decoder再計算/checkpointing/chunking/microbatchは使いません。数式/勾配/保存量26項目と学習器13項目が合格し、元実装との4更新の全数値状態/履歴、両条件の全state保存再開が一致。実元親CPU一回0.796039秒でも全5損失値・二回の予測・乱数・全119パラメータ勾配が厳密一致（最大差0）、元重み不変・Adam0・通常/高速/cache推論を確認しました。32x4096のCPUで生存する保存済み密テンソルは8個/4MiB→2個/1MiBですが、GPUピーク・速度・日本語品質は未確認です。初回25pass/1failの保存量計測と原test sourceを保全し、一時的pack履歴から生存オブジェクトの計測へ修正。解析損失sourceと合格基準は変更していません。新GPU/科学/教材/DEV/TEST0、専用GPU検証/科学workflowは未実装です。次は最大48x1024を最初のAdam前に検証し、元実装・既存25M対照の実機一致、乱数を含む全state再開/実6cache/全32計時を確認します。累計3064.548473秒を元180/4800へ継承し残り技術61.613828/総1735.451527秒。旧OOM実行を再起動せず、元品質条件と本比較資格・独立全pipeline/fullDEV/全440/新封印TEST/採用までの4項目goalを維持します。以下は以前の記録です。

2026-10-15最新実機判断: [R-Dropの二回グラフ保持条件](../reports/phase6/rdrop-probe-20261015/completion.json)は、最初の最大48x1024検証で対称KLの差分テンソル384MiBを確保できず、重み更新前に閉鎖しました。割当ピーク22,976,241,664bytes（約21.40GiB）、二回のCE計算後で共同逆伝播は未完了、optimizer/科学学習0です。通常/既存25M対照の実機一致・GPU再開・実6cache・全32計時・日本語品質はいずれも未検証です。CPU79項目の成功を実機容量や品質の証拠とはしません。追加GPU1.444389秒を全額継承し、累計3064.548473秒、元180/4800の残り技術61.613828/総1735.451527秒。実445044/start68362424とWindows7020は終了し、元UI445117/start68362952/正しいidle HTTP/実kernel FLOCKの復帰を確認しました。失敗source/config/traceを保存し、同じ検証の再実行やcheckpointing・microbatch・係数・dropout箇所/率・教師・親・seed・decoder・精度・形状・予算の救済をしません。次の別条件は元報告・実装と照合して事前定義し、元の全検証と品質基準を維持します。方式全般の品質の無効性は示しておらず、直近の実品質結果は前回進行予測の不採用です。本比較資格・独立fresh全pipeline/fullDEV/全440/新封印TEST/採用まで元4項目goalはactive/未達です。以下は以前の記録です。

2026-10-15次案のCPU準備: [R-Drop型の二回予測の整合性学習](../reports/phase6/rdrop-preparation-20261015/CPU_readiness.json)を事前提案から実装し、独立数式/実Adam学習器39・起動境界6・既存対照との直接比較2の計47項目が合格しました。両予測に勾配を流す対称KLを加え、元論文の全損失を2で割って元CEの強度にそろえます。推論・学習とも10,001,152パラメータで追加重みはありません。実元親のCPU検証は一回0.538269秒で、元の通常/高速/cache出力・KVのbitwise一致、元cache全条件と有限な二回分の逆伝播を確認。起動時の文字列パスの不具合は親読取り前の失敗として原source/config/errorを保存し、Path修正と境界検証だけで対応しました。新GPU/科学/教材/DEV/TEST0で、専用GPU検証・科学workflowは未実装です。次は二回分の計算を保持した最大48x1024、元学習・旧25M対照の実機一致、乱数を含む全state再開、実6cache、全32計時と予算を検証します。既消費3063.104084秒を元180/4800へ全額継承し、残り技術63.058218/総1736.895916秒。旧dropout/進行予測の条件を再試行せず、品質成功やKL単独の効果は未確認です。本比較資格・独立fresh全pipeline/fullDEV/全440/新封印TEST/採用まで元4項目goalは未達です。以下は以前の記録です。

2026-10-15最新結果: [文章の残り割合を補助予測する各25M比較](../reports/phase6/document-progress-science-20261015/completion.json)は、両条件4,420更新・正確25M、全数値状態/全履歴/同教師列と生成160件の個別内容確認まで完了し、不採用で閉鎖しました。対照→候補は文法44→46、一貫性1→1、適切完結3→1、EOS11→10、反復53→50、BPB0.992717→0.993464、対応CI[0,0]で、元品質条件は未達です。非blind Codexレビューで独立人手評価ではありません。実442192/start68129284とWindows34612は終了し、元10B WebUI443138/start68226666/正しいidle HTTP/実kernel FLOCKの復帰を確認。今回科学969.744771秒を含む累計3063.104084秒を元180/4800へ全額継承し、残り技術63.058218/総1736.895916秒です。固定した進行target・分母・head・係数・教師・親・seed・decoder・精度・形状・予算を救済せず、次は過去の原proposal/resultから異なる根拠ある未回答仮説を1件選びます。今回だけで進行予測全般の無効性や一意の原因は断定しません。本比較資格・独立fresh全pipeline/fullDEV/全440/新封印TEST/採用は有資格候補なしで未実施、元4項目goalはactive/未達です。以下の実行中・準備記録は当時の履歴です。

2026-10-15各25Mの対照比較が進行中: [実生存と凍結sourceの確認](../reports/phase6/document-progress-science-20261015/live_observation.json)。実442192/start68129284/同boot・Windows34612、唯一のGPU process/実kernel FLOCKを確認。現在native_CE_controlの600更新/3394390教師は途中経過で品質証拠ではない。新規対照/候補各25M、推論10,001,152/学習10,001,408、元親/48/42を固定し、各科学1396/1089秒＋全既消費2093.359313秒を元4800以内で継承する。500更新全state保存/20heartbeat、元UIは同job終端に永続launcherが復帰する。次は同じ実processの終端と全数値状態/全履歴/同教師列・全160件の個別内容採否を確認。凍結source編集・再起動・教師/係数/decoder/precision/形状/親/seed/予算救済なし。本比較資格・独立fresh全pipeline/fullDEV/全440/新封印TEST/採用と全4項目goalはactive/未達。以下は以前の観測。

2026-10-15実機検証合格: [document-progress専用GPU記録](../reports/phase6/document-progress-probe-20261015/completion.json)。両条件の最大48x1024をAdam前に検証、通常学習3更新の元重み/Adam/CE/source/RNG一致、両条件6対3+保存3の全state/history、実6の元FP32 cache全7項目、各全32計時が合格。新18.468181秒・技術累計116.941782秒、既科学込み総2093.359313秒。新規対照/候補各25Mの予測1396＋1089秒を足して4578.359313秒で元4800以内。専用科学workflow28 CPU checksと凍結configを準備済みで本学習は未開始。実441218/start68095927とWindows38116の終了、元UI441412/start68098170/正しいidle HTTP/kernel FLOCKを確認。次は凍結した各25Mを元親から新規学習し、全数値状態/履歴/同教師列と計160件の個別内容を検証する。全元品質条件を保持し、pilotだけで資格/完成とはしない。本比較・独立fresh全pipeline seed43/fullDEV/全440/新封印TEST/採用と元4項目goalは未達。以下は履歴。

2026-10-15次工程: [document-progress CPU準備](../reports/phase6/document-progress-preparation-20261015/CPU_readiness.json)44 checksを確認済み。専用GPU検証/launcherを実装→最大48x1024有限backwardをAdam前に確認→通常学習3更新の一致→両条件の全state保存再開・実6cache・各全32計時→全既消費込み元予算判定→成立時だけ新規対照/候補各25Mと各80件個別review。仮説は原CEを保持する学習時だけの残文書割合scalar L1で、推論10,001,152/学習10,001,408。教師予算を変更した閉鎖100Mの再試行ではなく事前定義した別目的pilotで、cached100Mを同25M対照にしない。元品質条件はすべて維持。残technical81.526398/総2725.108868秒、両forecastは各600秒の評価保存込み。pilot後も本比較の資格、独立fresh全pipeline seed43、fullDEV/全440、新封印TESTと採用が必要で全4項目goalは未達。以下は履歴。

2026-10-15最新判断: [self-rescaled RMS CPU条件](../reports/phase6/self-rescaled-norm-preparation-20261015/CPU_closeout.json)は実装前proposal・独立数式19/専用model22 checksと実数10,014,976まで確認したが、実元親の手動active beta=.01で元full/cache複合精度条件に不合格（max8.05854797e-5）。初期native出力・原tensor/tie/RNG・active K/V/metadataは合格でも科学資格にはならず、固定runtimeをtrainer/GPU前に閉じた。方式全般の品質無効性や一意の数値原因は示していない。

新GPU0で元予算の残81.526398/2725.108868秒を保持。beta/alpha/箇所/activation/grouping/epsilon/precision/親/seed/教師/decoder/形状/予算の救済や自動localizationをせず、原proposal/resultと一次資料から別の根拠ある未回答仮説を選ぶ。負の既存診断を原因に転用せず、CPU小fixtureの成功を実親精度や品質の代替にしない。全元品質条件と独立fresh全pipeline/fullDEV/全440/新TEST/採用の到達範囲を維持し、全4項目goalはactive/未達。以下は履歴。

2026-10-15最新判断: [固定ゼロK/V owned](../reports/phase6/quiet-attention-probe-20261015/completion.json)は実機容量・disabled/native3・全state保存再開・実6cache全7項目を通過したが、全32計時の科学3756秒と累計2074.891132秒を合わせると元4800秒超過で科学前に閉鎖。数値成功と予算資格、文章品質を分ける。この方式の日本語品質は未評価で、採用候補には進めない。

元技術180/総4800を維持し、既完了scienceも含む残総2725.108868秒を次判断へ継承する。warm再測定・計時除外・phantom/learned sink/親/seed/教師/precision/geometry/decoder/予算の救済なし。次は原proposal/resultから別の未回答仮説1件を根拠と対照付きで選定し、残予算内の実測資格を先に確認する。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用は有資格レシピなしで未実施、全4項目goalはactive/未達。実job/Windows worker終了と元UI復帰は終了receiptに保存。以下の未実装・CPUのみは準備時点の履歴。

2026-10-15次の準備: [固定ゼロK/V attention](../reports/phase6/quiet-attention-preparation-20261015/CPU_readiness.json)は原10,001,152パラメータと原重みを保持し、正規化の中へゼロの選択肢を追加する別仮説。CPU model37/trainer18と実親cache精度、両arm全state保存再開、disabled-native元Adam/stream一致まで完了。有効化時の初期関数は変わる。論文の別10M loss結果やCPU成功を日本語品質の証明にしない。

直近は専用owned CUDA probe/launcherとCPU scope checksの実装が必要で、まだ新GPU0。元最大48x1024の有限backwardをAdam前に確認し、disabled/native3、enabled6対3+save3全state/history、実6保存と元FP32 cache全subcheck、全32計時で資格を判定する。今回の完了科学も含む累計2063.031660秒を元総4800秒へ継承し、残2736.968340秒で固定100M＋評価保存の見積もりが成立しなければ閉じる。新しい予算・教師数・精度・phantom数/値/位置・learned sink等で救済しない。科学runner/evaluator/reviewerの契約は未完成・未凍結であり、CPU準備を比較完了にしない。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用と全4項目goalはactive/未達。

2026-10-15現在: [independent rank8 QK 100M](../reports/phase6/independent-map-science-20261015/completion.json)は全数値状態/全履歴/元CE対照streamと全80個別内容を確認し、**不採用で閉鎖**。文法44→59でも一貫性2→1・適切完結2→2・EOS19→19・反復45→48・BPB0.998487→0.998526で、元の全品質条件は未達。新52tensorの学習活動や技術成功は品質の証明にしない。

次の順序は、既存原proposal/resultから異なる未回答仮説1件を選ぶ→対照/10M/元全品質条件/実測予算を事前固定して必要な実装と技術検証→有資格比較ができた場合のみ真にfreshな全pipeline独立seed43→fullDEVと400生成＋長文40→新封印TESTと採用。現在は有資格レシピがなく後半未実施。固定rank/分岐/親/seed/normalization/decoder/教師/形状/予算の救済、旧job再実行、大型化・品質基準低下で進めない。元4項目goalはactive/未達を維持し、比較終了や文書保存へ縮小しない。

実science435642とWindows11280は終了、科学1976.417531＋継承済み技術86.614129＝2063.031660秒で元総4800秒内。元UI437167/start67703206/同boot・正しいHTTP情報/idle/実kernel FLOCKを復帰確認。以下の稼働中・50%・準備のみは日付付き履歴。

2026-10-15現在: **independent rank8 QK 100M科学比較が稼働中**。[50%通過の実process＋kernel lock観測](../reports/phase6/independent-map-preparation-20261015/science_observation_50pct.json)はPID435642/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start67505127、Windows worker11280と同kernel FLOCK ownerを確認。9460更新/53,519,125教師/1024.229221秒（50%通過、保存metadataは9000更新）は途中値で、文章品質は未判定。[科学契約](../configs/phase6/independent_map_science_20261015.json) SHA5791ebfbe40ff3a3967639db023066a68cfd0f85d1f44941b7d5fc408449cdd1は元10B親/fresh AdamW/原CE100M/48/42、native10,001,152対新rank8 Q2/K2座標66,612追加10,067,764を明記。同一architectureや厳密同parameter数とは呼ばず、全元品質gateを維持する。

[owned gate完了](../reports/phase6/independent-map-probe-20261015/completion.json)は実435092/start67467767終了・Windows38264終了、50技術更新、原関数/disabled3の全旧weights・Adam・CE・stream exact、新52tensor全活動、全state6対3+save3、最大48x1024と実6のFP32cache全subcheckを通過。新14.050476＋旧72.563653＝技術累計86.614129秒を元technical180/総4800へ継承し、実測科学4461秒で総上限内。科学workflow25 CPU checksも合格。検証重みは科学へ使わず、500更新全state保存/20更新heartbeat、元UIは実験中だけ停止し永続launcherが終端復帰する。

次は同じlive processを観測し、100M終端の全state/全history・原対照stream＋宣言した追加座標と全80 rawの個別内容を確認する。凍結source編集/条件救済/二重起動をせず、真のsignal中断だけvalid completed checkpoint/閉じた残予算で復旧する。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用は資格前で未実施、全4項目goalはactive/未達。以下は履歴。


2026-10-15次の独立比較準備: [independent rank8 QK proposal/CPU](../reports/phase6/independent-map-preparation-20261015/CPU_readiness.json)。閉鎖cross-GQAは既存Q/Kのhead置換、headwise gateは出力scalar、ContextMixingはgreedy入力置換であったと原source/resultを照合した。新案は各層に共有down(rank8)＋独立Q2/K2 upを学ぶ新座標を追加し、元Vに対する二つ目の注意分布をtanh(raw)で差し引く。原論文の再現ではなく、NoQKNorm/RoPE/元Q/K/V/O/全backboneを保持した別architecture提案。raw0で元関数を保存し、実count10,067,764（追加66,612）は元9.5M〜10.1M内。元native10,001,152と厳密同parameter数とは呼ばない。

model27/trainer18/probe19 CPU checksは独立dense oracleの全勾配、旧map/出力scaleで得られない反例、real K2 cache/holes/allPAD/過去再計算なし、両arm全state6対3+save3、disabled対native全旧weights/Adam/source/CE一致と新投影全勾配を確認。実元10M親CPU0.377899秒で全旧weights/初期logits/cacheがbitwise一致し、raw.25のactive cacheも元3e-5/2e-5内。科学の対照は元CE100M cachedで、実CUDA原関数/disabled/stream資格を先に確認する。閉鎖forgettingは初期関数が変わるため両新arm必須だったが、新案へその弱いstatic対照を流用しない。全絶対/native/strong/historical/最終品質条件は維持する。

新owned gate/config/永続launcherはCPU preflight合格・新GPU0。元48x1024容量をAdam前に検査し、disabled/native3・新52tensor活動・実6 snapshotと全cache subcheck・全state resume/各32timingsで資格判断。既消費72.56365345604718秒を元technical180/総4800へ継承し、rank/分岐/親/係数/教師/decoder/形状/予算救済をしない。科学/独立fresh全pipeline/fullDEV/全440/新TEST/採用と全4項目goalはactive/未達。以下は履歴。


2026-10-15最新限定診断完了: [single operator profile](../reports/phase6/forgetting-attention-operation-profile-20261015/completion.json)は実saved6＋既存48x1024だけのforward/backward1回、optimizer/新TRAIN/DEV/TEST/重み保存0、全勾配有限・重み不変・RNG保持を確認。実434159/start67316608・Windows30428終了、ledger closed。新2.514122＋旧70.049531＝累計72.563653秒を元technical180/総4800へ継承、残り107.436347/4727.436347。元UI434223/start67317300/同boot・HTTP元親/Tokenizer/10M/idleへ復帰実確認。

元collectorのCUDA-event集計には自分のrecord_function範囲1件959578.843usとmemory activityも含まれる。[保存済み結果のoffline解析](../reports/phase6/forgetting-attention-operation-profile-20261015/analysis.json)で既知名称を分け、元総数/総時間との一致を確認した。kernel名activity3065件133467.593usは名称分類で、元scope metadataは未保存。raw3184件1096151.319usをkernel計算時間と呼ばず、包含時間や初回module loading/計測器の時間から定常速度・固有の根因・科学予算を推定しない。collector/sourceは変更せずGPU再計測0。

これ以上の微調整をGPUへ進める根拠は今回の単発計測だけでは不足。[次比較の既存資料audit](../reports/phase6/forgetting-attention-operation-profile-20261015/next_comparison_audit.json)はstrong source-orderが既存の別historical親/継承Adam・LR/4stream/順序比較であると確認し、単なる親切替による閉鎖条件の救済を除外した。次は原proposal/resultから異なる未回答仮説を1件に絞って対照・全gate・実測予算を定義する。新条件は未選定、科学/独立fresh全pipeline/fullDEV/全440/新TEST/採用と全4項目goalはactive/未達。以下は履歴。


2026-10-15最新終端: [shared-RoPE owned completion](../reports/phase6/forgetting-attention-shared-rope-probe-20261015/completion.json)は両armのaccepted prefetch3/6/38全数値state・全32非時間historyがexact、初期/最初CE・6対3+save3・実6 FP32cache全subcheck差0・最大48x1024を通過。しかし両科学100M＋各評価600秒予測6475秒は元4800を超え、科学0で条件閉鎖。旧6168から速度改善したとは言えない。新18.874430＋旧51.175102＝累計70.049531秒を元technical180/総4800へ全額継承。実433547/start67284552・Windows35640終了、ledger closed、元UI433631/start67286859/同boot・HTTP元親/Tokenizer/10M/idleへ復帰実確認。

次の[一回限定operator profile準備](../reports/phase6/forgetting-attention-operation-profile-preparation-20261015/CPU_readiness.json)はCPU6 checks/preflight合格、新GPU0。saved actual6と既存48x1024技術windowだけで元BF16 forward/backwardを1回計測し、optimizer/新TRAIN/DEV/TEST/重み保存0。CPU operatorと実CUDA eventを分離し、包含時間の二重加算や計測器付き時間の科学予測への転用を拒否する。新上限30秒かつ元180/4800へ累計70.049531秒を継承。旧probeのwarm再計時/救済変更をせず、観測後にだけ次の実装価値を判断する。科学/独立全pipeline/fullDEV/全440/新TEST/採用と全4項目goalはactive/未達。以下は履歴。


2026-10-15新runtime準備: [shared-RoPE CPU runtime](../reports/phase6/forgetting-attention-shared-rope-preparation-20261015/CPU_runtime_readiness.json)は同inv/phase/cos/sin/castを一呼出し内だけ共有する別model/cache/trainer kind/spec/lineageを実装。元BF16演算・vendor kernel/FP32 canonical推論/real cache/同10,014,516/入力/予算/品質条件を維持し旧state/cacheを拒否。CPU model/trainer43・probe29（既存数学12再利用）、実元10M親0.617724秒・旧weights/両arm初期logits exact・cache差1.239777e-5で元3e-5/2e-5内。初回42pass/1failのpolicyコピー不具合をGPU前に修理し、元XMLとpolicy不変guardを保持。CPUの全6対3+save3と同期prefetch対全数値state/非時間history exactはCUDA shared-tableの証明ではない。

専用新owned gateはaccepted prefetch3/6/38・全32非時間historyと実6 snapshot/cache全subcheckを保持し、両arm初期/最初CE・全state resume・最大48x1024・各32timingsを元基準で判定する。新GPU0・preflight合格の準備記録、既消費51.175101520027965秒を元technical180/総4800へ全額継承。旧probe再launch/warm再計時/閾値/教師/形状/予算救済をしない。科学/独立全pipeline/fullDEV/全440/新TEST/採用と全4項目goalはactive/未達。以下は履歴。


2026-10-15最新終端: [prefetch owned completion](../reports/phase6/forgetting-attention-prefetch-probe-20261015/completion.json)は両armのaccepted canonical3/6/38全数値state・全32非時間historyがexact、全state6対3+save3・実6 FP32cache全subcheck差0・最大48x1024・初期一致を通過。待ち時間は各平均約47usだが、両科学100M＋各評価600秒予測6168秒が元4800を超え、科学0で条件閉鎖。新17.898267＋旧33.276834＝累計51.175102秒を元technical180/総4800へ全額継承（残り128.824898/4748.824898）。実249980/start67232241・Windows39404終了、ledger closed、元UI250064/start67234446/同boot・HTTP元親/Tokenizer/10M/idleへ復帰を実確認。旧条件をwarm再計時/outlier除外/教師削減/閾値/形状/予算拡大で救済しない。既存cache/OS状態もあるため速度差の単独因果効果とは呼ばない。

次の[共有RoPE定数案](../reports/phase6/forgetting-attention-shared-rope-preparation-20261015/CPU_readiness.json)は先行proposalと純粋helperを別保存。元model.ropeの同じinv/phase/cos/sin/キャスト順序を共有し、FP32/BF16・長さ1/7/64/65/1024・不規則positions・Q/K全入力勾配がCPU12 checksでexact。helperのみで新model/cache/trainer/owned gateは未実装、CUDA/速度/品質の証拠ではない。次は別typed runtime/全state接続後にaccepted3/6/38・全32非時間history・元cache/容量/予算を検証する。新GPU0、累計51.175102秒を保持。独立fresh全pipeline/fullDEV/全440/新TEST/採用と全4項目goalはactive/未達。以下は履歴。


2026-10-15最新終端: [canonical owned completion](../reports/phase6/forgetting-attention-canonical-probe-20261015/completion.json)は両armのCUDA初期状態/最初CE、旧saved3の全数値state、各6対3+save3、実6のFP32 cache全subcheck（差0）、最大48x1024/peak11.023GB、各32timingsを通過。ただし両科学100M＋各評価600秒の予測8137秒が元総4800を超え、科学0で条件閉鎖。新19.509915＋旧13.766920＝累計33.276834秒を元technical180/総4800へ全額継承。実66184/start67186372・Windows18832終了、ledger closed、元UI66278/start67188762/同boot・HTTP元親/Tokenizer/10M/idleへ復帰確認。旧失敗6の原因確定や品質改善とは呼ばない。

次の[CPU staging/prefetch準備](../reports/phase6/forgetting-attention-prefetch-preparation-20261015/CPU_readiness.json)は先行proposal後、同じ入力/ラベルをCPUでまとめ2転送にし、元TRAINを最大1batchだけ先読みする別trainer。checkpointは消費済みlogical samplerだけで、先読みによる欠落/重複/未来cursorを拒否。CPU loader9/trainer31/probe29と両arm同期canonicalとの全数値state/全非時間history一致、全6対3+save3 exact。初回CPU preflightのPath型エラーはsource/config/失敗記録を残して修理、新CUDA/科学0。次は新ownedでaccepted canonical3/6/38・全32非時間historyとGPU数値/cache/速度を比較し、全消費33.276834秒を継承する。旧条件をwarm再計時・outlier除外・教師/形状/閾値/予算変更で救済しない。独立全pipeline/fullDEV/全440/新TEST/採用と全4項目goalはactive/未達。以下は履歴。


2026-10-15最新準備: [canonical FP32 readiness](../reports/phase6/forgetting-attention-canonical-preparation-20261015/CPU_readiness.json)は別proposal後に固定64行pointwise/Q64・元context長K workspaceのFP32/MATH実装を追加。実cacheは実tokenのKV/logs/validity/positionsだけを保持し、過去decoder再計算なし。新runtime/model/cache/trainer kind/spec/lineageで旧stateを拒否、元BF16 tiled学習経路/13,364 gate座標/元品質条件は維持。CPU model23/trainer27/probe24、実元10M親0.589500秒/count10,014,516・旧weights/両arm初期logits exact、cache差1.239777e-5で元atol3e-5/rtol2e-5内。GPU preflightのみ合格、科学未資格。

先行[read-only CUDA saved3完了](../reports/phase6/forgetting-attention-fused-cache-diagnostic-20261015/completion.json)は元全subcheck合格、max5.531311e-5・複合許容範囲外0。これは失敗した旧CUDA6の再現/原因確定/修理証拠ではない。新0.885824＋既消費12.881096＝累計13.766920秒を元technical180/総4800へ全額継承。次の新owned gateは旧saved3とのBF16全数値比較、両arm実6snapshot・全cache subcheck保存、全state resume/最大48x1024/各32timingsを検証する。旧probe/診断を再launch・閾値/初期化/形状/予算を救済しない。独立fresh全pipeline/fullDEV/全440/新TEST/採用と全4項目goalはactive/未達。以下の診断準備等は履歴。


2026-10-15最新終端: [tiled owned gate](../reports/phase6/forgetting-attention-fused-probe-20261015/completion.json)は独立BF16値/全勾配・resident48x1024 full backward（peak11.023GB）・learned全state/history resumeを通過後、update6 FP32 cache guardで失敗し閉鎖。subcheck/max値未保存を推測せず、static/32timings/科学未実施を保持する。新11.636436＋旧1.244660＝累計12.881096秒、技術12更新/67400教師のみ。CPU saved3は元cache基準内だが別endpoint。次は別read-only CUDA saved3診断、旧学習/源条件を再実行・救済しない。元180/4800全額継承、独立全pipeline/fullDEV/全440/新TEST/採用と全4項目goalは未達。

2026-10-15別[author tiled runtime準備](../reports/phase6/forgetting-attention-fused-preparation-20261015/CPU_readiness.json)は依存変更0・26/24/22 CPU checksと実親FP32cache合格。新owned gateは独立BF16値/全勾配→最大48x1024→両arm初期一致/全state resume/active cache/各32timingsを検証する。既消費1.244660秒を元technical180/総4800へ継承し、両科学100Mと各600秒評価reserveを含む実測資格前に科学へ進まない。新GPU0の準備記録、独立全pipeline/fullDEV/全440/新TEST/採用と全4項目goalは未達。

2026-10-15最新判断: [key-bias owned GPU](../reports/phase6/forgetting-attention-key-bias-probe-20261015/completion.json)はcapacity FIRST48x1024のOOMで閉鎖。GPU1.244660秒、学習更新0、CUDA resume/cache/timing/科学未実施、元UI実63743/start66877161へ復帰確認。元technical180/総4800へ全額継承し、形状/allocator/backend等で現契約を救済しない。次は[公式タイル化kernelの一次source assessment](../reports/phase6/forgetting-attention-key-bias-preparation-20261015/fused_kernel_assessment.json)から別実装proposal/勾配・runtime/cache・license/依存条件を判断する。導入/追加GPU0、独立全pipeline/fullDEV/全440/新TEST/採用と全4項目goal未達。

2026-10-15別runtimeの[CPU readiness](../reports/phase6/forgetting-attention-key-bias-preparation-20261015/CPU_readiness.json)はmodel17/trainer23/probe16・両arm全state resumeと実元親cache精度を通過。softmax行定数を省く同数式で元FP32/初期化/10M/品質を維持し旧実装は保存。次は専用owned180秒CUDAで48x1024 resident capacityを最初に確認し、通過時だけ両armのresume/cache/32timings・総4800内を実測する。新GPU0/科学未凍結の準備記録で、独立全pipeline/fullDEV/全440/新TEST/採用と全4項目goalは未達。

2026-10-15対象限定CPU診断は[完了](../reports/phase6/forgetting-attention-preparation-20261015/CPU_cache_layer_localization.json)。元nativeは同cache基準内、forgetting referenceは未達、非exactの出始めは双方共通で原因を断定できない。完了診断を反復せず、次は別の同数式安定実装の価値を判断する。閾値/初期化/親/decoder/予算を変更せず、実親cache・勾配・typed stateの資格前に科学/GPUを開始しない。独立全pipeline/fullDEV/全440/新TEST/採用と全4項目goalはactive/未達。

2026-10-15最新CPU判断: [forgetting attention model/trainer closeout](../reports/phase6/forgetting-attention-preparation-20261015/CPU_model_trainer_closeout.json)で実count10,014,516、両arm初期関数一致・元weights保持、model14/trainer19 checks（両arm全state/history resume含む）はpassed。ただし実元親full/chunk差0.0001010895が元3e-5/2e-5を超えreference実装閉鎖、科学/GPU0。synthetic成功を代替にせず、次は同accepted technical spanで数値差を局在化する。元cache閾値/10M/品質/対照/実測予算を維持し、別実装の資格確認前にGPUを起動しない。独立fresh全pipeline/fullDEV/全440/新TEST/採用と全4項目goalは未達。以下の数学のみ/未実装は履歴。

2026-10-15次の準備: [forgetting-attention proposal](../reports/phase6/forgetting-attention-preparation-20261015/proposal.json)は正規化前の累積decayのCPU数学だけを選び、[7 checks](../reports/phase6/forgetting-attention-preparation-20261015/CPU_math.json)を完了した。実model/count/cache/trainerは未実装で、新GPU学習0。有限sigmoid gateはnative初期関数を変えるためfresh対照かmatched conversionかを先に解決し、元10M/品質条件・own technical180/総4800提案内の実測を要する。旧next-two/recurrentは原記録から既閉鎖と判断し再実行しない。資格候補後の独立全pipeline/fullDEV/全440/新TEST/採用を省略しない。

2026-10-15最新終端: [causal-QKV contiguous100M](../reports/phase6/causal-qkv-contiguous-science-20261015/completion.json)は正確100M/全17,698更新state/history/原CE対照＋宣言lag差・全80内容を確認し不採用。文法61/80・BPB0.998450に対し一貫性1/80・適切完結1/80・EOS21/80・反復47/80で元品質未達。科学1889.042532＋累計技術34.850105＝1923.892637秒、元UI実PID60818/start66693747へ復帰確認。固定条件を延長・再launch・係数等で救済しない。次は原結果から重複しない根拠ある同10M比較を選定する。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用は候補資格なしで未実施、全4項目goalはactive/未達。以下の進行中等は履歴。

2026-10-15最新実行: [causal-QKV contiguous100M](../configs/phase6/causal_qkv_contiguous_science_20261015.json)を新owned CUDA後に凍結・起動。実PID58473/start66504429・worker35512、240更新/1355486教師の途中を確認。同verification保存点から3更新のreference対contiguous全state/history、保存済みreference0/3/38と32非時間metricsがexact、新runtime自身の全state resumeもexact。旧19.769017＋新15.081088＝累計技術34.850105秒を元technical180/総4800へ継承し、科学予測4291秒で資格を得た。元親/原TRAIN100M/48/42・候補10,014,464/全元quality gates維持、科学workflow22 CPU checks・500保存/20heartbeat。次は同job終端の原対照/全80採否。独立fresh全pipeline/fullDEV/全440/新TEST/採用と4項目goal未達。以下のGPU-pending等は当時の履歴。

2026-10-15最新技術: [causal-QKV参考実装](../reports/phase6/causal-qkv-probe-20261015/completion.json)はmodel24/trainer12/実親CPU parity/probe10とowned CUDA全state/history resume・48x1024・raw cache一致を通過したが、技術19.769017秒に対する科学予測8581秒が元総4800秒を超え、科学0でreference条件を閉鎖。次の[同数式contiguous別実装CPU11項目](../reports/phase6/causal-qkv-contiguous-preparation-20261015/CPU_equivalence.json)は共有joined tensorで値/全勾配/3更新Adam exact、masked/cache経路はreferenceを保持。初回6pass/5failを保存し閾値を緩めていない。GPU同値性・速度は未検証。次は新しい別CUDA実装比較と実測で、元技術180秒の残り160.230983秒・総4800秒を維持。reference再launch・教師削減・tap/予算救済をしない。独立fresh全pipeline/fullDEV/全440/新TEST/採用と4項目goalは未達。

2026-10-15最新終端: [first-layer value residual100M](../reports/phase6/value-residual-science-20261015/completion.json)は全17,698更新state/原CE対照＋宣言した12scalar差・全80個別内容まで確認し不採用。文法44→58、EOS19→23に対し一貫性2→1・適切完結2→1・反復45→47・BPB0.998487→0.998524・CI[-.0375,0]で元gate未達。科学1504.763362＋技術9.812882秒、元UI実PID54129/start66299802へ復帰確認。次は別の根拠ある同10M比較1件の選定。固定V0係数/層subset/normalization/親/seed/decoder/予算の救済をしない。独立fresh全pipeline/fullDEV/全440/新TEST/採用と4項目goalは未達。以下のrunning等は当時の履歴。

2026-10-15最新実行: [first-layer value residual100M](../configs/phase6/value_residual_science_20261015.json)を凍結・起動。実PID52873/start66148908・worker23232・40更新/233183教師を確認。元base config/weights/初期関数と元CE全streamを保持し、12scalar/10,001,164の宣言済み構造差のみ。実親CPU parity差0/model21/trainer12/probe10/科学18 checks、owned CUDA9.812882秒・全state/history resume exact・48x1024有限gradient/peak10768065024bytesを確認。科学上限3568秒/技術含む4800秒、元全品質gate不変。次は同jobの終端・原対照照合・全80個別採否。独立fresh全pipeline/fullDEV/全440/新TEST/採用と全4項目goalは未達。下のCPU-pending等は当時の履歴。

2026-10-15次案CPU準備: [first-layer V shortcut](../reports/phase6/value-residual-preparation-20261015/CPU_preparation.json)は先行proposal後に別modelを実装。追加12scalarの10,001,164、元Q/K/map/RoPE/O/逐次blockを保持し、最初のVを後段Vへ零係数から加える。model18＋追加learned-clip1 CPU checks passed、static norm reductionの初回失敗も保存してexact修理。実元親parity/専用trainer/全state resume/owned GPU/科学契約は未完で、元native hidden helperは経路省略を明示拒否する。次は実元親の限定CPU parityと専用trainer。新data/DEV/TEST/GPU/科学学習0、最終4項目の品質は未達。

2026-10-15最新終端: [cross-GQA signed-map100M](../reports/phase6/cross-gqa-map-science-20261015/completion.json)は全17,698更新のstate/元CE対照と宣言した構造差・全80個別内容まで確認し、不採用で閉鎖。文法44→60だが一貫性2→2・適切完結2→2・EOS19→18・反復45→47・BPB0.998487→0.998503・CI[0,0]で原gate未達。科学1673.349337＋技術10.287119秒、元UI実PID50207/start66037939へ復帰確認。次は別の根拠ある同10M比較1件の選定。固定map/係数/normalization/親/seed/decoder/予算の救済をしない。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用と4項目goalは未達。以下のrunning記述は当時の履歴。

2026-10-15最新実行: [cross-GQA map100M契約](../configs/phase6/cross_gqa_map_science_20261015.json)を凍結・起動。実PID48654/start65870189・worker33840・760更新/4289851教師を確認。同元base configと52scalarだけの宣言済み差（candidate10,001,204、reference10,001,152）、元CE全stream/schedule/全品質gateを保持。owned CUDA10.287119秒で全state/history resume exact、48x1024有限gradient、FP32 cache事前許容差内、18 science CPU checksを通した。科学3743秒/技術込み4800秒、500保存/20heartbeat。次は同job終端と全80採否で、独立fresh全pipeline/fullDEV/全440/新TEST/採用は未達。

2026-10-15次案CPU準備: [cross-GQA signed mapの明示構造proposal](../reports/phase6/cross-gqa-map-preparation-20261015/proposal.json)を保存し、native本体を変更せずmodel18/trainer12 CPU checksと実元10B親CPU parityを完了。元重み・初期関数を保持し、52scalar追加の10,001,204 params。注意mapは別KV groupのものを現在Vへ適用し、旧output gate/同KV内の線形head混合と区別した。原CE全教師/streamを維持、全state resume exact。GPU/科学比較0、次は専用owned CUDA180秒・総4800秒提案内の実測とsafe typed science接続。CPU準備を品質合格・独立学習/fullDEV/新TEST/採用へ読み替えない。

2026-10-15最新終端: [sentence-copy確率減衰100M](../reports/phase6/pseudo-repetition-science-20261015/completion.json)は全17,698更新state/元CE対照一致・全80個別内容まで完了し、不採用に閉鎖。文法44→53、一貫性2→2、適切完結2→3、EOS19→22、反復45→31、BPB0.998487→0.999679、CI[0,0]で原gate未達。科学2544.969800＋技術12.190336秒、元UI実PID44053/start65703471へ復帰確認。次は別介入の選定で、固定条件の救済をしない。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用と4項目goalは未達。以下のrunning記述は当時の履歴。

2026-10-15最新: [sentence-copy確率減衰100M](../configs/phase6/pseudo_repetition_science_20261015.json)を凍結・起動。[実観測](../reports/phase6/pseudo-repetition-preparation-20261015/science_launch_observation.json)はPID41491/start65448557・300更新/1694544教師、科学4746/技術込み4800秒。native trainer14/科学workflow13 CPU checks、owned CUDA12.190336秒・全state/history resume・48x1024/8x512有限gradientを通した。次は同jobの終端・全80採否。準備/途中値をBase品質合格にしない。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用と4項目goalは未達。下の未実装・未凍結記述は当時の履歴。

2026-10-15次案準備: [TRAIN全句copy確率減衰](../reports/phase6/pseudo-repetition-preparation-20261015/proposal.json)をprospective選定。旧生成4gram ULと異なる正のdetach目標0.5×前copyを使い、元全CEを保持する同10M比較。pure14 checksと32x48元TRAINの一回限りCPU feasibility256row/94405比較/2.702730秒が完了。新model/GPU/学習/DEV/TEST/教材export0。次は専用trainerの全stateとCE equality、owned CUDA180秒・総4800秒提案内の実測、永続safe science接続と凍結。準備を品質・独立学習/fullDEV/新TEST/採用に読み替えない。

2026-10-15最新終端: [context likelihood100M](../reports/phase6/context-likelihood-science-20261015/completion.json)は全17,698更新の数値監査・同CE stream照合・全80個別内容reviewまで完了し不採用。一貫性2→1、適切完結2→1、EOS19→22、反復45→50、BPB0.998487→0.998524で資格なし。科学2410.335961＋技術9.415508秒、元10B UI実PID38043/start65165302へ復帰確認。次は別介入の選定で、独立fresh全pipeline学習/fullDEV/全440/新封印TEST/採用は未達。固定条件を救済しない。4項目Base goalはactive/未完了、下の稼働/停止記述は各記録日時の履歴。

2026-10-15final準備の追補: [DEV400/long40の安全入力・生成adapter](../reports/phase6/isolated-continuations-preparation-20261015/completion.json)を追加、8+4 CPU checksと元DEV80/codecの440入力context前検査を完了。旧5 modes/seed/temperature/top-p/6-ID suppression/128512長文順序とraw失敗を維持。実モデルや未知TESTを使わず、旧400/long40結果とfixtureで一致。独立学習/実fullDEV/全440内容/採用や永続runnerの代替ではない。現在のPID6927は44246925/100M教師で稼働、凍結scienceへ変更を加えず全80終端採否を待つ。

2026-10-15保存状態の追補: [同更新CE対照を使うcheckpoint2000 CPU監査](../reports/phase6/context-likelihood-preparation-20261015/checkpoint2000_CPU_audit.json)で11297746 main教師、原stream/sampler/実schedule/EOS/bytes/physicalと全numerical/FIFO/metrics prefix整合を確認。追加学習/GPU/評価0、品質の証拠ではない。同science PID6927は4180更新/23632643教師の途中で稼働確認。次は100M終端と全80内容採否、全4項目の最終品質は未達。

2026-10-15最新: [凍結context likelihood100M科学比較](../configs/phase6/context_likelihood_science_20261015.json)を開始。[観測](../reports/phase6/context-likelihood-preparation-20261015/science_launch_observation.json)は実PID6927/start64923858、840更新/4744814教師の途中。owned CUDA44技術更新/全state6対3+3/max CE48x1024/aux96x512はpassed、GPU9.415508秒/180内、最大11.0GiB。実32timingsから科学3656秒/技術含む総4800秒を凍結、専用永続runner/isolated evaluation/reviewerと13 CPU checksを完成。次は同processの終端、元CE対照の全stream/state会計照合、DEV256/Japanese/all80個別内容・元全quality guardsの採否。未達なら固定条件閉鎖、有資格時だけfresh whole-pipeline seed43/fullDEV/all440/新封印TEST/採用。4項目goal未達、Chat/量子化へ進まない。以下は先行準備の履歴。

2026-10-15次案選定: [natural same-suffix/equal-prefix-length native likelihood contrast](../reports/phase6/context-likelihood-preparation-20261015/proposal.json)をprospective選定。原10M/元10B親/元CE100M・48・42・Adam条件を維持し、既に学習した別文脈をFIFO128に保持、同suffix語彙尤度差を直接softplusで学習する。新parameter0。旧表現InfoNCE/template rankingの救済ではなく、同suffix prior/位置数を固定した別機構。pure12＋trainer11 CPU checksと[32x48 TRAIN feasibility](../reports/phase6/context-likelihood-preparation-20261015/CPU_feasibility.json)551pair/31 activeがpassed。科学/GPU0、品質未確認。次は新owned CUDA180秒以内の全state/resident/速度測定から、総4800秒提案内の科学予算・safe評価/採否CLIを凍結する。元の全品質・独立fresh seed/fullDEV/全440・新封印TEST/採用条件は未達のまま維持。

2026-10-15最新準備: [safe Japanese scoring回帰](../reports/phase6/isolated-japanese-scoring-20261015/CPU_regression.json)で隔離DEV-role inputs1642例/6641choiceの元codec境界・保存2M TRAIN counts・全score/tie規則がexact一致。新adapter16 CPU checks passed、実回帰0.165426秒/GPU0。本文の「safe scorer接続」はadapter単体まで完了、次prospective runnerへのcheckpoint binding/永続評価は未接続。新学習や品質改善ではなく、独立seed/fullDEV/新TEST/採用は未達。別の根拠ある比較選定を継続。

2026-10-15追補: [TRAIN index-byte監査](../reports/phase6/sampling-boundary-20261015/sampling_audit.json)で包含行skip/次行選択と直前行byte重みをCPU11 checks・固定256 metadata drawsで確認。旧「record-byte weighted」の説明は自身の長さによる重みと解釈できない。観測された条件内分布差は小さく、品質失敗原因や新学習の根拠にはしない。過去の対照・候補の同抽出pairingは保全。stream/DEV/TEST/GPU/学習0。次はsafe Japanese scorerの必要接続と別比較選定で、独立学習/fullDEV/新TEST/採用は未達。

2026-10-15最新終端: [fresh FIM pilot completion](../reports/phase6/base-fim-pilot-20261015/completion.json)は10000更新/正確94160195教師・DEV256/全80個別review・全state/元stream/全更新監査を完了し不採用。文法28→31、一貫性2→2、適切3→2、EOS13→14、反復49→51、BPB1.290203→1.292414、主差CI[-.0375,.0375]。科学1527.822100＋技術9.153452＝1536.975552秒で科学2519/総3600内。元UI復帰。固定FIM条件を閉鎖し救済・延長をしない。独立学習/fullDEV/新TEST/採用は候補資格なしで未実施、Baseと4項目目標は未達。次はactiveなBase-only範囲で別の根拠ある比較を選定する。以降の稼働・準備記述は過去の観測で、現在のjob生存や品質完成ではない。

稼働中のCPU補足は[保存状態監査](../reports/phase6/fim-feasibility-20261015/checkpoint2000_CPU_audit.json)と[日本語fixed diagnosticsの入力分離](../reports/phase6/fim-feasibility-20261015/Japanese_diagnostic_export.json)。将来の本比較の安全な診断入力として192/331/1119の元inputs/goldのみを保存済みDEV結果から投影、新reader13 checks passed。payloadをGit/学習へ移さず、元混在suiteやTESTを開かない。既知DEV/fixed benchmarkで未知評価・独立監査・品質改善ではない。現在のpilotを変更・再起動しない。

2026-10-15最新: [凍結fresh FIM pilot](../configs/phase6/base_fim_pilot_20261015.json)と永続実行/DEV-only評価/採点CLI、13 CPU checksが完成し科学学習を開始。[観測](../reports/phase6/fim-feasibility-20261015/science_launch_observation.json)は実PID1343/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start64143474、675更新/6352596教師。終端目標10000更新/94160195教師、science2519秒/技術含む総3600秒。v2 launcherのUI解放待ち修理は科学条件を変更せず、初回開始前失敗を保全。次は同じ実processを観測し、終了後の全80 raw-bound内容/全stateと元stream/採否を確認する。pilot screenをBase採用に読み替えず、独立fresh学習・全文DEV/全440・新封印TEST・採用までの4項目を保持する。以下の準備のみの記述は科学開始前の履歴。

更新: 2026-10-15 JST。文書/計画納品d44b8a0の後、「4まで」で評価分離修理からBase最終判定までが明示再開。[修理147](147_evaluation_boundary_repair.md)は新DEV reader/生成/review・CPU21 checks・実DEV80入力のread-set監査まで進んだ。後続は下のfresh FIM prospective選定と専用技術検証。科学学習/品質評価0・科学契約未凍結。Base/Chat未完成・未採用、原10M/品質を維持し、Chat/量子化へ自動移行しない。

[最新準備](../reports/phase6/fim-feasibility-20261015/protocol_readiness.json)は、同native10M・元2B schedule/TRAIN/batch80/seed42と既存対照10000更新/94160195教師を使うfresh FIM PSM pilotをprospective選定。新sampler/trainer16＋workflow9 CPU checks、実10M zero/元source各2560行を照合し、専用CUDA40技術更新/383190教師・全state4対2+2・80x1024/32 timingsがpassed。GPU9.153451952966861秒、pilot予測2519秒/提案総上限3600秒。次はscience永続CLI・隔離DEV256/80評価・notes/reviewerを完成して凍結する。pilotの相対screenを正式Base資格へ置き換えず、独立fresh学習・全文DEV/全440・新封印TEST・採用を維持する。技術probeを再起動しない。

選定前の[FIM CPU feasibility](../reports/phase6/fim-feasibility-20261015/selection_assessment.json)はserializer20 checksと固定24 TRAIN文書のtoken/bytes/EOS保存・context1024適合を確認。固定4096 ordinary marker35tokenの追加入力は標本比26.2746%。科学教師/GPU0で、FIMの通常Base改善・source全体への適合は未実証。成熟親100Mを自動選定せず、fresh対照/意味のあるhorizon/marker教師と長文処理/予算を定義してから比較の採否を決める。新recipe未選定、後半の独立学習・全文DEV・封印TEST・採用を省略しない。

[最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md) / [次の計画145](145_post_rejection_next_plan.md) / [今回更新146](146_documentation_followup.md)。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。

## 前回停止時の道筋（歴史記録）

| 経路 | 現在の判断 | 次に必要なもの |
|---|---|---|
| 閉じた139 | 内容20/18/19/15 of80・自己文脈5/5/5/1 of24、主CI・反復/文字失敗も未達。不採用 | 終了job・採点・NLL・別LR/seed/予算の救済を再開しない |
| 独立確認 | 7分岐は候補なしで未実行・品質未確認 | 原gateを満たすrecipeが先。生成乱数やCPU準備でfresh学習を代替しない |
| Base復旧124 | 未再開、介入未選定 | 根拠ある介入1件と原品質・対照・資源・終了条件。合格Baseで通知停止 |
| 次SFT・教材/目的/効率 | 未選定・未凍結、提供履歴でも品質不足 | 未回答の問いと別の明示再開。既に拒否したpadding等を再試行しない |
| 量子化・20B/50B・公開 | 今回の範囲外 | 採用モデルと別の範囲判断。残予算を開始許可にしない |

前回Chat139の新GPUは2,658.673158秒/33,600秒。以前の比較やCPU時間とは別。目的・Phase定義・原品質条件を以下に保持する。初期・途中のロードマップ全文は[更新前原文](../reports/investigation/documentation-refresh-20261014/baseline.json)から参照する。

## 目的と停止境界

約10Mパラメータの日本語モデルをスクラッチ学習し、短い自然な文章を生成できるBase、その後に短い雑談を行うChat、ローカル利用一式を作る。現モデルは10,001,152 parameters、context1024、Tokenizer4096。9.5M〜10.1Mの元予算を維持する。高度な推論・コード生成・長文RAGは成功条件に加えない。

128/131/133の限定Chat-first比較は、未採用の元WebUI10BからSFTする診断として明示再開後に実行し、いずれも品質未達で閉じた。最新の結果は141。教材比較135は138、低LR比較139は141で不採用終了し、Base採用条件を飛ばして完成扱いにせず、量子化へ進まない。Base復旧を再開する場合は従来どおり必要な証拠を満たすBaseまでで通知・停止する。新しい計画や準備コードを完成・実行許可の証拠にしない。

## 10Mを維持する制約

ユーザーは2026-10-08に、10Mのサイズ維持が重要であり、その小ささを優位性とする方針を明示した。精度を上げるための大型化は本計画の解決策に含めない。現在10,001,152 parameters、既存9.5M〜10.1Mの総パラメータ予算を維持する。サイズ内の構成配分・教材・学習目的・最適化は比較対象になり得るが、改善効果は未実証。大型モデル比較は別の明示依頼がある場合に限る。元の日本語Base品質目標を維持し、対象領域を勝手に狭めて達成扱いにしない。学習・研究実行の停止は継続する。

<a id="phase-0-成功条件環境実験管理"></a>
<a id="phase-1-データの小規模pilotと評価split"></a>

## Phaseごとの目的とゴール

| Phase | 現在の状態 | 目的 | 完了に必要な成果・証拠 |
|---:|---|---|---|
| 0 | 完了 | 成功条件・実験管理を固定する | config/schema/seed/評価split。[証拠16](16_phase0_completion.md) |
| 1 | 完了 | 追跡可能な小規模pilotを作る | corpus/manifest/split/会話pilot。[証拠17](17_phase1_completion.md) |
| 2 | 完了 | 日本語Tokenizerを確立する | 同sampleの4k/8k学習と特殊token契約。[証拠18](18_phase2_completion.md)。再学習しない |
| 3 | 完了 | モデル・cache・exportを成立させる | forward/cache/HF/float GGUF等。[証拠19](19_phase3_completion.md)。学習済み量子化品質とは別 |
| 4 | 完了 | 4090で再現可能な学習基盤を作る | WSL/CUDA/BF16、shard学習、全state保存再開、安定batchと速度。[証拠21](21_phase4_completion.md) |
| 5 | 完了 | 小予算で候補を選ぶ | overfit/smoke/100M比較と候補判断。[証拠23](23_phase5_completion.md)。品質完成とは別 |
| 6 | 学習・多数比較実施済み、品質未達。一時停止 | 自然に完結する日本語Baseを完成する | 固定品質・保持比較、独立学習seed、fullDEV/全生成内容、protectedTEST、採用・復旧記録 |
| 7 | 128/131/133/135の限定SFT比較と全内容確認は完了・不合格。138で6段階の実行監査を閉鎖、追加実験停止・採用未達 | 現Baseからの会話適応の不足を切り分ける。後続の教材比較・完成段階は別の再開判断 | 正式品質は保持・独立学習seed・人間blind・最終評価等も必要。実施条件不成立の保持/回復は未確認 |
| 8 | 最終成果物は未着手、範囲外 | 量子化とローカル利用を完成する | 採用モデルのfloat/量子化比較、容量・速度・品質、独立環境での再現 |
| 9 | 未着手、別の判断が必要 | 20B/条件付き50Bの継続価値を測る | 同条件10B→20BのBPB差CI下限>0、生成に重大退行なし、追加予算内のときのみ50B候補 |
| 10 | 後半構想、範囲外 | baseline以後の追加研究を行う | 共有/蒸留/hybrid/規模比較等の定義済み対照と採否。paid cloudは別途許可 |

Phase0〜3の成果物と歴史的な証拠を維持する。既存環境での文書更新に、再取得・Tokenizer再学習・export再検証・速度benchmarkを加えない。

## Phase6の現在地

元10Bモデルの本学習・保存と評価は完了したが、Baseの品質目標は未達。別の約10.6B staged系列は一貫性23/80・適切完結26/80で基準に近いが合格ではない。系列の異なるモデルのtokensを合算しない。

以前の同native2B比較では、教師量正規化weight decayでBPB1.106386→1.090316に改善したが、一貫性3→3、適切完結7→5、EOS20→23、反復27→27、Unicode失敗0→1（各80）。固定条件は閉鎖・不採用。独立seed43や10B延長へ自動的に進めない。[証拠](../reports/phase6/base_teacher_decay_2b_completion.json)。

データ量、学習量、モデル容量のどれか一つを原因と断定できていない。限定Chat診断と教材/低LR比較は141、Base文書長重みは144まで完了したが、Chat完成もBase不足の単独原因も実証されなかった。低LRの1件比較も不採用で閉じた。次の介入は計画145の評価隔離修理・既存証拠照合と、別の明示再開時の契約で選定・凍結する。Base復旧が必要なら[計画124](124_base_recovery_plan.md)の段階0〜5へ戻り、既存結果の再利用で次の比較を最大1件に絞る。研究の一巡が不採用で終わった場合も報告して止める。

<a id="品質目標と判断ルール"></a>

## 現行の採否条件

技術的に動いたことと能力目標の達成を分ける。原品質目標・各凍結実験の比較条件を結果に応じて緩めない。

| 判断の段階 | 現行条件 |
|---|---|
| 固定Base DEV80の絶対screen | 文法2≥56、一貫性2≥27、適切完結≥27、EOS≥37、反復≤18、empty/role/Unicode失敗0 |
| 比較と保持 | 指定されたmatched/strong/cached/historical参照を区別し、元相対条件・paired CI・BPB guardを満たす。相対一貫性差≥8かつCI下限>0等を省略しない |
| 独立学習seed | 同レシピをfresh seed43で学習。生成乱数の変更では代用しない。有利なseedだけ選ばない |
| fullDEVと生成確認 | 全文DEVと400生成＋長文40の全内容を確認。DEV256のBPBを全文結果へ読み替えない |
| protectedTEST | 選定封印後に20prompt×5mode=100生成等。文法70%、一貫性/適切完結27/80の率、停止95%、反復≤18/80の率、文字等の失敗0を元実装どおり判定 |
| Base採用 | 上記の実証、追跡可能なweights/Tokenizer/data/config、再開・ローカル利用記録をそろえる |

[元policy](../configs/phase6/base_parallel_residual_review.json)、[現行適用例](../scripts/review_base_teacher_decay_2b.py)、[最終TEST条件](../scripts/run_final_base_test.py)、[最終採否](../scripts/review_final_base_test.py)、[評価契約](evaluation_protocol.md)を参照する。表は要約であり各実験の全guardを置き換えない。元のBase文法70%、Chatの文法・関連性70%、文脈60%、停止95%等の目標も維持する。

native独立seedのfactoryとCPU testsは準備済みだが、永続runner/reviewerとfullDEV/TESTへの明示的な接続は未完成。旧stable+20M-decay専用runnerへnative checkpointを偽装して渡さない。[準備122](122_base_native_seed_confirmation_preparation.md)は作成当時の記録であり、候補の採否は後続123を参照する。

DEVを繰り返し見た非blind評価の限界を明記する。最終TESTを調整用に使わず、不合格後の改訂には新たな未使用TESTが必要。独立corpus監査や人間blindが未完了のままなら、完了したと記載しない。

<a id="高速に完成させる進め方"></a>

## 資源・時間・実行の原則

全Pythonはuv管理3.12.7。学習はWSL2/RTX4090/Linux disk。速度は教師tokens/秒・CE入力/秒・padding込みphysical入力/秒を区別する。過去のFlash/compile高速系列の値を、現在のBF16/math/native教師速度として使わない。最大VRAM使用量と最速設定も別々に実測する。

長期学習の前に実CUDA保存再開gateと安定batchを確認する。checkpointにはmodel/Adam/scheduler/RNG/sampler/countersを保存し、実PID/boot/start・累積GPU ledger・logsを永続化する。予算は現条件の実測から固定し、未達時に暗黙に増やさない。

同じデータの反復を新規データ量に足さず、目標データ量を準備済み量と呼ばない。既存受入データと証拠を再利用し、独立全corpus再走査を学習の前提にしない。新しい環境や変更箇所に必要な確認だけを行う。

## 後続フェーズの扱いと履歴

128/131/133/135/139の限定Chat比較は実行・不合格終了し、追加の実行は別の明示再開・新契約待ち。通常のPhase7完成とPhase8〜10も別の再開判断が必要。診断にmid-training比較まで自動追加せず、最終Chat段階ではrouteの効果、生成seed・独立学習seed・会話family・保持を分ける。量子化は採用floatモデルとの許容退行を先に固定し、全artifact5〜10MB級という目標を実容量・品質で判定する。有料cloud・公開・他者への送信は別途許可が必要。

更新前のPhase定義・全追記・予算と比較契約の原文は[ロードマップ履歴20261008](project_roadmap_history_20261008.md)にbyte一致で保存した。各実験の凍結config/reportが証拠の正本。履歴の将来案を現在の開始指示として扱わない。

今回整理前の全文は[20261013履歴保存一覧](../reports/investigation/documentation_plan_refresh_20261013/baseline.json)にbyte一致で保全した。
