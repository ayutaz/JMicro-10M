# プロジェクト目的

更新: 2026-10-14 JST。現在の依頼は全現行文書の最新化と今後の計画作成。Base/Chatは未完成・未採用。研究・教材準備・診断・生成評価・GPU学習は再開していない。

[最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md) / [次の計画145](145_post_rejection_next_plan.md) / [今回更新146](146_documentation_followup.md)。

最終成果物はJMicro-10M-BaseとJMicro-10M-Chat。日本語corpus選別→独自Tokenizer→ランダム初期化/スクラッチBase→Dialogue-oriented mid-training→Assistant本文+EOT SFT→量子化/ローカル利用という元目標を維持する。約10M、日本語Baseと短い会話の原品質・領域を変えない。合格Baseで通知停止し、Chat/量子化は別の再開段階。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

元Base TEST20 promptと元Chat TEST20行は別のCPU解析問題を保存した。学習・GPU TEST採点に使っていないこととCPU未解析は別。将来の有資格最終確認にはreader分離と新しい封印TESTが必要。今回data/TESTを開封・再処理しない。

次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。

## 更新前の本文・契約（当時の記録）

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
