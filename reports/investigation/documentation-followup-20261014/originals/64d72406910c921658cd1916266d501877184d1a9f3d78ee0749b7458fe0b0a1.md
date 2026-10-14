# Base初期化の短期比較（2026-10-08）

Base限定。完成時にユーザーへ通知して停止し、Chat/SFT/量子化へ進まない。

同stream勾配蓄積pilotは不採用で閉じた。既存17学習比較では、教材量や教師量を増やすだけで全品質条件を満たす根拠はない。Web95%・物語5%の500M対2Bは既に準備済みだが、固定64件中11件が弱く、上限10件の内容条件に不合格だった。再準備・再抽選・基準緩和で救済しない。75/20/5の合成教科書を含む比較と混同しない。

次は独立した初期化仮説を検証する。現在のnative13層はAttentionとFFNの出力行列も標準偏差0.02の初期化。GPT-2論文2.3節の残差深度に応じた初期化を参考に、同じfresh seed42の標本のうち、26個のattention.o_proj/MLP.down_projだけを1/sqrt26（0.196116）倍する。追加パラメータ、推論時の係数、層数・幅・正規化・活性化の変更はない。[原論文](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)は異なる大規模モデルを扱い、この10M日本語での改善を証明しない。

以前に実際に消費したTRAIN6窓・756教師位置で、fresh FP32のforward/backwardを両条件でCPU実測した。0.936秒、上限30秒、GPU/optimizer更新/科学学習は0。

| 初期状態・6窓の集計 | 従来 | 残差出力初期化を縮小 |
|---|---:|---:|
| 最終残差RMS / 埋め込みRMSの平均 | 16.592949 | 2.718360 |
| 入力と最終残差のcosine平均 | 0.064781 | 0.370156 |
| 教師数加重の初期NLL | 8.359544 | 8.366678 |
| 全パラメータの勾配有限 | yes | yes |

初期NLLは改善していない。RMSの差は初期状態の局所観測で、学習不安定の証明・学習後品質・原因特定とはしない。事前CPU entry条件「両条件の勾配が有限、従来RMS比2以上、候補が従来の半分以下」は満たした。

次の学習は同じ元94,160,195教師・10,000 microbatch・10,000 optimizer更新・batch80。従来の実10,000更新checkpointと既存256DEV/80生成・採点を再利用し、候補だけをfresh学習する。元の2B教師位置scheduler、原TRAIN、draw順、CE教師、source/EOS、sampler、更新回数を揃える。初期化以外の条件を変更しない。6窓を科学学習用の反復教材にはしない。

科学学習前に候補自身のCUDA連続4対2+save+2で重み/Adam/scheduler/RNG/sampler/会計/初期化metadata/全更新履歴・有限値・VRAMを検証し、検証重みを捨てる。CPUの実更新・全状態resume・変更行列/RNG/tie・異種checkpoint拒否の5 testsは2.91秒で成功済み。これらはGPU/品質の証拠ではない。初期化状態は別kindで保存し、旧checkpoint loaderへの混入を防ぐ。

累積GPU上限は1,992秒。従来の実10,000 microbatchの1,301.472520秒からceil(1.3倍+300秒)で算出し、own CUDA gate・学習・save・候補評価を含む。有限の実測予算であり、Base完成時間ではない。永続launcherは既存科学process不在・元UIの実process/HTTPの親とidleを確認してからUIを停止し、終了時に元10Bへ復帰する。

同256DEV・固定80 prefix/greedy64を評価し、新しい80件すべてを原生成と理由付きで個別採点する。旧control80の原採点は保持し、都合のよい再採点をしない。探索screenは事前に固定したBPB2%以上改善、文法2/一貫性2/適切完結/EOSの各件数を悪化させない、反復を増やさない、Unicode/role/empty0のすべて。対応文書byte加重BPBと対応生成の一貫性差CIを報告する。独立人間blindではない。

不合格ならこの固定条件を閉じ、LR・係数・seed・capを変える救済や自動2B延長をしない。合格してもBase採用とはせず、元の絶対品質・歴史Web保持・独立した学習seed43・fullDEV・protectedTEST・採用条件を維持する。原モデルコード、古い失敗・全raw/notes/重みを保存する。

実行: `scripts/run_base_residual_initialization_pilot.ps1`。再開は記録された実PID/boot/start不在と閉鎖台帳・valid checkpointを確認してから同scriptの`-Worker`。CPU集計はWSLで`env CUDA_VISIBLE_DEVICES= .../uv run --frozen --extra hub --extra data --extra ml --extra export scripts/review_base_residual_initialization_pilot.py`。現在の実状態は`docs/autonomous_status.md`とactive_jobを参照し、計画を実行証拠として扱わない。
