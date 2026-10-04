# 配合10%・学習量比較の実行

2026-10-05 JST。ユーザー「3までを進めて判断をして提案をしてください」により[計画49](49_next_mixture_and_training_budget_plan.md)の段階1〜3を再開した。まず物語10%の各100Mと同条件保存対照を比較する。原採用条件を全て通る場合、同じ親からWeb/物語10%各500Mの学習量比較へ進む。未達なら計画の低LR同量比較を一つ定義して実施し、結果に基づく判断・次案の報告/local commit・UI復帰で停止する。1B/20B/50B/Chat/test/pushは今回は提案のみで開始しない。

## 段階1の固定条件

親は元final10B SHA410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290。同じmodel/Adam/RNG/Web cursorから明示fork。100,007,936追加tokens/3,052 updates、物語305 updates=9,994,240 tokens、Web90,013,696、実配合9.993%。既存25,000,067-token物語poolを使用し、新source/filter/長さは変更しない。peak LR0.0002、stable2900/decay152、floor0.00002、context1024/batch32/BF16/Flash/compileは前回と共通。終端総10,100,015,104/update308228。

新専用`run_story10_comparison.py`/`.ps1`とconfig/schemaを作成する。以前の凍結runner・scorer・モデル・評価suiteは変更しない。Web100%/物語20%の学習・評価・内容採点は保存結果を再利用する。必要な10%ルート/共同選定条件のCPU testsと実CUDA8updatesの保存再開だけ確認する。検証262,144 tokensと科学100,007,936 tokensは別会計。

一次dev256/固定80/意味192/JBLiMP331/JCQA1119と80件Codex内容診断を行う。原EOS・反復・BPB・raw条件と一貫性差8件以上・paired95%下限>0を保持する。事前条件を通る場合だけ候補の全文89,416/固定400/長文20prefix128・512を一度測る。Web全文対照も保存済み結果を明示再利用する。全文BPBは親0.9540184727984398＋0.001以内、原条件は不変。Codex内容診断は独立人手品質合格に代入しない。

一次GPU上限900秒、条件付き全文/長文1,800秒。旧run失敗・raw・失敗gateは保持する。GPU実行前にactual process/lockを確認し、UIを一時停止・finallyで元final10Bへ戻す。runはLinux`reports/phase6/story10-10b-100m-20261005`、process PID/boot/start_ticks/checkpoint/log/sourceを永続保存する。CPU/data準備時間とGPU計算時間は別。

## 段階2と最終判断

段階1の採用結果を確認してから条件を凍結する。通る場合は同じsource/選別の約60M pool、同じ親・同量各500Mと共通LR計画、中間100M/終端500Mの比較、GPU上限7,200秒を定義する。未達なら10%固定・peak LR0.0001のWeb/物語各100Mを一つの別比較として定義し、LR以外の変更を同時に行わない。失敗でも報告と次案を出して停止する。安全条件を緩めて未採用枝を増量しない。十分量・容量上限を断定せず、学習不足仮説と必要なら10B対20Bの次案を残す。
