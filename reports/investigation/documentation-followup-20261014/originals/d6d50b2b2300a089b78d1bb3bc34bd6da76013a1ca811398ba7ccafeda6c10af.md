# 日本語Base追加評価v2の実施計画

2026-10-04。評価追加の実装・現在10Bモデルの採点まで進める。追加学習は行わない。
[棚卸し](44_japanese_base_evaluation_audit.md)に続く、[凍結設定](../configs/evaluation/japanese_base_v2.json)。

**実施完了: [結果と制限](46_japanese_base_evaluation_v2_results.md)。** 初回runは元設定/sourceをsnapshotで保存した。v2.1は合成suiteの語彙family重複を修正してその192件だけ再採点し、CIを問題数で重み付けするcluster bootstrapへ修正した。JNLIのCIは同じimage IDをまとめる。修正前のraw/sourceは保持し、変更のない公開taskや長文生成は再実行しなかった。

1. 既存の保存結果をCPUで集計する。文書単位paired BPB差CI、長さ別BPB、category別生成長・char/token 4-gram反復・同文再出現・raw Unicode・EOSを保存する。旧v1の問題・判定・結果は保持する。
2. 公開評価の小さいデータだけをcommit固定で取得する。JBLiMP全331対、JCommonsenseQA/JNLIの公式dev、JCoLAのin/out dev、JSQuADの事前固定dev100件を評価用として分離する。公式testは取得しない。各データのURL/hash/licenseをmanifestへ保存する。JNLI/JCoLAの少数例は公式trainからラベルごとの最初の1件で固定し、重みの学習には使わない。
3. 基本意味診断は否定・数量・時間・比較・照応・因果の120 familyを固定し、各familyの二つのcontextで同じ候補の正解が反転する。dev96 family/192件、test24 family/48件。候補順をfamily間で交互に変える。合成・未専門家検証の診断であり、同型templateを使うため独立した汎化benchmarkではない。
4. nativeの候補尤度scorerを実装する。固定Tokenizer/BOS、FP32 CE、BF16/math、右padding、候補だけのloss、EOSなし。protected newlineでcontextを終え、joint tokenizationのprefix一致を確認する。不安定境界・context超過は拒否し、答えを切り詰めない。rolling本文はBOSと最大512 tokensの過去文脈を使い、各body tokenを一度だけ採点する。harnessのEOT conventionとは異なり、harnessへ登録したadapterとは称さない。
5. CPUの手計算・mask・shift検証後に実モデルGPU pilotを行う。JCommonsenseQA/JNLI/JCoLAの事前seed固定200件、意味dev/JBLiMPを採点し、120秒以内の有限値とpadding対照を確認する。その後公式dev全体とJSQuAD100件、外部本文100 paragraph、greedy128/512 tokensの20 prefixずつを900秒以内で測る。UIは停止・評価後に復帰する。既存の全dev/400生成はGPUで再測定しない。
6. 保存済みWeb5.1B/10Bの固定80ずつを匿名化packetにする。文法・prefix関連性・文間一貫性を各0/1/2でCodexが採点し、原文・理由・採点者を記録する。独立人手blind採点は未実施と表示し、文法70%の原目標の達成根拠に流用しない。EOSは停止・内容完結・早すぎる終了・逸脱を分ける。

候補全文のlog likelihoodを主成績、token平均を事前固定の副成績として併記し、成績がよい方だけを採用しない。JNLI/JCoLAは0-shotとbalanced few-shotを両方報告する。同点は正解を含む最大候補数の逆数でaccuracyを採点し、confusion/MCC/F1だけは最初の最大候補を使ったことを明示する。

JBLiMPの主成績はtrainから先頭2M既存token IDsで推定したadd-one unigramを用いるsample SLOR。全train頻度を用いた原論文の再現ではない。生の文尤度の成績も別記録する。最初の候補が常にgoodなので「常に先頭」を日本語能力のbaselineとは扱わない。他taskにはchance・train最頻label・同じtrain unigramを付ける。

JNLIのCIはcaption ID、基本意味はfamily、その他は問題/promptを単位にbootstrapする。同じ入力のvariantを独立問題数に水増ししない。学習seedは1個で、CIは入力標本の不確実性のみ。新成績は診断であり、CI下限がchanceを超えた場合のabove-chance evidenceと、既存の実用品質合格を分ける。

JSQuADは先にseed固定100件を選ぶ。本文・質問・64-token出力が1024に収まらない件数を記録し、残った答案の損失と自由生成を別測定する。生成答案は最初の改行/句点までを使う。EMは空白・日本語/ASCII句読点を除去した独自normalized EM、F1は文字単位と明記し、公式の形態素単位scoreとは比較しない。100件subsetを公式全体scoreと呼ばない。

外部本文はJSQuADのWikipedia説明文100 unique paragraphs、上限1M bytes。既存Webは長さ別BPB。会話/文学等を代表する独立外部domain、公開Base参照重み、JMMLUは後続P2/P3として残す。初回完了条件は基本文法・意味・生成・EOS・反復の診断と指定した初回taskの全件記録、scorer検証、baseline/分母/CI、UI復帰、local commit。独立人手・外部Base・JMMLUの未実施を隠さない。

```bash
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/prepare_japanese_evaluation.py
uv run --frozen --extra hub --extra data --extra ml --extra export -m pytest tests/test_japanese_evaluation.py -q
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/evaluate_japanese_base.py --pilot
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/evaluate_japanese_base.py
```

実行先はWSL repo。初回は`reports/phase6/japanese-base-v2-20261004/{pilot,full}`、修正版の意味診断は`reports/phase6/japanese-base-v2-20261004-r1/pilot`に保存した。現在の設定はr1で新規の全taskを実行できるが、今回の完了済みtaskの再評価は不要。job identity・source/data/config binding・chunkごとの保存結果を保持する。同じbindingなら保存済みcaseから再開する。source/configを変えた場合は旧runを上書きせず新しいoutputを指定する。予算到達をcompleteと表示しない。Windowsから一括実行する入口は`scripts/run_japanese_evaluation.ps1`で、UIを評価中だけ停止し、失敗時もfinallyで復帰する。既存の完了証拠を再利用するCPU集計は`analyze_saved_japanese_evaluation.py`、内容採点検証は`review_japanese_content.py`、今回の最終reviewは`review_japanese_base_v2.py`。
