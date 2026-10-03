# 500Mの反復退行・EOS・データ構成の調査

2026-10-03。既存artifactと推論のみ。学習更新0、1B未開始。[事前計画](repetition_diagnosis_plan.json)、[数値・binding・20項目監査・次の比較案](repetition_diagnosis_review.json)、[終了・同期・旧証拠保持の監査](repetition_completion_audit.json)。全102 tests成功、既存225 source/config/eval/lock/reportのraw SHA256不変。推論249.75秒（事前900秒上限以内）。

## 判断

EOS教師の欠落や、拡張データでの文書長・反復の大幅増加を支持する結果は出なかった。真の文書末尾のEOSと本文BPBは改善している。短いprefixからgreedyで生成すると同じ続きを選び続け、EOSを選ばない。短文生成とWeb文書の学習分布の違い、greedyの反復への入りやすさが有力な調査候補である。ただし、旧100Mと新500Mはデータ、露出回数、token予算、batch、schedule、学習backendが同時に変わるため、一つの原因に確定できない。

データ量が主因とは判断せず、1Bへ自動延長しない。まず同じ重みでdecoderの対照比較を提案し、その結果から短文末尾の教師構成を比較する。今回のscopeは調査・記録・commitで終了する。

## 同じ80件のgreedyと悪化の時期

| checkpoint | input tokens | 反復 | EOS停止 |
|---|---:|---:|---:|
| 旧100M・pilot/cosine/batch8 | 100,007,936 | 48/80 | 0/80 |
| 拡張stable131M | 131,072,000 | 69/80 | 0/80 |
| 拡張stable328M | 327,680,000 | 70/80 | 0/80 |
| 拡張stable500M | 500,006,912 | 70/80 | 0/80 |
| 独立decay500M | 525,008,896 | 66/80 | 0/80 |

全greedyは同じ64-token上限まで生成している。旧→最終は24件が新たに反復、6件が解消、42件が両方で反復、8件が両方で非反復。反復検出完了の文字位置中央値は44→40文字（反復した文のみの集計で、同じ部分集団の比較ではない）。

131M時点ですでに反復が多く、学習量に対する単調な悪化ではない。stable500M→decayは8件解消・4件新規、合計4件改善した。decayを全体の悪化の発生源にはできない。これらは同じseedのcheckpoint推移で、学習seed間の再現性ではない。

既存sampling（temp0.8/top_p0.9、seed42/43/44）の最終反復は11/240、greedyは66/80。旧samplingは6/240。最終samplingのEOS1/240、Unicode失敗1/240も保持する。samplingの低い反復率だけで文章の正しさや品質合格とは判断しない。

## EOS教師と実際の末尾予測

全文trainのBOS/EOS位置を確認し、保存samplerのepoch・positionと同じblock shuffleを再現した。BOSだけが教師から除かれ、実checkpointのinput−supervised tokensと一致する。block境界のEOSも数えている。

| checkpoint | EOS教師回数 | supervised tokens内の割合 |
|---|---:|---:|
| 旧100M | 214,629 | 0.2151% |
| stable500M | 1,061,096 | 0.2127% |
| decay500M | 1,114,159 | 0.2127% |

EOS学習の欠落や大きな密度低下は見つからなかった。全文同一dev89,416文書のEOS平均NLLは3.00827→2.53698、確率の幾何平均は4.94%→7.91%へ改善した。これは算術平均確率ではない。

同じ最初のdev256文書の末尾を個別推論すると、EOSがargmaxになる数は旧30、stable30、decay35。EOS算術平均確率は15.02%→14.45%→18.11%。一方、固定80短文prefix直後でのEOS argmaxは全モデル0、最終の確率算術平均は0.00247%。短文prefixは元から続きを求める入力で、真の文書末尾と同じ条件ではない。

最終の8件再現生成では、最後16tokenの平均top確率が0.8199、entropy0.9703 nats（同じ8件の旧生成は0.6524/1.7790）。EOSは全追跡stepでargmaxにならなかった。生成が進むにつれて候補が集中し、反復を選び続ける挙動と整合する。因果的な証明ではない。

## データ構成

| 全train統計 | pilot | 拡張 |
|---|---:|---:|
| documents | 18,022 | 1,604,292 |
| stream tokens | 8,398,329 | 756,087,912 |
| 平均body tokens | 464.00 | 469.29 |
| 中央値body tokens | 443 | 448 |
| p95 body tokens | 790 | 798 |
| streamのEOS割合 | 0.2146% | 0.2122% |
| seed42の2,048文書sample・512文字prefix反復 | 42 | 42 |
| sampleの平均char4gram重複割合 | 0.0911 | 0.0882 |

拡張trainはWeb 100%、bucketはcommercial_web 100%。128tokens以下の文書は0.8505%、64以下は0.0206%。短い文章を完結させる例は少なく、通常約470tokensのWeb文書と、今回の短いprompt＋64tokensの生成には長さ・内容の違いがある。短文末尾の教師を増やす提案はこの違いに基づく仮説である。

sampleのregex該当は主に点・罫線・空白・数字等で、最初に検出された反復単位が4文字以上のものは両sampleとも0件。生成の文句反復と同じ現象と断定できない。512文字sampleのため、後半・稀なboilerplate・意味の反復や、個別に暗記したsourceは除外していない。trainだけを診断し、dev/testを学習に混ぜていない。

## 生成実装・数値精度

旧と最終の同じ8caseを各64tokensまで再生成し、計16outputsすべてで既存generated IDsが完全一致した。元reportの破損や別decoderによる比較は支持されない。

同じ8caseの短いforced prefixでFP32 full/cacheを比べ、旧/最終の全16probeが元のatol1e-5＋rtol1e-4以内だった。最大絶対差は旧0.0000111163、最終0.0000085831。相対項を含む要素ごとの比較である。

BF16 full/cacheは最大絶対差0.15625/0.125、argmax差は各checkpointで1位置あった。FP32用の数値許容には収まらない結果をそのまま保持する。BF16とFP32のfullではargmax差が旧3位置/最終1位置。精度が個別のtoken選択に影響する可能性を残し、全1024context/backendの同値や、精度の因果的影響を除外した結果にはしない。凍結code・許容値を変更していない。

## 次の比較案と停止

最初は同じdecay500M checkpoint・同じ80dev prompt/64-token上限で、元のgreedy/3seed samplingとrepetition penalty1.1を別条件として比べる。最大640outputs、GPU15分上限、反復/EOS/Unicode/role/emptyの対応比較を記録する。固定20件のblind人手評価を準備するが、未実施・担当者未確保を品質合格へ変えない。元の400outputsは保持する。

必要なら、その後に同じstable500Mから原train対照と短い完全文書のmixtureを各25M input tokens、同じbatch/backend/optimizer/branch scheduleで比較する。短文20%は提案値である。文の途中をEOS扱いにせず、EOS/body教師量・bytesを併記し、dev/testを除外する。distribution介入なのでEOSだけの効果とは言えない。別loader/trainerの実装、finite・保存再開gate、独立manifest、比較条件と20分上限を確定してから起動する。既存凍結trainerを変更しない。比較の追加採否条件をJSONに記載し、元のBase品質基準は維持する。

上記は次回案で、今回開始していない。学習・GPU jobは終了。raw data sample・generation trace・source/plan hash・PID/boot/start_ticks・log・tests.xmlはLinux `reports/phase6/repetition-diagnosis-20261003/`に保持する。過去の500M学習/evaluation artifactは変更していない。
