# Base再開: 文書長による損失配分の比較

2026-10-14 JST。「6まで進めてください」により、直前に提示した6段階のBase改善から最終判定までが明示再開された。前回の文書更新はcommit70aa002で完了。Chat/SFT・量子化・大型化・公開は今回の範囲に含めない。

## 問いと根拠

既存accepted TRAINでは本文と元EOSを正解として一度ずつ数え、1024文脈・512教師strideの文書内windowを使う。`NaturalCorpusTrainer.step`は全教師位置のCE平均を使うため、長い文書ほど一drawの損失への寄与が大きい。これは実装から分かる性質であり、生成失敗の原因の証明ではない。

[最新Base結果123](123_base_teacher_decay_2b_results.md)はBPB改善に対し一貫性3/80、適切完結5/80、反復27/80。既存TRAIN/DEV履歴診断でも教師履歴でのEOSと自己生成時の進行が一致しない。損失の平均値だけでは短い日本語の続きが自然に完結する証拠にならない。

今回の候補は、**同じ正解位置に、元文書の教師数（本文tokens+元EOS1）の逆数を掛け、update内の重み合計で正規化したCE**。本文とEOSの重みは同じ。短いwindow長やpadding数を分母にしない。元のgold、入力、文書抽出、source quota、教師量、architecture、推論は変えない。

閉じたEOSのみの重み変更・genre混合変更・uniform smoothing・confidence penalty・反復UL・contrastive objectivesとは機序が異なる。ただし、既存indexのbyte位置抽出は一様文書抽出ではないため、この介入を母集団の完全な文書均等化と呼ばない。短文の雑音も増幅し得る。外部論文の性能をこの10Mへ外挿しない。

## 6段階と停止条件

1. 既存小reportとtrainerを照合し、上記の1比較に限定する。closed comparisonの再開や全corpus走査をしない。
2. 新しいCPU診断として同TRAIN samplerの最初の192windowだけで重みの実変動を確認する。比率max/min≥2、選択goldの重みCV≥0.25を事前screenとする。原因の証明・品質評価ではない。CPU analytic gradient、mask、元文書window、全state再開、異常checkpoint拒否を確認する。
3. screen合格時だけ実CUDA/BF16の有限forward/backward・最大48×1024・連続4対2+保存+2・同TRAIN streamを確認。probeは180秒以内、pilotはcached CEと同じ元10B親・fresh AdamW LR1e-5/WD0.1・batch48・seed42・accepted TRAIN75/20/5配分・正確100M教師。GPUは技術確認と学習/評価/保存を合計4800秒以内、実測から本実行上限を凍結する。既存17698update対照の全sampler/counter/digestを一致させる。
4. pilot生成全80の内容、共通byte DEV256 BPB、日本語評価、matched/strong/cached/historical保持を確認。元条件を満たす場合のみ、本比較の教師/GPU予算と別runを定義する。損失低下だけで進めない。
5. 有資格recipeに限りfresh独立学習seed43、fullDEV、400生成＋長文40を確認する。未完成native runner接続を先に実装する。CPU準備や生成seedの変更は独立学習の代替にしない。
6. 選定条件の封印後だけBase protectedTESTを評価し、全件内容確認・復旧・重み/Tokenizer/config/採否を保存。全条件合格でBase完成を通知して停止する。

元DEV絶対条件は文法≥56/80、一貫性・適切完結各≥27/80、EOS≥37/80、反復≤18/80、empty/role/Unicode失敗0。元比較policyの差≥8・paired CI下限>0・BPB/保持等も維持する。最終TEST停止95%などは別の最終基準であり、DEV screenに置換しない。

各段階が不合格ならその条件を閉じ、後続を`not_executed_no_eligible_candidate`として理由と証拠を保存して報告する。別係数・別seed・親・source・上限の救済を自動追加しない。拒否結果はBase完成ではない。

## 現在の実行状態

新trainerのCPU11 checks、runner予算・counter/digest/samplerのCPU10 checksは全件passed。[192window診断](../reports/phase6/base_document_balance_length_diagnostic.json)は重み比11.85185、選択goldの重みCV0.50065で事前screen合格。

GPU起動前の既存capacity payload schema照合で、元本文長が`window`ではなく`original_record.body_tokens`に保存されていることを確認し修正した。初版contractを保持して実行v2へ分け、同recipe・同shape・同予算の修正を[記録](../reports/phase6/base-document-balance-preparation-20261014/prototype_amendment.json)。記録保存先がWSLに未作成だった中断も、作成済みcontractを照合してreceiptのみ回復した。GPU前の準備修理であり、失敗科学条件の再試行ではない。

[実CUDA probe](../reports/phase6/base-document-balance-probe-20261014/result.json)は47技術更新/273,521教師、最大shapeの24,576教師forward/backward（optimizer更新0）を実行。GPU8.721357秒、最大allocator約10.71GB。モデル/Adam/scheduler/RNG/sampler/counters/全history一致と原同streamを確認した。probe重みは本学習へ使っていない。

[本比較contract](../configs/phase6/base_document_balance_comparison.json)は正確100M教師、既存同100M CE対照の再利用、実測上限3,855秒、probe込み合計4800秒以内。[採否policy](../configs/phase6/base_document_balance_review.json)は科学結果を読む前に凍結した。

2026-10-14T06:41:35Zに永続runnerを開始。WSL PID337424/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start60325743、Windows launcher PID37808。実jobはWSL `reports/phase6/base-document-balance-comparison-20261014/job.json`、metrics/checkpointsはその`document_balance/`。開始後の実process・更新・教師消費・checkpoint作成を確認済み。現在の終了・進捗は同handle/identityと最新jobで確認する。観測timeoutだけで終了と扱わない。

元UIはGPU比較中だけ停止し、wrapperのfinallyで元10Bへ戻す。新科学比較の結果・全80内容・採否は未確定、protectedTEST未使用、Base/Chat未採用。合格候補ができるまでは独立学習・fullDEV・protectedTESTへ進めない。真に独立したBase学習seed43はfresh初期化・学習RNG/material RNG・同recipeの証拠が必要で、同seed42親から別生成seedや別samplerだけで続きを作ることでは代用しない。
