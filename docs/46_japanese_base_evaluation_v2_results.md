# 日本語Base評価v2.1の結果

2026-10-04。[計画と採点仕様](45_japanese_base_evaluation_v2.md)を実装し、現在の10M/総10B学習済みcheckpointをWSL/RTX4090で測定した。[集計・証拠確認](../reports/phase6/japanese_base_v2_review.json)。追加学習0、公式test未取得・未採点。**統語の選好と一部の常識は測れるが、意味関係の保持、自然な文章の展開・停止は弱い。Baseの実用品質は未達のまま。**

## 公開課題と基本意味診断

主成績は候補全文の条件付き尤度。ただしJBLiMPはtrain先頭2M token IDsのadd-one unigramで補正したsample SLOR。原論文の全train頻度による再現とは呼ばない。括弧内は入力familyを再標本化した95%区間。accuracyだけでクラス分類に成功したとしない。

| 条件 | 件数 | 主accuracy | chance / train最頻回答 | 読み方 |
|---|---:|---:|---|---|
| JBLiMP sample SLOR | 331対 | 74.62%（70.09–79.46） | 50% / 該当なし | 11現象の最小対に選好あり。生の文尤度は75.83%、unigramのみ40.48% |
| JCommonsenseQA | 1,119公式dev | 30.38%（27.70–33.07） | 20% / 21.18% | chance・最頻回答より高いが大半は誤答。token平均の副成績30.65% |
| 基本意味診断 | 96 family・192 dev | 59.38%（54.69–64.08） | 50% / 50% | 独自の合成診断。二つの文脈で同じ候補の正解を反転させる |
| JNLI 0-shot | 2,434公式dev | 14.34%（12.66–16.04） | 33.33% / 55.46% | 回答語のpriorに強く偏る。MCC0、macro F1 0.0836程度 |
| JNLI 3-shot | 2,434公式dev | 14.59%（12.91–16.33） | 33.33% / 55.46% | MCC0.0224、macro F1 0.0889。理解できた証拠にしない |
| JCoLA in-domain 2-shot | 865公式dev | 74.80%（72.02–77.57） | 50% / 83.93% | MCC−0.0373。多数派より低く、容認度を判別できたとは言えない |
| JCoLA out-domain 2-shot | 685公式dev | 68.47%（64.96–71.68） | 50% / 73.28% | MCC0.0053で判別力はほぼ見られない |

JCoLA 0-shotはin20.00%/out31.24%も測定して保存した。JNLIのtoken平均では0/3-shotとも55.46%だが、最頻回答と同じで改善証拠ではない。結果を見て高い正規化方式だけを主成績へ変更していない。ラベル語を続ける形式への対応も含む評価なので、この低成績だけから日本語理解の全体を断定しない。

基本意味診断の内訳は否定100%、数量62.50%、時間43.75%、比較46.88%、照応53.13%、因果50%。否定は単純な文の対応をコピーできる課題であり、広い否定理解の証明ではない。**二つの文脈を両方正答したfamilyは23/96＝23.96%（15.63–32.29）**で、独立randomの期待値25%を超える証拠はない。片方の答えに固定したモデルはこの両方正答で0になる。合成suiteは語彙familyを分けるが同じtemplateを共有し、専門家による妥当性確認は未実施。数量の助数詞は一律「個」で、文具等の名詞ごとの自然さを統制していない。数量成績を純粋な算術能力として扱わず、次版では助数詞と自然さを事前確認する。

JSQuADは事前seed固定の公式dev100件で、context超過の除外0。独自normalized EM0/100、**文字F1 12.69%（9.54–16.12）**。正答のteacher-forced尤度を生成成績とは別に保存した。形態素単位の公式F1や公式全体scoreの再現ではなく、prompt・64-token生成・答案切出しを含む小さい読解診断である。

## 生成・反復・停止と本文予測

保存済みWeb5.1B/10Bの固定80ずつを、モデル名を除いたpacketで順序をseed固定して混ぜ、全160原文をCodexが0/1/2で採点した。[全件理由](../reports/phase6/japanese_base_content_annotations.json)。単独Codex診断で、独立人手blind採点ではない。

| 固定greedy64 | 文法2点 | prefix関連性2点 | 文間一貫性2点 | 三項目すべて2点 |
|---|---:|---:|---:|---:|
| Web5.1B | 38/80（47.50%） | 31/80（38.75%） | 0/80 | 0/80 |
| 10B | 38/80（47.50%） | 25/80（31.25%） | 0/80 | 0/80 |

文法は局所構文、関連性は人物・条件・話題保持、一貫性は意味の通る展開を別に判定する。capによる最後の未完成語だけで文法0とはしないが、未完の従属句だけが繰り返される出力は部分的な文法1とする。一貫性0は今回の強い循環・矛盾の診断であり、新しい入力での成功確率が厳密に0という意味ではない。元の文法70%の人手目標にCodex成績を代入しない。

現在10Bの20 dev prefixを各128/512 tokensまでgreedy生成した。自然EOSはどちらも0/20。char 4-gram重複率平均は**128で83.26%、512で95.76%**、同じ文断片の再出現10/20ずつ、raw UTF8失敗0。これらの重複率は同一条件内の診断で、長さ依存があり、新しい合否thresholdではない。512を表示修正・反復抑制で改善したものではない。

元の400生成中の自然EOS9件を全件再読し、内容完結として適切なのはCodex診断で1/9。残る8件は話題逸脱・意味不整合等で、EOS停止を内容成功に数えない。[EOSの全件理由](../reports/phase6/japanese_base_natural_stop_annotations.json)。自然EOS条件付き標本で、9独立promptや全80での成功率とは扱わない。

既存devのBPB差95%区間は10B−Web5.1Bが**−0.004156〜−0.003990**、10B−5Bが−0.010560〜−0.010377。89,416文書の保存NLLを再利用し、GPU全文評価をやり直していない。文書長を1–63/64–255/256–1023/1024+ tokensに分け、各階層のNLL合計/bytes合計でBPBを保存した。短文に対して長文の全体成績を代用しない。

外部説明文はJSQuADのWikipedia100 unique paragraphs/51,362 UTF8 bytesでBPB1.335143。混入は不明で、未学習保証はない。本文rollingのcontext方式と分布が異なるため、既存WebのBPB0.954018との比を学習改善率にはしない。文学・会話を代表する独立した外部domainは後続に残す。

## 実装・保存と次の判断

新しいscorer・取得script・GPU runner・CPU再集計・採点packet/reviewer・WindowsのUI停止/復帰付き入口を追加した。新依存0。shift/mask/BOS/右padding/rolling/context超過/同点/MCC/cluster重み/合成familyの新8 CPU testsと既存契約・評価メモリを合わせた21 tests成功。全configを検証する既存契約で新configのschema不足により2件が失敗したため、凍結値をconstで固定したschemaを追加して修復した。旧criteriaは変更していない。実10BのBF16/math有限値、直接target gather、padding対照も確認し、15の保存証拠checks成功。これは採点基盤の確認で、15言語能力の合格ではない。

GPU時間はpilot7.505秒、全体320.820秒、意味診断の修正版1.686秒。各上限内。実行中のPID/boot/start ticks、source/data/config/checkpoint hash、chunk保存・ログ・原文・候補尤度を保持した。学習コード/Tokenizer/重み/旧v1は変更していない。UIは評価後に http://127.0.0.1:7860 へ復帰した。

最終確認で、初回合成suiteの一部の語彙familyが重複していたため、uniqueな名前でv2.1を作り、意味診断だけ再測定した。CIはclusterを再標本化しつつ問題数で重み付けするratioへ修正した。JNLIのCIはimage単位1,089 groups、JSQuADはparagraph単位94 groupsで、点推定は2,434/100問題の平均を保つ。初回のraw/source/設定は保持し、最終reportへ採用値を明示した。統計CIは一つの学習seedに対する入力標本の不確実性であり、学習seed差・template汎化を含まない。全0/全1のbootstrap区間が退化する場合もある。

次の学習比較で優先すべきものは、**意味の通る完結文の生成と反復の減少**、その上で時間・比較・照応等の条件保持。本文BPBとEOS率だけを成功条件にしない。JNLI/JCoLAはlabel prior・prompt依存が強いため、今のaccuracyを学習採用の単独gateへ使わず、文脈を反転させる診断と自由生成を併記する。追加学習はまだ開始していない。

独立人手による20%の二重採点、公開日本語Base参照モデル、会話/文学の外部domain、JMMLUは後続計画。公式testは候補・仕様の決定後に一度のみ評価し、学習・template選びには使わない。今回の初回評価実装・実測・記録とlocal commitで停止し、学習を自動再開しない。

公開データの出典: [JBLiMP](https://github.com/osekilab/JBLiMP)、[JGLUE](https://github.com/yahoojapan/JGLUE)、[JCoLA](https://github.com/osekilab/JCoLA)。取得commit/URL/hash/利用条件はWSL `~/jmicro-data/evaluation-v2/manifest.json`と各runのsource snapshotへ保存した。
