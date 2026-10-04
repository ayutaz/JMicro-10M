# Phase 6 Base学習の現在地と進行条件

2026-10-04更新。Phase6全体の品質目標は未達。基盤①〜⑤、データ12.23B、2B・5B学習、各100M仕上げ比較、10B専用設定の準備は完了した。**本学習10BとCPU保存確認19項目、同条件品質評価とCPU確認23項目は完了。Base/Chat品質目標は未達。** [現在地](autonomous_status.md)、[次の詳細計画](39_learning_scale_and_generation_plan.md)、[準備証拠](40_base_10b_preparation.md)。旧計画全文は [履歴](autonomous_history_20261004.md) に保持する。

## 完了した基盤と実験

| 対象 | 状態 | 証拠 |
|---|---|---|
| データ・WSD/再開の基盤①② | 完了 | [基盤完了](26_phase6_preparation_completion.md) |
| GPU容量・速度・厳密/cold再開③ | 完了。batch32/Flash/compileを継続 | [実測](29_phase6_performance_completion.md) |
| 生成・CPU変換精度・設定凍結④⑤ | 当時の準備を完了、品質合格とは別 | [結果](30_phase6_readiness_execution.md) |
| 12.23Bデータ | 整備/loader受け入れ済み、独立全件audit未完了を保持 | [記録](../reports/phase6/corpus_10b_ready_review.json) |
| 2B・5Bと比較 | 完了、EOS/反復/意味品質は未達 | [5B比較](36_base_5b_comparison.md) |
| 5Bから各100M仕上げ | 完了、短文のraw失敗条件不合格 | [結果](38_eos_5b_finish_results.md) |
| 直接10B準備 | 14tests/実CUDA保存再開一致、科学tokens0 | [準備](40_base_10b_preparation.md) |
| 直接10B本学習 | 総10,000,007,168 tokens、CPU保存確認19項目成功 | [本学習](41_base_10b_training.md) |
| 直接10B品質評価 | 同条件dev/400、CPU23項目成功。BPB0.954018 / EOS0・反復53 / Unicode0、品質目標未達 | [品質結果](42_base_10b_quality_evaluation.md) |

## 現在の凍結設定

選定候補はT4K / NoQK-Norm / AdamW / 10,001,152 parameters。新しい長期入口は [base_10b.json](../configs/phase6/base_10b.json)。以前のbase_frozen.jsonや5B launcherを新10B設定として起動しない。

保存stable4.75Bから同じmodel/Adam/RNG/Web位置を維持する明示forkで、stable9.5B＋15,259-update decay、累積10,000,007,168 tokensへ到達した。[学習結果と速度](41_base_10b_training.md)。実追加科学5,249,990,656 tokensと、準備検証524,288 tokensは別。旧重み・旧reportsを保持し、7.5Bの別実験は省く。

## 評価と進行条件

同じ保護dev89,416文書/164,344,743本文bytesと固定400生成で新10Bを評価し、元5Bと最良Web5.1Bの保存結果を再利用する。BPB悪化+0.001以内、固定反復増加8件未満、all400 raw Unicode/empty/role0、生成条件一致という元増量安全条件を両対照に適用する。さらに次の仕上げ候補には最良Web BPB0.958091981より改善していることを要求する。

自然停止・反復・意味・文字化け・BPBを個別に報告する。表示補正や制約decoderの成功を元raw方式の採用成功へ加算しない。固定greedy64と元の反復指標を維持する。未使用test・独立人手blind評価がない段階ではBase/Chat品質達成を主張しない。

## 終了点と予算

現在の依頼step2の直接10B学習は完了し、専用jobと実processは終了済み。中断時の復旧commandは `bash scripts/run_base_10b.sh --train`。引数なし/--verify-onlyは準備のみで完了結果を再利用する。actual job/lock/latestを確認して重複起動を避ける。

今回は再開された品質評価も完了し、報告/local commitで一区切り。全文/生成のstep3品質比較も完了。[結果](42_base_10b_quality_evaluation.md)。学習GPU上限9,000秒に準備19.217秒を含め、別評価予約1,800秒、計10,800秒。見積もり145〜165分、実装・内容確認は別。短文仕上げ/UTF8制約、20B/50B/Chatへは自動移行しない。

## 開始前に揃える条件

既存文書からの参照先。直接10Bの環境・入力・保存再開準備は完了した。次回起動前はactual process/lockとvalid checkpointを確認し、専用10B設定を使う。完了済みgateを再実行しない。

## 暫定のcompute見積もり

旧段階別見積もりに代わり、現在は追加5,249,990,656 tokensの学習区間約126分、評価込み145〜165分を目安にする。科学上限9,000秒（準備19.217秒含む）と評価予約1,800秒。実装・内容確認時間は別。
