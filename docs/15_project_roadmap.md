# JMicro-10M フェーズ別実行計画

2026-10-13 JST 最新の計画: [課題解決計画135](135_chat_problem_solution_plan.md)をt1全内容判断・NLLとt2保存記録に合わせて更新した。t2状態監査と不足評価、同じ凍結条件の最終比較、条件が成立する保持/回復、結果報告を順に計画する。未知質問への汎化を最優先とし、動的paddingは数値gate不合格で不採用。今回の依頼で新しい学習・評価・診断・教材準備は開始していない。10Mと元の品質基準を維持し、Base/Chat採用・独立seed・fullDEV/TEST・量子化へ自動移行しない。以下は各時点の履歴。

2026-10-13 JST 実行継続: goal『4まで』に従い実作業を進めている。[実行記録134](134_chat_generalization_execution.md)。親とD0/D1 t1の新旧6suite・1,314内容判断とNLL3点を完了。t1内容はD0/D1新14/18、旧11/6（各80）、自己生成文脈は新6/4・旧1/2（各24）で不合格。D1を同じ有効stateからt2へ継続中。別paddingはGPU24確認更新・再開一致・速度測定まで完了したが、事前の数値一致gateを満たさず不採用。最終B比較・条件付き分岐・全体完了監査は未完了。10M、凍結条件、累積GPU6時間、元品質gateを維持する。以下の日付段落は各時点の履歴。

2026-10-13 JST 最新の計画更新: [課題解決計画135](135_chat_problem_solution_plan.md)を現在の記録に合わせて改訂した。優先順は教材の汎化→同条件比較の全評価→登録条件を満たす場合だけ誤履歴回復→独立したpadding検証。記録上、D1はt1（1,214更新・633,391教師）保存と実消費監査、CUDA gate、新旧rawの機械評価まで到達しているが、全内容判断・最終B比較・品質改善は未確認。paddingはCPU一致までで、GPU数値/再開/速度は未確認。今回行ったのは計画・文書更新と小記録の保存のみで、新規jobの起動・学習再開・教材準備・GPU診断は行っていない。10Mと元の基準を維持し、Base/Chatは未完成・未採用。以下の各日付段落は記載時点の履歴として読む。

2026-10-13 JST 継続実行: ユーザーの『4まで進めてください』に従い、教材改訂・同条件比較・条件付き回復・別padding検証を進めている。[実行記録134](134_chat_generalization_execution.md)。D1 TRAIN40,126/660,065教師、280sample内容確認、CPU消費、新DEV80/自己生成24会話59turn、対照の歴史的再利用と実行config固定まで完了。D0は旧C1の一致した保存stateを再利用し新学習0、D1は未学習。共有GPU6時間内に回復/効率の枠も登録した。CUDA gate・学習・全内容評価・品質は未完了、Base/Chat未採用。旧job・TEST・採用・量子化・公開/pushへ進まない。

2026-10-13 JST 計画更新: 最新の課題解決方法と計画を[計画135](135_chat_problem_solution_plan.md)に整理した。教材の汎化改善を第一比較、正しい履歴での改善後に誤履歴回復、paddingを別の効率比較とする。既存D1準備の小記録はTRAIN40,126 target・固定280sample問題0・CPU消費チェック合格を示すが、独立人間確認・新DEV・CUDA gate・学習・品質は未確認。今回の依頼では計画と記録のみを更新し、新しい教材生成・GPU実験・学習は開始しない。Base/Chat未完成・未採用、10Mと元の品質基準を維持する。

2026-10-12 最終状態: 計画131の段階0–5の学習・全評価・結果報告を終え、C0/C1とも不合格で閉鎖。各1,899,555 Assistant本文+EOT教師、全14suite・3,066内容判断、固定NLL7点を確認した。最終新DEVの文法・関連性同時2はC0 11/80、C1 15/80（必要56）、自己生成最終文脈2は4/24、2/24（必要15）。GPU累積70.794分/6時間上限。合格候補がなく保持/samplingは条件付き省略・品質未確認。Base/Chat未完成・未採用。元10B UIを復帰。追加実験は停止し、[結果132](132_chat_improvement_execution.md)と[次の未実行計画133](133_chat_generalization_followup_plan.md)を参照する。

[完了監査](../reports/phase7/chat-improvement-20261012/completion.json)。以下の調査・事前計画・過去実験の記述は各時点の履歴で、現在の開始指示ではない。

## 過去の計画と経緯

2026-10-12 対策計画作成: [計画131](131_chat_improvement_execution_plan.md)に問題ごとの対策と段階0–5を具体化した。最初は元親から雑談対照/条件回答教材の2条件、各約1.9M Assistant教師、教師量schedule、未使用DEVと旧回帰、累積GPU6時間案。報告で止め、回復教材・効率・再現/最終採用は別の後続段階。新規教材/runner/config/実験は未開始、明示再開待ち。

2026-10-12 調査完了: 保存済みChat失敗・実装・公開研究から、教材の役割/条件回答を最優先とする改善案を[調査130](130_chat_failure_improvement_investigation.md)に整理した。自生成履歴の回復、未使用評価、教師量とscheduleの公平な比較を次候補とする。新規教材/GPU診断/追加学習は未実施・明示再開待ち。原品質基準と10M制約を維持する。

2026-10-10 完了・停止: ユーザーの「5まで進めてください」で128の限定診断を実装・GPU gate・3周学習・全4条件876内容評価・paired比較・結果記録まで完了した。全DEV screen不合格で条件を閉じ、追加研究/学習を停止。[結果129](129_chat_first_sft_execution.md)。Base/Chat未採用、追加比較/量子化/公開は範囲外。

最終更新: 2026-10-12 JST。現在の事実は[状態](autonomous_status.md)、直近の学習結果は[結果129](129_chat_first_sft_execution.md)、改善の根拠は[調査130](130_chat_failure_improvement_investigation.md)、最新の提案は[計画131](131_chat_improvement_execution_plan.md)。[Chat-first計画128](128_chat_first_sft_plan.md)は終了済み診断の事前計画。Base復旧が必要な場合は[計画124](124_base_recovery_plan.md)を参照する。**限定診断を実行・不合格終了し、現在は学習・GPU診断・データ準備を停止。**

[作り直す前の調査127](127_rebuild_investigation.md)にAkebonoとの構成・用途・評価の違い、前回の原因候補と反証を整理した。その後、ユーザーの方針で「現在のBaseから直接SFTして先に会話を確認する」限定診断を128に計画した。参考の低い会話成立率や未公開recipeから改善を保証せず、実行configは再開後の実測で凍結する。127/128は調査と事前計画で、後続の明示再開・実行結果は129。実行完了は品質達成の証拠ではない。

## 目的と停止境界

約10Mパラメータの日本語モデルをスクラッチ学習し、短い自然な文章を生成できるBase、その後に短い雑談を行うChat、ローカル利用一式を作る。現モデルは10,001,152 parameters、context1024、Tokenizer4096。9.5M〜10.1Mの元予算を維持する。高度な推論・コード生成・長文RAGは成功条件に加えない。

最新の128は、未採用の元WebUI10Bを直接SFTする限定診断として、従来のBase-first順序の例外を計画する。1条件・最大3周、matched会話評価・自生成履歴・Base保持を確認して報告・停止。Baseの採用条件を飛ばして完成扱いにせず、量子化へ進まない。Base復旧を再開する場合は従来どおり必要な証拠を満たすBaseまでで通知・停止する。新しい計画や準備コードを完成・実行許可の証拠にしない。

## 10Mを維持する制約

ユーザーは2026-10-08に、10Mのサイズ維持が重要であり、その小ささを優位性とする方針を明示した。精度を上げるための大型化は本計画の解決策に含めない。現在10,001,152 parameters、既存9.5M〜10.1Mの総パラメータ予算を維持する。サイズ内の構成配分・教材・学習目的・最適化は比較対象になり得るが、改善効果は未実証。大型モデル比較は別の明示依頼がある場合に限る。元の日本語Base品質目標を維持し、対象領域を勝手に狭めて達成扱いにしない。学習・研究実行の停止は継続する。

## Phaseごとの目的とゴール

| Phase | 現在の状態 | 目的 | 完了に必要な成果・証拠 |
|---:|---|---|---|
| 0 | 完了 | 成功条件・実験管理を固定する | config/schema/seed/評価split。[証拠16](16_phase0_completion.md) |
| 1 | 完了 | 追跡可能な小規模pilotを作る | corpus/manifest/split/会話pilot。[証拠17](17_phase1_completion.md) |
| 2 | 完了 | 日本語Tokenizerを確立する | 同sampleの4k/8k学習と特殊token契約。[証拠18](18_phase2_completion.md)。再学習しない |
| 3 | 完了 | モデル・cache・exportを成立させる | forward/cache/HF/float GGUF等。[証拠19](19_phase3_completion.md)。学習済み量子化品質とは別 |
| 4 | 完了 | 4090で再現可能な学習基盤を作る | WSL/CUDA/BF16、shard学習、全state保存再開、安定batchと速度。[証拠21](21_phase4_completion.md) |
| 5 | 完了 | 小予算で候補を選ぶ | overfit/smoke/100M比較と候補判断。[証拠23](23_phase5_completion.md)。品質完成とは別 |
| 6 | 学習・多数比較実施済み、品質未達。一時停止 | 自然に完結する日本語Baseを完成する | 固定品質・保持比較、独立学習seed、fullDEV/全生成内容、protectedTEST、採用・復旧記録 |
| 7 | 128/131の限定SFT比較と全内容確認は完了・不合格。停止中、採用未達。次は未実行計画133 | 先に現Baseから会話適応を検証。その後の完成段階は別の再開判断 | 診断はmatched学習前後・自生成履歴・保持。最終品質は複数seed・blind/最終評価等も必要 |
| 8 | 最終成果物は未着手、範囲外 | 量子化とローカル利用を完成する | 採用モデルのfloat/量子化比較、容量・速度・品質、独立環境での再現 |
| 9 | 未着手、別の判断が必要 | 20B/条件付き50Bの継続価値を測る | 同条件10B→20BのBPB差CI下限>0、生成に重大退行なし、追加予算内のときのみ50B候補 |
| 10 | 後半構想、範囲外 | baseline以後の追加研究を行う | 共有/蒸留/hybrid/規模比較等の定義済み対照と採否。paid cloudは別途許可 |

Phase0〜3の成果物と歴史的な証拠を維持する。既存環境での文書更新に、再取得・Tokenizer再学習・export再検証・速度benchmarkを加えない。

## Phase6の現在地

元10Bモデルの本学習・保存と評価は完了したが、Baseの品質目標は未達。別の約10.6B staged系列は一貫性23/80・適切完結26/80で基準に近いが合格ではない。系列の異なるモデルのtokensを合算しない。

最新の同native2B比較では、教師量正規化weight decayでBPB1.106386→1.090316に改善したが、一貫性3→3、適切完結7→5、EOS20→23、反復27→27、Unicode失敗0→1（各80）。固定条件は閉鎖・不採用。独立seed43や10B延長へ自動的に進めない。[証拠](../reports/phase6/base_teacher_decay_2b_completion.json)。

データ量、学習量、モデル容量のどれか一つを原因と断定できていない。最新方針は128の限定Chat診断で作り直しの必要性を先に判断する。Base復旧が必要なら[計画124](124_base_recovery_plan.md)の段階0〜5へ戻り、既存結果の再利用で次の比較を最大1件に絞る。研究の一巡が不採用で終わった場合も報告して止める。

## 現行の採否条件

技術的に動いたことと能力目標の達成を分ける。原品質目標・各凍結実験の比較条件を結果に応じて緩めない。

| 判断の段階 | 現行条件 |
|---|---|
| 固定Base DEV80の絶対screen | 文法2≥56、一貫性2≥27、適切完結≥27、EOS≥37、反復≤18、empty/role/Unicode失敗0 |
| 比較と保持 | 指定されたmatched/strong/cached/historical参照を区別し、元相対条件・paired CI・BPB guardを満たす。相対一貫性差≥8かつCI下限>0等を省略しない |
| 独立学習seed | 同レシピをfresh seed43で学習。生成乱数の変更では代用しない。有利なseedだけ選ばない |
| fullDEVと生成確認 | 全文DEVと400生成＋長文40の全内容を確認。DEV256のBPBを全文結果へ読み替えない |
| protectedTEST | 選定封印後に20prompt×5mode=100生成等。文法70%、一貫性/適切完結27/80の率、停止95%、反復≤18/80の率、文字等の失敗0を元実装どおり判定 |
| Base採用 | 上記の実証、追跡可能なweights/Tokenizer/data/config、再開・ローカル利用記録をそろえる |

[元policy](../configs/phase6/base_parallel_residual_review.json)、[現行適用例](../scripts/review_base_teacher_decay_2b.py)、[最終TEST条件](../scripts/run_final_base_test.py)、[最終採否](../scripts/review_final_base_test.py)、[評価契約](evaluation_protocol.md)を参照する。表は要約であり各実験の全guardを置き換えない。元のBase文法70%、Chatの文法・関連性70%、文脈60%、停止95%等の目標も維持する。

native独立seedのfactoryとCPU testsは準備済みだが、永続runner/reviewerとfullDEV/TESTへの明示的な接続は未完成。旧stable+20M-decay専用runnerへnative checkpointを偽装して渡さない。[準備122](122_base_native_seed_confirmation_preparation.md)は作成当時の記録であり、候補の採否は後続123を参照する。

DEVを繰り返し見た非blind評価の限界を明記する。最終TESTを調整用に使わず、不合格後の改訂には新たな未使用TESTが必要。独立corpus監査や人間blindが未完了のままなら、完了したと記載しない。

## 資源・時間・実行の原則

全Pythonはuv管理3.12.7。学習はWSL2/RTX4090/Linux disk。速度は教師tokens/秒・CE入力/秒・padding込みphysical入力/秒を区別する。過去のFlash/compile高速系列の値を、現在のBF16/math/native教師速度として使わない。最大VRAM使用量と最速設定も別々に実測する。

長期学習の前に実CUDA保存再開gateと安定batchを確認する。checkpointにはmodel/Adam/scheduler/RNG/sampler/countersを保存し、実PID/boot/start・累積GPU ledger・logsを永続化する。予算は現条件の実測から固定し、未達時に暗黙に増やさない。

同じデータの反復を新規データ量に足さず、目標データ量を準備済み量と呼ばない。既存受入データと証拠を再利用し、独立全corpus再走査を学習の前提にしない。新しい環境や変更箇所に必要な確認だけを行う。

## 後続フェーズの扱いと履歴

128の限定Chat診断は実行・不合格終了し、追加の実行は再開待ち。通常のPhase7完成とPhase8〜10も別の再開判断が必要。診断にmid-training比較まで自動追加せず、最終Chat段階ではrouteの効果、生成seed・独立学習seed・会話family・保持を分ける。量子化は採用floatモデルとの許容退行を先に固定し、全artifact5〜10MB級という目標を実容量・品質で判定する。有料cloud・公開・他者への送信は別途許可が必要。

更新前のPhase定義・全追記・予算と比較契約の原文は[ロードマップ履歴20261008](project_roadmap_history_20261008.md)にbyte一致で保存した。各実験の凍結config/reportが証拠の正本。履歴の将来案を現在の開始指示として扱わない。
