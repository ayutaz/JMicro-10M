# 日本語Baseモデル評価の棚卸しと改善案

2026-10-04。ユーザー依頼は「ほかの評価も追加し、日本語Baseモデルとして正しく評価できるようにする。まず現在の評価と改善部分を洗い出す」。今回は実装・保存結果の棚卸し、一次資料の調査、追加仕様案までを完了した。新しいbenchmarkのモデル採点・追加学習・test採点は行っていない。[CPU棚卸し記録](../reports/phase6/base_eval_inventory_20261004.json)。

**結論: 現行BPBの計算と同条件比較には根拠があるが、日本語の意味・話題維持・一貫性の測定が不足している。元の数値gateは次の候補を選ぶ条件であり、「意味の通る日本語を生成できた」という合格ではない。** 10Bは本文BPB0.954018、固定greedy EOS0/80・反復53/80で、[品質未達](42_base_10b_quality_evaluation.md)。

## 現在の測定と不足

| 項目 | 実装・実測済みの部分 | 不足と改善箇所 |
|---|---|---|
| 本文予測 | `evaluation.bits_per_byte` / `readiness.evaluate_batched`。同じdev89,416文書・164,344,743 bytes、本文を一度採点、EOSは別損失 | 全体のBPBは意味の正しさ・自由生成を測らない。長い文書の影響、source/domain/長さ/短文別の差と日本語外部データの汎化を追加 |
| 自由生成 | `training.generate_suite`。dev80 prefix×5条件、greedy抑制あり/なし・sampling3 seeds、最大64 tokens。raw IDs/textあり | 400出力は80入力の繰返しで、400独立問題ではない。UIの128〜512 tokensに対応する崩れを測っていない。追加長文生成は別条件として記録 |
| 文法・意味 | 0/1/2 rubricと11設計例、10Bの全80と自然EOS9件をCodexで内容確認 | 保存400件の`human_scores`はすべてnull。文法70%の原目標を実測していない。文法・prefixとの関連性・文間一貫性を独立採点し、率と分母を保存 |
| 問題ごとの条件 | Base devは10 category×8件、`checks`を保存 | dev80件の`checks`はすべて同じ3つの説明文。自動採点には未接続。否定・数値・時刻・人物保持の明示ラベル/正解候補を持つ新診断suiteが必要 |
| 日本語の文法知識 | 固定grammar prefixが8件 | 助詞・格・語順・係り受け等の最小対、容認度、現象別の定量評価がない。JBLiMPを優先、JCoLAを補助候補にする |
| 意味理解・常識 | 数字・常識のprefixを含み、誤りを内容診断 | 正答率は未測定。候補尤度によるJCommonsenseQA/JNLI、独自の否定・比較・照応診断を追加 |
| 反復 | 2文字以上の同じsubstringが連続3回以上のv1 flag | 言い換え反復・離れた同文・2回反復を見逃す。char/token n-gram helperは既にあるが主10B結果に未接続。v2で連続値、同文再出現、最初の反復位置を追加 |
| EOS | 自然停止とEOS NLLを保存。強制停止なし | EOSで止まることと意味が完結することを分離していない。早すぎるEOS・適切な完結・話題逸脱後のEOS・上限を別記録。Baseの開放的prefixにChat停止95%をそのまま流用しない |
| raw Unicode/特殊ID | raw byteからUTF8、空応答、role leakageを再照合。表示修正を合格に流用しない | 有効UTF8のU+FFFD生成を別集計していない。文書のrole 4/5/6に対しコードは7もflagに含む。v2でroleとBaseのEOTを分け、旧flagは残す |
| 集計・統計 | 文書/入力/条件の一致確認、Phase5のdocument paired bootstrap helper | 最新10B比較にBPB差CIはなく、生成category別の成績も主表にない。既存保存値からCPU集計し、prompt/family単位で生成CI。単一学習seedの限界を併記 |
| 外部比較 | 自モデル2B/5B/Web5.1B/10Bを同条件比較 | 日本語Base参照、最頻選択・random・unigram等の対照がない。「何も学習していない選択」より良いかと、既存Baseとの距離を追加 |
| 再現性・採用 | hash、固定split、RNG保全、保存状態、23 CPU evidence checks | 23 checksは採点基盤の正しさであり23言語能力ではない。実装検証/予測性能/生成品質/候補採用/実用合格を別欄にする |

元のprotocolと受入基準は[評価仕様v1](evaluation_protocol.md)、[protocol.json](../configs/evaluation/protocol.json)、[原ロードマップ](15_project_roadmap.md)。今回の案で旧閾値・旧問題・旧結果を上書きしない。

## 今回の出力が現在の指標から分かりにくい理由

パン屋の書き出しに「いけばな」「きょうだい」を繰り返す出力は、文法的に読める部分があっても話題・因果・意味の一貫性が破綻している。正しい文字コードや低いBPBだけで高品質と判定できない。teacher forcingでは正しい前文を毎回与える一方、自由生成は自分の誤った続きも次の入力にする。この差も測る必要がある。

保存済み10B400出力だけをCPUで再集計した。固定greedy80のchar 4-gram重複率は平均0.6583、中央値0.6601。4文字以上の同一文断片が再出現する出力は33/80。文断片は`。！？`/改行で区切り、前後空白だけを除いた診断であり、意味反復率や新しい合否閾値ではない。元の反復53/80を置き換えない。samplingの元反復はseed別3/2/1件でも、意味が通ることを示さない。

## 追加評価の優先順位

| 優先 | 評価 | 測る能力・方式 | 実施条件 |
|---|---|---|---|
| P0 | 既存生成の内容採点 | prefix接続の文法、話題関連性、文間一貫性を各0/1/2。否定/数値/時刻保持と反復/矛盾は別flag | まず保存された10B/Web5.1Bの固定80ずつを利用。モデル名を隠して順序を固定seedで混ぜる。Codex診断と人手blind採点は別の欄。独立人手未実施は未実施と表示 |
| P0 | 新しい基本意味診断 | 否定・数量・時間・比較・照応・日常の因果。自然なprefixに整合/矛盾した続きを対置し、候補を尤度で比較 | 6能力×20 familyの計120 family案。作成時にdev/testをfamilyで固定。言い換え/選択肢順を同じfamilyへまとめる。最頻選択と50% chanceも記録 |
| P1 | JBLiMP | 日本語統語の331 minimal pairs/11現象。容認文を非容認文より好むか | 原論文は長さ・語彙頻度を補正するSLORを使用。生の対数尤度による独自診断とは別名で記録。unigram頻度の推定元と平滑化も凍結。原論文との条件差を表示 |
| P1 | JCommonsenseQA | 日本語の5択常識。候補ごとの条件付き尤度によるaccuracy、5択のchance20%、majority対照 | まず公式devから事前固定seed/IDで200件のpilot案。その後公式dev全体。選択肢の文字列・順序・few-shot/正規化方式を固定し、独自subsetを公式全体scoreと呼ばない |
| P1 | JNLI | 含意/矛盾/中立の3択。accuracy・macro F1・ラベル別成績。chance33.3%、majority対照 | 同じく公式dev200件pilot案→全dev。BOS＋自然文形式の0-shot/少数例条件を区別。指示形式の失敗を日本語理解の失敗と同一視しない |
| P1 | 日本語domain別本文予測 | 既存Webの短文/長さ別BPB、外部の説明文・叙述・会話文等の固定reference本文BPB | 最初は最大1M UTF8 bytesの小set案。revision/source/date/hashを固定。新データが未学習とは保証せず、既存indexによる限定照合と混入不明を記録。分布ごとのBPBとbytesを併記 |
| P2 | JSQuAD | 与えた日本語文章からの読解。生成答案のEM/F1、抽出正解の条件付き損失を別報告 | 長文が1024 tokensに収まるか先に判定。除外数/回答が残るかを記録。自作選択式に変えた場合はJSQuAD公式EM/F1と混同しない |
| P2 | JCoLA | 日本語の容認度。in-domain/out-of-domain別、MCCとaccuracy | 文の確率だけに勝手な閾値を付けない。few-shot分類/補正scoreと校正devの使い方を先に固定。JBLiMPと同じ評価だと扱わない |
| P3 | JMMLU等の知識試験 | 日本語の知識・専門問題 | 基本文法・意味診断に続く能力確認用。低得点でも基本日本語能力だけの原因にしない |

JBLiMPは原著者の[論文](https://aclanthology.org/2023.findings-eacl.117.pdf)と[公開データ](https://github.com/osekilab/JBLiMP)を確認した。原論文§4.2のSLORは`(log P_model(sentence) − log P_unigram(sentence)) / token_count`。初回にtrainの固定上限sampleから頻度を求める場合はsample近似として明記し、原論文scoreの完全再現とは呼ばない。全12.23Bの再tokenize/重複照合を前提にしない。

JCommonsenseQA/JNLI/JSQuADは日本語で構築した[JGLUE](https://github.com/yahoojapan/JGLUE)、JCoLAは[原著者データ](https://github.com/osekilab/JCoLA)を参照。MARC-jaはJGLUE公式が現在配布停止を明記しているため、初回の追加対象にしない。データの利用条件と取得versionは対象ごとに確認し、benchmarkを学習poolへ混ぜない。

既存日本語Base参照の候補は[rinna/japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small)。公開cardは約0.1B規模、CC-100/日本語Wikipediaの言語モデルであり、今回の10Mとは容量・Tokenizer・学習履歴が違う。評価の参考モデルで、JMicroの規模を変更する案ではない。normalization/lowercaseを含むcodec差を確認し、同じ原文bytesを損失なく扱えない場合は共通BPBの直接比較を保留する。cardのperplexity21をJMicroのBPBと比較しない。今回、参照重みは取得・実行していない。

## Base向けの実装方針

指示に従って「答えはAです」と生成できるかだけをBaseの主評価にしない。**まず自然文/少数例prefixを与え、候補の続きの尤度を測る。別に自由生成も採点する。** 選択問題で高得点でも、今回のような自由生成の破綻を解決したとは判定しない。

JMicroは独自外部codecを使うため、既存のrandom-weight HF/GGUF artifactや通常のAutoTokenizerを現在の重みとして流用しない。現在のcheckpoint＋`jmicro.tokenizer.Tokenizer`を使うscorerを追加し、BOS・候補の先頭空白・token境界・context超過・targetだけのloss maskをgolden例と短い手計算で確認する。FP32 CE、BF16/math、EOS分離、raw evidenceを維持する。

[lm-evaluation-harnessのモデル契約](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/model_guide.md)は`loglikelihood`/`loglikelihood_rolling`/`generate_until`。この契約へ独自adapterを用意する方向が適合する。まず小さいnative scorerで候補境界とmaskを確認し、使うtask/template/commitだけを固定して接続する。[llm-jp-eval](https://github.com/llm-jp/llm-jp-eval)の日本語データ定義とBase用few-shot設定も照合する。同projectはbenchmark高得点だけで実利用の優位を断定しないよう注意しており、JMicroでも自由生成を併記する。tool/依存の大規模入替を採点の前提にしない。

選択肢全文のlog likelihood、token長補正等はtaskごとに方式を固定して別名で報告する。結果を見て都合の良い正規化やpromptだけを選ばない。0-shotとfew-shot、選択肢順変更は別条件で、label priorの影響を記録する。Chat template/role IDはBase採点の既定にしない。

## 改善実験へつなげる判断

| 追加評価の結果 | 最初に疑う部分 | 対照比較の候補 |
|---|---|---|
| 文法minimal pair/短文BPBが弱い | 日本語表現・構文を学習できていない | 一貫した短文のdata mixtureを同じ追加tokensで比較 |
| 文法は比較的保つが否定/人物/数量が弱い | 条件や関係の保持 | 意味関係を含む自然文dataの適合性を比較。単にEOS teacherを増やすだけでは合格としない |
| 候補を正しく選ぶが自由生成はループする | 自由生成中の誤り蓄積・反復・終端学習 | cleanな完結文mixtureを元Webと比較。decoder抑制実験は別の推論policyとして計測 |
| teacher EOS損失は改善するが適切な完結が増えない | EOSの位置・早すぎる停止・話題逸脱 | EOS率と内容の完結を同時採点し、空/逸脱終了を成功扱いしない |
| 多数の基本課題で小規模参照との差が残る | data/最適化/容量のいずれか | 今の10Mだけから原因を断定しない。必要なら別の定義済み予算で規模比較を計画 |

これらは原因候補で、現在の出力だけから確定していない。追加評価を凍結して現在の10Bを測ってから、次の学習比較の主指標を選ぶ。

## 次の作業と完了条件

1. **CPUで既存結果を活用。** category別集計、char/token n-gram・同文再出現、生成長、paired BPB差CI、匿名化した80×2内容採点packetを追加。旧v1は不変。Codex採点と独立人手を分ける。
2. **v2仕様を凍結。** 自由生成の文法/関連性/一貫性、基本意味診断、JBLiMP/JCommonsenseQA/JNLIのtaskと入力/候補/少数例/score方式/取得条件、dev/test/混入状態、予算を設定へ固定する。v1の文法70%等は維持し、新規閾値は結果を見る前に設定する。
3. **小pilotでscorerを検証。** 各taskの数件を用い、BOS/target shift/候補境界/padding/長さ補正を確認。random/majority/unigramの対照を揃え、処理速度から本評価を見積もる。初回GPU pilot上限120秒、GPU本評価上限900秒を案とし、上限時は未完了を記録する。既存42M本文tokensの全dev GPU再採点は初回の条件にしない。
4. **同じv2で現在10Bを測定。** 必要な参照だけを追加し、score/category/分母/CI/失敗例を並べる。正式のblind人手がなければその欄は未実施のままにする。testは選定後に一度、学習や閾値調整には使わない。

初回報告の完了条件は、基盤検証と品質を別表示し、文法・意味・生成・EOS・反復の未測定欄をなくすこと（独立人手欄は実施状況を明示）、定義されたtask/pilotの全件成績とchance/majorityを保存し、次の学習比較で何を改善するか決められること。採点を実装しただけでモデル品質合格にしない。

今回の依頼は最初の棚卸しまで。Web UIは停止せず維持する。将来GPU評価を行う前にUIのactual identity/GPU lockを確認し、短時間の停止と再起動を実行計画へ含める。追加学習、評価用大規模データ取得、参照重み取得、公開/pushは今回行わない。
