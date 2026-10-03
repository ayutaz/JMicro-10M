# NoNorm T4Kの速度・容量選定（2026-10-03）

採用は**Flash / torch.compile reduce-overhead / fullgraph・static shape / deterministic / batch 32 / accumulation 1 / context 1024**。FP32 parameters、BF16 forward/backward、fused AdamW。定常速度の3回中央値は**694,521 tokens/s**、32,768 input tokens/update。学習用の固定長・PADなしcausal経路を使う。[全結果](batch_performance_report.json)、[要約](performance_summary.json)。

| 設定 | 3回中央値 tokens/s | 確認した最大安定batch | 次のOOM batch |
|---|---:|---:|---:|
| reference/math・最速batch 16 | 127,772 | 45 | 46 |
| compiled/math・最速batch 32 | 292,079 | 53 | 54 |
| compiled/Flash・最速batch 32 | 694,521 | 111 | 112 |

選択設定は最速reference比**5.436倍**。同じbatch 8の短い比較では4.321倍だった。速度比較は同じモデル/data/Tokenizer/context/precisionを使い、batchが異なる最終比較のtoken予算も各raw metricsへ記録する。品質比較にはしない。

選択batch 32はsave/小sample評価込みpeak allocated **5.73 GiB**、reserved **6.59 GiB**、driver peak **7.53 GiB**。data waitは測定時間の**0.55%**で、今回の測定では入力供給が主な制約ではない。最大容量batch 111はallocated **19.61 GiB**、reserved **22.48 GiB**、driver **23.42/23.99 GiB（97.64%）**まで使用し、3×200更新・保存・評価を通過した。速度は649,563 tokens/sだったため、32を選択する。

driver使用率の最大観測は選択設定95%、容量設定98%。2秒間隔の全sampleはstartup/save/evalを含み、選択設定の全区間中央値14.5%を定常学習の使用率として扱わない。MFUやGPUの理論性能を使い切った証拠ではない。容量は94% allocator cap・現在のWSL/driver/固定shapeで測った境界であり、任意条件の上限ではない。

採用と容量の各設定でstable 200 vs 100+100、独立decay 100 vs 50+50の全state・loss/LR/token/digest履歴が完全一致し、親の不変性と元継続も確認した。9設定のrunner検証に加え、採用・容量6設定を含む[独立監査1286項目](performance_completion_audit.json)が成功。選択設定は[空compiler cacheからの100→200再開26項目](performance_cold_resume_report.json)も完全一致した。[全79 tests](performance_tests.xml)。

500Mの純粋な学習換算は約12分、10Bは約4時間。compile起動・保存・全文dev/生成・WSD枝・LR調整は含まない。本学習のLR/warmup/effective batch/WSD予算は⑤で凍結する。既知の生成品質・NoNorm変換課題は④として残し、今回開始しない。

初回のcache backend取り違え、CUDA Graph replayに対するCPU-only観測の不足は[失敗記録](performance_failures.json)に保持。監査の初回には1 promptを1 outputと誤解した判定もあり、[失敗report](performance_audit_initial_failure.json)を保持した。既存generation APIは抑制あり/なしのgreedyを各promptから生成するため、正しい容量契約は4 dev文書＋1 prompt×2 outputs/各最大8 tokensである。元のGPU測定・評価隔離は成功しており、条件を変更せず監査の分母を修正した。

③の高速化・資源活用検証は完了。commit後、④以降・長期Base学習の前で停止する。
