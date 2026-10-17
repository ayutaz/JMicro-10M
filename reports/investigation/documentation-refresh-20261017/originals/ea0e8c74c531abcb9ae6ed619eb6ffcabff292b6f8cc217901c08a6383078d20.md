# Base改善の今後の計画

2026-10-17初RDrop25M科学比較は全件確認して不採用・閉鎖: reports/phase6/rdrop-science-20261016/completion.json / review.json。元25M/4420更新、二回hardgold計50M/整合対25M、全typed native/Adam/dropout RNG/sampler状態・全履歴とnative25M主stream/時計を確認。対照→候補は文法44→47、一貫性1→3、適切完結3→6、EOS11→19、規定反復53→49、BPB0.9927168291→1.0279654060（3.5507%悪化）。対応coherence差2/80・CI[0,.0625]と元差8/絶対27を満たさず、全5内容/停止/反復の絶対条件も不合格。全80を新raw-bound日本語理由で個別採点し、非blind Codex・独立人手でないことを保持。文字/role/空0でも意味循環・数量/因果誤りが残る。新科学777.297900秒、技術169.245628＋科学4241.304909＝総4410.550537秒。累積時間上限なしのユーザー許可は有効、元1757秒の単一run内で終了。実459024/start80531912/同bootとWindows32704/14:49:13.5052660Zは終了、元UI459564/start80610052/正しいidle HTTP/実FLOCKへ復帰を再確認。旧probe再実行0、全state/metricsはWSL、raw/notes/小metadataをWindows同bytes保全し、共有logは観測bytesのsnapshotを保存。係数/dropout/sites/教師/親/seed/decoder/元品質の救済延長をしない。9層256/FFN1040と6層384/FFN832の既存300M構造比較は不採用済みと原config/reviewで確認し、未検証と誤称して再試行しない。次は異なる根拠ある未回答比較を1件定義する。Base本比較資格・真の独立fresh全pipeline seed43/fullDEV/全440/新封印TEST/採用は未達、時間不足を理由に再blockせず元4項目を維持する。

2026-10-16ユーザーが「上限はないので無限に使っていいです」とローカルGPU累積上限を解除し、元4項目の研究を再開。reports/phase6/rdrop-science-preparation-20261016/authorization.json / proposal.json / readiness.json。旧180/4800は過去条件として費用判定ごと保全し、既消費技術169.245628＋科学3464.007009＝総3633.252637秒を継承する。10M/元品質/評価隔離/独立全pipeline/全文DEV/全440/新TEST/採用の要件は不変。品質不採用条件は再開しない。予算だけで科学未実行だったRDropは、旧target-batch CUDAの最大二回グラフ/元座標対照/全state再開/実6cache/全32履歴を再利用し、新契約で初の科学25Mを準備した（旧probe/job再起動0）。専用runner/reviewer/protocol/永続launcher、35 CPU workflow checksが合格しconfigs/phase6/rdrop_science_20261016.jsonを凍結・preflight済み。最初33pass/2failのadapter schema/arm名誤りは元source/XMLを残して修理し、凍結数値条件や元閾値は変更していない。元10B/fresh Adam/48/42/元25M、学習は平均二CE+.5対称KL/dropout.1、通常eval推論10001152。対照と元教材/主physical/時計一致、候補は二回physicalと学習dropout RNG差を明示し、対照と終端torch RNGの同一を誤要求しない。新累積時間上限なし、単一runは元全32予測1757秒（評価保存600秒込み）と固定教師・失敗終了条件を保持。元UI450807/start68828958/同boot/正しいidle HTTP/実FLOCK・唯一GPU peerを再確認。現時点新GPU/科学0、次は新永続科学jobを起動し終端と全80内容・全履歴/数値stateを確認する。Base/独立学習/fullDEV/新TEST/採用は未達。以前のblocked3回は過去の判断で、再開後のblocked監査は0から。

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

2026-10-15次案: [原文書の残り割合を補助予測する事前proposal](../reports/phase6/document-progress-preparation-20261015/proposal.json)と[CPU44 checks/一回限り既知192窓](../reports/phase6/document-progress-preparation-20261015/CPU_readiness.json)を保存。原CEを変えずscalar sigmoid/L1係数.1・zero初期256重みを学習時だけ追加し、推論はnative10,001,152。新規対照/候補各25Mの別目的pilotで、cached100Mを同25M対照にしない。GPU/品質は未検証。次は専用probeとscope checks、最大容量FIRST、native学習一致、両条件全state再開/実6cache/各32計時を実装し、全既消費2074.891132秒と両25M＋各600秒評価保存が元4800秒内と実測確認できる場合だけ科学workflowを完成・凍結して実行する。元technical残81.526398/総残2725.108868秒、係数/教師/precision/geometry/予算や品質gateの救済なし。pilot成功は本比較資格やBase完成ではなく、独立fresh全pipeline seed43/fullDEV/全440/新封印TEST/採用まで元4項目goalを維持する。以下は履歴。

2026-10-15最新CPU判断: [入力依存RMS倍率の別仮説](../reports/phase6/self-rescaled-norm-preparation-20261015/proposal.json)は[数式19/専用model22 checks・実親cache判断](../reports/phase6/self-rescaled-norm-preparation-20261015/CPU_closeout.json)まで実行した。実数10,014,976、原全weight/NoQKNorm・初期native関数は保持したが、active beta=.01で元full/cache複合精度条件を超え固定実装をGPU前に閉鎖。K/V・metadataの合格とlogitsの不合格を分け、原因未確定・新科学0を残す。

次は旧source再実行・beta/alpha/箇所/activation/grouping/epsilon/precision/親/seed/教師/decoder/geometry/予算救済や自動localizationではなく、別の根拠ある未回答仮説を原proposal/resultと照合する。累計2074.891132秒・残元81.526398/2725.108868秒は不変。負のgain/saturation/conflict診断は新原因を示さず、既存sampler境界監査の小さな差も新学習の根拠にはしない。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用と全4項目goalはactive/未達。以下は履歴。

2026-10-15実機判断: [固定ゼロK/V注意](../reports/phase6/quiet-attention-probe-20261015/completion.json)はCPU37/18/23と実機容量・元学習一致・全state再開・実6cache全項目に合格。ただし全32計時の科学3756秒＋既消費2074.891132秒が元総4800秒を超え、科学前に固定条件を閉じた。日本語品質の失敗実験とは扱わず、品質未評価・科学0を残す。

次は既存原proposal/resultから、閉鎖条件と異なる根拠ある未回答比較を1件選定する。元180/4800へ既scienceも含めて全額継承し、残81.526398/2725.108868秒内で実測資格を示すことが必要。warm再予測・計時除外・phantom/learned sink/親/seed/教師/decoder/形状/precision/予算による救済をしない。有資格レシピ後の独立fresh全pipeline/fullDEV/全440/新封印TEST/採用と全4項目goalはactive/未達。以下の次案準備・GPU未実施は履歴。

2026-10-15次の別仮説: [固定ゼロK/V注意](../reports/phase6/quiet-attention-preparation-20261015/proposal.json)を実装前に定義し、[CPU model37/trainer18＋実親cache](../reports/phase6/quiet-attention-preparation-20261015/CPU_readiness.json)まで完了した。原10,001,152/全原重みを保持しつつ、注意の分母にゼロ値の選択肢を加える。過去のquery-only出力gate・独立Q/K signed map・時間decay・語彙Sigsoftmaxとの差を記録し、同query/同native mapで異なる出力となる数学例と独立全勾配を検証。有効化初期関数が変わることと、CPU成功が品質証拠でないことを保つ。

次は専用owned CUDA検証を実装して範囲を確認してから、元最大形状/disabled-native学習一致/有効化6更新保存再開/実保存点cache/全32計時で判定する。新GPU0、科学workflowは未実装・契約未凍結。今回完了したscienceも含め累計2063.031660秒を元総4800へ継承し、残2736.968340秒内で元100M＋評価保存の実測見積もりが成立することを必須にする。元品質・10M・独立全pipeline/fullDEV/全440/新TEST/採用の到達範囲を変えず、全4項目goalはactive/未達。

2026-10-15最新判断: [independent rank8 QK100M](../reports/phase6/independent-map-science-20261015/completion.json)は全state/history・元CE対照との条件一致と全80の個別内容確認まで完了し、不採用で固定条件を閉じた。文法44→59に対し一貫性2→1・適切完結2→2・EOS19→19・反復45→48・BPB0.998487→0.998526で、元品質・保持基準を満たさない。新しい独立Q/K座標が技術的に更新された事実を、有用な表現や10M全般の根因の証明としない。

次は既存原proposal/resultから、今回や閉鎖済み比較と異なる未回答仮説を1件に絞り、対照・元全品質条件・実測予算を定義する。固定rank/分岐/親/seed/normalization/decoder/教師/形状/予算救済や旧条件再実行で進めない。有資格レシピができた場合だけ独立fresh全pipeline seed43/fullDEV/全440/新封印TEST/採用へ進む。全4項目goalはactive/未達で、比較閉鎖を全体完了にしない。実科学/Windows worker終了・元UI復帰・hash一致portable記録を終了receiptへ保存。以下の稼働中・未選定・準備値は当時の履歴。

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


2026-10-15最新判断: [tiled owned gate](../reports/phase6/forgetting-attention-fused-probe-20261015/completion.json)は最大容量/独立全勾配/learned全state resumeを通過したが、update6 FP32 cache guardで閉鎖。subcheck/max未保存を推測せず、CPU saved3の合格をCUDA6の修理に読み替えない。次は別read-only CUDA saved3観測で条件を切り分け、旧学習再現・閾値/初期化/形状/backend等の救済をしない。新GPU11.636436＋既消費1.244660＝12.881096秒を元180/4800へ全額継承。技術12更新のみで科学/独立全pipeline/fullDEV/全440/新TEST/採用と全4項目goalは未達。

2026-10-15別tiled実装の[CPU準備](../reports/phase6/forgetting-attention-fused-preparation-20261015/CPU_readiness.json)は元kernel/precision/10M/gate/data/品質を維持し、明示runtimeとlicenseを保存、26/24/22 checksと実親FP32cache合格。次は独立BF16 operatorの値/全勾配、resident48x1024、両arm初期一致/全state resume/active cache/各32timingsを同owned gateで実測する。前回1.244660秒を元technical180/総4800へ継承、両科学100Mと各600秒評価reserveを含む。新GPU0/科学未資格、独立全pipeline/fullDEV/全440/新TEST/採用と全4項目goalは未達。

2026-10-15最新判断: [key-bias数学SDPA owned gate](../reports/phase6/forgetting-attention-key-bias-probe-20261015/completion.json)は最大48x1024の容量不足で閉鎖、GPU1.244660秒・学習更新0。CPU精度合格を実機学習可能と読み替えず、形状/allocator/backend/予算で閉鎖条件を救済しない。次の[公式タイル化kernel一次調査](../reports/phase6/forgetting-attention-key-bias-preparation-20261015/fused_kernel_assessment.json)は未導入・未実機で、別実装proposal/勾配/runtime/cache/全state資格が必要。全消費を元technical180/総4800へ継承し、元10M/品質/独立全pipeline/fullDEV/全440/新TEST/採用の範囲を維持する。全4項目goalはactive/未達。

2026-10-15[別key-bias実装](../reports/phase6/forgetting-attention-key-bias-preparation-20261015/CPU_readiness.json)は同数式のsoftmax行定数を省き、元精度/初期化/FP32/10M/品質を変えず実親cache gateを通過。17/23/16 CPU checksと両arm全state resumeもpassed。次は専用owned180秒で最大48x1024のresident capacityをAdam前に確認し、通過時だけ両armの学習再開/cache/32timingsと総4800内を実測する。失敗時は閾値・batch・backend等で救済せず閉鎖。科学/独立全pipeline/fullDEV/全440/新TEST/採用は未資格、全4項目goalはactive/未達。

2026-10-15対象限定[実親cache層別診断](../reports/phase6/forgetting-attention-preparation-20261015/CPU_cache_layer_localization.json)は完了。最終差はnative1.4305115e-5で元基準内、forgetting reference0.0001010895で未達、最初の非exact箇所は双方共通で原因は未確定。完了診断の反復や初期gate/親/精度閾値等の救済をせず、同数式の別安定実装の価値と必要証拠を次に判断する。新科学/GPU0、独立全pipeline/fullDEV/全440/新TEST/採用と全4項目goalはactive/未達。

2026-10-15CPU判断: [forgetting attention model/trainer](../reports/phase6/forgetting-attention-preparation-20261015/CPU_model_trainer_closeout.json)は同元重み＋初期forget.5のlearned/static両arm設計を先に保存し、実count10,014,516・model14/trainer19 checksまで完了。しかし実元親cache差が元3e-5/2e-5を超え、reference実装は科学0で閉鎖。小fixtureや全state resume合格を実親精度の代替にしない。次は既存technical span上で数値差を局在化してから別実装の価値を判断し、元cache/10M/品質/対照/実測予算を維持する。新GPU/学習/DEV/TEST0、独立fresh全pipeline/fullDEV/全440/新TEST/採用と全4項目goalは未達。

2026-10-15次案: [forgetting-attention proposal](../reports/phase6/forgetting-attention-preparation-20261015/proposal.json)は独立したCPU数学referenceで[7 checks](../reports/phase6/forgetting-attention-preparation-20261015/CPU_math.json)を通した。正規化前の累積decayと旧出力後gateの差を確認しただけで、現在の失敗原因や品質向上は未証明。有限sigmoid gateの初期関数はnativeと異なるため、fresh対照か正当なmatched conversionかを解決してから実model/count/cache/selected CE/trainerと実測予算を準備する。新学習/DEV/TEST/GPU0、実count/科学契約未検証。旧next-two/recurrentは原記録から既閉鎖と確認し小変更で再試行しない。元全品質条件と独立全pipeline/fullDEV/全440/新TEST/採用の到達範囲を維持する。

2026-10-15最新判断: [causal-QKV contiguous100M](../reports/phase6/causal-qkv-contiguous-science-20261015/completion.json)は全state/原CE stream＋宣言lag差・全80個別内容を確認して不採用に閉鎖。文法44→61、BPB0.998487→0.998450でも、一貫性2→1・適切完結2→1・反復45→47で元gate未達。文法・BPBと意味の進行・完結を区別し、固定lag/tap/層subset/activation/親/seed/decoder/予算を救済しない。次は原proposal/runtime/resultから別の未回答仮説1件を選定して元gate・対照・実測予算を固定する。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用は有資格候補なしで未実施、全4項目goalはactive/未達。下の進行中・技術のみは当時の履歴。

2026-10-15進行: [causal-QKV contiguous100M](../configs/phase6/causal_qkv_contiguous_science_20261015.json)を凍結・起動。新GPU実装比較で同verification3から各3更新の全state/history、保存済みreference0/3/38と32非時間metricsがexact、保存再開/48x1024/raw cacheも合格。旧reference19.769017＋新15.081088＝技術累計34.850105秒を元technical180/総4800へ継承し、実測科学4291秒で予算を満たした。モデル/lag/教師/precision/backend/品質を救済変更せず、元親/原CE100M/48/42、明示runtime・候補10,014,464で実PID58473/start66504429が240更新/1355486教師の途中。次は同job終端の原対照全state/stream＋宣言構造差と全80内容採否。資格後だけ独立fresh全pipeline/fullDEV/全440/新封印TEST/採用へ進む。全4項目goalはactive/未達。

2026-10-15新案の技術段階: 前2有効tokenのprojected Q/K/Vを加える10,014,464 modelはCPU/実親parityとGPU数値/cache/保存再開を通過したが、[reference実測](../reports/phase6/causal-qkv-probe-20261015/completion.json)の科学予測8581秒が総4800秒を超え、科学0でreference条件閉鎖。[別の同数式contiguous実装](../reports/phase6/causal-qkv-contiguous-preparation-20261015/CPU_equivalence.json)は共有joined tensorの値/勾配/3更新Adam exactをCPU11項目で確認。初回失敗も保全し、元構造/教師/品質/precision/backendを変更せずGPU同値性・速度はこれから検証する。次の新CUDA gateは既消費19.769017秒を元technical180/総4800へ継承する。予算/教師/tapの救済やreference再実行では進めない。独立fresh全pipeline/fullDEV/全440/新TEST/採用と4項目goalは未達。

2026-10-15最新判断: [first-layer value residual100M](../reports/phase6/value-residual-science-20261015/completion.json)も全state/元CE対照・宣言12scalar差・全80個別内容を確認して不採用に閉鎖。文法44→58/EOS19→23に対し一貫性2→1・適切完結2→1・反復45→47・BPB0.998487→0.998524。初期関数を保存した層間V0経路の追加だけでは今回の生成品質改善は成立しない。固定V0係数/層subset/normalization/親/seed/decoder/予算を救済せず、次は既存の原proposal/runtime/resultから別の未回答仮説1件を選定する。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用は有資格候補なしで未実施。4項目goalはactive/未達、以下のrunning等は当時の履歴。

2026-10-15進行: [first-layer value residual100M契約](../configs/phase6/value_residual_science_20261015.json)を実元親CPU parity/専用trainerと全state resume/owned GPU9.812882秒・最大48x1024/18科学workflow checks後に凍結・起動した。science3568/技術込み4800秒、元親/原CE100M/48/42と全元品質gateを保持。実PID52873/start66148908は40更新/233183教師の途中で、品質未判定。次は同job終端の原対照全state/stream＋宣言12scalar差と全80個別内容採否。未達なら固定条件閉鎖、有資格時だけ独立fresh全pipeline/fullDEV/全440/新封印TEST/採用。全4項目goalはactive/未達、下の未実装/科学0記録は履歴。

2026-10-15次案選定: [first-layer V residual proposal](../reports/phase6/value-residual-preparation-20261015/proposal.json)を実装前に保存し、別modelの[18＋1 CPU checks](../reports/phase6/value-residual-preparation-20261015/CPU_preparation.json)を完了。元Vに最初のVを零係数から足す12 scalar/10,001,164で、閉鎖したcross-map/output gate/parallel residualとは情報経路が異なる。ただし局所の原因診断・品質改善ではない。実元親CPU parityと専用typed trainer/全state resumeが次で、元native hidden helperは流用不可。owned CUDA/科学CLI/科学契約は未完、予算は実測後に凍結し元全gateを維持する。科学学習/GPU/new data/DEV/TEST0、独立fresh全pipeline/fullDEV/全440/新TEST/採用は未達。

2026-10-15最新判断: [cross-GQA signed-map100M](../reports/phase6/cross-gqa-map-science-20261015/completion.json)も全state/元CE stream・宣言した構造差と全80個別内容を確認し不採用に閉鎖した。文法44→60に対し一貫性2→2・適切完結2→2・EOS19→18・反復45→47・BPB0.998487→0.998503。文法と意味の進行・完結は別に評価する。今回だけでGQAや10M規模が根因とは断定せず、固定条件のmap/係数/normalization/親/seed/decoder/予算を救済しない。次は原proposal/trainer/resultから別の未回答仮説1件を選定し、対照・元gate・実測予算を事前固定する。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用は有資格候補なしで未実施。全4項目goalはactive/未達、下のrunning/準備記録は当時の履歴。

2026-10-15実行追補: cross-GQA構造案はowned CUDA10.287119秒で全state/history resume exact・48x1024有限gradient・事前精度内のcache比較を通し、[科学100M契約](../configs/phase6/cross_gqa_map_science_20261015.json)を凍結して開始した。元base config一致＋宣言52scalar差のguardと全品質条件を維持、科学3743/総4800秒。現在PID48654/start65870189の同job終端と全80内容採否を待つ。下のGPU/CLI未実装記述は当時の履歴で、独立学習/fullDEV/新TEST/採用は依然未達。

2026-10-15別構造案: [cross-GQA signed-map proposal](../reports/phase6/cross-gqa-map-preparation-20261015/proposal.json)を明示してからCPU実装・検証した。元nativeを置き換えず、原関数を保つ初期0の52scalar追加（10,001,204）で、他KV groupのmapを現在Vへ適用する。旧query-dependent output gate/同KV内の線形混合/閉鎖MHA allocationと区別し、model18/trainer12 checksと実元親parityを完了した。次は専用owned CUDA/typed保存再開/明示的architecture対照/隔離評価・reviewerの接続と実測予算を先に完成する。CPU成功や論文を品質改善の証拠にせず、元全gateと独立全pipeline/fullDEV/全440/新封印TESTを維持する。

2026-10-15終端追補: [sentence-copy確率減衰100M](../reports/phase6/pseudo-repetition-science-20261015/completion.json)を実行し、全state/元CE対照/全80内容を確認して不採用に閉鎖した。反復45→31は減ったが、一貫性2→2・適切完結2→3・BPB0.998487→0.999679で元品質・保持は未達。反復対策だけで意味の進行と完結が成立するとは確認できなかった。固定条件を救済せず、次は別の根拠ある未回答仮説を1件選定する。4項目goalはactiveで、独立fresh全pipeline/fullDEV/全440/新封印TEST/採用は有資格候補なしの未実施。下のCPU準備・科学未凍結記述は当時の履歴。

2026-10-15次条件選定: [TRAIN全句copy確率減衰のprospective案](../reports/phase6/pseudo-repetition-preparation-20261015/proposal.json)を選び、原source比較/pure14 checks/一回限り元TRAIN32x48 CPU feasibilityを完了した。原CE/10Mを保持するDITTO系variantで、旧rollout4gram ULとは負例生成と正のdetach確率目標が異なる。次は専用trainer・全state resume/disabled CE equality、その後だけowned CUDA180秒と総4800秒提案内の実測・safe science接続・凍結。教材/モデル/学習/DEV/TEST/GPU0の準備までで、品質改善や最終資格ではない。固定scopeと原品質条件は維持する。

2026-10-15進行追補: 「4まで」の再開範囲で評価reader分離と新同10M比較を実施した。最新[context likelihood100M](../reports/phase6/context-likelihood-science-20261015/completion.json)は全80内容と全state/対照照合まで完了し、不採用に閉鎖。一貫性1/80・適切完結1/80・反復50/80、全保持条件未達。次は既存結果から別の未回答介入を1件選定し、対照/原gate/実測予算を事前固定する。独立fresh全pipeline学習/fullDEV/全440/新封印TEST/採用は有資格候補ができてからで、まだ未達。Base完成までの4項目goalを比較閉鎖へ縮めない。以下の2026-10-14文書限定scope・未選定記述は当時の履歴で、後の明示再開を上書きしない。

更新: 2026-10-14 JST。現在の依頼は全現行文書の最新化と今後の計画作成。Base/Chatは未完成・未採用。研究・教材準備・診断・生成評価・GPU学習は再開していない。

[最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md) / [次の計画145](145_post_rejection_next_plan.md) / [今回更新146](146_documentation_followup.md)。

元の段階0〜5は維持し、実行の詳細は計画145へ接続する。143/144の一巡は不採用で停止、前の「6まで」は未達/blocked後にユーザーが解除。新しい介入は未選定。次の実行契約で一巡か定義済み複数比較か・総予算・ゴールを明記する。今回の文書依頼は新しい研究cycleの再開ではない。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

元Base TEST20 promptと元Chat TEST20行は別のCPU解析問題を保存した。学習・GPU TEST採点に使っていないこととCPU未解析は別。将来の有資格最終確認にはreader分離と新しい封印TESTが必要。今回data/TESTを開封・再処理しない。

次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。

## 当時の資料・保存手順

## 目指す状態と現在の判断

10,001,152パラメータ規模を維持して、日本語の短い続きを関連性・一貫性を保って完結できるBaseを完成させる。必要な品質・独立学習seed・fullDEV・protectedTEST・採用記録がそろったら通知して止める。Chat、量子化、20B/50B、公開は今回の再開後の到達範囲に含めない。

最新2BではBPB約1.45%改善に対し一貫性3/80のまま、適切完結7→5/80、反復27/80のまま。元の6絶対条件と全比較条件は未達。この候補の自動10B延長やseed43確認へ進む根拠はない。過去の2B→5B、教材増量、初期化、勾配蓄積等も結果と条件を保ったまま参照し、失敗条件を小変更して繰り返すことを既定路線にしない。

## 固定する制約

2026-10-08のユーザー方針: **10Mのサイズ維持が重要であり、それ自体を優位性とする。** 大型化と品質を選び直す計画ではなく、10Mの制約内で品質改善を目指す。

- 総パラメータは既存の約10M予算（9.5M〜10.1M、現モデル10,001,152）を維持する。大型化や大型モデル診断比較は次回の既定作業にしない。
- 比較候補は教材の品質・文脈・終端、学習目的、最適化、同予算内のパラメータ配分などから選ぶ。候補の有効性や大幅改善を事前に保証しない。
- 日本語Baseの品質基準・評価分離を維持する。モデルが小さいことを理由に基準を下げたり、物語だけ等へ対象を無断で縮めたりしない。
- 改善が得られなければ、10Mのまま限界と未達を報告する。この方針記録は学習・研究実行の再開指示ではない。

## 次の比較を選ぶ順序

まず全80の既存notesと過去completionを再利用し、文章品質の失敗と検証済み条件を対応付ける。採点のやり直しや新しいDEV抽出は行わない。例えばbase-001/002/005には同じ発話・描写・文の循環が記録されているが、これは失敗の観察であり原因の確定ではない。[既存notes](../reports/phase6/base_teacher_decay_2b_candidate_notes.json)。

| 検討順 | 調べる問い | 既存証拠と限界 | 次案に必要な条件 |
|---:|---|---|---|
| 1 | 教材の文脈・終端・配分が、関連した続きと完結を学ぶために適しているか | LF感度や原文脈診断はあるが、自由生成改善の証拠ではない。過去の教材/配合比較も複数閉鎖済み | 既存比較と異なる未回答の問いを示す。単なる増量や末尾表示修正を品質改善と扱わない |
| 2 | 正解履歴での学習と自己生成履歴での反復の差に、介入可能な要因があるか | 少数原文の記憶は成功、TRAIN既知例の自由生成にも循環がある。過去のsequence目的比較も再利用する | 既に失敗した目的・係数の再試行ではない根拠と、同教師対照を定める |
| 3 | 10M内の構成配分や最適化に、未検証の改善余地があるか | 初期化・勾配蓄積・teacher-decay等の固定条件は不採用 | 総parameter予算を先に確認し、主要変更1つの別proposalを作る。frozen model/sourceを上書きしない |

この順序は調べる優先順位であり、新しい原因・介入の採用決定ではない。既存結果だけで次案を定義できれば追加診断は省略する。どの案にも根拠が不足する場合は、調査を自動延長せず不足を報告する。

## 次案に必ず記載する項目

1. 対象とする失敗を1つと、その改善を測る主要指標。文法・関連性・一貫性・完結・停止・反復は別に記録する。
2. 仮説を支える既存report/例ID、交絡・反証、閉じた比較と何が違うか。
3. 対照と候補の実parameter数（9.5M〜10.1M内）、checkpoint/初期化、TRAIN/Tokenizer、教師予算、seed、主要変更1つ。
4. 学習時の変更と生成/表示時の変更の区別。raw文字・停止失敗を後処理で消して元品質合格としない。
5. pilot固有の事前screenと、元の全品質/保持guard。BPB低下だけで本比較へ進めない。
6. 必要CLI/未実装箇所、関連checks、実CUDA全state再開gate、ログ/identity/ledger/checkpoint保存。
7. 実測に基づくGPU上限・評価/保存の時間、失敗時の閉鎖、一巡後の報告・停止。

次の介入、教材作成、25M〜100Mのどの教師予算を使うかは、まだ選定・凍結していない。この文書は実行済みの比較や開始commandではない。

## 再開後のフェーズ

| 段階 | 目的 | 具体的な作業 | 終了条件・成果物 | 進行判断 |
|---|---|---|---|---|
| 0: 実験の整理と次条件の選定 | 同じ失敗の反復を避ける | 既存completion・raw-bound notes・実験索引を使い、未解決仮説と既検証条件を対応付ける。教材の文脈/終端、学習時と生成時の差、最適化/モデルの候補を区別する | 次の比較を最大1件に絞った提案。仮説、対照、変更点、固定量、指標、予算、反証・終了条件、未実装CLIを記載 | 未回答の問いと実行可能な比較を特定できなければ、その理由を報告して止める |
| 1: 必要な最小診断 | 次の学習が何を検証するか明確にする | 段階0で欠けていると確認した診断だけを実装。既存6文記憶/32文train-dev/LF/原contextを再実行しない | 実診断結果と事前screenの採否。追加学習は0 | 結果が次の介入を支持しない場合はその条件を閉じる |
| 2: 同条件の短い学習比較 | 文章品質が改善する兆候を調べる | 同fresh親または同学習済み親のどちらかを明記。モデル、TRAIN、教師予算、seed、評価をそろえ、主要変更は1つ。専用command/凍結config/実CUDA再開gateを用意 | 候補と対照の同教師pilot、固定DEV256/日本語評価/全80内容。raw、failure、採否を保存 | BPBだけの改善では進めない。事前に定めた生成改善screenと全保持guardを満たす場合のみ次段階を提案 |
| 3: 有望条件の本比較 | 小予算の改善が本学習でも続くか確認する | 短い比較の実測から教師予算とGPU上限を固定し、別runとして継続。段階評価と全80レビューを行う | 同条件対照との生成改善、既存絶対条件、strong/cached/historical保持条件をすべて判定 | 全条件合格でのみ最終確認候補。未達なら閉鎖し、係数/seed/予算の救済延長をしない |
| 4: 独立学習・全文DEV | 再現性と選定用小標本以外の品質を確かめる | 合格レシピでfresh学習seed43。必要なnative runner/reviewer・型付き証拠接続を実装してから実行。fullDEVと400生成＋長文40を確認 | 両学習seedの結果、fullDEV、全440 rawの内容評価、保持guard | 不合格seedを捨てて選ばない。保護TESTにはまだ触れない |
| 5: protectedTEST・採用 | 選定を固定したうえで最終判断する | 最終条件を封印後、保護TEST20prompt×5mode=100生成と本文評価を実行し全件確認 | 元最終基準の達成・再現/復旧・重み・model card・採否記録 | 全条件達成でBase完成を通知して停止。未達なら不採用と限界を報告 |

段階1は、既存証拠で次の比較を定義できる場合は省略できる。段階0の文書整理をさらに長い調査の入口にせず、一度の選定で比較案または「根拠不足」を出す。まだ次の介入条件は選定・凍結していない。QK等の検索語に一致がないことだけを、新規性や有効性の証拠にしない。

## 予算と時間の扱い

次の数値は研究を際限なく続けないための**提案上限**で、新しい凍結configや実行許可ではない。元の完了実験の予算・品質条件は変更しない。

- 段階0: 既存小記録と必要な原結果だけを調べ、選定メモ1件で完了する。全corpus再scan、全重み再hash、旧GPU再評価は行わない。
- 段階1: 新たなGPU診断が必要なら追加学習0、累積GPU120秒以内を目安に事前固定する。必要性と終了条件を定義できなければ開始しない。
- 段階2: 初回は各条件25M〜100M教師の範囲から、検出したい差と過去の立ち上がりを根拠に1つの予算を事前固定する。途中結果で範囲内を総当たりしない。小予算で比較可能でなければ、その理由と別予算を先に文書化する。
- 段階3: pilotの学習・評価・保存時間を別々に実測して見積もる。2Bや10Bを既定にせず、事前の学習曲線と比較目的から決める。
- 段階4〜5: native方式への必要な実装接続を済ませてから各予算を凍結する。既存fullDEV確認のGPU上限3000秒は旧形式の値であり、型を偽装して使ったり暗黙に増やしたりしない。

参考として、今回の追加1,905,839,805教師は評価・保存込みGPU26,060.094秒（約7時間14分）。この平均から100Mあたり約23分と計算できるが、初回compile・再開gate・固定評価・モデル/shape差を分離した学習速度ではなく、次回の所要時間保証には使えない。完成までの暦日数は未確定。

この選定→必要時診断→pilot→本比較の一巡が不採用で終わったら、いったん結果を報告して停止する。次の仮説を自動的に連続起動しない。品質基準は維持し、達成困難ならその事実と追加比較の価値をユーザーと見直す。

## 品質を判断する順序

探索screenとBase採用条件は別。短いpilotのscreenは実験固有の比較目的に合わせて事前定義するが、最終条件を代替しない。

現行固定80の絶対DEV条件は文法2≥56、一貫性2≥27、適切完結≥27、EOS≥37、反復≤18、empty/role/Unicode失敗0。加えて元policyの相対条件（一貫性差≥8・paired CI下限>0、EOS/反復/文字等の非退行、BPB保持）とstrong/cached/historical参照を各実験の指定どおり判定する。[現行policy](../configs/phase6/base_parallel_residual_review.json)、[適用したreviewer](../scripts/review_base_teacher_decay_2b.py)を参照。

独立seed、fullDEV、最終TESTの各条件も省略しない。最終TESTの停止95%等とDEVの37/80を混同しない。[最終TEST実装](../scripts/run_final_base_test.py)、[採否実装](../scripts/review_final_base_test.py)、[評価契約](evaluation_protocol.md)を維持する。新形式を既存runnerへ渡す接続は未完成であり、文書上の計画を実行可能なcommandと扱わない。

## データ増量・学習延長をどう扱うか

データ供給は一般Web準備12.23B等があり、「公開データが少ない」ことと「目的に有効なaccepted TRAINが足りる」ことは異なる。最新比較は既存accepted2B poolであり、新規データ増量ではない。

増量する場合は同source/長さ/文脈/終端を可能な範囲でそろえて教師予算を固定し、既存poolと比べる。学習延長はTRAINを固定して教師予算だけを変える。両方を変えた実験から量だけの因果効果を主張しない。重複や繰り返し学習を新規教材量として足さない。

これまでの結果は「増量は無効」「学習量は十分」「10Mでは不可能」の証明ではない。一方、今回のBPB改善だけを根拠に量を追加する判断も支持しない。次回は改善する失敗の種類を先に決めて比較する。

## 維持する運用条件

Python3.12.7はすべてuv経由、学習はWSL/Linux disk/RTX4090。実processとGPU lockを確認し、長期jobはPID/boot/start、ledger、logs、全state checkpointを永続化する。元UIは必要なGPU実験中だけ停止し、終端で元10Bへ戻す。関係のない全suiteや旧corpus照合を繰り返さない。

本計画は[ロードマップ](15_project_roadmap.md)のPhase6に対応する。Phase7〜10は長期の構想として保持するが、Base完成後もユーザーが再開するまで着手しない。

今回の見出し更新前の全文は[履歴保存一覧](../reports/investigation/documentation_plan_refresh_20261013/baseline.json)に保存した。本文の2B時間実測は当該Base比較の歴史値で、最新Chat比較の所要時間ではない。
