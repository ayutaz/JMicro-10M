# 文書長による損失配分の比較結果

2026-10-14 JST。[計画143](143_base_document_balance_plan.md)の比較は終了し、全80生成の理由付き採点と元の採否条件を確認して**不採用**とした。Base/Chatは未完成・未採用。合格候補がないため、本比較への延長・独立学習・全文DEV・封印TEST・採用は実行していない。

## 変更と確認した範囲

元10B親・native10,001,152 parameters・Tokenizer4096・context1024・accepted TRAIN75/20/5・seed42・batch48・fresh AdamW LR1e-5/WD0.1をそろえた。元文書の本文tokens+元EOS1の逆数を本文/EOS全教師へ同じ重みで掛け、update内の重み合計で正規化した。文書抽出・入力・教師・architecture・推論は変えていない。反復学習を新規教材量と呼ばない。

対照は過去の同100M CE結果を再利用。候補は17,698更新・正確100,000,000教師を新学習した。全更新の損失/勾配/LR、教師counter、元文書長の重み平均/比率、最終モデル/Adam/scheduler/RNG/sampler/counters、対照の全sampler・入力/教師digest一致を確認。[数値監査](../reports/phase6/base-document-balance-comparison-20261014/numeric_completion_audit.json)。

CPU checks21件、CUDA技術47更新/273,521教師、最大48×1024のforward/backwardを別勘定で確認した。技術重みは科学学習へ使っていない。新GPUは科学1,474.808693秒＋技術8.721357秒＝1,483.530050秒（約24分44秒）。科学上限3,855秒、技術込み上限4,800秒以内。終了runを再起動しない。

## 生成品質と採否

候補の全80 prefixと全文を読み、個別理由を保存した。既存対照・strongの元採点は再利用し、変更していない。Codex非blind・同じDEVの反復参照・1学習seedであり、独立人間blindの証拠ではない。

| 指標 | 同100M CE対照 | 文書長重み候補 | 元DEV絶対条件 |
|---|---:|---:|---:|
| 共通byte BPB | 0.998487 | 1.000710 | 元保持/比較guardも必要 |
| 文法2 /80 | 44 | 23 | ≥56 |
| 関連性2 /80 | 25 | 28 | 補助記録 |
| 一貫性2 /80 | 2 | 1 | ≥27 |
| 適切完結 /80 | 2 | 2 | ≥27 |
| EOS /80 | 19 | 20 | ≥37 |
| 自動反復 /80 | 45 | 50 | ≤18 |
| empty/role/Unicode | 0/0/0 | 0/0/0 | 全0 |

対照からの一貫性差は−1/80、paired95%CIは−3.75〜0ポイント。元条件の差≥8、CI下限>0を満たさない。strongに対しても−22/80、CI−37.5〜−17.5ポイントで未達。反復・BPBの保持条件とhistorical Web BPB条件も未達。EOSが1件増えたことを完成や改善の採用根拠にしない。[全採否](../reports/phase6/base_document_balance_comparison_review.json)、[個別80理由](../reports/phase6/base_document_balance_notes.json)。

例: base-004は朝の続きを夜の条件節の反復へ変え、base-046は足の痛みの同一文を反復、base-085は姉が甘いものを食べない条件に反して菓子を勧めた。base-086は短い方針として自然に完結した。自動反復flagがfalseでも意味の循環がある出力は個別理由へ残し、元の自動flagを上書きしない。

この固定条件の不採用は、文書長による損失配分の全方式の否定、Base不足の単独原因、教材量不足、10Mの普遍的限界を証明しない。

## 6段階の実施と未実施

| 段階 | 結果 |
|---|---|
| 1. 次仮説の選定 | 既存証拠と実装を照合し、比較を1件に限定した |
| 2. 必要診断・準備 | 最初192 TRAIN windowの重み比11.85/CV0.50、CPU21 checks、独自CUDA再開/最大shapeを確認 |
| 3. 小規模比較 | 正確100M・全state・同stream・予算内・プロセス終了を確認 |
| 4. 本比較への判断 | 全80・共通DEV256・日本語192/331/1119・元全guardで不採用。本比較延長は未実行 |
| 5. 独立確認 | 有資格recipeなしでfresh独立学習seed43、fullDEV、400生成＋長文40は未実行・品質未確認 |
| 6. 最終TEST・採用 | 選定条件不成立で封印TEST・採用を未実行と判定。Base未完成・未採用 |

比較と必要な条件分岐・不採用判定は終了した。**6段階をすべて実行した、最終TESTに合格した、Baseを完成したという結果ではない。** 計画143および124の不合格時の報告・停止条件に従ってこの条件を閉じる。別係数・別seed・別親・増量・予算延長を救済として自動実行しない。[閉鎖記録](../reports/phase6/base_document_balance_comparison_completion.json)。

## 元Base TESTのCPU解析問題

今回使った既存`greedy80`は、`eval/base.jsonl`全行をJSON構文解析してからDEV80を抽出する。元TEST20行もCPU構文解析されていた。内容reviewの既存case照合も同じ構造だった。TESTの学習・GPU採点は0、TEST shardは未開封だが、元TEST promptを未参照とは呼べない。

旧resultの`protected_test_used/scored=false`は今回のGPU TEST採点なしと整合するが、CPU未解析の証拠にはならない。旧報告/source/混在suiteは保全し、[問題と訂正](../reports/phase6/base-document-balance-comparison-20261014/original_TEST_prompt_exposure.json)を別記録にした。以前のChat TEST事故とは別のBase側の問題で、当時のChat事故でBase TESTを解析しなかったという記録は改変しない。

今後有資格Baseができた場合は、DEV/封印TESTを別artifactとして扱うreaderへの置換と、新しい封印TESTが必要。合格候補がない今回に代替TESTを準備・解析・採点しない。

## 保存と停止

全重み・全optimizer/RNG/sampler・checkpoint・metricsはWSL `reports/phase6/base-document-balance-comparison-20261014/document_balance/`に保全。最終は`checkpoint-00017698.pt`、SHA `d89caf23bd7d2d8d81f298cb6f1fcbfe5fbd581105f91be1c3cfc18cefc9f86b`。元10B/Tokenizer/Phase0〜3/全旧runとデータは変更していない。

元10B WebUIはPID338403/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start60473641で復帰し、HTTPの元親SHA・Tokenizer・10M・idleを確認した。科学worker PID337424は終了し、二重実行していない。最終納品時にも実process/lockを照合する。

研究・学習の一巡をここで停止する。Chat/SFT・量子化・大型化・外部公開/pushは実施していない。最終ローカル保存・Git内容の検証は納品記録で確認する。
