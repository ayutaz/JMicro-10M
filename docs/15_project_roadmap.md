最新の実状態（2026-10-07 JST）: fresh同10M ReLU²960対SwiGLU640を事前定義・model/trainer/typed評価実装、CPU22と両actual CUDA保存再開・80×1024有限値に合格。actual745144終了・不在、probe22.55秒/検証86更新は科学へ足さない。各300M＋評価の元予測15,027.55秒>固定14,400秒で本学習/品質評価0、この固定FFN比較を終了。短いwall速度差は測定順とsampler待ち/cacheの交絡がありactivation高速化と断定しない。元10B UI745223実alive/APIへ復帰。次は元TRAIN row/stateを保持するCPU入力供給・測定妥当性の限定調査を結果前に定義する。詳細は [autonomous_status.md](autonomous_status.md) 冒頭と [終了記録](../reports/phase6/base_relu_squared_probe_completion.json)。Base未完成・未採用、品質Base完成を通知して停止、Chat/Dialogue/SFT/量子化/展開・pushなし。以下は歴史記録。

最新の実状態（2026-10-07 JST）: 同重み二回decoder案の重複調査を完了。既存13physical/26logicalのgated sharingは実100M・全80まで評価済みで全採用基準未達。whole-stack順序やdamping変更で旧固定recipeを再開せず、新GPU/教師0。architecture文書のLayer Sharing未実装という古い記述を修正。次は未実装ReLU² FFNの一次定義/既存fresh対照/予算を限定調査し、同parameter予算の比較を選ぶか断る。Base未完成・未採用、元10B UI744423のみ稼働。詳細は [autonomous_status.md](autonomous_status.md) 冒頭と [重複調査](../reports/phase6/base_recurrent_compute_novelty_review.json)。品質Base完成で通知して停止、Chat/Dialogue/SFT/量子化/展開・pushなし。以下は歴史記録。

最新の実状態（2026-10-07 JST）: 七条件の同100M負結果を旧snapshotを保持して統合。別token表現幾何仮説をCPU4と実CUDA readonly1.34秒で検証、同TRAIN12unitsの強い類似性markerは0sourceで事前基準未達、この仮説の追加学習は行わず終了。actual744364不在・元10B UI744423へ復帰。詳細/事前条件/終了記録・次の具体的アクションは [autonomous_status.md](autonomous_status.md) 冒頭参照。Base未完成・未採用、品質Base完成を通知して停止、Chat/Dialogue/SFT/量子化なし。以下は歴史記録・既存計画。
最新の実状態（2026-10-07 JST）: Sigsoftmax同100M学習・全日本語/全80内容評価を完了。文法40/一貫性1/適切1/EOS19/反復48/BPB1.001040で全既存品質条件に至らず不採用。actual740850は実終了・不在、元10B UI742417へ復帰。詳細/全80理由/可搬保存・次の具体的アクションは [autonomous_status.md](autonomous_status.md) 冒頭および [終了記録](../reports/phase6/base_sigsoftmax_comparison_completion.json) を参照。Base未完成・未採用。品質Base完成を通知して停止、Chat/Dialogue/SFT/量子化なし。以下は歴史記録・既存計画。
最新の実状態（2026-10-07 JST）: 同Sigsoftmax科学actual740850は実psで稼働確認、元9.94M/100M goldまで進行。実終了・全80採否後の可搬終了commandを追加し、live拒否と歴史80fixtureの同文採点保持/変更拒否を検証。Base未完成・未採用、現候補80は未生成/未読。詳細と次の具体的アクションは [autonomous_status.md](autonomous_status.md) 冒頭参照。科学設定・品質基準を保持、品質Base完成を通知して停止しChat/Dialogue/SFT/量子化なし。以下は歴史記録・既存計画。
最新の実状態（2026-10-07 JST）: Sigsoftmax typed evaluator/永続CUDA probe・science・reviewerを実装、追加CPU15checksと実GPU全state保存再開/最大長有限backwardに合格。同original100M比較actual740850/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start23633274を永続起動。science3,809秒/total4,800秒、元UIは科学中停止。Base未完成・未採用、詳細/実起動証拠/正確な再開条件は [autonomous_status.md](autonomous_status.md) 冒頭参照。品質Base完成を通知して停止、Chat/Dialogue/SFT/量子化なし。以下は歴史記録・既存計画。
最新の実状態（2026-10-07 JST）: 六条件の実100M負結果を旧snapshotを保持して統合。新一条件Sigsoftmax（元10M/追加parameters0/出力確率linkだけ）のmodel/trainerを実装しCPU14と実10M親の全8parity checksに合格。実SigsoftmaxGPU0、typed evaluator/persistent CUDA probe・science・reviewerはまだ未実装。事前totalGPU4800/probe180・既存全品質基準を保持。詳細/事前案/次の具体的実装は [autonomous_status.md](autonomous_status.md) 冒頭参照。Base未完成・未採用、品質Base完成を通知して停止、Chat/Dialogue/SFT/量子化なし。以下は歴史記録・既存計画。
最新の実状態（2026-10-07 JST）: native中間特徴転移100M/別25M hintの学習と全日本語/全80内容評価が終了。文法38/一貫性1/適切1/EOS20/反復42/BPB0.998357で全既存品質基準に至らず不採用。actual737020は終了・実不在、元10B UI738096へ復帰。詳細/全80理由/可搬保存と次の具体的アクションは [autonomous_status.md](autonomous_status.md) 冒頭および [終了記録](../reports/phase6/base_native_hint_comparison_completion.json) を参照。Base未完成・未採用、品質Base完成を通知して停止、Chat/Dialogue/SFT/量子化なし。以下は歴史記録・既存計画。
最新の実状態（2026-10-07 JST）: 同native hint科学actual737020は実psで稼働確認、original18.65M/100M goldまで進行。終端/全80採否後の可搬保存commandを追加し、actual live拒否と歴史80fixtureの採点保持・変更拒否を検証。Base未完成・未採用、現在の候補80は未生成/未読。詳細は [autonomous_status.md](autonomous_status.md) 冒頭参照。科学設定・品質基準を保持、品質Base完成を通知して停止、Chat/Dialogue/SFT/量子化なし。以下は歴史記録・既存計画。
最新の実状態（2026-10-07 JST）: native中間特徴転移の関連CPU10checksと実CUDA全state保存再開/最大長有限backwardに合格し、original100M/別25M hint比較を永続起動。actual737020/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start23344138、run reports/phase6/base-native-hint-comparison-20261007、science4066秒/total4800秒。元UIは科学中停止・終端で復帰予定。詳細/正確な再開条件/可搬launch証拠は [autonomous_status.md](autonomous_status.md) 冒頭参照。Base未完成・未採用、実終端と全日本語/全80内容採否が次。品質Base完成を通知して停止、Chat/Dialogue/SFT/量子化/展開・自動pushなし。以下は歴史記録・既存計画。
最新の実状態（2026-10-07 JST）: 別のnative教師中間特徴転移を事前定義・trainer実装しCPU13checksに合格。元100M hardgold/別25M hint位置、same10M推論/第6block unit-feature/係数1、事前totalGPU4800/probe180。GPU workflowはまだ未実装・新科学GPU0、Base未完成・未採用。詳細・旧fixture失敗の保存・次の実装と実CUDA gateは [autonomous_status.md](autonomous_status.md) 冒頭参照。品質Base完成を通知し停止、Chat/Dialogue/SFT/量子化なし。以下は歴史記録・既存計画。
最新の実状態（2026-10-07 JST）: dense native教師KLの同100M/別25M分布監督・全日本語/全80評価を完了。一貫性2→5/EOS19→46/反復45→25と一部改善したが全既存品質基準では不採用。Base未完成・未採用、科学732636は終了し元10B UI733851へ復帰。詳細と次の具体的アクションは [autonomous_status.md](autonomous_status.md) 冒頭および [終了記録](../reports/phase6/base_native_teacher_KD_science_comparison_completion.json) を参照。品質Base完成を通知し停止、Chat/Dialogue/SFT/量子化なし。以下は歴史記録・既存計画。
最新の実状態（2026-10-07 JST）: 同dense native教師KL actual732636は稼働中。終了後の全80内容評価・可搬保存commandを実装、live拒否と歴史fixtureのみ検証。詳細と次の具体的アクションは [autonomous_status.md](autonomous_status.md) 冒頭参照。Base未完成・未採用、品質Base完成を通知し停止、Chat/Dialogue/SFT/量子化なし。以下は歴史記録・既存計画。
最新の実状態（2026-10-07 JST）: 未学習だったdense native教師KLを別のprospective資源計画で検証し、実CUDA保存再開に合格して同100M比較を起動。科学actual732636、Base未完成・未採用。元3600予算超過とcompile数値失敗を上書きせず、数学的新規性は主張しない。詳細・active job・次の具体的アクションは [autonomous_status.md](autonomous_status.md) 冒頭参照。品質Base完成で通知して停止し、Chat/Dialogue/SFT/量子化には進まない。以下は歴史記録・既存計画。

最新の実状態（2026-10-07 JST）: confidence penalty同100M比較は全評価・全80内容まで終了し、既存品質条件で不採用。Baseは未完成・未採用。詳細と次の具体的アクションは [autonomous_status.md](autonomous_status.md) 冒頭および [終了記録](../reports/phase6/base_confidence_penalty_comparison_completion.json) を参照。品質Base完成を通知して停止し、Chat/Dialogue/SFT/量子化には進まない。以下は歴史記録・既存計画で、古い実状態や停止境界で最新statusを上書きしない。

Base限定・SAM100M学習/全日本語・全80内容評価を完了、不採用（2026-10-07 JST）。Baseは未完成・未採用。

[実終了記録](../reports/phase6/base_sam_comparison_completion.json)・[全採否](../reports/phase6/base_sam_comparison_review.json)・[全80個別理由](../reports/phase6/base_sam_notes.json)。前turnのSAM実装/19CPUchecks・実CUDAgate・永続科学起動b04f313と今turnのcloseout準備0832a02はprogress。今回同actual721383/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start22188114を各実psで監視、科学終端と実不在を確認。元gold100,000,000/17,698更新、Web75M教材20Mstory5M、source EOS657,450/148,625/38,222。digest a1ab0170…・main CE valid102,655,467/physical370,838,917/body405,882,136bytes・full sampler等の全11cachedCE条件がtrue。別会計の同batch第二pass教師評価100,000,000/valid102,655,467/physical370,838,917を記録。新教材100Mやunique corpus増加ではなく、同位置の第二評価。最終checkpoint-00017698.pt/SHAa78317d515cf29490ae979c1505b9a3cf9f05b8d78ab5ade6d8a7950e2ed50e8をWSL保持。heartbeat末尾17,680/99,900,395より実terminal17,698/100Mを使う。

science+全自動評価のGPU2618.292246秒/事前5398秒、probe12.272191秒込み2630.564438秒（約44分）/総7200上限。科学source・rho.05/同batch二回CE・single AdamW/LR1e-5/WD.1/batch48/seed42・native推論は変更せず、再GPU学習/増量/decoder救済0。固定共通DEV256/472,055bytes/122,343tokensのBPB0.999486、意味192=63.542%、JBLiMP331=77.039%、JCQA1119=35.031%。greedy80はEOS12/反復44/Unicode・role・empty0。全80を個別に読みraw SHA3e2bf31e…へ結合したnonblind Codex採点で文法2=22/関連2=23/一貫性2=1/適切完結3。旧on-policyと同prefix/同text/同stopの19例も今回実際に読み同じ採点を維持、旧notesやcached CE80を再採点しない。人間/盲検/独立学習seedの証拠ではなく反復DEVの限界を保持。

cachedCEはBPB0.998487/文法44/関連25/一貫性2/適切2/EOS19/反復45。SAMは一貫性差-1/paired95%CI[-.0375,0]で改善証拠なし、EOSは7件減、反復1件減だけで品質を改善としない。strong stagedの一貫性23/EOS76/反復2に対し差-22/CI[-.375,-.175]。matched/strong/absolute/historicalWebの全採用条件へ至らずeligible_for_final_Base_validation=false。文法56/一貫性27/適切27/EOS37/反復18以下・歴史WebBPB上限と旧数値7失敗を維持。この固定SAM条件を終了しrho/adaptive/period/optimizer/LR/親/data/batch/decoder/capで救済しない。この一保守的LR・成熟親からの結果で全SAMや新しいデータ/学習量の無効を断定しない。

初回 frozen review --templateは全stateとhistoryの読込後にstdlib mathのimport漏れによるNameErrorで終了、notes/品質判定は未作成。[修復記録](../reports/phase6/base_sam_reviewer_import_repair.json)へ実command/error/stageを保存。original reviewer/科学source/config/policy/resultsの凍結bytesを変更せず、review_base_sam_v2.pyから元moduleへstdlib mathだけを供給。既存全state/history・有限値/rho・同byte/日本語/all80・matched/strong/absolute/historical checksを元codeで実行し、未採点template→全80理由→採否まで正常終了。品質基準や許容差を変更した修復ではない。complete_base_sam.pyはV2/元reviewer/resultのSHAとimport-only flagsも確認して修復source/記録をarchiveへ含めた。科学をやり直さず新GPU0。

元10B WebUIactual722575/同boot/start22450363を実alive確認、HTTPは元親410f975d…/10,000,007,168/busy=falseへ復帰。科学実PIDなし。終端/fullstate/全評価/notes/予算/元UI actual/APIをcloseoutが確認し43text/106,105,504bytesの可搬証拠を保存。gzip46,390,369bytes/SHA37ffb5c5f6aaee3ddd38dacc305bd3a6085845010b1c9119bede3f5cc41c114eをWindowsへコピーし一度照合。tensor/corpusはarchiveに含めずnative checkpointsを保持。

次の具体的アクション: 今回の負結果を失敗経路の参照へ加え、同SAM tuning・既失敗data/親/保護objectiveを繰り返さず、未検証の独立したBase比較を一つだけ目的・比較対象・測定予算・終了条件付きで結果前に定める。資格ある実候補のみ独立学習seed/full DEV/protected final TEST/adoptionへ進む。今回それらは0、Baseは未完成・未採用で完了時刻を確約しない。最新境界を保持し品質Base完成を通知して停止、Chat/Dialogue/SFT/量子化/展開・自動pushなし。Python3.12.7はWSL uv、意味のある検証済み変更をlocalcommit。今回実科学終端/全内容採否/可搬保存のprogressでgoal completeではない。以下は過去の履歴。

Base限定・同SAM科学jobを実監視し、全内容評価後の可搬closeout commandを準備（2026-10-07 JST）。Baseは未完成・未採用。

前turnは実SAM実装/CPU19checks/実CUDA保存再開・有限値/同100M科学起動をb04f313へ保存したprogress。今turnもrequired docs/worktree・actual721383/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start22188114を実psで確認。snapshotは1,320更新/7,441,900original gold/100M、CE2.630862有限、累積201.311秒/凍結5398秒、latestcheckpoint-00001250.pt。元goldとは別の同batch第二pass教師評価も同じ量で進み、二倍の新教材量とはしない。最新heartbeat/metricsはWSL reports/phase6/base-sam-comparison-20261007を参照。新設定/再取得/重複GPUjobなし。

complete_base_sam.pyを追加しWSL uvのCLI helpを確認。実科学終了・同original100M/別会計repeated100M・全評価/全80raw-bound個別notesと凍結全quality gates・元10B UI actual/API復帰が揃った後だけ、科学text/source/metrics/evaluationのarchive/manifest/終了記録を保存する。学習は現在稼働中なのでcloseoutをまだ実完了させず、CLI helpを終端/有用品質/採用/UI復帰の証拠にしない。学習・評価・既存品質基準の凍結sourceは変更しない。

次はこのexact PIDとcompletedcheckpointを監視→同100M＋別会計第二pass100M/full state終端→日本語192/331/1119・共通DEV256・native80→全80を個別に判定して採否/可搬保存。資格ある候補だけ独立学習seed/full DEV/protected final TEST/adoptionへ進む。品質Base完成を通知し停止、Chat/Dialogue/SFT/量子化/展開・自動pushなし。Python3.12.7はWSL uv、localcommitのみ。今回はcloseout実装/実job監視のprogressでgoal completeではない。以下は過去の履歴。

Base限定・未検証のSAM二回CEを実装、CPU19checks/実CUDA全state保存再開に合格、同100M比較を永続起動（2026-10-07 JST）。Baseは未完成・未採用。

前turnはon-policy100M/全日本語・全80内容/不採用の終端と可搬保存を1530346へlocalcommitしたprogress。今回required docs・既存failure_route_synthesis/Muon/on-policy/gradient precision結果と実processを確認。最新on-policyの一貫性3/80、反復46/80は既存条件未達、gold-prefixKDのeager予算/compile数値失敗も閉じたまま。既存optimizer/objectiveの検査ではAdamW/Muon/contrast/teacher/anchor/dropout/smoothingはあるがfull-parameter二回SAMは未実施。新sourceの取得・旧2B corpus全scan・Tokenizer再訓練なし。

[結果前の一条件案](../reports/phase6/base_sam_proposal.json)。元10B親410f975d…・同10,001,152パラメータ/4096codec、同TRAIN source Web75M教材20Mstory5M・元100Mgold/seed42/batch48/freshAdamW1e-5/WD.1constantを維持。同一ids/targets/masksの原CEで全gradientを求め、global L2半径rho.05の重み摂動→同batchで第二CE/backward→元FP32重みをsubtractでなくexact copy復元→第二gradientをclip1して単一AdamW更新。rho/adaptive/period/LR/source/親/batch/decoder/予算の救済探索はしない。元gold/bytes/EOS/digest/samplerは一回、追加同位置100M教師評価と追加valid/physical inputはSAM辞書へ別会計、新教材100Mとはしない。teacher/追加parameters/Chat/SFTなし。

[原SAM論文](https://arxiv.org/abs/2010.01412)・[言語モデル研究](https://arxiv.org/abs/2110.08529)・[著者実装](https://github.com/google-research/sam)を確認。摂動近傍のCEも低くする最適化としての独立仮説であり、言語論文の大きなモデル・task finetuning/choice/QAを日本語10M自由生成の成功証明や厳密再現にしない。sharpnessが現在の反復の原因と実証したわけではない。

base_sam_trainer.py/生成した独立probe/runner/reviewer/persistentPSを実装。CPU9checks/4.66秒は独立二次式の摂動・第二gradient/未更新exact復元、第二pass例外cleanup、元gold全stream/counters/tiedweight保持、continuous4vs2-save-resume2全state/history、wrongrho/repeat/Adamstep/samplerの拒否、未完stepの保存/継続拒否。runner10checks/.80秒は全32実timingと固定17698更新forecast、部分/非有限/変更予算/changed token digest/fullsamplerの拒否。PS構文/CLI help/preflight成功。CPU fixtureはGPU学習や有用品質の証拠にしない。src/jmicro/model.pyの凍結bytes/hash、旧数値7失敗は保持。

[実CUDAgate・launch記録](../reports/phase6/base_sam_probe_launch.json)。probe config SHA2e84490bec81ffd3b4ec4b1fe4167f9a7d106b06de5adbb9e6c0a6f922ca0bf9、Windowsworker36812/actual720895/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start22179810はcomplete・実ps不在。初期4checks、CUDA continuous4対saved2+2のkind/spec/binding/lineage/modelconfig/weights/Adam/scheduler/RNG/fullsampler/gold/SAM全12keysとfinite/history/source/controlの全16checks一致。47検証更新/273,521original gold/250,313 repeated評価は科学予算に加えずprobe重みを破棄。all48x1024/stride512の二回stressはoriginal/repeated各24,576位置・optimizer0、CE2.266642/摂動CE2.432005/firstgrad3.162025/secondgrad3.510246・摂動L2.05000000447有限、exact重み復元true、peak10,745,064,960bytes。短いshapeだけの容量証明にしない。

probe GPU12.272191秒/180上限。postwarmup32二回stepの全平均×exact17,698更新×1.3＋900評価余裕をceilしscience5398秒、probe込み5410.272秒で事前total7200秒内。median29,514.387872 originalgold/秒は参考値でforecastへ使わず、追加第二pass computeを元CE学習量に混ぜない。これは別の二回SAM比較の事前予算で、旧KD3600秒条件を広げたものではない。

science config SHA f8c956f16d7cb00c77ce8208191eb9bf2532f5766745c303b79f6591498414f2と従来matched/strong/absolute/historicalWeb全品質policyを学習結果前に凍結。Windowsworker34232からactual721383/同boot/start22188114を起動し実ps/heartbeatでrunningを確認。reports/phase6/base-sam-comparison-20261007、launch snapshot180更新/1,017,618original gold/CE2.724817有限、latest位置はこのsnapshot以後増加。250完了更新checkpoint・20更新heartbeat・PID/boot/start・ログ・optimizer/scheduler/RNG/sampler/counters/SAM状態を保存。restart command scripts/run_base_sam.ps1 -Worker、実同PID不在と有効completed checkpointを確認した場合のみ同累積5398秒内で再開。科学中の元10B UIは停止、終端で元親へ自動復帰予定で、今は復帰完了としない。cachedCE100MのGPU再学習/全80再採点0。

可搬gate/source/config/実結果/launch snapshot bundle162,014bytes/SHA66117cf809ac330f07c4fc2d1ebfc8d6da78d61770489e95289a857dd4210094をWindowsへ保存し一度照合。probe tensors・科学checkpoints/metricsはWSL保持。科学100M終端/全日本語/共通DEV256/native80・個別内容採否はまだ未完、独立学習seed/full DEV/protected final TEST/adoption0。

次はこのexact科学PIDとcompletedcheckpointだけを監視し、同100M＋別会計repeated100M/full state終端→全日本語/共通DEV256/native80→全80を個別に読んで凍結全gateを適用。稼働中に無関係な研究・重複GPU・新設定を始めない。資格ある候補だけ独立学習seed/full DEV/protected final TEST/adoptionへ進む。最新境界を保持し、品質Base完成を知らせて停止、Chat/Dialogue/SFT/量子化/展開・自動pushなし。Python3.12.7はWSL uv、検証済み変更をlocalcommit。今回実装/CPU・CUDAgate/実科学起動のprogressでgoal completeではない。以下は過去の履歴。

Base限定・on-policy教師feedbackの100M学習・全日本語評価・全80内容判定を終了、不採用（2026-10-07 JST）。Baseは未完成・未採用。

[終了記録](../reports/phase6/base_on_policy_teacher_comparison_completion.json)・[採否](../reports/phase6/base_on_policy_teacher_comparison_review.json)・[全80個別理由](../reports/phase6/base_on_policy_teacher_notes.json)。actual718057/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start21898450はcomplete・実ps不在。元hardgold100,000,000/17,698更新、Web75M・教材20M・story5M、元token digest/full sampler/全11cached CE一致を終端で確認。CE valid102,655,467/main physical370,838,917/body405,882,136bytes。別会計の現student rollout1,106回/8,784系列/279,734 distribution positions（本文279,587/EOS147）、各rollout/student scoring/teacher valid420,278・physical421,632。教師全重み不変/eval-no-grad/student-only optimizer全true。初回probe21.751486秒＋science/evaluation2187.343045秒＝2209.094531秒、science3562/全7200上限内。最終checkpoint-00017698.pt/SHA6e098877…をWSLに保持。staleheartbeat17,680より実terminal17,698を採用。

固定共通DEV256/472,055bytes/122,343tokensのBPB0.996386、意味192=64.583%、JBLiMP331=77.946%、JCQA1119=35.210%。greedy80はEOS22/反復46/Unicode・role・empty0。全80を個別に読みraw SHA64c591e3…へ結合したnonblind Codex採点で文法2=30/関連2=24/一貫性2=3/適切完結6。花・虫の擬人化をそれだけで失敗にせず、統語・関連・一貫性・EOS後の適切完結を別判定。独立人手/盲検ではなく、反復して使うDEVの限界を維持。

cached CEは再GPU/再採点せずBPB0.998487/文法44/関連25/一貫性2/適切2/EOS19/反復45を保持。一貫性差+1/paired95%CI[-0.025,0.0625]で改善の証拠不足、反復は1件増。strong stagedは一貫性23/EOS76/反復2で、差-20/CI[-0.35,-0.15]。matched/strong/absolute/historicalWeb全採用条件へ至らずeligible_for_final_Base_validation=false、この固定条件を終了。文法56/一貫性27/適切27/EOS37/反復18以下と歴史WebBPB上限を緩めない。独立学習seed/full DEV/protected final TEST/adoptionは今回0、Base完成や全五目標達成を主張しない。alpha/温度/rollout頻度/prefix長/decoder/親/LR/量/batch/上限の救済探索なし。

complete_base_on_policy_teacher.pyが終端・実history/state/source/refs・全評価/notes・予算・元UI actual/APIを確認して比較記録と44text/118,911,276bytesのarchiveを保存。gzip47,127,300bytes/SHA667197519458eda2ca4b4f3de9a94c9865348a8ad2c48b1793c175b17de56370をWindowsへコピーし一度照合。tensor/corpusはarchiveに含めずWSLへ保持。元10B WebUIactual719212/同boot/start22117643、HTTP親410f975d…/10,000,007,168/busy=falseへ復帰確認、新科学GPUjobなし。注記書込みの初回PowerShell配列式をID guardが拒否し未採点templateを保持、括弧を修正して全80保存後に凍結reviewerが正常終了した。科学設定や品質閾値の変更なし。

最新境界を保持: 実評価合格・採用までBaseに限定して進め、完成を知らせて停止。Chat/Dialogue/SFT/量子化/展開・自動pushなし。次の具体的アクションは今回の負結果を既存の失敗経路一覧へ反映し、既失敗の設定探索を再開せず、未検証の独立したBase比較について目的・比較対象・測定予算・終了条件を結果前に定めること。有望な候補だけ独立seed/full DEV/protected final TEST/adoptionへ進む。現段階で完了時刻は確約できない。Python3.12.7はWSL uv、検証済み変更をlocalcommit。今回は実科学終端・全内容判定・採否・可搬保存のprogressで、goal completeではない。以下は過去の履歴。

Base限定・同一科学jobを実監視し、全内容判定後の可搬記録commandを準備（2026-10-07 JST）。Baseは未完成・未採用。

前turnは新on-policy teacher実装/31関連CPUchecks・実CUDA32vs16+16/131検証更新/実科学起動をb09dfe4へ保存したprogress。今turnもrequired docs/worktreeを確認し、actual718057/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start21898450の同科学jobをpsで稼働確認。2,740更新/original15,470,284/100M gold、CE2.5784158707有限、累積351.376秒/凍結3562秒、最新完了checkpoint-00002500.ptを確認。重複job/新研究/設定変更なし。この数値は監視時点のsnapshotで、最新heartbeat/metricsはWSL run job.jsonを参照。

complete_base_on_policy_teacher.pyを追加しCLI helpをWSL uvで確認。実科学process終了・全評価/all80 raw-bound notesと採否・同元gold stream/fullsampler・測定上限・元10B UI actual/API復帰が揃った後だけtext/source/metrics/evaluationのarchiveとmanifest/完成比較記録を保存するcommand。aux distribution位置/生成input会計/教師不変checksをgold100Mとは別に記録。現在本学習は稼働中なのでarchive commandはまだ実完了させておらず、CLI helpを品質・終端・UI復帰の証拠にしない。

次はこのexact jobの学習と評価完了を待ち、80件を個別に判定→凍結matched/strong/absolute/historicalWeb全gate→終了記録/可搬保存。資格ある実候補だけ独立学習seed/full DEV/protected final TEST/adoptionへ進む。Base完成を知らせて停止、Chat/Dialogue/SFT/量子化/展開なし。Python3.12.7はWSL uv、localcommitのみ、pushなし。goal completeではない。以下は過去の履歴。

Base限定・現在生成したprefixへのnative教師feedbackを実装し、実CUDA保存再開に成功、100M科学学習を開始（2026-10-07 JST）。Baseは未完成・未採用。

[実gate・起動記録](../reports/phase6/base_on_policy_teacher_probe_launch.json)・[結果前の修正済み案](../reports/phase6/base_on_policy_teacher_proposal_v2.json)。前turnのgold-prefix KDのeager3600秒予算失敗とcompiler数値失敗は5b65dbcへ保存したprogress。今回保存済みsynthesis/source-order/gradient-precision・両KD終了・context-mixing終了を確認。次の一条件は、現studentがTRAIN短文の頭からsamplingしたprefixに未採用native staged教師fb43f261…のfull4096予測を与える。goldを変更したprefixにそのまま与える旧mixing、反復UL/localDPO、未学習gold-prefix KDとは異なる実学習機構。[GKD一次論文](https://arxiv.org/abs/2306.13649)を参考にした仮説で、日本語10Mの成功証明や論文の厳密再現ではない。

同元410f親・original100M gold/Web75M教材20Mstory5M・同sampler/batch48/seed42/freshAdamW1e-5WD.1constant・originalCE/body/EOS/mask/physical main入力を保持。16更新ごとに同main batchの先頭最大8教材/storyのoriginal document headsだけ使い、BOS＋最大16bodytokensから現studentがT1/32tokensまでsample、0/1/2/4/5/6/7抑制・EOS3停止。元gold CE backward後、同pre-update studentでno-grad native KV/math BF16生成、教師とstudentを同生成prefixでscoringしgenerated位置だけmean forwardKL(T1/coefficient1) backward、単一clip/Adam更新。教師eval/no-grad/不変・optimizer student-only、teacher重みをstudent checkpointへ複製せずSHA/lineage保存。gold/input全会計と追加rollout/scoring/teacher/distribution位置は別に保存、新data0・Chat/SFT0。元model.py/Tokenizer/旧2Bの再scanや再訓練なし。

初回proposal作成時の短縮completion filename誤りを保存前に修正。CPU初版ではserialized BOS位置0と最初body位置1を取り違えtarget_first0を要求し全auxをskip、3testsが拒否した。original proposal/failed XMLを保持し、意図した既存original_document_first_window/target_first1へ修正をV2案へ明記。GPU/品質を見てsource/settingを選び直した修正ではない。関連CPU20checks/25.03秒＋rare rollout込み予算4checks/.74秒＋runner/history7checks/3.27秒、両CLI help/PS構文成功。fixtureは実品質証拠ではない。

probe config SHA0269e8d90c7ee4659f8ce4d7fd29563cfa06c68c99dc86d67a9ab2677b823aaf、Windowsworker35464からactual717260/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start21880729はcomplete・実不在。CUDA32対saved16+16はscheduled rollout2回を含む全12state/RNG/生成列/history/source/fullsampler/committed checksすべてtrue。教師全重みはstress/continuous/resume/timingで不変。最長gold48×1024＋aux8×49上限のBF16 backwardはCE2.271785/KL.606474/gradnorm4.283653有限、peak11,034,152,960bytes（aux実max8×48より1token大きい診断のみ）。131検証更新/762296originalgold/1470distribution、capacity24576gold＋256auxは別、すべてscienceへ足さずprobe重みを捨てる。実21.751486秒/事前180秒。

warmup3除外32の合計3.702359秒には実rollout更新2回/.682260秒と.641807秒を含む。普通step中央値だけで見積もらず、cached exact17698updates×合計32/32×1.3＋900評価余裕をceilして科学予算3562秒、probe込み3583.751486秒。追加autoregressive教師feedbackという別objectiveに先に固定したtotal7200秒へ入り、旧gold-prefix KD3600秒条件を拡張/再開したものではない。runner/reviewer/persistentlauncherと全既存matched/strong/absolute/historicalWeb policyをscience結果前に凍結。cachedCE100MはGPU再学習/再採点しない。

science config SHAedd40c9cf7f69ee8677310f953183ecc10bd4f961388c1b25739c1fb7220fdb4、Windowsworker34264からactual718057/同boot/start21898450、reports/phase6/base-on-policy-teacher-comparison-20261007で実runningを確認。launch snapshotはoriginal2,829,899/100M gold、有限lossで増加。全sampler/optimizer/scheduler/RNG/aux/digestを250完了更新ごと保存、20更新heartbeat・PID/boot/start/実ログ/累積予算を保持。再開commandは scripts/run_base_on_policy_teacher.ps1 -Worker、実同PID不在・有効完了checkpointを確認した場合のみ同累積3562秒内へ再開。科学job中の元UIは停止し終端で元10Bへ復帰予定、復帰完了をまだ主張しない。

可搬text archive755290bytes/SHAc3a7117654182fce7f2ac3a116963f1ac10617d2dbcc034fa3c64893c57ea6d6をWindowsへ保存し一度照合。probe tensors・本学習checkpoints/進行中metricsはWSLに保持。今回GPU品質生成/全80判定/独立seed/full DEV/protected TEST/adoptionはまだ0。次はこのexact科学jobだけを監視し、同100M終端/全source/fullstate・全日本語/共通DEV256/native80を完了→全80を個別に読み凍結全品質gateを適用する。稼働中に無関係な研究・重複GPUを開始しない。資格ある候補だけ独立学習seed/full DEV/protected final TEST/adoptionへ進む。

最新ユーザー境界: 評価基準を満たすBaseの採用が終わったら知らせて停止し、Chat/Dialogue/SFT/量子化/展開には進まない。現在Base未完成・未採用。Python3.12.7はWSL uv、意味のある検証済み変更をlocalcommit、自動pushなし。今回実新teacher-feedback実装/CPU+CUDA gate・永続science起動はprogressで、goal completeではない。以下は過去の履歴。

Base限定・同損失コンパイル性能案は実勾配差の事前基準に未達で終了（2026-10-07 JST）。Baseは未完成・未採用。

[実終了記録](../reports/phase6/base_native_teacher_KD_compile_completion.json)。前のeager版は保存再開・有限値に成功したが、元3600秒予算へ収まらず未学習。その同teacher/gold/shape/lossを維持する別の有限性能案だけ実装した。base_native_teacher_KD_compiled.pyはoriginal right_padded_hiddenをinductor/default/dynamic=True/fullgraph=Trueで一度compileし、bare student/teacherとtied vocab・保存keyを保持、stepのdispatchをfinallyで復元する。実行recipeをspecへ保存し異なるrecipe/eager状態のresumeを拒否。凍結model.pyのSHA298bbac7…や既存科学sourceを変更しない。関連CPU15checks/4.22秒、CLI help/PS構文・preflight成功。CPU mockは実CUDA support/速度/品質の証拠ではない。

config SHA f688503fc84f3b018f40c043605267953fef368b081d600bf52bb713b03a4fa0、永続Windowsworker30416からactual716109/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start21821569を実行し、numeric_webで終了・ps不在を確認。新sourceをdrawせず既存fixedTRAIN24のWeb8原文を使用、shape8×262/849gold位置、optimizer更新0。元BF16 eager CE2.8211193085対compiled2.8215847015、絶対差0.0004653931は事前0.005以内。教師logits相対L2=.0059370348も事前.01以内。しかし全student gradient cosine=.9998670119は事前.9999未満、relativeL2=.0163123451は事前.01を超え、この一条件を終了。Web教師forwardは数値確認だけでWeb KD科学教師へ再分類していない。

teacher cold forward22.498390秒、student cold forward29.987588秒（backwardコンパイル等は全wall会計へ含む）。新probe54.533804秒＋旧12.282180秒＝累積66.815985秒/元180秒、総3600秒は拡張しない。初期7checks（parent/teacher全重み、teacher eval/no-grad、両tied vocab、bare保存key、student-only optimizer）は全true。textbook/story数値・48×1024stress・compiled CUDA連続4vs2+2・32timings/速度forecastは未実施で、欠損をpassとしない。compilerがこのshapeで動いたことだけでは科学使用資格にならない。mode/backend/dtype/buckets/batch/shape/capの再調整、eager fallback、100M科学、品質生成採点は0。従来eager CUDA成功と旧数値7失敗・全品質基準を保持。この失敗はcompiler許容差条件の結果でありnative teacher KDの品質や全torch.compileの無効の証明ではない。

実terminal/source/refs/事前条件・欠損gate・science config不在・元UI actual/APIを終了commandが確認。可搬text archive22673bytes/SHA15e59cb04313333b5c1d91f6dbe6da8782d9588c2ffe2a67b67afa1e0cbba554をWindowsへ保存し一度照合。元10B WebUIactual716463/同bootのserver.json identityを保存、APIは元親410f975d…/10,000,007,168/busy=falseを確認。新科学GPUjobなし。

次の具体的アクション: native KDのeager予算終了と今回compile数値終了を保持し、既存base_failure_route_synthesis.json・source_order_condition_comparison_completion・base_gradient_precision_completionの保存済み結論と今回2記録を整理して、未検証の独立したBase学習比較を一つ選ぶ。同compiler tuning/既失敗sourceの再取得・高コスト原因assayを繰り返さず、次の実学習条件と測定予算を結果前に定める。品質が有望な実候補だけ全matched/strong/absolute/historicalWeb・独立学習seed/full DEV/protected final TEST/adoptionへ進む。

最新ユーザー境界を保持: Baseの実全評価合格・採用が終わったら知らせて停止。Chat/Dialogue/SFT/量子化/展開は開始しない。現在Base未完成・未採用、今回独立seed/full DEV/protected final TEST/adoption0。Python3.12.7はWSL uv、検証済み変更をlocalcommit、自動pushなし。今回は実compiler実装/CPU checks/一度のCUDA数値・条件終了/可搬保存のprogressで、goal completeではない。以下は過去の履歴。

Base限定・native教師KDの実CUDA保存再開/有限値は成功、eager版は時間予算で本学習未開始（2026-10-07 JST）。Baseは未完成・未採用。

前goal turnはOpenJAの実group61/50k準備・TRAIN127,409bodytokens/事前1M未達の固定条件を終了し3331efaへ保存したprogress。今回はrequireddocs/AGENTS/実worktree/全processを確認し、[先に定めたnative教師案](../reports/phase6/base_native_teacher_KD_proposal.json)を実装。base_native_teacher_KD_trainer.pyは元100MhardgoldCE/body/EOS/mask/input/source/byte/digestを保持し、同4096/同10,001,152モデルの未採用strongstaged教師fb43f261…をeval/no-gradで使い教材/storyだけfullvocabT1/coefficient1のKLを同全gold分母へ加える。teacher initializationがstudent RNGを進めないよう復元、teacherをoptimizer/state重みへ混ぜず immutable SHA/spec/lineageを保存し、元Gold countersとsoft25M別会計、oldCE state relabelを拒否。src/jmicro/model.pyの凍結混在改行/hashは変えていない。

[実CPU10checks](../reports/phase6/base_native_teacher_KD_tests.xml)/3.73秒に成功。KLの独立式/gradient/全gold分母/teacher stopgradient、RNG/両tiedvocab/optimizer studentonly、source/masks/digest/fullsampler一致・short限定soft/EOS/teacher全weights不変、実saved2+2対continuous4の全state/history、wrong teacher/temperature/kind/counterの拒否を確認。fixtureはGPU訓練/品質改善の証拠ではない。PS構文/preflight後に元config SHAe270f7b2392505030c206530db6aeaacad4c3628f8327f9fc568caa836f8aedcを凍結、永続Windowsworker34004からactual715261/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start21753198を起動。

初版は実35updatesのtiming後、cached payloadのJSON readerへstrを渡すコードのAttributeErrorでworstshape前に終了。GPU7.349648秒、source/config/job/全35historiesを保存。V2は既存pathをPathへ変換する修正だけで未完capacity/resume/controlを完了、35timingsを再実行せず旧消費時間を元180/3600秒へ加算。config SHAf840e6774e7ebb0666dccf1fa678e3f58482196992649d67a0e89bb79df8f449、Windowsworker35572、actual715491/同boot/start21761013はcomplete・実不在。初版timing後のteacher-equality boolは失敗時に未保存なので捏造せずmissingと記録。別の初期/長stress/continuous/resumedで全teacher weights不変/no gradを実確認した。

[実終了記録](../reports/phase6/base_native_teacher_KD_probe_completion.json)・[全結果](../reports/phase6/base-native-teacher-KD-probe-v2-20261007/result.json)。V2の連続4対saved2+2はkind/spec/binding/lineage/config/model/Adam/scheduler/RNG/fullsampler/counters/KDの全12key、有限全state・timingを除く全history・元goldstream・同fullsampler・short限定teacherの全条件一致。全47probe updates/273,521originalgold positions/62,601distribution positionsは検証用、scienceへ足さない。既存原TRAIN1024/512stressを48行並べた人工all-KD上限形状でCE2.271785/KL0.333067/gradnorm3.975021が有限、peak13,047,812,096bytes、optimizer0・diagnostic24,576positions別。Webstressをshortsource科学教師へ再分類したものではない。固定TRAIN/旧2Bの再scan・新data/Tokenizer再学習0。

実probe累積12.282180秒（旧7.349648＋追加4.932533）/事前180秒。元35からwarmup3を除く実32updatesのmedianは41,557.727582 originalgold positions/秒。事前のceil(100M/median*1.3+900)は4,029秒、probe込み4,041.282秒で元総上限3,600秒を超えscience_budget_eligible=false。このforecastは初期32の測定と固定margin/評価余裕で、実100M所要時間ではない。上限を広げずeager版の科学予算条件を終了、本学習/GPU品質評価/新生成採点は0、モデル精度の負結果とも成功とも主張しない。未凍結/未起動のscience-runner prototypeは取り除いた。complete_base_native_teacher_KD_probe.pyが実終端・全source/refs・初期失敗/再利用記録・全forecast/caps・science config不在・元UI実identityを確認。text archive251,428bytes/SHAedb4f17ee83cdb3869ab81a447f5a2a664356083f67a499398e27e3d2d7bf9f7をWindowsへ保存し一度照合。検証tensor checkpointsはWSL保持。

元10B WebUIはactual715555/同boot/start21761903へ復帰、元parent410f975d…/10,000,007,168を維持。この実eager予算条件と全品質条件/旧数値7失敗を保持したまま、次の具体的アクションを[別の有限コンパイル性能案](../reports/phase6/base_native_teacher_KD_compile_proposal.json)へ固定。original right_padded_hiddenだけtorch.compile/inductor/default/dynamic=True/fullgraph=Trueで実装し、数学的損失/teacher/gold/物理shape/grouping/seed/batch48を変えず新保存重みにOptimizedModule名を混ぜない。[PyTorch一次API](https://docs.pytorch.org/docs/2.14/generated/torch.compile.html)はdynamicのspecializationが残る可能性とfullgraph失敗を説明しており、実モデルsupport/速度は未確認。別のパラメータ探索やteacher/量/shape/capの救済ではなく、同処理の演算実装の一性能比較。旧12.282秒を含めprobe180秒/総3600秒を維持、compilation/cold/recompile costを全計上し、一度の実CPU/実CUDA数値/全state/shape/速度確認で決める。失敗時にmode/backend/dtype/buckets/batchを調整しない。

現在compiled版は未実装/実GPU0。数学的同値を浮動小数点のbitwise一致と混同せず、結果前に別compiler guardを明記（既存TRAIN24各genreの同BF16loss差<=.005・全student gradientcos>=.9999/relL2<=.01・teacherlogitsrelL2<=.01）。旧数値7失敗をこの許容値で合格へ替えない。コンパイル以外の全source会計/control・actual continuous/resume同一性と全Base品質gatesを維持、実forecastが残予算へ入った場合だけscience runner/reviewerを用意して同100Mを開始する。sourceや高コスト原因assayの再取得/再試行を続けない。

Baseはまだ未完成・未採用、科学品質/独立学習seed/full DEV/protected final TEST/adoptionは今回未実施。資格ある実候補のみ最終検証し、Base完成を通知して停止。Chat/Dialogue/SFT/量子化/展開なし。Python3.12.7はWSL uv、検証済み意味のある変更をlocalcommit、自動pushなし。今回は実native教師KD手順/finiteCUDA/保存再開/測定予算判断/可搬記録のprogressで、goal completeではない。以下は過去の履歴。

Base限定・国会発話の一固定groupを実取得・準備し量不足で終了、次は同構造の既存教師分布の比較（2026-10-07 JST）。Baseは未完成・未採用。

前goal turnはCC0実2文/47TRAINtokens、2008PD例文のactive本文encoding失敗を実測・終了しfc402a0へ保存したprogress。今回はrequireddocs/AGENTS/実worktree/processと既存public_prose_registry_reviewを確認。OpenJAは以前「短い物語」仮説と文体が違うためmetadataだけで未選定、本文取得/学習失敗済みsourceではなかった。今回はhuman parliamentの完結した説明発話として明示的に別の仮説を[有限source案](../reports/phase6/openja_base_source_feasibility_proposal.json)へ先に固定した。物語へ再分類せず旧判断を保持。[NDL API一次資料](https://kokkai.ndl.go.jp/api.html)・[現コンテンツ規約](https://www.ndl.go.jp/sitepolicy/terms)・[配布者card](https://huggingface.co/datasets/zait-ai/OpenJA)を確認。配布者のCC-BY4.0 compilation/cleaned表示は個々の発言の包括権利・品質の独立証明ではないと区別し、原speechURL/帰属/限定文体を保持。外部公開なし。

[footer実測](../reports/phase6/openja_base_footer.json)は以前pin済みzait-ai/OpenJA revision f4e26dbf5abd705290ac68e1756d0e7b7a30db9d のopenja.parquetをexact206 Rangeで取得。実429,490bytes/3requests/3.779427秒、source本文0、3,244,877rows/65groups/17fields。宣言fullblob SHA1c975ff6a7f135e1bf38a5c1f8865e0599887ece39787449e1b24ba46bfaef7e/1,858,885,357bytesを保持するがfullhash独立検証とはしない。元range helperを変えず、incorrect206を大きなbodyを読む前に拒否。original footer/header bytesのdigestを後続に結合した。

実CPU4checks/0.06秒（verified speaker-headerだけ除いたexactUTF8span/nativecodec/構造ID除外、同meeting splitとexactbodyidentity、長いbodyをtruncateせず固定DEV/role/未完除外、TRAIN限定uniform80/no duplicate）に成功。本文を読む前に実compressed列sizeで96MiBへ入るgroup集合からseed2026100753で一つ、group61/50,000rowsを固定、config SHA8804766e628e1f2dcb09173393ad4d4a84ac6b3a399ec0627502e983abbd8b69。追加selected4columns text/id/issueID/speechURLのみ取得。実29,061,026bytes/network10.487636秒/事前120秒、CPU0.684993秒/事前90秒。rawpartialrangeと原文splitはWSL /home/aihub_ubuntu/jmicro-data/phase6/openja-base-source-20261007 に保持。全1.86GB download・旧2Bscan・Tokenizer再学習なし。

[実準備](../reports/phase6/openja_base_source_preparation.json)・[実終了](../reports/phase6/openja_base_source_completion.json): actual714835/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start21705274はcomplete・実不在。speakerheader以外は原文字/punctuationを変えず、完全body10..256chars/6..64tokens/JP終句/元codecbyte一致/既存DEVprefix>=12除外で一pass準備。meeting-family90/5/5split、exactbody重複は全splitで一度だけ保持。TRAIN4,133発話/215meetings/127,409bodytokens（serialized135,675）/581,848bodybytes、事前最低1Mbodytokens未達、eligible=false。固定TRAIN80seed2026100755の原文/IDs/span/pinは準備時に凍結したが、全80内容判定は未実施、量未達を品質合格へ替えない。80発話は独立80会議とはしない。50kの一group結果で全OpenJA量・品質やhuman Japaneseの有効性を否定しない。

この固定group/量条件を終了し、他group/revision/filter/seed/threshold/epoch/全fileで救済せず科学GPU/optimizer更新0。初版と同原文byte一致を維持、canonicalizationによりbyteが変わる2,040件も黙って書換えず除外として報告。complete_openja_base_source.pyは実終端/全凍結source・refs SHA/全50k会計/samplebinding/partialpin・preparedstatを確認。15textのgzip48,320bytes、SHA813a16efdaf9bdfd33cac6a75fd59d4b8ab8b2fef2cf1aee8dbbe9968b29a97aをWindowsへ保存し一度照合。元10B WebUI713143をsourceCPU中停止せず、新科学GPUなし。

次の具体的アクションは[同構造native教師KD案](../reports/phase6/base_native_teacher_KD_proposal.json)のtrainer/runner/persistentlauncher/reviewerを実装し、実CUDA full-save-resume・最大安定batch/有限値・速度/上限を測ること。既存strongstaged native10M（fb43f261…、文法65/一貫性23/EOS76/反復2、WebBPB1.133613で未採用）を凍結教師として、元10B410f975d…の同100MgoldCE/Web75M・教材20M・story5Mへ短文positionだけfullvocabT1/KL coefficient1を加える一条件。native10M同architecture/4096codecなので大きなQwen教師とのfeature/vocab対応とは別の機構。元parentのWeb分布を保つ旧WebKLとも教師/対象が違い、全旧負結果を保持。[Born Again Neural Networks一次論文](https://proceedings.mlr.press/v80/furlanello18a.html)の同構造distillationを仮説の参考とするが日本語10Mの成功証明/厳密再現とはしない。

同元gold100Mを保持、追加softtarget25M positions・教師forward/GPUは別会計。source/親履歴、既存教師の未採用を明記し、その重みを単に採用してWebguardを回避しない。固定T1/coefficient1/LR1e-5WD.1/freshAdamW/seed42、cachedCEはGPU再実行・再採点しない。追加GPU総上限3600秒、実state/batch/timing180秒以内→science/eval予測が残りへ収まった場合だけscience capを凍結、未達ならcap/batch/教師量/形状を替えず終了。全Base matched/strong/absolute/historicalWeb条件と旧数値7失敗を維持。現在このKDは未実装/実CUDA0/科学0、改善・採用を主張しない。追加data取得・高コストroot診断を繰り返さず、測定に必要なら既存fixedTRAIN24/1024stressだけを再利用する。

最新境界を保持: 資格ある実Baseのみ独立学習seed/full DEV/protected final TEST/adoptionへ進み、Base完成を通知して停止。Chat/Dialogue/SFT/量子化/展開は開始しない。Base未完成・未採用、Python3.12.7はWSL uv、検証済み意味のある変更をlocalcommit、自動pushなし。今回は新sourceの実取得/一pass会計/固定条件終了・可搬保存のprogressで、goal completeではない。以下は過去の履歴。

Base限定・2008年編集例文の公式取得とCPU検証を終了、厳密encoding条件で不採用（2026-10-07 JST）。Baseは未完成・未採用。

[実終了記録](../reports/phase6/tanaka_edited_pd2008_source_completion.json)・[source pin](../reports/phase6/tanaka_edited_pd2008_source_pin.json)・[実encoding診断](../reports/phase6/tanaka_edited_pd2008_encoding_failure.json)。以下のTatoeba閉鎖記録の「次のarchive未取得」は当時の状態。今回、同EDRDG publisherの実HTML SHA13525a5acbdafbcb009f55ceba3cd3270dc2c89ac0a8552fc2eece3cac96334fに掲載された正確なFTP URL ftp://ftp.edrdg.org/pub/Nihongo/examples_pd.gz のOctober2008最終Public Domain編集版を一度だけ取得した。実8,386,099bytes、SHA b98033e3d740dae6a2c572795e6c0c768502ab0c2b0a268020e34ebdbb2b05e2。network累積8.340231秒/事前60秒。rawはWSL /home/aihub_ubuntu/jmicro-data/phase6/tanaka-edited-pd2008-20261007/examples_pd.gz に保持し、再取得なし。

候補HTTPS endpointはhostname不一致certificateで失敗、TLS検証は弱めていない。実publisherのpublished FTP linkとlast editedPD2008説明を確認し、FTP SIZEの非数値213metadata失敗後に同exact RETRをstream cap/hash付きで実施した。これらの初期metadata失敗と修正script/resultを保持。同archive/source/license/network/CPU/内容基準を替えた救済ではない。権利・原著者を独立監査したとはしない。

最初の5行の厳密EUC-JP/CRLF/A:日本語TAB英語/B:index構造だけをCPU0.008786秒で確認。これは全archiveのencoding証明ではなく、本文を表示・採点して選別しないdiscovery。元4096codec/原文10..256characters・6..64bodytokens・日本語終句/構造ID・wrapper除外/fixedDEV prefix>=12除外/原文body family90/5/5split/一pass exact dedup/固定TRAIN80seed2026100751・最低TRAIN1Mbodytokens/文法72・一貫性64を変更せずCPU準備を実装。元の2B corpus再scan・Tokenizer再学習なし、英語対訳/index/role/EOTは学習しない。

実CPU4checks/0.04秒成功後、初版config SHA3efe15d27fcd5a18dce79178f55050f62b0e066d170d406eaf0d3288998be12dを凍結。actual714209/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start21663195は147,262 activeA/line294525でpublisherの#A:/#B:コメント化された非学習部分をparserが誤拒否して終了。構造診断で提供元が「学習用として有用でない」と区別したmetadataを確認。元proposalはheader/indexの除外を予定していたため、内容を変更せずコメントを除外するV2 parserへ修正、失敗済みsource/config/jobを保持。最初のtest collectionの括弧記述ミスも修正し初期XMLを保持した。

V2も実CPU4checks/0.04秒成功、config SHAd4e7587f3dd71c7345e62f97b3e1b14c6d070307914de094eceb41a0c49356f1を凍結。actual714357/同boot/start21668310は終了・実不在。activeAを149,187処理した時点のline298737、byte33=0xadで標準EUC-JPのUnicodeDecodeError。実診断で当該行は除外commentではなくactiveA:本文であることを確認。decompressed25,154,490bytesまでの部分scanであり、全量・採用TRAINtoken数を推定しない。初版失敗・両構造診断込みCPU累積5.195449秒/事前90秒。source/schemaを全件厳密検証できず固定source readiness失敗。encodingを推測して替える・error ignore/置換・問題行drop・別版/mirror/filter/seed/threshold/epochで救済せず、この2008条件を終了する。3回目の準備なし。

prepared train/dev/test、fixed80、内容合格、科学教師、optimizer更新、GPU学習はすべて0。sourceの取得・形式検証失敗でありモデルの学習失敗ではない。全human Japanese/大きな学習量の無効を証明せず、旧数値7失敗/全歴史負結果/全Base品質基準を維持。complete_tanaka_edited_pd2008_source.pyは実process終了・失敗stage/line・全凍結source/refs SHA・stream pin stat・prepared/sample不在を確認。28text/portable archive20,482bytes、SHA78cc2613e99f95791aec84b9eb03e525bdd6c1b693f567fda91053ea4645c40dをWindowsへ保存し一度照合。rawgzip/full checkpointsはWSLに保持、旧2B・rawgzipの再全hashなし。元10B WebUI713143をCPU準備中に停止/変更せず、新GPUjobなし。

次の具体的アクション: 既存のsource registryと公的日本語本文の一次metadataを有限に確認し、未検証かつ実UTF8原文を用意できる候補を一つだけ比較案にする。既に終了したWeb/HQ/Wikipedia/青空/翻訳story/生成教材/CC0/2008例文を同じ条件で再試行せず、source選別の無制限探索にしない。新sourceを使う場合も、取得/CPU上限と量・固定TRAIN80の品質条件を結果前に記録し、原文・family split・既存DEV分離を維持する。source合格と実CUDA state/安定batch/測定予算が揃うまで追加科学GPUを開始しない。有望な実学習候補だけ既存matched/strong/absolute/historicalWeb gatesと独立学習seed/full DEV/protected final TEST/adoptionへ進む。

最新ユーザー境界: Baseの実全評価合格・採用が終わったら知らせ、そこで停止する。Chat/Dialogue/SFT/量子化/展開は開始しない。現在Base未完成・未採用、独立seed/full DEV/protected final TEST/adoptionは今回未実施。Python3.12.7はWSL uv、意味のある検証済み変更をlocal commit、自動pushなし。今回は公式archiveの実取得・CPU検証・固定source条件終了・可搬記録のprogressで、goal completeではない。以下は過去の履歴。

Base限定・Tatoeba日本語CC0取得を実行、量不足で固定案を終了（2026-10-07 JST）。Baseは未完成・未採用。

前goal turnは全parameter FP32/BF16勾配の実CUDA診断・精度修復分岐終了・92fac76保存のprogress。今回、required3docs/AGENTS/現worktree/既存source案を確認。[Tatoeba公式download](https://tatoeba.org/en/downloads)の実HTMLから日本語CC0専用URL /exports/per_language/jpn/jpn_sentences_CC0.tsv.bz2 と4column（ID/lang/text/modified）を特定。[CC0 original-only方針](https://en.wiki.tatoeba.org/articles/show/cc0-contributions)も実取得して確認。general Japanese/翻訳/音声/全言語exportへ替えない。

[実終了記録](../reports/phase6/tatoeba_original_short_source_completion.json)・[実準備結果](../reports/phase6/tatoeba_original_short_source_preparation.json)・[2文の観察](../reports/phase6/tatoeba_original_short_source_observations.json): actual713617/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start21575831はcomplete・実process不在。Windows worker35924。固定config SHA6ef993f6fbecfb0cf845881794be8512b619229aafdc4261e67205daac5f5019。元の失敗済みCUDA/科学jobは実不在、元UIだけが稼働する状態からCPU専用uv3.12.7 workerを起動。network5.713639秒/事前60秒、source preparation CPU0.006176秒/事前90秒、GPU/optimizer更新/科学教師0。compressed228bytes/decompressed260bytes、snapshot SHA39e6768de61f901a0904d9e74e554772d4e12286121ec3e2c6bd5307ce543465、HTTP Content-Length228/Last-Modified2026-10-03 06:31:09GMTを保存。一度のstream hash/pinと一度のdecompressionで完了、再取得0。

取得ファイルは実際に2文のみ。全2文が事前のUTF8/jpn/terminal punctuation/6..64bodytokens/10..256characters/codec原文byte/exclusionを満たし、TRAIN2文/47bodytokens（BOS/EOS込み51 serializedtokens）/192bodybytes、reserved DEV/TEST各0、rejection0。元の本文・sourceID/URL/CC0 metadataを保ち、exact body-family hashで90/5/5splitと一pass dedupを実装。元4096codecの再学習なし。旧2B index/tokenstreamの再scan/照合なし。既存public-magpieのfixed Base DEV prefix>=12characters除外契約を再利用し、source splitを学習と分離。semantic near-duplicateや全cross-corpus decontaminationを証明したものではない。

事前最低TRAIN1,000,000bodytokensに未達、amount_screen_passed=false/eligible_for_training=false。80文が存在せず、fixed80はrows/indicesとも空の記録として保持。代わりに2文を80文と見なすことも閾値を替えることもしない。2文を個別に読み、両方がCreative Commonsライセンス宣言の表記違いであることを記録。本文のCC BY4.0表記と取得ファイル自体のCC0 metadataを混同しない。全80内容screenは未実施で品質合格0、モデルの学習失敗ではなくこのCC0 snapshotの量不足。Tatoeba全体/他license版の量不足を主張しない。

実CPU5checks/0.11秒（実元codecの原文byte/構造ID除外、異なるsourceIDの同body同split、未完/URL/役割wrapper拒否、厳密UTF8/4column/schema/既存DEV除外、TRAIN限定80sampleのseed再現・duplicate/DEV混入拒否）・PS構文・uv CPU preflightが成功してからsourceを凍結/取得。complete_tatoeba_original_short_source.pyの実終端・全source/refs SHA・rawpin stat・split会計/家族漏洩・空80・元UI実identity/HTTP監査に成功。23text/642,511bytes、gzip194,717bytes/SHA9c94d75983a741bda5b843104b6fc72afae07465c5aed3cd850a2aee1a1e0fbbをWindowsへ保存し一度照合。rawcompressed/officialHTML/原文splitはWSL data環境に保持。元10B UI actual713143/同boot/start21525511は実稼働、HTTP親SHA410f975d…/10,000,007,168/busy=falseを確認。UI停止/変更なし、新科学GPUjobなし。

この固定CC0案を閉じ、CC-BY/現行翻訳export/seed/filter/threshold/epochで救済せず、追加GPU学習なし。全Base品質条件と旧数値7失敗/全歴史負結果を保持。この結果から自然な日本語教材や追加学習一般の無効を断定しない。

次の具体的アクションを[別のhistorical edited corpus案](../reports/phase6/tanaka_edited_pd2008_source_proposal.json)として記録。[EDRDG publisher](https://www.edrdg.org/wiki/Tanaka_Corpus.html)はOct2008の最後のPublic Domain編集版と、エラーの多い元収集/現行CC-BY版を区別している。編集版にも不自然な翻訳・人工的用例・反復/誤りが残るとの注意を保持し、自然な教材だと保証しない。既存repoにexamples_pd/Tanaka corpus実装/比較の該当なし。候補 examples_pd.gz の実official catalog/provenance/アクセス/encodingを先に確認する（web catalog fetchはInternal Errorで実archive未取得）。別のpublisher固定編集版の一調査であり、閉じた2文CC0案の再開/現行CC-BY exportへの置換ではない。network60秒/compressed64MiB/decompressed128MiB/CPU90秒、元codec/同最低1M TRAINbodytokens/結果前のfixed TRAIN80（seed2026100751、文法2>=72・standalone一貫性2>=64）、未達なら同2008条件終了を維持。元2001/current版/別archive/mirrorによる救済なし。qualified sourceだけ同100M/Web75M・新短文20M・物語5M比較の実装/実CUDA state/実測予算へ進む。今はこのarchive取得/品質/科学GPU0で、モデル品質改善を主張しない。

実Baseの全評価合格・独立学習seed/full DEV/protected final TEST/adoptionが完了したら知らせて停止する。現在Base未完成、Chat/Dialogue/SFT/量子化は開始しない。全五目標/Phase0–3/全基準/歴史負結果を保持。Python3.12.7はWSL uv、verified local commitのみ、自動pushなし。今回は新sourceの実取得・全量会計・量不足の確定・可搬保存のprogress。以下は過去の履歴。

Base限定・学習勾配の精度差を実CUDAで測定し、この固定診断を終了（2026-10-07 JST）。Baseは未完成・未採用。

前goal turnは入力混合100Mの実終端・全80採否・UI復帰・e1120d6保存のprogress。今回、required3docsと現worktree/実processを確認。旧root診断はFP32 full/causalの3parameter勾配とBF16 flash/mathの3parameter勾配比較、旧precision followupはno-grad分布/FP32生成であり、全parameterのFP32対BF16学習勾配とは異なる。FP32推論でも反復する既測定結果と旧数値7失敗を保持し再実行しない。[PyTorch AMP一次資料](https://docs.pytorch.org/docs/stable/notes/amp_examples.html)のforwardに選択されたdtypeをbackwardも使う説明、[数値精度資料](https://docs.pytorch.org/docs/main/notes/numerical_accuracy.html)を確認し、新しいreadonly比較だけを定義。

[固定config](../configs/phase6/base_gradient_precision.json) SHAfff9402934896b6ea45617d6c5358ea4f3c98277821fc3d6dc7eeb3e23c6dd64・[実終了記録](../reports/phase6/base_gradient_precision_completion.json)・[全結果](../reports/phase6/base_gradient_precision_result.json): actual713034/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start21522851はcomplete・実不在。Windows worker32064。GPU22.728672秒/事前cap120秒、peak665,210,368bytes、allocator90%。元10Bとcached CE100Mの同native10,001,152/tied/FP32 master weightsを使い、既存固定TRAIN24文書（Web/教材/物語各8）と既存original長1024窓1を再利用。新source draw/新distinct教材0。14batch・3pathsで全25窓/endpointのFP32 math（TF32 off）対BF16 math/flashを完了。元body/EOS mask・position/教師/input会計は同じで、診断teacher位置18,264（各path/endpoints合計）を新しい科学教師に数えない。optimizer更新/科学教師/新生成採点0。

全10,001,152個のdistinct parameter勾配と元教師数で重み付けしたsource平均、各layer/embed/norm群を保存。global clip1/eps1e-8後のfresh AdamW初回data方向も一時vectorとして計算し、実モデル/optimizer更新はしない。全source/stressでgradient cosine0.998683以上、relative L2差1.64–5.30%。初回data方向cosine0.987631以上、L2差14.03–15.73%。この差はゼロではないが、事前の重大marker（勾配cosine<.99またはL2>.10、初回方向cosine<.98またはL2>.20、同BF16 pathで元3source中2以上かつ両endpoint）に該当するsourceは0。bf16_math/flashともsupported=false。Stress/per-groupは記述で、都合よくscreenへ足さない。

実CPU4checks/1.70秒（方向対scale/zero・非有限拒否、global clip後の実fresh AdamWと初回式一致、全distinct群/入力不変、両endpoint・同path・2source条件）・PS構文/uv CPU inspect成功。最初のprepareはWindows portable aliasをnative report pathと誤認し、config作成/UI変更/GPU開始前にFileNotFoundError。初期source/partial payload/失敗理由を保存し、実native root-cause-20261005/precision-contract.jsonへ修正、全referencesを先に確認して同cached25窓で準備成功。新random draw/threshold/recipe/budget変更0。actual CUDAの全weights/tied/RNG不変・no accumulated grads・FP32 master/all rows checksに合格。scalar loss読み出しwarningをstderrへ保持、診断は正常終了し、凍結sourceを終了後に書き換えない。

complete_base_gradient_precision.pyの実終端・全14batch/全path会計・固定screen再計算・全source SHA・UI復帰・archive監査成功。42text/2,084,614bytes、gzip490,198bytes/SHA2df811f3061f2a793cc3936c737c75fdf43f7a29fe84d3cc9ccef66c95980508をWindowsへ保存し一度照合。full checkpointsはWSL保持。元10B UI actual713143/同boot/start21525511を実processとHTTP親SHA410f975d…/10,000,007,168/busy=falseで確認。新科学GPUjobなし。

この固定25窓・両成熟endpointの重大精度差仮説を閉じ、FP32/precision修復の追加学習やsample/backend/threshold/上限の救済へ進まない。局所勾配/初回data方向の比較で、全corpus・蓄積optimizer・長期精度影響・唯一の原因を否定した証明ではない。全Base品質条件・旧数値7失敗・歴史負結果を保持。

次の具体的アクションを[新sourceの有限調査案](../reports/phase6/tatoeba_original_short_source_feasibility_proposal.json)へ固定。既存scripts/docs/configs/reportsのtatoeba検索は既存実装/比較の該当なし。公式[download](https://tatoeba.org/en/downloads)・[CC0 original説明](https://en.wiki.tatoeba.org/articles/show/cc0-contributions)・[reuse guidance](https://en.wiki.tatoeba.org/articles/show/using-the-tatoeba-corpus)を確認したが、実データの取得/量/品質は未測定。日本語CC0 original短文の公式URL/schema/license/provenanceを確認→network60秒/compressed64MiB/decompressed128MiB/CPU90秒以内で一度だけpin→同既存codec/原文・固定split・exact dedup・dev/test分離→結果前に固定したTRAIN80を個別確認する。minimum eligible TRAIN1M bodytokens/文法72/80・standalone一貫性64/80を満たした場合だけ、同100M/Web75M・短文20M・物語5Mのsource置換比較を別途実装し実測予算/stateを定める。現段階はGPU0/取得0で採用や改善を主張しない。未達ならこのCC0 source条件を閉じ、CC-BY/翻訳版/seed/filter/閾値/epochで救済しない。これはChat/SFTではなく原文Base教師の仮説。

実Baseの全評価合格・独立学習seed/full DEV/protected final TEST/adoptionが完了したらユーザーへ知らせて停止する。現在Base未完成、Chat/Dialogue/SFT/量子化は開始しない。全五目標/Phase0–3/全基準/歴史負結果を保持。Python3.12.7はWSL uv、verified local commitのみ、自動pushなし。今回は新しい全parameter学習精度診断の実測・条件終了・可搬保存のprogress。以下は過去の履歴。

Base限定・入力混合100M比較の学習と全評価を終了、不採用（2026-10-07 JST）。Baseは未完成・未採用。

[終了記録](../reports/phase6/base_context_mixing_comparison_completion.json)・[全80レビュー](../reports/phase6/base_context_mixing_comparison_review.json)・[個別観察](../reports/phase6/base_context_mixing_observations.tsv): actual709696/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start21284143はcomplete・実process不在。terminal full stateで元gold100,000,000教師/17,698更新を確認。最終heartbeat99,900,395/17,680は途中値として保持し、完了量とはしない。科学GPU1,823.248917秒（30.4分）/固定cap4,072秒、probe込み1,833.718489秒/事前総cap7,200秒。最終checkpoint SHA1490a80e327e6b6476d3cf6e44cdcbdb8a26dea4671f5b639963cc5221ba6c6b。native10,001,152params/同parent/同gold/source/batch/seed/fresh AdamWは維持、cached CE対照のGPU再実行・再採点0。

予測用追加forwardはvalid102,655,467/physical370,838,917入力。混合対象101,805,988位置のうち5,091,856位置で予測を選択、実変更2,732,520位置（5%は選択確率で、実変更率ではない）。元gold教師/Web75M・教材20M・物語5M/元EOS・bodybytes/digest/full samplerの全11一致checks、専用mixing RNGを含むfull state、全17,698完了metrics・有限値/会計を実レビュー。追加教師/params/新distinct教材0。追加forward computeは元教師tokensと分けて記録。

|条件|共通byte BPB|文法2/80|関連2/80|一貫性2/80|適切完結/80|EOS/80|自動反復/80|
|---|---:|---:|---:|---:|---:|---:|---:|
|cached CE100M|0.998487|44|25|2|2|19|45|
|入力混合100M|1.007638|43|24|1|4|11|53|

固定全80を個別に読み、prefix/text/generated_ids/停止が完全一致した11件のみ既存CEの理由・採点を再利用、変化した69件に個別理由を保存。非blind Codexの反復DEV判定で独立人間ではない。犬の擬人化を単独で誤りにせず、数値/条件の誤りは文法と分離し、自動反復falseでも実際の循環を記録。単なるEOSを適切な完結としない。一貫性差-1/80、paired95%CI[-.05,.025]で悪化確定ではないが改善条件は未達。意味192件59.896%/JBLiMP331件77.946%/JCQA1,119件34.853%、Unicode/role/empty各0。common256文書/472,055bytes/122,343tokensで比較。matched CE/strong relative/absolute/historical Webの全採用gateは未達、eligible=false。

review_base_context_mixing.py、complete_base_context_mixing.pyの実終端監査・全80 raw/codec/suite結合・採否保存・元UI復帰・text archiveに成功。42text/107,768,551bytes、gzip46,995,094bytes/SHA56e7830c4deef7a628f157f4d7da7e2a58777c7a67e46e10a92309bd1e772c4cをWindowsへ保存し一度照合。full checkpointsはWSL保持。元10B UI actual711570/同boot/start21466885を実processとHTTP親SHA410f975d…/10,000,007,168/busy=falseで確認。新科学GPUjobなし。

この固定5%・greedy一回の条件を閉じ、確率/pass/decoder/LR/source/parent/batch/教師/上限の救済変更で再実行しない。単一成熟親・単一seed・尤度不整合/元goldと混合履歴の矛盾を含む変形の負結果であり、全scheduled sampling/10M容量/追加学習の無効を証明しない。既測定のUL/next-two/Muon/packing/BOS/teacher/Attention等を再実行せず、corpus再全scan・Tokenizer再学習・自動20B/50B延長なし。次の具体的アクションは既存のTRAIN内容と学習・生成評価を統合して未検証の根本要因を一つ特定し、追加GPU開始前に固定対照・実測予算・終了条件を記録すること。資格ある候補だけ独立学習seed/full DEV/protected final TEST/adoptionへ進む。

最新ユーザー指示を保持: 実Baseの全評価合格・採用が完了したら知らせて停止する。Chat/Dialogue/SFT/量子化は開始しない。現在Base未完成、独立学習seed/full DEV/protected final TEST/adoptionは今回未実施。全五目標/Phase0–3/旧数値7失敗/歴史負結果と品質条件を保持。Python3.12.7はWSL uv、verified local commitのみ、自動pushなし。今回は一比較の実終端・全80採否・可搬保存のprogress。以下は過去の履歴。

Base限定・入力混合の実CUDA検証を終了、同gold100M比較を永続起動（2026-10-07 JST）。Base未完成・未採用。

前goal turnはcontext-mixing trainerの実装/CPU9checks/固定比較案・5d07579保存のprogress。今回は不足していたprobe/science/review/closeoutと2永続PS launcherを実装し、旧Muon harnessは変更せず評価と会計の契約を再利用。新state/worst-window fixtureとCPU runner8checks/2.55秒（予算7200秒固定、同教師でもdigest/full sampler違い拒否、未commit optimizer/mixing/source会計拒否、元TRAIN worst1024/512/EOS保持と再実行拒否）に成功。AST9sources/両CLI import/2PS構文/CPU inspect成功。凍結されたprototype/旧trainer/model/既存品質helperは変更していない。

[実CUDA検証終了](../reports/phase6/base_context_mixing_probe_completion.json): actual709297/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start21275597はcomplete・実process不在。probe config SHA7983ec64ea2ee060ee129a4bffa87e181bbb83e6ab4c927b09e91a25ccd8b2ca。GPU10.469572秒、48検証更新/298,097元教師（worst capacityの1更新/24,576位置をこの合計に含み、追加で二重加算しない）。native10,001,152params/tied/親weights/一度だけのparameter partitionの4初期checks、専用mixing RNGを含む全model/Adam/scheduler/global RNG/full sampler/counters/mixing/digest/historyの連続4対2+save/resume+2・元CEの同source/教師/EOS/input/bodybytes/digest/full sampler一致など19checksに合格。worst batch48/context1024/stride512の元TRAIN教材窓で、元gold24,576/追加予測forward49,152入力、選択2,428・実変更1,269、CE2.566937/gradient norm3.054288有限の完了更新を確認。5%は予測を選択する確率で、正しい予測では入力が変わらない。peak11,078,919,680bytes、resident allocator90%。全32timing中央値40,992.21元教師/秒。probe重みは科学へ流用しない。

science capは事前式ceil(100M/speed*1.3+900)=4,072秒（約67.9分）、probe込み4,082.469572秒で固定総cap7,200秒内。学習だけの目安は約40.7分、保存/評価を含む上限と区別する。WSL空き82GB。21textのgzip162,129bytes/SHA f230cb93fc0a5c0a78e36822e29c6fcf262fa100bf0795de5f884dbcc4ad6ab0をWindowsへ保存・一度照合、full checkpointsはWSL保持。

[本学習の実起動](../reports/phase6/base_context_mixing_science_start.json)・[runner準備記録](../reports/phase6/base_context_mixing_runner_preparation_completion.json): reports/phase6/base-context-mixing-comparison-20261007、actual709696/同boot/start21284143、Windows worker34004、開始2026-10-06T23:33:58Z。科学config SHA e1b2b64d9b57ccd1dc1ba341eb5a389c424842a7ce735583365da9ed2518b782、同accepted2B TRAIN/元gold100M/Web75M・教材20M・物語5M/batch48/seed42/fresh AdamW LR1e-5・WD0.1 constant/同native推論を維持。追加教師/新distinct教材/params0、prediction forwardとmixed-inputの会計は別保存。actual PIDと教師増加・有限loss・checkpoint-00000250.ptを実確認、runner準備記録時の元教師4,513,754で本学習が稼働。250更新ごとに全state、20更新ごとにheartbeat、各完了更新metricsを保存。live closeoutを一度実呼出しし、実processが終了していないため意図通りValueErrorで拒否、completion/archive/manifestを作らないことを確認。これは科学停止/失敗ではない。

UIは科学中停止し、永続launcherが終端で元10Bへ復帰する。restart: scripts/run_base_context_mixing.ps1 -Worker。先にactual PID/boot/start不在・有効completed checkpoint・同凍結sourceを確認し、同累積4,072秒内でのみ再開。重複起動なし。次は本学習100M終端→同256文書/common-byte BPB・日本語192/331/1119・固定全80→新全80個別raw-bound採点とcached CE80再利用→review_base_context_mixing.py→complete_base_context_mixing.py→Windows evidence SHA確認/local commit。今は科学が実稼働しており、品質改善/採用をまだ主張しない。

確率/pass/decoder/LR/source/親/batch/教師/上限の救済変更・同診断の再実行・全corpus再scan/Tokenizer再学習なし。likelihood不整合/元goldと混合履歴の矛盾/byte片UTF8・単一seed/反復nonblind DEV・追加computeの限界を保持。全matched/strong/absolute/歴史Web品質条件を保ち、資格ある候補だけ独立学習seed/full DEV/protected final TEST/adoptionへ進む。実Baseの全評価・採用完了時にユーザーへ知らせて停止し、Chat/Dialogue/SFT/量子化を開始しない。全五目標/Phase0–3/旧数値7失敗/全過去の負結果を保持、Python3.12.7はWSL uv、verified local commitのみ、自動pushなし。今回のturnは実装・実CUDA gate・科学実起動のprogressでBase完了ではない。以下は過去の履歴。

Base限定・モデル予測を入力へ混ぜる新比較のCPU処理を実装・検証（2026-10-07 JST）。Base未完成・未採用。

前goal turnはMuon100Mの実終了・全80採否・UI復帰・423fba4保存のprogress。今回はrequired3docs/current worktreeと既存root/FP32・sequence UL/選好/全般化の証拠を確認。旧数値7失敗は保持し、FP32でも反復する既測定診断を再実行しない。Muonやnext-two等の失敗条件を救済しない。

[固定比較案](../reports/phase6/base_context_mixing_proposal.json)と[実CPU検証記録](../reports/phase6/base_context_mixing_prototype_completion.json): native10,001,152/元成熟10B/同accepted2B TRAIN/同gold100M（Web75M・教材20M・物語5M）/batch48/seed42/fresh AdamW LR1e-5・WD0.1 constant/cached CEを保つ。新方式はno-gradientのclean-context一回予測から直前位置のgreedy body tokenを選び、元body入力の5%へ混ぜるparallel history mixing。position0/PAD/全元specialを保持し、元gold本文/EOSラベルは一切変更せず各一度だけCEで学ぶ。追加head/params/新distinct教材/追加教師0、予測forwardのvalid/physical入力と変更数・mixed digestは元gold教師/元source digestと別会計。旧ULの自己反復tokenへの負の勾配とは異なり、混合履歴に対して元goldの正の勾配を与える仮説で、改善の保証はない。

[Parallel Scheduled Sampling](https://arxiv.org/abs/1906.04331)と[Transformerでの二回経路](https://aclanthology.org/P19-2049/)を一次資料として確認。[目的関数の不整合の指摘](https://arxiv.org/abs/1511.05101)も保持。今回はgreedy一回・固定5%の変形で、完全な逐次samplingや尤度整合性を保証しない。固有名詞/数値を替えた入力は元goldと矛盾し得るし、byte片の混合が単独UTF8文になる保証もない。既存すべてのBPB/strong/absolute/歴史Web採用基準を保持し、Devの基準を緩めない。

base_context_mixing_trainer.pyを追加し、実WSL uv3.12.7 CPU9checks/4.53秒に合格。直前位置だけの予測と未来を使わないこと・境界/PAD保持、混合0のnative weights/Adam/scheduler/global RNG/full sampler/会計/履歴と元CEの完全一致、実際に入力が変わっても元gold/source/EOS/digest/full samplerが一致、混合専用CPU Generatorを含む連続4対2+save/resume+2の全state/history完全一致、recipe/update/count/source/RNGの5不正state拒否を確認。最初は反復文字のtied random fixtureが元入力をコピーし変更数0で1check失敗。XMLを保存し、tiedを保った誤予測stress fixtureへ修正、元の変更数>0判定は維持して成功。これは実モデル品質/実CUDA成功の証拠ではない。凍結された旧trainer/model/reviewerは変更していない。

比較前の固定GPU総cap7,200秒、CUDA probe180秒。二回forwardによる追加computeを見込み、科学capは実32timing中央値からceil(100M/speed*1.3+900)を求めprobe実時間込み総cap内でのみ実行する。予算/有限値/state/品質で不合格なら確率/pass/decoder/LR/source/親/batch/教師/上限を替えて救済しない。GPU probe/science/reviewer/永続launcherはまだ未実装・未実行で、今回GPU0/科学教師0。次はこれらの必要コマンドを実装しsource/configを凍結→実CUDA worst1024/512・batch48有限性と全save/resume/source gate・速度を測定→予算内のみ元100Mと同256byte/日本語192・331・1119/全80個別内容を比較→資格ある候補だけ独立学習seed/full DEV/protected final TEST/adoption。

元10B UI actual707311/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start21203291を実processとHTTP親SHA410f975d…/10,000,007,168/busy=falseで確認、終了Muon705306は実不在。UI停止/新GPUjob/新教材全量scan/Tokenizer再学習なし。Baseの全評価・採用が完了したらユーザーへ知らせて停止し、Chat/Dialogue/SFT/量子化へ進まない。全五目標/Phase0–3/旧数値7失敗/全歴史負結果と全品質基準を保持。PythonはWSL uv、verified local commitのみ、自動pushなし。今回は必要trainer実装・実CPU保存再開検証・一比較の固定案保存のprogress、Base完了ではない。以下は過去の履歴。

Base限定・Muon100M比較の全評価を終了、不採用（2026-10-07 JST）。Baseは未完成・未採用。

[終了記録](../reports/phase6/base_muon_comparison_completion.json)・[全80レビュー](../reports/phase6/base_muon_comparison_review.json)・[個別観察](../reports/phase6/base_muon_observations.tsv): actual705306/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start21012791はcomplete・実process不在。terminal full stateで元gold100,000,000教師/17,698更新を確認、最終heartbeat99,900,395/17,680は途中値として保持。科学GPU1,900.415525秒（31.7分）/固定cap4,331秒、probe込み1,910.642585秒/事前総cap4,800秒。最終checkpoint SHA fab4bb0db05aee57759265de5ec38acd1e7f8a58b3a9357e967952ed1a5f9dd7。native10,001,152params、追加params/新distinct教材0。全native・Muon/AdamW・scheduler・RNG・sampler・全17,698完了metrics・有限値/会計とcached CE100Mの同一元教師/source/EOS/input/physical/bodybytes/digest/full sampler一致を実レビュー。cached対照のGPU再実行/再採点0。

|条件|共通byte BPB|文法2/80|関連2/80|一貫性2/80|適切完結/80|EOS/80|自動反復/80|
|---|---:|---:|---:|---:|---:|---:|---:|
|cached CE100M|0.998487|44|25|2|2|19|45|
|Muon100M|0.999279|52|26|1|2|24|45|

全80を個別に読み、prefix/text/generated IDs/停止が完全一致した32件は既存CEの理由・採点を再利用、変化した48件へ個別理由を保存。非blind Codexの反復DEV判定で独立人間ではない。木や犬の創作・擬人化はgold不一致だけで減点せず、数値/条件の誤りと文法を分離。自動反復falseでも同語の循環は内容評価へ記録した。EOS増加だけで適切な完結としない。一貫性差-1/80、paired95%CI[-.0375,0]で有意な悪化の確定ではないが改善条件は未達。意味192件59.896%、JBLiMP331件77.341%、JCQA1,119件35.389%、Unicode/role/empty各0。共通256文書/472,055bytes/122,343tokensでBPBを比較。matched CE/strong relative・absolute・historical Webの全品質条件未達、eligible=false。単一成熟親・保守的100M optimizer移行の負結果であり、全Muon/10M容量/追加学習の無効を証明しない。

review_base_muon.py --templateの終端state監査、全80notesのnative codec/raw SHA/固定suite・内容/同byte/日本語レビュー、complete_base_muon.pyの実終了/UI復帰/可搬保存はすべて実成功。41text/103,241,988bytes、gzip45,247,981bytes/SHA dad32c9b7b6b115331de6d2eb4ebd7b468fcdcf8b1cfb553fc2ee115e39dda41をWindowsへ保存・一度照合、full checkpointsはWSL保持。元10B UI actual707311/同boot/start21203291を実processとHTTP親SHA410f975d…/10,000,007,168/busy=falseで確認。新科学GPUjobなし。

この固定momentum.95/Nesterov/NS5/match_rms_adamw/constant LR1e-5条件を閉じ、momentum/NS/scale/LR/source/親/batch/教師/上限による救済をしない。次の具体的アクションは既存比較の品質・会計・TRAIN内容観察を統合し、追加学習前に未検証の一要因を特定して固定対照・実測予算・完了条件を定めること。既測定のpacking/BOS・teacher transfer・sequence UL・next-two・Attention・構造予算の負結果を保持し再実行しない。corpus全量再scan・Tokenizer再学習・自動20B/50B延長なし。

Base未完成、独立学習seed/full DEV/protected final TEST/adoptionは資格のある候補にのみ実行し今回は未実施。実Baseの全評価・採用が完了したらユーザーへ知らせて停止する。Chat/Dialogue/SFT/量子化に進まない。Python3.12.7はWSL uv、verified local commitのみ、自動pushなし。Phase0–3/全五目標/旧数値7失敗/全品質基準を保持。直前の待機turnは実PID・教師/保存増加を確認したverified wait、今回は終端・全80採否・可搬保存のprogress。以下は過去の履歴。

追加準備・Muon学習継続（2026-10-07 JST）。

前goal turnはnative Muonの実CUDA検証・元100M科学起動・7aab865保存のprogress。actual705306/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start21012791は実process稼働を再確認。22:53:31Zに14,120,225元教師/2,500更新/loss2.660657有限、checkpoint-00002500.ptを保持。失敗や停止の証拠はなく、同凍結config・4,331科学GPU秒/総4,800秒内で継続、重複起動なし。

[complete_base_muon.py](../scripts/complete_base_muon.py)を追加。実process終了・科学終端・凍結policyとraw-bound全80採点・元UIの実process/HTTP親SHA復帰を確認して、text証拠だけをtmp→atomic archiveへ保存する準備。資格ありでも独立学習seed/full DEV/protected final TEST/adoption待ちとしBase_complete=Falseを保持し、失敗済み条件を救済しない。uv pinned CPU AST成功、現在live PIDへの実呼出しは意図通りValueErrorで拒否しcompletion/archiveを作らないことを確認。実終端への保存はこれからで、コード追加はBase完成の証拠ではない。学習・既存reviewer/source/configの変更0、新教材/GPU診断0。

次は同本学習終端と自動評価→新全80個別採点/cached CE80再利用→review_base_muon.py→complete_base_muon.py→Windows bundle SHA確認/local commit。学習中は元UI停止、launcherが終端で元10Bへ復帰する。Base未完成・未採用、全五目標/全歴史gate/旧数値7失敗を保持。実Baseの評価・採用完了時に知らせて停止し、Chat/Dialogue/SFT/量子化なし。Python3.12.7はWSL uv、local commitのみ、自動pushなし。以下は過去の履歴。

Base限定・更新方法の比較を実WSL CUDAで開始（2026-10-07 JST）。Baseは未完成・未採用。

前goal turnは公開日本語Base一参照の回復・実評価・全80個別採点・db61143保存のprogress。今回は既存sequence UL/低係数・TRAIN64選好・source-local generalizationの実診断/全内容/負結果を再確認し、自己生成反復の同じlossを再実行しない。公開参照の失敗は容量限界やnative故障の証明ではない。未実施だった更新方法を一要因として、[固定Muon案](../reports/phase6/base_muon_proposal.json)を定義。native10,001,152params/元成熟10B親/同accepted2B TRAIN/同元gold100M（Web75M・教材20M・物語5M）/batch48/seed42を保持し、hidden2D matrixだけ公式torch.optim.Muonへ変更。tied4096 vocabularyとnormはfresh AdamW、同nominal constant LR1e-5/WD0.1。momentum.95/Nesterov/NS5/match_rms_adamwを一条件として固定。[Muon一次論文](https://arxiv.org/html/2502.16982v1)の0.2*sqrt(max(shape))更新scaleと[PyTorch公式実装](https://docs.pytorch.org/docs/2.14/generated/torch.optim.Muon.html)を使用。更新幅の厳密一致や日本語改善の保証ではない。追加params/新distinct教材0、cached CE100Mを再GPUしない。

[実CUDA検証終了](../reports/phase6/base_muon_probe_completion.json): actual704896/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start20996967はcomplete・実process不在。CPU trainer7checks/3.15秒とrunner5checks/0.81秒、PS構文・CPU inspect成功。GPU10.227060秒、47検証更新/273,521元教師、worst original1024/512・batch48の24,576教師位置forward/backward（optimizer0）を別会計。全native・hybrid Muon/AdamW・constant scheduler・RNG・full sampler・countersと全履歴の連続4対2+save/resume+2が完全一致。元AdamWの教師列/source/EOS/input/physical/bodybytes/digest/full samplerも一致。全4初期不変checksと全15保存再開/source checksに合格。worst peak10,719,607,808bytes、resident allocator90%。固定32timing中央値37,893.91元教師/秒、100M学習予測約44.0分。保存・評価30%margin+900秒を含む科学cap4,331秒、probe込み4,341.227秒で事前総cap4,800秒以内。probe重みは本学習に流用しない。

最初のCPU preflight前に既存capacity payloadのwindowキーを補正し、最初のlauncher inspectではread_jsonへ文字列を渡したAPI誤りを検出した。どちらも科学/検証GPU0・UI変更前。Path対応へ修正、configへ旧SHA/時刻/理由を保存して実CPU inspectを通した後にcorrected Workerを一度起動し成功。レシピ・教師・品質条件・予算の救済変更ではなく、同じ失敗の無修正再試行なし。20textのgzip153,864bytes/SHA3b67e5bdd7a6432b20608fcf0cce4ce0886b95ab6b5f30ecde2c7411d1f037e0をWindowsへ保存・照合、検証full checkpointsはWSL保存。

[本学習の永続起動](../reports/phase6/base_muon_science_start.json): reports/phase6/base-muon-comparison-20261007、actual705306/同boot/start21012791、Windows worker13656、開始2026-10-06T22:48:45Z。凍結config SHA1cd6fb131c2589fe5f03bb75d9dd2461ef81baed9da6d3f7648c85fd9f118dfd。22:49:49Zに実process稼働、2,942,766元教師/520完了更新/loss2.620010有限、checkpoint-00000500.ptを実確認。モデル品質の改善はまだ未測定。250更新ごとに全state、20更新ごとにheartbeat、全完了metricsを保存。science中元UI停止、終端launcherが元10Bへ復帰する。restart: scripts/run_base_muon.ps1 -Worker。先に実PID/boot/start不在と有効completed-update checkpointを確認し、同凍結source・同累積GPUcap内でのみ再開。重複起動しない。

次の具体的アクション: 実元100M終端→同256/common-byte BPB・日本語192/331/1119・固定全80→review_base_muon.pyでnative codec/raw-bound新全80を個別採点しcached CE80を再利用、元matched/strong/absolute/historical Webの全gateで判定→科学完了archive/UI復帰/verified local commit。現時点は学習稼働で、品質レビューと科学の終端監査は未実施。新reviewerは旧rubric/gatesを再利用してhybrid会計を追加、実終端データでの受入確認はこれから。単一optimizer条件が不合格ならmomentum/NS/scale/LR/source/親/batch/教師/上限で救済しない。資格のある候補だけ独立学習seed/full DEV/protected final TEST/adoptionへ進む。

Base未完成・未採用、全五目標未達。実Baseの全評価合格・採用が完了したらユーザーへ知らせて停止する。Chat/Dialogue/SFT/量子化を開始しない。Python3.12.7はWSL uv、local verified commitのみ、自動pushなし。Phase0–3/全過去の負結果/旧数値7失敗・全品質条件を保持。今回のturnは実装・実CUDA gate・科学実起動のprogress。以下は過去の履歴。

Base限定・公開日本語Baseの固定80件参照を終了（2026-10-07 JST）。Baseは未完成・未採用。

[全80内容と終了記録](../reports/phase6/public_japanese_base_reference_review.json)・[個別観察](../reports/phase6/public_japanese_base_reference_observations.tsv): rinna/japanese-gpt2-xsmallの公開MIT重みをrevision8e91527b3276e0565154935e84a08bf0137ed99fへ固定し、公式config/slow SentencePiece/do_lower_case=Trueを使用。回復CPU8.779888秒/156,701,691bytes、重みSHAとサイズ・mtimeを保存して再全量照合しない。実測37,398,016paramsでnative10,001,152と規模・構造・語彙・教材・学習量が異なる。旧checkpointの6個のmasked_bias bufferだけが現Transformersのload reportでUNEXPECTEDとなる。CPU finite forward/codec確認を通過し、原文DEV80/BOS1/plain/FP32 eager/greedy64 foreign tokens・GPU上限180秒を結果前に固定。未知語0、9prefixで公式codecの表記正規化差を記録。

actual703948/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start20945474は実CUDA15.512964秒で全80生成を完了・実process不在。新student教師/optimizer更新0、protected TESTなし。全80 raw IDs/text/停止/長さを公式foreign codecで再構築し、全件を個別に読んで既存rubricで採点。文法2=16/関連2=27/一貫性2=2/適切完結5/EOS9/反復44、Unicode/role/empty0（各80）。cached native CE100Mは文法44/関連25/一貫性2/適切2/EOS19/反復45、GPU再実行・内容再採点0。foreign生成本文20,935bytes/中央値93文字、native18,341bytes/中央値77文字で、同64tokensは同byte長ではない。非blind Codex診断で独立人間ではなく、外国語彙のBPBや日本語選択式は未測定。参照条件もabsolute生成条件を満たさず、モデル・prompt・decoder・上限で救済しない。この結果から10M容量限界・native実装故障・追加学習の無効を断定しない。

旧文書境界/packed-history診断はendpoint marker=false、旧Qwen教師のpaired accuracy CI下限0でtransfer gate=falseだった実証拠を再確認。packing学習やteacher feature転移の分岐を再開しない。next-twoの失敗・構造比較予算不合格・全歴史Web/strong/absolute条件・旧数値7失敗を保持。今回の参照モデルは10Mとして採用せず、Base未完成/未採用、独立学習seed/full DEV/protected final TEST/adoption未実施。

可搬15textのgzip42,114bytes/SHAd6e1d026745d673a73e64a84ab39a5d07ba17676580aeba68035909e27658565をWindowsへ保存・照合。reviewer初回のnative IDキーの誤参照をgenerated_idsへ修正し、CPU再実行で全80/長さ/UI実確認とarchive成功、GPU再実行なし。元10B UI actual704069/同boot/start20947486を実processとHTTP親SHA410f975d…/training_tokens10,000,007,168/busy=falseで復帰。科学GPUjobなし。Python3.12.7はWSL uv、local verified commitのみ、自動pushなし。

次の具体的アクション: 既存TRAIN rollout・sequence-objective診断を棚卸しし、今回の参照結果を加えて短いprefixから自己生成履歴・反復へ至る経路の未測定差を特定する。既測定の診断・失敗済み補助loss/teacher/source/構造条件を繰り返さず、次の比較は単一仮説・固定対照・実GPU見積りと完了条件を決めてから実装する。全corpus再scan・Tokenizer再学習・自動20B/50B延長なし。実Baseの全評価合格・採用が完了したらユーザーへ知らせて停止し、Chat/Dialogue/SFT/量子化に入らない。今回のturnは一参照の回復・実評価・全80採点・証拠保存のprogressで、全五目標の完了ではない。以下は過去の履歴。

Base限定・next-two補助学習100Mの全評価終了、不採用（2026-10-07 JST）。

[実終了と可搬証拠](../reports/phase6/base_next_two_token_comparison_completion.json)・[全80採点と比較](../reports/phase6/base_next_two_token_comparison_review.json): actual701073/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start20668823はcomplete・実process不在。元gold教師100,000,000/17,698更新をterminal stateで確認。最終training heartbeat99,900,395/17,680は途中の値で、完了量ではない。追加next-two教師99,150,521、総label位置199,150,521、追加係数mass9,915,052.1を元教師と別計数。native推論10,001,152paramsは不変、学習専用688,896params、同TRAINの再利用で新教材量0。GPU1,571.634540秒（26.2分）/凍結3,793秒、checkpoint SHA4d76e678f57d61fc6c6f1617b322dd04f6846ca69a7568cb70cec706c0a0b024。全native・aux・Adam・scheduler・RNG・sampler・17,698完了履歴と全会計をreview。aux Adamも今回は全17,698更新で進行。元教師/source/EOS/input/physical/bodybytes/digest/full samplerはcached CEと一致、対照GPU再実行・再採点0。

|条件|共通byte BPB|文法2/80|関連2/80|一貫性2/80|適切完結/80|EOS/80|反復/80|
|---|---:|---:|---:|---:|---:|---:|---:|
|cached CE100M|0.998487|44|25|2|2|19|45|
|next-two補助100M|1.000047|45|23|1|1|19|45|

全80を個別に読み、同一prefix/text/IDs/停止の38件は既存内容採点を再利用、変わった42件へ個別理由を保存。非blind Codex診断で独立人間ではない。自然な創作・擬人化をgold不一致だけで落とさず、数値誤答と文法を分離した。唯一の一貫性2/適切完結は不眠から夜の時間を大切にする短文。母の呼称、接続節、同一原因、名詞の自己説明を反復する失敗が残る。対照一貫性差-1/80、paired95%CI[-.0375,0]で独立した悪化の確定ではないが、改善条件は未達。BPB差+0.0015597/文書paired CI[0.0012701,0.0018405]、相対+0.1562%は1% guard内でも改善ではなく、単一seed/反復DEVの範囲。全256文書/472,055byte/122,343tokensを同条件で比較した。

意味192件60.9375%（対照62.5%）、JBLiMP331件76.7372%（77.3414%）、JCQA1,119件34.6738%（35.0313%）。意味差CI[-.041667,.005208]は0を含む。Unicode/role/empty0。strong相対・absolute・historical Webの全条件を満たさず、eligible=false/全品質基準不変。固定horizon2/係数0.1/contextual head条件を閉じ、係数・horizon・head・LR・source・親・epoch・教師量・GPU上限で救済しない。next-two一般、全容量限界、全追加学習の無効を証明する結果ではない。

complete_base_next_two_token.pyは終端の実review/個別TSV/元UI実process・HTTP親SHAを確認して実行成功。45text/109,070,455byte、gzip46,920,058byte/SHA28ee81e23fec0dc9410ab2b88e4634472350b91b0ea51cd8bb2f7e9e88d4ccd9をWindowsへ保存・照合。full checkpointsはWSL保持。元10B UI actual701993/同boot/start20826405は実processとHTTP親SHA410f975d…/training_tokens10,000,007,168/busy=falseで復帰。新科学GPUjobなし。

次の具体的アクション: 元10Bのpacked-block学習と固定Base短いprefix生成のBOS/文書境界・過去文脈条件を、既存trainer/config/shard・保存済み診断から棚卸しする。旧診断との重複を確認し、未測定の差があればそれ一つのTRAIN限定診断を上限と完了条件付きで定義・実装してから実行する。全corpusの再scan・重複照合・Tokenizer再学習をしない。今回の未来教師条件や予算不合格の構造比較を再開しない。

Base未完成・未採用。独立学習seed/full DEV/protected final TEST/adoptionは資格のある候補にのみ行い、今回は未実施。実Base完成時にユーザーへ知らせて停止し、Chat/Dialogue/SFT/量子化に進まない。Python3.12.7はWSL uv、local verified commitのみ、自動pushなし。Phase0–3/旧数値7失敗/全負の結果を保存。直前の待機turnはactual701073の実稼働と教師更新を確認したverified wait、今回は実終了・全80採点・採否保存のprogress。以下は過去の履歴。


追加準備／実学習継続（2026-10-07 JST）: actual701073/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start20668823を再確認。21:56:27Zに18,191,049元教師/3,220更新/loss3.343921有限、checkpoint-00003000.ptを保持。前goal turnはdiagnostic完了・科学実起動・39ad757 commitのprogress。complete_base_next_two_token.pyを追加し、実終了・凍結review/raw notes・元UI実process/HTTP復帰に基づく終端記録と可搬archiveを準備、uv pinned CPU AST構文成功。live jobにはまだ実行していない。次は本学習と全日本語/80生成の実終了を待ち、全80個別採点→review_base_next_two_token.py→complete_base_next_two_token.py→Windowsへbundle SHA確認→local commit。未合格条件の救済延長・Chat/量子化なし、Base未完成・未採用。

Base限定・Attention診断終了／next-two補助学習100Mを実WSL CUDAで開始（2026-10-07 JST）。

[Attention診断の完了記録](../reports/phase6/base_attention_saturation_completion.json): 固定TRAIN24文書を使い元10B・既存CE100M・fresh calibrationを読み取り専用で観測。CPU4checks/1.39秒、実CUDA3.526430秒、診断7,596位置、科学更新・新品質評価0。事前の広範な飽和markerに該当するlayerは両学習済みendpointの各sourceで0/13。集中queryは1.71–2.56%、主にBOSであり、Attentionが生成失敗の原因だと示す結果ではない。このmarkerによるQK正規化等の変更を開始しない。全native出力・重み・RNG・hook復元を確認し実process終了、24text/4,363,514byteのgzip証拠667,323byteをWindowsへ保存してSHA照合。旧構造比較の予算不合格・負の結果は維持する。

[next-twoの固定案](../reports/phase6/base_next_two_token_proposal.json)・[実CUDA probe完了](../reports/phase6/base_next_two_token_probe_completion.json): native推論10,001,152paramsを保持し、学習専用688,896paramsのcausal contextual headで2トークン先の同じTRAIN goldを予測する。総学習params10,690,048、L=CE_next1+0.1*CE_next2。元teacher100M（Web75M/教材20M/物語5M）と追加next-two教師を別計数し、新教材・同総教師の効率比較とはしない。CPU core5checks/3.37秒、runner5checks/1.35秒、reviewer22checks/2.82秒。実CUDA probe10.010668秒、48検証更新、元279,240/追加253,920教師（科学学習と区別）、保存再開等18checksと初期native不変7checksに合格。batch48、worst peak11,987,593,728bytes、全32timingの元教師/秒中央値44,940.8。元100M学習予測2,225.15秒、保存・評価を含む凍結GPU上限3,793秒（当初3,965以内）。24text/1,182,383byteのgzip証拠343,096byteをWindowsへ保存・SHA照合済み。probe重みは本学習へ流用しない。

[実本学習の起動記録](../reports/phase6/base_next_two_token_science_start.json): run reports/phase6/base-next-two-token-comparison-20261007、actual PID701073/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start20668823、Windows worker32056、開始2026-10-06T21:51:25Z。config SHA dcd0247be516eb73e07e9b71aca27493f1d914b88270139651408ef3fae59563。21:54:43Zに実process稼働、元11,856,189教師/2,100完了更新、loss3.225421有限、checkpoint-00002000.ptを確認。RTX4090/WSL、GPU allocator90%、WSL空き97GB。250更新ごとに全native・aux・Adam・scheduler・RNG・sampler・教師会計を保存、20更新ごとにheartbeat、全完了更新metricsを保持。science中UI停止、終端launcherが元10Bへ復帰する。restartは scripts/run_base_next_two_token.ps1 -Worker。先に実PID/boot/start不在と有効checkpointを確認し、同凍結source・同累積GPU予算内でのみ再開。重複起動しない。

次の具体的アクション: 元100M終端→同byte BPB/日本語選択式/固定80生成→新80全内容の個別raw-bound採点と既存CE80の再利用→事前のrelative・strong・absolute・historical Web基準で判定する。next-two位置のない更新ではaux Adamが進まないことを全metricsから別に検証する。固定horizon2/係数0.1/headが不合格ならこの条件を閉じ、horizon/係数/LR/source/epoch/教師量/上限の救済変更をしない。基準を満たす候補だけ独立学習seed/full DEV/protected final TEST/adoptionへ進む。

Base未完成・未採用。品質基準を維持し、実Base完成時にユーザーへ知らせて停止する。Chat/Dialogue/SFT/量子化は開始しない。Python3.12.7はWSL uv経由、local verified commitのみ、自動pushなし。Phase0–3と過去の負の結果を保存。以下は過去の履歴。


Base限定・共有K/V診断と構造比較の実GPU準備終了／300M本学習は予算未達で未開始（2026-10-07 JST）。

[共有K/V診断の完了記録](../reports/phase6/base_kv_head_gradient_completion.json)・[最新の失敗経路統合](../reports/phase6/base_post_smoothing_root_synthesis.json): 元10Bと既存CE100Mへ、前回固定のTRAIN24文書（Web/教材/物語各8family）の同じ窓を使用。5CPU checks/0.90秒、実FP32 CUDA2.693570秒/180、5,064診断位置、optimizer/科学教師/新品質評価0。全native logits/loss/共有勾配の分解と重み・tied・RNG・forward復元を確認し、actual696961/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start20436942は終了・実process不在。両endpointの全3sourceで事前cosine<=-.1/cancellation<=.9の研究markerを満たす。一方、各sourceの全26共有groupで通常の合算更新が片方のhead経路に逆向きになる件数は0。局所的相殺でありGQAが生成失敗の原因という証明ではなく、同一損失のhead-pathへPCGradを適用しない。33text/392,639byte gzipの証拠をWindowsへ保存・bundle SHA確認。

[固定構造配分案](../reports/phase6/base_kv_allocation_proposal.json): GQA4Q/2KV/FFN640は実10,001,152、MHA4Q/4KV/FFN560は10,054,400（+53,248/+0.5324%）。他の13layer/hidden256/Tokenizer4096/NoNorm/native推論は同じ。これはattention対FFNの配分比較であり、KVだけの因果比較や完全同数paramsではない。両fresh seed42/fresh AdamW、同accepted2B TRAIN、各300M元gold（Web225M/教材60M/物語15M）、5M warmup+295M cosine、同DEV全80/日本語評価、全研究・strong/absolute/historical Web基準を維持する案。旧成熟CE100Mをfresh対照として流用しない。

CEOnlyOriginalSampler/FreshKVAllocationTrainerを別実装。不要な文ペア抽出を省くがoriginal body SHA/BOS・EOS/1024context512教師stride/既読mask/全source cursorを保つ。CPU9checks/3.26秒で元gold/bytes/長文overlap・fresh初期化・両構造full state/history4対2+save/resume+2・target位置LR・改変拒否を確認。実TRAIN first32窓の元samplerとのgold/bytes/EOS/draws一致をCPU0.172572秒で確認、全corpus再scanなし。新sampler種別/auxiliary metadataは別と明記し旧InfoNCE full-stateと同一だとはしない。

[最初の実CUDA probe](../reports/phase6/base_kv_allocation_probe_completion.json): actual697431/同boot/start20511441はcomplete・実process不在、CUDA24.499315秒。両native BF16 finite/全state保存再開/同original stream成功、90% residentで共通stable48/64/80/96、112は両OOM後に増量停止。共通最速80、worst1024/512 peakはGQA17,793,596,416/MHA17,137,370,112bytes。科学各300Mの予測GPU（保存・評価margin含む）はGQA6,983/MHA5,138、probe込み12,145.499秒で固定9,000秒超過。このflat protocolは予算不合格で終了し、科学GPU/教師/新品質評価0。24text可搬archive保存、capの引上げや教師量の隠れた削減をしない。

[長さgroup高速化の実GPU比較](../reports/phase6/base_kv_allocation_bucketed_completion.json): 元のlogical batch/教師分母を保持し、近い長さのforward/backwardを分けて最後に一回のglobal clip/Adam/target LR更新をする別trainerを実装。CPU4checks/3.40秒で不均一groupのnative CE/全勾配一致と両構造のown full state再開に合格。BF16の蓄積順が変わるため旧CUDA更新とbit-identicalとはしない。実GPUのloss絶対差はGQA1.18e-6/MHA1.09e-5、全勾配relative L2は両約0.00296（固定許容内）。original教師/source/EOS/bodybytes/digest/全sampler・LRはflat/grouped/両構造で一致、PAD physicalだけ異なる。全32timed steps/各routeを保持し有利な部分選定なし。

|native構造|flatの教師/秒中央値|length groupの教師/秒中央値|実測比|
|---|---:|---:|---:|
|GQA|53,777|65,778|1.223|
|MHA|86,101|68,383|0.794|

同32stepsの各308,066教師に対しphysical inputsは1,314,080→435,022へ低下するが、MHAは小forwardの回数増で遅くなった可能性がある（profilingによる因果証明ではない）。actual698609/同boot/start20529714は終了・実process不在、CUDA31.330358秒。両prototype合計55.829673秒で当初180秒以内。grouped各300M予測はGQA6,830/MHA6,604＋全prototypeで13,489.830秒、同9,000秒上限外。この単一効率化案も終了し、別bucket/追加timing/batch/LR/source/epoch/teacher/cap救済や科学学習を開始しない。28text/3,456,783byte・gzip962,478byteのraw証拠をWindowsへ保存・bundle SHA確認。短いsource timingは全300M実時間の保証やモデル品質の証明ではない。MHAは未学習なので生成品質不合格という結論にしない。

元10B UI actual698737/同boot/start20533254は実processとHTTP親SHA410f975d…/training_tokens10,000,007,168/busy=falseで復帰確認。科学GPUjobなし。次の具体的アクション: 保存済みの今回の予算・局所K/V診断・旧depth/width/実8K学習・元raw生成の固定証拠を使い、約10Mの容量/日本語表現で残る未検証原因を整理する。次の科学recipeは未選定・新科学commandを未実装のまま実行しない。新規比較は一条件の教師/GPU上限・完了条件を先に定義する。今回のMHA300M/同効率化の枠を再開・拡大しない。

Base未完成・未採用。独立学習seed/full DEV/protected TEST/adoptionは品質資格のある候補だけに行う。実Base完成時にユーザーへ知らせて停止し、Chat/Dialogue/SFT/量子化に進まない。Phase0–3/旧数値7失敗/元全品質基準を保持。WSL pinned uv/Python3.12.7・local verified commitのみ、自動pushなし。以下は過去の履歴。
Base限定・ラベル平滑化100Mの全評価終了、不採用（2026-10-07 JST）。

[完了記録](../reports/phase6/base_label_smoothing_comparison_completion.json)・[全80採点と比較](../reports/phase6/base_label_smoothing_comparison_review.json): actual693649/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start20212215はcomplete・実process不在。正確100,000,000元gold教師/17,698更新、GPU占有1,432.763981秒（23.9分）/凍結3,583秒。native10,001,152・追加param/推論変更0、固定epsilon0.1/full4096、重み付きgold mass90M/uniform mass10M・uniform soft positions100M。全native/Adam/scheduler/CPU・CUDA RNG/full sampler/全17,698完了履歴と0.9/0.1の会計をreview済み。同元gold/source/EOS/input/physical/digest/full samplerがcached CE100Mと一致、対照GPU再実行0・新corpus0。jobの99,900,395教師/17,680更新は最後のtraining heartbeatであり、terminal train-result/full stateの正確100Mを完了根拠とする。checkpoint SHA5d6ae5726c63b69edb7d7f7b74c232fe1b3d2093f5297787df1ce6ed42a7869b。

|条件|共通byte BPB|文法2/80|一貫性2/80|適切完結/80|EOS/80|反復/80|
|---|---:|---:|---:|---:|---:|---:|
|既存CE100M|0.998487|44|2|2|19|45|
|ラベル平滑化100M|1.045711|58|2|1|27|42|

EOS+8と文法+14、反復-3という点の改善はあるが、一貫性差0/paired CI[-.0375,.0375]、適切完結2→1で生成品質の根本改善には至らない。共通256文書/472,055byteのBPBは+0.047224/CI[0.045345,0.049156]（4.73%悪化）。新意味59.896%/JBLiMP79.154%/JCQA32.082%、意味のCE差-2.604pp/CI[-5.221pp,0]。旧strong/absolute/historical Web・matched全gate未達、最終Base検証eligible=false。固定epsilon/full-vocabulary条件を終了し、epsilon/語彙support/LR/source/checkpoint/epoch救済や自動延長をしない。

新全80はraw SHA付きCodex個別非blind判定で、独立人手なし・旧CE80採点は変更しない。base-057は二＋一を三つと正しく一文で補うため内容一貫性2だが、大量改行の反復・上限停止により完結0。base-086は既存CEの同文と同じ2/2/2/完結1を維持。自動反復falseでも手動で観察した循環を理由に記録する。48text/109,419,403bytesのraw証拠とlossless gzip46,887,710bytes（SHA9ca6c083b67d132013657d460abd55a3d072f93a5ac6834dab3329e1e1139fb6）をWindowsへ可搬保存、tensor/dataは元WSL pathに保持。元10B UI actual695344/同boot/start20355937を実processとHTTP親SHA410f975d…/training_tokens10,000,007,168/busy=falseで復帰確認。科学GPUjobなし。

次の具体的アクション: 既存のBase失敗経路の合成記録へ今回の結果を統合し、学習済みのKL保存/Dropout/contrast/parameter-anchor/ラベル平滑化を繰り返さず、未検証の根本原因比較を一つに絞る。先に実source/既存negative/一次根拠/教師・GPU上限と完了条件を定義する。新科学recipeは未選定・新GPU未起動。Base未完成・未採用。資格のある候補だけ独立学習seed/full DEV/protected final TEST/adoptionへ進め、実Base完成時に通知して停止。Chat/Dialogue/SFT/量子化なし、WSL pinned uv/local verified commitのみ/pushなし。Phase0–3・旧数値7失敗・元品質条件を保持。以下は過去の履歴。
Base限定・ラベル平滑化100M比較を実WSL CUDAで開始（2026-10-07 JST）。

[検証完了](../reports/phase6/base_label_smoothing_prototype_completion.json)・[実起動記録](../reports/phase6/base_label_smoothing_science_start.json)。actual693649/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start20212215、Windowsworker32536を実processで確認。凍結config SHA0332d41532e2b861559bf7c28395e1dca91263154bebf8ef72630b51cb63d16d、run reports/phase6/base-label-smoothing-comparison-20261007。最新確認は6661649元gold教師/1180更新/combined loss3.63441228866577有限、保存checkpointは/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-label-smoothing-comparison-20261007/smoothing/checkpoint-00001000.pt。同accepted2B TRAIN/原10B親/元1024context・512teacher stride/同batch48・seed42/同source75M・20M・5M/同fresh AdamW1e-5 WD.1を保持。元gold100M positions、重み付きgold mass90M/uniform mass10M・soft positions100Mを別会計。対照CE100Mは既存結果/全80notesを再利用、GPU再実行0。

元probeは9初期/14再開checksに実CUDA合格、worst1024形状peak10,756,030,976byte、最初5step中央値33,021.92から予算見込み4,836.78秒は元3,965秒上限外。そのまま科学学習を始めず、固定32step追加測定と元5を全37含めた中央値40,980.03/見込み4,073秒も上限外として保存し、その測定を終了。48個のteacher転送をCPU側でまとめて1回のH2DにするPackedLabelSmoothingTrainerを追加、損失/元trainer・sourceを変更しない。関連CPU2checks/3.86秒、実packed全16checks（own4対2+2全state、cached元4全数値、同32step履歴を含む）一致。新32測定の全中央値48,459.78 tokens/秒、100M見込み2,063.57秒、保存・評価込みceil(見込み*1.3+900)=3,583秒へ凍結（元上限3,965秒以内）。別process warmupがあるので全速度差を転送だけの因果効果と断定しない。三つのprototypeはすべて終端・実process不在、GPU合計20.911519秒/180、93検証更新・541,359教師を科学学習と別会計し重みは流用しない。45text/1,969,120bytesをlossless gzip618,927bytesへ可搬保存。科学runnerCPU5checks/0.79秒、PS構文成功。

review_base_label_smoothing.pyと固定review policyを準備し、native全Adam・scheduler・CPU/CUDA RNG・full sampler・完了history・0.9/0.1 loss/mass・改変support・未終了拒否をCPU22checks/2.24秒で確認。fixtureは品質証明でなく、新生成はまだ未採点。次は科学100M終端→同body256bytes/日本語192・331・1119/全80→新80個別内容と旧CE80で同matched/strong/absolute/historical Web全gate判定。固定epsilon0.1/full4096が失敗したらこの条件を閉じ、epsilon/語彙support/LR/source/checkpoint/epoch救済をしない。資格のある候補だけ独立学習seed/full DEV/protected final TEST/adoptionへ進む。

Base未完成・未採用。実Base完成時に通知して停止し、Chat/Dialogue/SFT/量子化を開始しない。旧数値7失敗・品質条件・Phase0–3と負の結果を保持。WSL pinned uv、永続job/実PID/保存・再開、local verified commitのみ/pushなし。restartは scripts/run_base_label_smoothing.ps1 -Worker、先に実PID/boot/start不在と有効checkpointを確認し、同凍結累積予算内でのみ再開。科学中UI停止、終端launcherが元10B UIを復帰する。以下は過去の履歴。
Base限定・共有埋め込みのreadonly勾配診断完了／次の出力正則化を準備（2026-10-07 JST）。

[実CUDA診断完了](../reports/phase6/base_embedding_gradient_completion.json): actual691868/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start20101380はcomplete・実process不在。accepted2B TRAINのWeb/textbook/story各8distinct family、計24文書の元first/last窓を固定（今回は全24が一窓）。index-byte biased sampling/seed2026100741、原10B対cached CE100Mの両checkpointへ同24窓を使用、合計5,064診断target positions、学習更新/科学教師/DEV/TEST0。CPU3checks/0.88秒、実FP32 math CUDA2.030722秒/180・peak540,574,208byte。入力/出力分離用の一時leafは保存せず、両forwardのnative logits/loss一致と全tied勾配=input+outputの分解、全native重み/tied/RNG不変・蓄積gradなしを確認。

|checkpoint|Webの勾配cosine|教材の勾配cosine|物語の勾配cosine|
|---|---:|---:|---:|
|元10B|-0.010855|-0.002039|-0.007949|
|同CE100M|-0.005295|0.000402|0.012116|

両endpointの2/3source以上でcosine<=-0.1かつcancellation ratio<=0.9という事前研究screenは両方不合格。個々の語彙行に負のdotがあってもglobal勾配の強い相殺とはしない。cancellation ratioは直交でも1未満なので単独の証拠にしない。小さいTRAIN sample・first/last窓・FP32に限る局所結果で、共有が常に無害/10M容量が十分という証明ではない。この固定診断を終了し、同仮説によるgradient projection/untied構造学習、sample/閾値救済を開始しない。[weight tying論文](https://aclanthology.org/E17-2025/)も共有を推奨しており、共有解除の成功根拠に置換しない。22text/824,456byteのraw証拠とlossless gzip256,763byteをWindowsへ保存。元10B UI actual691937/同boot/start20102004を実process/HTTP親SHA410f975d…/busy=falseで復帰確認。

[単一ラベル平滑化案](../reports/phase6/base_label_smoothing_proposal.json)・[CPU準備の実証](../reports/phase6/base_label_smoothing_preparation.json): まだ未確認の出力分布の正則化を一条件で比較する。過度な確信が唯一原因と断定せず、[先行研究](https://arxiv.org/abs/1701.06548)を日本語10Mの改善証明にしない。固定epsilon0.1、native4096全語彙（EOS/予約ID含む）へ0.9*元gold CE+0.1*uniform CE。元10B/同accepted2B TRAIN/元body+EOS・source75M/20M/5M・batch48/seed42/fresh AdamW1e-5 WD.1 constantとexact100M元gold positionsをcached CEへ揃え、対照GPUを再実行しない。native追加param0・推論変更0・新corpus0。教師位置100Mと重み付き元target mass90M/uniform mass10M・uniform soft positions100Mを分けて記録する。パディング/既読overlapは損失外。未検証のnative samplingやEOS調整へ置換しない。

scripts/base_label_smoothing.py と独立base_label_smoothing_trainer.pyを実装。損失/厳密勾配/教師mask/epsilon0のCE一致をCPU3checks/1.38秒、native初期重み/logits/parameters/tied/RNG一致・同source/教師/EOS/input/physical/digest/full sampler・全state/history4対2+save/resume+2一致・旧CE/改変recipe/eval学習拒否をCPU4checks/3.36秒で確認。浮動target massの累積丸めを避け、完了更新の整数教師総数から0.9*Nと0.1*Nを算出する。fixtureは小CPU modelで実native CUDA/品質ではない。旧corpusを再scanせず、closed dropout/UL/gradient仮説は改変・延長しない。

次の具体的アクション: 専用の永続CUDA probe commandを実装する（まだ未実装のcommandを実行しない）。CPU30秒/実CUDA180秒でnative10M・BF16 finite gradient、own全state4対2+2、uniform会計、最大実window/90percent resident安定batch48速度を確認しprobe重みを捨てる。実測100M/median速度*1.3+900秒が3,965秒以内の場合だけ科学config/永続runnerを凍結して新smoothed100Mを開始する。終了後の同256bytes/全日本語/新80個別内容と既存CE80/strong/absolute/historical Web全gateを維持する。失敗時は固定epsilon/full-vocabulary recipe終了、epsilon/語彙support/LR/source/checkpoint/epoch救済なし。

ラベル平滑化の新GPU学習/科学教師は0、科学・probe runner未実装。Base未完成・未採用、全五目標未完了。資格のある候補だけ独立学習seed/full DEV/protected final TEST/adoptionへ進め、実Base完成時に通知して停止。Chat/Dialogue/SFT/量子化なし、WSL pinned uv/local verified commitのみ/pushなし。旧数値7失敗とPhase0–3・元全品質条件を保持。以下は過去の履歴。
Base限定・Dropout100Mの全評価終了、不採用（2026-10-07 JST）。

[完了記録](../reports/phase6/base_residual_dropout_comparison_completion.json)・[全80採点と比較](../reports/phase6/base_residual_dropout_comparison_review.json): actual689085/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start19897021はcomplete・実process不在。正確100,000,000 CE教師/17,698更新、学習・保存・全評価込みGPU占有1,467.667秒（24.5分）/上限3,965。native10,001,152・追加param0、学習時のみ固定Dropout0.1。全state/Adam/scheduler/CPU・CUDA RNG/source sampler/完了更新historyの最終reviewに成功し、同CE教師/EOS/input/physical/digest/full cursorがcached CE100Mと一致。対照GPU再実行0、auxiliary教師・入力0、旧corpus再scanなし。job最終heartbeatの99,900,395教師は保存前の値で、terminal train-result/full stateの正確100Mを完了根拠とする。

|条件|BPB|文法2/80|一貫性2/80|適切完結/80|EOS/80|反復/80|
|---|---:|---:|---:|---:|---:|---:|
|既存CE100M|0.998487|44|2|2|19|45|
|新Dropout100M|1.023869|55|1|1|13|43|

新条件の関連2=21/80、意味60.417%/JBLiMP77.341%/JCQA35.299%、Unicode・role・empty0。CE比の一貫性-1/paired CI[-.05,.025]で独立seedの有意差証明ではない。共通256文書/472,055byteのBPBは+0.025381/CI[0.023991,0.026815]で悪化。同192意味は-2.083pp/CI[-7.292pp,3.125pp]。元strong/absolute/historical Web・matched全gateを満たさず、最終Base検証eligible=false。固定Dropout recipeを終了し確率/sites/LR/source/checkpoint/epoch救済や自動延長を行わない。

新全80はraw SHA付き個別非blind Codex判定。独立人手なし・旧CE80採点は変更しない。base-051の「残りは食べた」は残ったりんごを後で食べる短い読みとして関連/一貫性1・EOS完結1、残数二個の正解や満点とはしない。43text/103,603,956byteのlossless archiveと圧縮49,205,820byte/SHA ebf86ea351acc05f082ec3a2f0f62cbe1f5084bd372c8f65c54c4e16b7bcbea7を保存、Windowsへ全raw評価・notes/review/completionと圧縮証拠を復元。tensor/dataは元WSL pathに保持。

元10B UI actual690043/同boot/start20044230は実process生存・HTTP親SHA410f975d…/10,000,007,168入力training tokens/busy=falseを確認。GPU科学jobは終了済み、UIは http://127.0.0.1:7860 。完了した比較を再起動しない。

次の具体的アクション: 終了済みBase機構とTRAIN→DEV転移の証拠を再利用し、未検証の比較を一つに絞って元採否条件・教師/GPU上限・終了条件を先に明示する。終了済み診断/全corpus照合や救済sweepは繰り返さない。新科学recipeはまだ選定・起動していない。Baseは未完成・未採用。資格のある候補だけ独立学習seed/full DEV/protected final TEST/adoptionへ進め、実際のBase完成時に通知して停止。Chat/Dialogue/SFT/量子化なし。WSL pinned uv/local verified commitのみ/pushなし、Phase0–3と旧数値7失敗・元全条件を保持。以下は過去の履歴。
Base限定・Dropout100Mを維持／採否処理の準備完了（2026-10-07 JST）。

[採否準備の証拠](../reports/phase6/base_residual_dropout_review_preparation.json): 新 scripts/review_base_residual_dropout.py と凍結policyを追加、CPU18checks/2.43秒に合格。既存CE80/同256byte/同192意味cacheを使う実CPU API・実live最終CLI拒否確認は2.075秒、GPU/新教師/新内容採点0。準備用callerが意味paired結果のtop-level pointを誤参照した初回KeyErrorを別JSONに保存し、candidate_minus_controlへ修正して成功。frozen科学/reviewerや採点は変更していない。

最終reviewはnative10M/全Adam/scheduler/CPU・CUDA RNG/source sampler/完了更新全historyと正確100Mを要求し、追加headやauxiliary入力・目的、確率/sites/推論Dropoutの改変を拒否する。全CE入力/physical/教師/EOS/digest/full cursorをcached CEへ揃える。中断後は後attemptのcommitted pathを使い、切れた未完末尾rawを保持、欠損完了更新や改行付き壊れた行を拒否。既存CE80採点は変更せず、元strong/absolute/historical Web gateを維持。byte-weighted BPB/同192 exact-input cluster意味CIは補足で採用条件を緩和しない。

actual689085/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start19897021を実ps確認。8060更新/45604736教師/loss2.88087725639343有限、latest completed CP /home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-residual-dropout-comparison-20261007/dropout/checkpoint-00008000.pt。同job/確率0.1/batch48/3965秒/source/configは固定、重複GPUjobや対照再評価なし。

新native80と全日本語が完了してから、native cwdでWSL pinned uv run --frozen --extra hub --extra data --extra ml --extra export scripts/review_base_residual_dropout.py --template を実行し未採点notesを作る。全80を個別に読み六列TSV reports/phase6/base_residual_dropout_observations.tsv を記録後、同uv prefix＋同script --record reports/phase6/base_residual_dropout_observations.tsv で取り込む。実master completeかつPID/boot/startが実ps不在になってからだけ、同uv prefix＋同script引数なしでfinal reviewを保存する。live拒否と最終artifact不在を実確認、scored notes/reviewの上書きを拒否する。

Base未完成・未採用、資格のある候補だけ独立学習seed/full DEV/protected final TEST/adoption。Base完成時に通知して停止し、Chat/Dialogue/SFT/量子化なし。新prepared/GPU品質/独立人間評価として準備やfixtureを扱わない。WSL uv/local verified commitのみ/pushなし、旧数値失敗・Phase0–3と元全条件を保持。以下は過去の履歴。
Base限定・学習時Dropoutの実CUDA確認完了／100M比較実行中（2026-10-07 JST）。

[単一仮説](../reports/phase6/base_residual_dropout_proposal.json)を実装。既存512TRAINの適合改善とDEV生成退行、source-local DEVへの転移失敗から、学習時のco-adaptation抑制を一条件で試す。一般的な[Dropout一次論文](https://jmlr.org/papers/v15/srivastava14a.html)からの仮説で、日本語10M改善の証明ではない。確率0.1をtoken embeddingと各attention/MLP残差出力に適用し、attention probabilityは0、追加パラメータ0、native推論10,001,152を保持。元src/jmicro/model.pyを変更せずtrain-only hooksを新trainerに付け、既存torch RNGを全stateへ保存する。native評価ではhooksを付けない。

[実probe完了](../reports/phase6/base_residual_dropout_probe_completion.json): CPU5checks/2.96秒＋runner3checks/1.32秒、実CUDA9.546565秒/180。native初期重み/tied/logits/RNG、学習mask有効/推論mask無効を確認し、4対2+save/resume+2の全13state/history checks一致。44検証更新/220,036教師は科学と別、probe重みは捨てる。actual688679/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start19876351は実終了・ps不在。17text/716,702byte archiveと原文SHA付きconfig/source/testsを保存、元UI688753/start19877709を復帰・実ps確認してから科学へ移行した。

全source batch16/32/48/64を測定、64が測定内最速58,060教師tokens/秒・最大context1024/最大512教師strideでpeak13.713GiB。測定を超える最大stable batchは未確認。科学は既存CE100Mとの同batch/source/cursorを保つ48、実測44,579教師tokens/秒・worst peak10.333GiB、90percent resident制限内。新教材量/独立品質の証明ではない。旧13GBindex再scanやTokenizer再学習なし。

[科学開始記録](../reports/phase6/base_residual_dropout_comparison_start.json): actual689085/同boot/start19897021、Windowsworker26960を実ps/start確認。native run reports/phase6/base-residual-dropout-comparison-20261007、凍結config SHA bd36050f4ec23798186e020098de54cbffab16f36554c6c0dbc064192875051a。600更新/3,394,390教師/loss有限まで実学習を確認。元10B親、accepted2B TRAIN、正確Web75M/textbook20M/story5M教師、batch48/seed42/fresh AdamW1e-5 WD0.1/constant、元本文+元EOSを固定。既存ordinary CE100MのGPU/全80採点を再利用し対照再実行0、auxiliary loss/input0。Dropout100Mのみ新科学、比較終端で教師/EOS/入力/physical/digest/full samplerまで同じことを要求する。

短い実測から学習予測2,243.203秒（37.4分）、科学GPU上限3,965秒（66.1分、保存/評価込み）。実際の完了時刻やBase品質達成期限ではない。250update completed-update checkpointと20update heartbeat/PID付きmetrics、native/Adam/scheduler/RNG/sampler/countersを永続保存。科学中は元UI停止、worker finallyで元10Bへ戻す。中断時のみactual PID/boot/start不在とvalid CP/残予算を確認後、scripts/run_base_residual_dropout.ps1 -Workerで同configから再開し、completed jobを再起動しない。

次は同科学jobを維持して、終了後の新全80個別内容/旧CE80/strong/historical Web/共通byte/日本語・元全gateを確認するreviewerを実装・CPU確認する。凍結scientific source/configや確率/sitesを変更しない。失敗ならこの固定条件を終了し確率/sites/LR/source/epoch sweep・自動延長なし。合格candidateだけ独立学習seed/full DEV/protected final TEST/adoptionへ進める。Base未完成、完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。WSL pinned uv/local verified commitのみ/pushなし、旧数値失敗とPhase0–3保存。以下は過去の履歴。
Base限定・projection100Mの全評価終了、不採用（2026-10-07 JST）。

[完了記録](../reports/phase6/natural_context_contrast_projection_comparison_completion.json)・[全80採点と比較](../reports/phase6/natural_context_contrast_projection_comparison_review.json): actual685602/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start19518840は実終了・ps不在。新科学100,000,000 CE教師/17,698更新、native10,001,152＋train-only98,304param。GPU占有2,382.820秒（39.7分）/上限5,009。既存CE/direct各100Mの全会計/digest/source quota/EOS/full sampler一致、対照GPU再実行0。全state/historyと全日本語/生成80の実reviewに成功、旧160採点は変更しない。

|条件|BPB|文法2/80|一貫性2/80|適切完結/80|EOS/80|反復/80|
|---|---:|---:|---:|---:|---:|---:|
|既存CE100M|0.998487|44|2|2|19|45|
|既存direct contrast100M|1.002890|48|0|3|6|53|
|新projection100M|1.000722|57|4|3|21|47|

新条件の意味62.500%/JBLiMP77.644%/JCQA34.495%、Unicode/role/empty0。文法は改善するが、一貫性/適切完結/停止/反復とhistorical Web BPB guard等は不合格。CE比の一貫性+2/paired CI[-.025,.075]、direct比+4/CI[.0125,.1]で元+8条件未達。strong比-19/CI[-.3375,-.1375]。共通byte BPBはCE比+0.002235/CI[0.001920,0.002551]で悪化、同192意味はCE比0/CI[-.020833,.020833]。補助headでBase品質問題が解消したとは言えない。この固定recipeを終了しhead/LR/係数/source/epoch/checkpoint救済・自動延長は行わない。

全80は非blind Codex個別判定、独立人手なし。41text/106,225,836byteの原文archiveとlossless gzip52,105,787byteを保存し、tensor/dataは元WSL path。Windowsに全評価/notes/review/completionと圧縮証拠を復元。元10B UI actual686877/同boot/start19757580は実psとHTTP親SHA410f975d…/10,000,007,168/busy=false確認済み。科学GPUjobなし、元10B UIを維持する。

[限定CPU調査](../reports/phase6/base_capacity_reference_synthesis.json): 公開TinyStories-8Mの固定revision8612e3b15c66ffa94eaa6ee0de5c96edd2d630afのconfigのみ取得し、CPU metaで6.393秒、GPU/学習/weight取得0。公開config全19,702,528param（token埋込12,865,792）に対し現nativeは全10,001,152で、名称だけで同容量とは扱えない。[論文](https://arxiv.org/html/2305.07759v2)はtop10K語彙と短い単純な英語物語を記述し、公開full50,257語彙/2048位置との違いを保持する。同公開構造をphysical10Kにした9,396,736は明示counterfactualで論文重みの再現ではなく、旧BOS/EOS範囲warningも保存して推論しない。旧depth/width/FFN比較・量/学習比較、512TRAIN fittingとsource-local DEV転移診断の既存証拠を再利用。10M容量限界、全設定不可能、Tokenizer不良を断定しない。

次は既存trainfit/generalization/source rawに基づき、未検証の生成への転移機構を一つ選んで、同10M/対照/教師/完了条件と実測GPU予算を明示する。新科学recipeはまだ選定・起動していない。終了済み診断、全corpus照合や構造/比率総当たりは繰り返さない。Base未完成・未採用、元全品質条件/独立学習seed/full DEV/protected TEST/adoptionは未達のまま保持。Base完成時にユーザーへ通知して停止し、Chat/Dialogue/SFT/量子化へ進まない。WSL pinned uv/local verified commitのみ、自動pushなし。以下は過去の履歴。
現在のBase限定milestone（2026-10-07 JST）。

[projected100M終了後の採否処理](../reports/phase6/natural_context_contrast_projection_review_preparation.json)を実装・CPU17checksに合格。新80全内容と旧160を同raw-boundで使い、同CE/cursor・別head/全optimizer/RNG・全committed logを確認して元strong/両matched/absolute/historical Web条件を維持する。共通byte BPB/同192 exact-input意味CIは補足、完成/採用へ置換しない。

実scientific685602は同100Mへ継続、確認時22,624,125教師/4,000更新と保存CP/loss有限。次は終端・新80全内容・元全gate、資格がある候補のみ独立学習seed/full DEV/protected final TEST/adoption、完成Base通知停止。Chat/Dialogue/SFT/量子化なし、元基準/旧失敗保持、以下は過去の履歴。
現在のBase限定milestone（2026-10-07 JST）。

[train-only projection試験](../reports/phase6/natural_context_contrast_projection_probe_completion.json)は実CUDA11.138秒/全state14checks合格。推論10Mと追加98,304の学習headを分け、初期native重み/logits/RNGを維持。全source batch48でresident容量と再開を確認したため、[同100M比較](../reports/phase6/natural_context_contrast_projection_comparison_start.json)を永続実行開始。元10B/2B教材・元各75/20/5M教師・同batch48/fresh Adam/seedを保持し、既存CE/direct100Mは再学習・再評価しない。新headは評価で破棄、同CE digest/会計/full samplerと追加計算を別に報告する。

次は終端100M/同固定DEVと新生成80全内容→既存strong/matched/absolute/historical Web gate。識別loss・コード・再開だけでBase完成にしない。資格がある候補だけ独立学習seed/full DEV/protected final TEST/adoptionへ進み、Base完成時通知停止。Chat/Dialogue/SFT/量子化なし、元品質条件/旧失敗/Phase0–3を保持。以下は過去の履歴。
Base限定・同64の次token尤度転移診断完了（2026-10-07 JST）。

[全3モデル×3prefix view](../reports/phase6/natural_context_contrast_likelihood_transfer_review.json): 同suffix16,509token/63,511byte、元前文BPB元10B0.981316/CE0.995055/contrast1.000546。contrast−CE+0.005491/文書byte-weighted CI[0.003823,0.007581]で、このsampleでは次token予測が改善しない。全モデルで元前文は有用、前文benefit変化のCIは0を含む。GPU2.122014秒/60・新教師/更新0、actual683973終了・ps不在/元UI復帰。前の識別改善をBase採用としない、suffix-only BPBをfull DEV guardへ代入しない。

[次のtrain-only projection仮説](../reports/phase6/natural_context_contrast_projection_proposal.json)を実装し、native語彙経路とaux識別の計算空間を分ける。推論Base10,001,152は保持、98,304の学習専用headは別計数して評価で破棄。視覚表現の[SimCLR一次論文](https://arxiv.org/abs/2002.05709v3)からの仮説で、日本語改善未証明。CPU30秒/実CUDA180秒のnative/head初期一致・有限梯度・全state再開と全source容量/速度に合格してから、同source/100M教師・同親/optimizerの一科学比較を実測予算で凍結する。既存CE/direct対照を再GPUしない。未実装・未開始、旧recipe救済やhead sweepなし。

Base未完成。元全quality gate/全80/独立学習seed/full DEV/protected final TEST/adoptionを保持し、完成時通知停止。Chat/Dialogue/SFT/量子化なし、旧失敗・Phase0–3保存。以下は過去の履歴。

Base限定・readonly DEV表現転移の診断完了（2026-10-07 JST）。

[元10B/CE/contrast同64の実レビュー](../reports/phase6/natural_context_contrast_dev_transfer_review.json): unique識別7.031%/7.813%/18.750%、contrast−CE+10.938ポイント/文書paired CI[3.906,19.531]ポイント。GPU1.501791秒/60・更新/新教師0、actual683176終了・ps不在、元UI復帰。固定DEVで識別が一部改善しても元全80生成とBase全gateの失敗は変更しない。near-family/反復DEVの限界、二方向の相関を保持。

[次の同64・3prefix view条件付き尤度診断](../reports/phase6/natural_context_contrast_likelihood_transfer_proposal.json)を実装し、元前文/固定別文書前文/BOSだけで同suffix本文のNLL/共通byteを一度ずつ測る。CPU30秒/GPU60秒・学習0、context1024/stride512・suffix target完全保持。未実装・未起動で実commandを準備してから実行する。表現の変化が次token分布へ移るかの診断で、旧recipe再調整・Base採用にしない。

Base完成時に通知停止、Chat/Dialogue/SFT/量子化なし、元全品質条件/独立学習seed/full DEV/protected TEST/adoption/失敗を保持。以下は過去の履歴。

Base限定・固定各100M比較終了、不採用（2026-10-07 JST）。

[終端と全160採否](../reports/phase6/natural_context_contrast_comparison_completion.json): 同CE accounting/cursor・各100M教師、GPU3762.998秒/5229、actual676378終了・ps不在。CE→contrastで一貫性2→0/EOS19→6/反復45→53（各80）、BPB0.998487→1.002890。意味差1.042ポイント/CI[-2.083,4.167]ポイントは改善の確証でない。全strong/matched/absolute/historical Web条件不合格、両固定recipeを終了し救済sweep・自動延長なし。

[次の一回のDEV転移診断案](../reports/phase6/natural_context_contrast_dev_transfer_proposal.json): TRAINの補助識別loss低下が未学習DEVの原文前後識別へ移ったかを元10B/CE/contrast同64で測る。CPU30秒/GPU60秒、更新・新教師0、commandは実装前で起動しない。元BOS/cache/shiftのtrained診断は[既存証拠を再利用](../reports/phase6/base_decode_cached_evidence_review.json)し、数値失敗を保存して重複GPU検査を避ける。次の学習機構を決めるための限定診断で、Base採用gateを増減しない。

Base未完成。資格のある候補だけ独立学習seed/full DEV/protected final TEST/adoptionへ進め、完成時に通知して停止。Chat/Dialogue/SFT/量子化なし、local commit/pushなし、既存失敗とPhase0–3を保持。以下は過去の履歴。

Base専用・同job継続と意味評価のsuite版確認（2026-10-07 JST）。

[固定DEV/元cacheの内容一致証拠](../reports/phase6/natural_context_contrast_semantic_review_preparation.json): 今回のv2_1はDEV192/96distinct content pair、旧teacher v2は64content pairで、同IDでもcontext88/choices40が異なる。旧と新の点数差を学習効果へ混同しない。元CE62.500%/CI[57.8125%,67.7083%]保持、補足はGPU/教師0、関連3CPUchecks成功。新版の完全重複なしをBase品質達成にしない。

同contrast100M/元全160採否へ継続。日本語のpaired CIは同じ新版・同入力に対して出し、元Base採否基準は変えない。合格candidateだけ独立seed/full DEV/protected final TEST/adoption、Base完成時通知停止、Chat/SFT/量子化なし。以下は過去の履歴。
Base限定・同100M CE対照の評価/内容完了、contrast継続（2026-10-07 JST）。

[従来CEの実終端・全80内容](../reports/phase6/natural_context_contrast_CE_completion.json): 正確100M教師/17698更新、BPB0.998487、意味62.500%/JBLiMP77.341%/JCQA35.031%、文法44/関連25/一貫性2/適切完結2/EOS19/反復45（各80）、Unicode・role・empty0。元絶対Base基準と歴史Web1% BPB guard未達でCE採用なし。全80非blind Codex notesとraw評価を保存、独立人間/最終Base品質証明とはしない。

科学actual676378は同源/各100Mのcontrast-trainingを継続、source/config/予算不変。次はcontrast100Mと全日本語/全80内容→実終了後の両arm160採否/同CE digest・会計/元全gate。資格のある固定candidateだけ独立学習seed/full DEV/protected TEST/adoption。Base完成時通知停止、Chat/SFT/量子化なし、以下は過去の履歴。
Base限定・比較学習継続、採否の準備完了（2026-10-07 JST）。

[終了後レビュー処理/実CPU確認](../reports/phase6/natural_context_contrast_review_preparation.json): 同各100M科学actual676378を継続、科学code/config不変。新reviewerは既存strong一貫性23/EOS76/反復2に対する相対条件と絶対Base/historical Webを維持し、contrastにはmatched CE改善も要求。全160個別raw-bound内容、実終端full-state/同CE digest/cursor/各教師quota/両CUDA再開/全日本語を確認する準備。CPU8checks/0.96秒とactual live最終レビュー拒否確認、GPU/新教師/内容採点0。

次は各100M終端→全日本語/生成160内容採否→資格のある固定candidateだけ独立学習seed/full DEV/protected final TEST/adoption。終端や対照との差だけでBase完成とはしない。Base完成時通知して停止、Chat/Dialogue/SFT/量子化なし。以下は過去の履歴。
現在のBase限定milestone（2026-10-07 JST）。

[全2B TRAIN供給/実CUDA完了・科学起動](../reports/phase6/natural_context_contrast_corpus_completion.json)。CPU6tests、両arm CUDA4対2+2全state/history26checksに合格。旧TRAINのdocument-local1024/stride512でbody+元EOSを一度ずつ教え、非eligible pairでもCEを保つ。元family/body negative除外・PAD/overlap head省略。旧巨大index/stream再scanなし、最大元body1024を小compact arraysで確認。source pilotの追加採用や新供給ではない。

最速同batch48、CE95472.5/contrast49069.2教師tokens/秒、最大context stress17.8658GiB。nominal128の47.4GiB allocationはresident24GiBを超えるので最大活用とはしない。process allocator90percentへ限定する実API検査済み、driver/OS設定は不変。

[科学config](../configs/phase6/natural_context_contrast_comparison.json)でactual676378/boot53f39671…/start18891158を起動。各100M CE教師/元10B親/同fresh Adam LR1e-5/同seed/source/EEOS/batch48、extra auxiliaryとGPU別会計。累積GPU5229秒、forecast学習3085.36秒。checkpoint250updates、heartbeat20、同config/残予算内のvalid completed-update再開のみ。次は両100M/同CE stream会計/固定dev256・日本語・全160内容と元Base採否。合格時のみ独立学習seed/full dev/protected final test/adoption。

Base未完成。完成時に通知停止し、Chat/Dialogue/SFT/量子化は開始しない。元全条件/旧失敗/Phase0–3保持、WSL uv/local commitのみ/pushなし。以下は過去の履歴・後続段階設計。
現在のBase限定milestone更新（2026-10-07 JST）。

[実native contrastive probe完了](../reports/phase6/natural_context_contrast_probe_completion.json)。loss/元全文CE・診断保存再開commandを実装、CPU5testsと両arm実CUDA4対2+2の全state/history26checksに合格。actual673463終了、GPU12.507994秒、検証64updates/367840 CE教師、科学0。fixed64 TRAINの最大測定batch64でCE98844.6/contrast52853.9教師tokens/秒、peak約7.1GiB、有限非zero auxiliary勾配。品質/4090全容量/本教材の速度の証明とはしない。

次はaccepted全2B TRAINの元unit/familyを保つsamplerとgenre/EOS/CE/extra auxiliary会計を実装し、本sourceの長文/より大きなbatch・保存再開を測定してから、同親fresh等しいAdam/LR・各100M CE対照の実GPU予算を凍結。固定64反復を本教材にしない、追加処理の約1.87倍時間負担も別会計。科学sampler/長期command/予算は未完成で、本比較未開始。既存教師転移/分類branchの失敗は維持。

全Base品質・独立学習seed/full DEV/protected final TEST/adoptionが完了条件。完了時に通知・停止し、Chat/Dialogue/SFT/量子化は開始しない。以下は過去の履歴・後続段階設計。
現在のBase限定milestone（2026-10-07 JST）。

[教師semantic診断完了](../reports/phase6/teacher_semantic_signal_completion.json): DEV192の平均72.917%対61.979%は教師が上だが、同内容別IDを64clusterへ補正した差CI[0,.22]は元lower>0条件未達。転移branch終了、教師feature/蒸留を開始しない。元出力/採点/nominal96family結果・全99不一致を保存し、内容aliasを独立例数にしない。保護TEST本文未使用。

[次のnative contrastive計画](../reports/phase6/natural_context_contrast_proposal.json): 既存accepted2B TRAINだけを使い、10Mの観測原文prefix/suffix hidden表現の対応をInfoNCEで学ぶ別機構を、同body+EOS CEと比較する。新head/teacher/生成教材/分割点EOSなし。固定係数/temperature各0.1、実装probe64はCPU0.306秒で準備済み。loss/実training commandを先に実装し、GPU180秒内で有限勾配・測定batch/速度・CUDA全state保存再開に合格した場合だけ本比較条件/予算を凍結。各100M CE案で追加auxiliary露出とGPUを別会計、科学jobは未開始。論文の着想をモデル改善証拠としない。失敗時の同条件救済/自動延長なし。

完了milestoneは元の全Base品質基準、独立学習seed/full DEV/protected final TEST/adoptionを満たすこと。未達のままChat等へ移らない。Base完成時に通知して停止し、Chat/Dialogue/SFT/量子化は別の再開指示まで開始しない。以下は過去の履歴・後続段階の設計資料。
Base専用・公開モデルによるsource意味判定の有限比較完了、不採用（2026-10-07 JST）。

[全64予測/採点比較](../reports/phase6/base_source_semantic_judge_review.json)と[実結果](../reports/phase6/base_source_semantic_judge_result.json)。既に全hash検証済みの公開Apache2 Qwen3-4B-Instruct-2507 revision cdbee75f17c01a7cc42f958dc650907174af0554をnativeから再利用、重み再取得0byte。以前の自然文生成recipeは不採用のまま、今回は原文記事の分類という別機構。一モデル/一prompt・greedy/BF16/SDPA・全原文保持、元gold/入力hashとsourceを予測前に凍結。元64をsource file別32development/32holdoutに固定し、holdout accepted>=8・precision>=90%/recall>=50%/format error0、GPU180秒/peak22GBを要求。判定集計の関連2CPUtests/0.02秒、PS構文・model stat/pin preflight成功後、actual669341/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start18548324で実GPU54.228秒/peak11,565,212,672bytes、全64完了・ps不在。

全64predictionの理由を読んだ。既存非blind Codex goldと比べ全64は60accept/true40/false positive20/false negative1、precision66.667%。file holdout32は31accept/true20/false positive11、precision64.516%・recall100%・format error0で事前条件を不合格。翻訳構文を文法2、未完引用後のサイト質問を完結、検索/ポイント/注文案内をboilerplate0とする。本文にない落城理由をあると述べるなど、表面的な話題の整合を主な根拠にして欠損を見逃す。出力JSONが全件parseできることと内容を正しく評価できることを区別する。固定classifier branchをここで終了しprompt/model/thresholdの救済sweep、誤採用教材による大量学習はしない。sourceの元41/64不合格や採点は改変しない。

[次のreadonly診断案](../reports/phase6/base_teacher_semantic_signal_proposal.json): 固定Japanese semantics dev192を公開4Bと元native10Mのplain-BOS conditional likelihoodで直接比較する。全context対・同じ候補・反対goldを保持し、原byte/codec境界の一致、モデル別token数、family CI、全不一致、実GPU秒を記録。Chat template/役割、生成・truncation・optimizerなし、GPU180秒・全192終端で診断終了。まだrunner未実装/未開始で新GPU/知識転移成功の証拠ではない。source classifier失敗を教師の日本語能力全体の不存在とみなさず、もしteacherの文脈信号が確認された場合だけ、共通原文の文脈特徴/例間関係を10Mへ移す新機構の同教材CE対照を設計する。語彙/Tokenizerの違うlogitsを直接同一視しない。参考RKD論文はCVPR2019で、日本語Baseに効くことは未実証。公開4Bで10Mの成果を置換しない。

既存goldは非blind Codex採点で独立人間0、prompt作成者は全64を既知。全corpus品質やBase精度・容量限界の証明ではない。原全64/hash/終端identityとscript/config/tests/results/review/proposalを可搬archiveへ保存。新training prepared0/科学教師0/optimizer0/保護test本文0。元UIをactual669495/start18554349へ復帰、HTTP元10B SHA410f975d…/10000007168tokens/busy=false確認。Base未完成、完成時に通知停止。Chat/Dialogue/SFT/量子化なし、WSL uv Python3.12.7/local commitのみ/pushなし、元品質基準・旧失敗・数値7・Phase0–3保持。以下は過去の履歴。
Base専用・固定未確認64の原親/保持本文の全内容採否完了（2026-10-07 JST）。

[全64の原親/span-bound個別採点](../reports/phase6/base_hq_acceptance_review.json): 文法2=57、一貫性2=54、原記事完結2=53、dominantサイト運用等4。全条件を同時に満たす41/64、弱23で、取得前の凍結基準54以上/弱10以下を不合格。本文内部の切れた節/引用、宣言した内容や例文の欠落、未説明の参照、反復する翻訳構文、UIを具体的に記録。正当な抽象・要旨・手順・名詞句・プロフィール・問い・署名・少数OCRを自動失敗扱いせず、政治/医療/法律/歴史/製品等の事実保証とも区別した。全原親と連続spanのSHA、char/UTF8境界、family/固定file数、元契約SHAと終端processを実WSL uvで照合し成功。検査はこの小sample内だけ、旧corpus再scan/新取得/新教師/GPU0。レビューの検査成功を内容合格とはしない。

固定構造抽出branchをここで終了し、この候補から大量学習しない。結果後のselector修正・閾値変更・同条件source再抽選なし。元取得の46.318秒/14.54MBと46463tokensはsource inspectionであって新training preparedではない。全64原文はnative base-hq-acceptance-20261007、可搬理由・原文index・コード・契約・master archiveを保存。actual665631は終了/ps不在。元10B UI actual663394とHTTP SHA410f975d…/10000007168tokens/busy=falseを維持。全Base基準と合格時の独立学習seed/full dev/protected test/adoptionは未達のまま。

次は構造抽出の再調整をせず、公開日本語対応の学習済みモデルによる文法・局所参照・記事完結の判定という別機構の可否を有限比較として定義する。重み取得前に公開性・ライセンス・4090への適合を確認し、一モデル/一prompt・固定holdout、採用条件と実GPU/供給処理の上限を先に決める。既存64採点は変更しない。判定器のholdout精度と新source適性/固有供給/family除外が確認された場合だけ新しい対照付きBase学習へ進む。判定器を研究用に使うことは本プロジェクトのChat学習開始ではない。

Base未完成、完成時に通知して停止。Chat/Dialogue/SFT/量子化なし。Python3.12.7はWSL uv/local commitのみ、pushなし。旧失敗・数値7・Phase0–3を保持。以下は過去の履歴。
Base専用・未確認source64件の抽出完了（2026-10-07 JST）。

固定4files/各16、distinct URL family64の原親と原文連続記事bodyを取得。actual665631/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start18466229はjob completeかつ実ps不在。原親およびbodyと全range SHAはnative /home/aihub_ubuntu/jmicro-data/phase6/base-hq-acceptance-20261007/ 保存。145候補中、旧URL12/旧本文exact27/new holdout19/文末構造22/日本語不足1を除外、結果後の再抽選なし。46463 native body tokens/171664 original span bytes、取得14544548bytes/28requests/46.318秒<60、CPU0.624秒<30。語句/句読点の補作なし・全連続byte範囲一致。原親と抽出bodyはまだ内容未判定0/64、新training prepared0/科学教師0/GPU0。既存near-family/suite除外は次の供給準備で未達のまま。元UI actual663394/start18278075/HTTP元10B SHA・10000007168tokens/busy=falseを確認、GPU科学jobなし。

次はこの同64の原親と保持bodyを全件個別に読み、事前契約54/64以上の文法・一貫性・記事body完結/非dominant案内の採否をbyte-bound notesへ保存。適性合格時だけ、大きな新教材の供給/protected-family除外を有限予算で測って対照付きBase学習を凍結する。抽出した量を新規学習量やBase完成としない。失敗時の再抽選/selector再調整なし。Base未完成、完成時通知停止。Chat/Dialogue/SFT/量子化なし、WSL uv/local commitのみ/pushなし。以下は過去の履歴。
Base専用・HQ原文64件の内容確認と本文抽出calibration完了（2026-10-07 JST）。

[全64個別原文理由](../reports/phase6/base_hq_source_content_review.json): 非blind Codex判定で文法2=58/一貫性2=53、自然な本文終わり25、文法・一貫性・非dominant UIと終わりが揃う22。途中切れ7件、予約定型4件、空見出し・サイト運用・引用通知・他記事リスト等を個別分類。参考文献/署名/箇条書き/問い/意図的な反復を自動的に文法不良やEOS誤りとはしない。sourceの医療/法律/宗教/政治等の内容は文法判定で事実保証しない。先頭fileのeligible sampleなのでglobal品質率でも学習成果でもない。このHQ content screenに事前の採用閾値はなく記述的結果として保存、未処理全文を自動採用しない。

[一つの原文記事body抽出](../reports/phase6/base_hq_article_calibration.json)を実CPU0.023963秒/30でcalibration。同64から自然な文末までの連続した原文byte span35/35families、32494tokensを得た。記事内のheadingは保持し、認識した末尾案内等だけを落とす。本文/句読点の補作なし、長すぎる全文は切らず拒否、文を分割してEOS用の断片にしない。CPU3tests/0.03秒でCRLF含む原byte範囲一致、末尾未完文拒否、過長全文拒否と操作案内/疑問の終わりの区別を確認。calibrationで判定を調整するsweepはせずselector SHAを固定。これは未確認の構造candidateで新学習prepared0/教師0/GPU0。

[次の未確認source acceptance契約](../configs/phase6/base_hq_acceptance.json)を本文取得前に凍結。seed2026100731でpinned Japanese564未使用filesから000_00037/000_00289/000_00301/000_00440の4file、各一様random groupから16件の固定shuffle先頭eligible、計64。原親と抽出bodyの旧exact/URL索引、calibration全ID/URL/body、local重複と新URL holdoutを除外。全64の原親と保持bodyを個別に確認し、文法・一貫性2と原記事の完結/非dominant案内が54/64以上という元source pilotの弱<=10相当を新contentを見る前に固定。失敗時は同selector/source再抽選や閾値変更で救済しない。取得60秒/100MiB、CPU30秒、embedding要求なし・旧corpus scanなし・protected test本文を読まない。永続jobはnative /home/aihub_ubuntu/jmicro-data/phase6/base-hq-acceptance-20261007/job.json、終端結果はreports/phase6/base_hq_acceptance_sample.json。完了したone-shotを再起動しない。

次は実未確認64の全raw-bound内容採否。合格した場合だけ、旧protected-family/固定suite除外と新教材の固有供給量を有限予算で測り、新しい対照付きBase教材品質比較の量・教師・GPU予算を先に固定する。旧小news/CE/DPOのepoch/係数/LR/CP/source救済として続けない。元全Base品質基準、合格時の独立学習seed/full dev/protected test/adoptionは維持。

Base未完成、完成時通知して停止。Chat/Dialogue/SFT/量子化なし、WSL uv Python3.12.7/local commitのみ/pushなし、旧失敗・旧数値7・Phase0–3保持。以下は過去の履歴。
Base専用・高品質日本語sourceの取得検証完了（2026-10-07 JST）。

[取得・固定64件](../reports/phase6/base_hq_source_sample.json)、[footer検証](../reports/phase6/base_hq_footer_inspection.json)、[公開source pin](../reports/phase6/base_hq_source_feasibility.json)。epfml/FineWeb2-HQ Japaneseをrevision c0c06e94fd3a44ae9e802b2b0fc533817601eb5eへ固定、公開非gated・565 Parquetを確認。実206 exact Rangeを用いる選択列readerを実装し、ignored Rangeをbody読み取り前に拒否、byte上限とseek/cache、実Parquet embedding大列を取得しないCPU3tests/0.45秒に合格。約1GBの先頭fileはfooter412484bytes/5.506秒だけで83816行・84 groupsを確認。固定seed2026100723のgroups26/40/48/59からtext/id/url/quality_scoreのみを取得し、既存SQLite exact/URL索引で全旧登録を照会（旧本文・protected test本文は読まない）。131候補中、exact37/URL14/new URL family holdout16を除外し固定64件、reroll/品質・長さ・score選別なし。実4000行decode、取得13793569bytes/18requests/30.978秒（100MiB/60秒以内）、CPU0.456秒/30、embedding列要求なし。元UI actual663394・HTTP元10B SHA410f975d…/10000007168tokens/busy=falseを確認。

抽出64件の本文は67194 native tokens/238511bytes、89〜10681tokens。これは内容未確認のinspectionで、新学習prepared0/科学教師0/GPU0。先頭fileの概算87.999Mはeligible64の平均×file行数だけで、global/独立固有/品質採用済み供給量にしない。HQは既存Eduと同じFineWeb2祖先、実際の旧一致51件も保持。未検出のnear-family/評価suite重複は未保証。論文の1Bモデル結果を日本語10Mの改善・高速化保証にしない。全64原文・取得range SHAはnative /home/aihub_ubuntu/jmicro-data/phase6/base-hq-sample-20261007/ に保存、可搬版はpin/plan/row SHA・ID indexと測定値のみ。研究用source適性をまだ採用しない。

次の具体的アクション: 同64原文を全件個別に読み、文法/文脈一貫性/自然な文・段落・文書の終了とboilerplate/反復をbyte-bound notesへ記録する。元本文の書換え・都合のよい再抽出なし。適性がある場合だけ、既存protected-familyと固定suite除外・新教材の供給見積りを有限予算で定義し、次の新しい多様性/品質に関する対照付きBase学習の条件・教師/GPU予算を先に凍結する。旧CE/DPO/newsのsource/係数/epoch/LR/CP救済として続けない。検証だけでBase完成とはせず、元relative/absolute/historical BPB条件、合格時の独立学習seed/full dev/protected test/adoptionを維持する。

Base未完成、完成時に通知して停止。Chat/Dialogue/SFT/量子化には進まない。既存失敗・旧数値7・Phase0–3を保持、WSL uv Python3.12.7/local commitのみ/pushなし。以下は過去の履歴。
Base同source一般化diagnostic: complete（2026-10-07 JST）。

実4CP・TRAIN56/DEV64の同mask共通bytes/全64個別DEV生成をGPU61.120621秒/120で完了、actual663168不在・元UI復帰。共通→CE→DPO: TRAIN completion CE2.957661→0.006942→0.007069、DEV body BPB1.161984→1.485290→1.484922、DEV一貫性0→2→1/16、事前flag={'chosen_CE_terminal': {'memorization_signal': True, 'domain_specialization_signal': False}, 'chosen_CE_DPO_terminal': {'memorization_signal': True, 'domain_specialization_signal': False}}。全4weights/parentSHA/RNG不変・eval・gradなし、学習更新/科学教師0、TEST0。小sample/非blind/oldWeboverlap未保証/旧数値7を保持、単独原因や10M容量不足の証明にしない。このreadonly診断を終了。旧固定CE/DPOrecipe不採用と全基準を維持し、実TRAIN/DEV転移証拠から新しい機構の比較を定義する。source/coefficient/epoch/LR/CP救済なし。

Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。元全品質基準/失敗/Phase0–3保持、WSL uv/local commitのみ/pushなし。以下は過去の履歴。

Base同source一般化diagnostic: launch（2026-10-07 JST）。

実diagnostic actual663168/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start18271519稼働、stageoriginal_d18-DEV16-greedy/GPU11.653秒。各尤度batchと生成caseを永続保存、上限120秒、更新0。元UIはfinally復帰。重複起動なし・終端oneshotは同一再試行せず保存。次は全64個別内容・readonly/原SHA/flagを確認して診断終了。

Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。元全品質基準/失敗/Phase0–3保持、WSL uv/local commitのみ/pushなし。以下は過去の履歴。

Base同source一般化diagnostic: prepared（2026-10-07 JST）。

既存archiveからDEV374のみ本文をdecode、TRAIN6617/TEST376はheaderだけ。元同paragraph/token長/localDEV同文重複除去でeligible278→固定seed20261007の64、選別結果でrerollなし。CPU0.865123秒/30、TRAIN56対DEV64/先頭16各4モデルの同CE-mask/本文byte BPB/greedy64。local article-family overlap0、DEV同文overlap curated56=0/旧news5050=2、oldWebglobal overlap未保証。CPU3tests/1.39秒でDEV固定draw・TRAIN/TEST不正byte未decode、quarter prefix UTF8境界だけ進行、単一shift/promptPAD除外・EOS CEとbody BPB分母を確認。四つの固定原親/共通6M/CE/DPO終端・設定/source/checkpointを凍結、GPU上限120秒/追加学習0。次は永続readonly→全64個別内容→小教材記憶と同source転移の事前定義flag、診断だけでBase完成としない。

Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。元全品質基準/失敗/Phase0–3保持、WSL uv/local commitのみ/pushなし。以下は過去の履歴。

次の具体的アクション（2026-10-07 JST）：固定CE対DPOの両条件は不採用。reports/phase6/base_preference_generalization_diagnostic_plan.json に、同TRAIN56と既存記事family DEV64の同本文byte尤度・先頭16各4CPの全64生成を比較する読み取り専用診断案を保存。実原親/共通6M/両終端のみ、学習更新0・CPU準備30秒/GPU120秒。小教材への記憶と同source内の一般化/領域偏りを切り分け、全個別内容・readonly状態を記録したらこの診断を終了する。新データ/設定/source未凍結・GPU未開始、TESTを使わず、旧基準/失敗/数値7を維持、係数/epoch/source/CP救済なし。Base未完成、完成時通知して停止。Chat/Dialogue/SFT/量子化なし。

Base専用CE対CE+DPO: 実比較・全160評価完了（2026-10-07 JST）。

共通Web6M一度＋同positive2M/armのCE対CE+DPO(beta.1/係数0対.1)と全160個別raw-bound内容を完了。CE→DPOでBPB1.222117852→1.223634669、文法29→30/関連15→16/一貫性4→6/適切8→12/EOS57→57/反復3→3（各80）。同CEinput/auxiliary全history一致、native10M・Adam/scheduler継承/cursor/quota/固定参照を確認。実新positive10M/各arm8M、総新GPU303.635796/1800、actual661405完了/不在/元UI復帰。最終Base検証eligible={'chosen_CE': False, 'chosen_CE_DPO': False}。固定56/4565positions約438反復は教材増量ではない。小TRAIN/長さ・作風/固定旧negative/非blind繰り返しdev/旧数値7の限界を保持。合格recipeのみ独立学習seed/full dev/protected test/adoptionへ。未合格はこの固定両recipe終了、source/beta/coefficient/epoch/LR/decoder/CP救済sweepなし。

Base未完成・完成時通知して停止。Chat/Dialogue/SFT/量子化なし。元全品質基準/全失敗/Phase0–3維持、WSL uv/local commitのみ/pushなし。以下は過去の履歴。

Base専用CE対CE+DPO: 実比較開始（2026-10-06 JST）。

科学actual661405/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start18181798実稼働、stagechosen_CE-training、GPU累積30.463秒。共通6M一度と両同positive2M、250更新/中断時全state原子的保存。restartは実PID不在を先に確認して scripts/run_base_preference_comparison.ps1 -Worker。元UIは終端finallyで復帰。次は同日本語/dev256/各80/bridge-retention512→全160個別内容・旧品質条件→採否。Base未完成、完成時通知停止。Chat/Dialogue/SFT/量子化なし、WSL uv/local commitのみ/pushなし。

以下は過去の履歴。

Base専用CE対CE+DPO: GPU継承・再開合格、本比較準備完了（2026-10-06 JST）。

ownCUDA actual660704完了/不在、GPU36.104523秒/180、native W/Adam/scheduler/全RNG/Webcursor/tied10M初期保存と共通Web・両損失4対2+2全state/history一致。152検証更新/1694058教師は科学と別、検証重み破棄。8対56の実速度から重複なし56を選択、両条件CEinput/auxiliary順序一致、全reference readonly。科学予測759.400083秒/probe込み795.504606/1800。実共通6Mを一度→同chosen2MをCE0対CE+DPO.1(beta.1)の一要因、参照は実共通6M endpointから新計算。専用runner/同全日本語dev256・各80/bridge-retention512/採否/個別raw-bound notesを実装し凍結、CPU3tests/2.84秒で累積費用、native common cursor/Adam会計改変拒否、両末尾quota/negative会計と同順序を確認。新科学10M・各arm8M予定、固定56/4565positionsの約438反復は教材増量ではない。新科学0の準備証拠・旧69.957秒diagnostic別記。次は永続実比較→全160内容→元相対/絶対/歴史BPB1%で採否。合格のみ独立学習seed/full dev/protected test/adoptionへ。未合格はこの固定両recipe終了、source/beta/coefficient/epoch/LR/decoder/CP救済sweepなし。

Base未完成・完成時通知して停止。Chat/Dialogue/SFT/量子化なし。既存全失敗/旧数値7/Phase0–3/品質基準を維持。WSL uv/local commitのみ/pushなし。以下は過去の履歴。

Base専用・原文CE対CE+DPOの継承trainerとown GPU probe実装（2026-10-06 JST）。

原d18/native10M/Adam2group/scheduler/RNG/LR1e-5/Webcursorを継ぐ共通Web6Mと、固定56の同chosen教師2Mをquotaで学習する両条件を実装。prompt/BOS/PADを除くCEと原全chosen/rejectedの参照比DPOを分け、最後の部分CE例も完全なDPO系列を採点するが別会計・EOS補作なし。負例も対照で同じ形状で評価し、係数0対.1だけが目的差。完了更新の全state/cursor/digest/CE・aux/padding・bytes/Adam/RNGを保存/再開する。新CPU3tests/2.28秒で継承と共通quota、両係数の連続4対2+2全state/historyとepoch境界、部分末尾CE7/aux chosen9・negative12の会計と参照改変拒否に合格。旧coreと損失実装は不変。

ownGPU config凍結、180秒で共通Web4対2+2/32timing、paired8対56各DPO32timingを実測し、重複なし最大56組内の教師/秒でshape選択、選択shape両係数4対2+2とCE32timing。VRAM/有限値/全継承一致とread-only参照cacheを確認し、全検証重みを破棄。実測30%margin+600評価+probe全1800内のみ科学runner/採否を実装して凍結する。新科学0・Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。固定4565positionsの反復を新教材量に足さず、元原文8弱/非blind/旧数値7失敗/既存全品質基準を保持。source/coef/beta/epoch/LR/decoder/CP救済sweepなし。WSL uv/local commitのみ/pushなし。

以下は過去の履歴。

Base専用・文章全体の比較損失の実診断完了（2026-10-06 JST）。

元d18/native10Mの固定TRAIN64を実GPU69.957002秒/180で生成・score・gradient診断、actual659437完了/不在、元UI復帰。全64EOS0/重度4gram位置8以上64/UTF8良64、正解残文CE2.955113、初期DPOloss ln2。全64勾配DPO/CE norm8.693232/cosine0.558403、重み/parentSHA/RNG不変・終了gradなしの5checksに合格、optimizer更新/科学教師0。全64原文と生成を個別nonblind比較し56に原文の文法/一貫性優位を確認、元source受入時から弱だった8は勝者とせず保持。固定56のpositive completion+EOSは4565positionsのみ。次案は同d18継承状態・LR1e-5から共通Web6M一度→chosenCE対chosenCE+DPO(beta.1/係数0対.1)各positive2M、共通を含め各8M/新実学習10M、negative/prompt/physical/反復を別会計。新loss一要因、原分岐のsource/epoch/LR/decoder/CP救済なし。まだ科学未実装/未凍結/未開始。次は56新reference cache/専用trainer/CPU会計とresume→ownCUDA各4対2+2/32timing→実測30%margin+600評価+probe全1800内のみ科学凍結。全日本語/両80/bridge-retentionと元全品質条件で採否、合格のみ独立学習seed/full dev/protected testへ。小TRAIN集合/元原文8弱/非blind/旧数値7失敗/長さ・作風差を保持しDPOや学習増量の成功を保証しない。

Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。WSL uv/local commitのみ/pushなし。以下は過去の履歴。

Base専用・文章全体の比較損失の診断（2026-10-06 JST）。

前turnのnews full100M/全80はa2d7809で不採用を保存。今回既存root診断・構成/packing/sequence objectiveの証拠を参照し、同DPO型の原文続き対自身の実生成という新しい損失機構をTRAINだけで診断する。学習後のnews枝を親にせず元d18/native10Mを固定、旧source/epoch/LR/decoder/CP救済なし。元受入ニュースの固定TRAIN64全部、body first quarter/min8・UTF8境界のみ進めた原tokenprefix、原全残文+EOS対greedy64。元sourceには8弱例がありchosenが自動的に勝者とはしない。prompt/BOS/PADを教師から除きcompletion+EOSを一shiftだけscore、固定reference比のsequence-sum DPO(beta.1)とchosen-CEの勾配を比べる。CPU2tests/1.36秒でmask/shift/EOS勾配・参照比/初期ln2/勾配方向に合格、PS構文成功。未実行prelaunchのgeometry fieldをmarginからloss方向微分へ正しく改名し元config/sourceを保存、損失/条件変更0。科学教師/optimizer更新0、Chat/SFTではなく役割なしBase文章のreadonly診断。

actual659437/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start18066087実稼働、Windowsworker27376、GPU上限180秒。再起動前は必ずPIDを確認しone-shot完了/失敗を再実行しない。終端で元UIへ復帰。次は全64実生成・reference scores・CE/DPO勾配と重み/RNG不変を確認、全64原文比較の個別内容を読む。その証拠を満たす場合のみ別予算・新save/resume・一要因CE対CE+DPOを設計する。参考: https://arxiv.org/abs/2305.18290 および https://huggingface.co/docs/trl/dpo_trainer 。長さ差/genre/非blind/単一seed/旧数値7失敗を保持、BPB guardやKL保持の保証なし。Base未完成・完了時通知停止、Chat/量子化なし、WSL uv/local commitのみ/pushなし。

以下は過去の履歴。

Base専用ニュース比較: completion（2026-10-06 JST）。

ニュース条件と全80個別raw-bound採点を完了。旧staged対照→newsでBPB1.133612866→1.021511075、文法65→45/関連39→46/一貫性23→17/適切26→18/EOS76→49/反復2→24（各80）。相対gate=False/絶対全gate=False/歴史Web全gate=False/最終Base検証eligible=False。科学新26428122/再利用73571878教師、総新GPU144.871550/1800。実native10M・継承Adam/scheduler・同Web継続と全会計を確認、元UI復帰。source/EOS/多様性・input/update数が変わる比較、523883本文tokensの約47.265反復を新規教材量としない。一学習seed/非blind反復dev・独立人手なし。合格recipeのみ独立学習seed/full dev/protected test/採用へ。未合格なら固定news分岐を終了しsource/epoch/LR/decoder/CP救済sweepなし。

Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。元相対・絶対・歴史Web1%品質基準/全旧失敗/数値7/Phase0–3維持。WSL uv/local commitのみ/pushなし。以下は過去の履歴。

Base専用ニュース比較: launch（2026-10-06 JST）。

科学actual658203/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start18010439の実稼働、stageauthored_news-dev256/観測新教師25976793/26428122を確認。科学GPU上限1770.245130秒。共通Web73571878教師は再GPUしない。250更新ごと全state原子的CP、中断時は実PID不在を確認して scripts/run_livedoor_base.ps1 -Worker で再開。元UIは終端finallyで復帰。学習終端/全日本語/80内容/採否は未完了。

Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。元相対・絶対・歴史Web1%品質基準/全旧失敗/数値7/Phase0–3維持。WSL uv/local commitのみ/pushなし。以下は過去の履歴。

Base専用・ニュース比較の本学習準備完了（2026-10-06 JST）。

原native10,001,152/tied・継承Adam/scheduler/LR1e-5/共通prefixの条件を維持する科学runner・評価・全80内容/採否経路を実装。CPU3tests/2.51秒で失敗probeを含む累積予算、再利用prefixからの同Web継続、実CPU終端の教師/bytes/Adam/scheduler/cursor会計と改変拒否に合格。PS構文成功。config凍結、予測は検証・旧失敗込み479.012075秒/1800。本学習は残Web1,428,122→news25M、共通Web73,571,878と旧対照は再GPUせず別記。prepared news本文523,883tokens、約47.265反復を新教材量と混同しない。次は一条件の永続実学習→同dev256/日本語/全80個別採点/bridge・retention→元品質条件の判定。Base未完成・完了時通知停止、Chat/量子化なし。全旧失敗と基準維持、source/epoch/LR/decoder/CP救済sweepなし、WSL uv/local commitのみ/pushなし。

以下は過去の履歴。

Base専用news CUDA probe: passed（2026-10-06 JST）。

actual657464実完了/不在、GPU28.335452秒/120。実native W/Adam/scheduler/CUDA含む全RNG/Webcursor/tied10M初期一致、本goals Webと明示Web=1 news境界stressの両4連続対2+2全state/history/LR/有限値一致・各32timingに合格。80検証更新/2603282教師は科学と別、stress重み破棄。科学予測449.257206秒・ownprobe/旧失敗込み479.012075/1800。次は費用内のみ残26428122教師の専用科学runner/同全日本語・dev256・全80reviewを実装して凍結、共通73571878教師/旧対照を再GPUしない。これは再開/実装/費用の証明でモデル品質/完成ではない。

Base未完成・完成時通知停止、Chat/量子化なし。元品質条件/全旧失敗保持、source/LR/epoch/decoder/CP救済sweepなし。WSL uv/local commitのみ/pushなし。以下は過去の履歴。

Base専用news GPU照合の限定修復（2026-10-06 JST）。

初回actual656937はnative GPU tensorと保存CPU tensorのtorch.equal直接比較で初期照合時に失敗。GPU1.419417秒、forward/optimizer0、原config/source/job/失敗archiveを保存し元UI復帰。新v2は同じtensor値/dtypeをCPUへ揃える再帰device正規化だけ、学習recipe/幅/LR/source/epochs不変。新CPU3tests/2.76秒で全state境界再開/quotaとnested state正規化の値・型保持に合格。実親CPU準備1.320159秒。旧失敗も総1800秒へ算入、ownCUDA120秒・本Web/news stressの両4対2+2/各32timingの厳密基準は維持。次はこの同条件probe。Base未完成・完成時通知停止、Chat/量子化なし。WSL uv/local commitのみ/pushなし。

Base専用news CUDA probe: failure_v1（2026-10-06 JST）。

own news probe actual656937実終端/不在、GPU1.419417秒、理由RuntimeError('Expected all tensors to be on the same device, but got other is on cpu, different from other tensors on cuda:0 (when checking argument in method wrapper_CUDA__equal)')。原config/source/job/失敗を保存し元UI復帰。

Base未完成・完成時通知停止、Chat/量子化なし。元品質条件/全旧失敗保持、source/LR/epoch/decoder/CP救済sweepなし。WSL uv/local commitのみ/pushなし。以下は過去の履歴。

Base専用日本語news trainer/own probe実装（2026-10-06 JST）。

原native10M/継承Adam・scheduler・LR1e-5と共通prefix322685のWebcursor/RNGを保持し、残Web1428122→news25Mを正確な教師quotaで学習する専用処理を実装。親prefix73571878教師は再GPUせず別会計、BOS mask/partial末尾教師/全masked余剰physical Web/bytes/EOSを保存。news contiguous1024 shuffled blocksの最終478tokensは未サンプルと明記、全5050の全語学習を断定しない。CPU2tests/1.55秒でnative W/Adam/scheduler/RNG継承とWeb→news境界の4連続対2+2全state/history、正確quota/bytes/EOS/末尾physicalを確認。初回tiny旧fixtureに本番Webmanifest fieldがなく1failを保存、本番CPにあることを確認しfixtureへ実CPU source metadataだけを補完した。

実親CPU構築でW/Adam/scheduler/host RNGを確認しprobe config凍結、CPU1.238661秒。初回はCPUでCUDA RNGまで比較して拒否し、元script/失敗metadataを保存。hostはCPUで、CUDA含む全RNGはこれからのown GPUで従来の厳密一致を要求し基準を緩和しない。GPU120秒で実full-goals Webと明示web=1のnews-boundary stressそれぞれ4連続対2+2/32timingを測る。80検証更新は全scientific教師と別、stress重み破棄、2source実速度・save・warmupの1.3margin+300評価+probe全1800予測内のみ科学runnerを実装/凍結。今のnew GPU/科学0、Base未完成・完成時通知停止、Chat/量子化なし。全旧失敗・元品質基準維持、source/LR/epoch/decoder/CP救済sweepなし。WSL uv/local commitのみ/pushなし。

Base専用・日本語ニュースsource準備完了（2026-10-06 JST）。

前turn出力変換100M/全80は2dfea0aで不採用。今回同3068/100M全paired TRAIN historyをCPU.098275秒で分析し、末尾32のCEは4sourceともnativeより高い。事後/fresh readout Adam差/混在境界別会計で、原因や容量不足の証明にしない。新[配布者livedoorニュースコーパス](https://www.rondhuit.com/download.html#ldcc)をdownload2.484144秒・CPU1.349822秒で準備。元7367記事→TRAIN5050原first paragraphs/本文523883・BOS/EOS込533983tokens、EOS/教師.009548。article-ID family90/5/5のdev374/test376本文をdecode/tokenizeせず、local exact127重複を除外。旧Webcross重複/独立audit未完、新規distinctを断定しない。固定64全個別nonblind採点・弱8<=10でsource受入。医学宣伝/こちら参照/語欠落などの弱い例を記録し、後から除去/rerollせず原5050を保持。これはsource readinessで全5050監査・モデル品質・独立人手の証明ではない。原archive/LICENSE/全文章/64raw/binaryはnative保存、portableはhash/provenance/notes/codeのみ。CPU0.399831秒で旧native stagedの最大Web-only保存CP322685を品質参照なしに選び、実weights/Adam2group・LR1e-5/RNG/Webcursor/親d18/全会計と10M tiedを確認。共通Web73571878教師を再GPUせず、残Web1428122+news25M=26428122新教師・全100Mにする一案。news25Mは約47.265反復で、本文523883を教材量として別記。source/EOS/多様性・物理input/update数が変わる比較で、量のみ/同targetとは称さない。native core/Tokenizer/decoder/旧cached対照を変更しない。次は専用2source trainer/会計/実保存再開を実装、ownCUDA120秒/32timing後、1.3margin+300評価+probe全1800秒予測内のみ科学凍結。newGPU/科学0、元UI確認、Base未完成・完成時通知停止、Chat/量子化なし。

元相対・絶対・歴史Web1%品質基準/全旧失敗/数値7/Phase0–3維持。source/selector/epoch/LR/decoder/CP救済sweepなし。WSL uv/local commitのみ/pushなし。以下は過去の履歴。

Base専用・著者による日本語ニュース段落pilot準備（2026-10-06 JST）。

前turnの出力変換100M/全80は2dfea0aで不採用、Base未完成。今回CPU0.098275秒で実3068全更新/同100M input・target・source・digestのpaired lossを分析、混在3境界lossは単一sourceへ配賦しない。末尾32更新CEは新readout対nativeでWeb2.585706/2.577496、story1.994395/1.929531、ordinary2.196530/2.149302、conditional.288487/.259440。TRAINのみ・事後・fresh Adam差あり、品質悪化の原因/他の容量不足の証明にしない。関連CPU1test/1.28秒。

次は[配布者のlivedoorニュースコーパス](https://www.rondhuit.com/download.html#ldcc)の新source pilot。2012年収集の日本語記事、URL/date/titleを除く原first paragraphだけ、補作文/後段fallbackなし、24..256tokens、article-ID family90/5/5でheldout本文を読まない。元archive/category LICENSEをnative保存、公開なし。download60秒/20MB、CPU120秒、Tokenizer不変・新GPU0。固定seed2026100652/64TRAIN内容弱<=10を学習前に判定、未達なら分岐終了しselector/reroll救済なし。CPU1test/.73秒で後段置換・補完・引用途中・見出し拒否/familyを確認してconfig凍結。量は実測まで未確定、epoch反復をdistinct教材量に足さず、旧Webとの重複/独立全audit未完を保持。受入後のみ同d18 native親/継承Adam・LR1e-5/Web75M+news25Mの100M対cached旧full100Mを実GPU再開/速度/全費用1800秒予測後に科学凍結する案。source/EOS/多様性の変更で量のみの効果と称さない。元品質基準・全旧失敗維持。Base完成時通知停止、Chat/量子化なし、WSL uv/local commitのみ/pushなし。

Base専用gated出力変換: completion（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

同親/同full100Mの出力変換対cached native比較と全80個別raw-bound採点を完了。BPB1.035666704→1.032951419、文法65→46/関連52→39/一貫性32→7/適切37→9/EOS69→46/反復6→24（各80）。事前strong-staged相対gate=False、絶対全gate=False、歴史Web全gate=False、最終Base検証eligible=False。科学100M/3068updates/100532224input、総新GPU178.915812/900、actual654827実不在/元UI復帰。nonblind Codex/一学習seed/反復devを独立人手や確実な一般化の証明としない。合格recipeのみ独立学習seed/full dev/protected test/採用へ。未合格の場合は固定readout分岐を終了し、同幅/LR/source/decoder等の救済sweepは行わない。stock HF adapter未対応を完成としない。

全旧失敗/数値7/Phase0–3/既存相対・絶対・歴史Web1%品質基準保持。幅/activation/placement/LR/初期値/source/CP/decoder救済sweepなし。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用gated出力変換: launch（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

科学actual654827/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start17811675の実稼働、stagereadout-adapter-Base-training/観測教師4577776/100Mを確認。科学GPU上限876.205509秒。250更新ごと全state原子的CP、中断時は実PID不在を確認して scripts/run_readout_adapter_comparison.ps1 -Worker で再開。元UIは終端finallyで復帰。学習終端/全日本語/80内容/採否は未完了。

全旧失敗/数値7/Phase0–3/既存相対・絶対・歴史Web1%品質基準保持。幅/activation/placement/LR/初期値/source/CP/decoder救済sweepなし。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用gated出力変換: preparation（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

own実CUDA/全state再開/32timingのGPU23.794491秒を再利用し、専用科学runner・同native評価factory・全80採点/採否経路を実装して凍結。同mixed親6d/元119重み全凍結/新98,304の2tensorだけfresh Adam・LR.0001/WD0、同full CE100Mのcached native対照は再GPUしない。新CPU2tests（source/費用と明示評価factory復旧）・PS構文成功、旧core/source不変。科学GPU予測798.859647秒、ownprobe込み822.654138/900、科学未開始。次は一候補100M実学習→同日本語・dev256・native80/内容→旧相対・絶対・歴史Web基準の採否。

全旧失敗/数値7/Phase0–3/既存相対・絶対・歴史Web1%品質基準保持。幅/activation/placement/LR/初期値/source/CP/decoder救済sweepなし。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用frozen nonlinear readout: probe（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

actual653986実完了/不在、ownCUDA probe23.461776秒/120。初期FP32/BF16 native32/1024・nonzero full/cache1024とnative119重み凍結/RNG/13KV、fresh readout-only Adam/fixedLR.0001・連続4対2+2全state/history/finiteと32timingに合格。40検証更新/1307952教師/11readonly forward6272contextは科学へ混ぜない。ピークVRAM2.117GiB、科学予測798.859647秒・ownprobe/旧失敗込み822.654138/900。旧probeはCPU準備moduleのimport副作用でCUDAを隠したため失敗。元source/config/失敗を保存しproposal定数path参照だけへ限定修復、GPU可視性import回帰testを追加し科学recipe不変。これは実装/再開/費用の証明で、日本語品質やBase完成の証明ではない。次は予算内のみ専用科学runner/明示readout評価/全80reviewを実装し、cached native full100M対照を再GPUせず固定条件で比較する。

[Houlsby adapter](https://proceedings.mlr.press/v97/houlsby19a.html)と[feature distortion/linear probing](https://arxiv.org/abs/2202.10054)を参考にした独自の転移仮説。per-layer BERT分類adapter/主にvisionの報告を日本語10Mでの改善保証としない。全旧失敗/数値7/Phase0–3/元相対・絶対・歴史Web1%基準保持。幅/activation/placement/init/LR/source/mask/parent/decoder/CP救済sweepなし、native HF export未対応を完成としない。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用readout probe実データschema修復（2026-10-06 JST）。

v2 actual653385は固定memoryのキーinputs誤読でKeyError、GPU0.232884027秒・学習0、元source/config/job/ログを保存し元UI復帰。実packetのx/y int64[32,1024]へ合わせ、GPU前に同実packetを読む事前検証を追加。GPU可視性と実packet schema/不正形式拒否のCPU2tests/2.89秒合格。v3は同科学recipe、旧二失敗0.332715188秒を900秒総上限へ算入。次は同own CUDA identity/cache/fullstate再開/32timingへ。Base未完成・完成時通知停止、Chat/量子化なし。

Base専用frozen nonlinear readout: probe_failure_v2（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

出力変換probe actual653385実終端/不在、GPU0.232884秒、理由KeyError('inputs')。原source/partial/失敗を保持し、基準や幅等を変えて救済せず実原因に対する限定修復または別機構を定義する。

[Houlsby adapter](https://proceedings.mlr.press/v97/houlsby19a.html)と[feature distortion/linear probing](https://arxiv.org/abs/2202.10054)を参考にした独自の転移仮説。per-layer BERT分類adapter/主にvisionの報告を日本語10Mでの改善保証としない。全旧失敗/数値7/Phase0–3/元相対・絶対・歴史Web1%基準保持。幅/activation/placement/init/LR/source/mask/parent/decoder/CP救済sweepなし、native HF export未対応を完成としない。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用readout probe限定修復（2026-10-06 JST）。

初回actual652808は準備用module importによるCUDA_VISIBLE_DEVICES=''の副作用でGPU初期化失敗、0.099831161 GPU秒、学習0。元source/config/job/失敗archiveと元UI復帰を保存。GPU自体はRTX4090/driver616.92・uv torch CUDA available=Trueを確認。probeの準備module importを固定proposal path参照に置換するだけの修復、新config/run v2で旧証拠を上書きしない。GPU可視性をNone/0の両方で保持するsubprocess回帰test1件/2.07秒合格。新条件/source/LR/init/decoderの変更なし、旧失敗時間も900秒上限に算入。次は同120秒own CUDA probe、合格・費用内のみfull100M比較へ。Base未完成・完成時通知停止、Chat/量子化なし。

Base専用frozen nonlinear readout: probe_failure（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

出力変換probe actual652808実終端/不在、GPU0.099831秒、理由RuntimeError('No CUDA GPUs are available')。原source/partial/失敗を保持し、基準や幅等を変えて救済せず実原因に対する限定修復または別機構を定義する。

[Houlsby adapter](https://proceedings.mlr.press/v97/houlsby19a.html)と[feature distortion/linear probing](https://arxiv.org/abs/2202.10054)を参考にした独自の転移仮説。per-layer BERT分類adapter/主にvisionの報告を日本語10Mでの改善保証としない。全旧失敗/数値7/Phase0–3/元相対・絶対・歴史Web1%基準保持。幅/activation/placement/init/LR/source/mask/parent/decoder/CP救済sweepなし、native HF export未対応を完成としない。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用frozen nonlinear readout: preparation（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

前の層共有100Mは全gate未達・不採用のまま。元d18 greedy80の固定64token pathをCPU0.059142秒で再利用し、終了判定だけの非EOS順序不変/CE二値勾配一致をCPU2tests/0.90秒で確認。人手の第一可用prefix62件・文法54/一貫性36、文法56のfeasibility marker未達。nonblind・事後・非全停止位置の診断で、全EOS法やモデル容量の不可能性を主張しない。次は同mixed親6dに一つのpostnorm256→192→256/biasなしSiLU/zero-up readoutを追加。元119/10,001,152重みは全凍結、新2tensor/98,304のみfresh Adam・LR.0001/WD0、合計10,099,456。native tied/13KVを保ち、本文の語選択とEOSを変えられるがWeb保持は保証しない。旧rank4全層linear融合とは異なる非線形final readoutを一条件として定義。CPU3tests/2.06秒で初期native出力/重みobject/独立RNG/新梯度のみ、nonzero ragged/cache/未来非参照/labels/native saveとfresh2Adam4対2+2全state/historyに合格。CPU proposal0.277456秒・probe準備0.109018秒、新GPU/科学0。次はown native FP32/BF16 identity32/1024・nonzero cache1024・CUDA全state再開/32timingを120秒内で測る。1.3margin+300秒評価+ownprobeが900内の場合だけ専用科学runner/全80採否を実装・凍結し同full100Mへ。

[Houlsby adapter](https://proceedings.mlr.press/v97/houlsby19a.html)と[feature distortion/linear probing](https://arxiv.org/abs/2202.10054)を参考にした独自の転移仮説。per-layer BERT分類adapter/主にvisionの報告を日本語10Mでの改善保証としない。全旧失敗/数値7/Phase0–3/元相対・絶対・歴史Web1%基準保持。幅/activation/placement/init/LR/source/mask/parent/decoder/CP救済sweepなし、native HF export未対応を完成としない。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用gated層共有: completion（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

同親/同full100Mの層共有対cached native比較と全80個別raw-bound採点を完了。BPB1.035666704→1.035926040、文法65→68/関連52→53/一貫性32→30/適切37→36/EOS69→73/反復6→7（各80）。事前strong-staged相対gate=False、絶対全gate=True、歴史Web全gate=False、最終Base検証eligible=False。科学100M/3068updates/100532224input、総新GPU438.496675/1800、actual651138実不在/元UI復帰。nonblind Codex/一学習seed/反復devを独立人手や確実な一般化の証明としない。合格recipeのみ独立学習seed/full dev/protected test/採用へ。未合格の場合は固定gate分岐を終了し、同gate/source/decoder等の救済sweepは行わない。stock HF adapter未対応を完成としない。

全旧失敗/数値7/Phase0–3/既存相対・絶対・歴史Web1%品質基準保持。gateLR/初期値/count/source/CP/decoder救済sweepなし。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用gated層共有: launch（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

科学actual651138/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start17619163の実稼働、stagegated-shared-Base-training/観測教師3269803/100Mを確認。科学GPU上限1752.741499秒。250更新ごと全state原子的CP、中断時は実PID不在を確認して scripts/run_gated_shared_comparison.ps1 -Worker で再開。元UIは終端finallyで復帰。学習終端/全日本語/80内容/採否は未完了。

全旧失敗/数値7/Phase0–3/既存相対・絶対・歴史Web1%品質基準保持。gateLR/初期値/count/source/CP/decoder救済sweepなし。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用gated層共有: preparation（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

own実CUDA/全state再開/32timingのGPU47.258501秒を再利用し、専用科学runner・同native評価factory・全80採点/採否経路を実装して凍結。同mixed親6d/継承native Adam・LR.00001/新13gateのみfresh Adam・LR.0001/WD0、同full CE100Mのcached native対照は再GPUしない。新CPU1test/0.88秒・PS構文成功。初回CPUはdict対strの不一致でAttributeErrorとなったため、その失敗XMLを保存して新照合関数の型/欠損guardを修正、旧core/source不変。科学GPU予測1007.293266秒、ownprobe込み1054.551767/1800、科学未開始。次は一候補100M実学習→同日本語・dev256・native80/内容→旧相対・絶対・歴史Web基準の採否。

全旧失敗/数値7/Phase0–3/既存相対・絶対・歴史Web1%品質基準保持。gateLR/初期値/count/source/CP/decoder救済sweepなし。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用gated層共有: probe（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

actual650199は実完了/不在、probeGPU47.258501秒/120。zero-gate native FP32/BF16の32/1024とsigned gate full/cache1024、native重み/RNG不変・logical26KVに合格。初期native W/Adam・scheduler/RNG/Webcursor継承/新gateのみfresh、own CUDA4連続対2+2全state/history・finite/固定nativeLR.00001/newgate.0001、32timing完了。40検証更新/1307952教師/11readonly forward6272contextは科学から除外。ピークVRAM9.735GiB、科学予測1007.293266秒、ownprobe込み1054.551767/1800。これは初期構造と再開/実費用の証明で、日本語品質/容量原因/完成の証明ではない。次は予算内のみ専用科学runnerと全80reviewを実装、同full100M native対照を再GPUせず比較する。

[MobileLLM](https://arxiv.org/abs/2402.14905)の即時block sharingと[ReZero](https://arxiv.org/abs/2003.04887)の0初期gateを参考にした独自の転移仮説。公開論文の正確な再現や日本語10Mでの改善を主張しない。全旧失敗/数値7/Phase0–3/旧品質基準保持、gateLR/初期値/count/source/CP/decoder救済sweepなし。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用gated層共有: preparation（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

KL/full・nonEOS/金body復習/positive anchor/Fisherの不採用を確認し、未実装の層共有を別機構として定義。同13 unique blockに追加の共有呼出を挟み、追加attention/MLP residualの同一scalarを0初期化して元関数を保つ。重み10,001,152→10,001,165（新13gate/1tensor）、logical26、tied/独立26KV/cache/causality/native save/load。CPU4tests/2.07秒でゼロ時の元logits・重みobject/梯度/RNG一致、非ゼロsigned gateのragged/chunk/未来非参照、native Adam継承/新gate group/全state4対2+2を確認。random tiny fixtureで品質の証明ではない。実CPU proposal0.286228秒、probe準備0.118820秒、新GPU/科学0。比較はsame mixed親/継承native Adam・LR.00001/source/full100M CEとcached matched_staged_CE、追加gateのみfresh Adam・LR.0001/WD0固定。計算/KVが増え、stock HF adapterは未対応で完成としない。次はown native FP32/BF16 zero-gate32/1024、signed full/cache1024とCUDA4対2+2/32timing/batch32を120秒内で測る。1.3margin+300秒評価+ownprobeが1800内の場合のみ科学runnerを実装・凍結して100M一候補へ。

[MobileLLM](https://arxiv.org/abs/2402.14905)の即時block sharingと[ReZero](https://arxiv.org/abs/2003.04887)の0初期gateを参考にした独自の転移仮説。公開論文の正確な再現や日本語10Mでの改善を主張しない。全旧失敗/数値7/Phase0–3/旧品質基準保持、gateLR/初期値/count/source/CP/decoder救済sweepなし。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用Fisher anchor: completion（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

同親/継承Adam・LR/全source full100MのFisher対cached uniform比較と新全80個別採点・36exact旧raw採点継承を完了。candidate BPB0.984992397（uniform0.990667075）、文法59→63/関連60→66/一貫性25→28/適切29→30/EOS67→65/反復6→7（各80）。絶対screen全合格だが、強いstaged23に対し一貫性28/+5<8、EOS65<76/反復7>2、歴史WebBPB上限.9812859519も超過。最終Base検証eligible=False、不採用を保持。科学100M/100532224input、検証1307952教師・field65276model-sampled label別、総新GPU280.070139秒/1800、actual648919実不在/元UI復帰。日本語意味・構文・常識の微差とnonblind内容採点は独立改善の証明ではない。固定field/lambda等分岐終了、独立seed/full dev/protected test/採用なし。次は既存結果を根拠に残るEOS/反復と保持の別機構を定義、同field等の救済sweep/対照再GPU/全量scanはしない。

全旧失敗/数値7/Phase0–3/既存相対・絶対・歴史Web1%品質基準保持。field/seed/回数/lambda/source/mask/CP/decoder救済sweepなし。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用Fisher anchor: launch（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

科学actual648919/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start17456444の実稼働を確認、stagefisher_anchor-training/観測教師26812706/100M。科学GPU上限1777.215966秒。250更新ごと全state原子的CP、実PID不在後 scripts/run_fisher_parameter_anchor.ps1 -Mode Train -Worker で再開。終端・全日本語/80内容採否は未完了、元UIは終端finallyで復帰。

全旧失敗/数値7/Phase0–3/既存相対・絶対・歴史Web1%品質基準保持。field/seed/回数/lambda/source/mask/CP/decoder救済sweepなし。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用Fisher anchor: probe（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

ownCUDA4連続対2+2の全state/history/有限値/LR/親Adam・scheduler・RNG/Webcursor・anchor/fieldに合格、32timing完了。実40検証更新/1307952教師は科学と別、ownprobe19.161004秒/120。1.3margin・200秒非学習余裕付き科学予測805.390661秒、field+probe込み828.174695/1800。次は予算内のみ同full100M一候補/同日本語・dev256・native80/旧全gate採否へ。GPUgateは品質の証明ではない。

全旧失敗/数値7/Phase0–3/既存相対・絶対・歴史Web1%品質基準保持。field/seed/回数/lambda/source/mask/CP/decoder救済sweepなし。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用Fisher anchor: preparation（2026-10-06 JST）。Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

同mixed親6d/継承Adam・RNG/scheduler・LR.00001/同full CE100M/Web75M-story5M-ordinary10M-conditional10M/lambda.04161064039180984、差分は固定mean1 Fisher fieldのみ。既存一律L2対照100M/全80/日本語/devを再利用、再GPUなし。field実3.623030秒/64MC score gradient・65276sampled labelはsource CEと別。新CPU予算1test/1.47秒・PS構文合格、CPU準備0.264034秒、本学習0。次はownCUDA4対2+2全state/history/固定field・anchor/継承状態と32timingを120秒内で測定。field+probe+本科学+評価を実測margin付き1800秒内の場合のみ科学凍結、同eval/旧全gateを保持。

全旧失敗/数値7/Phase0–3/既存相対・絶対・歴史Web1%品質基準保持。field/seed/回数/lambda/source/mask/CP/decoder救済sweepなし。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用Fisher parameter field: terminal（2026-10-06 JST）。Base未完成・完成時通知して停止、Chat/Dialogue/SFT/量子化なし。

固定conditional MC Fisher field実完了、actual647866は実不在。GPU3.623030秒/120、実64score gradient/65276model-sampled label/65536physical、source CE/optimizer0。10,001,152 unique119/weights・RNG・Param.grad不変/会計合格、field globalmean1.00000000、max41089.039062、zero0。model-sampled conditional Fisherの局所近似で有限保持/日本語品質の証明ではない。field.ptはnative保存/親・memory・source・tensor/rawSHA拘束。次はown inherited-state CUDA4対2+2/32timing/保存費用を120秒内で測り、field+probe+本科学+評価1800秒予測内のみ同parent/Adam/source/full100M CE/lambdaの一候補比較を凍結する。旧uniform全80/日本語/dev対照は再実行せず再利用。

全旧不採用/数値7/Phase0–3/相対・絶対・歴史Web1%品質基準を維持。field/seed/回数/normalization/module/lambda/CP救済sweepなし。合格recipeのみ独立学習seed/full dev/protected test/採用へ。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用Fisher parameter field: preparation（2026-10-06 JST）。Base未完成・完成時通知して停止、Chat/Dialogue/SFT/量子化なし。

一律L2の完了済み不採用対照に対し、同mixed親/継承Adam・LR.00001/同full100M CE・source・mask・lambda.04161064039180984を保ち、model-sampled conditional diagonal Fisherのglobal unique-coordinate mean1で重み別抑制を行う別案。同TRAIN32窓/2反復/seed2026100647、行sum NLLをsqrt(全body32638)で割り、行score gradient二乗を和/2するtoken-weighted推定。GT empirical Fisher/全joint Fisher/Hessian/有限NLL保持の証明ではない。関連CPU4tests/1.97秒（独立ラベルの全列挙期待値、tied/一律一致/非有限拒否、private RNG不変、native全state4対2+2と改変拒否）、準備0.280308秒。新GPU/本学習0。次はfield64 gradient/65276model-sampled label（通常source CE0）を120GPU秒内で計算、own CUDA trainer gate/timing後、field+probe+本科学+評価1800秒予測内のみ100M一候補へ。旧対照再GPU/再全量scanなし。

全旧不採用/数値7/Phase0–3/相対・絶対・歴史Web1%品質基準を維持。field/seed/回数/normalization/module/lambda/CP救済sweepなし。合格recipeのみ独立学習seed/full dev/protected test/採用へ。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

固定20境界Baseの失敗原因を既存rawからCPU分析（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。

受入2600更新/84961352CE教師＋memory gradient424294、拒否20更新/650524source梯度＋memory gradient32638別会計。全science梯度exposures86068808、ownprobe5231748教師は別。最終安全NLL2.607065320、上限2.607075455。単一gradientの線形予測2.607049643に対して実修正後2.608679235、正の非線形残差0.001629592/内側marginの63.13倍。最後0.125の実NLL2.607168734も上限を0.000093279超えるため規定通り全区切りrollback。単一修正/固定試行が不十分という局所TRAIN診断で、全学習解不存在やモデル容量/教材不足の証明ではない。条件教材の学習到達=False、全91,641,755/日本語・全80/品質評価は未達。分析CPU0.311259秒/20、新GPU/学習0。science193.647秒＋ownprobe33.679＋旧診断70.561=関連297.887秒/2400。

raw proposalへ残った旧毎更新algorithm/prerequisite文言は元provenanceのまま保持し、事前に凍結したkind/block_updates/transaction/probe/budgetおよび実trainer/CPU/CUDAをactive20境界契約と明示。品質selectionは旧と完全一致、後から基準を変えて採用していない。次は固定分岐を終了し、この非線形残差と条件段階未到達の根拠から別のBase改善機構を研究・定義。cadence/projector/backtrack/source/CP救済sweepなし。元10B UI保持・WSL uv3.12.7/local commitのみ/pushなし、全旧失敗/数値7/Phase0–3保持。以下は過去の履歴。

Base専用固定20境界constraint: terminal（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。

固定20区切りの有限受入不能で分岐終了、actual646766はcomplete・実不在。受入2600更新/84961352CE教師、拒否した全区切りは重み/Adam/scheduler/RNG/samplerを直前境界へrollbackしnativeCP保持。拒否source梯度/追加memorygradient・forwardは別会計。科学GPU193.647007秒、全3068/91,641,755や品質達成とはしない。元UI復帰、cadence/packet/bound/projector/LR等救済sweepなし。次はこの実失敗を根拠に別のBase改善を定義する。

旧毎更新予算超過は不採用のまま、cadence20は別研究として固定。元math保持packet/bound/margin/projector/LR/元staged入力・教師mask/decoderと旧相対・絶対・歴史Webの全品質基準を維持。追加Web gradient/拒否試行を別会計し総教師量matchedと称さない。Phase0–3/数値7/全旧失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用固定20境界constraint: launch（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。

science実起動actual646766/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start17296120、実stageblock-constrained-Base-training・受入1400/3068更新・教師45777941を確認。科学上限2295.760321秒＋ownprobe33.678573＋旧診断70.561106=2400。各受入境界で重み/Adam/scheduler/RNG/sampler/全会計CP保存、未確定区切りは一切保存/完了量へ加算しない。終端・全日本語/80内容・採否は未完了。restartは実PID不在確認後 scripts/run_block_Web_constraint.ps1 -Mode Train -Worker。

旧毎更新予算超過は不採用のまま、cadence20は別研究として固定。元math保持packet/bound/margin/projector/LR/元staged入力・教師mask/decoderと旧相対・絶対・歴史Webの全品質基準を維持。追加Web gradient/拒否試行を別会計し総教師量matchedと称さない。Phase0–3/数値7/全旧失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用固定20境界constraint: probe（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。

ownCUDA固定20更新×連続2区切り対1+1の全state/history/LR/有限値/境界NLLに合格、4区切り80更新timing完了。検証160更新/5231748CE教師は科学から除外、GPU33.678573秒/120。元math有限projector controlは不変source/同memoryの旧実証を再利用と明示し、新診断GPUへ足さない。最悪科学予測910.385827秒、旧3診断/ownprobe込み1014.625506秒/2400。内部tentative点がboundedとの証明ではない。予算内のみscience凍結し、同元親/Adam/actualLR.00001/同staged91,641,755CE＋追加memory gradient別会計/同日本語・全80/旧全gate採否へ。

旧毎更新予算超過は不採用のまま、cadence20は別研究として固定。元math保持packet/bound/margin/projector/LR/元staged入力・教師mask/decoderと旧相対・絶対・歴史Webの全品質基準を維持。追加Web gradient/拒否試行を別会計し総教師量matchedと称さない。Phase0–3/数値7/全旧失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用固定20境界constraint: preparation（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。

固定20更新の提案区切りごとに元FP32/math TRAIN body NLL<=original*1.01を確認し、旧と同じ有限projector/0.5・.25・.125の修正または全区切りrollbackを行う別研究。内部の未確定更新は上限を超える可能性があり、旧毎更新契約の成功へ置換しない。CPU4tests/2.16秒でnative全state連続対再開・全区切り拒否/途中中断rollback・末尾短区切り/改変拒否、CPU準備0.113392秒。217MB cache/固定32窓を再利用、全量scanなし。新GPU/本学習0。次はownCUDA連続2区切り対1+1/全state、4区切り80更新timingを120秒内で測り、旧3診断70.561106秒と新probe/最悪154区切り/全科学予測が2400秒内の場合のみ本学習へ。

旧毎更新予算超過は不採用のまま、cadence20は別研究として固定。元math保持packet/bound/margin/projector/LR/元staged入力・教師mask/decoderと旧相対・絶対・歴史Webの全品質基準を維持。追加Web gradient/拒否試行を別会計し総教師量matchedと称さない。Phase0–3/数値7/全旧失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用compiled oracle: terminal（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。

readonly compiled FP32診断が実完了、actual645132終端/実不在。GPU26.820366秒/120、optimizer/新source学習0。両固定点で元math NLL/勾配・bitwise反復/weights・RNG/grad不変合格。max forward0.050037/gradient0.242527秒。元math受入監査一回/各更新と初回compile余裕を含む科学予測3550.722645秒、旧2診断/ownprobe込み3621.283751秒/2400。これは計画で、owntransactional CUDA gateや将来全重みparity/品質/完成の証明ではない。厳密受入監査を保つ計画でも40分予算を超えるため、本科学を凍結/起動しない。compile/mode/dtype等の救済sweepなし、次はこの実費用を根拠に別のBase改善機構を定義する。

[PyTorch公式compile仕様](https://docs.pytorch.org/docs/2.14/generated/torch.compile.html)を参照し、当固定FP32計算の数値/時間は実測で判定。元10B UI復帰、全旧失敗/数値7/Phase0–3/相対・絶対・歴史Web品質基準保持、WSL uv3.12.7/local commitのみ/pushなし。合格recipeのみ独立学習seed/full dev/protected test/採用へ接続。以下は過去の履歴。

Base専用compiled oracle: preparation（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。

同FP32/micro8/固定TRAIN32/効率Attentionへtorch.compile(fullgraph=True, mode=default, dynamic=False)を一つだけ適用。元親/固定旧masked-stagedの2点で同math NLL2e-6/gradient element絶対2e-6+相対2e-5・global L2相対2e-5/bitwise反復/weights・RNG・grad不変を確認し、4forward+4gradient実timingを測る。初回compileも含む120GPU秒、CPU準備0.216440秒、新GPU/optimizer0。旧2診断43.740740GPU秒も次の2400秒予算へ計数。dtype/backend/mode/packet/CP救済なし。次は実GPU比較を起動、元math厳密受入監査込みの予測と新全stateCUDA gateなしでは本科学を起動しない。

[PyTorch公式compile仕様](https://docs.pytorch.org/docs/2.14/generated/torch.compile.html)を参照し、当固定FP32計算の数値/時間は実測で判定。元10B UI復帰、全旧失敗/数値7/Phase0–3/相対・絶対・歴史Web品質基準保持、WSL uv3.12.7/local commitのみ/pushなし。合格recipeのみ独立学習seed/full dev/protected test/採用へ接続。以下は過去の履歴。

Base専用compiled oracle: preparation（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。

同FP32/micro8/固定TRAIN32/効率Attentionへtorch.compile(fullgraph=True, mode=default, dynamic=False)を一つだけ適用。元親/固定旧masked-stagedの2点で同math NLL2e-6/gradient element絶対2e-6+相対2e-5・global L2相対2e-5/bitwise反復/weights・RNG・grad不変を確認し、4forward+4gradient実timingを測る。初回compileも含む120GPU秒、CPU準備0.331529秒、新GPU/optimizer0。旧2診断43.740740GPU秒も次の2400秒予算へ計数。dtype/backend/mode/packet/CP救済なし。次は実GPU比較を起動、元math厳密受入監査込みの予測と新全stateCUDA gateなしでは本科学を起動しない。

[PyTorch公式compile仕様](https://docs.pytorch.org/docs/2.14/generated/torch.compile.html)を参照し、当固定FP32計算の数値/時間は実測で判定。元10B UI復帰、全旧失敗/数値7/Phase0–3/相対・絶対・歴史Web品質基準保持、WSL uv3.12.7/local commitのみ/pushなし。合格recipeのみ独立学習seed/full dev/protected test/採用へ接続。以下は過去の履歴。

Base専用oracle高速化: terminal（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。

FP32 efficient Attentionのreadonly実GPU診断を完了、actual644301終端/実不在。GPU9.280214秒/60、optimizer/新source学習0。両固定点のNLL/勾配/bitwise反復/weights・RNG・grad不変に合格: {"original_fullparent": {"NLL_absolute_error": 0.0, "gradient_global_relative_L2": 6.3803901568322135e-06}, "fixed_masked_staged": {"NLL_absolute_error": 1.1920928955078125e-07, "gradient_global_relative_L2": 1.4672964010969208e-06}}。max forward0.080572/gradient0.285183秒。source timing再利用の計画上科学予測3887.025097秒は元mathの厳密受入監査・新全stateCUDA gate費用を含まず、40分超過が続くため科学config/起動なし。将来全重みparity/held-out品質の証明ではない。次は同FP32/micro8/効率Attentionへtorch.compile fullgraph/defaultを一つだけ適用するreadonly比較を実装し、同2点/NLL2e-6・勾配element/L2/bitwise/RNG/weights不変と4forward+4gradientを120GPU秒以内で測る。初回コンパイル時間も計数、未達ならbackend/dtype/packet等救済なし。owntransactional CUDA gate・元math厳密受入監査と全累積GPU2400秒予測を満たすまで本科学は始めない。

[PyTorch一次資料](https://pytorch.org/blog/accelerating-large-language-models/)がFP32のmemory efficient Attentionを説明するが、当10M/4090の速度や精度はこの実測で判定。旧math科学上限拒否/数値7/全不採用/Phase0–3と旧全品質基準を保持。合格recipeのみ独立学習seed/full dev/protected test/採用。元10B UI復帰、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用oracle高速化: preparation（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。

固定TRAIN32 Web窓・同FP32/autocastなし/TF32なし/micro8/全body教師と分母を保ち、Attention backendのみMATH対EFFICIENT_ATTENTIONを比較するreadonly60GPU秒診断。元10.5B親と固定旧masked-staged終端の2点。事前NLL絶対2e-6、各gradient絶対2e-6+相対2e-5/global L2相対2e-5、candidate反復bitwise/weights・RNG・grad不変を要し、4forward+4gradient実timingを両方式/両点で測る。CPU準備0.229171秒、新GPU/optimizer0。実装最適化は旧40分予算超過を受けた一案で、packet/dtype/制約/品質救済sweepなし。次はこのownGPU診断を実行、失敗なら同backendの無制限再試行なし。

[PyTorch一次資料](https://pytorch.org/blog/accelerating-large-language-models/)がFP32のmemory efficient Attentionを説明するが、当10M/4090の速度や精度はこの実測で判定。旧math科学上限拒否/数値7/全不採用/Phase0–3と旧全品質基準を保持。合格recipeのみ独立学習seed/full dev/protected test/採用。元10B UI復帰、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用有限Web実損失制約: budget_rejected（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。

実CUDA probeは成功・actual643402終端/実不在、検証GPU34.460526秒。本科学最悪予測5509.804174秒＋検証=5544.264699秒>2400、実--freezeが拒否し科学configなし/本学習0。有限投影controlの実NLL2.881102→2.604513は上限2.607075を満たすが学習品質の証明ではない。追加FP32/math保持oracleの最悪5forward+1gradient費用が支配的。上限/packet/制約/品質を変えて救済せず、元10B UI復帰・Base未完成。次は同固定TRAIN/制約を維持する単一のoracle計算高速化案について、数値誤差と実GPU速度を事前条件付きで検証する計画を定義。本科学/Chat/量子化は起動しない。

固定TRAIN保持はheld-out/自然品質の証明ではない。元LR.00001/Adam/全source/条件outcome+EOS maskと旧相対・絶対・歴史Webの全品質基準を保持。合格recipeのみ独立学習seed/full dev/protected test/採用へ接続。Phase0–3/旧数値7/全失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用有限Web実損失制約: probe（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。

実CUDA全state8対4+4/有限値/LR/元Webcursor/実制約に成功、32timingと固定旧CPの有限投影control完了。検証GPU34.460526秒/120、科学教師0。最悪ケース科学予測5509.804174秒、検証込み5544.264699秒/2400。予測は品質/完成の証明ではない。上限内だけscience凍結、同staged実91,641,755CE教師＋追加Web gradient別会計/同日本語・全80/旧全gate採否へ進む。

固定TRAIN保持はheld-out/自然品質の証明ではない。元LR.00001/Adam/全source/条件outcome+EOS maskと旧相対・絶対・歴史Webの全品質基準を保持。合格recipeのみ独立学習seed/full dev/protected test/採用へ接続。Phase0–3/旧数値7/全失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

Base専用有限Web実損失制約: preparation（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。

CPU4testsで有限制約・拒否時rollback・全state連続対再開を確認。CPU準備1.431405秒、固定TRAIN32 Web窓/32638body教師・32768input・130336bytesを既cacheから再利用。新GPU/本学習0。次はownCUDA8対4+4・32timing・有限投影数値controlと最悪ケース速度を120秒内で測り、検証を含む2400秒内の場合だけ本学習へ進む。

固定TRAIN保持はheld-out/自然品質の証明ではない。元LR.00001/Adam/全source/条件outcome+EOS maskと旧相対・絶対・歴史Webの全品質基準を保持。合格recipeのみ独立学習seed/full dev/protected test/採用へ接続。Phase0–3/旧数値7/全失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

次のBase専用有限比較を定義: 実測Web TRAIN body NLLの制約（2026-10-06 JST）。未実装・未起動、newGPU/学習0、Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

rank4対full fresh Adamは全160/採否/終端/UI/224file可搬SHAをcb3c114へ保存し、両不採用。一貫性3対10、EOS13対23、反復64対37、BPB.972906対.973113。当比較598.744819GPU秒。rank4/LR/CP等の救済総当たりは行わない。前の有限変位診断ではWeb CE増分の94.6–98.9%が一次近似の外にあり、soft L2もWeb保持に失敗、stagedはprefix90M時点でBPB1.013622>.981286。次は関数の実損失を制約し、能力を落とす一律低ランク制限と区別する。[GEM一次資料](https://arxiv.org/abs/1706.08840)の記憶損失の不等式制約を参考にしたowned nonlinear extensionで、論文再現/成功保証ではない。

元10.5B親/model/Adam/RNG/scheduler/floor/actualLR.00001から、同Web75/story5/ordinary10/conditional10M referenceをstagedで始める。既conditional outcome+EOS mask/他source不変、完了時91,641,755 CE教師/100M reference/3068更新。旧masked-stage whole recipeのcoh35/EOS79/rep1/BPB1.086812を再利用。既固定TRAIN16から最初32 Web窓（元staged75Mにも含まれる）のbody-only FP32/math CEをoriginal基準の1.01以内に保つ。Adam提案後の有限値が超えた場合のみ、一回のWeb gradientによるNLL超過修正→実NLL確認→同一更新の0.5/.25/.125 backtrack。全不成立なら重み/Adam/RNG/samplerを直前完了状態へ戻して研究分岐終了、未受入教師を完了量へ足さない。追加Web gradient教師・forward観測・拒否試行・GPUを別会計し、旧対照と総教師量やGPUが同じとは称さない。固定TRAIN保持はheld-out Web保持や自然品質の証拠ではない。

先にCPUの厳密constraint/rollback/fullstate testsと永続runnerを実装。CPU60/ownCUDA8対4+4・32timing/projection数値control120秒、実測最悪3068*(source step+5 memoryforward+1 memorygradient)/保存×1.3+評価200秒とprobeが全2400秒内の場合だけscienceを凍結。完了candidateは同dev256/common bytes/Japanese/固定80を全内容判定、または明示数値/受入不能/予算の失敗分岐。強い旧相対/絶対/歴史Webの全gate不変、memory/bound/margin/LR等の救済sweepなし。独立学習seed/full dev/protected test/採用は未達。Phase0–3/数値7/旧全失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

固定rank4対full fresh-AdamのBase比較を実完了（2026-10-06 JST）。Base未完了、実完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

actual641226/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16983459はcomplete・実不在。両3068更新/同91,641,755実教師、全科学183,283,510/physical201,064,448、100M reference各と区別。元10.5B親/同Webcursor/元mixed入力・条件outcome+EOS mask/source窓・教師/末尾cursor/hashを全3068で照合、両fresh Adam/actualLR.00001/scheduler clockとfloorを維持。実CUDA8対4+4と32timingの96更新/2867838検証教師は別会計。科学GPU539.816385+probe58.928433=当比較598.744819秒/1800。GPU予測1144.75秒は実績に置換した。元LoRA W0全不変、rank4学習232,960/一時10,234,112→native merge10,001,152、両実FP32/math native merge control成功。full controlは全10M学習可、raw merge helperの共通frozen flagはfull armに適用せず独立endpoint auditを正本とする。旧数値7失敗/旧全不採用は維持。

同dev256/122,343body tokens/472,055common bytes・日本語192/331/1119各・固定greedy80各/全160を個別に読み、raw全項目一致の旧採点だけを継承。非blind Codex、独立人間ではない。結果: {"full_fresh_Adam": {"BPB": 0.9731125484176233, "rates": {"outputs": 80, "eos": 23, "repetition": 37, "unicode_failure": 0, "role_leak": 0, "empty": 0}, "grammar2": 31, "relevance2": 63, "coherent": 10, "appropriate": 11, "notes_sha256": "aef67ea301ef9ced00b526fc09b81ce8d5c24e892f375086c5a421722708e581", "generation_sha256": "076ea651ea6c14da8ca8370a711a90258737750c339c648f53b06d67c5e153ff", "Japanese": {"semantics": 0.6041666666666666, "jblimp": 0.7673716012084593, "jcqa": 0.353887399463807}}, "rank4_frozen_backbone": {"BPB": 0.9729061351952771, "rates": {"outputs": 80, "eos": 13, "repetition": 64, "unicode_failure": 0, "role_leak": 0, "empty": 0}, "grammar2": 18, "relevance2": 59, "coherent": 3, "appropriate": 3, "notes_sha256": "5f27ccc46d3809ae02fd5e312c6babadb6cbc102ca6be5a55f93f6f28df986d8", "generation_sha256": "6042967682ea3142b13b060955f247aaa51b1279ff24a5e105593a5029e7902f", "Japanese": {"semantics": 0.6041666666666666, "jblimp": 0.7522658610271903, "jcqa": 0.3342269883824844}}}。採否fixed_rank4_and_fresh_full_control_rejected、qualified recipes[]、strong23+8/coh pairedCI>0/EOS>=76/反復<=2・絶対grammar56/coh27/適切27/EOS37/反復<=18/errors0・歴史WebBPB<=.9812859519097707を緩めていない。rank4/fresh fullのpaired差・全理由・会計/source/PID/可搬証拠を保存し、frozen weights/RNG/cursorとnative CPはWSL保持。元final10B UI642223/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start17037931をactual ps/HTTP親410f975d…/busy=falseで確認。

次はQualified recipe only: independent learned recipe seed/full dev/protected test/adoption; otherwise end rank4/reset comparison and identify a distinct evidence-backed Base mechanism. No salvage sweep. rank/module/scale/LR/source/mask/CP/decoder sweepなし。独立学習seed/full dev/protected test/採用は未達、Base完了と実験完了を分ける。関連series累積3848.909241秒は全project費用ではない。Phase0–3/旧失敗/全品質基準保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

固定rank4 LoRAのBase比較: running（2026-10-06 JST）。Baseのみ継続・実完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

文書間packing依存markerは不支持、sequence unlikelihoodは既2比較不採用で再実行しない。今回は元W0を固定してrank4/scale1/dropout0の全attention/MLP7projection×13層だけを学習し、full更新と比較する。一方だけAdamをリセットする交絡を避け、両方fresh AdamW/同hyperparams/元scheduler clockとpermanent floor/actualLR.00001を使う。旧親Adamはprovenanceとして保持し継承したと偽らない。元native10,001,152、rank4の学習232,960/一時10,234,112、統合後10,001,152でnative評価する。凍結backboneでもactive adapterのWeb性能維持は保証されず、soft L2/KL/平均重みと同じ仮説へ代入しない。[一次論文](https://arxiv.org/abs/2106.09685)は当10Mの成功証拠ではない。

実測で両科学configを凍結。actual641226/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16983459をps確認、永続job/log/完了更新のmerged native＋unmerged adapter/Adam/scheduler/RNG/sampler/教師・input/source会計を保存。本科学上限1741.071567秒、検証58.928433秒と合計1800。元UIは科学中停止しfinallyで元final10Bへ復帰。両actual91,641,755教師/各100,532,224input、全160内容/日本語/256common-byteと全旧gateの採否は未完了。restartは実PID不在確認後 scripts/run_low_rank_base_comparison.ps1 -Mode Train -Worker。

同元10.5B親/元Webcursor/seed42/入力/条件outcome+EOSmask/75-5-10-10 reference quota/decoderを維持、両actual91,641,755教師、100M referenceと区別する。旧inherited-Adam mixed/full staged/masked stagedは歴史参照として保存し新matched controlと称さない。strong23+8 coherence/pairedCI>0・EOS>=76/反復<=2、絶対grammar56/coh27/適切27/EOS37/反復<=18/errors0、歴史WebBPB<=.9812859519097707の旧全gateを維持。不合格でrank/module/scale/LR/source/mask/CP/decoder sweepなし。合格recipeだけ独立学習seed/full dev/protected test/採用へ進む。Base/最終採用未達、Phase0–3/旧数値7/全失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

固定rank4 LoRAのBase比較: launch（2026-10-06 JST）。Baseのみ継続・実完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

文書間packing依存markerは不支持、sequence unlikelihoodは既2比較不採用で再実行しない。今回は元W0を固定してrank4/scale1/dropout0の全attention/MLP7projection×13層だけを学習し、full更新と比較する。一方だけAdamをリセットする交絡を避け、両方fresh AdamW/同hyperparams/元scheduler clockとpermanent floor/actualLR.00001を使う。旧親Adamはprovenanceとして保持し継承したと偽らない。元native10,001,152、rank4の学習232,960/一時10,234,112、統合後10,001,152でnative評価する。凍結backboneでもactive adapterのWeb性能維持は保証されず、soft L2/KL/平均重みと同じ仮説へ代入しない。[一次論文](https://arxiv.org/abs/2106.09685)は当10Mの成功証拠ではない。

実測で両科学configを凍結。actual641226/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16983459をps確認、永続job/log/完了更新のmerged native＋unmerged adapter/Adam/scheduler/RNG/sampler/教師・input/source会計を保存。本科学上限1741.071567秒、検証58.928433秒と合計1800。元UIは科学中停止しfinallyで元final10Bへ復帰。両actual91,641,755教師/各100,532,224input、全160内容/日本語/256common-byteと全旧gateの採否は未完了。restartは実PID不在確認後 scripts/run_low_rank_base_comparison.ps1 -Mode Train -Worker。

同元10.5B親/元Webcursor/seed42/入力/条件outcome+EOSmask/75-5-10-10 reference quota/decoderを維持、両actual91,641,755教師、100M referenceと区別する。旧inherited-Adam mixed/full staged/masked stagedは歴史参照として保存し新matched controlと称さない。strong23+8 coherence/pairedCI>0・EOS>=76/反復<=2、絶対grammar56/coh27/適切27/EOS37/反復<=18/errors0、歴史WebBPB<=.9812859519097707の旧全gateを維持。不合格でrank/module/scale/LR/source/mask/CP/decoder sweepなし。合格recipeだけ独立学習seed/full dev/protected test/採用へ進む。Base/最終採用未達、Phase0–3/旧数値7/全失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

固定rank4 LoRAのBase比較: probe（2026-10-06 JST）。Baseのみ継続・実完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

文書間packing依存markerは不支持、sequence unlikelihoodは既2比較不採用で再実行しない。今回は元W0を固定してrank4/scale1/dropout0の全attention/MLP7projection×13層だけを学習し、full更新と比較する。一方だけAdamをリセットする交絡を避け、両方fresh AdamW/同hyperparams/元scheduler clockとpermanent floor/actualLR.00001を使う。旧親Adamはprovenanceとして保持し継承したと偽らない。元native10,001,152、rank4の学習232,960/一時10,234,112、統合後10,001,152でnative評価する。凍結backboneでもactive adapterのWeb性能維持は保証されず、soft L2/KL/平均重みと同じ仮説へ代入しない。[一次論文](https://arxiv.org/abs/2106.09685)は当10Mの成功証拠ではない。

両armの実CUDA/BF16/Flash/compile連続8対4+4 fullstate/history/有限値/no-reheatと初期native/RNG/freshAdam/cursor/count全checks成功。各32timing後の実FP32/math merged native control（atol.0002/rtol.00002・固定4×1024 TRAIN）成功、元数値7失敗は維持。検証96更新/2867838教師は本科学から除外、実GPU58.928433秒/240。実測両3068更新/保存と評価余裕を含む予測1144.749499秒、合計予測1203.677932/1800。実終端/ps不在と元10B UIを確認。本科学/品質はまだ未実施。次は実測予算でconfig凍結→同actual91,641,755各の本比較/全日本語/全160→旧全gate採否。

同元10.5B親/元Webcursor/seed42/入力/条件outcome+EOSmask/75-5-10-10 reference quota/decoderを維持、両actual91,641,755教師、100M referenceと区別する。旧inherited-Adam mixed/full staged/masked stagedは歴史参照として保存し新matched controlと称さない。strong23+8 coherence/pairedCI>0・EOS>=76/反復<=2、絶対grammar56/coh27/適切27/EOS37/反復<=18/errors0、歴史WebBPB<=.9812859519097707の旧全gateを維持。不合格でrank/module/scale/LR/source/mask/CP/decoder sweepなし。合格recipeだけ独立学習seed/full dev/protected test/採用へ進む。Base/最終採用未達、Phase0–3/旧数値7/全失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

固定rank4 LoRAのBase比較: preparation（2026-10-06 JST）。Baseのみ継続・実完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

文書間packing依存markerは不支持、sequence unlikelihoodは既2比較不採用で再実行しない。今回は元W0を固定してrank4/scale1/dropout0の全attention/MLP7projection×13層だけを学習し、full更新と比較する。一方だけAdamをリセットする交絡を避け、両方fresh AdamW/同hyperparams/元scheduler clockとpermanent floor/actualLR.00001を使う。旧親Adamはprovenanceとして保持し継承したと偽らない。元native10,001,152、rank4の学習232,960/一時10,234,112、統合後10,001,152でnative評価する。凍結backboneでもactive adapterのWeb性能維持は保証されず、soft L2/KL/平均重みと同じ仮説へ代入しない。[一次論文](https://arxiv.org/abs/2106.09685)は当10Mの成功証拠ではない。

CPU4tests/1.65秒でzero-B初期native出力一致、私有初期化RNG、実勾配/frozen W0、数学的merge/native tied keys/params、両fresh-Adam連続4対2+2全state一致・改変拒否を確認。最初のwrapper階層とfixture key参照の3失敗は修正し、成功結果を保存した。実CPU準備0.122730秒/上限30。完了済み3068 input/target/source ledgerと217MB compact cacheを再利用し、全corpus照合/再変換なし。newGPU/学習0。次はownCUDA両armの連続8対4+4/全state・有限値/32timing/nativeFP32mergeを240秒以内に実測し、検証＋両学習/評価予測が1800秒以内の場合のみ本比較を凍結する。

同元10.5B親/元Webcursor/seed42/入力/条件outcome+EOSmask/75-5-10-10 reference quota/decoderを維持、両actual91,641,755教師、100M referenceと区別する。旧inherited-Adam mixed/full staged/masked stagedは歴史参照として保存し新matched controlと称さない。strong23+8 coherence/pairedCI>0・EOS>=76/反復<=2、絶対grammar56/coh27/適切27/EOS37/反復<=18/errors0、歴史WebBPB<=.9812859519097707の旧全gateを維持。不合格でrank/module/scale/LR/source/mask/CP/decoder sweepなし。合格recipeだけ独立学習seed/full dev/protected test/採用へ進む。Base/最終採用未達、Phase0–3/旧数値7/全失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

固定rank4 LoRAのBase比較: preparation（2026-10-06 JST）。Baseのみ継続・実完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

文書間packing依存markerは不支持、sequence unlikelihoodは既2比較不採用で再実行しない。今回は元W0を固定してrank4/scale1/dropout0の全attention/MLP7projection×13層だけを学習し、full更新と比較する。一方だけAdamをリセットする交絡を避け、両方fresh AdamW/同hyperparams/元scheduler clockとpermanent floor/actualLR.00001を使う。旧親Adamはprovenanceとして保持し継承したと偽らない。元native10,001,152、rank4の学習232,960/一時10,234,112、統合後10,001,152でnative評価する。凍結backboneでもactive adapterのWeb性能維持は保証されず、soft L2/KL/平均重みと同じ仮説へ代入しない。[一次論文](https://arxiv.org/abs/2106.09685)は当10Mの成功証拠ではない。

CPU4tests/1.65秒でzero-B初期native出力一致、私有初期化RNG、実勾配/frozen W0、数学的merge/native tied keys/params、両fresh-Adam連続4対2+2全state一致・改変拒否を確認。最初のwrapper階層とfixture key参照の3失敗は修正し、成功結果を保存した。実CPU準備0.232737秒/上限30。完了済み3068 input/target/source ledgerと217MB compact cacheを再利用し、全corpus照合/再変換なし。newGPU/学習0。次はownCUDA両armの連続8対4+4/全state・有限値/32timing/nativeFP32mergeを240秒以内に実測し、検証＋両学習/評価予測が1800秒以内の場合のみ本比較を凍結する。

同元10.5B親/元Webcursor/seed42/入力/条件outcome+EOSmask/75-5-10-10 reference quota/decoderを維持、両actual91,641,755教師、100M referenceと区別する。旧inherited-Adam mixed/full staged/masked stagedは歴史参照として保存し新matched controlと称さない。strong23+8 coherence/pairedCI>0・EOS>=76/反復<=2、絶対grammar56/coh27/適切27/EOS37/反復<=18/errors0、歴史WebBPB<=.9812859519097707の旧全gateを維持。不合格でrank/module/scale/LR/source/mask/CP/decoder sweepなし。合格recipeだけ独立学習seed/full dev/protected test/採用へ進む。Base/最終採用未達、Phase0–3/旧数値7/全失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

固定同TRAIN16の文書間history ablationを実完了（2026-10-06 JST）。Base未完了、実完成時に通知・停止、Chat/Dialogue/SFT/量子化なし。

actual638526/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16900679はcomplete・実不在。元10.5B親と前mask/mixed終端で各16同input/実masked教師/絶対RoPE位置を固定し、same-document causal attentionのみ新評価。全32既full-causal CEは再利用、各先頭8のowned対native BF16/math control一致、全weights不変/gradなし/eval/finite/RNG成功。GPU6.211293秒/上限30、optimizer/新学習教師0。局所TRAIN記述: {"original_fullparent": {"conditional": {"teachers": 8473, "isolated_teacher_weighted_CE": 2.553360956021609, "cached_full_teacher_weighted_CE": 2.798207910061164, "teacher_weighted_CE_change": -0.24484695403955486, "supported_batches": 16, "positive_batches": 0, "batches_increase_at_least_point1": 0, "minimum_CE_change": -0.27555912816247297, "median_CE_change": -0.24579462489689097, "maximum_CE_change": -0.21217391623119086}, "EOS": {"teachers": 1215, "isolated_teacher_weighted_CE": 4.1753979718243635, "cached_full_teacher_weighted_CE": 6.615145723319348, "teacher_weighted_CE_change": -2.4397477514949846, "supported_batches": 16, "positive_batches": 0, "batches_increase_at_least_point1": 0, "minimum_CE_change": -2.5350683057630388, "median_CE_change": -2.4411620644175867, "maximum_CE_change": -2.3104166143080764}, "marker": false}, "completed_masked_mixed": {"conditional": {"teachers": 8473, "isolated_teacher_weighted_CE": 0.24023822393493896, "cached_full_teacher_weighted_CE": 0.17014298397684083, "teacher_weighted_CE_change": 0.07009523995809813, "supported_batches": 16, "positive_batches": 16, "batches_increase_at_least_point1": 0, "minimum_CE_change": 0.04992692486216971, "median_CE_change": 0.07254832744108443, "maximum_CE_change": 0.08593639362551989}, "EOS": {"teachers": 1215, "isolated_teacher_weighted_CE": 0.030822170075075126, "cached_full_teacher_weighted_CE": 0.008565040381908907, "teacher_weighted_CE_change": 0.02225712969316622, "supported_batches": 16, "positive_batches": 16, "batches_increase_at_least_point1": 0, "minimum_CE_change": 0.018228417997689622, "median_CE_change": 0.021473775563403456, "maximum_CE_change": 0.028195749011452068}, "marker": false}}

事前終端history依存markerはFalse（conditional教師weighted CE増分>=.1かつ増分>=.1のbatch>=12/16）。この固定TRAIN/単一学習seed・cache再利用の局所観測で自然生成改善の証明ではない。次の具体分岐: End this packing hypothesis; no packing training variant. Determine a distinct Base mechanism from retained evidence.。当診断のinput/CP/ratio/mask/source/tolerance/decoder sweepなし、旧全不採用と全品質基準維持。raw points/control/会計/PID/source/tests/configはdocument_context_ablation_completion/portable/archiveへ保存、tensorはnative。元10B UI638600/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16901736をactual ps/HTTP親410f975d…/busy=falseで確認、関連series累積3250.164423秒（全project費用ではない）。Base採用/独立seed/full dev/protected test未達、Phase0–3/数値7失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

文書間historyの固定ablationを実装・CPU準備完了（2026-10-06 JST）。Baseのみ継続/実完成時に通知・停止、Chat/Dialogue/SFT/量子化なし。

関連CPU3tests/0.84秒で先頭partial segment/BOSごとの正確なcausal境界、native full-causal path一致（atol/rtol1e-6）、実small modelの他文書変更/未来変更の非干渉・weights/RNG不変、異なる教師数の集計/marker/欠損・count改変拒否を確認。fixtureは学習品質の証明ではない。実準備0.138553秒/上限15、既TRAIN16/全32 cached model point/実masked targetsとsource教師数を再利用、source scan0。configs/phase6/document_context_ablation.jsonを凍結、newGPU/optimizer/学習教師0、未起動、GPU全30秒。元10B UI637630をactual ps/HTTP親410f975d…/busy=falseで確認。

次はscripts/diagnose_document_context_ablation.ps1で永続起動→各model先頭8のnative対owned full-causal BF16/math control一致（atol.02/rtol.002固定、失敗なら終了）→全16同input/教師/絶対RoPE位置のsame-document causalのみ新評価→全32delta/局所marker/readonly/実終端/UI/可搬証拠/commit。終端conditional教師weighted CE増分>=.1natsかつ増分>=.1のbatch>=12/16が支持された場合のみ別の数値条件を両armで揃えたattention-policy学習比較を定義。未支持なら当packing仮説を学習せず終了。全品質基準/旧不採用/Phase0–3/数値7失敗維持、Base採用/独立seed/full dev/protected testは未達、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

TRAIN勾配診断の解釈と一つの文書境界context仮説を定義（2026-10-06 JST）。前診断は6bae3d1へ保存。Baseのみ継続/実完成時に通知・停止、Chat/Dialogue/SFT/量子化なし。

固定TRAIN16で条件文の実教師比1.772%に対し元親の全勾配二乗への寄与中央値20.594%、終端0.344%。本文CE2.159→.197/EOS6.615→.008565で学習例はよく予測されるが、自然な生成80は一貫性11/EOS22/反復35で不採用。教師比だけでloss希釈や学習不足を確定せず、reference-mass再重み付けは起動しない。既文学+Web/Wikipedia/自然story/別public source等の失敗も保持し、無制限のsource/filter探索へ戻らない。

document_context_ablation_proposal.jsonで元causal packingの文書間historyへの依存を局所診断する。元親/前mask-mixed終端と同TRAIN16/同IDs・mask教師・絶対RoPE位置・logical32/micro8を固定し、BOS2ごとのsame-document causal attentionだけを変えたread-only forwardを比較。元全32CEは再利用、各checkpoint先頭8のみowned control一致確認。CPU準備15秒/GPU全30秒/optimizer・新学習教師0、native forward/境界隔離・未来遮断/元path一致CPUtest/永続runnerを先に用意。未実装・未起動、同学習実験やBase採用ではない。終端conditional平均CE増分>=.1natsかつ増分>=.1のbatch>=12/16の事前局所markerが支持された場合だけ、別の数値条件を両armで揃えたattention-policy学習比較を定義する。未支持なら当packing仮説で新学習せず終了。元strong/absolute/歴史Web保持・旧失敗/Phase0–3/数値7失敗は維持、独立学習seed/full dev/protected test/採用は未達。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

固定TRAIN16・二endpointのread-only勾配寄与診断を実完了（2026-10-06 JST）。Base未完了、完成時に通知/停止、Chat/Dialogue/SFT/量子化なし。

actual637533/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16844400はcomplete・実不在。元10.5B親と前mask/mixed終端で全16同TRAIN batch/context1024/logical32を固定micro8で測定、unique10001152paramを一回、実勾配target478111/model・distinct input524288。optimizer/新学習教師0。全32pointの5source-target group和と独立token-mean CEの相対L2誤差<=.02、全不変weights/gradなし/eval/finite/RNG checks成功。GPU36.001037秒/上限90。局所記述値: {"original_fullparent": {"conditional_TEACHER_fraction": 0.017721826103143413, "conditional_gradient_total_squared_norm_contribution": 0.2059382125735283, "Web_conditional_median_cosine": 0.010003392343895115, "maximum_decomposition_relative_L2_error": 0.002434558467939496}, "completed_masked_mixed": {"conditional_TEACHER_fraction": 0.017721826103143413, "conditional_gradient_total_squared_norm_contribution": 0.003440591273829341, "Web_conditional_median_cosine": -0.0016139320091399173, "maximum_decomposition_relative_L2_error": 0.002827463438734412}}

source_gradient_attribution_completion/portable/archiveへraw points/実会計/PID/コード/tests/config/数値分解を保存。元10B UI637630/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16848446はactual ps/HTTP親410f975d…/busy=false。関連series累積3243.953129秒（全project費用ではない）。勾配はこのTRAIN16/一学習seed/選定済二endpointの局所観測、optimizer方向/品質/因果/自動loss重み変更の証明ではない。元第四条件の不採用・全品質基準/旧失敗・Phase0–3/数値7失敗を保持、Base採用/独立seed/full dev/protected test未達。次はこの結果と既四条件から別機序の一つのBase介入を比較/予算付きで定義する。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

固定TRAIN16・二endpointの勾配寄与診断を実装・CPU準備完了（2026-10-06 JST）。Baseのみ継続し実完成時に通知/停止、Chat/Dialogue/SFT/量子化なし。

関連CPU3tests/0.85秒（tied parameter一回・不均一mask/分母・microbatch加算・逆向き勾配・zero support/null cosine・不変model/RNG・数値不一致/非有限値拒否）とPS構文成功。CPU準備3.162608秒/上限30、元mixedの先頭16同TRAIN input/reference digest/実masked target digest/source routes/会計が実旧historyと一致。217MB cache再利用・全source再scanなし。original10.5B親と前失敗終端を品質選別せず固定、logical32/context1024を8系列ずつ計算し、同logical全実教師分母でFP32 parameter gradientsを加算する。nativeBF16/math・unique tied parameter・元token-mean CE、5target group和と独立元CE勾配の相対L2誤差<=.02を全model/batchに事前固定。数値基準を品質基準と混同しない。新GPU/optimizer/学習教師0、configs/phase6/source_gradient_attribution.json凍結・未起動、全GPU上限90秒。

元10B UI635754をactual ps/HTTP親410f975d…/busy=falseで確認。次はscripts/diagnose_source_gradient_attribution.ps1で永続read-only起動→全32point/不変weights・gradなし/eval/finite/RNG/数値分解一致/実終端/UI/可搬証拠/commit。前第四条件は0c81347へ不採用保存、Base採用/独立学習seed/full dev/protected test未達。勾配は局所観測で品質や原因・重み変更の自動推奨ではない。凍結旧source/Phase0–3/数値7失敗/全品質基準保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

混在順序×outcome/EOS教師の第4条件と全評価を完了、不採用（2026-10-06 JST）。Baseは未完了。完成・採用時に通知して停止し、Chat/Dialogue/SFT/量子化は開始しない。

actual635420/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16750671は実終了・不在。科学3068更新/実教師91641755/reference100M/physical100532224、source別窓・元教師・mask教師・digest/cursorは既3条件と一致。検証48更新/1433919教師は科学と別。scienceGPU261.299751+probe17.989334=新全279.289085秒/上限900。全256body/common472055byte・日本語192/331/1119・greedy80・bridge/retention128を完了し、全80rawに個別理由を保存（同raw8例は旧採点継承、非blind Codex/独立人手なし）。

新mask/mixedはBPB0.973096652、文法31/関連64/一貫性11/適切12/EOS22/反復35/Unicode-role-empty0（各80）。意味61.458%/JBLiMP77.039%/JCQA35.389%。歴史Web保持guardは通るが、strong23比一貫性-12/paired CI[-.2625,-.025]、mask/staged35比-24/CI[-.425,-.175]で内容・EOS・反復基準未達。4条件ではmixedがWeb保持、stagedが完結に優れる局所tradeoffを観測。mask効果の一貫性交互作用-5/CI[-.2,.0875]は0を含む。全旧採点/失敗/品質基準を保持し、独立seed/full dev/protected test/採用は未実施。今回比較は終了、weight/ratio/mask/source/CP/LR/decoder sweepで救済しない。

terminalのactive_job/全raw/review/会計/費用をinterleaved_outcome_completion/portable/archiveへ保存。元10B UI635754/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16777332をactual ps/HTTP親410f975d…/busy=falseで確認。関連series累積3207.952093秒（全project費用ではない）。次はsource_gradient_attribution_proposal.jsonのread-only TRAIN勾配診断のみ。固定元親と今回終端/先頭16同TRAIN batches、5source-target groupの実token-mean CE勾配寄与/内積を測る。CPU準備30秒/新GPU全90秒/optimizer・学習教師0、実装/解析CPUtest/不変性・RNG/数値分解一致/永続PIDを先に用意する。未実装・未起動。局所勾配で原因や増量の有効性を断定せず、新学習介入は別の比較・予算を要する。Phase0–3/旧数値7失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

混在順序×固定outcome/EOS教師の実GPU比較を永続起動（2026-10-06 JST）。own source会計/CUDA gate/実測設定は6970309へ保存したprogress。Baseのみ完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

actual635420/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16750671をalive/ps確認、configSHA4f91703748a2f3f83b40ef0e291266537cc494dac0b65359c3b8eec1d86c22e9、run reports/phase6/interleaved-outcome-order-20261006。観測stagegeneration80、直近教師91426867/新実hard教師91641755（reference100Mと区別）、直近loss2.5054211616516113有限。status setupの初期ラベルだけで停止を推定せずPID/heartbeat/教師/完了checkpointを根拠とする。既3条件/両CPU source hashesはそのまま、Web実cursor・全model/Adam/scheduler/RNG/実LR.00001継承。GPU新全上限900/own probe17.989334秒、元UIは実job中停止・durable finallyで復帰。実GPU gate48更新/教師は科学へ加えない。

reviewer/four-cell analysisを追加、CPU2tests/1.70秒で実CPU masked stateのreference教師誤計数・source target SHA改変・欠損更新と不均一byteのpaired四条件交互作用を確認。fixtureは実モデル品質/独立seedの証明ではない。関連source/counter digestと全80raw採点を要求し、既strong/絶対/歴史WebBPB基準を変更しない。全評価/80内容/四条件採否は未完了。再開はactual不在確認後scripts/run_interleaved_outcome_order.ps1 -Mode Train -Worker、観測timeoutだけで重複起動しない。

次は同jobの全256commonbytes/日本語192-331-1119/greedy80/bridge-ret128完了→全80個別raw notes/既3条件の旧採点そのまま四条件比較→採否/元UI/可搬証拠/commit。qualified recipe後だけ独立学習seed/full dev/protected test/adoption、Base未完了。ratio/mask/source/CP/LR/decoder sweepで今回を救済しない。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

混在順序×固定outcome/EOS教師のownCUDA準備完了・science設定凍結（2026-10-06 JST）。前shared-prefix診断は3024a2a。Baseのみ完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

actual634770/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16735578はcomplete・不在。元10.5B fullparent d18e3e…のmodel/Adam/scheduler/RNG/actual Web cursor/親sampler lineage/実LR.00001を初期一致確認。mixed8対4+4で全4source/実conditional maskを含む全state/history/finite/source digest/会計の一致に成功。own32steady step0.050137秒、検証48更新/1433919教師/1572864inputを科学と別に記録。probeGPU17.989334秒/上限120。

CPU3tests/1.59秒・実CPU準備28.609346秒/上限60、元mixed3068全reference global digestと両順序source別input/元教師/同mask教師/focus/EOS/全cursors/hashが一致。217MB compact cache再利用、full source index scan/dedupなし。新whole recipeは実hard教師91641755/reference100M/physical100532224/3068更新、源内の系列は同じでglobal順序を変える一条件。旧3条件の学習/評価を再利用し新教師に加えない。CPU歴史global countersはsynthetic protocol fixtureで10.5B実CPU学習と称さない。

configs/phase6/interleaved_outcome_order.json SHA4f91703748a2f3f83b40ef0e291266537cc494dac0b65359c3b8eec1d86c22e9を実測から凍結。train見積157.899330秒に1.3×/save/評価reserve150/余裕50を含みscience405.269129秒、probe込み900秒以内。新科学教師/optimizer0、未開始。raw gates/timings/source会計/元teacher予算差/tests/codeはinterleaved_outcome_preparation/portable.json/archiveへ保存。旧Phase0–3/数値7失敗/全不採用/品質条件を保持。

次はscripts/run_interleaved_outcome_order.ps1 -Mode Trainで永続起動→実91641755教師→共通256bytes/Japanese192-331-1119/80個別/bridge-ret128→既3条件と四条件review/元strong23+8/CI正/EOS76/反復2・absolute/歴史WebBPB全guard→元UI/可搬証拠/commit。既mask-staged35/EOS79/反復1の差も明記して旧採点を変更しない。失敗は一条件で終了しratio/mask/weight/source/CP/LR/decoder sweepで救済しない。qualified recipe後だけ独立学習seed/full dev/protected test/adoption、Base未完了。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

混在順序×固定outcome/EOS教師の未測定条件を実装・CPU準備完了（2026-10-06 JST）。前shared-prefix診断は3024a2a。Baseのみ完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

元10.5B fullstate/実LR.00001を継ぎ、元mixed reference教師進度のmin比率で選ぶsamplerを保持、conditionalだけ既outcome+EOSを教師にする実装。source比率75/5/10/10・本文・source相対順序・mask位置不変。CPU3tests/1.59秒で元mixed reference digest/両順序source別input/reference target/masked target/focusSHA・EOS・全cursors一致、実CPU重み/Adam/scheduler/RNG初期保持・4対2+2全state/history・予算を確認。歴史global counterはsynthetic protocol fixtureで10.5B実CPU学習の証拠とはしない。PS構文成功。

実CPU準備28.609346秒/上限60。3068更新の元mixed全input/reference targets/global digestを旧metricsと確認し、既staged全窓とのsource別input/教師/EOS/focus/終端cursor/hashが一致。217MB compact cache再利用・full source index scan/dedupなし。元reference100Mに対し実hard教師91641755、conditional1641755/他90000000、同source masked教師量のwhole recipe比較でglobal順序は異なる。configs/phase6/interleaved_outcome_order_probe.jsonを凍結。科学/実GPUはまだ0、元UI634033を直前ps確認。

次はscripts/run_interleaved_outcome_order.ps1 -Mode Probeでown実CUDA mixed8対4+4/全source実mask保存再開・有限値・32steady timing→実測1.3×+save+評価reserve150+50/all probe失敗込み900秒に収まる場合のみscience凍結→実91.641755M新教師/共通256bytes・全日本語192-331-1119・80個別/bridge-ret128/4条件比較→採否/元UI/可搬証拠/commit。旧3条件再学習/旧GPU再評価なし、元strong/absolute/歴史WebBPB全guardと旧mask35/EOS79/反復1の差を保持。失敗は一条件で終了しratio/mask/source/CP/LR/decoder sweepで救済しない。Base採用/独立学習seed/full dev/protected testは未達、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

固定shared-prefix Web loss診断を実完了、学習順序×教師対象の未測定一条件を定義（2026-10-06 JST）。前mask全学習/80不採用は4a9d124。Baseのみ品質・独立学習seed/full dev/protected test/採用まで継続し実完成時に通知/停止、Chat/Dialogue/SFT/量子化なし。

actual633971/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16678125はcomplete・不在。固定CP323185一つだけに全256 full body122343/common472055byteのnativeBF16/mathを新評価、教師・optimizer0、GPU2.093511秒/上限30。weights不変/no gradients/eval/finite/RNG復元の全5checks成功。関連CPU3tests/0.10秒、実準備0.159927秒/上限10、既3model評価再利用・旧GPU再実行0。

歴史WebBPB.971570249→conditional教師0のshared prefix1.013622108→full-target staged1.133612866、masked suffix1.086812357。prefix差+.042051859/paired byte-weighted CI[.040278905,.043796689]、full suffix差+.119990758/CI[.116045128,.124765116]、mask suffix差+.073190249/CI[.069758141,.077377444]、全差で256/256増加。mask全Web悪化の約36.490%は既prefix側で観測され、mask前から歴史guard<=.981285952を超える。残159637普通文教師もsuffixに含むのでconditional単独原因とはしない。source順序/範囲/独立seedを変えていない局所観測で、個々sourceや10M容量限界の証明ではない。原mask採否・全品質基準はそのまま、旧Phase0–3/数値7失敗も保持。

全256paired差/原raw/actual PID/readonly/コード/tests/configをshared_prefix_web_loss_completion/portable.json/archiveへ保存。元10B UI634033/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16678784をactual ps/HTTP親410f975d…/10000007168/busy=falseで確認。関連series累積2928.663008秒（全project費用ではない）。Base未採用/独立学習seed/full dev/protected test未実施。

次はinterleaved_outcome_order_proposal.jsonの未測定一条件。同元10.5B fullparent/実LR.00001、元mixed samplerのmin(reference source教師/quota)による混在順序を使い、conditionalの既outcome+EOS maskと全source比率75/5/10/10・source原文/相対stream順序を固定する。全target/mixed・全target/staged・mask/stagedの既3条件にmask/mixedだけを加え学習レシピ4条件で交互作用を調べる。旧mask比較は結果を変更せず終了、source比率/新素材/mask位置/係数/EOS/decoder/CP選別を追加しない。global順序は変わるがsource別同窓/元target/maskedtarget/cursor/会計をCPUで確認。whole mask recipeの実教師予測91641755（conditional1641755+他90000000）、元reference100Mをactualと混同せず旧shared-prefix/対照学習を新教師に加えない。

新mixed mask sampler/trainer/accounting/runnerとCPUtestsを先に実装、CPU準備60秒/GPUprobe120/新全900秒。own mixed8対4+4実mask/source保存再開・32timing・実測1.3×+save+評価150+50/all probe失敗込みを通してからscience凍結。new科学/検証/GPU0、未実装/未起動。全256/Japanese192-331-1119/80個別/bridge-ret128、元strong23+8/CI正/EOS76/反復2・absolute/歴史WebBPB全guardとmasked-staged35/EOS79/反復1の差を明示。qualified recipe後だけ独立学習seed/full dev/protected test/adoption、失敗は一条件で終了しsweep救済なし。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

shared-prefix固定Web loss診断を実装・CPU準備完了（2026-10-06 JST）。前mask科学/全80/不採用は4a9d124。Baseのみ完了まで継続し通知/停止、Chat/Dialogue/SFT/量子化なし。

CP323185は元source会計のみで固定されたconditional教師0のshared fullstate。既cached historical/strong/maskedの全256body122343/common472055bytesを再利用し、sole new CPのみnativeBF16/math・body/EOS別評価する。関連CPU3tests/0.10秒で不均一byte重み/phase加算/ID・byte・token・非有限値拒否を確認、実準備0.159927秒/上限10。model/Adam有限/実source会計とcached全ID・共通分母を確認しconfigs/phase6/shared_prefix_web_loss.jsonを凍結、GPU全上限30秒/教師・optimizer0。PS構文成功。元UI632547を直前ps確認、newGPUはまだ未実行。

次はscripts/diagnose_shared_prefix_web_loss.ps1で永続read-only起動→全256body/paired byte-weighted差をprefixとsuffixへ分解→実weights不変/no gradients/eval/有限値/RNG隔離/終端/UI/可搬証拠/commit。ordinary残159637もsuffixに含むためconditional単独因果としない。checkpoint選別・旧GPU再評価・Base採用・元品質条件の緩和なし。Base未完了・旧Phase0–3/数値7失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

conditional prefix maskの同入力suffix学習/全評価/80個別読解を完了。生成は改善、Web保持で不採用（2026-10-06 JST）。ownCUDA準備は5ac0fb0へ保存したprogress。Baseのみ実完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

actual632307/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16632215はcomplete・不在。CP323185→323503の科学318更新/同input10420224、reference教師10159637に対し実masked hard教師1801392、削除prefix8358245。他3source/全source順序/元target digest/全終端samplerが元対照と一致。既先行learning/old100M controlは新教師に加えず同教師比較とはしない。実LR.00001/model/Adam/scheduler/RNGを継承、conditionalのみ既outcome+EOS教師、penalty/KL/rank/newsourceなし。probe48更新/653485教師別、実scienceGPU50.638847+probe17.082727=新全67.721573秒/上限600。CPUreview1test/1.77秒でreference教師をactualへ混同/欠損更新/改変reference digestを拒否。

同256 full body122343token/common472055byte・日本語192/331/1119・greedy80・bridge-ret各128を完了。BPB1.086812357、文法72/関連53/一貫性35/適切54/EOS79/反復1/Unicode-role-empty0（各80）。意味61.458%/JBLiMP75.831%/JCQA29.133%。元strongは一貫性23/適切26/EOS76/反復2/BPB1.133613。paired一貫性+12/CI[.025,.275]、全strong相対gateは通る。歴史WebBPB<=.981285952は未達で採用なし。maskは教師数/EOS率も変えるので量のみや単独原因の証明ではない。全80 rawSHA/具体理由、同raw6例は旧スコア継承。幻想/新人物/暗黙設備/自然な別行動/gold不一致は自動失敗にせず、数値誤りと構文は別。非blind Codex・独立人手なし。

全raw/会計/80notes/review/probe/旧CPU失敗/code/testsをconditional_prefix_mask_completion/portable.json/archiveへ保存、tensorはnative。元10B UI632547/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16637761をactual ps/HTTP親410f975d…/10000007168/busy=falseで確認。旧Phase0–3/数値7失敗・全不採用と関連費用を保持、当series累積2926.569497秒（全project費用ではない）。今回mask比較は終了、mask位置/weight/source/checkpoint/ratio/decoder sweepで救済しない。Base採用/独立学習seed/full dev/protected testはまだ未達。

次はshared_prefix_web_loss_proposal.jsonの固定CP323185一つだけのread-only Web body診断。元Web75M/story5M/ordinary prefix後・conditional教師0のCPは未Web評価で、既cached historical/strong/maskedの全256同ID/bytesと比較し劣化が既prefix側にあるかを局所化する。普通文教師159637もsuffixに残るためconditionalだけの因果としない。CPU準備10秒/GPU全30秒/教師・optimizer0、owned runner/tests/有限値/weights不変/no gradients/RNG隔離を先に用意。checkpoint選別/adoption/基準緩和や旧GPU再評価なし。未実装/未起動、証拠に基づく別Base介入だけを定義する。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

条件prefix maskのown実CUDA保存再開/速度測定を完了、同入力suffix設定を凍結（2026-10-06 JST）。Baseのみを完成まで継続し通知して停止、Chat/Dialogue/SFT/量子化なし。

actual631701/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16623816はcomplete・不在。元CP323185のmodel/Adam/scheduler/RNG/全stream・source会計/cursor/実LR.00001が初期一致、実CUDA8対4+4でordinary→conditional切替と実mask更新を含む全state/history/有限値が一致。own32timing中央値0.051915秒、検証48更新/653485教師/1572864inputを科学と別記。probe実GPU17.082727秒/上限120。CPU3tests/1.65秒・実準備2.868702秒/元残318全input/reference target digest一致、初回fixture padding1failed XMLも保持。新source/full index scanなし。

科学suffixは元source-order CP323185→323503の同318更新/physical10420224、reference quota教師10159637に対しmask後教師1801392を予測。元75M Web→5M story→10M ordinary→10M conditionalの先行学習/対照100Mを再利用するので新100M教師・同教師比較と称さない。conditional setup bodyだけをhardCEから外し既存outcome+EOSを保持、他source/input/順序/fullstate/LR不変。configs/phase6/conditional_prefix_mask.json SHA0a363551b149a330ce2a92851baa4057eeede146ef0505e384bef8931a831aab。train実測予測18.403642秒に1.3×/save/評価reserve150/余裕50を含みscience223.924735秒、probe込み600秒以内。本学習まだ未開始。raw gates/timing/counters/failure/source/testをpreparation/portable.json/archiveへ保存。

次はscripts/run_conditional_prefix_mask.ps1 -Mode Trainで永続起動→同256common bytes・全日本語192-331-1119・greedy80個別raw/bridge-ret128→元strong/絶対/歴史WebBPBなど全guardで採否→元UI/可搬証拠/commit。失敗時にmask位置/EOS weight/source/checkpoint/decoder sweepで救済しない。qualified pilot後だけ独立学習seed/full dev/protected test/adoption、Baseまだ未完了。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

条件文prefix targetのmaskを実装・CPU準備を完了（2026-10-06 JST）。Baseのみを完成まで継続し通知して停止、Chat/Dialogue/SFT/量子化なし。前L2両100M不採用は3d56a71へ保存。

元source-orderのfullstate CP323185から全stream/sampler/quota/model/Adam/scheduler/RNG/実LR.00001を保持する実装。conditionalだけ既存outcome focus+EOSをhard教師とし、他3sourceは変更しない。元の残318更新をCPU2.868702秒で一度だけ再構築し全input/元target digest/source counters/終端全samplerが対照と一致。physical input10,420,224、reference教師10,159,637、実masked教師1,801,392の予測を分け、同教師100M比較としない。関連CPU3tests/1.65秒（実入力/terminal padding/zero-focus conditionalのEOS保持/全state4対2+2/予算）、PS構文成功。初回1testはfixtureの末尾にpaddingがなかったため失敗、十分な終端batchで明示的に検証するようtestだけ修正・初回XMLを保存、実GPU0。source/full corpus再走査なし。

probe設定configs/phase6/conditional_prefix_mask_probe.jsonを凍結。own CUDA8対4+4はordinary→conditionalの切替と実mask更新を含める（最初4更新だけではmaskの検証にならない）。32steady timings・probe全120秒/比較全600秒、実suffix見積1.3×+save+評価reserve150+50を満たしてからscience凍結。実probe/GPU/科学教師はまだ0、元UI629733を直前ps確認、永続起動scripts/run_conditional_prefix_mask.ps1 -Mode Probe。実終了まで重複しない。

次はown実CUDA gate/timings→予算内のみ同suffix318更新/同256bytes・全日本語192-331-1119・greedy80個別/bridge-ret128→全80raw notes・元strong/absolute/歴史WebBPB等の全条件で採否・UI復帰・commit。oldstrong EOS>=76/反復<=2/一貫性23+8/CI正などを変更せず、失敗時にmask/weight/source/checkpoint/decoder sweepで救済しない。Base品質採用/独立学習seed/full dev/protected testは未達。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

固定parameter L2の両100M学習/全評価/160個別読解を完了・不採用（2026-10-06 JST）。CUDA準備d1b44f0・永続起動66bdd3dはprogress。Baseのみ継続・実完成時に通知/停止、Chat/Dialogue/SFT/量子化なし。

actual629059/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16481322はcomplete・不在。両科学200000000教師/6136更新、同input/targets/source/全cursor会計が一致、fixed L2教師0。検証80更新/2615904教師別。scienceGPU481.338513+probe/失敗33.680480=新全515.018993秒/上限1800。係数.04161064039180984/親6d901bd…/実LR.00001を保持。全256common472055bytes/日本語192-331-1119/greedy80各/bridge-ret128各が完了、2arm全160をrawSHA/具体理由で保存。旧raw完全一致は対照7/candidate15の採点をそのまま継承し、幻想/新人物/暗黙設備/自然な別行動/gold不一致を自動失敗にしない。非blind Codex、独立人手なし。

newmatched CE: BPB1.035666704、文法65/関連52/一貫性32/適切37/EOS69/反復6、意味54.167%/JBLiMP76.133%/JCQA29.759%。parameteranchor: BPB0.990667075、文法59/関連60/一貫性25/適切29/EOS67/反復6、意味52.604%/JBLiMP75.529%/JCQA32.172%。両Unicode-role-empty0（各80）。candidate一貫性差-7/CI[-.2125,.05]、oldstrong23比+2/CI[-.0875,.15]でいずれも相対条件未達。絶対一貫性27・歴史WebBPB<=.981285952も失敗。差のCIは0を含み有意な悪化の証明ではない。newCEは絶対screenを満たすがoldEOS76/反復2/歴史WebBPBを満たさず採用なし。oldstrongへの比較は追加mixed100Mの履歴も違い、単純学習量だけの因果としない。

全raw/counters/160notes/review/transfer/probe費用/失敗はparameter_displacement_anchor_completion/portable.json/archiveへ保存、モデルtensorはnative。元10B UI629733/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16529959とHTTP親410f975d…/10000007168/busy=falseを確認。旧Phase0–3/数値7失敗・全不採用と関連費用を保持、当series累積2858.847924秒（全project費用ではない）。Base品質採用/独立学習seed/full dev/protected testは未達。L2係数/anchor/層/source/decoder sweepで救済しない。

次はconditional_prefix_mask_proposal.jsonの一つの別の損失target仮説を実装。Setup語句のhardCEを外し既存outcome focus+EOSだけをconditional教師とする案。source変更0、roleなし、他3source・同残input/順序/実LR/fullstateを保持。oldsourceの最初conditional教師update323190直前の250保存CP323185をsource会計だけで選定・実finite/fullstate/conditional教師0確認、quality/endpoint選別なし。全source2048docs/body85350/outcome12302/prefix73048/EOS2048を既小arrayで確認。hard教師数とEOS率は変わるので同教師100Mとは言わず、原reference quota/digestとmasked actual教師/byte/digestを分ける。CPU準備30/GPUprobe120/新全上限600、own実maskedCUDA保存再開/steady32/実測1.3+reserve150+50を満たしてから科学設定凍結。元strong/absolute/歴史全guardを維持、未実装/未起動、GPU/教師0。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

固定parameter L2対照の本比較を永続起動（2026-10-06 JST）。実両CUDA gate/32timingと凍結設定はd1b44f0へ保存したprogress。Baseのみ継続・完成時に通知/停止、Chat/Dialogue/SFT/量子化なし。

actual629059/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16481322を実確認、configSHA7fb897e9905eceaecc754a4d323f2e8d90c68e47e592872c8f20cf980721e249、run reports/phase6/parameter-displacement-anchor-v3-20261006。stage matched_staged_CE-training、追加教師78457227/当arm100M、loss1.9584909677505493有限で継続。初期status setupラベルで終了/停止を推定せずPID/heartbeat/teacher更新を用いる。両科学200M＋検証2615904教師は別、probe成功/失敗GPU33.680480秒を保ち全上限1800。元UIは科学実行中停止、durable finallyで元10Bへ復帰。

review_parameter_displacement_anchor.pyを準備、実CPU terminal ledger/anchor/body+EOS CE+L2/連続更新/教師0の誤会計を拒否する1test/1.63秒成功。これは品質判定ではなく、本流/評価/全160内容/採否は未完了。親state/core/anchor/source/係数は凍結後不変、checkpoint/optimizer/RNG/samplerは完了更新で保存。再開はactual不在確認後scripts/run_parameter_displacement_anchor_v3.ps1 -Mode Train -Worker。観測timeoutやラベルだけで再起動しない。

次は同実jobの両100M/共通256bytes・日本語192-331-1119・全80各・bridge/retention各128→160個別raw notes/両対照と旧全基準の採否→UI/可搬証拠/commit。fixed lambda/anchor/source/decoder sweepなし、pilot合格後だけ独立学習seed/full dev/protected test/adoption。Base未完了・未採用、全旧失敗とPhase0–3/数値7失敗を保持。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

parameter変位の固定L2比較を実装・両arm実CUDA gate/速度測定を完了（2026-10-06 JST）。前TRAIN診断はd516c78へ保存したprogress。Baseのみ継続、品質・独立学習seed/full dev/protected test/採用で完成時に通知・停止。Chat/Dialogue/SFT/量子化なし。

same mixed fullstate SHA6d901bd…/update323503から両新arm同追加staged100Mを実装、candidateだけlambda=.04161064039180984のunique parameter L2。両armmodel/Adam/scheduler/RNG/actualWebcursor/親sampler/anchor/actualLR.00001の初期一致を実確認。短source/local quotasのみ同seed42でresetし親cursorはlineageへ保持。tieは一回、L2教師0。CPU初回fixtureのscheduler base_lrsとoptimizer initial_lr不一致2failedを保存し修正、4tests/1.64秒で解析勾配・anchor不変・両CPU4vs2+2全state/phase/counters・費用計算が成功。

v1preflightはnormalized core hashをrawSHAと比較してGPU前に拒否。v2はCUDAanchor対CPU親の検証でGPU1.878139秒・optimizer0で停止、actual628139不在。旧source/config/rawを変えずv3owned修正版に分離。v3probe actual628394/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16468641はcomplete・不在。実両CUDA4vs2+2のmodel/Adam/scheduler/RNG/sampler/lineage/全会計/digest/loss/CE/L2/有限値一致、各32steady timingsを確認。検証80更新/2615904教師は科学へ加えず、成功GPU31.802341＋失敗=33.680480秒/上限120に保持。

本比較の設定configs/phase6/parameter_displacement_anchor_v3.jsonを実測から凍結。対照step0.145319秒/candidate0.054650秒、2armtrain予測に1.3×・save・評価reserve150・余裕50を含み1004.601240秒、probe込み1800秒以内。run reports/phase6/parameter-displacement-anchor-v3-20261006、永続起動scripts/run_parameter_displacement_anchor_v3.ps1 -Mode Train、再開はactual不在確認後-Worker。新科学教師/optimizer0、本学習まだ未開始。全raw/gates/timings/failures/source/testsはparameter_displacement_anchor_preparation/portable.json/archiveへ保存、旧失敗/Phase0–3/数値7失敗を保持。

次は実両100M→同256共通byte/日本語192-331-1119/greedy80各/bridge-ret128→全160個別raw notes/採否/UI復帰/commit。newmatched対照とoldstrong staged23+8/CI正/EOS76/反復2・絶対/歴史BPB全guardを維持。coefficient/anchor/source/decoder sweepなし。pilot合格後だけ独立学習seed/full dev/protected test/採用へ進む。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

有限な重み変化のTRAIN診断を実完了（2026-10-06 JST）。前回midpoint不採用はb4e71dcに保存。Base未完了・未採用、完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

既保存TRAIN Web32 blocksの元x/ySHAを再利用し、mixed/midpoint/staged同3重みのFP32 mathを測定。CPU3tests/.82秒、実準備0.332303秒/上限30、GPU2.118768秒/上限120。actual627394/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16421220はcomplete・不在。全12点/raw metadataと統計を確認、全119unique paramsの有限勾配、全モデル重み不変/.gradなし/RNG復元。input32768/body32626/EOS71各model、科学教師/optimizer0。巨大corpus再scan/再encode/新選別なし。

Web bodyCE増加は4/4で0.438–0.474 nats/token、一次予測0.0050–0.0257、非線形残差比94.6–98.9%。事前harm>=.02/3以上と非線形>=50%/3以上はいずれも4/4。body-token加重実差0.462941963/一次0.016857954/残差0.446084009。局所一次診断が捉えなかった有限変化を観測したが、一方向/4 TRAIN batchesでHessian・全path凸性・唯一原因・モデル容量限界・品質改善は証明しない。全旧quality/source失敗とPhase0–3/数値7失敗を保持。

全点/会計/source/tests/次proposalをfinite_parameter_displacement_completion/portable.jsonとrawSHA付きarchiveへ保存。元10B UI627463/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16421867をactual/HTTP親410f975d…/10000007168/busy=falseで確認。関連GPU累積2343.828931秒（全project費用ではない）。独立学習seed/full dev/protected test/採用は未達。

次はparameter_displacement_anchor_proposal.jsonの一つのmatched2-arm比較を実装・実probeする。完了mixed fullstateを両arm同親とし、同追加staged100M教師×2、candidateだけunique parameter変位のL2 penaltyを加える仮説。lambda=0.0416106403918を今回の加重残差/固定direction normから一度定義、sweepなし。これは一方向からの等方性仮説で効果保証ではない。以前のparent-output KLと異なるparameter制約・mixed anchorを試し、親変更に対して新matched CE対照を必須にする。元strong staged23+8/CI正/EOS76/反復2・絶対/歴史BPB全guardを保持。実CUDA4vs2+2/steady32/実測1.3+reserve150+50/全probe込み1800秒gate前に科学設定を凍結・起動しない。提案未実装/未起動、教師/GPU0。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

同一親の重み50%平均を実評価・全80採点し、不採用（2026-10-06 JST）。前turnの翻訳source不採用は1b22447に保存したprogress。Baseのみ継続・完成時に通知して停止、Chat/Dialogue/SFT/量子化なし。

既存7モデル/不採用3sourceの92,256bytes summaryをCPU0.00994秒で整理し、同10.5B親/同100M教師のmixed対staged重みを各50%で平均する未実施一条件を凍結。関連CPU3tests/0.75秒、実prepare0.35952秒で10,001,152param/120model keys。FP32平均とtied embeddingを保持、optimizer/scheduler/RNG/sampler/会計を混ぜずmodel-onlyとして保存し、resume可能な学習stateと称さない。新科学教師/optimizer0、係数やendpoint/layer選別の総当たりなし。WiSE-FT/Model soupsは着想の一次資料で、日本語10Mへの効果の証拠に代入しない。

actual625718/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16346405は全GPU評価終了・不在。実GPU52.114144秒/上限300、native run reports/phase6/weight-average-comparison-20261006。全256 body/same472055bytes・日本語192/331/1119・greedy80・bridge/retention各128を完了。BPB1.011781478、文法66/関連45/一貫性20/適切21/EOS71/反復8/Unicode-role-empty0（各80）。意味52.083%/JBLiMP76.435%/JCQA31.859%、bridge両条件65/128・retention35/128。全80個別読解/rawSHA/理由を保存、同じrawの旧4例はスコアそのまま再利用。幻想・新人物・自然な別行動・暗黙の設備・gold不一致は自動失敗にしない。非blind Codexで独立人手なし。

staged対照23/26/76/2/BPB1.133613からWebBPBは改善するが一貫性20/適切21/EOS71/反復8で強いrelative条件未達。paired一貫性差-3/CI[-.15,.075]、絶対一貫性27/適切27・歴史WebBPB<=.981285952も失敗。不採用を確定し、このmidpointの係数/重み組合せ/layer/decoder変更で救済しない。保存済全256を同ID/bytesで集計すると、midpoint BPBはendpoint平均1.054216223を0.042434746下回り、256/256文書で平均NLLより低い。これは一点の非線形性の観察で、全path凸性や能力改善の因果保証ではない。新forward/GPU0。

全採否/会計/全80/transfer/rawをSHA付きweight_average_comparison_portable.json/archiveに保存。元10B UI625983/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16352051をactual ps/HTTP親410f975d…/10000007168/busy=falseで確認。旧Phase0–3/数値7失敗/全source不採用/既関連GPU2289.596018秒を保持、新比較込み2341.710163秒（全project費用ではなく当該series）。独立学習seed/full dev/protected test/採用は未達。

次はfinite_parameter_displacement_proposal.jsonの一つのread-only診断を実装する。旧source-gradient assayで未測定だったfinite displacementの害と一次勾配予測を、既保存TRAIN Web32 blocks（4×8×1024）の同x/ySHAで測る。mixed/midpoint/staged三既存重み・FP32 math、mixedのbodyCE gradient dot(staged-mixed)、実損失差と非線形残差、EOS別を記録。教師/optimizer0、CPU準備30秒/GPU全上限120秒、基準を先に固定。旧cosine/仮想一Adam更新を反復せず、新Web/source全量scan/評価語句の学習/自動regularizer/merge sweepなし。局所TRAIN32で唯一原因や全品質は証明しない。実source/runner/tests/事前条件の準備とactual CUDA完了をこれから進め、証拠に応じた別のBase比較だけを選ぶ。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

同一親の2つの完了100Mモデルを50%ずつ平均したBase診断を実行中（2026-10-06 JST）。前turnは翻訳sourceのfixed64不採用を1b22447へ保存したprogress。Base完了時に通知・停止、Chat/Dialogue/SFT/量子化なし。

既存7モデル/不採用3sourceのsummary92,256bytesだけを実CPU0.00994秒で集約、raw再採点/GPU/全量scanなし。段階CEは一貫性23/EOS76/反復2/BPB1.133613、mixed同親100Mは4/30/31/.974820、既KL・replay・rankingはWeb BPBと一般生成の同時条件未達。このtradeoffから未実施の同親重みmidpoint一条件を凍結。係数[.5,.5]・FP32/同tied embedding・nonfloating buffer一致、optimizer/scheduler/RNG/samplerを平均せずmodel-onlyと明記。関連CPU3tests/0.75秒、実prepare0.35952秒で同10,001,152param/120model keys、科学教師・optimizer0。論文WiSE-FT/Model soupsからの適用仮説でこのモデルへの効果保証なし。

actual625718/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16346405、Windowsworker28260をps確認。native run reports/phase6/weight-average-comparison-20261006、configSHAb1be4f9e21c4138884e45cef0c7280f5bce95820d55fea6548d63e9fa22ad114、GPU上限300秒（累積/失敗込み）でdev256全bytes・日本語192/331/1119・greedy80・bridge/retention128を評価。元10B UIは評価中停止・永続worker finallyで復帰。再開はactual PID不在を確認しscripts/run_weight_average_comparison.ps1 -Worker。全80個別raw notes/採否/実終了/UI/可搬証拠/commitはこれから。強いstaged対照23+8/CI正/EOS>=76/反復<=2、全絶対/歴史WebBPB<=.98128595等の元基準を保持、係数/endpoint/layer sweepなし。合格時のみ独立学習recipe seed/full dev/protected test/採用へ進む。旧Phase0–3/数値7失敗・全不採用/関連GPU費用を保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

既存TinyStories-JA翻訳源の固定64を全確認し、今回の置換比較を不採用（2026-10-06 JST）。Baseだけを完成時に通知して停止する境界を維持。Base未完了・未採用、Chat/Dialogue/SFT/量子化は未開始。

凍結proposal/source/seed2026100693/calibration除外から、既存TRAIN追加区間のwhole499066文書を本文変更・再encode・新取得なしで読み出した。serialized140036743/body139038611/本文+EOS139537677、長さ44–512。実CPU0.337270秒/上限60、535MB元indexは1200995bytesのみ部分読み。関連CPU3tests/0.76秒で境界・codec・途中文書とepoch再開・固定除外を確認。固定64は個別rawSHA/rationale付きで全読解し、weak12（上限10）/未解消日本語表現6/所有・主体接続2で内容基準未達。めかしめ、パパとうさぎ、バジーを言い返す、店の絵の具を自分の所有物扱い、父が閉めたドアを姉妹の行動へ置き換える等を記録。幻想・悲劇・省略・未使用の属性は自動失敗にしない。非blind Codex判定で独立人手/外部事実保証なし。

rejected sourceはnative loaderも拒否し、提案100M/CUDA probeは内容前提で取り消した。新科学/検証教師・optimizer/GPUすべて0。凍結後の本文修正/selector変更/reroll/別translation filterでの救済なし。前の13翻訳例の表現0からsource全体の品質を保証できなかった結果で、モデル学習効果や容量限界を示さない。全旧採否/Phase0–3/数値7失敗と関連GPU2289.596018秒は保持。completion/review/全64/code/testsをtranslated_story_source_portable.jsonのraw SHA付きarchiveへ保存、全corpusとcompact arrayはWSL側に保持。元10B UI618479をactual identity/HTTP親410f975d…/busy=falseで確認。

次は既存の完了・採否metadataだけで、今回終了した生成/混合/翻訳source置換と完了したモデル比較の未達項目を一つの有限表へ整理する。追加の全量照合・source選別・同実験GPU反復は行わない。別のBase介入は未検証の仮説・比較・終了条件が定義できた場合だけ実装する。既存品質基準を維持し、合格pilot後の独立学習seed/full dev/protected test/採用まで完了としない。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

既存物語100Mの固定64を全確認・不採用、全64の元sourceを小部分読みで確定（2026-10-06 JST）。前回の16384生成文/source失敗はfd48644に保存したprogress。Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続し、実完成時に通知して停止。Base未完了・未採用、Chat/Dialogue/SFT/量子化なし。

natural_story_source_reuse_proposal.jsonで別親/LR/素材の旧自然25M・storyweight100M・fresh教材量比較と、現在same10.5B staged条件源を比較し、最後のconditional10Mだけを既原文物語に置換する対照を定義。GPU起動前にTRAINの761448whole docs/serialized100000968/body98478072/本文+EOS99239520を確認、長さ34–511で切断0。旧2B poolのaccepted manifest/217MB compact cacheを再利用し13GBindex/5.37GBraw再走査・再取得なし。new corpus0/元原文変更0で、新量の用意やモデル改善としない。

CPU準備v1は固定64を保存した後、記録関数名refとループ変数の衝突TypeErrorで失敗。old metadata Windows-only2filesを正確SHA付きでWSLへ復元した初回定義失敗も隠さない。frozen v1/job/pilotを変えずowned metadata-repair-v2を用い、元draw64 IDs/text/token SHA完全一致で記録だけ完成。失敗+repair CPU0.364282秒/上限60、GPU0。actual64は全件読解/rawSHA/rationaleを保存、weak10で件数は通るが未解消表現4（ひとつの風/一番の素敵/むすんでいるように見えた太郎/ぎくりとした音）がゼロ条件を満たさず全mixed-story source不採用。grammar旗は自然な表現の未解消で、全て詩的読解が不可能という形式的証明ではない。幻想/暗い結末/新しい人物を自動失敗にせず、human/external truth認証なし。100M/GPU probe未実行。

source metadata探索をowned byte-seekで実装し、UTF8/最初・中間・末尾/欠損key/読出し上限のCPU2tests/.04秒成功。元13GB mixture JSONLと上流536MB JSONLから全64を2段のoffset二分探索で照合、実CPU0.181063+0.164494秒（各上限10）、読出し1658555+1222486=2881041bytesのみ。全64本文SHA/bodytokens/TRAIN/source-family/元file-rowが一致。retained SimpleStories51件はweak7/表現4、translation13件はweak3/表現0。これは固定64の相関・非blind観察で元corpus全品質や因果を証明しない。旧root診断72の翻訳の意味失敗も消さない。

次はtranslated_story_source_proposal.jsonの別pinned source-origin比較。既shibatch/TinyStories-JA revision155b4e…のTRAIN追加区間59963449–200000192（serialized140036743、候補499066docs）だけのwhole native viewを用意する案。失敗mixed sourceの良い例だけを選別するのでなく、記録済copy-old-then-append builderで別公開sourceを全件再利用。原文/content/長さで再filterせずcalibration除外/seed2026100693/固定64/CPU60秒を生成前に凍結。新原文/GPU0、source原文・BOS/body/EOSからcompact offsetsを一度だけ導出し、536MBJSONLは64だけ部分読み。候補自身のweak<=10・grammar-grounding0に失敗ならこのorigin比較も終了、filter/length/source sweepで救済しない。

accepted sourceだけをsame fullparent/Adam/scheduler/RNG/実LR.00001、Web75M→story5M→ordinary10M→translation10M/ordinary CE1で強いstagedCE100Mに比較。first90M入力/cursors/counters一致を確認し、末尾source/EOS長さとall-masked Web padding差を正直に別会計。own changed-source実CUDA4vs2+2/32steady timings、150秒reserve/30%/50秒余裕・全probe込み900秒前に科学設定を凍結しない。全既存relative/absolute/歴史WebBPB guard・256full/Japanese192-331-1119/80個別/bridge-ret128維持。旧関連GPU2289.596018秒/Phase0–3/数値7失敗保持、科学GPUjob0、元10B UI618479/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16015140とHTTP親410f975d…/10000007168/busy=false確認。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

TRAIN由来の短文教材16384件を実準備・固定64全読解し不採用（2026-10-06 JST）。前診断・単一source案はdbdd9c5へ保存したprogress。Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続し、実完成時に通知して停止。Base未完了・未採用、Chat/Dialogue/SFT/量子化なし。

narrative_condition_source_freeze.jsonでproposal/accepted TRAIN input/owned renderer/prep/reviewer/test/seedをactual source生成前に凍結。既accepted1024facts/両branch/各8surfaceの全16384文、同48category×surfaceの固定48＋追加16の64を一度だけ準備。実CPU1.353232秒/上限60、body1056722、serialized1089490、本文+EOS1073106、EOS16384。native4096 exact bytes/BOS/EOS/wholebody入力1024内、重複全体文0/切捨て0/role-pad本文0。新独立semantic families/原文corpus0で、表現数増加を意味の独立例数・新公開自然文に置換しない。元24source formsは場面/関係/機構に残り、同surface内でも元formの違いがある。

CPU4tests/1.02秒で実TRAIN全coverage・ opposed状態/数量/時刻/人物/機構・native96 fixture codecと中途document再開・raw content改変拒否が成功。fixtureはactual内容レビューではない。固定64は全件個別に読みraw SHA/rationaleをcontent-notes/reviewへ保存、弱7/64でweak<=10は通るが未解消文法表現3・grounding時系列1のゼロ条件に失敗。causalityの重ねた主語2件、靴の非購入で退店前に「持ち帰ることはなかったのを見て」とする観測理由が問題。grammar旗は自然な文法表現の未解消で、全て形式的に構文解析不可能という証明ではない。全件nonblind Codex、人間/外部事実認証なし。

教材全体を不採用、実native loaderも拒否。凍結後renderer/pilot/selector修正・良い例だけ選択・rerollなし、提案100Mはcontent prerequisiteで取り消し、CUDA probe/学生科学・検証教師/optimizer/新GPUすべて0。失敗は今回の生成表現/時系列でありモデルの学習効果・容量限界・唯一原因を証明しない。既存強いstagedCE/absolute/歴史WebBPB guardの全基準を保持、過去関連GPU2289.596018秒も消さない。準備済みsource/tensorはnative/data、text/source/proposal/tests/全64は可搬archiveへ保存。

次は既存の採用済み自然物語TRAINのmanifest・provenance/content acceptanceと完了same-parent対照だけを有限CPUで確認し、過去と重複しない単一source置換比較を定義する。この不採用sourceは再試行しない。別source/protocolの準備・実CUDA4vs2+2/steady timings/予算gate前にGPUを開始しない。品質pilot合格時だけ独立学習seed/full dev/protected test/adoptionへ進む。科学GPUjob0、元10B UI618479/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16015140とHTTP親410f975d…/10000007168/busy=falseを確認。旧Phase0–3/数値7失敗を保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

同一入力の選択位置・完全greedy本文診断を完了（2026-10-06 JST）。前turnのpositive-anchor100M/全評価不採用を7afe0bfへ保存したprogress。Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続し、実完成時に通知して停止。Base未完了・未採用、Chat/Dialogue/SFT/量子化なし。

decision_span_diagnostic_result/completion.jsonに強いstagedCE/relative ranking/positive anchorの3実終了model×bridge128/retention128×両context/candidateの全3072既存BF16 score requestsを集計。実CPU0.975498秒/上限10、GPU0/newforward0/optimizer0。1536pair rows全てに候補の最初の異なるtarget位置があり、そこまでの完全input IDs一致を確認、共有先行token NLL差最大0。全18cohortと全categoryを保持、元のsum/tokenmean/bytemean・全対照aggregate完全再現。prefix包含を明示するhelper、後続NLLで誤った選択が隠れるcounterexample/argmax連言と候補順位の区別にCPU2tests/.03秒成功。新チェックポイント推論/旧zero-context再測定/巨大index再scanなし。

bridge両極正答（全body/最初distinct選択/完全goldbody greedy）はstaged59/57/31、ranking86/84/27、anchor79/79/68（各128）。anchorでfullsum正解だがdistinct位置が誤りは0/256で、当初疑った後続teacher forcingによる開始選択の隠蔽は主bridge失敗を説明しない。retentionはstaged36/35/15、ranking80/72/14、anchor80/77/32、anchor隠蔽17/256は全て構造cohort。語彙/構造の全分解を残し、小局所のgreedy body改善を自然文一貫性5/80・反復28/80の成功へ置換しない。is_greedyの全target argmax連言は候補body経路を支持するが、その後のEOS停止/新文脈/自然文品質は保証しない。Shared generator/相関poles/teacher forcing/一つのseedの限界を保ち、単独のfirst-distinct loss修正へは進まない。

accepted条件TRAIN sourceは2048docs/serialized89446/body85350/本文+EOS87398、1024facts/16人物/24source表現。例は行動の言い直しを同じ出来事で閉じる記録文。main conditional10Mは同じ小poolの反復で、主Web12Bデータ量と条件・自然文の表現幅を混同しない。これは全corpus品質や唯一原因の証明ではない。既不採用Qwen4B teacher64弱37/publicMagpie64弱23・供給4.23Mも再確認し、そのモデル/prompt/filter/sourceを再試行せず不採用を保持。

次はnarrative_condition_source_proposal.jsonの一つのTRAIN由来自然短文source比較。既accepted1024facts/両branchはそのまま、各category8個の完結2-3文/計16384surface docs案。単なる記録/質問/言い直しから、局所条件を保持して行動/観測結果へ進む文章にする。新独立semantic families/public corpus0、surface量/style/length/EOS頻度も変わるので単純な増量効果とはしない。CPU準備60秒/native4096/wholebody1024上限、予め固定した48category×surface＋16追加の64全読解・weak<=10/未解消grammar-grounding0が必要。不合格からrenderer/filter/rerollで同pilotを合格へ変えない。まだactual source0/学生GPU0。

accepted sourceだけをsame10.5B fullparent/Adam/scheduler/RNG/実LR.00001、Web75M→story5M→ordinary10M→newconditional10M、ordinary body+EOS CE weight1の100Mで強いstagedCE対照へ比較する案。aux rank/KL/anchorなし、変更はconditional source、他3source sequence/cursor/counter一致と変更したconditional physical/EOS頻度を別記。own actualCUDA4vs2+2/32timing/同150秒reserve/30%/50秒＋全probe込み900秒を満たしてから科学設定凍結。元256full bytes/日本語192-331-1119/全80個別読解/bridge-ret128・強いcoherence23+8/CI下限正/EOS>=76/反復<=2・absolute・歴史WebBPB<=.981285952を維持する。品質pilot合格時だけ独立学習seed/full dev/protected test/adoption。GPU科学job0、元10B UI618479/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start16015140とHTTP親410f975d…/10000007168/busy=falseを確認。旧Phase0–3/数値7失敗/全基準/関連GPU2289.596018秒を保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

正解確率を加えた単一100M比較と全評価を完了・不採用（2026-10-06 JST）。実CUDA58checksと永続開始を45cd1faへ保存。Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続し、実完成時に通知して停止。Base未完了・未採用、Chat/Dialogue/SFT/量子化なし。

actual616427/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15962167はcomplete・実identity不在。main100000000CE教師/maininput100532224/3068更新、CP323503 SHA7eeeaa51690a89f95d1504ae02aa5f28938cdeebca7514212aa0584324bba662。同Webreference25133056input/25026383body/親nonEOS mass24981892.629882812。同rank6136family presentations/12272relational labels/1022980valid/6283264padded/gold73725・foil73725位置/gold315047・foil315047bytes。positive CEに正解73725 hard教師を別計数しmain込み100073725、combined physical131948544/valid126688260。新corpus/追加input relative to ranking0。全3068main/Web/pair入力・mask digest・親massと全cursor一致、全rank/newhard台帳を再現監査。

train440.826677秒、science GPU523.499829+probe31.258545=新全554.758374秒<900。旧関連1734.837644秒を消さず累積2289.596018秒。40検証更新/main1307967/positivehard933/rank160choice labels81920paddedは科学学習へ加算しない。

ranking→anchor: BPB.988409457→0.989858640悪化、文法2=37→34/関連2=41→70/一貫性2=2→5/適切22→16/EOS41→40/自動反復21→28、Unicode-role-empty0（各80）。一貫性差+3/paired95%CI[-.0125,.0875]で有意改善の証明なし。強いstagedCE23に対し-18/CI[-.325,-.125]、relative/absolute/歴史Web1% BPB guard未達、不採用。意味59.375→67.1875%/JBLiMP75.227→76.435%/JCQA33.959→34.942%の改善を文章品質/完成Baseへ置換しない。

bridge両極正答86→79/128（語彙63→63/64・構造23→16/64）、retention80→80/128。同256全文472055bytes/122343bodytokens、日本語192-331-1119、全80greedy64を完了。全80を個別に読み78新観察/同id-prefix-raw-stop2件だけ旧notesを再利用し、raw SHA/rationale/TSVとreview/completionを保存。非blind Codex、独立人間なし。新しい人物/幻想/自然な別継続をgold不一致だけで落とさず、数値の誤りは文法とは別に判定した。

全256familyの既存BF16 raw2048requestsだけを実CPU0.876809秒/上限10、GPU0/新forward0で集計。bridge全gold平均tokenNLL1.909050→.697495・222/256 poles改善、foil4.096298→2.661693。一方、構造gold全body3.061216→1.374313でもfirst-gold3.174599→5.162815悪化。語彙first-gold.306681→.055691改善を隠さず、全体first1.740640→2.609253。retention全gold2.238642→1.257412・215/256改善でも全first3.495138→4.053743、構造first3.858534→5.374053悪化。teacher-forced後続の改善と開始位置/自然文の保持を分ける。唯一因果/全vocab top1成功の証明ではない。

可搬401text/20154183rawbytes、gzip3786879/SHAa064e30ab681583f2022773fd8a5dc5895903cdd5dd9f7eddc2831dad6a51f56を保存。モデルtensor/dataarraysはnativeのみ、workspace metadata/次proposalはarchive後の別記録。元10B UI618479/同boot/start16015140のlive identityとHTTP元CP410f975d…/10000007168/busy=falseを確認、failed candidateをUIへ置換しない。GPU科学job0。

この単一anchor比較は終了し、係数/温度/normalizer/order/LR/source/batch sweep、cap拡張、自動延長/有利CP探索を行わない。次はdecision_span_diagnostic_proposal.jsonの単一cached CPU診断（上限10秒/GPU0/newforward0）を実装・実行。強いstagedCE/relative ranking/anchorの3実終了model、同bridge128/retention128、全3072保存済scoresを用い、候補が初めて異なる位置まで入力が同一であることを確認してその位置の正解対foil確率と全body選好を比べる。prefix包含等の測れないcaseは除外を隠さず別記、EOS/padを勝手に補わない。保存済is_greedy全target argmaxの連言も集計し、完全gold body経路とEOS後の停止/自然文品質を区別する。全family/両context/3modelを記録し、後続teacher forcingに隠れた開始選択の誤りが実際に支持されるかから次の一つの有限Base学習条件を定義する。CPU FP32再推論/旧zero-context再診断/巨大source再scanなし。pilot品質合格時だけ独立学習seed/full dev/protected testへ進む。旧Phase0–3/数値7失敗/全品質条件/過去費用保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

正解続きの生成確率を高める単一100M比較を実CUDA検証後に開始（2026-10-06 JST）。前のrelative-only100M/全評価不採用を44b092cへ保存。Baseだけを品質・独立学習seed/full dev/protected test/採用まで続け、実完成時に通知して停止。Base未完了・未採用、Chat/Dialogue/SFT/量子化なし。

owned anchored_context_outcome loss/trainer/resident/runner/accountant/reviewer/durablePSを実装。元10.5B fullparent/Adam/scheduler/RNG/実LR.00001、main100M CEと4source順序、conditional WebKL8x1024、TRAIN pair8x256/全cursor/inputを維持。同paired logitsの正解bodyにだけ非EOS CE係数1を加え、ranking係数/温度1を保持。foil/prefix/pad/EOS3は新hard教師外、追加forward/新教材量0。正解73725位置が新hard教師、main込み100073725とrelational labels/parent probability mass/combined physical131948544を別計数する。

CPU4tests/1.678秒は実tiny学習済重みで全state4対2+2/3samplers/new ledger/singleAdamstep、loss masks/directEOS勾配0/低gold確率でも相対ranking改善する例とcausal/padding経路を確認。scope/実TRAIN会計改変拒否2testsも合格、PS構文成功。新builderの初回newline-fragment拒否とCPU prepareのproposal key誤読を新unfrozen sourceで修正後に凍結、実GPU失敗0、旧frozen files/基準/予算変更なし。

probe actual616014はcomplete・実identity不在。実CUDA4対2+2全58state/history/有限値checksと初期parent10checks成功。40検証更新/mainCE1307967/positivehard933/rank160labels81920paddedを科学へ加算しない。全32主/Web/pair入力・mask digest・親massが終了済rankingと一致、probeGPU31.258545秒。更新median0.140814317秒、3068更新train推定437.202909秒。同150秒非学習枠/30%/50秒余裕を保持しscience813.363782+probe=844.622327<900秒でscience凍結。旧関連1734.837644秒を消さず別記。

Windows durable worker33620、actual616427/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15962167をlive確認。主CE追加7847591教師/loss2.934326230548322有限で100M学習中。RUN reports/phase6/anchored-context-outcome-comparison-20261006、configs/phase6/anchored_context_outcome_comparison.json/launch.jsonにPID/log/checkpoint/source snapshotsを保存。actual不在・valid completed-update checkpointのときだけscripts/run_anchored_context_outcome_comparison.ps1 -Mode Train -Workerで再開、二重GPUなし。GPU中の元10B UIは停止しwrapper finallyで元CPへ復帰する。probe/sourceの可搬292text/3292371rawbytesとarchiveを保存、active科学log/model tensor/dataはportable外、launch metadataはarchive後の別記録。

次は同job終端→256全文472055bytes/122343bodytokens、日本語192-331-1119、全80greedy64と全80個別raw-bound内容、bridge/retention各128、絶対gold/foil NLLとmargin、全3068入力/新hard台帳の採否。mechanism対照は前ranking、品質対照は強い元stagedCE23+8/CI lower>0/EOS>=76/反復<=2と既存absolute/歴史WebBPB<=.981285952のまま。設定sweep/量だけの延長/有利CP探索/自動予算拡張なし。pilot品質合格時だけ独立学習seed/full dev/protected test/adoption。旧Phase0–3/数値7失敗/全品質条件/過去費用保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

train文脈比較100Mと全評価を完了・不採用（2026-10-06 JST）。実CUDA53checks/永続起動はdf3e2a3へ保存。Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続、実完成時に通知して停止。Base未完了・未採用。Chat/Dialogue/SFT/量子化なし。

actual610335/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15803746はcomplete・実ps不在。main100,000,000CE教師/maininput100,532,224/3068更新、CP323503 SHAc95d649b8d3a0c8ede55c2edec80ef8ed4a24bae8ce0ca9e8fe3ccf7434a832c。同reference25,133,056input/25,026,383body positions/parent非EOS mass24,981,892.629882812。rank6136family presentations/12272relational labels/1,022,980valid/6,283,264padded/gold73,725・foil73,725位置/gold315,047・foil315,047bytes、combined131,948,544physical/126,688,260validを別計数。rankはCE教師0/soft targets0、新corpus0。全3068主/参照input-mask-digest-sourceとmassがconditionalKLと一致、全rank入力/順序/digest/会計を再現監査、全4終端source cursors一致。

train441.077806秒、science GPU529.834262＋probe31.407991=新全561.242253秒<900。旧関連1173.595391秒を消さず累積1734.837644秒。検証40更新/CE1,307,967/reference327,680/body326,339/mass325,778.16796875/rank80family・160labels・81920paddedは科学学習へ加算しない。

conditionalKL→rank: BPB.983031489→0.988409457悪化、文法2=58→37/関連2=49→41/一貫性2=11→2/適切28→22/EOS44→41/自動反復20→21、Unicode-role-empty0（各80）。一貫性差-9/paired95%CI[-.1875,-.0375]、強いstaged CE23に対して-21/CI[-.3625,-.1625]。relative/absolute/歴史Web BPB guard失敗、不採用。意味57.292→59.375%/JBLiMP74.320→75.227%/JCQA33.959%同値でもBase完成とはしない。

bridge両極正答54→86/128、語彙42→63/64・構造12→23/64、同候補70→22、文脈反転方向98→102。retention33→80/128。全256全文472055bytes/122343bodytokens、日本語192-331-1119、全80greedy64と全80個別読解（77新観察/同id-prefix-raw-stop3件だけ旧notes再利用）を保存。nonblind Codexで独立人間なし。選択式の改善と生成品質の大幅悪化を両方保持する。

既存BF16 rawのみを用いる全256familyのgold/foil方向分析を実CPU0.940229秒/上限10、GPU0/新forward0で完了。bridge256polesの正解NLL悪化180、誤候補悪化208、margin改善190うち両候補とも悪化したのにmargin改善120。gold平均tokenNLL.283227→1.909050、foil.457043→4.096298。retention正解悪化210/foil悪化250、両方悪化＋margin改善153、gold.933116→2.238642/foil1.094956→5.052400。語彙bridge first-gold-tokenは.544424→.306681改善だが全goldbody.305072→.824021悪化、構造goldbody.260030→3.061216。相対選好の成功を正解そのものの生成確率/自然文品質の成功へ置換しない。これはteacher-forced/shared-generatorの算術診断で、zero-context/唯一の因果やtop1成功の証明ではない。CPU FP32との数値混合なし。

可搬380text/21,585,569rawbytes、gzip3,730,221/SHA6a557c3a3f9852afa8c20d6f0f094084dde74b4be1c2a97d410ef826ab40fa8eを保存。モデルtensors/dataarraysはnativeのみ。workspace metadataと次proposalはarchive後の別記録。元10B UI612068/同boot/start15857321のlive identity・HTTP親410f975d…/10,000,007,168/busy=falseを確認、failed pilotをUIへ置換しない。

次はanchored_context_outcome_proposal.jsonの単一positive likelihood anchor比較をowned実装。親fullstate/実LR.00001・main100M・WebconditionalKL・同pair8x256/入力/順序/全露出を保ち、同TRAIN正解bodyへconditional非EOS CE係数1だけ追加、ranking係数/温度1を保持する。既存gold73,725位置が新hard教師となりmain込み100,073,725教師（別監査）、新corpus/追加入力0、foilはhard教師にしない。EOS3/prefix/padはauxから除外しsharedparameter/MainCEのEOS変化は許容し実測する。まだ新prototype/CUDA/science0・新config未凍結。CPU masks/gradient/fullstate→actualCUDA4vs2+2と32combined timings→従来150秒/30%/50秒余裕＋全probe込み900秒なら単一100M→同全評価/全80/絶対gold NLLとmargin/全3068会計・元強い基準で採否。設定sweep/自動延長/有利CP探索なし。pilot合格後だけ独立学習seed/full dev/protected test、Base完成時通知して停止。旧Phase0–3/数値7失敗/全品質条件/過去費用保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

train文脈比較100Mの実CUDA検証完了・科学学習を永続開始（2026-10-06 JST）。前goal turnは有限CPU診断/全raw/3損失prototypeの実CPU再開をd4587a5へ保存したprogress。Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続し、実完成時に通知して停止。Base未完了・未採用、Chat/Dialogue/SFT/量子化なし。

owned runner/reviewer/accountant/durablePSを実装、既存凍結source/prototype/dataは不変。関連scope/実TRAIN入力台帳改変拒否のCPU2tests/1.01秒とPS構文成功（実XMLはcontext_outcome_ranking_comparison_tests.xml）。新コード生成のblank-line置換は初回に拒否されtest未copyの最初のpytestは0件で終了、own unfrozen同期を修正後2tests成功、実GPU失敗0・基準/予算変更なし。rank係数/温度1・2family/8x256/eager BF16 math、main32x1024/ref8x1024 compiled flashの同100M＋conditional WebKLを保つ。

probe actual609903/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15795098はcomplete・実ps不在。実CUDA連続4対2+2の全53state/history/有限値/LRと初期親10checks合格、rank sampler/state/counters/digestも一致。40検証更新/CE1,307,967/reference input327,680/body326,339/mass325778.16796875、rank80family presentations/160choice labels/13376valid/81920padded/gold933・foil933位置/gold4022・foil4022bytes、GPU31.407991秒を科学学習へ加えず重みを破棄。全32 main/ref入力が終了済controlと一致。

combined更新中央値0.140283270秒、3068更新のtrain推定435.487230秒（約7.3分）。従来150秒非学習枠＋30%＋50秒余裕を保持してscience見積811.133399＋probe31.407991=新全842.541390秒<900で科学configを凍結。旧関連全1173.595391秒を別保存し消さない。

durable Windows worker34292、actual WSL610335/同boot/start15803746をlive identity確認、main追加19,619,060CE教師/loss2.5711560393683612有限で科学100M学習中。configs/phase6/context_outcome_ranking_comparison.jsonとreports/phase6/context_outcome_ranking_launch.json、RUN context-outcome-ranking-comparison-20261006へjob/log/checkpoints/source snapshotsを保存。元10B UIはGPU中停止しwrapper finallyで復帰。actual不在・valid checkpointのときだけscripts/run_context_outcome_ranking_comparison.ps1 -Mode Train -Workerで再開、二重GPUなし。main100M/reference25,133,056inputに加わるrank6,283,264padded/12,272choice labelsは別会計、combined131,948,544input、valid/gold/foil/bytesは全3068実値を監査。新corpus0・同supervision量とは言わない。

次はこのowned job終端→同256全文472055bytes/122343tokens、日本語192-331-1119、全80greedy64と全80個別内容、bridge/retention各128family、全3068主/参照input-digest-mask-sourceとrank入力・全露出台帳の採否。conditionalKLは機序対照、採用は強い元staged CE23+8/CI lower>0/EOS>=76/反復<=2と既存absolute/歴史Web BPB<=.981285952を維持、弱いcontrolへ置換しない。pilot合格後だけ独立学習seed/full dev/protected test。設定sweep/有利CP探索/予算追加/自動延長なし。旧Phase0–3/数値7失敗/過去費用保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

文脈と候補priorの有限CPU診断を完了・train文脈比較損失を準備（2026-10-06 JST）。Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続し、実完成時に通知して停止する。Baseは未完了・未採用。Chat/Dialogue/SFT/量子化は開始しない。

context_prior_diagnostic_completion.jsonに実4checkpoint/2suite/全256familyのoriginal4096と同じtargetを保つBOS-only4096、計8192requestsをCPU FP32/math/eval/no-gradで保存。実16.773451秒/上限180、GPU0、全4modelの重み/RNG/grad/eval/device/CUDA未初期化checks合格、actual603932は終了・ps不在。元GPU BF16とCPU FP32を混ぜて引かず、採用値をCPU補正で置換しない。conditionalKL→gold replayのbridgeは両極正答53→40/128、喪失13/獲得0。算術切り分けで文脈側変化だけで喪失10、priorだけ0、どちら単独でも2、両方必要1。retention32→22、喪失13/獲得3、文脈だけ11/priorだけ1/どちらでも1。単純prior offsetだけが主因という仮説は支持せず、文脈分離の弱まりを支持する局所診断。BOS-onlyの位置/文法差、shared generator/形重複、算術交換が実現可能なモデル変更/因果証明ではない限界を保持する。全family/category/3normalizers/raw scoreを保存。

診断可搬547text/17,565,308rawbytes、gzip1,972,432/ SHA3c1091bb513b7093c45b08b79f3e6d9aaf5ae97217ae2d631cd456419cfce27d。Windows raw/archive SHA確認。CPU診断2tests合格。launcherはWindows側にありnative側のcopyはパス不在で中止したが、実診断・archiveは正常完了、再診断/予算追加なし。

context_outcome_ranking_preparation.jsonとproposal.jsonを保存。新corpus0、既存accepted TRAIN1024family/2048positive recordsの反対文脈/共有2outcomesから4096candidate rowsを実CPU.215551秒/60で用意。joint encoding全4096一致、max74tokens、valid170700/body24604、prefix/pad/EOSはaux教師外。固定2family/update、8x256、conditional nonEOS mean-body logPのsoftplus(foil-gold)、係数/温度1。従来main100MCEと同Web参照conditionalKLを保ち、rankは別のrelational supervisionでありCE教師/soft target数へ足さない。計画上6136family presentations/12272choice labels/6283264padded positions、combined131948544を別会計し、valid/gold/foil/bytesは実samplerで測る。

owned context_outcome_ranking_trainer.py/resident adaptorはmain CE→Web KL→短いpad付きrankの3backward後に1回clip/Adam/scheduler。main/ref compiled flashは維持しrankはeager BF16 math案。実CPU loss/直接EOS勾配ゼロ/文脈反転・global候補bias、local shuffle/globalRNG不変、全state連続4対2+2と3samplers/全ledger/digest一致、main/ref control入力一致に3tests合格（rank2/fulltrainer1）。これはfixtureで実10M CUDA/品質の証明ではない。科学GPU0・科学追加教師0・CUDA gate未実施・科学config未凍結。

次はowned runner/reviewer/durable launcherとactual CUDA連続4対2+2＋32combined timings→従来150秒非学習枠/30%/50秒余裕＋全probe costs込み900秒内なら単一100M比較だけ凍結/実施→同256全文/日本語/全80内容/bridge-retention/全3068入力と新rank台帳の採否。control conditionalKLは機序対照、採用は強い元staged CE23+8/CI lower>0/EOS>=76/反復<=2、既存absoluteと歴史Web BPB<=.981285952を維持する。失敗済gold replayのvariant・設定sweep・量だけの延長・有利CP探索なし。品質pilot合格後だけ独立学習seed/full dev/protected test。元10B UI599823/同boot/start15623625とHTTP親410f975d…/10,000,007,168/busy=falseを確認、CPU作業で停止しない。WSL uv3.12.7/local commitのみ/pushなし。旧Phase0–3/数値7失敗・品質基準・過去費用は保持。以下は過去の履歴。

正解語によるWeb本文replayの100M比較を全評価まで完了・不採用（2026-10-06 JST）。実CUDA検証/永続起動は91369daへ保存。Baseだけを品質・独立学習seed/full dev/protected test/採用まで進め、実完成時に通知して停止する。Baseは未完了・未採用、Chat/Dialogue/SFT/量子化なし。

owned WSL598415/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15588101はcomplete・実ps不在。通常CE100,000,000教師/maininput100,532,224/3068更新、参照input25,133,056/gold body教師25,026,383/main込み125,026,383 hard positions、combined student input125,665,280。親nonEOS probability mass24,981,892.629882812は整数教師数と別保存。新教材量0・既存train重複replay。親fullstate/Adam/scheduler/RNG/実LR.00001と4primary source quotas/順序を保持。全4終端source cursor/counterと全3068主/参照input-digest-mask-source counters、全32/3068の親probability massが終了済conditionalKLと完全一致。教師はsoft distributionから実gold wordへ変わり、同露出でもhard supervision情報量は同じではない。

train280.87秒、science GPU349.432259＋CUDA検証28.810827＝新研究378.243087秒<新900秒。旧関連KL研究795.352305秒を消さず、累積1173.595391秒を別記。40検証更新/CE1,307,967/aux gold326,339/input327,680/mass325,778.16796875を科学学習へ加算しない。CPU math初回丸め差とrunner初回self-importの失敗XMLを保管、実GPUsource凍結前に修正、科学失敗の隠蔽や基準/余裕変更なし。

conditionalKL→gold replay: BPB.983031489→.985528435悪化、文法2=58→45/関連2=49→56/一貫性2=11→17/適切28→34/EOS44→53/自動反復20→15、Unicode-role-empty両方0（各80）。意味57.292→56.771%/JBLiMP74.320→77.039%/JCQA33.959→33.780%。一貫性差+6/paired95%CI[0,.15]、gain8/CI lower>0未達。強い元staged CE23/EOS76/反復2に対して一貫性差-6/CI[-.2,.05]で有意な悪化の独立証明ではないが、relative EOS/反復・absolute文法56/一貫性27・歴史Web1% BPB(.981285952)を満たさず不採用。Base完成とはしない。

全256全文472055bytes/122343bodytokens、日本語192-331-1119、全80greedy64、bridge/retention各128family/512requests完了。80件全てを個別に読み、59新観察/同id-prefix-raw-stop21件だけ旧notesを再利用。原文/notes SHAと観察TSV、all32/3068入力・mass audit、review/completionを保存。独立人間blindなし。CPU既存全文paired集計でconditionalKL比は本文203悪化53改善/goldEOS160改善96悪化、元staged比は本文256改善/goldEOS201悪化55改善。末尾lossと生成一貫性を同一視しない。

sumLLでbridge両極正答54→40/128（語彙42→33/64、構造12→7/64）、同じ候補を両文脈で選ぶfamily70→77/128、文脈反転方向のmargin shiftは98→98/128。旧retention両極正答33→20/128。停止の改善と文脈判断の悪化は両方記録し、対象語のprior変化と文脈応答の弱さをまだ区別できない。これだけでcontextを全く無視する/教師コピーだけが唯一原因と断定しない。

可搬372text/15,569,125rawbytes、gzip2,739,302/SHAbfed0f3ce84e8f3d41edd01d4db92ec3facdb8afaca3d95623f9ba47b7780a27。全Windows raw/archive SHA一致、モデルtensorsと150MBcache/31GB原文はnativeのみ。科学GPU job0、元10B UI599823/同boot/start15623625の実identityとHTTP親410f975d…/10,000,007,168/busy=falseを確認。workspace stateと次のproposalはarchive後の別metadataとして保存。

この単一gold-replay比較は終了し、係数/温度/normalizer/order/LR/source-weight/batchのvariant、自動延長、有利なCP探索、追加data量だけの学習へ進まない。次はcontext_prior_diagnostic_proposal.jsonの有限CPU診断（GPU0/最大180秒/8threads）だけ。実歴史親・staged CE・conditionalKL・gold replayの4checkpointに対し、既存bridge128/retention128の全encoded requestsをoriginal prefixとBOS2-onlyで測る。両条件を同じCPU FP32/math/eval/no-gradで再計算し、元GPU BF16とCPU FP32の数値を混ぜて引かない。target_ids/span/byte分母は同一のまま、family単位の元margin・候補prior margin・差による文脈寄与をsum/tokenmean/bytemean別に報告する。BOS-onlyの位置/文法差やshared generator/一部train形重複の限界を明記する。PMI補正を採用スコア/生成/品質基準の変更に使わない。

次の具体作業はown read-only CPU commandとencoded target保持の確認→全4model/2suite/全256family/両contextの有限スコアとweights/RNG/eval/grad不変・elapsed台帳→原文family/category表。候補priorのoffsetと文脈応答の退行、または両方のどれが実際に支持されるかを調べ、結果から次の1つの有限Base比較/修正を定義する。診断のtimeoutでcapを拡張しない。品質pilot合格時だけ独立学習seed/full dev/protected testへ進む。既存relative/absolute/歴史Web guard、旧Phase0–3/数値7失敗を維持。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。
正解語でWeb本文を再学習する100M比較の実CUDA検証を完了・学習を開始（2026-10-06 JST）。前goal turnは終了済EOS成分比較と全評価の不採用をf684137へ保存したprogress。最新ユーザー境界を保ち、Baseだけを品質・独立学習seed/full dev/protected test/採用まで進め、実完成時に通知して停止する。Base未完了・未採用、Chat/Dialogue/SFT/量子化なし。

hard_body_web_replay.pyとown trainer/resident adapterを実装。元10.5B親fullstate/Adam/scheduler/RNG/実LR.00001、main100M CE/Web75M-story5M-ordinary10M-conditional10Mの順序、同参照8x1024/親non-EOS mass重み/学生EOS3を除く4095語彙を保ち、soft distributionから実gold body label>=8のCEへ教師を変更。新hard target数とfloat probability massを別にhistory/checkpointへ保存する。新教材量0・既存train重複入力であり、同露出でもsoft対照とhard supervision情報量は同じではない。

実CPU gold CE/mask/直接EOS勾配ゼロ/parent detach/全state連続4対2+2/4入力一致の3testsは1.74秒、scope/会計2testsは.89秒で合格。CPU初回は一般logit並べ替えのFP32丸め差9.5367e-7をbitwise同値と誤要求して失敗。XMLを保持し、重みがFP32で厳密同値となる入力で親body distribution変更に対する厳密loss一致を確認、非退化重みテストも保持。実損失/科学基準は変更なし。runner初回importが生成時の名称置換で自己参照となったcollection errorもXML保存、実GPU凍結前にown import/builderのみ修正。旧source不変。

probe actual598033/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15582082はcomplete・実ps不在。実CUDA/BF164対2+2の全42state/history/finite/no-reheat checksと初期親10checksが合格、new hard target ledgerも完全再開一致。40検証更新/CE1,307,967/参照input327,680/gold body326,339/親nonEOS mass325,778.16796875、GPU28.810827秒は科学学習と別。全32主・参照input/digest/counterがcached conditionalKLと一致。1更新中央値.088744431秒、3068更新の学習推定277.318637秒。従来150秒非学習枠＋30%＋50秒の余裕を維持してscience605.514229＋検証28.810827＝634.325056秒<新900秒で凍結。旧関連2つのKL研究795.352305秒は別報告し消さない。

durable Windows worker32992、actual WSL598415/同boot/start15588101で科学main100M＋参照25,133,056inputを学習中。configs/phase6/hard_body_web_replay_comparison.jsonとreports/phase6/hard_body_web_replay_comparison_launch.jsonに実gate/shape/測定予算/identityを保存。job/log/checkpoint/source snapshotsはreports/phase6/hard-body-web-replay-comparison-20261006。実process不在を確認した場合だけscripts/run_hard_body_web_replay_comparison.ps1 -Mode Train -Workerで正確に再開。GPU中UIを止め、wrapper finallyで元10Bを戻す。想定aux hard body25,026,383/main込み125,026,383を新corpusやprobability massへ混ぜない。

次はowned job終端→同256全文byte/日本語192-331-1119/全80greedy/bridge128/retention128・全80個別読解と全3068入力一致・gold count/mass会計の採否。教師の種類の対照は終了済conditionalKL11/EOS44/反復20を再利用するが、採用は元staged CE23+8/CI lower>0/EOS>=76/反復<=2とabsolute/歴史Web1% BPB guardを維持する。弱い比較対照へ差し替えない。合格時だけ独立学習seed/full dev/protected test。係数/温度/normalizer/order/LR/source-weight/batch sweep・自動延長・有利なCP探索なし。旧Phase0–3/数値7失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。
EOS質量を切り離す100M比較を全評価まで完了・不採用（2026-10-06 JST）。実CUDA/永続起動はda4e7e4へ保存。Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続し、実完了時に通知して停止する。Baseは未完了・未採用。Chat/Dialogue/SFT/量子化なし。

owned WSL593649/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15443335はcomplete・実ps不在。通常CE100,000,000教師/maininput100,532,224/3068更新、CPupdate323503 SHAa27547b6223c3708d6dbf8c9f211631b44fb9518771ed7c08a89ae40506e1213。追加soft referenceinput25,133,056/body positions25,026,383、parent非EOS probability mass24,981,892.629882812/EOS省略mass44,490.3701171875を別保存。combined student input125,665,280、新教材量0。全4primary終端cursor/教師/EOS/input/bytes/focus countsと全3068主・参照input/digest/counterが終了済full KLと一致、Web73421blocks/参照24544blocks。目的損失が変わることとdata窓一致を区別する。

train287.574895秒、science GPU364.789503＋実CUDA検証29.086883＝新研究全393.876386秒<900。旧関連full KL全401.475919秒を消さず、2つのKL研究累積795.352305秒を別記。新検証40更新/1,307,967 CE教師/referenceinput327,680/body326,339/retained mass325,778.16796875は科学学習と別。旧失敗/拒否/CPU初回丸め差のXMLを保持し、予算・余裕・品質基準を緩和しない。

full KL→EOS成分除去: BPB.982266745→.983031489（一部悪化）、文法2=58→58/関連2=47→49/一貫性2=9→11/適切25→28/EOS40→44/自動反復22→20、Unicode/role/empty両方0（各80）。意味57.292%/JBLiMP74.320%は同値、JCQA34.004→33.959%。一貫性差+2/paired95%CI[0,.0625]で明確な全般改善の証明ではない。機序差と別の強い元staged CE23/EOS76/反復2に対しては一貫性差-12/CI[-.2625,-.0375]、relative coherence+8/EOS非悪化/反復非悪化、absolute coherence27/反復18、歴史Web1% BPB guard(.981285952)に未達。不採用。適切28だけでBase完成とはしない。

同256全文472055bytes/122343bodytokens・全日本語192/331/1119・全80greedy64・bridge128/retention128完了。全80を個別に読み28新観察/同id-prefix-raw-stop52件だけ旧notes再利用、独立人間blindなし。既存paired CPU集計でfull KL比のgold EOS NLLは256/256改善だが、本文NLLは226悪化/30改善。元staged比は本文256改善/gold EOS203悪化53改善。正しい末尾のteacher-forcing改善を実生成の一貫性改善と同一視しない。local bridge両極正答54→54/128（構造11→12/64、語彙43→42/64）、旧retention32→33/128。強いquality baselineとmechanism comparatorを差し替えない。

eos_decoupled_web_kl_comparison_completion.json/review/all80 raw-bound notes/observationsを保存。可搬341text/15,197,592bytes、gzip2,667,048/SHA6da9d2551c7ffff5b2a2a29d36d93e5a4e12f4fab1ac985f40dc56f8498b01ca、全Windows raw/archive SHA一致。モデルtensors/150MBcache/原文arraysはnativeのみ。元10B UI595028/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15480373の実identityとHTTP親410f975d…/10,000,007,168/busy=falseを確認、科学GPU job0。

EOS質量だけを調整する路線はこの2つの有限比較で区切り、係数/温度/normalizerの別variantや自動長期延長へ進まない。次はhard_body_web_replay_comparison_proposal.jsonで定義した新しい1条件だけ。元train Webの同じ参照窓で親soft distributionの保持から実gold wordのCEへ教師の種類を変える。学生の非EOS語彙4095と親(1-pEOS)重み・body mask・親fullstate/実LR.00001/main100M/4source quota/order・参照8×1024/追加露出を保持し、対象の語を直接学習する仮説。追加hard target positionsは同窓なら25,026,383、mainと合計125,026,383 hard positionsとなりsoft-target対照との教師情報量は同一でない。probability massと位置数・新教材量を混同しない、新教材量0。既存data量の不足やteacherコピーだけが唯一原因と断定しない。限定local implementation/configのhard-body-replay検索は一致0で、未登録研究/外部研究の網羅証明ではない。

次の具体作業はown gold-body helper/trainerのmask/teacher-detach/直接EOS勾配/実gold targetと新hard位置・weight-mass counters/全state再開のCPU検証。own runner/reviewer/durablePSへ接続し、実process確認→実CUDA4対2+2/32 combined timing/saveの余裕付き測定が新900秒内の場合だけ本学習を凍結・永続起動する。目的対照は終了済conditionalKL（11/44/20）を再利用するが、採用screenは元staged CE23+8/CI/EOS>=76/反復<=2、absolute、歴史Web1%を維持する。全256byte/日本語/80/bridge/retention・全80読解と全3068入力一致で採否。係数/温度/order/LR/source-weight/batch sweep・有利なCP探索・自動延長なし。品質pilot合格時だけ独立学習seed/full dev/protected test。旧Phase0–3/数値7失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

EOS質量を切り離す比較の実CUDA検証を終え、100M学習を開始（2026-10-06 JST）。前goal turn e94d866は実CPU9.29秒の分解診断と新成分のCPU実装/全state再開まで完了したprogress。Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続し、実完了時に通知して停止する。Base未完了・未採用、Chat/Dialogue/SFT/量子化なし。

own runner/reviewer/durablePS/会計を実装。新追加のparent非EOS probability-massをhistory/checkpoint/KL state/再開gate/最終reviewで扱う。終了済fullKLは機序対照として再評価せず、元staged CE23/EOS76/反復2の強い品質screenを別に維持。own scope/accounting CPU2tests/1.00秒で品質対照の差し替えとmass隠蔽を拒否、PS構文成功。builder初回は既存sourceの同一行にある変数初期化を行頭と誤認して生成前に拒否、生成fragmentだけ修正。GPU/科学学習前の処理で旧source不変、品質/検査を緩和しない。

新probe actual593289/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15436720は終了・実ps不在。実CUDA連続4対2+2の全41 state/history/finite/no-reheat checksと初期親model/Adam/scheduler/RNG/cursor/teacher/LR保持10checksが合格。新probability massも完全再開一致。40検証更新/1,307,967 CE教師/referenceinput327,680/soft body326,339/retained parent非EOS mass325,778.16796875を科学学習へ足さない。GPU29.086883秒。全32 timingのmain/ref input digest・教師/EOS/input/byte/focus countsが旧fullKL probeと完全一致。損失/勾配は新目的のため旧と一致を要求しない。

1更新実測.090427864秒、3068更新の学習推定282.595547秒。旧非学習GPU証拠150秒枠＋30%＋50秒を保ち、science余裕付き612.374211＋新検証29.086883＝641.461094秒<新900秒で凍結。旧関連研究401.475919秒は既存別費用として保持・報告し、旧失敗capや余裕を変更しない。configs/phase6/eos_decoupled_web_kl_comparison.json SHA1d31739438ffcd2e2ef93c725e16b0ed23d0fec6417ece5f2268766e88881017。

durable Windows worker30372、actual WSL593649/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15443335で通常CE100M＋別参照25,133,056inputの学習中。reports/phase6/eos-decoupled-web-kl-comparison-20261006/job.jsonに累積費用/heartbeat/PID/再開命令を保存。再開はscripts/run_eos_decoupled_web_kl_comparison.ps1 -Mode Train -Worker（実process不在確認後）。科学GPU中UIを停止、wrapper finallyで元10Bを戻す。eos_decoupled_web_kl_comparison_launch.jsonに実gate/shape/費用/identity/mass根拠。新教材量0、親10.5B fullstate/実LR.00001/4sources quota/順序/同主・参照窓/temperature1/coefficient1を維持し、EOS-mass項だけを外す。確率質量は位置数・CE教師・新教材量と別。

次はowned job終端→同256byte/全日本語192/331/1119/全80greedy64/bridge128/retention128・全80個別読解と新mass/全3068主・参照入力・counter一致を確認して採否。機序差fullKL対新条件と品質screen元staged CE対新条件を区別し、元relative coherence+8/CI/EOS/反復/BPB、absolute、歴史Web1%を維持。劣ったfullKL基準へ差し替えない。合格時だけ独立学習seed/full dev/protected test。失敗時の係数/温度/order/LR/source/batch sweep・自動長期延長/有利なCP探索なし。旧Phase0–3/数値7失敗を保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

EOS確率質量の実CPU診断を完了し、成分を切り離す1条件を準備（2026-10-06 JST）。前goal turnは実100M/full評価/全80読解/不採用までecd1594へ保存したprogress。Baseだけを品質/独立学習seed/full dev/protected test/採用まで継続し、実完了時に通知して停止する。Base未完了・未採用、Chat/Dialogue/SFT/量子化なし。

凍結web_kl_followup_diagnostic_proposal.jsonの同train cursor順first16 resident windowsで親/対照staged CE/終端full KLをCPU FP32でread-only評価し、float64確率でKLを分解した。実9.290633秒（180秒内）、16,384input/16,320body/64ignored、GPU0/optimizer0/科学学習0。全モデル/同input-target digest/元manifest/cache SHA/親cursor順を保持し、語彙のEOS3も確率正規化に含まれる損失をBernoulli EOS確率質量項＋(1-parentEOS)×非EOS条件付き分布項へ正確に分けた。平均分解誤差5.55e-17/3.47e-18、全finite。web_kl_EOS_component_diagnostic.jsonとjob/result保存。数学identity・body mask・EOS gradientと成分分離のCPU2tests/1.34秒成功。

staged CEの本文位置EOS平均.0108181に対し親.00181360、KLのEOS logit勾配q-pの平均+.00900447。正7386/負8934/全16320なので一様な抑制ではなく、一部位置の大きな確率差が平均を押し上げる。full KL平均.503142のうちEOS質量項.0136183（約2.707%）、非EOS項.489524。終端full KLでは学生EOS平均.00163912、全KL.0301574/EOS項.000216077/非EOS項.0299413、勾配平均-.000174473（正13377/負2943）。従ってEOS制約の独立成分は存在するが、この小train窓/CPU精度だけで生成悪化の唯一原因やEOS-only説は証明しない。

eos_decoupled_web_kl_comparison_proposal.jsonは新しい1条件だけを定義。full KLからEOS質量のBernoulli項だけを外し、親の非EOS質量で重み付けした条件付き非EOS KLを残す。係数1/温度1/親10.5B fullstate/Adam/scheduler/RNG/実LR.00001、100M CE/各source quotaと順序、参照8×1024と元train重複入力/新教材量0を維持。parent(1-pEOS)のsoft probability massは位置数や通常CE教師と別に保存/再開/集計する。学生EOS logitの直接勾配はゼロでも、共有重み経由の変化や品質改善を保証しない。

機序の比較には終了済みfull KL100Mを再評価せず使うが、採用screenは強い元staged CE基準coherence23+8/CI lower>0/EOS>=76/反復<=2を維持し、absoluteと歴史Web1% BPB guardも維持する。劣ったfull KL9/40/22へ品質対照を差し替えて通しやすくしない。新しい成分比較は実CUDAと32timingから900秒内の学習/全評価推定を凍結して初めて実行する。旧関連研究全401.475919秒を別の既存費用として報告し、旧失敗runの上限や余裕を緩めない。係数/温度/order/source/LR/batch sweep・自動長期延長なし。

eos_decoupled_web_kl_preservation.py/own trainer/own resident adapterを準備。親teacher detach、body target mask、EOSだけ変更しても同loss、非EOS KLへの一致と直接EOS勾配ゼロを検証。小CPU実fixture連続4対2+2の重み/Adam/scheduler/RNG/主cursor/参照cursor/全state/新probability-mass/historyが完全一致、main96/reference64 input分離/teacher不変（全3tests/1.65秒）。初回はFP32 normalizer差の引き算により同logitsのKL=-1.8694e-8となり旧exact-zero検査に失敗、XMLを保持。親条件付きlogsoftmaxを直接計算する実装へ修正し数学成分を保ちexact-zero検査を緩和しない。CPU fixtureは実10M CUDA/学習性能/品質の証明ではなく新GPU0。

可搬18text/74,852bytes、gzip20,167/SHA90f3c9e93c93cd721346643e29dc9a5d9ca8857e3ce6cd4eafe8f67780b30733と全Windows raw/archive SHA一致。モデルtensors/原文arrays/cacheの複製なし。元10B UI588904の実ps稼働を確認、旧科学586602はcomplete、重複GPU jobなし。

次は新条件own runner/reviewer/durablePSを実装して両cached controlsに結び付け、追加probability-massのhistory/checkpoint/review会計と全3068 primary/ref input/digest/counter一致を扱う。実process確認→実CUDA continuous4 vs2+2（新mass・KL state/teacher/全sampler）＋32 combined timing/saveを測り、元150秒非学習枠/30%/50秒の余裕付き推定が新900秒内の場合のみ通常CE100M＋別参照学習を凍結・永続起動する。全256byte/日本語192/331/1119/全80/bridge128/retention128/全80個別読解と元品質gateで採否。合格時だけ独立学習seed/full dev/protected testへ。旧Phase0–3/数値7失敗/失敗費用を保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

親Web保持KLの100M比較を全評価まで完了・不採用（2026-10-06 JST）。前準備/実CUDA一致/高速化/起動は3c6a5ccへlocal commit。最新ユーザー境界はBaseのみを品質/独立学習seed/full dev/protected test/採用まで継続し、実完了時に通知して停止すること。Baseは未完了・未採用。Chat/Dialogue/SFT/量子化なし。

owned WSL586602/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15318244はcomplete・実ps不在。普通CE100,000,000教師/maininput100,532,224/3068更新を学習。追加参照はinput25,133,056/soft body positions25,026,383、無視特殊位置106,673、combined student input125,665,280で別会計。終端CPupdate323503 SHA646683b704f9c8fb25dbfdeebef0d7eb29776e45d11c15aea272d30efcfc9afc。全4primary source終端cursor・教師/EOS/input/byte/focus countsは凍結staged CE対照と一致、Web73421blocks、追加参照cursor24544blocksを確認。新教材量0、追加Web露出もあるので純objective単独/同総supervision比較ではない。

学習255.144406秒、science GPU333.195595＋全検証68.280325＝全401.475919秒<900。初回CUDA失敗8.727056/v2成功30.861475/v3成功28.691794の全費用を含み、v2の1020.878777秒推定拒否も保持。既知検証2,615,934 CE teachers/referenceinput655,360/soft positions652,678は科学学習へ足さない。初回失敗の実行済optimizer更新数は不明のまま保持。RAMに同train Webの150.5MBを載せて1更新.182958→.080785秒（2.264747倍）、実32更新のloss/gradient/IDs/reference/4source countersは旧v2と完全一致。形状/予算/品質基準/教師/親/実LRは緩和なし。

対照staged CE→親Web KL追加: BPB1.133612866→.982266745（13.3508%改善）、文法2=65→58/関連2=39→47/一貫性2=23→9/適切26→25/EOS76→40/自動反復2→22、Unicode/role/empty両方0（各80）。意味56.250→57.292%、JBLiMP78.248→74.320%、JCQA26.542→34.004%。一貫性差-14/paired95%CI[-.2875,-.0625]は固定devのnonblind判断。relative coherence+8/EOS非悪化/反復非悪化、absolute coherence27/適切27/反復18、歴史Web1% BPB guard(.981285952)に未達で不採用。本文だけ/停止だけの改善をBase完成とは扱わない。

同256全文472055bytes/122343bodytokens、全日本語192/331/1119、全80greedy64、bridge128/retention128を完了。全80を個別に読み77新観察/同id-prefix-raw-stop3件のみ過去note再利用、独立人間blindではない。既存paired CPU計算では本文NLL256/256で改善（悪化0）、gold EOS NLL223/256で悪化（改善33）。gold EOSは正しい末尾のteacher forcingであり生成適切停止の保証ではない。local bridge両条件正答59→54/128、構造8→11/64、語彙51→43/64、旧retention36→32/128。局所probeを自然文品質の代わりにしない。

web_kl_comparison_completion.json/web_kl_comparison_v3_review.json、全raw-bound80notes/observationsを保存。可搬546text/16,007,899bytes、gzip2,999,646/SHAA019F5DA9D9ECF9B032A90F7E8F6BDD89CA153CE26F30A42CF72E5640E6D6748をWindowsへコピーして全SHA一致。モデルtensors/150MB cache/原文arraysはnativeのみ。元10B UI588904/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15352115の実identityとHTTP親410f975d…/10,000,007,168/busy=falseを確認、科学GPU job0。

次はweb_kl_followup_diagnostic_proposal.jsonの有限CPU180秒/GPU0診断。既存residentの親train cursor順first16blocksだけで、親/対照stagedCE/終端KLの同body位置をread-only FP32評価し、全vocabulary KLをEOS確率質量のBernoulli項と非EOS条件付き分布項へ分解する。qEOS-pEOSの勾配符号と規模・分解恒等式/finite/SHA/countを記録し、本文保持と停止退行が結びつく機序を限定的に調べる。小train窓/CPU精度は唯一原因・CUDA学習・一般生成改善を証明しない。新学習なし、全dataset再parse/生成再採点/別samples/係数/温度/order/LR/source sweepなし。完了条件は固定3models/16windowsを1pass内180秒、平均KL分解差1e-9内とfinite/counter/hashの記録。根拠があれば次の有限objective-component比較を最大1条件だけ別計画し、なければKL調整を続けない。自動長期延長/有利なCP探索なし。品質pilot合格前の独立seed/full dev/protected testなし。旧Phase0–3/数値7失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

親Web保持KLの実CUDA検証を完了し、読み込み高速化後の100M比較を開始（2026-10-06 JST）。最新指示に従いBaseだけを学習・評価・改善し、品質/独立学習seed/full dev/protected test/採用の実完了時に通知して停止する。Base未完了・未採用。Chat/Dialogue/SFT/量子化なし。

同100M ordinary CEのstaged条件にfrozen親Web本文KLを加える1条件。参照は元train Webとの重複で新教材量0、main CE100Mとreferenceinput25,133,056を別計数する。係数1/温度1/実LR.00001/4source順序・教師・fullstate保持。旧staged CE100M評価は再利用し、追加supervisionも変わるため純objective単独/同総学習量の比較とはしない。

初回実CUDAはgrad-buffer/CUDAGraphの上書きで8.727056秒失敗。own v2でstable grad buffersを確保し、実CUDA連続4対2+2の全40checks/40検証更新に成功（30.861475秒、1,307,967 CE teachers/referenceinput327,680/soft positions326,339）。その1更新0.182958秒から全予算1020.878777秒と推定され900秒上限に未達、本学習は開始せず拒否。両attempt・source/config/log・失敗費用を保持。初回の実行済optimizer更新数は終端CP不在のため不明、0と扱わない。

空きRAM約60GBに対し、この比較で使う実親cursorから73421 Web blocksだけを150,513,050bytesへ連続化（CPU処理6.565475秒/GPU0）。元BlockSamplerを保ちuint16 context+1の同train IDsをRAMから供給、通常/参照cursorを別々に維持。CPU cache test1件1.62秒、v2 trainer/accounting3件2.88秒、v3 scope/accounting2件1.10秒成功。初回toy fixture不備XMLも保持。元31GB全体hash/13GB index再parseなし。

v3実CUDA全40resume checks・10initial preservation checks成功、32更新すべてで凍結v2とloss/CE/KL/gradient/LR/token/reference digest/counterが完全一致。1更新0.080785秒、v2比2.264747倍。v3検証28.691794秒、検証GPU累積68.280325秒。両成功probeの既知検証計2,615,934 CE teachers/referenceinput655,360/soft positions652,678を本学習から分離する。科学学習の余裕付き推定574.276327秒＋全検証＝642.556652秒<元900秒。150秒非学習枠/30%余裕/50秒を維持し、品質/予算/教師を緩和しない。

configs/phase6/web_kl_comparison_v3.json SHA60fcb3e6236f66bcdea397c09cc0f927212a1e3e3dbe94e23c6ff2a7837db0a9を凍結。durable Windows worker26376、actual WSL586602/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15318244で本学習中。reports/phase6/web-kl-comparison-v3-20261006/job.jsonにheartbeat/費用/再開命令を保存。再開はscripts/run_web_kl_comparison_v3.ps1 -Mode Train -Worker（実process不在確認後）。UIは実GPU中停止しwrapper finallyで元10Bへ戻す。web_kl_comparison_launch.jsonに実speed・全budget・identityの根拠。

次はこのowned jobの100M CE＋別参照学習を終え、同256byte/全日本語/全80/bridge/retention・全80個別読解・4primary stream終端一致/KL別会計を評価。relative coherence23から+8/CI/BPB/EOS76非悪化/反復2非悪化、absolute、歴史Web1% BPB guardを維持。品質pilot合格時だけ独立学習seed/full dev/protected testへ進む。失敗時の係数/温度/order/source/LR sweep・自動長期延長・有利なcheckpoint探索なし。WSL uv3.12.7、旧Phase0–3/数値7失敗を保持、local commitのみ/pushなし。以下は過去の履歴。

学習順序の本文/EOS退行を実CPUで分離し、親予測を保持する学習器を準備（2026-10-06 JST）: 前turn4b369bcは同100Mの全評価・全80読解・不採用まで完了したprogress。Baseだけを品質/独立学習seed/full dev/protected test/採用まで継続し完了通知して停止する。Chat/Dialogue/SFT/量子化なし。Baseは未完了・未採用。

固定proposalの既存paired256をCPU処理本体0.018418秒/GPU0で整理（uv起動/importはこの値に含めない、実コマンドも30秒内）。全472055bytes/122343bodytokensを再現し、本文NLLは256/256で悪化（改善0）、goldEOS NLLは216/256で改善/40で悪化。BPB .974820→1.133613、goldEOS平均NLL2.287282→1.581696、EOSの文別確率算術平均.218735→.469190。文長で決めた64文ずつの4quartilesも全64本文が悪化し、短文だけ/少数外れ値の現象ではない。goldEOSは正しい文末でのteacher forcingであり、生成途中の適切停止の保証ではない。全80既存notesと日本語差を再利用し新採点/tensor・data再parseなし。source recency/forgettingは仮説で、唯一原因や容量上限は断定しない。source_order_followup_diagnostic.jsonに全paired table/数値を保存、関連CPU1test/1.36秒成功。

先行研究Li/Hoiem Learning without Forgetting（https://arxiv.org/abs/1606.09282）とSunほか Distill and Replay for Continual Language Learning（https://aclanthology.org/2020.coling-main.318/）をprimary paper pageで確認。旧出力の蒸留とreplayという一般原理を参考にし、vision/continual NLU論文を10M日本語自由生成での効果の証明とはしない。登録phase6 top-level80configsには該当親Web KL条件なし（限定scanで未登録研究の網羅証明ではない）。web_kl_comparison_proposal.jsonで新しい有限1条件だけを定義。

歴史10.5B fullstate/Adam/scheduler/RNG/実LR.00001・同Web75/story5/ordinary10/conditional10M・同順序を維持し、frozen親のtrain Web本文位置の全vocabulary KL(parent||student)を補助損失に加える。temperature1/coefficient1/各更新、reference8×1024を固定しsweepなし。gold EOS/BOS/role/padding位置をKLから除外するが確率のvocabularyはEOSも含む4096全体で正規化する。通常CE100M＋別計数のsoft targets、referenceinputは3068更新なら25,133,056でmaininput100,532,224に追加。参照は親Web cursorの別forkでmainのWeb75Mと重なり、新教材量へ足さない。旧staged CE100Mの全評価を対照に再利用する。この補助Web exposureも変わるため同総supervision量/純objective単独比較とはしない。

web_kl_preservation.pyはKL方向/teacher detach/body位置maskと別replay位置・counter・digestを実装、CPU2tests/1.60秒成功。web_kl_condition_trainer.pyはCE backwardとKL backwardを同更新に蓄積してからcombined gradient clip/Adam/schedulerを実行し、両samplerとKL/teacher/source identityを一つのatomic fullcheckpointへ保存。小CPU実fixtureの連続4対2+2で全stateとloss/gradient/digest/counter一致、元model/Adam/RNGとteacher weights/eval/no-grad保持、main96/reference64inputを分離（1test/1.66秒成功）。初回2件のtest不備（differentiable tensorをNumPy比較、toy parent initial_lrとschedule baseの不整合）はXML保持しfixture/比較だけ修正。旧凍結trainer/evaluator/品質条件は変更しない。CPUfixtureは実10M CUDAや品質の証明ではなく、本turn科学学習/GPU0。

web_kl_trainer_preparation.jsonと可搬15text/177060bytes、gzip49112/SHAc3e43b4761d25e953fd5868e9a6483d907811c66d685867d7b6576a17d32efc5を保存、全Windows raw/archive一致。旧actual581514は実ps不在、科学GPU job0。元10B UI582426/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15117517の実identity/HTTP親410f975d…/10,000,007,168/busy=falseを確認し稼働継続。

次はown runner/reviewer/durablePSを実装し、既存process確認→実CUDA全state再開（KL_state/replay/teacherも含む）＋32 combined timing→全900秒内と測定できた場合だけ科学config凍結・通常CE100M＋別reference学習。全4primary終端stream/counterとcached staged controlを一致させ、同256byte/全日本語/全80/bridge/retention・全内容読解・元relative coherence+8/CI/BPB/EOS/反復、absolute、歴史Web1%を維持して採否。今回の対照coherence23から+8が必要で基準を緩めない。失敗時のcoefficient/temperature/shape/order/source/LR sweep・自動長期延長・有利なCP探索なし。最終seed/full dev/protected testは品質pilot合格後。旧数値7失敗/Phase0–3保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。
同100M教師の学習順序比較を全評価まで完了・不採用（2026-10-06 JST）: Baseのみを品質・独立学習seed/full dev/protected test/採用まで継続し、実完了時に通知して停止する。Chat/Dialogue/SFT/量子化は開始しない。Baseは未完了・未採用。前準備/起動は6ac4ad3へlocal commit。

actual581514/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15094429はcomplete・実process不在。科学100,000,000教師/100,532,224input/3068更新、CPupdate323503 SHAfb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae。train163.394035秒、scienceGPU224.477945＋実CUDA検証20.297709＝全244.775654秒<900。検証40更新/1,307,967教師はscienceと別会計。v1推定922.223216秒の拒否を保持し、v2は同評価の過去全非学習GPU88.466379/92.796498秒から150秒枠＋30%＋50秒を使い、全予算817.223216秒を事前凍結した。実上限/品質条件/教師/形状/親/実LR/順序は緩めていない。

同historical10.5B fullstate/実LR.00001/Adam/scheduler/RNG/同Web75M・story5M・ordinary10M・conditional10Mで、混合→Web→story→ordinary→conditionalの順だけを変更。cached control100MはGPU再評価せず保存結果/全notesを再利用。全4source終端cursorと教師/EOS/input/bytes/focus counterが一致、親Web cursorから73421blocks継続を実stateで確認。教材増量や独立学習seedの比較ではない。

対照→順序変更: BPB .974820→1.133613（16.2895%悪化）、文法2=69→65/関連2=51→39/一貫性2=4→23/適切18→26/EOS30→76/自動反復31→2、Unicode・role・empty両方0（各80）。意味60.938→56.250%、JBLiMP76.133→78.248%、JCQA34.584→26.542%。一貫性差+19/paired95%CI[.1375,.3375]は固定devのnonblind結果で、独立seed/一般自然文/唯一原因を証明しない。EOS/反復には改善がある一方、relative BPB guard・歴史Web1% BPB guard・絶対一貫性27/適切27に未達で不採用。停止率だけをBase完成としない。

同byte256/472055bytes・全日本語192/331/1119・全80greedy64・bridge128/retention128を完了。全80を個別読解、同id/prefix/raw/stop2件だけ過去notesを再利用し78新観察、独立人間評価なし。最後のrelation教材のライト/人名/在庫の型への脱線が目立つ。source recency/forgettingは仮説であり確定原因とはしない。local bridge両極正答62→59/128、未見構造20→8/64、未見語彙42→51/64、旧retention45→36/128。自然文の改善と局所probeは区別する。

completion source_order_condition_comparison_completion.json/review source_order_condition_comparison_v2_review.jsonと全raw-bound notesを保存。可搬331text/12,599,429bytes、gzip2,687,752/SHAbd14762b47fc51c0b22872f516d7239a9ae273dbd6b0f3fd3b402039952424a1、全Windows raw/archive SHA一致。checkpoint tensors/13GB index/原文arraysは重複しない。元10B UI582426/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15117517の実identityとHTTP親SHA410f975d…/10,000,007,168/busy=falseを確認、科学GPU job0。

次の具体作業はsource_order_followup_diagnostic_proposal.jsonのCPU30秒/GPU0の既存paired256 body/goldEOS NLL整理。全byte BPB再現・変化の件数/固定文長quartiles・既存日本語/全80notesの差を記録し、停止の改善と本文予測の退行を区別する。新採点/tensor・data再parse/保存点探索なし。仮説に根拠がある新規な有限比較を最大1つだけ定義し、根拠がなければ新実験なしを記録する。別順序/比率/LR/weight/source sweep・自動長期延長・有利なCP選定・基準緩和なし。独立seed/full dev/protected testは品質pilot合格後。旧数値7失敗/Phase0–3を維持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。
同100M教師・教材順序比較の実CUDA検証を終え、本学習を開始（2026-10-06 JST）: Baseのみを品質・独立学習seed/full dev/protected test/採用まで継続し、完了時に通知して停止する。Chat/Dialogue/SFT/量子化には進まない。Baseは未完了・未採用。

own v1の実CUDA4対2+2で全32state/history/finite checksが一致、親model/Adam/scheduler/RNG/実Web cursor/実LR.00001を維持。32timingを含む40検証更新/1,307,967教師、GPU20.297709秒、科学教師0。actual580440はcomplete・実process不在。固定300秒の評価枠を含む見積922.223216秒は900秒超過のため本学習前に拒否、v1 source/config/resultとsource_order_budget_rejection_v1.jsonを保持。

own v2は予算推定だけを修正し、v1 CUDA証拠を再利用する。完了historical/original routeの同256byte/80greedy/日本語192・331・1119/bridge512/retention512を実metricsと照合し、学習以外の全GPU占有88.466379/92.796498秒を確認。純評価timerとはしない。max(150秒,実測最大×1.5)の枠＋学習との合計に30%＋50秒の余裕、検証20.297709秒を全て算入した見積817.223216秒。実累積上限900秒・全品質条件・教師量・形状・親/実LR・source orderは不変。CPU3tests/0.90秒、v1/2のscience関数AST一致、PS構文成功。別順序/比率/LR/weight/shape sweepなし。

科学config configs/phase6/source_order_condition_comparison_v2.json SHA03b4ad47fa42b9a669c4588e736648e6339c93b9eb0cf3d08aac22a46cf90a88。新100M教師/Web75M→story5M→ordinary10M→conditional10M、same historical10.5B fullstate・cached mixed100Mを再評価せず対照に再利用。Windowsworker32208/actual581514/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start15094429をps確認、training1,307,936教師/loss2.633086有限で稼働。run reports/phase6/source-order-condition-comparison-v2-20261006、再開 scripts/run_source_order_condition_comparison_v2.ps1 -Mode Train -Worker。元10B UIはGPU中停止しwrapper finallyで復帰。

次は同job100M終端・同byte/全日本語/全80/bridge/retention→全80個別読解→cached controlと全4source cursor/counter一致・会計確認→relative/absolute/歴史Web1%採否→可搬保存/UI復帰/local commit。品質失敗から自動延長・別順序/有利なCP探索・基準緩和へ進まない。独立seed/full dev/protected testは品質pilot合格後。旧数値7失敗/Phase0–3を維持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。
公開候補4件の有限調査と、同教師の学習順序比較のCPU準備を完了（2026-10-06 JST）: Baseだけを品質・独立学習seed/full dev/protected test/採用まで継続し、完了時に通知・停止する。Chat/Dialogue/SFT/量子化なし。前turnの両教材不採用をf7e9bd9へ保存したprogress後、4 actual jobsの終端と元10B UI578328の実ps稼働を再確認。本turn GPU0/学生学習0、Base未完了/未採用。

公開metadata/card4件を匿名・pinned revisionで実5.391722秒取得、bulk raw0。kai271/TinyStories-JapaneseはMIT/GPT4o-mini・概算3000話/train2.44MBで10M sourceの見込み不足。aixsatoshi/cosmopedia-japanese-20kは27byte cardにlicense/翻訳teacher/family splitなし、上流の許諾だけを翻訳版の許諾としない。OpenJAはCC-BY4.0 compilation/国会会議録3.24Mrecords・約679M Qwen tokensという著者主張であり、学生tokensや日常物語の供給量ではない。izumi-labのWikipediaは別snapshotでも既試行と同じsource class、byte一致/全重複は未確認。今回の候補から新規sourceを選ばず、全日本語コーパスに適材が存在しないとは断定しない。public_prose_registry_metadata.json/review.jsonとpinned cards/APIを保存。追加のsource/filter探索へ無制限に進めない。

元curriculum_strategyはfresh100Mでも1M短文/4M物語/5M Webの混合poolで一貫性6/80だった。純物語学習と誤記せず、新たな比率sweepを始めない。次の有限仮説はデータと教師量を変えず学習順序だけを変えること。歴史10.5B Web fullstate/d18e3e…/実LR.00001・親Adam/scheduler永久0.1floor/RNG/Webcursorを維持し、同100M教師/Web75M/story5M/ordinary10M/conditional10MをWeb→story→ordinary→conditionalの順へ変える。対照は同じ親/実LR/材料/教師の完了historical mixed100Mを保存評価ごと再利用。これはsource recency/order仮説で、読取専用gradient marker falseを干渉の確定診断へ言い換えない。

source_order_condition_trainer.pyの新sampler/trainerを追加。既存凍結sourceは不変。CPU3tests/2.21秒で、混合対照と全4streamの実x/y/focus block SHA、全5counter群・終端cursor・physical batch数が一致し、source間順序だけ変わることを確認。phaseをまたぐ保存再開でexact targets/cursors復元、order/旧kind変更を拒否。終端全mask Web paddingも維持。これは小CPUfixtureでGPU fullstate/科学学習/品質の証明ではない。実CUDA再開と計測は未開始。

source_order_condition_comparison_proposal.jsonを実CPU0.025207秒で定義、登録phase6 top-level source_order configs0（限定scan、未登録研究を含む網羅証明ではない）。新100M/保存control100M、全新GPU900秒上限を固定。次はown runner/reviewer/永続PSを実装・必要CPU/CLI/PSチェック→既存process確認→実CUDA4対2+2全state/history/finite32条件＋32timing→実測全budget<=900秒の場合だけ本science config凍結・同100Mを起動する。元の256byte/Japanese192・331・1119/全80greedy64/bridge128/retention128、relative/absolute/歴史Web1% gateを維持。完了checkpointの全4source終端cursor/counterもcached controlと一致が必須。全80を読んで採否・可搬保存/UI復帰/local commitまで進める。失敗時に別順序/比率/LR/weight/shape sweep・自動延長・有利な保存点選定・条件緩和なし。現在の実GPU学習job0、UI稼働。WSL uv3.12.7、旧数値7失敗/Phase0–3維持、local commitのみ/pushなし。以下は過去の履歴。

Base用公開教材の2候補を実確認し両方不採用（2026-10-06 JST）: 最新境界は品質・独立学習seed/full dev/protected test/採用を満たすBaseの実完了まで継続し、完了時に知らせて停止。Chat/Dialogue/SFT/量子化/最終deploymentは始めない。本turnの学生学習0・新checkpoint0、Base未完了/未採用。

固定13完了reportの整理を実CPU0.016503秒/GPU0で完了（base_failure_route_synthesis.json）。24 summary appearancesは独立24実験とはせず、既知raw10種類とhash未記録10行を区別。量・学習量・親/actualLR・shape・train fit/局所transferの改善だけで自由生成の基準達成とはならない。容量の限界や唯一原因は断定しない。

公開Apache2 Qwen3-4B-Instruct-2507 revision cdbee75f…を匿名で8.06GB回復/全hash確認（103.276秒）。既存評価promptを与えず独立train familyの自然文64件を実BF16生成、teacher inference34.447秒/全GPU36.393399秒/peak allocated8.57GB、teacher6611・student body7511 tokens、64EOS。全64個別読解で弱37/64（上限10）・format12/content24/grammar7/language4（重複あり）、不採用。raw body218.046 tokens/secから10Mは約12.74h、除外/packingを含まない見積で全量生成なし。同teacherのprompt/settings再試行なし。上流teacherを使った教材調査でありproject Chat/SFT学習ではない。

既使用SimpleStories-JAを新教材と数えず、公開llm-jp/magpie-sft-v1.0（Assistant生成Qwen2.5-32B、Apache2、revision4f949e…）の284MBを匿名回復/全hash確認10.163秒。固定whole-body条件でtrain132476行を一度だけ走査、実CPU3.754377秒/GPU0、16057文/4,226,508 serialized source tokens（body4,194,394/fullCE候補4,210,451/EOS16057）。目標10M未達。固定uniform-document64件を全件読解、会話応答18件など弱23/64>10（content3/language3/grammar1、重複あり）で内容も不採用。外部事実の網羅確認はしておらず未flag文を正しい事実の保証にしない。候補は隔離保持し学生学習へ入れない。元のsource/selector/reviewを変更して合格にしない。

4 actual jobs 577732/578050/578629/578816は全complete・boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe・実process不在。UI578328/start14899123の実identityとHTTP元10B親410f975d…/10,000,007,168/busy=falseを確認。public_prose_feasibility_completion.jsonに正確identity、reviewsとraw SHAを保存。関連CPU2+3tests成功（3.41秒/0.89秒）、PS構文成功。可搬121text/872890bytes、gzip219606/SHA78a692a006bc45a4ccd965f0e17955a59877be2455ca14913e6be236209f952d、全Windows raw/archive SHA一致。8GB weights/284MB raw/arraysはarchiveへ重複しない。旧数値7失敗・全品質条件/Phase0–3を維持、PythonはWSL uv3.12.7、local commitのみ、pushなし。

次の具体作業: 新規日本語の短い物語/独立説明文の公開候補を最大4件までmetadata/cardのみで調べ、license/gated/language/upstream teacher・whole-document規模/split・既試行との重複を一覧にする。bulk download/GPUなし、必要な10M sourceを供給できる見込みと新規性がある1候補だけに実供給/固定64内容pilotを定義する。見つからない場合はnone-feasibleを記録し、無制限の教材/filter/model sweepへ進めない。採用sourceが用意できた場合だけ元10B fullstate/.0002・同100M教師/Web75/story5/ordinary10/newprose10Mと保存controlを比べ、実CUDA再開/実測予算と全256byte/Japanese/80・relative/absolute/歴史Web1%基準を維持。source量/内容/多様性/上流生成を同時に変えるため単純増量の因果とはしない。最終seed/full/testは品質pilot合格後。以下は過去の履歴。

歴史Web親の100Mと全80評価を完了・不採用（2026-10-06 JST）: 前準備17a46ddは実CPU parent監査/修正の凍結/全32CUDA保存再開/100M起動まで。本turnはactual571973/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14810743の実終了・ps不在と終端を確認。最新境界は品質・独立学習seed/full dev/protected test/採用までBaseだけを続けて完了通知・停止、Chat/Dialogue/SFT/量子化なし。

歴史10.5B Web fullstate d18e3e17…/実LR.00001/Adam/scheduler/RNG/実nested Web cursorを維持しreheatなし。新science100,000,000教師/100,532,224input/3068updates、元relation2048の同Web75M/story5M/ordinary10M/conditional10M。CPupdate323503 SHA6d901bd290cc5b7ab0b52a3a2309232d1e08c7fba32ecb8ec1e5656fe1a2f5a0、train160.611815秒、scienceGPU249.078194+成功probe16.049172+失敗2件13.190772=278.318138秒<900。成功40/失敗8の検証更新と計1,565,061検証教師はscience別、V1更新0/V2保存state8更新も全証拠を保持。3短sourceの終端cursor/教師/EOS/input/bytes/focusは旧controlと全一致、実Web73421blocks継続を確認。heartbeat99,765,337ではなく完了CPの100Mを採用。

元10B/.0002 route100M→歴史親/.00001 route100M: BPB .990936→.974820、文法2=72→69/関連2=68→51/一貫性2=12→4/適切26→18/EOS34→30/自動反復21→31/Unicode1→0、role/empty両方0（各80）。意味59.896→60.938%、JBLiMP75.529→76.133%、JCQA35.567→34.584%。歴史Web1% guardは今回は全条件合格するが、relative/absoluteは不合格。一貫性差-8/paired95%CI[-.1875,-.0125]は今回の固定80のnonblind差で、独立seed/自然文一般やLRだけの唯一因果を証明しない。Base不採用・未完了、独立seed/full/test未実施。

同local bridge両極正答57→62/128、新文型2→20/64、未見語彙55→42/64、旧retention60→45/128。局所構造の改善と自由生成品質は異なり、shared generator/旧train forms重複を明示。全新80を個別読解しexact id/prefix/raw/stop4件だけ同評点・根拠を再利用、76新観察・raw SHA付きnotes、独立人間評価なし。result SHAb45b55ac4e332d97ccfe717b85b7972db60478ba3fa027d7bb94acf5363251b2。completion historical_parent_condition_comparison_completion.json/review historical_parent_condition_comparison_v3_review.jsonを保存。terminal452text/14,432,622bytes、gzip3,411,869/SHA8a01b98aa9f20758d838ee9af8e3e31cf7d0b577ef07f3321950b9b9d8a7372c、全Windows raw/archive SHA一致。元10B UI574008/boot53f…/start14836164の実psとHTTP親410f975d…/10,000,007,168/busy=falseを確認、科学GPUjob0。

次はbase_failure_route_synthesis_proposal.jsonの固定13完了reportだけを読むCPU30秒/GPU0の有限整理。教材量・学習量・親/actualLR/source順・形状・train fit/局所transfer・自由生成を実証予算と品質の小表へ集約し、否定された説明と未検証の説明を分ける。raw再採点・新GPU・tensor/13GBindex再parse/全コーパス照合なし。まだ未実装/未開始で、重複した失敗routeを新研究として繰り返さず、根拠がある新しい有限比較だけを定義する。容量限界の断定・自動長期延長/再加熱・template/ratio/weight/LR sweep・有利なCP走査・基準緩和なし。旧数値7失敗を保持、WSL uv3.12.7/local commitのみ、pushなし。以下は過去の履歴。
歴史Web親の実CPU監査と新100M比較を起動（2026-10-06 JST）: 最新境界は品質・独立学習seed/full dev/protected test/採用までBaseだけ、実完了を知らせて停止。Chat/Dialogue/SFT/量子化なし。actual parent2件と登録74configのtraining-parent refsをCPU0.323秒で確認。元10Bは実LR.0002・BPB.985891、歴史10.5B Webは実LR.00001・BPB.971570・EOS0/反復62、同10M形状。この歴史fullstateを親とする同Web75/story5/ordinary10/relation10M条件は登録済み比較にない。旧lowLRは別の混合親・Web0/短文200Mなので今回の対照として流用しない。親/model/Adam/RNG/scheduler/Web cursor/実LRが同時に変わり、純粋なLR因果ではない。

元の採用済みrelation2048/source manifest154f13da…を再利用し、問いbalance不採用材料・教材増量・Tokenizer変更なし。V1初期検証はCPU/CUDA直接比較で学習更新前に失敗(GPU1.853119秒)。V2は初期model/Adam/scheduler/RNG/実Web cursor/LRを厳密保持、連続4対2+2の全state/history/finite31条件一致したが既存gateの旧LR.0002固定で失敗(GPU11.337653秒/8検証更新260868教師)。両旧source・job・checkpointを凍結保存し、ownV3 gateで同じ全32条件と実親LR.00001を厳密確認、条件緩和なし。新CPU4tests/0.85秒・PS構文/preflight成功。V3実CUDA全32保存再開一致と32timing成功、40検証更新はscience別、GPU16.049172秒。失敗を含む全検証29.239944秒を新GPU総900秒へ算入。

科学config SHA8201c995e37421869d43361fe9b381e0bd90ee16bfd8b54fca90f93b093dc99d、歴史CPd18e3e17…/update320435/input10,500,014,080/fullAdam/scheduler/RNG/実nested sampler-web cursor/LR.00001を保持しreheatなし。元10B/.0002の同100M controlを正確cacheとして再利用し新科学100Mのみ学習。実測見積844.347+全検証29.240<900秒、科学上限870.760秒。Windowsworker28616/actual571973/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14810743を確認、本学習中。run reports/phase6/historical-parent-condition-comparison-v3-20261006、再開はscripts/run_historical_parent_condition_comparison_v3.ps1 -Mode Train -Worker、重複起動なし。科学中UI停止・wrapper finallyで元10B復帰。準備300text/3,465,628bytes、gzip1,055,574/SHA2ba3be1f373e5b0ced82d689c4c81b7cc1148402ad031e52a4dc6498db64faed、全Windows raw/archive SHA一致。

次は同job100M終端/同byte256/全日本語192・331・1119/全80greedy64/同bridge128/retention128→全80個別読解/exact peerのみ再利用→3短source cursor/counters一致と全実state/教師→元relative/absolute/歴史Web1% guard採否→可搬保存/UI復帰/local commit。Base未完了・最終seed/full/test未実施。品質失敗時は自動500M/2B延長・再加熱/LR比率weight/template sweep・有利なCP走査・基準緩和なし。旧数値7失敗を保持、WSL uv3.12.7/local commitのみ、pushなし。以下は過去の履歴。
query-balanced同100Mと全80採否を実完了・不採用（2026-10-06 JST）: 前準備333b60bはCPU診断/固定64採用/実CUDA保存再開/100M起動までのprogress。本turnで同jobを終端まで進めた。最新境界は品質採用までBaseだけを継続し完了時に通知・停止、Chat/Dialogue/SFT/量子化なし。actual566992/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14661392はcomplete・実ps不在。新science100M教師/100,532,224input/3068更新、Web75M/story5M/ordinary10M/conditional10Mを実終端で満たし、元10B fullAdam/RNG/実LR.0002/元Web cursorを保持。checkpoint00308244 SHA001b12678273465d1468ae737a9a6b4c0c7d502ccd649c5dbb5446f834109a4e。train160.272985秒、scienceGPU253.213834+検証16.879824=270.093658秒<900、検証1,304,156教師/40更新は新scienceとは別計上。3 unchanged Web/story/ordinaryのterminal sampler/counters一致、Web73421blocks、fullstate/history/有限値会計採否成功。

同byte256/472055bytes/全日本語192/331/1119・80greedy64/同128bridge/旧128retentionを実完了。新80を全件読み、同id/prefix/raw/stopの既存peer37件は評点/根拠を保持し、新43件の観察を保存したnonblind採点（独立人間ではない）。対照→新: BPB .990936→.990857、文法2=72→74/関連2=68→69/一貫性2=12→10/適切26→24/EOS34→35/反復21→25、Unicode両方1・role/empty0（各80）。意味59.896→59.375%、JBLiMP75.529→74.622%、JCQA35.567→36.104%。一貫性差-2/pairedCI[-.075,.025]で有意な悪化や改善の独立証明ではない。relative/absolute/歴史Web1%の元条件に未達、不採用・Base未完了、最終seed/full/test未実施。

trainの最後の人名が正解の頻度は304→164/342へ減少したが、未見comparison32組の両正解1→4/両逆22→16は事前定義gain8に未達でsecondaryも不合格。広い自然文の改善には届かなかった。教材のgrounded関係を変えていないことやlocal probeの小さい増加をBase採用にしない。データ・query word/答え/文長のconfoundsを保持し、推測したshortcut原因を確定したとはしない。失敗から自動延長・queryvariant/比率/weight/LR総当たり・都合のよい保存点走査・基準緩和を行わない。

result SHA6e2428c5788cb673c653d215ac934c5fcc5f3f61700572a6dcba4f741695c06c、raw SHA付きnotes/review/completion保存。terminal314text/21,370,074bytes、gzip3,953,663/SHA03e46203a8b27733a4365a69be3b3429dff476160312583489eefb5b3d18f8fa、全Windows entry/archive raw SHA一致。元10B UI567465/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14687227の実ps/HTTP親SHA410f975d…/10,000,007,168/busy=false確認、科学GPU job0。次はbase_parent_baseline_audit_proposal.jsonのCPU30秒限定で、実original10B親と歴史10.5B Web guardの実LR/教師/input/sampler/Adam/schedule/evaluationと旧lowLR recoveryのparent/materialを整理し、別の親から同短文mixtureを学ぶ比較が未試行か重複かを判断する。GPU/学習/保存点探索/guard変更なし、未試行の有限比較が定義できるまで次の科学学習を自動起動しない。旧数値7失敗・全品質条件保持、WSL uv3.12.7・local commitのみ・pushなし。以下は過去の履歴。

queryの偏り診断・教材採用・実CUDA確認を完了して同100Mを起動（2026-10-06 JST）: 前turnf01b927はearly8.15M/100M全80比較を実完了・不採用まで保存したprogress。今回も最新境界のBaseのみ、Chat/Dialogue/SFT/量子化なし。新CPU raw-margin診断0.066秒/GPU・学習0で、両CP×bridge/retentionの全2048requestをSHA/共通targetで照合し元の集計に一致。候補EOSを含まないことを明記し、固定256 goldEOSの平均NLL2.361645→2.291431/143文改善を別扱いにした。新診断は過去のEOS採点や元指標を変更しない。

100Mの未見comparison32組は両正解1/両逆22/正方向context shift3、候補token/byte長補正では両正解0、等token長21組も両正解0。未見negation32組は両正解1/同候補31/正方向shift31で、2種類の失敗が異なる。train比較342文すべて長い方を答え、304/342は最後の人名が答え、grounded label error0。頻度とmarginはmodelの学習規則・唯一原因・capacity限界の因果証明ではない。元primary/BPB/全内容基準は維持する。

固定seed2026100671で同171比較trainfamilyの86family/172文だけ問いを短い方へ変え、論理的な答えを反転した新sourceをCPU0.211秒で準備。2048文/同1024families・category数・順序・事実/関係文を保持し、残1876文は完全一致。長い方170/短い方172、同24 relation train formsに4 query variantを加えた28 surface/query組合せ。未見form4/5・評価promptは教材に加えず、bridge/retentionのraw bytesは元のまま。generated body85350/fullCE87398/EOS2048、serialized89446は対照と同総数、学習は普通body+EOS CE weight1。問い語・答えの人名・個別文長等を一緒に変えるためpure position causalityとはしない。固定64を全件読み、exact prior52件の評点/根拠を再利用し新12観察、弱い文/未解決grammar0・全paired state一致で採用。人間独立blindではない。manifest fd39c41e…/arrays bbb483bb…を凍結。

旧凍結trainer/evaluatorを変更せず、own trainer/run/review/永続PSを実装。関連CPU6tests/0.91秒・PS構文・actual preflight成功。actual565908/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start14653059のCUDA4対2+2全32state/history/finite checks一致、32stable timing、40検証更新/1,304,156教師をscienceとは別計上、GPU16.879824秒。probe complete/実ps不在。実測から100M学習378.341秒・save/warmup込み、評価/余裕を含む新science見積841.844+probe16.880<900秒として設定を固定。

science config SHA aa65e594d47b996df3dbe3e7aa42466cfc3d13604e84a75afd8950c708ff0297、元10B親/実LR.0002/fullAdam/RNG/元Web cursor/seed42、Web75M/story5M/ordinary10M/conditional10Mを維持。元Web対照100Mの実評価/notesを正確に再利用しGPU再評価しない。新science教師100Mのみを新規計上し、独立seedには数えない。Windowsworker23392/actual566992/boot53f…/start14661392の実ps/job確認、training1956167教師/loss2.32770586有限まで進行。run reports/phase6/condition-query-balance-comparison-20261006、restart scripts/run_condition_query_balance_comparison.ps1 -Mode Train -Worker。科学中元UI停止、wrapper finallyで復帰。準備84text/9,460,165bytes、gzip1,301,118/SHA bdbf0d850d85120f2fe0cb11d3d1e38086e2bfe3bd615dead9fe09cab6dd1eb4、全Windows entry/archive SHA一致。

次は同jobの100M終端/全評価→新80全件の個別読解/exact peerのみ再利用→3 unchanged source cursor/counterと履歴確認→元relative/absolute/歴史Web1%採否＋事前定義の32未見比較secondary gain8/逆答え減少を報告→可搬証拠/UI復帰/local commit。secondaryだけの改善を採用にしない。Base未完了・最終seed/full/test未実施、失敗時に自動延長/問いvariant・比率・weight・LR sweep/都合のよいCP走査/条件緩和なし。旧数値7失敗保持、WSL uv3.12.7/local commitのみ、pushなし。以下は過去の履歴。

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
