# 現在の状態

更新: 2026-10-14 JST。**Base/Chatは未完成・未採用。** 文書更新はcommit70aa002で納品検証まで完了。その後「6まで進めてください」により、提示した6段階のBase改善から最終判定までが明示再開された。[実行計画143](143_base_document_balance_plan.md)。Chat/SFT・量子化・大型化・公開は範囲外。

最新の[文書長重み比較144](144_base_document_balance_results.md)は17,698更新・正確100M教師・全80理由付き内容・共通DEV256/Japanese192/331/1119・全state/元文書重み/対照全samplerとdigestを確認して**不採用で閉鎖**。文法44→23、一貫性2→1、適切完結2→2、EOS19→20、反復45→50（各80）。BPB0.998487→1.000710、一貫性差CI−3.75〜0ポイントで原品質・保持未達。

CPU21 checks、有限192 TRAIN診断、実CUDA47技術更新/273,521教師は別証拠。新GPUは科学1,474.808693＋技術8.721357＝1,483.530050秒、科学上限3,855/技術込み上限4,800以内。[数値監査](../reports/phase6/base-document-balance-comparison-20261014/numeric_completion_audit.json)、[全採否](../reports/phase6/base_document_balance_comparison_review.json)、[閉鎖・条件分岐](../reports/phase6/base_document_balance_comparison_completion.json)。

本比較延長・fresh独立学習seed43・fullDEV/400＋40・封印TEST・採用は有資格候補なしで未実行・passed=false・品質未確認。6段階すべての実施、Base完成とは記載しない。計画143/124の不合格時の報告停止条件でこの1比較を終了。追加の研究・学習を自動起動しない。

元Base TEST20 promptも既存greedy80がDEV抽出前にCPU構文解析していたことを確認。学習・GPU TEST採点0、TEST shard未開封だが、元TEST promptを未参照とは呼べない。[問題と訂正](../reports/phase6/base-document-balance-comparison-20261014/original_TEST_prompt_exposure.json)。将来の有資格Base最終確認は別artifactのDEV/TEST readerと新しい封印TESTが必要。今回は候補なしで代替TEST未準備・未採点。

科学PID337424/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start60325743は終了。元10B UIはPID338403/start60473641で復帰、HTTP元親/Tokenizer/10M/idleを確認。最新Base候補はWSL `reports/phase6/base-document-balance-comparison-20261014/document_balance/checkpoint-00017698.pt`、SHA `d89caf23bd7d2d8d81f298cb6f1fcbfe5fbd581105f91be1c3cfc18cefc9f86b`。重み・全sampler・全metricsはWSL保全。ローカル納品検証を終えたら報告停止する。

## 前回Chatの完了結果

[低学習率比較141](141_chat_lr_comparison_results.md)で、計画139の介入選定・同10M比較・有資格候補だけの独立確認への分岐を完了し、候補S1を不採用で閉鎖した。元10B親、同accepted TRAIN/Tokenizer/seed42/教師量/schedule/paddingでpeak LR1e-4→3e-5を比較。S0は138のS1の歴史state、新学習0。

| 項目 | 実際の証拠 |
|---|---|
| 固定参照 | native10,001,152 parameters、Tokenizer4096、context1024。9.5M〜10.1Mを維持 |
| 教材 | TRAIN41,529 target、660,109教師/周。280sample QAを再利用。新教材・新QA0 |
| S1学習 | 3,646更新・1,899,557 Assistant本文+EOT教師、許容内超過2。全3state・全update入力/label digest確認 |
| 全評価 | 28セット・6,132理由付き内容判断・共通NLL7点×2,634 target。既知12セット2,628判断は出典付き再利用 |
| 技術確認 | CUDA probe9＋連続/保存再開16の25検証更新。品質や本学習へ数えない |
| 資源 | 新GPU2,658.673158秒/33,600秒。過去の学習やCPUレビュー時間と別 |
| 保存 | 結果commit89275a8、納品commit09f338eの360ファイル保存・Git内容を確認。push/公開なし |

| 最終セット | S0内容 /80 | S1内容 /80 | S0自己文脈 /24 | S1自己文脈 /24 |
|---|---:|---:|---:|---:|
| 新DEV | 13 | 20 | 3 | 5 |
| 138 DEV | 19 | 18 | 3 | 5 |
| 133 DEV | 21 | 19 | 6 | 5 |
| 元旧DEV | 11 | 15 | 1 | 1 |

原条件は全セット内容56/80以上、自己生成文脈15/24以上など。新内容差+8.75ポイント、95%CI −1.25〜+18.75も改善条件未達。反復非退行・停止の条件も不成立、新自己生成Unicode失敗1を保存。低LRでDEV NLLが対照より低くても品質合格ではない。

[科学監査](../reports/phase7/chat-lr-20261014/completion.json)、[採否](../reports/phase7/chat-lr-20261014/selection.json)、[納品記録](../reports/phase7/chat-lr-20261014/final_delivery_checks.json)。

## 完了したことと未確認

前の「3まで進めてください」は比較・採否・条件分岐・報告・保全・ローカル納品まで完了した。Base保持、sampling、fresh学習seed43、人間blind、fullDEV、封印TEST、採用の7分岐は候補なしで未実行・passed=false・品質未確認。独立確認を実行した、モデルが完成したとは記載しない。

判断はCodex非blind、QAは標本、対照は歴史state。独立corpus監査・正式Base/Chat採用も未確認。Base単独原因・10M容量限界は確定していない。

元Chat TEST20行を準備時にCPU構文解析した事故を[141](141_chat_lr_comparison_results.md)へ保存。学習・GPU評価への使用0だが、未参照の主張は取り消した。将来の有資格Chat最終確認には新たな封印TESTが必要。元Base TESTは事故では解析していない。

## 次の判断と停止境界

[比較143/結果144](144_base_document_balance_results.md)は不採用で閉鎖。今回の比較・必要な条件分岐・保存結果を報告して停止する。原品質・10M・独立確認を維持し、閉じた条件の係数/seed/親/予算延長で救済しない。Chat・量子化・公開へ自動移行しない。Base/Chatと全体projectは未完成。

## UI・保存先・履歴

最新の保存された科学観測2026-10-13T16:54:20Zでは元[WebUI](http://127.0.0.1:7860) PID309447/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start55170810、元親/Tokenizer/10M・busy=false・kernel GPU lock一致・競合なし。現在の稼働保証ではなく必要時に実processを照合する。終了runは再起動しない。

最新S1はWSL `reports/phase7/chat-lr-20261014/S1/checkpoint-00003646.pt`、SHA `f7e8bb8b1569cb45ac399108455a66c5922f64d7898e8ab6b4931ba13c856018`。重み・samplerを含む全state・教材はWSL、Git正本はWindows。[引継ぎ](windows_handoff.md)。

Base結果[123](123_base_teacher_decay_2b_results.md)、教材汎化[136](136_chat_generalization_results.md)、意味多様性[138](138_chat_semantic_diversity_results.md)、最新LR[141](141_chat_lr_comparison_results.md)は別runの閉鎖済み証拠。元UI10B・別staged約10.6B・teacher-decay2B・後続SFTの学習量を合算しない。

[公開保存版126](126_model_archive.md)は2026-10-09の主要3系列保存で、dataset/samplerを除外。後続Chat重みは公開していない。当時のpush許可は当時の納品に限る。

旧運用全文と全311文書のhashは[更新前baseline](../reports/investigation/documentation-refresh-20261014/baseline.json)に保全。[全体125](125_project_retrospective.md)と[固定台帳](retrospective/README.md)は当時のrevisionを保持する。
