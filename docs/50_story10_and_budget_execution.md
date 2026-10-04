# 配合10%・学習量比較の実行

2026-10-05 JST。ユーザー「3までを進めて判断をして提案をしてください」により[計画49](49_next_mixture_and_training_budget_plan.md)の段階1〜3を再開した。まず物語10%の各100Mと同条件保存対照を比較する。原採用条件を全て通る場合、同じ親からWeb/物語10%各500Mの学習量比較へ進む。未達なら計画の低LR同量比較を一つ定義して実施し、結果に基づく判断・次案の報告/local commit・UI復帰で停止する。1B/20B/50B/Chat/test/pushは今回は提案のみで開始しない。

## 段階1の固定条件

親は元final10B SHA410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290。同じmodel/Adam/RNG/Web cursorから明示fork。100,007,936追加tokens/3,052 updates、物語305 updates=9,994,240 tokens、Web90,013,696、実配合9.993%。既存25,000,067-token物語poolを使用し、新source/filter/長さは変更しない。peak LR0.0002、stable2900/decay152、floor0.00002、context1024/batch32/BF16/Flash/compileは前回と共通。終端総10,100,015,104/update308228。

新専用`run_story10_comparison.py`/`.ps1`とconfig/schemaを作成する。以前の凍結runner・scorer・モデル・評価suiteは変更しない。Web100%/物語20%の学習・評価・内容採点は保存結果を再利用する。必要な10%ルート/共同選定条件のCPU testsと実CUDA8updatesの保存再開だけ確認する。検証262,144 tokensと科学100,007,936 tokensは別会計。

一次dev256/固定80/意味192/JBLiMP331/JCQA1119と80件Codex内容診断を行う。原EOS・反復・BPB・raw条件と一貫性差8件以上・paired95%下限>0を保持する。事前条件を通る場合だけ候補の全文89,416/固定400/長文20prefix128・512を一度測る。Web全文対照も保存済み結果を明示再利用する。全文BPBは親0.9540184727984398＋0.001以内、原条件は不変。Codex内容診断は独立人手品質合格に代入しない。

一次GPU上限900秒、条件付き全文/長文1,800秒。旧run失敗・raw・失敗gateは保持する。GPU実行前にactual process/lockを確認し、UIを一時停止・finallyで元final10Bへ戻す。runはLinux`reports/phase6/story10-10b-100m-20261005`、process PID/boot/start_ticks/checkpoint/log/sourceを永続保存する。CPU/data準備時間とGPU計算時間は別。

## 段階1の起動記録

準備local commit70304d6、関連14 CPU tests成功。専用config/schemaを凍結し、2026-10-04 16:13:58Z（JST10月5日01:13）にhidden Windows34152を起動した。actual Linux139467 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks1364277を確認。`screen-job.json`、Windows`screen.stdout.log`/`screen.stderr.log`、各checkpoint/metricsへ永続保存。実CUDA保存再開を終え、800updates時点で実process継続と約695k tokens/sを確認した。UIはこのGPU処理中だけ停止し、launcher finallyで元final10Bへ復帰する。科学終端・一次評価・80内容診断と条件付き評価はまだ未完了で、重複起動しない。

## 段階2と最終判断（次の条件付き作業）

### 段階1結果と分岐

物語10%の科学100,007,936 tokensを159.118秒で学習、一次評価込みGPU264.370秒。14関連tests、実CUDA25項目保存再開、保存state・raw80・全80Codex内容診断の確認が成功。[一次結果](../reports/phase6/story10_100m_result.json)、[内容・証拠確認](../reports/phase6/story10_100m_review.json)。dev256 BPB0.984584、固定EOS17/80、反復40/80、raw Unicode/empty/role0。元mixture五条件は全て通ったが、Codex一貫性2点4/80はWeb0からの差が8件に達せず、事前内容条件を満たさない。文法2点41、関連性2点15、適切な完結4/80。内容差95%区間[0.0125,0.1]でも改善幅の条件は不変。意味・統語・常識の差は全て95%区間が0を含む。

全文BPBの親悪化条件はこの枝で未測定。一次内容条件が未達なので、全文/長文を実行せず、500Mへ進めない。科学Linux139467は終了し、UIは元final10BでHTTP応答を確認した。100Mから十分量・容量上限を断定しない。

計画49の失敗時分岐に沿い、同じ10%を保った低LR同量比較を一つ凍結した。peak0.0001→floor0.00001、Web/物語各100,007,936追加tokens、同じfinal10B親・stable2900/decay152・Tokenizer/model/pool/evaluation/gates。科学合計200,015,872、実CUDA検証262,144は別。元LRのWeb対照を低LR対照へ流用せず、二枝とも新たに学習する。16関連CPU tests成功。新config/schema/専用runner・launcherを使用し、一次GPU上限1,800秒、条件を通る場合のみ両枝全文/長文3,000秒。これを終えて段階3の判断/提案とlocal commit・UI復帰で停止し、追加の混合率/LR/seed探索や500Mを自動開始しない。

段階1の採用結果を確認してから条件を凍結する。通る場合は同じsource/選別の約60M pool、同じ親・同量各500Mと共通LR計画、中間100M/終端500Mの比較、GPU上限7,200秒を定義する。未達なら10%固定・peak LR0.0001のWeb/物語各100Mを一つの別比較として定義し、LR以外の変更を同時に行わない。失敗でも報告と次案を出して停止する。安全条件を緩めて未採用枝を増量しない。十分量・容量上限を断定せず、学習不足仮説と必要なら10B対20Bの次案を残す。
