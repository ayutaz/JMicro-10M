# Base残差出力初期化の結果（2026-10-08）

固定条件を不採用として閉じる。Baseは未完成・未採用。Chat/SFT/量子化は開始しない。

[事前条件117](117_base_residual_initialization_pilot.md)のとおり、同じfresh seed42・10,001,152パラメータの26個の残差出力行列だけを1/sqrt26倍して、候補を94,160,195教師・10,000 microbatch・10,000 optimizer更新学習した。従来の実checkpoint・評価・80件の原採点を再利用した。原教師/CE入力/physical入力/BODY bytes/token digest/source教師・EOS/sampler/最終scheduler位置/更新数の11 checksはすべて一致した。科学学習に6窓を繰り返し使った実験ではなく、既存accepted2B TRAINから従来と同じdrawを使った。

| 同256文書DEV・固定生成各80件 | 従来 | 初期化縮小 |
|---|---:|---:|
| BPB（低いほどよい） | 1.290203 | 1.306606 |
| 文法2 | 28 | 27 |
| 一貫性2 | 2 | 1 |
| 適切な完結 | 3 | 2 |
| EOS停止 | 13 | 16 |
| 自動反復 | 49 | 54 |
| Unicode/role/empty異常 | 0 | 0 |

BPBは約1.27%悪化し、対応文書byte加重差は+0.016403、95% bootstrap CIは[+0.014029, +0.018854]。一貫性の件数差は-1、率差CIは[-0.0375, 0]で、この一貫性差だけを独立した有意悪化の証明としない。新しい80件をprefix・原生成・停止情報とともにすべて個別確認し、raw SHA付き理由を保存した。従来80件は以前の原採点を保持した。AIによる非blind評価であり、独立した人間の評価ではない。

事前の探索screenはBPB2%以上改善と全品質数の退行なしを必要とした。EOS件数と異常0以外は満たさず、不合格。元の絶対品質・歴史Web保持・独立学習seed43・fullDEV・protectedTEST・採用の条件も未達。初期RMSとcosineの変化は、学習後の品質改善を意味しなかった。今回の短い条件の失敗を、すべての初期化や10Mモデルの能力の否定へ一般化しない。

候補自身の実CUDA連続4対2+save+2は、14 checksすべて一致。検証8更新・75,076教師は科学学習と別会計で、検証重みは破棄した。科学学習・save・評価を含む累積GPUは1,420.907秒、事前上限1,992秒以内で台帳を閉じた。実process115517/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start7711680は終了・実alive=false。監視session40123も正常終了した。

元10B UIを実PID116142/start7854156で復帰し、CPU集計時に実processとHTTPの親SHA410f975d…/10,000,007,168 tokens/busy=falseを確認した。科学GPU jobはない。新raw、全80notes、result、terminal job、CPU completionとlauncher記録を可搬保存する。重みと更新ログはWSL native runに保持しGitへ含めない。

主な証拠: `reports/phase6/base_residual_initialization_pilot_completion.json`、同prefixの`candidate_evaluation.json`・`candidate_notes.json`・`result.json`・`job.json`。元の比較条件・失敗を保存し、係数/LR/seed/capを変える救済や自動2B延長はしない。

次の実学習条件は未選定。次の具体的なCPU作業は、既存383報告の索引で教師量に正規化するdecoupled weight decayの既試行有無を確認し、元10,000更新の既存metricsのprefixだけから更新単位の減衰を再構成すること。CPU上限30秒、追加GPU/学習/採点0。勾配蓄積比較はnoise/clipping/momentum/decay cadenceも同時に変えたため、減衰単独の学習効果を証明しない。未試行かつ独立した一変更の対照を定義できた場合だけ、終了条件と実測予算を凍結して新しい比較へ進む。既存量比較、失敗したWeb95/story5供給、初期化の固定条件は再実行しない。

Baseが必要な品質・最終評価の証拠を伴って完成した時点でユーザーへ通知し、そこで停止する。
