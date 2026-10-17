# 元10B BaseモデルのローカルWebUI

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

元の10B Baseで文章の続きを試すUI。正式採用Base/Chatではなく、不採用の最新RDrop候補へ置き換えていない。URLは[http://127.0.0.1:7860](http://127.0.0.1:7860)。

RDrop終了記録の観測2026-10-16T15:06:52.7804980Z（JST10月17日）では、科学WSL PID459024/start80531912とWindows32704は終了。元UIはPID459564/start80610052、boot4052bfc5-3850-44e4-9123-d34a9e19f36e、元10B親/Tokenizer/native10M・idle HTTP・kernel FLOCK一致で復帰済み。これは時点付き証拠で現在の生存保証ではない。今回の文書作業ではHTTP/生成/再起動を行っていない。

## 操作

Windowsのproject rootから状態を確認する。

```powershell
Invoke-RestMethod http://127.0.0.1:7860/api/model
```

停止中で実process/lockの競合もない場合だけ起動する。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/start_webui.ps1
```

停止が必要な操作時はscripts/stop_webui.ps1を使用。稼働中の重複起動、旧学習runnerの起動、候補重みへの無断差替えをしない。Git cloneにはcheckpointがないため、欠損時は[引継ぎ](windows_handoff.md)の手順を使う。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="使い方"></a>
<a id="保存と確認結果"></a>
<a id="更新前の本文契約当時の記録"></a>
<a id="起動停止"></a>
