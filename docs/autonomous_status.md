# 現在の状態

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

## 完了した検証

- 第一回RDrop科学比較：元10B親/fresh Adam、同25M教師、4,420更新。全型付き状態・全履歴・元主streamを照合済み。
- 全80件の個別内容確認と原採否判定。paired一貫性差+2/80、CI95[0,.0625]、BPB3.5507%悪化で不採用。
- DEV入力の隔離と全文DEV/440 CPU接続部品。後者36 checksは合成fixtureの検証で実品質ではない。

## 未達事項

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

## 実行状態と保存

RDrop終了記録の観測2026-10-16T15:06:52.7804980Z（JST10月17日）では、科学WSL PID459024/start80531912とWindows32704は終了。元UIはPID459564/start80610052、boot4052bfc5-3850-44e4-9123-d34a9e19f36e、元10B親/Tokenizer/native10M・idle HTTP・kernel FLOCK一致で復帰済み。これは時点付き証拠で現在の生存保証ではない。今回の文書作業ではHTTP/生成/再起動を行っていない。

最新完了commitはcf113068。checkpoint-00004420.ptの全stateはWSLのreports/phase6/rdrop-science-20261016/、小raw/notes/receiptはGitに保全。累積台帳は技術169.2456279549515＋科学4241.304908989929＝4410.55053694488秒。これは当該継承台帳の範囲であり、プロジェクトの全歴史GPU時間の総計ではない。

## 現在の目標と次の行動

元「4まで」は未達のまま解除済み。現在の文書目標は、全件カタログ・現行説明・計画・原文保全・リンク/同期/Git検証まで。比較を実行したことや文書更新の完了をBaseの達成へ読み替えない。将来の順序は計画145を参照。

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="ui保存先履歴"></a>
<a id="前回chatの完了結果"></a>
<a id="完了したことと未確認"></a>
<a id="次の判断と停止境界"></a>
