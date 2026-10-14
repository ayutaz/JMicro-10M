# 根本原因診断の結果と次の修正計画

2026-10-05 JST。契約71の三項目（計画70内部0〜2）を完了。**EOSの無効化や二重shiftを主原因とする証拠はなく、自然文の学習分布・展開能力と、狭い教材で得た能力の汎化不足を優先する。** BF16の数値契約は一部不成立のまま記録したが、FP32でもoriginal/mixedの停止/反復件数は変わらない。品質問題は未解決。新しい学習は0。

## 実施した範囲

三つの実checkpoint SHAを固定し、Web8・旧物語pool由来8・既存compact反転ペア16のtrain入力を使用。正解の続き/文末と自由生成を比較した。greedyと既存sampling条件（temperature0.8/top-p0.9、seeds42/43/44）、各64token、計384出力。数値差の追跡にFP32 greedy96出力を追加。既存dev80や旧512延長は再実行していない。

GPU占有は主診断56.513秒＋精度追跡6.927秒＝**63.440秒**、事前上限600秒以内。CPU4tests成功。optimizer更新0、全checkpointのSHAを終端でも確認した。診断コード、準備、原文確認/報告の時間はGPU占有とは別。UIを一時停止して単一GPU lockを使用、両jobは完了・不在、元10B UIへ復帰済み。

| 重み | 累積入力学習tokens | 役割 |
|---|---:|---|
| original | 10,000,007,168 | 現在の元UI、通常Web学習 |
| mixed | 10,100,572,160 | 結果69の混合shuffle候補 |
| story | 10,500,014,080 | 既存coherent20の物語混合枝 |

mixedの累積入力と科学body/EOS教師100Mは計数が異なる。Web準備量は12,225,819,077、物語比較用poolは200,000,192、compactは55,273準備tokens。用意した量と各重みが実際に消費した量を同一視しない。storyは旧59,963,449-token物語poolで学習した既存枝であり、200M候補を新しく学習したモデルではない。

## 1. 実装・精度

全32件のBOS/本文/EOS、x/y一位置shift、PAD教師除外を確認。実Trainerはshift済みyをCEへ渡し、modelの内部label shiftを呼ばない。EOS ID3は生成抑制対象に含まれず、実際に条件教材の回答後に出た。

元10B実重みのCUDA FP32 mathで64/1024実streamを比較した。fullとcausal fastのlogits/CE/代表三gradientは同一。cacheと独立HF NoNorm referenceは元のFP32許容範囲内。padding対単独は8,495,104要素中1要素だけ閾値外、最大差2.9564e-5。**このcheckは失敗として保持**する。微小な浮動小数点差があり、全経路の厳密一致を宣言しない。

BF16 math対FP32、Flash対math、compiled Flash対eagerは、固定atol0.05/rtol0.02のlogit契約を一部超過した。最大差は全32教師のFP32/BF16で0.35198、compiled/eagerで0.28125。数値7checksを失敗として保持し、thresholdを変更していない。BF16代表gradientは全てfinite、Flash/math cosine最小約0.999803、compiled/eager約0.999812。これに新しい合格基準を後付けしない。

そこで同じ三重み/32入力のFP32対BF16を別契約で追跡した。平均次token確率のtotal variationはoriginal0.00609/mixed0.00391/story0.00663、teacher平均NLL差の各最大は0.02479/0.00706/0.01189nats。正しい文末のEOSがtop1かどうかは三重み合計96件で変更0。全文対chunk cacheではEOSの細かな順位変更が4/1/1件あり、precisionによる微差を隠さない。greedyの全token一致は28/31/26件（各32）なので、精度で個々の文章が変わる場合はある。

FP32のgreedy EOS件数はoriginal0/mixed16/story13（各32）、BF16も同じ。4gram反復marker件数はFP32が32/16/23、BF16が32/16/24で、storyの物語1件だけmarkerが変わる。**精度の違いだけを修正してoriginal/mixedの自然文の主要な失敗が消えるという仮説は、今回のsampleで支持されなかった。** current mixed/storyの全Flash gradient/HF照合は再実施しておらず、学習trajectoryへの長期精度影響は未分離。数値契約の検討は残件だが、BF16全体を新しい品質改善として自動変更しない。

## 2. EOSと反復の発生点

表の文末確率は各本文を正しく最後まで与えたときの**算術平均**。以前のEOS mean NLLから求める幾何平均と区別する。全てtrain診断であり、独立dev性能ではない。

| 重み/対象 | n | 正解文末EOS平均確率 | 文末EOS top1 | greedy EOS | greedy 4gram marker |
|---|---:|---:|---:|---:|---:|
| original / Web | 8 | 14.52% | 1/8 | 0/8 | 8/8 |
| original / 物語 | 8 | 4.27% | 0/8 | 0/8 | 8/8 |
| original / compact | 16 | 0.49% | 0/16 | 0/16 | 16/16 |
| mixed / Web | 8 | 13.85% | 0/8 | 0/8 | 8/8 |
| mixed / 物語 | 8 | 5.82% | 0/8 | 0/8 | 8/8 |
| mixed / compact | 16 | 99.989% | 16/16 | 16/16 | 0/16 |
| story / Web | 8 | 16.14% | 2/8 | 0/8 | 8/8 |
| story / 物語 | 8 | 81.40% | 8/8 | 8/8 | 4/8 |
| story / compact | 16 | 1.99% | 0/16 | 5/16 | 12/16 |

4gram markerは今回の開始位置追跡用。正常な語句の再使用にも反応し、既存の重度反復率/品質gateとは別。storyの物語はまとまった自然な文章もあり、marker4/8を意味破綻4/8と解釈しない。Webは7/8でgoldの残りが64tokenより長く、64までにEOSがないこと単独では問題を証明しない。その前に明確なloopへ入った分布と原文を根拠にする。物語8件とcompact16件のgoldは64以内。

具体例:

- `web-6356293861`：正しいPoisson説明の末尾ならoriginalのEOS確率43.21%、順位1。自由生成では最初のtokenでequationよりNewsを選び、同じ見出しへ戻る。二度目の4gramが完成するstep25（0始まり）では選択token確率99.66%、entropy0.0352nats、EOS確率2.93e-7。正解の文末へ辿り着かず、非常に確信の強いloopへ入る。
- `web-1117927279`：originalはデータベースのデータベースを作成するという列挙を繰り返す。step10の選択確率99.86%、entropy0.0134、EOS1.82e-7。正解本文の末尾EOSは23.33%、順位2で、newlineの35.02%が優先される。自力展開の崩れと、文末で改行を優先する傾向が両方ある。
- `story200m-52355646`：originalは星の上に立つ星の定義のloop。正解末尾EOS4.11%、順位2、newline34.40%。story枝は同じ正解末尾EOS94.81%、順位1で、自由生成も星から夢への助言を受けて完結する。話者の彼女はprefixで明示されず、完全な意味保持とまでは判定しない。
- `story200m-20607202`：story枝は智史の祝い→友人を招く→お菓子を共有→絆というまとまった別の続きを生成しEOSで止まる。goldと異なる最初のtokenはstep0だが、それを意味破綻と扱わない。自然文を短く展開する能力が現在の10M構成に全くない、とは言えない。
- `train-reference-0000`の反転両方：mixedはなお/なつの保持者を反転に合わせて答え、EOSまでgold完全再現。全16条件例はgreedy/sampling三seedの全てで完全再現。停止実装と狭い条件学習は動作する。originalは質問を繰り返し、storyでは無意味な列挙/改行でもEOSが出るため、停止だけで品質を採用しない。

samplingはoriginalの自然16件でEOS seed別0/0/3、mixed1/2/1、story6/7/8。loop軽減や停止の変化はあるが、原文の意味評価と独立して数だけを改善としない。今回の上限/入力は旧dev80と異なり、既存結果37/42/69の採否を置き換えない。

## 3. 教材と目的の適合

Web64全文、200M物語pool64全文の原文を読み、各id/text SHA付きの理由を保存した。token位置・長さ層別の抽出は一様な文書sampleではなく、corpus全体の不良率を推定できない。Web内の細かなbucketは未分離。物語は先頭旧59,963,449tokensがSimpleStories-JAで、後半がTinyStories-JA翻訳追加（builderのcopy-then-appendとmanifestで区分）。sampleの32/32がそれぞれに対応する。

Webには、自然な解説/実体験に加えて、メニュー、企業宣伝、表、操作手順、辞典見出し、引用、フッターが多様に混ざる。`web-2560230148`は割合の数字4で切れ、`web-9108063504`は花という見出しで終わる。`web-9064898382`は続くと予告してEOSが付く。`web-4131594050`は記事本文後に別記事見出し十件が連なる。これらの文書EOSは自然な短文の意味的完結と同じ教師ではない。長い文章の終端だけを学ぶことと、短いprefixからまとまった続きへ進むことにもずれがある。

物語は短文完結の形に近いが、内容品質は一様ではない。翻訳の`story200m-104160816`は停止指示に従う教訓なのに最後が手を止めないと反転する。`story200m-172039396`は子どもと普通に遊ぶ場面を悪事への抵抗に結び付ける。`story200m-130582435`は食料の注文と宝の報酬を結び付け、因果が欠ける。旧SimpleStoriesにも風車の秘密を友達と書いた石に置き換える例などがある。長さ/句点/重複のfilterだけでは、対象同一性・指示の肯否・因果の正しさを保証できない。

manifestからBOSを除いた本文/EOS教師1000tokensあたりのEOSはWeb2.121、200M物語5.844。これは全準備poolの密度で、混合モデルが消費したteacherの密度と区別する。EOSを重くするだけでは、話題/因果の誤った展開を改善する証拠にならない。

4k/8kの同じ32全文7,822bytesでcodecは全件lossless。body tokensは2,042→1,793（約12.2%減）。byte破壊を確認していない。語彙配分の効果は残るが、Tokenizerの変更/再訓練を即座の解決とする証拠ではない。

## 原因順位と次の二条件

1. **自然文の展開・完結を学ぶ分布と目的のずれ、狭い学習の汎化不足**。mixedのtrain16成功と自然16loop、storyのtrain短文への改善が強い根拠。広いWebの予測を多く学んだ量だけで、求める短文生成を保証できない。
2. **自己生成でloopへ入り、その続きを過信する確率分布**。teacherとfreeのEOS/entropyが大きく異なる。samplingは一部変えるが、既存の品質gateを満たす修正ではない。
3. **教材の抽出末尾/因果・条件品質と文書連結の文脈依存**。今回の全文例と結果67/69が支持する。EOS密度・source・長さ・被覆は交絡し、一要因の因果は未確定。
4. **精度経路の差**。固定契約は失敗を残すが、FP32でも今回の主要件数が同じ。主因としての優先度は下がった。容量・optimizer履歴・最適化不足はまだ独立に切り分けていない。

最小の次案は、大量のcorpus増量前に、現在の構成/出発重みが意味の通る自然短文を生成まで学べるかを、小さな陽性対照で確かめること。**次の学習は未開始。**

| 次案 | 目的 | 固定する条件/提案予算 | 終了条件 |
|---|---|---|---|
| A：元10B＋Adam引継ぎ | 自然短文を記憶・適切停止できるか | 意味/指示/因果を原文確認した64全文、1文書1行、PAD教師除外、各8M body/EOS教師 | train teacher正答、適切EOS完結、固定goldの完全再現が各90%以上 |
| B：同じ元10B＋fresh Adam | 同じ初期重みでoptimizer履歴の影響を分離 | Aと同じ教材/順序/境界/LR1e-4/scheduler/教師予算。Adamのmoment/stepだけ変更 | A/B差を測定。予算内失敗なら容量不足と断定しない |

これは覚えられる一意の短いtrain continuationに対する診断で、自由作文の唯一正解を要求する一般品質gateではない。LR/最適化はなお別要因で、両失敗なら計画70の現在構成を新規初期化したC（提案8M）へ進むかを結果から判断する。未学習の自然文を別に固定してtrain記憶と汎化を分ける。二枝の提案教師計16M、GPU占有上限10分は開始前に契約化し、未測定の案として扱う。

記憶対照に成功したら、多様で因果の通る完結単位の教材と従来教材を同じ出発点/教師予算で各25M比較する。source/長さ/EOS密度を揃えられない場合は、品質/構成を含む変更と明示する。境界を比較する場合は末尾の教師被覆を一致させる。固定dev80の一貫性/適切完結/条件保持を評価し、元の採用条件（一貫性+8/80かつ対応95%下限>0、各27/80、EOS37/80、反復18/80以下、BPBとWeb比較）を保持する。今回のtrain sampleを独立devへ昇格させない。増量/20B/設計拡大はまだ開始しない。

## 保存・停止

凍結準備はlocal commit `d83ffa7`。主run `reports/phase6/root-cause-20261005` にcontract/job/numeric/三重み各teacher・生成全step/precisionを保持。可搬rawは[圧縮bundle](../reports/phase6/root_cause_traces.json.gz)で、元JSON文字列をSHA一致で復元できる。[summary](../reports/phase6/root_cause_summary.json)、[全文確認](../reports/phase6/root_cause_corpus_review.json)、[完了確認](../reports/phase6/root_cause_completion.json)とCPU XMLを保存。元重み/Tokenizer/core/過去結果は変更していない。

元UI actual PID374638/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start8753669、HTTPの元checkpoint SHA410f975d…/学習10,000,007,168/busy=falseを確認。初回集計はUIのstart_ticksがstringなのに整数と比較して停止したが、型変換だけ修正して完了した。再GPU/再学習0。ここで三項目の診断・計画・local commitを完了して停止する。自然文記憶対照、修正学習、20B、Chat、protected test、pushは未開始。
