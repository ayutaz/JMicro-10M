# 教材汎化の改善比較・実行記録

## 2026-10-13: 「4まで」の継続実行

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
