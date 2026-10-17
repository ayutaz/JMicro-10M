# 現在のチェックリスト

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

## 実績

- [x] DEV専用読取り/生成reviewの分離修理とCPU/既知DEV証拠。
- [x] 全文DEV/440接続部品と36 CPU checks。実品質は別。
- [x] ScaleGrad25Mを全80/全state/全guardで不採用に閉鎖。
- [x] 上限解除を新資源契約へ記録し、第一回RDrop25M科学比較を実行。
- [x] RDrop全80理由付き内容/全4,420履歴/状態/stream監査。不採用で閉鎖。

## 残る成果物

- [ ] 根拠ある未回答仮説1件の選定と、新比較/独立学習/最終評価の段階別契約。
- [ ] 元の全品質条件を満たす主recipe。
- [ ] 資格・全pipeline証拠を接続する永続native runner/reviewer。
- [ ] 親の事前学習から独立fresh seed43を実行し全state/再現性を検証。
- [ ] 実全文DEV、400生成＋長文40の全内容、必要な独立人間blind/corpus監査。
- [ ] recipe封印後の新TEST、原採否、復旧、Base採用。
- [ ] 別再開範囲のChat/SFT・量子化/配布。

DEV80の絶対条件は文法2≥56、一貫性2≥27、適切完結≥27、EOS≥37、規定反復≤18、empty/role/Unicode失敗0。相対一貫性差≥8、paired CI95下限>0、BPB/strong/cached/historical保持も必要。最終TEST停止95%は別条件であり、DEVのEOS37/80で代替しない。総trainable9.5M〜10.1M、参照10,001,152を維持し、日本語領域・元品質を勝手に狭めたり下げたりしない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="不変条件と停止境界"></a>
<a id="再開後に必要な成果物今回未実行"></a>
<a id="固定方針"></a>
<a id="完了した最新base比較"></a>
<a id="最新の閉じた比較139"></a>
<a id="次の実行境界"></a>
<a id="正式完成に未確認の証拠"></a>
