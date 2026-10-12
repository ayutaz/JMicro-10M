# 教材汎化・同条件比較・回復分岐・paddingの最終結果

2026-10-13 JST。ユーザーの「4まで進めてください」に対応した4項目の実行と監査を完了した。**改訂教材D1の品質改善は実証できず、D0/D1とも不採用。Base/Chatは未完成・未採用。** [完了監査](../reports/phase7/chat-generalization-20261013/completion.json)、[最終比較](../reports/phase7/chat-generalization-20261013/selection.json)、[全保存点解析](../reports/phase7/chat-generalization-20261013/final_analysis.json)。

## 4項目の到達点

| 項目 | 実施・検証した内容 | 結果 |
|---|---|---|
| 1. 教材の汎化改善 | first-turn・名前紹介なし・直接回答を増やすD1 TRAIN40,126応答、1周660,065 Assistant本文+EOT教師。凍結後に新DEV80familyと自己生成24会話59turnを固定。280sampleの内容QAとCPU消費契約 | 準備と限定QAは完了。独立人間確認・全TRAINの意味品質認証ではない。学習後の汎化改善は実証できなかった |
| 2. 同条件比較 | 同じ元WebUI10B親・Tokenizer・10,001,152 parameters・fresh optimizer・seed42・教師量schedule。D0は一致する旧C1を出典付き再利用、D1は実学習。親とt1/t2/t3の新旧全14セット・3,066内容判断・NLL7点 | 最終点t3の原品質gateは両条件とも不合格。保存/再開・実教師列・消費・全stateの技術監査は通過 |
| 3. 条件付き誤履歴回復 | 最終の新旧内容、正しい提供履歴、機械gate、新内容のD0比改善、自己生成の残る失敗を登録predicateで判定 | 内容・提供文脈・対照比改善を満たさずnot_triggered。回復学習0、効果未確認。条件を緩めて開始しない |
| 4. 別padding比較 | 全BのCPU教師列/更新group/LR一致、GPU固定/動的各8更新、動的連続/再開各4更新、速度・VRAM・全state・数値許容差 | 24確認更新を完了。動的条件内の全state再開は一致、固定との数値gateは不合格で不採用 |

4項目の検証完了はモデル品質の完成ではない。独立学習seed43、人間blind、fullDEV、protectedTEST、正式採用、量子化・公開は実施していない。

## 最終t3の結果

「内容」は既存rubricで文法・関連性とも2。「自己生成文脈」は実際の先行Assistant応答を含む会話の最終turnが文脈2を満たす数。「提供文脈」は同じ24 IDの正しい提供履歴での文脈2。Codex非blindによる理由付き判断で、独立した人間の評価ではない。

| 指標 | D0 新 | D1 新 | D0 旧 | D1 旧 | 元の条件 |
|---|---:|---:|---:|---:|---|
| 文法2 /80 | 59 | 62 | 58 | 54 | 単独採否なし |
| 内容 /80 | 16 | 12 | 18 | 15 | 新旧それぞれ56以上 |
| 自己生成文脈 /24 | 5 | 3 | 4 | 1 | 新旧それぞれ15以上 |
| 対応する提供文脈 /24 | 6 | 5 | 4 | 2 | 回復分岐は新旧15以上 |
| 固定自然停止 /80 | 79 | 80 | 79 | 79 | 新旧それぞれ76以上 |
| 自己生成自然停止 /59 | 55 | 59 | 57 | 59 | 新旧それぞれ57以上 |
| 固定反復 /80 | 1 | 0 | 1 | 1 | D1はD0より増えない |
| 自己生成反復 /59 | 4 | 0 | 3 | 0 | D1はD0より増えない |

最終の空応答・role token漏れ・raw Unicode破損・履歴削除は新旧の固定/自己生成で全0。D1は機械的な停止と反復非増加を通るが、内容と文脈が未達。文法のよいD1新62件のうち50件、旧54件のうち39件が関連性2未満だった。

D1−D0の内容率差は新−5.0ポイント（family paired95%CI −15.0〜+6.25）、旧−3.75ポイント（−12.5〜+5.0）。自己生成文脈差は新−8.33ポイント（−25.0〜+8.33）、旧−12.5ポイント（−29.17〜+4.17）。すべて0を含み、改善は実証されない。点推定だけで一般的な悪化の統計的確定も主張しない。保存点や59turnを独立family数へ加えず、自己生成24は提供80の部分集合として扱う。

## 学習量・NLLと汎化

D0は歴史的に一致する3,636更新・1,899,555教師を再利用し、新学習0。D1は3,641更新・1,899,562教師を実学習した。終端超過7は事前の完全応答0〜64規則内で、完全な教師数一致ではない。親・Tokenizer・教師量schedule・seed・モデル構成は同じで、教材recipe全体の比較。個々のfirst-turn追加だけの因果効果とは呼ばない。

D1最終checkpoint SHA `aa84a1dc3fbbf1c264ebd9327ecc7183bf3d88c606e01bd0f82bb5351945aed6`。[全state監査](../reports/phase7/chat-generalization-20261013/D1/training_audit.json)、[t3実教師列・cursor監査](../reports/phase7/chat-generalization-20261013/D1/t3_audit.json)でmodel/Adam/scheduler/RNG/sampler、有限metrics、全更新の教師数/LR、実padded列digestと最初の閾値到達更新を確認した。

| 同じ固定targetでの指標 | 親 | D1 t1 | D1 t2 | D1 t3 |
|---|---:|---:|---:|---:|
| D1 TRAIN本文平均NLL（112target） | 3.148497 | 0.004231 | 0.004050 | 0.001136 |
| 新DEV本文平均NLL（80target） | 3.058625 | 4.084001 | 4.272016 | 4.818918 |
| RPC DEV本文BPB（2,250target） | 1.351262 | 1.677399 | 1.808632 | 1.943257 |

[固定NLL最終原記録](../reports/phase7/chat-generalization-20261013/NLL/D1/t3.json)。全保存点でD0 TRAIN112・D1 TRAIN112・新DEV80・RPC DEV2,250の同じ2,554targetを用い、本文/EOTを分離した。分母の教師数・bytes・target順と数学的なtotalも監査した。TRAINへの適合に対し未知DEVでの損失が増え、汎化不足と分布差が優先課題。固定TRAIN標本から全TRAINの暗記や単独原因は確定しない。RPCのChat形式BPBは正式なBase保持suiteの代替ではなく、保持合格も忘却の確定も主張しない。

## 内容失敗の具体例

以下は最終の原rawと理由付きnotesで確認した例。正解単語一致による自動採点は行わず、別の自然な回答もrubricに従って認めた。

| 種類 | 実際の条件 | D1最終の返答・失敗 |
|---|---|---|
| 否定・話者混同 | 担当は私ではなく姉 | 「担当はあなたです。」と否定条件を反転 |
| 古い値への回帰 | 六枚を九枚へ訂正した自己生成会話 | 「六枚持っていくのは六枚です。」と古い数量へ戻る |
| 誤自発話の持越し | Userは叔母から叔父へ訂正。モデルは先に正人さんを作った | 「届ける相手は正人さんです。」と自身の誤答を保持 |
| 複数条件の不足 | 果物は梨のまま、飲み物を水へ変更 | 「最後の組合せははさみです。」と未提示の物を生成 |
| 汎用の受領だけ | 会う場所の駅前を再回答する依頼 | 「承知しました。」で具体的な質問に答えない |
| 感情の反転 | 約束延期を残念に感じている | 「それは楽しみですね。」と感情を逆にする |
| 好み・禁止の反転 | コーヒーが苦手で紅茶が好き | 「楽しめるのはコーヒーです。」と逆に返す |

[新DEV全判断](../reports/phase7/chat-generalization-20261013/evaluation/D1/t3/new/greedy/notes.json)、[旧DEV全判断](../reports/phase7/chat-generalization-20261013/evaluation/D1/t3/old/greedy/notes.json)。最終新95・旧83件の未判断回答を明示的に読み、残りは実履歴・raw IDs/bytes・prompt・checksが完全一致する判断だけを出典付き再利用した。各219件のrawと判断を保持する。

新DEVの分類別内容は挨拶3/8・日常3/8・感情0/8・質問への回答1/8・曖昧さ0/8・話者0/8・記号0/8・訂正2/8・後続0/8・文脈3/8。各8例の記述で広い能力の精密な推定ではない。[全分類と実履歴解析](../reports/phase7/chat-generalization-20261013/final_analysis.json)を参照する。

## 条件付き分岐・効率の判断

[分岐監査](../reports/phase7/chat-generalization-20261013/conditional_branches.json)では回復の機械gateと自己生成の残る失敗は成立したが、新旧内容56、提供文脈15、新内容のD0比改善が不成立。回復はnot_triggered、教師量20%置換を開始せず効果未確認。合格候補がないため保持・3seed samplingも登録条件による省略で、passed=false・quality_unconfirmed=true。

[padding結果](../reports/phase7/chat-generalization-20261013/padding/result.json)は固定/動的8更新ずつと動的連続4/保存再開4の24確認更新。warm-up2更新を除く教師速度は1,164.257対6,484.277 tokens/秒（約5.57倍）、peak allocated16,223,183,360対1,202,441,216 bytes。全B CPUではphysical入力163,577,856対10,562,871。しかしupdate2/3のloss差0.000953674/0.001758337が事前上限2e−6を超え、最初の3更新の勾配・重みもrtol2e−4/atol2e−7を満たさず不採用。短い速度実測から長期品質や速度を保証しない。main D1は固定paddingのまま。

## 完了監査と保存・停止

[完了command](../scripts/complete_chat_generalization.py)は全raw-boundレビュー/NLL、最終選定・paired CI、登録回復predicate、実checkpoint/metricsへのaudit binding、paddingの実保存/再開stateとloss差、台帳の非重複・個別/総枠・失敗保存、元UIの実identity/HTTP/lockを確認した。[20件のCPU確認](../reports/phase7/chat-generalization-20261013/completion_gate_checks.json)では不正な合格数・候補、NLL ID/分母/非有限/mean、歴史的消費改変・失敗削除・未登録config・job重複・枠増加を拒否し、自己生成23/24でも他の条件が通れば回復条件になる境界を確認した。新しいGPU品質確認ではない。

新completion observerの初回では歴史的台帳SHAを現configと誤って同一視し、次に再利用jobへ新PIDを要求する不備を検出した。[初回失敗](../reports/phase7/chat-generalization-20261013/completion_audit_initial_incident.json)、[job schema失敗](../reports/phase7/chat-generalization-20261013/completion_audit_historical_job_incident.json)。元台帳・採点・凍結sourceは変更せず、旧config/失敗予測/再配分履歴と元3entryの完全一致、再利用元の終了jobへ厳密につなぐobserverを修正し、完了監査を通した。

累積GPUは2,117.569秒（35.293分）/21,600秒上限。D1本学習1,373.630、評価694.437、probe10.428、resume18.411、効率20.662秒。D0新学習・保持・回復0。最初の失敗予測12.108秒も評価枠に含め、再配分前の3entryと元configを保存した。再学習や終了済みpaddingの再実行は行っていない。

元10B WebUIは完了監査時に実PID235826、boot `4052bfc5-3850-44e4-9123-d34a9e19f36e`、start_ticks47993707、元親/Tokenizer/10,001,152 parameters、busy=falseをHTTPと実process/lockで確認。将来の生存保証ではない。[保存一覧とbyte照合](../reports/phase7/chat-generalization-20261013/final_archive.json)に小記録を残し、重みと教材実体はWSLに保全する。

**この比較を不採用として閉じ、追加の研究・教材準備・GPU診断・学習を停止する。** 次は[計画135](135_chat_problem_solution_plan.md)の意味構造の多様性を広げる教材比較を最大1件として提案し、明示再開を待つ。Base復旧を選ぶ場合は[124](124_base_recovery_plan.md)のBase-only境界を守る。10M容量限界、Base単独原因、単純な学習量不足のいずれも断定しない。
