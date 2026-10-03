# Phase 5: 候補の採用・棄却理由

2026-10-03。固定100M主比較の候補として **T4K / QK-Normなし / LR 0.002** を1つ選ぶ。選択は本学習へ渡すarchitecture/Tokenizer/LRであり、実用品質や学習済みHF/GGUF変換の合格ではない。自動集約の[選択記録](candidate_selection.md)を保持し、以下に生成失敗・補助予算・配布制約も含めた判断を補足する。

## 各runの判断

| Run | 判断 | 根拠・留保 |
|---|---|---|
| T4K / NoQK-Norm / LR 0.002 | 採用候補 | 主比較のdev BPB 1.221443、共通短文BPB 1.546589が最良。Normありとの差0.010379、document paired 95% CI 0.008505〜0.012258。定常121,139 tokens/sでNormありより約8.5%速い。CUDA厳密resumeと有限値を通過。ただしsampling Unicode 2/240、HF/GGUF adapter未実装というリスクを持つ。 |
| T4K / QK-Norm / LR 0.002 | 今回の選択から棄却・対照を保存 | BPB 1.231823、共通短文1.591386でNoNormに劣り、速度111,693 tokens/s。sampling Unicode 0/240と既存Norm export経路は利点。NoNormの不具合が解消できなければ、この保存済み対照へ戻る判断が可能。既存exportはランダム重みでの検証であり、学習後品質の保証ではない。 |
| T4K / NoQK-Norm / LR 0.001 | 棄却 | BPB 1.235002、共通短文1.618124でLR 0.002より悪い。低LR BPB−基準BPBは0.013558、95% CI 0.011594〜0.015443。速度121,046 tokens/sで利点なし。greedy反復52/80は基準54/80より2件少ないが、EOSは両方0/80で、この差だけではBPB低下を補う品質改善とは判断しない。 |
| T8K / QK-Norm / LR 0.002 | 今回の主予算では棄却・予算依存の代替を保存 | BPB 1.258861、共通短文1.650058。同一token予算でT4K Normとの差0.027038、95% CI 0.024808〜0.029387。T8Kは同じ100Mで約476.1MB、T4Kは約390.3MBのbodyを処理し、同一bytes予算ではない。近いbytes予算ではT8Kが良く、語彙の普遍的優劣とは結論しない。 |

全主比較はseed 42、12,208更新、100,007,936 stream tokens。Norm/LR比較は同じtoken digest、supervised tokens、body bytesで単一要因を確認した。T4K/T8Kは約10Mのmodel familyでarchitecture寸法も異なり、語彙のみの因果比較ではない。95% CIは924 dev文書のsampling不確実性であり、1 seedの学習変動を測った値ではない。[実測比較](tokenizer_model_comparison.json)、[独立監査](independent_audit.json)

## 補助予算とTokenizer fallback

近いbody-byte予算はT8K 8,000更新 / 65.536M tokens / 311,994,662 bytes、T4K 10,000更新 / 81.920M tokens / 319,703,055 bytes。差は7,708,393 bytes（targetの約2.47%）。BPBは1.200920 / 1.203982で、T8K−T4Kは−0.003062、95% CI −0.004975〜−0.001101。

近い学習更新時間はT8K 10,000更新 / 81.920M tokens / 701.77秒、T4K 9,000更新 / 73.728M tokens / 663.23秒。時間差38.54秒（targetの約5.62%）。BPBは1.212407 / 1.194784で、T8K−T4Kは0.017623、95% CI 0.015518〜0.019637。

どちらも実際のcheckpointを全devと共通短文で採点したが、最も近い保存点の近似であり、厳密な同一予算・同一履歴ではない。cosine schedule内の位置も異なる。終端より良いBPBの途中checkpointがあり、反復pilotで予算を増やすだけの改善を保証しない。[補助評価のhash・counters・paired CI](evaluation_summary.json)

devのbyte-codec tokensは両Tokenizerとも12,362。body token分母はT8K 343,196 / T4K 418,205で、token率3.602% / 2.956%。保護文字の明示的byte encodingを含む。率の差だけでT4Kの文字fallbackが減ったとは解釈しない。

## 生成品質と進行条件

採用候補の抑制ありgreedyはEOS **0/80**、反復 **54/80**、Unicode/role/empty各0/80。抑制なしgreedyも同じ件数。sampling（temperature 0.8 / top-p 0.9、3 seeds）ではEOS **2/240**、反復 **8/240**、Unicode破綻 **2/240**、role/empty各0/240。NormありT4KのsamplingはEOS0/240、反復6/240、Unicode0/240。NoNormのUnicode退行を隠さず、停止95%・Unicode0等の凍結品質目標は未達とする。反復flagは固定regexの検出値で、意味的反復の全量ではない。文法・関連性の全件blind人手採点は未実施。

100件overfitでの末尾EOS 100%は暗記した文書末尾の検証であり、dev promptからの自発停止の合格ではない。Phase 5の機械的gateと将来のBase/Chat品質は区別する。候補の選択は、品質課題と配布経路を解決する責務を持つ研究上の選択であり、Phase 6の自動起動や配布承認ではない。

Muonは追加しない。AdamW全4比較が非発散・初期重みよりdev改善し、候補を選べたため、今回の目的に対する追加optimizer比較の必要性は認めなかった。既存の失敗runと対照checkpointを保持し、閾値を緩めない。

Phase 6再開時には拡張train corpus、WSDのstable/decay分岐・再開一致、math/compileの容量・速度を検証し、予算を凍結する。候補は次のcorpusで新規初期化し、100Mのdecay済みoptimizerへ予算だけを足さない。NoNormの変換adapterとsampling Unicode/反復/停止も明示的な検証項目として引き継ぐ。今回の作業はPhase 5で停止する。
