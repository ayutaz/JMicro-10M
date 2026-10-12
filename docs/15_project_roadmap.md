# JMicro-10M フェーズ別実行計画

最終更新: 2026-10-13 JST。最新の実行結果は[136](136_chat_generalization_results.md)、現在の提案は[135](135_chat_problem_solution_plan.md)、実際の状態は[status](autonomous_status.md)。**計画133の4項目は実行・監査完了、不採用で閉鎖。現在は文書・計画の更新のみで、追加研究・教材準備・GPU診断・学習は停止中。**

## 次に検討する道筋

| 段階・経路 | 現在の判断 | 成果物と停止条件 |
|---|---|---|
| 閉じた133 | D1最終学習、全14セット/3,066判断/NLL7点、回復predicate、padding24確認、全体監査を完了。D0/D1不合格 | 136とcompletionを保存済み。最終評価を再開手順へ戻さず、終了job・不採用paddingを再起動しない |
| 次の教材比較案135 | 意味構造・自然な質問の多様性を広げるrecipeを最大1件。対照は最新D1、同親・10M・同教師量条件 | 別の明示再開→TRAIN根拠QA/凍結→未使用DEV＋既知2回帰→実行契約/技術gate→学習/全評価→採否/報告・停止。21セット/4,599判断は次比較の予定で、実施済みではない |
| 回復・効率 | 回復は正しい提供履歴・内容改善の条件が先。現動的paddingは数値不一致で不採用 | 別の提案・契約・予算。条件不成立は未実行・未確認。旧結果を救済しない |
| Base復旧124 | 代替経路として未再開。日本語Baseの元品質条件を維持 | 必要な比較を最大1件、独立seed/fullDEV/TEST/採用を実証したBaseで通知・停止。Chatへ自動移行しない |
| 独立確認・後続 | 人間blind、独立学習seed43、fullDEV/最終suite/protectedTEST、採用・量子化は未達 | 有望recipeと別の再開判断が必要。初回比較の完了をモデル完成にしない |

次比較のGPU上限案6時間は新規proposalで、閉じたrunの残額や今回の文書依頼による実行許可ではない。個別枠・全評価時間を再開後の実測で凍結し、CPUレビュー時間とは分ける。対照stateの再利用を新学習や独立確認へ数えない。

## 目的と停止境界

約10Mパラメータの日本語モデルをスクラッチ学習し、短い自然な文章を生成できるBase、その後に短い雑談を行うChat、ローカル利用一式を作る。現モデルは10,001,152 parameters、context1024、Tokenizer4096。9.5M〜10.1Mの元予算を維持する。高度な推論・コード生成・長文RAGは成功条件に加えない。

128/131/133の限定Chat-first比較は、未採用の元WebUI10BからSFTする診断として明示再開後に実行し、いずれも品質未達で閉じた。最新の結果は136。次の教材比較は135の未実行提案で、Base採用条件を飛ばして完成扱いにせず、量子化へ進まない。Base復旧を再開する場合は従来どおり必要な証拠を満たすBaseまでで通知・停止する。新しい計画や準備コードを完成・実行許可の証拠にしない。

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
| 7 | 128/131/133の限定SFT比較と全内容確認は完了・不合格。136で4項目の実行監査を閉鎖、追加実験停止・採用未達 | 現Baseからの会話適応の不足を切り分ける。後続の教材比較・完成段階は別の再開判断 | 正式品質は保持・独立学習seed・人間blind・最終評価等も必要。実施条件不成立の保持/回復は未確認 |
| 8 | 最終成果物は未着手、範囲外 | 量子化とローカル利用を完成する | 採用モデルのfloat/量子化比較、容量・速度・品質、独立環境での再現 |
| 9 | 未着手、別の判断が必要 | 20B/条件付き50Bの継続価値を測る | 同条件10B→20BのBPB差CI下限>0、生成に重大退行なし、追加予算内のときのみ50B候補 |
| 10 | 後半構想、範囲外 | baseline以後の追加研究を行う | 共有/蒸留/hybrid/規模比較等の定義済み対照と採否。paid cloudは別途許可 |

Phase0〜3の成果物と歴史的な証拠を維持する。既存環境での文書更新に、再取得・Tokenizer再学習・export再検証・速度benchmarkを加えない。

## Phase6の現在地

元10Bモデルの本学習・保存と評価は完了したが、Baseの品質目標は未達。別の約10.6B staged系列は一貫性23/80・適切完結26/80で基準に近いが合格ではない。系列の異なるモデルのtokensを合算しない。

最新の同native2B比較では、教師量正規化weight decayでBPB1.106386→1.090316に改善したが、一貫性3→3、適切完結7→5、EOS20→23、反復27→27、Unicode失敗0→1（各80）。固定条件は閉鎖・不採用。独立seed43や10B延長へ自動的に進めない。[証拠](../reports/phase6/base_teacher_decay_2b_completion.json)。

データ量、学習量、モデル容量のどれか一つを原因と断定できていない。限定Chat診断と教材比較は136まで完了したが、Chat完成もBase不足の単独原因も実証されなかった。次の候補は135の意味構造を広げる教材比較で、別の明示再開待ち。Base復旧が必要なら[計画124](124_base_recovery_plan.md)の段階0〜5へ戻り、既存結果の再利用で次の比較を最大1件に絞る。研究の一巡が不採用で終わった場合も報告して止める。

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

128/131/133の限定Chat比較は実行・不合格終了し、追加の実行は135の提案から別の明示再開待ち。通常のPhase7完成とPhase8〜10も別の再開判断が必要。診断にmid-training比較まで自動追加せず、最終Chat段階ではrouteの効果、生成seed・独立学習seed・会話family・保持を分ける。量子化は採用floatモデルとの許容退行を先に固定し、全artifact5〜10MB級という目標を実容量・品質で判定する。有料cloud・公開・他者への送信は別途許可が必要。

更新前のPhase定義・全追記・予算と比較契約の原文は[ロードマップ履歴20261008](project_roadmap_history_20261008.md)にbyte一致で保存した。各実験の凍結config/reportが証拠の正本。履歴の将来案を現在の開始指示として扱わない。

今回整理前の全文は[20261013履歴保存一覧](../reports/investigation/documentation_plan_refresh_20261013/baseline.json)にbyte一致で保全した。
