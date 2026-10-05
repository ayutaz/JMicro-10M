# 物語20%・低学習率と学習量比較の実行計画

2026-10-05 JST。ユーザー「4まで進めて」により[提案51](51_story10_judgment_and_next_proposal.md)を再開する。段階1〜4は以下の条件分岐で実施し、判断・報告・local commit・元final10B UI復帰で停止する。旧停止境界は履歴で、完了済みjobを再実行しない。

1. 元final10Bから物語20%・peak LR0.0001/floor0.00001を追加100,007,936 tokens学習する。元weights/Adam/RNG/Web cursor、context1024、batch32、BF16/Flash/compile、stable2900/decay152を保つ。物語19,988,480/Web80,019,456で既存25,000,067-token poolを一周せず使用する。保存済み同LR Web100M対照を再利用し、旧0.0002対照とは混同しない。科学100Mと実CUDA保存再開検証262,144は別会計。GPU上限900秒。
2. 同じdev256/固定80 greedy64/基本意味192/JBLiMP331/JCommonsenseQA dev1119を比較し、全80をCodexが実際に内容診断する。原EOS差8件・反復非悪化・raw失敗0・BPB対照比+1%・句読点だけの停止禁止に加え、一貫性2点差8件とpaired95%下限>0を保つ。全条件通過時のみ候補と未測定の同LR Web対照を全文dev89,416/固定400/長文20prefix128・512で測る。元親全文BPB+0.001以内の基準は不変。追加GPU上限3,000秒、保存結果を再利用して累積予算を守る。
3. 全条件を通過した場合のみ、同じ元親からWeb/物語20%各500Mの学習量比較へ進む。減衰済み100M枝は再加熱せず、固定poolと共通scheduleの100M中間/500M終端を比較する。物語約100Mを消費するためpool約120Mを目標に必要分だけ準備し、出所・量・反復回数を開始前に明記する。source不足時は反復または追加sourceを別仕様として記録し、unique量を偽らない。予算・config・再開検証を500M開始前に凍結する。100M未達なら小さい配合/LR探索を増やさず、段階4で学習量不足を直接調べる診断比較か内容変更の次案を結果から選ぶ。
4. 生成品質・本文BPB・日本語診断をまとめ、モデル採否と次案を決める。停止の改善と意味的に適切な完結を区別し、Base/Chat品質や独立人手認証の達成とはしない。報告・証拠・local commitを保存し、元final10B UIへ復帰して停止する。

Pythonはすべてuv管理3.12.7、WSL2/RTX4090で実行する。protected test・Chat・1B/20B/50B・push/publicationは今回の対象外。既存全12.23Bの独立監査・sourceの広域混入確認は未完了のまま記録する。過剰な再走査・旧条件の再学習は行わない。

## 実行状態

段階1完了: 100,007,936 tokens/update308228/総10,100,015,104、物語19,988,480/Web80,019,456、一周なし。学習159.277秒・一次GPU262.543秒、実CUDA25checks/検証262,144別会計。80件の内容診断は文法2点66/関連性2点15/一貫性2点12/適切完結12、EOS23/反復22/raw失敗0、dev256 BPB0.984032485。同LR WebのBPB0.977459052に対して+0.672501%で原一次基準以内。一貫性対照差12/80、paired95%区間[0.075,0.2375]で原内容条件も通過。基本意味65.104%/両文脈31/96、JBLiMP74.924%/常識34.406%。対照差は基本意味+4.167pp（区間+0.521〜+8.333）、常識+3.217pp（+1.072〜+5.183）；一seed/dev診断で広範な理解や独立人手品質の達成とはしない。

段階2全文/長文を2026-10-05 00:11:52Zに起動。hidden Windows30472 / actual Linux143904 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe、start_ticksは`reports/phase6/story20_low_lr_full_launch.json`のactual identityに保存。Linux同runの`full/full-job.json`、Windows`full.stdout.log`/`full.stderr.log`を追跡する。追加科学学習0、同LR Web対照の全文も初回測定し、元親全文は再評価せず保存済み結果を使う。合格するまで500Mを開始しない。

2026-10-05 00:05:25Zに永続起動。準備commitca5dac0、hidden Windows30420、actual Linux143237 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4192785。Linux`reports/phase6/story20-low-lr-10b-100m-20261005/screen-job.json`とWindows同名folderの`screen.stdout.log`/`screen.stderr.log`を追跡する。launcherはfinallyで元final10B UIへ復帰する。以下は起動前の確認記録。

専用runner/config/schemaを凍結した。20関連CPU tests成功（1.78秒）、CPU上で元親checkpointの実SHA/finite state/update/tokens/batch/context/implementationと凍結source/参照を確認済み。実process確認では既存UI140800のみ、旧科学jobは終了。4090はdriver616.92、GPU使用2%/VRAM881MiBで推論待機中。科学GPUはまだ開始していない。準備commitを保存し、永続launcherがUIを停止して実CUDA保存再開→100M学習/一次評価を行い、finallyで元UIへ戻す。
