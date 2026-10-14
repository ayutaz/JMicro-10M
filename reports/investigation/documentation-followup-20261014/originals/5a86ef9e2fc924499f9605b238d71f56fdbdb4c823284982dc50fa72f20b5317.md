# 同じ減衰条件で累積2Bまで継続する

[短い比較120](120_base_teacher_decay_pilot_results.md)でBPB2.17%改善と事前の退行なしscreenを満たした条件だけを継続する。一貫性は同じ2/80で改善しておらず、Baseは未完成・未採用。Chat/SFT/量子化は開始しない。

事前proposalは `reports/phase6/base_teacher_decay_2b_proposal.json`。約94M親の実checkpoint SHA b7b9808a…から、重み・Adam・2Bを目標としたscheduler・RNG・sampler・累積会計・減衰metadataを変更せずに継ぐ。追加教師1,905,839,805、累積2,000,000,000。LR再加熱や初期化、係数、32768教師基準、新教材への変更はない。検証用の学習は別計数し、検証後に元の親を読み直す。

checkpoint内部のbindingはpilotの科学学習の祖先bindingを保持する。新しい実験のconfig SHA・親SHA・祖先binding・継続roleを別のjob/training-record/evaluation/resultへ結び付け、checkpointの内容を後から新しい実験名へ書き換えない。仕様上のfresh seed42は元の初期化の祖先であり、継続を新規初期化と呼ばない。

`base_teacher_decay_2b_protocol.py` の共通処理で、同じ学習済み親から連続4対2+save+2を実行し、全stateと全更新履歴を比較する。実CPU7 tests/3.72秒は中途親の不変性、実更新を含む再開一致、従来と同じstream、compactログの欠損・減衰改変拒否、live/予算超過/二重会計/stream不一致/教師量取り違えの完了拒否を確認した。これは実CUDAや生成品質の証明ではない。

`run_base_teacher_decay_2b.py` と永続PS launcherが、実processの重複確認、idle元10B UIの停止、実親CUDA gate、学習・保存・全評価、終了時の元UI復帰を担当する。CUDA gateは原モデル/Adam/RNG等に加えて、最初の更新前に同じ学習済み親かを確認する。旧worst80×1024の容量測定を再利用し、検証VRAMも記録する。Checkpointは完了更新の1000更新ごとと終端でatomicに保存し、heartbeatは20更新ごと、stdoutにも1000更新ごとの進捗を出す。

更新ログはCE・勾配有限値、全累積会計、実教師数、元のteacher-position LR、実効減衰、digest、時間を残すcompact JSONL。80窓すべてのdraw_traceを全更新へ重複保存せず、sampler checkpointと原stream digestを保持する。CPU採否はこの小さいログを一度だけ読み、全更新の連続性・有限値・LR/減衰・最終会計を確認する。既存2B対照の全ログやcorpusは再走査しない。

対照は既存fresh native sequential2Bのcheckpoint a1d29762…と、同256DEV・日本語semantics192/JBLiMP331/JCQA1119・greedy64の原80と採点を再利用する。対照GPU学習・再採点はしない。新候補は同じnative BF16/mathの評価経路を使い、RNGの不変性と各sectionのcheckpoint bindingを保持する。GPU実装・保存・評価の完了だけではBase合格にしない。

`review_base_teacher_decay_2b.py` は実processの終了・閉じた台帳・型付きcheckpoint・親の不変性・同2B教師と全counters/sampler/schedulerの一致・全80個別raw-bound採点を確認する。元の品質policy `configs/phase6/base_parallel_residual_review.json` と元のhelpersを再利用する。matched native2B、strong staged、cached CE100Mとの品質比較、絶対品質、歴史Web保持をすべて適用する。strong/cachedは学習履歴の異なる追加品質参照であり、同2B streamとは呼ばない。短いpilotの2%screenだけで最終採用しない。

追加GPUの上限は実pilotから算出した37,536秒。旧pilot1,415.133887秒は別台帳とし、両者の合算上限38,951.133887秒も記録する。保守的な追加分の見込み28,642.873秒にはpilotの固定評価費まで率として含まれ、純粋な学習速度の推定ではない。予算・品質失敗時のcap/基準/係数/LR/seed救済や自動長期sweepはしない。

実CUDA gateと本学習の状態は `reports/phase6/base_teacher_decay_2b_active_job.json` とstatus先頭を正とする。この文書のCPU準備段階では新しい長期GPUはまだ起動していない。条件とsource/configを凍結してから実GPUへ進む。Baseの品質、独立学習seed43、fullDEV、protectedTEST、採用の証拠が揃った時点でユーザーへ知らせて停止する。

初回の起動前preflightは、SHAを確認したCPUテストXMLまでJSONとして開いたため拒否された。GPU/UI変更は0。元の凍結config・runner・失敗理由を `reports/phase6/base-teacher-decay-2b-preflight-v1/` に保存し、参照のbyte照合とJSONの読込みを分けて修正した。科学条件・CPU7checks・品質基準・予算を変更せず、修正sourceで凍結し直す。
