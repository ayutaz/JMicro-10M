# 次に進める作業

2026-10-04更新。[現在地](autonomous_status.md)と[具体的な計画](39_learning_scale_and_generation_plan.md)に合わせる。**総10B学習step2とCPU保存確認19項目を完了。今回は報告とcommitで停止する。** ユーザーが再開した同条件品質評価step3も完了。[評価結果](42_base_10b_quality_evaluation.md)。[結果と速度](41_base_10b_training.md)。

## 完了していること

- [x] Phase0〜5の環境・Tokenizer・モデル・GPU学習器・評価・保存再開・候補選定。
- [x] 既存12.23B train tokens整備。独立全件auditの未完了は保持し、再照合を繰り返さない。
- [x] 主系列総5B学習と同じdev/生成比較。
- [x] final5BからWeb対短文20%各100Mと条件付き全文評価・内容確認。短文はraw Unicodeで採用不合格。
- [x] UTF8表示末尾helperを実装し、raw失敗・IDs・bytes・停止理由を保持。
- [x] 直接10B専用config/schema/launcher、14tests、実CUDA全state/history再開一致。[準備証拠](40_base_10b_preparation.md)。

## 次の実行区切り

- [x] 保存stable4.75Bから総10,000,007,168 tokens/update305176へ継続。実Linux/Windows processの終了を確認した。
- [x] stable9.5Bと最終decay checkpoint、連続/有限更新、Adam/scheduler/RNG/cursor/消費counterを専用CPU reviewerで確認した。
- [x] step3の専用品質比較入口とCPU reviewerを実装し、関連23tests成功。旧reportは保持。
- [x] 新10Bだけ全文dev89,416/本文164,344,743bytesと400生成を評価し、5B/最良Web5.1Bを再利用した。
- [x] BPB/EOS/反復/raw flagsと全固定80・自然停止9件の内容を比較。CPU保存確認23項目成功。元増量gateは合格、Base/Chat品質未達を報告し、local commitで停止する。

既存12.23Bを使用し、7.5B専用decay/中間全文評価、新しい収集、旧GPU比較、全コーパス再監査は追加しない。学習GPU上限9,000秒（準備19.217秒を含む）、別評価予約1,800秒。見積もり145〜165分、実装と内容確認は別。

## その後の候補

10Bの改善と元raw増量安全条件を満たした場合、同じ新親のWeb/短文20%各100Mを一対だけ比較する。途中不正UTF8と未完成末尾には保存重みの単一制約decoderを別policyとして比較する案がある。これらは現在未実装・未起動で、元raw失敗を合格に書き換えない。

Base/Chat品質条件、人手blind評価、未使用test、Assistant body＋EOT学習、量子化/local品質は[ロードマップ](15_project_roadmap.md)の条件を維持する。20B/50B、Chat、unlikelihood、parameter sweep、外部出版・有料cloudは現在の作業範囲に含めない。

古い500M/1B前停止や未着手記録は [履歴](autonomous_history_20261004.md) に保存した。
