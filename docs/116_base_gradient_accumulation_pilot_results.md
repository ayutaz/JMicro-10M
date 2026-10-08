# 同stream勾配蓄積pilotの結果（2026-10-08）

Baseは未完成・未採用。Chat、SFT、量子化には進まない。今回の固定条件は不採用として閉じる。

同じfresh seed42・10,001,152パラメータ・原教材・最初の10,000 microbatchについて、従来の毎microbatch更新と4 microbatchを教師数で加重してまとめる更新を比較した。従来checkpointを再利用し、候補だけ94,160,195教師を新規学習した。候補は2,500 optimizer更新。教師、元BODY bytes、token digest、source/EOS数、sampler、最終scheduler教師位置が一致した。更新頻度に伴いgradient noise、clip、momentum、weight decay、LRの離散化も同時に変わるため、weight decay単独の因果比較ではない。

| 同256文書DEV・生成各80件 | 従来 | 4 microbatchまとめ |
|---|---:|---:|
| BPB（低いほどよい） | 1.290203 | 1.279762 |
| 文法2 | 28 | 24 |
| 一貫性2 | 2 | 1 |
| 適切な終わり方 | 3 | 3 |
| EOS停止 | 13 | 14 |
| 自動反復 | 49 | 55 |
| Unicode異常・role漏出・空出力 | 0 | 0 |

BPBは約0.81%改善した。文書を対応させたbyte加重差の95% bootstrap CIは[-0.012982, -0.007831]。ただし、事前に固定した「BPBを2%以上改善し、各生成品質数を悪化させない」探索screenを満たさない。一貫性の件数差は-1、率差CIは[-0.0375, 0]で、独立した有意悪化の証明とはしない。全160件を原生成とprefixを含めて個別確認し、raw SHAへ結び付いた理由付き採点を保存した。AIによる非blind評価で、人間による独立評価ではない。

実CUDA連続対save/resumeの14 checksはすべて一致。検証の8 optimizer更新・32 microbatch・312,468教師は科学学習と別会計。GPU使用は実測1,624.021秒、上限1,992秒以内で台帳を閉じた。科学process113216/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start7412540は終了。元10B UIを114137/start7575369で復帰し、実processとHTTPの親checkpoint SHA410f975d…・10,000,007,168 tokens・busy=falseをCPU集計時に確認した。

証拠は `reports/phase6/base_gradient_accumulation_pilot_completion.json`、同prefixのresult/job/control_evaluation/candidate_evaluation/control_notes/candidate_notes。重みと約80MBの更新ログはWSL native runに保持し、Gitへ含めない。関連CPU fixturesはtrainer3件、review2件が成功済み。今回の終了処理で同じ学習・採点・GPU評価は繰り返していない。

この94.16M教師pilotの不採用だけで、あらゆる学習量の勾配蓄積や10Mモデルの能力を否定することはできない。ただし、この固定条件を自動的に2Bへ延長したり、LR・蓄積数・予算を変えて救済したりはしない。元のBase品質・保持・独立した学習seed43・fullDEV・protectedTEST・採用の条件は未達のまま。

次は既存17比較の意思決定表へ今回の結果を反映し、教材量または学習量のどちらを次に比較するか一つに絞る。新しいGPU試行は同一条件の対照、教師量、終了条件、実測予算を事前に固定してから行う。現在、科学GPU jobはない。Baseが証拠を伴って完成した時点でユーザーへ通知して停止する。
