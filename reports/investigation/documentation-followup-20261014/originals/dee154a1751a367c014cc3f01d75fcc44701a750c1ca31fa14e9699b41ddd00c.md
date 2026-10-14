# 現在のチェックリスト

2026-10-14 現行: [結果141](141_chat_lr_comparison_results.md)でLR1件の選定・小28セット/6,132判断/NLL7点・小state/台帳/採否監査と7条件分岐を完了、不採用。20件の最終CPU改変拒否確認も通過。作作業は文書の最終整合、小小report/raw/notesの保存一覧、Windows/WSL byte照合、ローカル結果/納品commitと完了監査。これらが終わるまでgoalはactive。保持/独立学習seed43/人間blind/fullDEV/封印TEST/採用は候補なしで未実行・品質未確認。追加研究・GPU・教材・別LRは開始しない。以下は前回の閉じた比較のチェック履歴。

最終更新: 2026-10-13 JST。[状態](autonomous_status.md)、[最新結果138](138_chat_semantic_diversity_results.md)、[計画135](135_chat_problem_solution_plan.md)末尾を正とする。**今回6段階の比較は完了・不採用で閉鎖。追加研究・準備・診断・評価・学習は停止する。** チェック印は証拠への案内で、独立した品質合格の証拠ではない。

## 固定方針

native10,001,152 parameters、既存9.5M〜10.1M予算、日本語Base目標と原品質基準を維持する。大型化や対象縮小で完成扱いにしない。Base/Chatは未完成・未採用、Base単独原因と10M容量限界は未確定。

## 最新の閉じた比較135・6段階

- [x] S0を最新D1歴史stateとして照合、新教材候補S1を1件だけ同親・同条件・登録B・原gateで凍結。
- [x] TRAIN41,529 target/660,109教師/周、280sample QA最終誤り0と修正前の失敗を保存。小TRAIN認証ではない。
- [x] TRAIN凍結後の新DEV80/24会話59turnと既知2回帰、固定NLL2,554 targetを分離して登録。TEST未使用。
- [x] 有限CUDAと小state保存再開25検証更新、小評価の時間gateを確認。本学習3,646更新/1,899,557教師、小3state/実消費列を監査。
- [x] 小21suite/4,599理由付き内容判断/NLL7点、最終t3小原gateとfamily paired CIを監査。不合格・不採用。
- [x] 保持/sampling分岐を候補なしで未実行・passed=false・品質未確認と記録。回復/効率を加えない。
- [x] CPU gate拒否確認20件、終端process/元10B UI/kernel lock、GPU2,443.006571秒/21,600秒を科学監査。
- [x] 結果138、小小report/notes/raw/metadata/文書を保存し、ローカルcommitで停止。push/公開なし。

証拠: [completion](../reports/phase7/chat-semantic-diversity-20261013/completion.json)、[selection](../reports/phase7/chat-semantic-diversity-20261013/selection.json)、[branches](../reports/phase7/chat-semantic-diversity-20261013/conditional_branches.json)、[保存一覧](../reports/phase7/chat-semantic-diversity-20261013/final_archive.json)、[納品確認](../reports/phase7/chat-semantic-diversity-20261013/final_delivery_checks.json)。科学監査と文書納品の記録を区別する。

## 閉じた旧比較と未再開の案

133は[136](136_chat_generalization_results.md)で小14suite/3,066判断/NLL7点を完了・不採用。旧動的paddingは24検証更新の数値差で不採用。各旧runと準備/失敗証拠を保小し、終了job・採点・NLLを繰り返さない。

次介入は135末尾の提案のみ。既存証拠からBase復旧124か限定SFT最適化の候補最大1件を、別の明示再開・新契約/予算で選定する。追加周回・中間点救済・LR探索・新教材を自動実行しない。Base復旧では必要な証拠を満たしたBaseで通知・停止。

## 正式完成まで未確認

- [ ] fresh学習seed43。生成乱数変更やCPU準備で代用しない。
- [ ] 独立人間blind評価、独立corpus監査。
- [ ] 正式保持、有資格sampling、fullDEV/小400生成＋長文40/最終継続suite。
- [ ] 選定封印後のprotectedTEST、原品質/保持条件・正式採用・再現/復旧記録。

比較完了・非blind判断・技術gateを上記の完了へ読み替えない。量子化・20B/50B・push/公開は別の明示判断で今回範囲外。更新前文書は[履歴baseline](../reports/phase7/chat-semantic-diversity-20261013/documentation_history/baseline.json)に保小した。
