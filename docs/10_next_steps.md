# 現在のチェックリスト

最終更新: 2026-10-09 JST。[状態](autonomous_status.md)、[結果123](123_base_teacher_decay_2b_results.md)、[計画124](124_base_recovery_plan.md)を正とする。チェック印は保存証拠の案内であり、それ自体を科学的な証拠とはしない。

## 固定方針

10Mのサイズ維持を最優先に、現10,001,152 parameters・既存9.5M〜10.1Mの予算内で改善する。大型化、品質基準の緩和、対象の無断縮小を解決策にしない。現在の低品質を10Mの容量限界と断定しない。学習・研究実行は再開待ち。

## 直近の完了

- [x] 同じnativeモデル・同じstreamの累積2B教師比較を完了。最終212095更新。
- [x] 実CUDA連続/保存再開15checksを通過。検証8更新/71464教師と科学学習を別計数。
- [x] 固定DEV256本文BPB、日本語評価、全80生成を保存。
- [x] 全80を個別に読み、raw SHA付き非blindレビューを保存。
- [x] BPB改善と文章品質未改善を分け、元基準で不採用・固定条件closedと記録。
- [x] 実science終了、Windows worker exit0、GPU ledger closed、元10B UI復帰を確認。
- [x] 重み・全stateはWSLに保全。小評価/レビュー/完了記録はGitに保存（科学結果commit `a26194c`）。
- [x] ユーザー指示で学習・研究実行を一時停止。

証拠: [completion](../reports/phase6/base_teacher_decay_2b_completion.json)、[全80notes](../reports/phase6/base_teacher_decay_2b_candidate_notes.json)、[science result](../reports/phase6/base-teacher-decay-2b-20261008/result.json)、[終端・停止記録](../reports/phase6/base_teacher_decay_2b_active_job.json)。

## 今回の文書更新

- [x] README・文書一覧・状態・ロードマップ・引継ぎ・AGENTSを最新結果と停止境界へ統一。
- [x] 旧運用文書の全原文を20261008履歴へ保存し、現在の指示と分離。
- [x] 次の比較の選定からBase採用まで、目的・成果物・進行/停止条件・予算の扱いを計画124へ記載。
- [x] 次の介入条件は未選定・新GPU/data/診断は未開始と明記。
- [x] 10M維持・限界判断の留保・再開後の検討順と次案の必須記載事項を関係文書へ反映。

## 明示的な実行再開後

- [ ] 計画124の検討順で既存結果と失敗条件を対応付け、10M内の比較を最大1件選ぶ。主要失敗・既存との差・固定量・全guard・予算・終了条件を記載。根拠不足なら理由を報告して停止。
- [ ] 必要な診断だけを定義・実装し、事前screenで採否を決める。既存診断の再実行を既定にしない。
- [ ] 同教師pilotを実装・凍結し、実CUDA再開gate後に実行する。
- [ ] 全80の生成品質・保持guardで判定し、BPBだけの改善を進行条件にしない。
- [ ] 有望条件のみ実測予算を固定して本比較。失敗時は閉鎖し、一巡の結果を報告して停止。
- [ ] 合格レシピのfresh学習seed43とnative runner/reviewer接続を完成・実行する。
- [ ] fullDEVと全400＋長文40を評価し、全内容を確認する。
- [ ] 選定封印後にprotectedTESTを実行し全100内容と元基準を確認する。
- [ ] Base採用・復旧・成果物がそろったらユーザーへ通知して停止する。

独立人間blind・独立全corpus監査・旧数値7失敗の未完了を隠さない。Chat/SFT/量子化・20B/50B・push/公開へ自動移行しない。旧selector等のチェックリストはGit履歴と当時の結果文書で参照する。