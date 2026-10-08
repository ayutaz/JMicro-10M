# 教師量正規化decayの短い比較結果

探索的な継続条件を満たした。Baseは未完成・未採用で、Chat/SFT/量子化は開始しない。

[事前条件119](119_base_teacher_decay_pilot.md)のとおり、fresh seed42/native10,001,152の初期重み、原TRAINのdraw、80窓／更新、CE、clip、Adam更新時点とLRを保持し、全パラメータのdecoupled weight decayだけを教師数に合わせた。候補94,160,195教師／10,000更新を完了。原教師・CE/physical入力・BODY bytes・digest・source教師/EOS・sampler・scheduler位置・更新数の11checksが実controlと一致した。

| 同256DEV・生成各80件 | 従来 | 教師量正規化 |
|---|---:|---:|
| BPB（低いほどよい） | 1.290203 | 1.262247 |
| 文法2 | 28 | 31 |
| 一貫性2 | 2 | 2 |
| 適切な完結 | 3 | 4 |
| EOS停止 | 13 | 16 |
| 自動反復 | 49 | 49 |
| Unicode/role/empty異常 | 0 | 0 |

BPBは約2.17%改善し、対応文書byte加重差は−0.027956、95% bootstrap CIは[−0.030557, −0.025371]。一貫性の件数差は0、率差CIは[0, 0]。自然に一貫した例は従来と同じ2prefixであり、意味の成立の改善を示していない。文法と完結の小さい件数増加について独立した有意改善とは主張しない。反復も49件のまま残る。

候補の全80prefix・原生成・停止・反復を個別に読み、raw SHA付き理由を保存した。従来80件の原採点は保持し、そのうち以前に適切な完結とした3例を尺度の確認に参照した。自然な構文でも循環する説明は一貫性0、EOSだけの意味破綻は完結0とした。AIによる非blind評価で、独立した人間の評価ではない。

事前screenの「BPB2%以上改善＋文法/一貫性/完結/EOSが悪化しない＋反復が増えない＋異常0」はすべて満たした。一方、絶対品質の文法56、一貫性27、完結27、EOS37、反復18以下はすべて未達。元の歴史Web保持、独立学習seed43、fullDEV、protectedTEST、採用も未達。短い同条件比較の損失改善を、最終Base品質や長期学習の改善へ一般化しない。

候補自身の実CUDA連続4対2+save+2は14checks全一致。検証8更新・75,076教師は科学学習と別会計で重みを破棄した。累積GPU1,415.134秒／上限1,992秒で閉鎖し、actual117377/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start7956207は実終了・alive=false。監視session60374も正常終了。Windows worker32512はexit0/UI restore成功で終了した。CPU reviewerが元10B UI117764/start8098103の実processとHTTP親SHA410f975d…/10,000,007,168 tokens/busy=falseを確認した。現在の科学GPU jobはない。

主な証拠は `reports/phase6/base_teacher_decay_pilot_completion.json`、同prefixの`candidate_evaluation.json`・`candidate_notes.json`・`result.json`・`job.json`・`resume_gate.json`。portable raw/notes/result/terminal job/launcherを保存し、重みと全更新ログはWSL native runへ保持する。control再学習／再採点はしていない。

次の比較は別の事前proposalとして、同じ減衰条件を累積2B教師まで継続する。既存candidate94,160,195教師から追加1,905,839,805教師で、元から2Bを目標としたscheduler・Adam・RNG・samplerをそのまま継ぐ。LR再加熱、初期化や減衰係数変更、新教材追加はしない。対照は既存のfresh sequential2B実checkpointと評価・採点を再利用し、同2B教師の原streamを合わせる。成熟10B系とcached CE100Mは追加品質参照であり、同じ学習履歴の対照とはしない。

実pilot全GPU1,415.134秒を94,160,195教師で割った保守的な速度から、追加分の予測は28,642.873秒（約7時間57分）。評価の固定費まで率へ含めるので純学習速度ではない。新しいgate・学習・save・評価込み上限は `ceil(1.3 * 28642.873 + 300) = 37536` 秒（10時間25分36秒）。pilot GPUとは別台帳で合算も記録する。予算は延長先の改善を保証しない。

新しい長期runner/reviewerはまだ未実装・未凍結・未起動。次は既存full2Bの原評価と品質policyを再利用できるよう、型付きの継続・正確な中途stateでのCUDA4対2+2・同stream会計・固定DEV/日本語選択式/80原文・元品質/保持による採否を接続する。必要なCPU checksを通してsource/configと終了条件を凍結し、実idle/UI/PIDを確認後に永続起動する。短いpilot合格だけで自動延長せず、定義した一比較の実装を先に完成させる。失敗時は基準教師数/係数/LR/seed/capの救済や次の長期sweepをしない。

Baseが品質・独立学習seed・fullDEV・protectedTEST・採用まで揃った時点でユーザーへ通知して停止する。
