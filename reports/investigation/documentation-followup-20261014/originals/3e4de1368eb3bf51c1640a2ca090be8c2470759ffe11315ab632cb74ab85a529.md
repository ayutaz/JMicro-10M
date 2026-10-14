# AdEMAMixの100M教師tokens比較（2026-10-07）

実学習、自動評価、生成80件の個別確認を完了した。この条件は不採用。品質基準を満たすBaseの完成・採用には至っておらず、Chat/SFT/量子化は開始していない。

元の10Bモデルから、既存の同じ約2B-token教材を使い、Web75M・教材20M・物語5Mの計100,000,000教師tokensを17,698更新で学習した。新しい固有教材の追加は0。対照のAdamW/CEは保存済みの同100M結果を再利用し、再学習・再採点していない。元sampler位置・全入力digest・source/EOS・教師・更新など11項目が一致した。

| 同じ親・同じ追加100Mの条件 | BPB↓ | 文法2/80 | 関連2/80 | 一貫性2/80 | 適切完結/80 | EOS/80 | 自動反復/80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 保存済みAdamW/CE | 0.998487 | 44 | 25 | 2 | 2 | 19 | 45 |
| 保存済みMuon | 0.999279 | 52 | 26 | 1 | 2 | 24 | 45 |
| 今回AdEMAMix | 1.075610 | 18 | 23 | 1 | 3 | 13 | 46 |

共通472,055 bytesのDEV256文書、日本語の意味192/JBLiMP331/JCQA1119、同じgreedy・最大64tokensの固定DEV80を使用した。今回の選択式正答率は61.458%/78.852%/36.908%、Unicode破損・role漏出・空出力は各0/80。選択式の一部の増減を文章品質の改善と置き換えない。

同AdamW対照との一貫性の差は-1件、paired 95% CIは[-0.0500, 0.0250]。単独で一貫性の有意な悪化を証明する値ではないが、事前の改善条件を満たさず、BPB・EOS・反復も改善しない。既存の強いstaged対照に対しては一貫性-22件、CI[-0.3750, -0.1625]。絶対基準の文法56・一貫性27・適切完結27・EOS37以上・反復18以下も満たさず、元WebのBPB保持条件も未達。

全80件を非blindのCodex判定で読み、各理由を[notes](../reports/phase6/base_ademamix_notes.json)へ保存した。完全一致する過去の9件は事前に固定した参照順で既存採点を保持した。自然な別の続きや幻想表現だけを誤りとはしない。例えばbase-077の短い笑顔の場面は合格、base-019はEOS停止しても「体重は減った／減らなかった」の矛盾で不合格。これは独立した人間・blind評価ではない。

科学学習と自動評価のGPU占有は1,866.856822秒（約31分7秒）、検証9.068181秒を含め1,875.925003秒。科学上限3,199秒・総上限4,800秒内で終了した。47検証更新/273,521教師tokensとstress backward24,576位置は科学100Mへ加えない。actual PID1816/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start100189の終了とlauncher exit0を確認した。

終端checkpointはWSLの`reports/phase6/base-ademamix-comparison-20261007/ademamix/checkpoint-00017698.pt`、SHA256は`a96c73161e006a64a48477eed32fc990a2664a4f3f1f844fc3ebbe63c63d88e6`。full optimizer/scheduler/RNG/sampler/stateを保持し、完了更新17,698件の有限lossと会計を確認した。古いheartbeatの99,900,395教師/17,680更新は終端値ではない。

[採否](../reports/phase6/base_ademamix_comparison_review.json)、[終了記録](../reports/phase6/base_ademamix_comparison_completion.json)、[可搬manifest](../reports/phase6/base_ademamix_comparison_evidence_manifest.json)を保存した。可搬67ファイル/107,102,576 bytes、圧縮45,755,220 bytes、SHA256 `7354c5a2860792059afa15ec2e79926cae93f4905471905b4d252eb17cad6971`。Windowsへコピーしmanifest/archiveと照合、tensor/corpusはarchiveに含めずnative側に保持する。

元10B WebUIはactual PID2758/同boot/start287335へ復帰し、実processとHTTPの親SHA410f975d…・10,000,007,168学習tokens・busy=falseを確認した。UIは今回の不採用候補を配信しない。

このalpha2/betas/warmup1000/LR/親/教材/教師/予算の固定条件を終了し、パラメータ調整で救済しない。単一成熟親からのoptimizer切替・単一学習seedの結果で、全AdEMAMixの無効や10Mの容量限界とは断定できない。同じ名目LRでも実更新方向・大きさは異なる。凍結reviewのlimitationsに残る「heuristic update RMS」はMuonから継承された不正確な記述であり、今回のAdEMAMix実装はRMS再スケーリングを行わない。科学sourceと凍結証拠は書き換えず、この点をここで訂正する。

次は保存済みBase比較の親・教材量・教師量・初期化・各品質基準を整理し、同条件の再試行を避けて未検証の原因を一つに絞る。追加GPU前に対照、測定予算、完了条件を定義する。資格ある候補だけ独立した学習seed・full DEV・保護TEST・採用へ進む。品質Baseが実際に完成したら通知して停止し、Chat/SFT/量子化へ進まない。
