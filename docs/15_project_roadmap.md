# JMicro-10M フェーズ別実行計画

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

## フェーズの状態

| Phase | 状態 | 残る成果物 |
|---|---|---|
| 0〜3 | 成功条件/データpilot/Tokenizer/model-cache-export基盤は完了 | 当時の16〜19の証拠を保全 |
| 4〜5 | WSL/4090学習・全state再開・小予算比較基盤は完了 | 技術成立と品質完成は区別 |
| 6 Base | 元10Bと多数の比較を実行、品質未達 | 有資格recipe→独立fresh全pipeline→fullDEV/全440→新TEST/採用 |
| 7 Chat | 限定SFT128〜141は実施・不採用 | 正式Chat、独立確認、人間blind、最終採用は未達 |
| 8 ローカル利用 | UI/変換基盤あり、正式量子化成果物は未完成 | 採用floatとの品質/容量/速度/独立環境の確認 |
| 9〜10 追加研究 | 条件付き後半構想 | 20B/50B・追加研究等を自動開始しない |

## 現在と今後の順序

現在は文書更新のみ。元「4まで」は未達で解除済み。将来の研究は[計画145](145_post_rejection_next_plan.md)の前向き契約で、次比較の選定・必要技術gate・科学比較・主資格・独立全pipeline・最終評価の順。累積時間が無制限でも、比較ごとの終了条件を保持する。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

DEV80の絶対条件は文法2≥56、一貫性2≥27、適切完結≥27、EOS≥37、規定反復≤18、empty/role/Unicode失敗0。相対一貫性差≥8、paired CI95下限>0、BPB/strong/cached/historical保持も必要。最終TEST停止95%は別条件であり、DEVのEOS37/80で代替しない。総trainable9.5M〜10.1M、参照10,001,152を維持し、日本語領域・元品質を勝手に狭めたり下げたりしない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## 原定義と履歴

Phase0〜3の完了は[16](16_phase0_completion.md)・[17](17_phase1_completion.md)・[18](18_phase2_completion.md)・[19](19_phase3_completion.md)、学習基盤は[21](21_phase4_completion.md)・[23](23_phase5_completion.md)。過去の全ロードマップは今回baseline snapshotと[旧履歴](project_roadmap_history_20261008.md)に保全。基盤の完了をBase/Chat採用へ読み替えない。

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="10mを維持する制約"></a>
<a id="phase-0-成功条件環境実験管理"></a>
<a id="phase-1-データの小規模pilotと評価split"></a>
<a id="phase6の現在地"></a>
<a id="phaseごとの目的とゴール"></a>
<a id="前回停止時の道筋歴史記録"></a>
<a id="品質目標と判断ルール"></a>
<a id="後続フェーズの扱いと履歴"></a>
<a id="現行の採否条件"></a>
<a id="目的と停止境界"></a>
<a id="資源時間実行の原則"></a>
<a id="高速に完成させる進め方"></a>
