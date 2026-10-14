# JMicro-10M フェーズ別実行計画

2026-10-15追補: [TRAIN index-byte監査](../reports/phase6/sampling-boundary-20261015/sampling_audit.json)で包含行skip/次行選択と直前行byte重みをCPU11 checks・固定256 metadata drawsで確認。旧「record-byte weighted」の説明は自身の長さによる重みと解釈できない。観測された条件内分布差は小さく、品質失敗原因や新学習の根拠にはしない。過去の対照・候補の同抽出pairingは保全。stream/DEV/TEST/GPU/学習0。次はsafe Japanese scorerの必要接続と別比較選定で、独立学習/fullDEV/新TEST/採用は未達。

2026-10-15最新終端: [fresh FIM pilot completion](../reports/phase6/base-fim-pilot-20261015/completion.json)は10000更新/正確94160195教師・DEV256/全80個別review・全state/元stream/全更新監査を完了し不採用。文法28→31、一貫性2→2、適切3→2、EOS13→14、反復49→51、BPB1.290203→1.292414、主差CI[-.0375,.0375]。科学1527.822100＋技術9.153452＝1536.975552秒で科学2519/総3600内。元UI復帰。固定FIM条件を閉鎖し救済・延長をしない。独立学習/fullDEV/新TEST/採用は候補資格なしで未実施、Baseと4項目目標は未達。次はactiveなBase-only範囲で別の根拠ある比較を選定する。以降の稼働・準備記述は過去の観測で、現在のjob生存や品質完成ではない。

稼働中のCPU補足は[保存状態監査](../reports/phase6/fim-feasibility-20261015/checkpoint2000_CPU_audit.json)と[日本語fixed diagnosticsの入力分離](../reports/phase6/fim-feasibility-20261015/Japanese_diagnostic_export.json)。将来の本比較の安全な診断入力として192/331/1119の元inputs/goldのみを保存済みDEV結果から投影、新reader13 checks passed。payloadをGit/学習へ移さず、元混在suiteやTESTを開かない。既知DEV/fixed benchmarkで未知評価・独立監査・品質改善ではない。現在のpilotを変更・再起動しない。

2026-10-15最新: [凍結fresh FIM pilot](../configs/phase6/base_fim_pilot_20261015.json)と永続実行/DEV-only評価/採点CLI、13 CPU checksが完成し科学学習を開始。[観測](../reports/phase6/fim-feasibility-20261015/science_launch_observation.json)は実PID1343/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start64143474、675更新/6352596教師。終端目標10000更新/94160195教師、science2519秒/技術含む総3600秒。v2 launcherのUI解放待ち修理は科学条件を変更せず、初回開始前失敗を保全。次は同じ実processを観測し、終了後の全80 raw-bound内容/全stateと元stream/採否を確認する。pilot screenをBase採用に読み替えず、独立fresh学習・全文DEV/全440・新封印TEST・採用までの4項目を保持する。以下の準備のみの記述は科学開始前の履歴。

更新: 2026-10-15 JST。文書/計画納品d44b8a0の後、「4まで」で評価分離修理からBase最終判定までが明示再開。[修理147](147_evaluation_boundary_repair.md)は新DEV reader/生成/review・CPU21 checks・実DEV80入力のread-set監査まで進んだ。後続は下のfresh FIM prospective選定と専用技術検証。科学学習/品質評価0・科学契約未凍結。Base/Chat未完成・未採用、原10M/品質を維持し、Chat/量子化へ自動移行しない。

[最新準備](../reports/phase6/fim-feasibility-20261015/protocol_readiness.json)は、同native10M・元2B schedule/TRAIN/batch80/seed42と既存対照10000更新/94160195教師を使うfresh FIM PSM pilotをprospective選定。新sampler/trainer16＋workflow9 CPU checks、実10M zero/元source各2560行を照合し、専用CUDA40技術更新/383190教師・全state4対2+2・80x1024/32 timingsがpassed。GPU9.153451952966861秒、pilot予測2519秒/提案総上限3600秒。次はscience永続CLI・隔離DEV256/80評価・notes/reviewerを完成して凍結する。pilotの相対screenを正式Base資格へ置き換えず、独立fresh学習・全文DEV/全440・新封印TEST・採用を維持する。技術probeを再起動しない。

選定前の[FIM CPU feasibility](../reports/phase6/fim-feasibility-20261015/selection_assessment.json)はserializer20 checksと固定24 TRAIN文書のtoken/bytes/EOS保存・context1024適合を確認。固定4096 ordinary marker35tokenの追加入力は標本比26.2746%。科学教師/GPU0で、FIMの通常Base改善・source全体への適合は未実証。成熟親100Mを自動選定せず、fresh対照/意味のあるhorizon/marker教師と長文処理/予算を定義してから比較の採否を決める。新recipe未選定、後半の独立学習・全文DEV・封印TEST・採用を省略しない。

[最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md) / [次の計画145](145_post_rejection_next_plan.md) / [今回更新146](146_documentation_followup.md)。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。

## 前回停止時の道筋（歴史記録）

| 経路 | 現在の判断 | 次に必要なもの |
|---|---|---|
| 閉じた139 | 内容20/18/19/15 of80・自己文脈5/5/5/1 of24、主CI・反復/文字失敗も未達。不採用 | 終了job・採点・NLL・別LR/seed/予算の救済を再開しない |
| 独立確認 | 7分岐は候補なしで未実行・品質未確認 | 原gateを満たすrecipeが先。生成乱数やCPU準備でfresh学習を代替しない |
| Base復旧124 | 未再開、介入未選定 | 根拠ある介入1件と原品質・対照・資源・終了条件。合格Baseで通知停止 |
| 次SFT・教材/目的/効率 | 未選定・未凍結、提供履歴でも品質不足 | 未回答の問いと別の明示再開。既に拒否したpadding等を再試行しない |
| 量子化・20B/50B・公開 | 今回の範囲外 | 採用モデルと別の範囲判断。残予算を開始許可にしない |

前回Chat139の新GPUは2,658.673158秒/33,600秒。以前の比較やCPU時間とは別。目的・Phase定義・原品質条件を以下に保持する。初期・途中のロードマップ全文は[更新前原文](../reports/investigation/documentation-refresh-20261014/baseline.json)から参照する。

## 目的と停止境界

約10Mパラメータの日本語モデルをスクラッチ学習し、短い自然な文章を生成できるBase、その後に短い雑談を行うChat、ローカル利用一式を作る。現モデルは10,001,152 parameters、context1024、Tokenizer4096。9.5M〜10.1Mの元予算を維持する。高度な推論・コード生成・長文RAGは成功条件に加えない。

128/131/133の限定Chat-first比較は、未採用の元WebUI10BからSFTする診断として明示再開後に実行し、いずれも品質未達で閉じた。最新の結果は141。教材比較135は138、低LR比較139は141で不採用終了し、Base採用条件を飛ばして完成扱いにせず、量子化へ進まない。Base復旧を再開する場合は従来どおり必要な証拠を満たすBaseまでで通知・停止する。新しい計画や準備コードを完成・実行許可の証拠にしない。

## 10Mを維持する制約

ユーザーは2026-10-08に、10Mのサイズ維持が重要であり、その小ささを優位性とする方針を明示した。精度を上げるための大型化は本計画の解決策に含めない。現在10,001,152 parameters、既存9.5M〜10.1Mの総パラメータ予算を維持する。サイズ内の構成配分・教材・学習目的・最適化は比較対象になり得るが、改善効果は未実証。大型モデル比較は別の明示依頼がある場合に限る。元の日本語Base品質目標を維持し、対象領域を勝手に狭めて達成扱いにしない。学習・研究実行の停止は継続する。

<a id="phase-0-成功条件環境実験管理"></a>
<a id="phase-1-データの小規模pilotと評価split"></a>

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
| 7 | 128/131/133/135の限定SFT比較と全内容確認は完了・不合格。138で6段階の実行監査を閉鎖、追加実験停止・採用未達 | 現Baseからの会話適応の不足を切り分ける。後続の教材比較・完成段階は別の再開判断 | 正式品質は保持・独立学習seed・人間blind・最終評価等も必要。実施条件不成立の保持/回復は未確認 |
| 8 | 最終成果物は未着手、範囲外 | 量子化とローカル利用を完成する | 採用モデルのfloat/量子化比較、容量・速度・品質、独立環境での再現 |
| 9 | 未着手、別の判断が必要 | 20B/条件付き50Bの継続価値を測る | 同条件10B→20BのBPB差CI下限>0、生成に重大退行なし、追加予算内のときのみ50B候補 |
| 10 | 後半構想、範囲外 | baseline以後の追加研究を行う | 共有/蒸留/hybrid/規模比較等の定義済み対照と採否。paid cloudは別途許可 |

Phase0〜3の成果物と歴史的な証拠を維持する。既存環境での文書更新に、再取得・Tokenizer再学習・export再検証・速度benchmarkを加えない。

## Phase6の現在地

元10Bモデルの本学習・保存と評価は完了したが、Baseの品質目標は未達。別の約10.6B staged系列は一貫性23/80・適切完結26/80で基準に近いが合格ではない。系列の異なるモデルのtokensを合算しない。

以前の同native2B比較では、教師量正規化weight decayでBPB1.106386→1.090316に改善したが、一貫性3→3、適切完結7→5、EOS20→23、反復27→27、Unicode失敗0→1（各80）。固定条件は閉鎖・不採用。独立seed43や10B延長へ自動的に進めない。[証拠](../reports/phase6/base_teacher_decay_2b_completion.json)。

データ量、学習量、モデル容量のどれか一つを原因と断定できていない。限定Chat診断と教材/低LR比較は141、Base文書長重みは144まで完了したが、Chat完成もBase不足の単独原因も実証されなかった。低LRの1件比較も不採用で閉じた。次の介入は計画145の評価隔離修理・既存証拠照合と、別の明示再開時の契約で選定・凍結する。Base復旧が必要なら[計画124](124_base_recovery_plan.md)の段階0〜5へ戻り、既存結果の再利用で次の比較を最大1件に絞る。研究の一巡が不採用で終わった場合も報告して止める。

<a id="品質目標と判断ルール"></a>

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

<a id="高速に完成させる進め方"></a>

## 資源・時間・実行の原則

全Pythonはuv管理3.12.7。学習はWSL2/RTX4090/Linux disk。速度は教師tokens/秒・CE入力/秒・padding込みphysical入力/秒を区別する。過去のFlash/compile高速系列の値を、現在のBF16/math/native教師速度として使わない。最大VRAM使用量と最速設定も別々に実測する。

長期学習の前に実CUDA保存再開gateと安定batchを確認する。checkpointにはmodel/Adam/scheduler/RNG/sampler/countersを保存し、実PID/boot/start・累積GPU ledger・logsを永続化する。予算は現条件の実測から固定し、未達時に暗黙に増やさない。

同じデータの反復を新規データ量に足さず、目標データ量を準備済み量と呼ばない。既存受入データと証拠を再利用し、独立全corpus再走査を学習の前提にしない。新しい環境や変更箇所に必要な確認だけを行う。

## 後続フェーズの扱いと履歴

128/131/133/135/139の限定Chat比較は実行・不合格終了し、追加の実行は別の明示再開・新契約待ち。通常のPhase7完成とPhase8〜10も別の再開判断が必要。診断にmid-training比較まで自動追加せず、最終Chat段階ではrouteの効果、生成seed・独立学習seed・会話family・保持を分ける。量子化は採用floatモデルとの許容退行を先に固定し、全artifact5〜10MB級という目標を実容量・品質で判定する。有料cloud・公開・他者への送信は別途許可が必要。

更新前のPhase定義・全追記・予算と比較契約の原文は[ロードマップ履歴20261008](project_roadmap_history_20261008.md)にbyte一致で保存した。各実験の凍結config/reportが証拠の正本。履歴の将来案を現在の開始指示として扱わない。

今回整理前の全文は[20261013履歴保存一覧](../reports/investigation/documentation_plan_refresh_20261013/baseline.json)にbyte一致で保全した。
