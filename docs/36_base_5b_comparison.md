# 5B学習済み10Mモデルの比較結果

2026-10-04、依頼された比較を完了。本文の予測精度は改善したが、自然停止・反復・内容の品質目標は未達。10Bへ進める元条件も不合格として保持し、記録とコミットで停止する。

## 共通条件

モデル10,001,152 parameters、準備済みtrain12,225,819,077 tokensは共通。今回は学習を追加せず、5B最終checkpointだけを評価した。元2B/低LRWeb100M/short20の保存済み評価を再利用し、全89,416 dev文書のID/本文164,344,743 bytes/42,003,934 tokens、全400生成keysが同じことを照合した。testは使わない。

全文BPBはcontext1024/stride512/batch16、CUDA BF16/Math attention/FP32 CE、本文をちょうど一回採点。BPBは同じ本文bytes当たりの損失で小さいほど良い。固定生成はdev80prompt、最大64新規tokensのgreedy・特殊role抑制あり。追加条件はgreedy抑制なし、samplingのseeds42/43/44（temperature0.8/top_p0.9）で計400。EOS bias/強制停止/反復penaltyはない。

## 結果

| 条件 | 累積学習input tokens | 全文BPB↓ | 固定EOS | 固定反復 | 固定Unicode失敗 |
|---|---:|---:|---:|---:|---:|
| 元2B | 2,000,027,648 | 0.982881558 | 0/80 | 60/80 | 0/80 |
| 低LR Web100M | 2,100,035,584 | 0.972968729 | 0/80 | 55/80 | 0/80 |
| 5B Web100% | 5,000,003,584 | 0.964484070 | 0/80 | 59/80 | 1/80 |
| 低LR short20：別mixtureの参考 | 2,100,035,584 | 0.974799263 | 27/80 | 41/80 | 0/80 |

5BのBPBは元2B比約1.87%、低LRWeb比約0.87%改善した。データセット量は増えておらず学習量が増えた比較。ただし2B対5Bで最終5%decayの期間が変わり、低LR100Mの曲線も異なるため、全差を学習量だけの因果効果とは断定しない。short20は短い完結文を混ぜた別条件であり、純粋な学習量対照ではない。

| 条件 | 全400 EOS | 全400反復 | 全400 Unicode失敗 | 全400 empty/role |
|---|---:|---:|---:|---:|
| 元2B | 6/400 | 122/400 | 0/400 | 0/0 |
| 低LR Web100M | 5/400 | 119/400 | 0/400 | 0/0 |
| 5B Web100% | 5/400 | 122/400 | 2/400 | 0/0 |
| 低LR short20参考 | 225/400 | 84/400 | 0/400 | 0/0 |

5Bのsampling3seedsのEOSは3/0/2件、反復1/0/3件。全400は異なるdecodingの合計であり、固定greedy80の停止率とは分けて扱う。

## Unicodeと内容の確認

Unicode失敗はbase-070「会議室『楓』に入ると、すでに」の同一greedy出力を抑制あり・なしで数えた2件。保存済み64 generated IDsのdecode bytesは170bytesで、末尾e6a5が未完了のUTF8文字となり、strict decodeはbyte168〜170でunexpected end of data。末尾以前は有効UTF8で、最大生成tokensでbyte fallback文字の途中に達したことが原因。評価の失敗を免除したり上限を延ばして結果を置き換えたりしない。

新固定80出力を全て読み、[13例の同一promptでの比較](../reports/phase6/base_5b_content_review.json)を保存した。base-092の電気を「消す」から「つける」、base-100の靴を「脱ぐ」から「履く」は冒頭改善。しかしその後は反復する。base-051のりんご3−1、base-057の玉2+1、時刻の関係、甘いものを食べない条件、雨が吹き込んだ窓への対応で誤りが残る。base-099は低LRの「乾いた靴下」から5Bの「布団」へ悪化した。

元反復指標は三回完全一致のsubstring検出を維持。falseでも二回/言い換え反復が残ることを例として記録した。これは独立した人手blind採点や総合正解率ではない。本文BPBの改善を文法70%やChat停止95%の達成証拠にはしない。

## 判定・保存

元の増量条件は各対照に対しBPB≤対照+0.001、固定反復<対照+8、新empty/role/Unicode失敗なし。BPBと反復の数値条件は通るがUnicodeで不合格。EOS0/80と内容誤りも未解決のため、10B/Chat/新しいmixture・decoder sweepに自動移行しない。改善した本文予測候補として5Bと旧条件の全weightsを保存する。

GPU累積788.433秒（13分8秒）で上限1800秒以内。本文377.329秒、生成409.343秒。実Linux477とWindows26484は終了、GPU compute processなし。source/core/Tokenizer/checkpoint/参照hash保持、有限値・本文一回採点・400生成flags・model/RNG/mode分離等の[CPU確認18項目](../reports/phase6/base_5b_comparison_review.json)が成功。追加GPU再実行や学習は行っていない。

正本はWSL repoの`reports/phase6/base-5b-comparison-20261004/`（job.json/full-dev.json/generation.json/result.json/aligned-content.json/source snapshot/pipeline.log）。重みは`reports/phase6/base-5b-20261004/decay/checkpoint-00152588.pt`、SHA256 `1d8e5274e1662063dedec355def1da3c9bcc972499a12b608c25c71b6758273a`。完了jobを再起動しない。次回はEOS・反復とUTF8末尾処理の改善を優先する。
