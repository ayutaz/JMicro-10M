# 教材汎化の改善比較・実行記録

2026-10-13 最終結果: goal『4まで』の4項目を実行・監査し、不採用として閉じた。[結果136](136_chat_generalization_results.md)。D1実学習3,641更新・1,899,562教師と全state/教師列監査、全14評価セット・3,066内容判断・NLL7点を完了。最終D1内容は新12/旧15（必要56）、自己生成文脈3/1（必要15）、提供文脈5/2。回復predicate不成立で未実行・効果未確認、合格候補なしで保持/samplingも未確認。padding24確認更新は数値不一致で不採用。20件のCPU gate確認・台帳・元UI復帰の監査まで終了。GPU累積2,117.569秒/6時間。Base/Chat未完成・未採用、追加研究/学習は停止。以下は各時点の実行履歴。

## 2026-10-13 実行再開：t2全評価とD0最終評価

goal『4まで』の継続で実作業へ戻った。直前の135計画更新だけでは目的を達成していない。D1 t2の実checkpoint・optimizer/scheduler/RNG・sampler位置・全padding込み教師列digest・実消費をCPU監査し合格。2,428更新・1,266,837教師、SHA `5a83ad58b6c9ee0e036dbc636d727d16d42296c450f04ae74d7de302b2ceb08f`。[t2監査](../reports/phase7/chat-generalization-20261013/D1/t2_audit.json)。

D1 t2新旧とD0 t2/t3新DEVの必要生成・NLLを実行し、各launcherは終了exit0・元UI復帰exit0。終了processを確認してから次を起動し、同時GPU jobは作らなかった。D1 t2新107/旧105、D0 t2新109/t3新90の未判断応答を明示的に読み、文法・関連性・実履歴文脈を理由付きTSVへ保存。残りは完全に同じ実履歴・raw IDs/bytes・checksの判断だけを出典付き再利用し、各219件の原raw/全notesを検証した。自動gold一致採点や独立人間の評価ではない。

| 条件 | 新内容 /80 | 旧内容 /80 | 新自己生成文脈 /24 | 旧自己生成文脈 /24 | 新提供文脈 /24 | 旧提供文脈 /24 |
|---|---:|---:|---:|---:|---:|---:|
| D0 t2 | 14 | 16 | 2 | 4 | 4 | 4 |
| D1 t2 | 14 | 6 | 4 | 0 | 7 | 2 |
| D0 t3 | 16 | 18 | 5 | 4 | 6 | 4 |

D1 t2の固定TRAIN本文NLLは0.004050、同じ新DEV本文NLLは4.272016、RPC本文BPBは1.808632。親の新DEV3.058625/RPC1.351262との違いを残す。原screenは未達で、正しい提供履歴も十分でなく回復条件は最終t3まで未判定。RPCは正式なBase保持確認の代替ではない。

新しい[全保存点の進捗監査observer](../scripts/audit_chat_generalization_progress.py)は、各raw/notes/reviewのbinding、再利用元のhashと実履歴fingerprint、全NLL targetのID・dataset・本文bytes・教師mask分母と再計算totalを照合する。実行した[進捗監査](../reports/phase7/chat-generalization-20261013/progress_audit.json)で12/14suite・2,628/3,066内容判断、6/7NLL点を確認。全体完了を宣言する機能は持たず、D1 t3と全state監査・選定・最終解析をpendingとして残した。[byte一致保存94file](../reports/phase7/chat-generalization-20261013/t2_review_archive.json)。

D1は有効t2 stateから同じ凍結recipe・元の累積学習2,400秒枠で最終Bへ学習中。実生存観測はWSL PID228316 / boot `4052bfc5-3850-44e4-9123-d34a9e19f36e` / start_ticks47910161、Windows worker20436。3,000更新・1,565,062教師までのheartbeatと実processを確認した。観測後の生存を保証するものではない。次は終端を確認し、t3実消費/全state監査→新旧全219応答とNLL→最終paired比較・原条件の分岐→全体完了監査。paddingは完了・数値不一致で不採用、10M/元gate/総GPU6時間は維持。以下の計画更新やt1実行は当時の履歴。

## 2026-10-13: 「4まで」の継続実行

### t1全レビュー・同条件比較とpaddingのGPU結果

計画135の文書更新後、ユーザーのgoal継続「4まで」により実作業へ戻った。D1 t1は1,214更新、633,391 Assistant本文+EOT教師、checkpoint SHA `918021b64db561820be1f56fc4ba4e9650e861ab110e1387f4b59eeaeefd0b4e`。実state・Adam/scheduler/RNG・sampler位置・全padded入力列digestと実metricsの監査が通った。親とD0/D1 t1の新旧6suite・1,314内容判断と共通NLL3点をそろえた。既存旧suiteの再利用も含む数で、新しい独立問題数ではない。全raw、実履歴、判断の理由と再利用fingerprintを保持する。Codex非blindで、人間blindや独立学習seedの証拠ではない。

| t1の指標 | D0新 | D1新 | D0旧 | D1旧 |
|---|---:|---:|---:|---:|
| 文法・関連性同時2 /80 | 14 | 18 | 11 | 6 |
| 対応する正しい提供履歴の文脈2 /24 | 7 | 8 | 2 | 1 |
| 自己生成履歴の最終文脈2 /24 | 6 | 4 | 1 | 2 |
| 固定自然停止 /80 | 79 | 78 | 75 | 79 |
| 自己生成自然停止 /59 | 59 | 59 | 59 | 55 |
| 固定反復 /80 | 1 | 2 | 7 | 2 |
| 自己生成反復 /59 | 0 | 0 | 0 | 4 |

D1−D0の同時2差は新+5.0ポイント、paired family95%CI[-5.0,+16.25]、旧−6.25ポイント、CI[-15.0,+1.25]。双方とも0を含む。t1は絶対screenも反復非増加も不合格で、改善確定や採用点とはしない。最終t3の採否・回復predicateはまだ判定できない。正しい提供履歴の保持も不足しており、自己生成だけを失敗原因とは扱わない。

固定112targetのD1 TRAIN本文NLLは親3.148497→t1 0.004231だが、同じ新DEV本文NLLは親3.058625→D0 4.080351 / D1 4.084001。RPC DEV本文BPBは親1.351262→D0 1.725132 / D1 1.677399。TRAINへの適合と未知DEVへの移行を区別する。RPCのChat形式BPBは正式なBase保持suiteの代替ではない。全TRAINの意味品質認証にも読み替えない。[中間解析](../reports/phase7/chat-generalization-20261013/intermediate_analysis.json)、[中間比較](../reports/phase7/chat-generalization-20261013/intermediate_screen.json)。

最初の中間比較では、過去対照のreviewer表示名 `Codex plan131 reviewer` と新判断の `Codex plan133 reviewer` が一致せずCPU比較が停止した。[原失敗](../reports/phase7/chat-generalization-20261013/comparison_reviewer_label_incident.json)を残し、凍結source/configや原notesを変更せず、[別の出典確認observer](../scripts/compare_chat_generalization_provenance.py)を追加した。同じRUBRICとCodex非blind/独立人間false/blind falseを厳密に確認し、この2表示名だけを明示aliasとして扱う。元の表示名、原notes hash、限界を比較JSONに保存する。未知の評価者・human・blind・独立性・rubricの不一致を拒否するCPU確認も通過。採点・raw・数値比較・品質gateは変更しない。歴史的判断を新しい再採点やblind一致として主張しない。

別padding条件は実GPUの24確認更新まで完了した。全BのCPU教師列・更新group一致を前提に、最初の8更新ずつを固定/動的で比較し、動的4更新の連続実行と2更新保存後の再開を比較した。全stateとloss/gradient/LR/教師列履歴の再開一致・有限性は通過。warm-up2更新を除く実測教師速度は固定1,164.257 / 動的6,484.277 tokens/秒（約5.57倍）、peak allocatedは16,223,183,360 / 1,202,441,216 bytes。短い測定であり、長期の速度保証ではない。

**数値一致gateは不合格で、padding候補は不採用。** update2/3のloss絶対差0.000953674 / 0.001758337は事前上限2e−6を超え、各stepでmodel/gradientもrtol2e−4・atol2e−7を満たさなかった。全差とparameter名を保存し、測定後に許容差を拡大しない。CPU教師列一致、自己条件内の厳密再開、速度改善は、固定paddingと同じ数値学習や品質改善の認証ではない。main D1の重み/recipeを置き換えず、TEST・採用へ進まない。[padding全結果](../reports/phase7/chat-generalization-20261013/padding/result.json)。当該GPU消費20.662秒、launcher終了exit0と元UI復帰exit0を確認した。

D1は有効t1 checkpointから、同じ凍結条件・累積学習枠2,400秒でt2へ継続。起動観測はWSL PID219772 / boot4052bfc5-3850-44e4-9123-d34a9e19f36e / start_ticks47775228、Windows worker36700。これは観測時点のidentityで、将来の生存証拠ではない。次はt2保存state監査と新旧全評価、必要なD0新DEV t2/t3評価、D1最終B、全t3判断と分岐監査。padding比較の判定が終わっても4項目全体の完了ではない。

### GPU gateと時間配分の見直し

D1有限BF16の9確認更新（4,229教師）と保存再開の16確認更新（7,764教師）を実GPUで行い、全state/各step loss・gradient/LR・教師消費の一致を確認した。確認用重みは本学習へ継がない。教師Bまでの保守的学習予測は1,914.807秒、peak allocated16,223,183,360 bytes。新しい回答品質の証拠ではない。

初回評価予測は15,819.117秒で旧評価枠10,800秒を超え、本学習を開始せず停止した。GPU失敗entryと元測定・source/config・再登録metadataを `pre_gpu_contract_v2/` に保全。必要評価には条件付きsamplingと回復の両方を残す。部分的改善では両方が必要になり得るため、排他的と仮定して予算を減らさない。回復の自己生成失敗条件は、新旧いずれかに最終文脈2未満の会話が1件以上あることで、全体15/24を通っても該当し得る。

証明済みの旧suite876応答とRPC NLL9,000targetを新規GPU件数から除いた実必要上限は4,818生成・520 NLLbatch。最大64tokens、測定最大rate、1.5倍の安全係数、cold27回、reserve600秒を保ち、13,448.058秒と再計算した。総GPU上限21,600秒を増やさず、実測で収まるD1学習2,400・評価13,500・保持900へ再配分した（probe600/resume600/回復2,700/効率900/D0新学習0は維持）。保持は必要時にその枠内の実測gateを確認し、省略を合格扱いしない。

CPU再照合では親・データ・教師列・specと数値学習/生成関数のAST一致を確認した。通過済みGPU gateは原証拠を参照して新configへ再登録し、測定値を取り直さず新GPU確認にも数えない。GPU台帳の実消費40.9469秒と全失敗を保持し、counterをリセットしていない。修正版のD0全state監査と9,000 RPC NLL bindingも再確認した。D1の本学習と全内容評価はまだ未完了。

ユーザーの継続指示により実作業へ戻った。直前の計画更新135だけを目標達成とは扱わない。今回も教材改訂・同条件比較・条件付き誤履歴回復・別のpadding検証の4項目を保持し、第一比較の全評価を先に行う。以下の計画のみという記述は作成時点の履歴。

準備済みD1 TRAINは40,126 target、1周660,065教師、単一Userへの教師23,515（約58.6%）。280sampleのCodex非blind内容確認は問題0（完全同一内容の260判断を再利用し、変更20件を再確認）。独立人間確認・全TRAINの意味品質認証はしていない。CPU消費はD0が3,636更新/1,899,555教師、D1が3,641更新/1,899,562教師。D1の最終超過7は事前の完全応答0〜64規則内で、正確なB一致とは書かない。更新数差0.1375%、長さTV0.07281、EOT比差0.000693等の全7条件を通った。

TRAIN実体凍結後に新DEV80familyを作成した。10分類×8、自己生成対象24familyは2turn15・3turn7・4turn2で59応答。全gold/historyを作者Codex非blindで確認し、符号化・role・履歴収まりを検査。TRAIN最終質問との完全一致0、表面類似性flag0、最大Jaccard0.35714。表面検査は意味的独立性の認証ではなく、親の全corpusは再走査していない。新DEVはTRAINに使用せず、protectedTESTは未使用。

D0=旧C1は同じ親/Tokenizer/seed/spec/教材/教師順・全更新group/counterであることを監査した。旧18sourceのhashを保全し、全3checkpointと旧CUDA連続/再開stateをCPUで照合。既存の旧suite4点876内容判断とRPC NLL4点9,000targetを、同じ実履歴・raw・入力・重みへの出典付き再利用として登録した。新しい学習・独立seed・新しいGPU評価に数えず、旧jobを再起動しない。新DEVとD1の新しい重みに必要な評価は実行する。

共有GPU上限21,600秒を維持し、probe600、resume600、D0新学習0、D1学習3,600、全評価10,800、条件付き保持2,400、条件付き回復2,700、別効率900秒として凍結した。回復は最終t3の新旧両suiteで内容56/80・対応提供文脈15/24・固定機械gateを満たし、新内容がD0より改善し、自己生成履歴で未達がある場合だけ。評価の事前時間予測には条件付き回復3保存点とsamplingも含める。全stageで共有上限を超えず、条件が成立しなければ回復を未実行と記録する。

GPU前の対照登録で新helperがPath専用関数へ文字列を渡す不備を検出した。失敗したconfig/source/proofを `pre_gpu_contract_v1/` に保存し、新helper/runnerだけを修正して再凍結。旧frozen sourceや品質gateは変更しなかった。修正版の対照登録・D0全state/消費監査・RPC NLL再利用の実CPU検証は通過。launcherのPowerShell構文と新Python群のcompileも通過。現時点で新しいCUDA gate・学習・品質確認は未完了。

現在の小記録は `reports/phase7/chat-generalization-20261013/`、実行configは `configs/phase7/chat-generalization-20261013.json`。重み・TRAIN/DEV/NLL教材はWSLに保持しGitに追加しない。次は有限CUDA、全state保存再開、全必要評価の時間gateを行い、合格後にD1のB/3へ進む。

## 開始・計画更新時の履歴

2026-10-13 JSTの最新依頼「課題の解決方法とその計画」は[計画135](135_chat_problem_solution_plan.md)に整理した。今回は計画・記録更新のみで、以下の過去の開始記述を新しい実行指示として扱わない。今回の小記録確認ではD1 TRAINの凍結・CPU消費チェック・固定sample内容確認まで証拠があり、新DEV・GPU学習・品質確認は未完了。

2026-10-13 JST開始。ユーザーの「4まで進めてください」で、直前の4項目（教材改訂→同条件比較→条件付き誤履歴回復→別のpadding検証）を再開する。[計画133](133_chat_generalization_followup_plan.md)の段階1〜4が第一比較の実行手順となる。番号の参照先について確認を提示済みで、返答があれば範囲を修正する。現在は両解釈に共通する事前登録・教材改訂の準備を進める。

第一比較は同じ元WebUI10B親・Tokenizer・native10,001,152 parametersから、D0=前回C1教材、D1=first-turn/名前なし/直接回答を含む改訂教材。各1,899,555 Assistant本文+EOT教師、seed42、教師量scheduleを共通にする。凍結済み131のsource/config/データ/rawは変更せず、新しいrun/data/configに分離する。今回のrecipe変更全体を比較し、個別原因の因果効果とは主張しない。

第一比較の累積GPU上限は21,600秒。probe600・resume600・D0学習3,600・D1学習3,600・全評価10,800・条件付き保持2,400秒を初案とする。新しい長さ/件数で実測予測し、収まらなければ本学習前に止める。旧runを再起動せず、新しい独立seedの証拠にも数えない。GPU使用の実台帳を作成するまでGPU作業は0。

D1のTRAIN設計を先に固定し、実体と内容確認を終えてから未使用DEVを作る。旧DEV/今回見た失敗回答はTRAINへ転用しない。各保存点B/3・2B/3・Bの固定80、無抑制80、自己生成24family59turn、新旧suiteの全内容と同一target本文/EOT NLLを確認する。原品質条件と生のEOS/EOT・反復・Unicode失敗を保持する。

誤履歴回復は正しい提供履歴で改善を確認した場合だけ別比較する。条件が成立しなければ未実行・未確認と記録する。padding効率は教師順・更新group・LR・mask・全state再開の同等性を先に検証し、品質比較へ混ぜない。独立seed43、人間blind、fullDEV/TEST、採用、量子化、外部公開/pushは今回の範囲に含めない。

現在の実確認: Windows Git開始HEAD `a2b7608`、worktree clean。WSL boot `4052bfc5-3850-44e4-9123-d34a9e19f36e`、元UI実PID198864、HTTP親SHA `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`・10,001,152 parameters・busy=false、競合学習jobなし。GPU RTX4090 24,564MiB中978MiB、Linux data空き874GiBは開始時の観察で、将来の生存証拠ではない。

教材作成・CPU確認・学習・全内容評価・品質達成を区別し、実証が揃うまで段階4完了やモデル採用を宣言しない。
