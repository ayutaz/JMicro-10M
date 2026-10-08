# 教師トークン数に合わせる重み減衰の比較

Base限定の一変更比較。Chat/SFT/量子化は開始しない。新しい条件は品質未確認であり、Baseは未完成。

既存383報告の小さいmetadataと元学習の最初10,000更新だけをCPU0.684秒／上限30秒で確認した。`base_teacher_decay_accounting_20261008.json` に原報告のSHA・検索文脈・84,799,468 bytesのmetrics prefix SHA・会計を保存した。全metrics、corpus、checkpointは再走査しない。検索で見つかった教師量正規化への言及は次の調査を記した2つのactive記録で、学習済み条件ではない。減衰に関係する原報告の文脈、勾配蓄積の不採用、norm診断、索引後の初期化結果も確認した。この範囲では同じ比較は見つからない。検索はすべての履歴についての数学的な新規性証明ではない。

元の94,160,195教師／10,000更新は平均9,416教師／更新で、AdamWの減衰単独の累積係数は0.143113だった。教師数nごとに `(1 - lr * 0.1)^(n / 32768)` を適用する条件なら0.571984になる。実効weight_decayは0.023140〜0.036691。これはAdamによる勾配更新を除いた乗算部分の算術であり、実際の重みがその比率に縮んだ証拠、減衰が品質低下の原因という証拠ではない。

32,768は従来のpacked32×1024入力形状を手掛かりに固定する基準教師数で、従来のvalid教師が毎回32,768だったという主張ではない。基準を生成品質から選ばず、係数sweepは行わない。[AdamW原論文の付録B.1](https://arxiv.org/html/1711.05101v3#A2.SS1)はbatch数と計算予算に合わせる平方根の正規化を提案している。今回の教師数を指数にする規約とは異なる。論文はこの日本語モデルの改善を保証しない。[PyTorchの実装](https://github.com/pytorch/pytorch/blob/main/torch/optim/adam.py)のdecoupled乗算 `1-lr*weight_decay` に合わせて実効係数を計算する。

候補はnative10,001,152パラメータ・fresh seed42・従来の初期重みで開始する。同じaccepted TRAIN、80窓／更新、10,000 microbatch・10,000 Adam更新、94,160,195教師、CE/clip/Adam betas・eps/LR/更新時点/source・EOS・samplerを保持する。変えるのは全パラメータに対する減衰だけ。normだけの減衰除外は行わず、以前のnorm診断の不合格も保持する。勾配蓄積4はnoise/clipping/momentum/cadenceまで変えたため、減衰単独の品質効果を示していない。

`TeacherDecayTrainer` はnative optimizerのstep直前に実教師数と同じ更新のLRから係数を設定し、Adam本体とforwardは元の経路を使う。checkpointにpolicy・直近教師数・実効係数・Adam/scheduler/RNG/sampler/全会計を保存する。独立した初回Adam更新の差分、実CPU連続4対2+save+2の全state/history、異種／改変stateの無変更拒否を含む7 testsが2.95秒で合格した。CPU fixtureは実GPU／品質の証拠ではない。

GPU上限は実controlの1,301.473秒から `ceil(1.3 * actual + 300) = 1992` 秒に固定。自身の実CUDA4対2+save+2の全state/history/有限値・90%メモリgateを先に通し、検証重みを捨てる。検証教師は科学教師と別計数。形状は元と同じなので既存worst80×1024 peak17,791,499,264 bytesを容量根拠に使い、最大VRAM使用率や最適速度とは主張しない。

controlは既存の実10,000更新checkpointと同256DEV・固定80生成・原採点を再利用する。候補256DEV・greedy64の全80を個別に読み、raw SHA付き採点を保存する。事前screenはBPB2%以上改善、文法・一貫性・適切な完結・EOSが悪化せず、反復が増えず、empty/role/Unicode異常0。元の絶対品質、歴史Web保持、独立学習seed43、fullDEV、protectedTEST、採用は別に必要で、pilot合格だけではBase完成にしない。繰り返しDEVと非blind採点の限界も保持する。

終了条件は候補自身のgate・同一streamの全会計・上限内終端・評価・全80内容採点・事前screenによる採否・実process終了と元10B UI復帰。失敗時はこの固定条件を閉じ、LR/基準教師数/係数/seed/cap救済や自動2B延長を行わない。正確な永続job identity、log、latest checkpoint、累積予算と再開コマンドをactive記録に残す。Baseが必要な評価を伴って完成した時点でユーザーへ通知して停止する。
