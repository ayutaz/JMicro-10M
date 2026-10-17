# プロジェクト目的

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

最終成果物は約10Mの日本語Baseと、その後の短い会話を行うChat。日本語corpus→独自Tokenizer→スクラッチBase→Dialogue-oriented mid-training/Assistant本文+EOT SFT→採用float/量子化/ローカル利用という元目標を維持する。Baseが資格・独立学習・最終確認まで合格したら通知して停止し、後続Chatは別の再開範囲。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## 設計・手順の保存記録

以下は作成時点の仕様・調査・復元手順。途中の「最新」「次は」「未実施」やPIDはその時点の記録で、現在の状態は本ページ冒頭と148を参照する。外部サービス/依存の最新仕様は今回再照会していない。

## 維持する目標

最終成果物は`JMicro-10M-Base`と`JMicro-10M-Chat`。日本語コーパスの選別・出所記録、独自Tokenizerの学習、config設計とランダム初期化、Baseのスクラッチ事前学習、Dialogue-oriented mid-training、Assistant応答部分のSFT、量子化・ローカル推論artifactまでを追跡可能なpipelineとして扱う。Dialogue-oriented mid-trainingと正式なChat完成・量子化は未達で、限定SFT診断の実行を全pipelineの完成へ読み替えない。

- 総学習可能パラメータ9.5M〜10.1M、現在10,001,152。大型化を改善策にしない。
- 日本語Baseの原品質条件と短文会話の目標を維持する。対象を物語だけへ縮めたり閾値を下げたりしない。
- BaseとChatを別checkpointとして管理する。ChatはBaseへ会話形式を追加学習したモデルで、別のarchitectureではない。
- 挨拶、相づち、感情への短い応答、質問返し、数turnの文脈維持と自然な停止を評価する。
- 高度な数学・コード生成・長文RAG・網羅的知識は当初の成功条件に加えない。
- 学習・保存再開・評価の再現性、Tokenizerの共通byte比較、反復・Unicode・役割混同の原出力を記録する。
- 量子化5〜10MB級は将来の目標。採用済みの学習モデルの量子化品質・実容量・独立環境検証は未達。

## 実績と未達

Phase0〜5の基盤を整備し、元10B Baseと多数の同10M比較を実行した。元Baseの品質採用は未達。Chat-first診断と教材比較128/131/133/135、低学習率比較139も全評価後に不採用で閉鎖した。最新139は全28セット・6,132内容判断・固定NLL7点。技術基盤や実学習の完了をモデル完成へ読み替えない。

独立学習seed43、人間blind、独立corpus監査、正式保持、fullDEV・最終suite、選定封印後TESTと正式採用は未確認。元Chat TEST20行の準備解析事故を保存し、将来の有資格Chat最終確認には新しい封印TESTが必要。

## 進め方と停止境界

通常の順序は基盤→Base→Chat→量子化。未採用Baseからの限定SFTはユーザーが明示再開した診断として実行し、既に閉鎖済み。新しい学習や追加教材へ自動移行しない。

再開するなら[Base復旧124](124_base_recovery_plan.md)等で介入を最大1件に絞り、対照・教師量・変更点・原品質・資源と終了条件を先に定める。Base復旧は必要な品質・独立確認・採用証拠がそろったBaseで通知して停止する。Chat・量子化・公開は別の再開判断。[フェーズ別計画](15_project_roadmap.md)。

初期計画・2024年の約355Mモデルとの比較・当初の概算は[全文書カタログ](document_catalog.md)と[更新前原文](../reports/investigation/documentation-refresh-20261014/baseline.json)へ保全した。

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="更新前の本文契約当時の記録"></a>
