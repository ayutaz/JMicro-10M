# 自律runnerの現在の運用

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

## 目標状態と実行範囲

元「4まで」はBase未達のままユーザーが解除。現在の文書目標を旧研究の達成・再開にしない。履歴のrunning/PID/next_actionは日時付き証拠であり起動指示ではない。文書更新で研究・データ/TEST準備・推論・GPU・環境変更・公開を開始しない。

continueは許可範囲の有用な作業が残る状態、needs_userは外部判断が必要な状態、completeは依頼範囲が証拠で完了した状態。技術gate/比較の完了と正式Base採用を分ける。同じ外部障害の3連続goal turn確認はその目標/再開ごとに数える。旧上限でのblocked判定を、新しい累積上限解除後の現在障害へ流用しない。

## 将来の学習運用

新しい比較の前に根拠・全品質・対照・有限の教師/時間/評価保存枠・停止条件を固定。実CUDA最大shape/finite・全state再開・cache・全timingを確認する。長期runはPID/boot/start・logs/checkpoint/heartbeat・GPU/kernel lockを記録し、重複起動を防ぐ。真の中断だけを同一契約/残りrun予算で復旧する。

有効なprocessを観測したwaitは進捗確認。観測timeoutだけでrestartしない。完了・失敗した固定条件を係数/精度/shape/教師/decoder/予算変更で救済しない。元UIの停止はowned学習中のみ、終端で元親へ復帰し実identity/HTTP/lockを確認する。共有log handleをworker生存と混同しない。

## 保存と納品

WindowsがGit正本。全Pythonはuv run --frozenで3.12.7を使う。全重み/Adam/scheduler/RNG/sampler/countersをcompleted updateで保存し、大容量実体はWSL。小raw/個別notes/receiptはhashでWindows/WSL/Gitを照合しローカルcommit。push/公開・他者送信・paid cloudは別の明示指示が必要。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="保存と再開"></a>
<a id="実行範囲と完了を区別する"></a>
<a id="実行範囲と目標状態を区別する"></a>
