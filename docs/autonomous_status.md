# Codex継続作業の現在地

最終更新: 2026-10-05 JST。今回の依頼は**ドキュメントと計画の更新**。計画58段階1〜3の実験は完了・停止済み。最新結果は[結果60](60_dataset_expansion_results.md)、次回案は[計画61](61_condition_preservation_next_plan.md)。新しい教材・GPU jobは開始していない。

## 実際の現在地

| 項目 | 確認済みの状態 |
|---|---|
| モデル | 10,001,152 parameters / Tokenizer4096 / context1024。10Mはパラメータ数、Bは学習tokens |
| 一般Web準備量 | 12,225,819,077 train tokens。独立全corpus混入・重複監査は未完了 |
| 主系列・UIの重み | final10B:10,000,007,168学習tokens/update305176。Chat未調整 |
| 最新物語準備量 | 旧59,963,449＋新日本語訳140,036,743＝200,000,192tokens/1,161,923全文 |
| 最新比較の学習量 | 同じ元10Bから旧/新各追加1,000,013,824、各終端11,000,020,992tokens。別枝の学習量を合算しない |
| 今回比較の計算量 | 科学2,000,027,648/検証262,144を別会計。一次GPU3129.607秒 |
| 実行環境 | WSL2/RTX4090/Linux disk。Python3.12.7をuvから実行 |
| 完了の確認 | 関連CPU5+LR2tests、実CUDA25checks、一次35/最終20evidencechecks成功 |
| 採否 | 新200M条件不採用。条件付き全文/400/長文は未起動。Base/Chat品質未達 |
| ローカル保存 | 実験完了commit `afad164`。Windows正本とLinux大容量runを別途引き継ぐ。今回pushなし |

## 最新の同条件比較

両終端は同じdev256/固定80/意味192/JBLiMP331/JCQA1119で評価し、全160生成に個別理由を保存した。内容診断はCodex非blindで独立人手評価ではない。

| 指標 | 旧60M・追加1B | 新200M・追加1B |
|---|---:|---:|
| dev256 BPB | 0.977154548 | 0.977322093 |
| EOS / 80 | 34 | 25 |
| 反復 / 80 | 15 | 14 |
| 一貫性2点 / 80 | 15 | 9 |
| 適切完結 / 80 | 20 | 19 |
| 基本意味 | 65.625% | 64.063% |
| JBLiMP主SLOR | 78.852% | 78.550% |
| JCommonsenseQA | 35.031% | 38.561% |

常識の対応差95%区間は+1.877〜+5.139ppで改善の証拠あり。意味・文法の差の区間は0を含む。一貫性差は−6/80、対応95%−16.25〜+1.25pp。原一貫性/EOS・実用条件が未達で採用しない。

長さ88.462→170.129/EOS密度11.054→5.810も変わり、量だけの効果ではない。実短文EOS教師は2,210,250→1,161,577。少ない終端教師は停止悪化の仮説で、原因を確定しない。データ増量の無効性、学習飽和、容量限界も未確定。

## 現在のprocessと保存証拠

実験PID239609は終了。元final10B UIを今回の読み取り確認で実PID359102とHTTPにより再確認した。boot`53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe`/start_ticks7216365。HTTP親SHA`410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`/training_tokens10,000,007,168/busy=false。[UI](http://127.0.0.1:7860)は元10Bであり最新11B候補ではない。後の再開時はactual process/boot/start ticks/HTTPを再確認する。

- Windows: [一次review](../reports/phase6/dataset_expansion_review.json)、[全160個別診断](../reports/phase6/dataset_expansion_annotations.json)、[カテゴリ](../reports/phase6/dataset_expansion_categories.json)、[採否](../reports/phase6/dataset_expansion_judgment.json)、[要求別完了確認](../reports/phase6/dataset_expansion_completion.json)、[result](../reports/phase6/dataset_expansion_result.json)。
- Linux: `reports/phase6/dataset-expansion-1b-20261005/`の両11B終端・500M中間checkpoint、全metrics/source/raw/job/review。教材は`~/jmicro-data/phase6/dataset-expansion-20261005/`。Git/Hubだけでは復元できない。
- LR記録時点の照合修正は独立reviewer v2。凍結v1/科学コード/config/schedule/採用条件は変更していない。

## 次の具体的な行動と停止境界

今回: 入口文書・roadmap・引継ぎ・checklistを結果60と計画61へ統一し、旧進捗を[2026-10-05履歴](autonomous_history_20261005.md)へ保存。リンク/数値/条件/元証拠不変/Linux同期を確認しlocal commitで停止する。

次回の提案: 保存した失敗を診断し、同じ翻訳sourceから品質改善だけを変えた長さ/EOS密度を一致させる各約20M pool、同じ元10Bから各100M、元gateによる条件付き全文・採否。目的・準備失敗時分岐・予算・終了条件は計画61にまとめた。提案の実行は未開始。

独立人手blind、保護test、主Web独立全件監査、実用Chat、新重みの量子化/local品質は未実施。20B/50B/Chat/外部公開は今回対象外。Phase0〜3を含む過去の成果物を保持し、終了済み学習・Tokenizer・全量照合を再実行しない。
