# Codex継続作業の現在地

進行中（2026-10-05 JST）: ユーザーが結果63後の四項目を再開。別train例でselectorを検証・凍結し、未確認各40を含む同source各20Mを準備、条件成立時だけ各100M/日本語と全160/原gateの条件付き全文、判断/report/local commit/元UI確認で停止する。[実行64](64_condition_selector_v2_execution.md)が新範囲。旧sampleを再抽出・再採点せず保存。現時点で新GPU jobは未起動。以下の結果63完了は前回の履歴。

最終更新: 2026-10-05 JST。**計画61段階1〜4の教材準備不成立の分岐まで完了・停止**。保存失敗診断と同sourceの各20,000,028-token教材を作ったが、候補の弱例12/40が学習開始条件10/40以下を満たさなかった。対照21/40。全80全文の個別理由、準備gate、採否、完了と元10B UIの実確認を保存した。新GPU学習/評価は開始していない。[結果63](63_condition_preservation_preparation_results.md)、[実行62](62_condition_preservation_execution.md)、[原計画61](61_condition_preservation_next_plan.md)を参照。

## 実際の現在地

| 項目 | 確認済みの状態 |
|---|---|
| モデル | 10,001,152 parameters / Tokenizer4096 / context1024。10Mはパラメータ数、Bは学習tokens |
| 一般Web準備量 | 12,225,819,077 train tokens。独立全corpus混入・重複監査は未完了 |
| 主系列・UIの重み | final10B:10,000,007,168学習tokens/update305176。Chat未調整 |
| 既存物語準備量 | 200,000,192tokens（旧59,963,449＋新日本語訳140,036,743） |
| 今回の比較教材 | 同じ翻訳sourceから各20,000,028tokens/71,268全文。文書長全並び/BOS/EOS位置一致。元200Mのsubsetで、新取得量に加算しない |
| 今回の準備結果 | 弱例21/40→12/40。候補10/40以下が未達、準備段階で不採用 |
| 今回の計算量 | 科学学習0/検証0、新GPU評価0。段階1＋builder13.752109秒、新pool証拠照合0.770125秒。個別診断・実装時間は別 |
| 実行環境 | WSL2/Linux disk、uv Python3.12.7。builder12CPU workers |
| 完了の確認 | 関連CPU4tests、101data evidencechecks、10failure-branch completionchecks成功。品質条件の合格ではない |
| 未実行の後続 | 準備失敗分岐に従い、各100M/CUDA再開/一次日本語と160生成/条件付き全文を未起動 |
| 採否 | 候補不採用。モデル精度の変化を測っていない。Base/Chat品質未達 |

## 最新の科学学習比較（変更なし）

[結果60](60_dataset_expansion_results.md)は旧60M/新200M条件を同じ元10Bから各追加1,000,013,824、各終端11,000,020,992tokensで比較した。科学計2,000,027,648/検証262,144を別会計にする。実験完了local commit `afad164`、文書更新 `d8a8f95`。終了済みrunを再起動しない。

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

常識の対応差95%+1.877〜+5.139pp。意味/文法の区間は0を含み、一貫性は−6/80、95%−16.25〜+1.25ppで不採用。source・長さ・EOS密度も変わったため量だけの効果とはしない。今回の準備失敗もデータ増量・追加学習の無効性や10Mの容量限界を確定しない。

## processと保存証拠

今回のbuilder actual362299は完了・不在、plan58科学239609も終了。元final10B UIは停止せず、完了確認でactual PID359102/boot`53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe`/start_ticks7216365を照合した。HTTP親SHA`410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`、学習tokens10,000,007,168、busy=false。[UI](http://127.0.0.1:7860)は元10B。後日再開時はactual identity/HTTPを再確認する。

- Windows可搬証拠: [診断](../reports/phase6/condition_preservation_diagnosis.json)、[ready](../reports/phase6/condition_preservation_ready.json)、[prepare job](../reports/phase6/condition_preservation_prepare_job.json)、[全80原文付きreview](../reports/phase6/condition_preservation_data_review.json)、[notes](../reports/phase6/condition_preservation_source_notes.json)、[採否](../reports/phase6/condition_preservation_judgment.json)、[要求別完了・UI](../reports/phase6/condition_preservation_completion.json)、[CPUtests](../reports/phase6/condition_preservation_tests.xml)。
- Linux教材: `/home/aihub_ubuntu/jmicro-data/phase6/condition-preservation-20261005/`に両20M stream/index/manifest/sample、凍結selector/builder、ready/diagnosis/jobを保存。Gitにはshardsを含めない。
- Linux実行: `reports/phase6/condition-preservation-100m-20261005/`にreview/judgment/completion/testsとbuilder launch/log。100mという名前は実学習の証拠ではない。
- 過去の全raw/重み/凍結sourceとPhase0〜3は保持。今回の実験はこれらを変更していない。

## 次の具体案と停止境界

今回の準備失敗分岐は完了し、verified local commitで停止。条件を弱める、今回の40例を見てselectorを直して再採点する、新GPU/500M/1B/20B/50B/Chat/test/pushを開始することはしない。

次回案は、意図の否定・物の所在・出来事と結論の不整合を、今回の確認sampleと分離したtrain診断例で検出できるか固定比較すること。selector凍結後、未確認の各40を一度だけ確認し、元準備条件を満たす場合に限定した各100Mを提案する。目的と限界は結果63へ記載し、追加の改修・抽出・学習は未開始。

独立人手blind、保護test、主Web独立全件監査、実用Chat、新重みの量子化/local品質は未実施。原ロードマップの品質目標と採用条件を維持する。旧進捗は[2026-10-05履歴](autonomous_history_20261005.md)と番号付き実験記録へ保持する。
