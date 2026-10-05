# 物語20%・低学習率と学習量比較の実行計画

2026-10-05 JST。ユーザー「4まで進めて」により[提案51](51_story10_judgment_and_next_proposal.md)を再開する。段階1〜4は以下の条件分岐で実施し、判断・報告・local commit・元final10B UI復帰で停止する。旧停止境界は履歴で、完了済みjobを再実行しない。

1. 元final10Bから物語20%・peak LR0.0001/floor0.00001を追加100,007,936 tokens学習する。元weights/Adam/RNG/Web cursor、context1024、batch32、BF16/Flash/compile、stable2900/decay152を保つ。物語19,988,480/Web80,019,456で既存25,000,067-token poolを一周せず使用する。保存済み同LR Web100M対照を再利用し、旧0.0002対照とは混同しない。科学100Mと実CUDA保存再開検証262,144は別会計。GPU上限900秒。
2. 同じdev256/固定80 greedy64/基本意味192/JBLiMP331/JCommonsenseQA dev1119を比較し、全80をCodexが実際に内容診断する。原EOS差8件・反復非悪化・raw失敗0・BPB対照比+1%・句読点だけの停止禁止に加え、一貫性2点差8件とpaired95%下限>0を保つ。全条件通過時のみ候補と未測定の同LR Web対照を全文dev89,416/固定400/長文20prefix128・512で測る。元親全文BPB+0.001以内の基準は不変。追加GPU上限3,000秒、保存結果を再利用して累積予算を守る。
3. 全条件を通過した場合のみ、同じ元親からWeb/物語20%各500Mの学習量比較へ進む。減衰済み100M枝は再加熱せず、固定poolと共通scheduleの100M中間/500M終端を比較する。物語約100Mを消費するためpool約120Mを目標に必要分だけ準備し、出所・量・反復回数を開始前に明記する。source不足時は反復または追加sourceを別仕様として記録し、unique量を偽らない。予算・config・再開検証を500M開始前に凍結する。100M未達なら小さい配合/LR探索を増やさず、段階4で学習量不足を直接調べる診断比較か内容変更の次案を結果から選ぶ。
4. 生成品質・本文BPB・日本語診断をまとめ、モデル採否と次案を決める。停止の改善と意味的に適切な完結を区別し、Base/Chat品質や独立人手認証の達成とはしない。報告・証拠・local commitを保存し、元final10B UIへ復帰して停止する。

Pythonはすべてuv管理3.12.7、WSL2/RTX4090で実行する。protected test・Chat・1B/20B/50B・push/publicationは今回の対象外。既存全12.23Bの独立監査・sourceの広域混入確認は未完了のまま記録する。過剰な再走査・旧条件の再学習は行わない。

## 実行状態

段階3・両科学枝の学習完了: Web747.396秒、物語735.280秒、各500,006,912/総10,500,014,080/update320435。物語sourceはWeb400,031,744/short99,975,168、終端SHA f336806bee562cf11fe29506f833deae45de228c4b8acb1b942c7df21c82daac。保存short sampler epoch1/position39074/blocks58558で約1.667周の使用を確認。EOS教師はWeb846,893/short1,105,092で、短文側の密度が高い。各100M中間も保存済み、同じactual Linux174280が起動約25分3秒時点で最初のWeb80生成評価中。科学計1,000,013,824を一つのモデルの累積に合算しない。一次評価・320内容診断・原gate条件付き全文・段階4は未完了。

段階3のWeb枝500M学習完了: 追加500,006,912科学tokens/15259更新、総10,500,014,080/update320435、学習747.396秒。終端checkpoint SHA d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4、100M中間も保存済み。同じactual Linux174280が起動約13分5秒時点で物語20%枝400更新を学習中、stderr空。両枝の評価は後続なのでWeb500MのBPB・生成品質は未測定。完了した実結果と未完了の物語学習/320内容診断/全文条件判定/段階4を分ける。[判断53](53_story20_low_lr_judgment.md)は途中原稿。

段階3の科学比較を永続起動: 準備commit742ec45、2026-10-05 00:56:22.906739Z開始、hidden Windows33908 / actual Linux174280 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4498545。actual processの存在を確認し、`screen-job.json`とWindows`screen.*.log`を追跡する。UI停止済みで、launcher finallyが元final10Bへ復帰する。現在CUDA保存再開確認段階、科学学習・320内容診断・条件付き全文・段階4判断は未完了。起動済みjobを重複起動しない。

段階3データ準備完了・500M条件凍結: 固定4 train filesを使い切り、59,963,449 tokens / 662,857文書 / 125,613 parent groupsを194.534秒で構築した。120M目標は未達、source exhaustedを記録し、99,975,168物語input tokensには約1.66727周を使用する。新規unique100Mとは主張しない。各file先頭10採用文書、計40全文を確認し、14弱例と非ランダムsample・合成物語・広域重複未確認の限界をcontent-reviewへ保存した。限定比較の既存基準で使用し、完結や意味品質の全件認証とはしない。26関連CPU tests保存済み、config/schemaを凍結しprobe成功。実科学GPUは起動前。各500,006,912科学tokens、計1,000,013,824、100,007,936中間地点を共通14500 stable/759 decay scheduleで保存する。中間100Mは共通scheduleのstable中で、旧減衰済み100Mとの純粋な量だけの比較ではない。一次GPU上限4,200秒、条件付き全文3,000秒。次は永続起動とactual identity保存、320内容診断、原gate条件付き全文、段階4判断・報告・local commit・元UI復帰で停止。

段階2完了・合格: 全文BPBは候補0.952080669620、同LR Web0.945960821011、元親0.954018472798。候補は元親より−0.001937803179、同LR Web比約+0.647%で、原BPB両条件を通った。全400は候補EOS127/反復45/raw0、Web6/126/raw0。候補長文128/512各20はEOS9/9・文再出現8/8・4gram反復0.473527/0.585897・raw0。全文/長文GPU1,940.030秒、原条件と共通scoring protocolを実保存データから確認するCPU30項目成功。科学143237/全文143904は終了し、元UI復帰を確認した。Base/Chat品質・独立人手blindの達成とはしない。

条件付き段階3を開始: データ準備の最初の複合起動コマンドは自動実行ポリシーにより拒否された（詳細理由なし）。起動を専用`prepare_story20_budget.ps1`へ分け、同じ許可範囲の直接実行で成功した。2026-10-05 00:46:47Z開始、hidden Windows21332 / actual Linux173735 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4440874。CPU builderのjobは`~/jmicro-data/phase6/simple-stories-ja-budget-20261005/job.json`。140.649秒時点でsource1,564,922行/44,931,893 tokensまで構築した。固定source4 train filesを必要分だけ使い、120Mへ届かなければ実量とepoch再利用を学習前に明記する。26関連CPU tests成功（1.81秒）；500M config未凍結・科学GPU未開始。

以下は途中の準備・実行履歴。

段階1完了: 100,007,936 tokens/update308228/総10,100,015,104、物語19,988,480/Web80,019,456、一周なし。学習159.277秒・一次GPU262.543秒、実CUDA25checks/検証262,144別会計。80件の内容診断は文法2点66/関連性2点15/一貫性2点12/適切完結12、EOS23/反復22/raw失敗0、dev256 BPB0.984032485。同LR WebのBPB0.977459052に対して+0.672501%で原一次基準以内。一貫性対照差12/80、paired95%区間[0.075,0.2375]で原内容条件も通過。基本意味65.104%/両文脈31/96、JBLiMP74.924%/常識34.406%。対照差は基本意味+4.167pp（区間+0.521〜+8.333）、常識+3.217pp（+1.072〜+5.183）；一seed/dev診断で広範な理解や独立人手品質の達成とはしない。

段階2全文/長文を2026-10-05 00:11:52Zに起動。hidden Windows30472 / actual Linux143904 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe、start_ticksは`reports/phase6/story20_low_lr_full_launch.json`のactual identityに保存。Linux同runの`full/full-job.json`、Windows`full.stdout.log`/`full.stderr.log`を追跡する。追加科学学習0、同LR Web対照の全文も初回測定し、元親全文は再評価せず保存済み結果を使う。合格するまで500Mを開始しない。

途中保存の実測: 同LR Web全文BPB0.945960821（dev89,416/164,344,743 bytes）、固定80はEOS0/反復59。長文128/512は各20件・EOS0/0、文再出現12/13、文字4gram反復率0.819828/0.953841。2026-10-05 00:30:17Zには同じactual Linux143904が候補全文47,104/213,432 windowsを処理中。ジョブheartbeatが長文中に止まっていても、actual processと保存済み40件の結果で進行を確認した。最終原gate判定はまだ未確定。

条件付き段階3の実装準備: 元親から各500,006,912 tokens/update320435/総10,500,014,080、common stable14500/decay759・peak0.0001/floor0.00001、100,007,936地点の中間checkpointを保存する学習/一次評価経路を準備。両枝を学習し終えてから中間/終端を評価し、評価が後続学習RNGへ影響しない順序とする。新poolを最大120M目標に同じ固定public train source/選別条件で構築するbuilderは、全文reviewの合格を開始条件に持つ。sourceを使い切って目標未達なら実量と必要epoch再利用を記録し、unique増量を偽らない。4つの新関連checksを含む24 CPU tests成功（3.30秒）。500M configは未凍結、データ構築/取得・500M GPUは未開始。実行が必要になった場合だけ実data検査・config/予算凍結・実CUDA保存再開へ進む。

2026-10-05 00:05:25Zに永続起動。準備commitca5dac0、hidden Windows30420、actual Linux143237 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4192785。Linux`reports/phase6/story20-low-lr-10b-100m-20261005/screen-job.json`とWindows同名folderの`screen.stdout.log`/`screen.stderr.log`を追跡する。launcherはfinallyで元final10B UIへ復帰する。以下は起動前の確認記録。

専用runner/config/schemaを凍結した。20関連CPU tests成功（1.78秒）、CPU上で元親checkpointの実SHA/finite state/update/tokens/batch/context/implementationと凍結source/参照を確認済み。実process確認では既存UI140800のみ、旧科学jobは終了。4090はdriver616.92、GPU使用2%/VRAM881MiBで推論待機中。科学GPUはまだ開始していない。準備commitを保存し、永続launcherがUIを停止して実CUDA保存再開→100M学習/一次評価を行い、finallyで元UIへ戻す。
