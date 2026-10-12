# 現在のチェックリスト

最終更新: 2026-10-13 JST。[状態](autonomous_status.md)、[最新結果136](136_chat_generalization_results.md)、[現行提案135](135_chat_problem_solution_plan.md)を正とする。チェック印は証拠への案内で、品質合格の独立証拠ではない。現在は文書・計画のみを更新し、研究・教材準備・GPU診断・学習は停止中。

## 固定方針

10,001,152 parameters、既存9.5M〜10.1M予算と日本語Base目標を維持する。大型化、対象の無断縮小、原品質基準の緩和を改善の既定手段にしない。Base/Chatは未完成・未採用、10M容量限界は未確定。

## 最新の閉じた比較133

- [x] D1 TRAIN40,126応答/660,065教師/周の凍結と280sample QA、新DEV80/自己生成24会話59turnを固定。全TRAIN/独立人間の認証とは別。
- [x] CUDA有限性・全state保存再開・同条件対照D0の歴史的再利用を確認。
- [x] D1を3,641更新/1,899,562教師まで実学習し、最終全state・実教師列・消費を監査。
- [x] 親＋D0/D1の全14評価セット、3,066理由付き内容判断、固定NLL7点を完了。
- [x] 最終新旧gateとpaired CIを判定。D0/D1とも不合格、不採用で閉鎖。
- [x] 回復predicateを原条件で監査しnot_triggered。保持/samplingも候補なしで未実行・品質未確認と記録。
- [x] 別padding24GPU確認更新を完了。動的内再開は一致、固定との数値不一致で不採用。
- [x] 失敗を含むGPU台帳2,117.569秒/21,600秒、終端process、元10B UI復帰を完了監査時に確認。
- [x] 重み/全state/教材はWSL、評価metadata/raw/全notes/文書をGitに保存。結果commit `ed3aa29`、追加実行停止。

証拠: [completion](../reports/phase7/chat-generalization-20261013/completion.json)、[selection](../reports/phase7/chat-generalization-20261013/selection.json)、[branches](../reports/phase7/chat-generalization-20261013/conditional_branches.json)、[保存一覧](../reports/phase7/chat-generalization-20261013/final_archive.json)。過去の未完了チェックや学習中PIDを現在の残作業へ戻さない。

## 今回の文書更新で確認するもの

状態・ロードマップ・引継ぎ・AGENTS・README・文書一覧・計画135/124を最終結果と停止範囲へ統一する。旧14文書をbyte一致で保存し、最終数値・未確認分岐・提案/実績の区別、ローカルリンク、WSL文書同期、凍結証拠/実装非変更、Git保存を検証する。[履歴baseline](../reports/investigation/documentation_plan_refresh_20261013/baseline.json)。検証結果は同directoryのverificationに保存する。文書確認はGPU/model品質確認ではない。

## 明示再開後だけ行う次比較案135

- [ ] 対照D1と候補1件、意味構造の多様性という変更、同親・seed42・B=1,899,555教師、原guard、新runと予算の契約を具体化。
- [ ] 新TRAINの意味family/正解根拠QA・凍結後、新未使用DEV80/自己生成24を固定。既知DEV2suiteを回帰に残す。
- [ ] 変更経路/対照再利用/技術gate/専用runnerと全必要評価時間を確認してから本学習。
- [ ] 親と両条件3保存点の21セット/4,599内容判断と共通固定NLLを全確認。これは次比較の予定量で、実施済みではない。
- [ ] 最終Bの新未使用内容改善・全原gate・回帰・反復を判定。有資格候補だけ登録保持/sampling、不成立は未実行・未確認。
- [ ] 比較の採否・raw失敗・予算・元UI復帰を保存し、報告して停止。新条件や追加周回へ自動移行しない。

回復と新効率方式は別契約・別予算。Base復旧を選ぶなら[124](124_base_recovery_plan.md)の段階0〜5へ分岐し、Base完成で通知・停止する。

## 正式完成まで未確認のもの

- [ ] 独立fresh学習seed43。生成seedを変えるだけでは不可。
- [ ] 独立した人間blind評価、独立corpus監査。
- [ ] native形式の必要なrunner/reviewer接続、fullDEVと全400生成＋長文40、最終継続suite。
- [ ] 選定封印後のprotectedTEST、原品質/保持条件と正式採否、再現・復旧記録。

既存CPU準備、学習終了、非blind判断を上記の完了へ読み替えない。量子化・20B/50B・push/公開は別の明示判断で、今回の範囲外。
