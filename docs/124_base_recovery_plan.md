# Base改善の今後の計画

2026-10-15最新判断: [key-bias数学SDPA owned gate](../reports/phase6/forgetting-attention-key-bias-probe-20261015/completion.json)は最大48x1024の容量不足で閉鎖、GPU1.244660秒・学習更新0。CPU精度合格を実機学習可能と読み替えず、形状/allocator/backend/予算で閉鎖条件を救済しない。次の[公式タイル化kernel一次調査](../reports/phase6/forgetting-attention-key-bias-preparation-20261015/fused_kernel_assessment.json)は未導入・未実機で、別実装proposal/勾配/runtime/cache/全state資格が必要。全消費を元technical180/総4800へ継承し、元10M/品質/独立全pipeline/fullDEV/全440/新TEST/採用の範囲を維持する。全4項目goalはactive/未達。

2026-10-15[別key-bias実装](../reports/phase6/forgetting-attention-key-bias-preparation-20261015/CPU_readiness.json)は同数式のsoftmax行定数を省き、元精度/初期化/FP32/10M/品質を変えず実親cache gateを通過。17/23/16 CPU checksと両arm全state resumeもpassed。次は専用owned180秒で最大48x1024のresident capacityをAdam前に確認し、通過時だけ両armの学習再開/cache/32timingsと総4800内を実測する。失敗時は閾値・batch・backend等で救済せず閉鎖。科学/独立全pipeline/fullDEV/全440/新TEST/採用は未資格、全4項目goalはactive/未達。

2026-10-15対象限定[実親cache層別診断](../reports/phase6/forgetting-attention-preparation-20261015/CPU_cache_layer_localization.json)は完了。最終差はnative1.4305115e-5で元基準内、forgetting reference0.0001010895で未達、最初の非exact箇所は双方共通で原因は未確定。完了診断の反復や初期gate/親/精度閾値等の救済をせず、同数式の別安定実装の価値と必要証拠を次に判断する。新科学/GPU0、独立全pipeline/fullDEV/全440/新TEST/採用と全4項目goalはactive/未達。

2026-10-15CPU判断: [forgetting attention model/trainer](../reports/phase6/forgetting-attention-preparation-20261015/CPU_model_trainer_closeout.json)は同元重み＋初期forget.5のlearned/static両arm設計を先に保存し、実count10,014,516・model14/trainer19 checksまで完了。しかし実元親cache差が元3e-5/2e-5を超え、reference実装は科学0で閉鎖。小fixtureや全state resume合格を実親精度の代替にしない。次は既存technical span上で数値差を局在化してから別実装の価値を判断し、元cache/10M/品質/対照/実測予算を維持する。新GPU/学習/DEV/TEST0、独立fresh全pipeline/fullDEV/全440/新TEST/採用と全4項目goalは未達。

2026-10-15次案: [forgetting-attention proposal](../reports/phase6/forgetting-attention-preparation-20261015/proposal.json)は独立したCPU数学referenceで[7 checks](../reports/phase6/forgetting-attention-preparation-20261015/CPU_math.json)を通した。正規化前の累積decayと旧出力後gateの差を確認しただけで、現在の失敗原因や品質向上は未証明。有限sigmoid gateの初期関数はnativeと異なるため、fresh対照か正当なmatched conversionかを解決してから実model/count/cache/selected CE/trainerと実測予算を準備する。新学習/DEV/TEST/GPU0、実count/科学契約未検証。旧next-two/recurrentは原記録から既閉鎖と確認し小変更で再試行しない。元全品質条件と独立全pipeline/fullDEV/全440/新TEST/採用の到達範囲を維持する。

2026-10-15最新判断: [causal-QKV contiguous100M](../reports/phase6/causal-qkv-contiguous-science-20261015/completion.json)は全state/原CE stream＋宣言lag差・全80個別内容を確認して不採用に閉鎖。文法44→61、BPB0.998487→0.998450でも、一貫性2→1・適切完結2→1・反復45→47で元gate未達。文法・BPBと意味の進行・完結を区別し、固定lag/tap/層subset/activation/親/seed/decoder/予算を救済しない。次は原proposal/runtime/resultから別の未回答仮説1件を選定して元gate・対照・実測予算を固定する。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用は有資格候補なしで未実施、全4項目goalはactive/未達。下の進行中・技術のみは当時の履歴。

2026-10-15進行: [causal-QKV contiguous100M](../configs/phase6/causal_qkv_contiguous_science_20261015.json)を凍結・起動。新GPU実装比較で同verification3から各3更新の全state/history、保存済みreference0/3/38と32非時間metricsがexact、保存再開/48x1024/raw cacheも合格。旧reference19.769017＋新15.081088＝技術累計34.850105秒を元technical180/総4800へ継承し、実測科学4291秒で予算を満たした。モデル/lag/教師/precision/backend/品質を救済変更せず、元親/原CE100M/48/42、明示runtime・候補10,014,464で実PID58473/start66504429が240更新/1355486教師の途中。次は同job終端の原対照全state/stream＋宣言構造差と全80内容採否。資格後だけ独立fresh全pipeline/fullDEV/全440/新封印TEST/採用へ進む。全4項目goalはactive/未達。

2026-10-15新案の技術段階: 前2有効tokenのprojected Q/K/Vを加える10,014,464 modelはCPU/実親parityとGPU数値/cache/保存再開を通過したが、[reference実測](../reports/phase6/causal-qkv-probe-20261015/completion.json)の科学予測8581秒が総4800秒を超え、科学0でreference条件閉鎖。[別の同数式contiguous実装](../reports/phase6/causal-qkv-contiguous-preparation-20261015/CPU_equivalence.json)は共有joined tensorの値/勾配/3更新Adam exactをCPU11項目で確認。初回失敗も保全し、元構造/教師/品質/precision/backendを変更せずGPU同値性・速度はこれから検証する。次の新CUDA gateは既消費19.769017秒を元technical180/総4800へ継承する。予算/教師/tapの救済やreference再実行では進めない。独立fresh全pipeline/fullDEV/全440/新TEST/採用と4項目goalは未達。

2026-10-15最新判断: [first-layer value residual100M](../reports/phase6/value-residual-science-20261015/completion.json)も全state/元CE対照・宣言12scalar差・全80個別内容を確認して不採用に閉鎖。文法44→58/EOS19→23に対し一貫性2→1・適切完結2→1・反復45→47・BPB0.998487→0.998524。初期関数を保存した層間V0経路の追加だけでは今回の生成品質改善は成立しない。固定V0係数/層subset/normalization/親/seed/decoder/予算を救済せず、次は既存の原proposal/runtime/resultから別の未回答仮説1件を選定する。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用は有資格候補なしで未実施。4項目goalはactive/未達、以下のrunning等は当時の履歴。

2026-10-15進行: [first-layer value residual100M契約](../configs/phase6/value_residual_science_20261015.json)を実元親CPU parity/専用trainerと全state resume/owned GPU9.812882秒・最大48x1024/18科学workflow checks後に凍結・起動した。science3568/技術込み4800秒、元親/原CE100M/48/42と全元品質gateを保持。実PID52873/start66148908は40更新/233183教師の途中で、品質未判定。次は同job終端の原対照全state/stream＋宣言12scalar差と全80個別内容採否。未達なら固定条件閉鎖、有資格時だけ独立fresh全pipeline/fullDEV/全440/新封印TEST/採用。全4項目goalはactive/未達、下の未実装/科学0記録は履歴。

2026-10-15次案選定: [first-layer V residual proposal](../reports/phase6/value-residual-preparation-20261015/proposal.json)を実装前に保存し、別modelの[18＋1 CPU checks](../reports/phase6/value-residual-preparation-20261015/CPU_preparation.json)を完了。元Vに最初のVを零係数から足す12 scalar/10,001,164で、閉鎖したcross-map/output gate/parallel residualとは情報経路が異なる。ただし局所の原因診断・品質改善ではない。実元親CPU parityと専用typed trainer/全state resumeが次で、元native hidden helperは流用不可。owned CUDA/科学CLI/科学契約は未完、予算は実測後に凍結し元全gateを維持する。科学学習/GPU/new data/DEV/TEST0、独立fresh全pipeline/fullDEV/全440/新TEST/採用は未達。

2026-10-15最新判断: [cross-GQA signed-map100M](../reports/phase6/cross-gqa-map-science-20261015/completion.json)も全state/元CE stream・宣言した構造差と全80個別内容を確認し不採用に閉鎖した。文法44→60に対し一貫性2→2・適切完結2→2・EOS19→18・反復45→47・BPB0.998487→0.998503。文法と意味の進行・完結は別に評価する。今回だけでGQAや10M規模が根因とは断定せず、固定条件のmap/係数/normalization/親/seed/decoder/予算を救済しない。次は原proposal/trainer/resultから別の未回答仮説1件を選定し、対照・元gate・実測予算を事前固定する。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用は有資格候補なしで未実施。全4項目goalはactive/未達、下のrunning/準備記録は当時の履歴。

2026-10-15実行追補: cross-GQA構造案はowned CUDA10.287119秒で全state/history resume exact・48x1024有限gradient・事前精度内のcache比較を通し、[科学100M契約](../configs/phase6/cross_gqa_map_science_20261015.json)を凍結して開始した。元base config一致＋宣言52scalar差のguardと全品質条件を維持、科学3743/総4800秒。現在PID48654/start65870189の同job終端と全80内容採否を待つ。下のGPU/CLI未実装記述は当時の履歴で、独立学習/fullDEV/新TEST/採用は依然未達。

2026-10-15別構造案: [cross-GQA signed-map proposal](../reports/phase6/cross-gqa-map-preparation-20261015/proposal.json)を明示してからCPU実装・検証した。元nativeを置き換えず、原関数を保つ初期0の52scalar追加（10,001,204）で、他KV groupのmapを現在Vへ適用する。旧query-dependent output gate/同KV内の線形混合/閉鎖MHA allocationと区別し、model18/trainer12 checksと実元親parityを完了した。次は専用owned CUDA/typed保存再開/明示的architecture対照/隔離評価・reviewerの接続と実測予算を先に完成する。CPU成功や論文を品質改善の証拠にせず、元全gateと独立全pipeline/fullDEV/全440/新封印TESTを維持する。

2026-10-15終端追補: [sentence-copy確率減衰100M](../reports/phase6/pseudo-repetition-science-20261015/completion.json)を実行し、全state/元CE対照/全80内容を確認して不採用に閉鎖した。反復45→31は減ったが、一貫性2→2・適切完結2→3・BPB0.998487→0.999679で元品質・保持は未達。反復対策だけで意味の進行と完結が成立するとは確認できなかった。固定条件を救済せず、次は別の根拠ある未回答仮説を1件選定する。4項目goalはactiveで、独立fresh全pipeline/fullDEV/全440/新封印TEST/採用は有資格候補なしの未実施。下のCPU準備・科学未凍結記述は当時の履歴。

2026-10-15次条件選定: [TRAIN全句copy確率減衰のprospective案](../reports/phase6/pseudo-repetition-preparation-20261015/proposal.json)を選び、原source比較/pure14 checks/一回限り元TRAIN32x48 CPU feasibilityを完了した。原CE/10Mを保持するDITTO系variantで、旧rollout4gram ULとは負例生成と正のdetach確率目標が異なる。次は専用trainer・全state resume/disabled CE equality、その後だけowned CUDA180秒と総4800秒提案内の実測・safe science接続・凍結。教材/モデル/学習/DEV/TEST/GPU0の準備までで、品質改善や最終資格ではない。固定scopeと原品質条件は維持する。

2026-10-15進行追補: 「4まで」の再開範囲で評価reader分離と新同10M比較を実施した。最新[context likelihood100M](../reports/phase6/context-likelihood-science-20261015/completion.json)は全80内容と全state/対照照合まで完了し、不採用に閉鎖。一貫性1/80・適切完結1/80・反復50/80、全保持条件未達。次は既存結果から別の未回答介入を1件選定し、対照/原gate/実測予算を事前固定する。独立fresh全pipeline学習/fullDEV/全440/新封印TEST/採用は有資格候補ができてからで、まだ未達。Base完成までの4項目goalを比較閉鎖へ縮めない。以下の2026-10-14文書限定scope・未選定記述は当時の履歴で、後の明示再開を上書きしない。

更新: 2026-10-14 JST。現在の依頼は全現行文書の最新化と今後の計画作成。Base/Chatは未完成・未採用。研究・教材準備・診断・生成評価・GPU学習は再開していない。

[最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md) / [次の計画145](145_post_rejection_next_plan.md) / [今回更新146](146_documentation_followup.md)。

元の段階0〜5は維持し、実行の詳細は計画145へ接続する。143/144の一巡は不採用で停止、前の「6まで」は未達/blocked後にユーザーが解除。新しい介入は未選定。次の実行契約で一巡か定義済み複数比較か・総予算・ゴールを明記する。今回の文書依頼は新しい研究cycleの再開ではない。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

元Base TEST20 promptと元Chat TEST20行は別のCPU解析問題を保存した。学習・GPU TEST採点に使っていないこととCPU未解析は別。将来の有資格最終確認にはreader分離と新しい封印TESTが必要。今回data/TESTを開封・再処理しない。

次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。

## 当時の資料・保存手順

## 目指す状態と現在の判断

10,001,152パラメータ規模を維持して、日本語の短い続きを関連性・一貫性を保って完結できるBaseを完成させる。必要な品質・独立学習seed・fullDEV・protectedTEST・採用記録がそろったら通知して止める。Chat、量子化、20B/50B、公開は今回の再開後の到達範囲に含めない。

最新2BではBPB約1.45%改善に対し一貫性3/80のまま、適切完結7→5/80、反復27/80のまま。元の6絶対条件と全比較条件は未達。この候補の自動10B延長やseed43確認へ進む根拠はない。過去の2B→5B、教材増量、初期化、勾配蓄積等も結果と条件を保ったまま参照し、失敗条件を小変更して繰り返すことを既定路線にしない。

## 固定する制約

2026-10-08のユーザー方針: **10Mのサイズ維持が重要であり、それ自体を優位性とする。** 大型化と品質を選び直す計画ではなく、10Mの制約内で品質改善を目指す。

- 総パラメータは既存の約10M予算（9.5M〜10.1M、現モデル10,001,152）を維持する。大型化や大型モデル診断比較は次回の既定作業にしない。
- 比較候補は教材の品質・文脈・終端、学習目的、最適化、同予算内のパラメータ配分などから選ぶ。候補の有効性や大幅改善を事前に保証しない。
- 日本語Baseの品質基準・評価分離を維持する。モデルが小さいことを理由に基準を下げたり、物語だけ等へ対象を無断で縮めたりしない。
- 改善が得られなければ、10Mのまま限界と未達を報告する。この方針記録は学習・研究実行の再開指示ではない。

## 次の比較を選ぶ順序

まず全80の既存notesと過去completionを再利用し、文章品質の失敗と検証済み条件を対応付ける。採点のやり直しや新しいDEV抽出は行わない。例えばbase-001/002/005には同じ発話・描写・文の循環が記録されているが、これは失敗の観察であり原因の確定ではない。[既存notes](../reports/phase6/base_teacher_decay_2b_candidate_notes.json)。

| 検討順 | 調べる問い | 既存証拠と限界 | 次案に必要な条件 |
|---:|---|---|---|
| 1 | 教材の文脈・終端・配分が、関連した続きと完結を学ぶために適しているか | LF感度や原文脈診断はあるが、自由生成改善の証拠ではない。過去の教材/配合比較も複数閉鎖済み | 既存比較と異なる未回答の問いを示す。単なる増量や末尾表示修正を品質改善と扱わない |
| 2 | 正解履歴での学習と自己生成履歴での反復の差に、介入可能な要因があるか | 少数原文の記憶は成功、TRAIN既知例の自由生成にも循環がある。過去のsequence目的比較も再利用する | 既に失敗した目的・係数の再試行ではない根拠と、同教師対照を定める |
| 3 | 10M内の構成配分や最適化に、未検証の改善余地があるか | 初期化・勾配蓄積・teacher-decay等の固定条件は不採用 | 総parameter予算を先に確認し、主要変更1つの別proposalを作る。frozen model/sourceを上書きしない |

この順序は調べる優先順位であり、新しい原因・介入の採用決定ではない。既存結果だけで次案を定義できれば追加診断は省略する。どの案にも根拠が不足する場合は、調査を自動延長せず不足を報告する。

## 次案に必ず記載する項目

1. 対象とする失敗を1つと、その改善を測る主要指標。文法・関連性・一貫性・完結・停止・反復は別に記録する。
2. 仮説を支える既存report/例ID、交絡・反証、閉じた比較と何が違うか。
3. 対照と候補の実parameter数（9.5M〜10.1M内）、checkpoint/初期化、TRAIN/Tokenizer、教師予算、seed、主要変更1つ。
4. 学習時の変更と生成/表示時の変更の区別。raw文字・停止失敗を後処理で消して元品質合格としない。
5. pilot固有の事前screenと、元の全品質/保持guard。BPB低下だけで本比較へ進めない。
6. 必要CLI/未実装箇所、関連checks、実CUDA全state再開gate、ログ/identity/ledger/checkpoint保存。
7. 実測に基づくGPU上限・評価/保存の時間、失敗時の閉鎖、一巡後の報告・停止。

次の介入、教材作成、25M〜100Mのどの教師予算を使うかは、まだ選定・凍結していない。この文書は実行済みの比較や開始commandではない。

## 再開後のフェーズ

| 段階 | 目的 | 具体的な作業 | 終了条件・成果物 | 進行判断 |
|---|---|---|---|---|
| 0: 実験の整理と次条件の選定 | 同じ失敗の反復を避ける | 既存completion・raw-bound notes・実験索引を使い、未解決仮説と既検証条件を対応付ける。教材の文脈/終端、学習時と生成時の差、最適化/モデルの候補を区別する | 次の比較を最大1件に絞った提案。仮説、対照、変更点、固定量、指標、予算、反証・終了条件、未実装CLIを記載 | 未回答の問いと実行可能な比較を特定できなければ、その理由を報告して止める |
| 1: 必要な最小診断 | 次の学習が何を検証するか明確にする | 段階0で欠けていると確認した診断だけを実装。既存6文記憶/32文train-dev/LF/原contextを再実行しない | 実診断結果と事前screenの採否。追加学習は0 | 結果が次の介入を支持しない場合はその条件を閉じる |
| 2: 同条件の短い学習比較 | 文章品質が改善する兆候を調べる | 同fresh親または同学習済み親のどちらかを明記。モデル、TRAIN、教師予算、seed、評価をそろえ、主要変更は1つ。専用command/凍結config/実CUDA再開gateを用意 | 候補と対照の同教師pilot、固定DEV256/日本語評価/全80内容。raw、failure、採否を保存 | BPBだけの改善では進めない。事前に定めた生成改善screenと全保持guardを満たす場合のみ次段階を提案 |
| 3: 有望条件の本比較 | 小予算の改善が本学習でも続くか確認する | 短い比較の実測から教師予算とGPU上限を固定し、別runとして継続。段階評価と全80レビューを行う | 同条件対照との生成改善、既存絶対条件、strong/cached/historical保持条件をすべて判定 | 全条件合格でのみ最終確認候補。未達なら閉鎖し、係数/seed/予算の救済延長をしない |
| 4: 独立学習・全文DEV | 再現性と選定用小標本以外の品質を確かめる | 合格レシピでfresh学習seed43。必要なnative runner/reviewer・型付き証拠接続を実装してから実行。fullDEVと400生成＋長文40を確認 | 両学習seedの結果、fullDEV、全440 rawの内容評価、保持guard | 不合格seedを捨てて選ばない。保護TESTにはまだ触れない |
| 5: protectedTEST・採用 | 選定を固定したうえで最終判断する | 最終条件を封印後、保護TEST20prompt×5mode=100生成と本文評価を実行し全件確認 | 元最終基準の達成・再現/復旧・重み・model card・採否記録 | 全条件達成でBase完成を通知して停止。未達なら不採用と限界を報告 |

段階1は、既存証拠で次の比較を定義できる場合は省略できる。段階0の文書整理をさらに長い調査の入口にせず、一度の選定で比較案または「根拠不足」を出す。まだ次の介入条件は選定・凍結していない。QK等の検索語に一致がないことだけを、新規性や有効性の証拠にしない。

## 予算と時間の扱い

次の数値は研究を際限なく続けないための**提案上限**で、新しい凍結configや実行許可ではない。元の完了実験の予算・品質条件は変更しない。

- 段階0: 既存小記録と必要な原結果だけを調べ、選定メモ1件で完了する。全corpus再scan、全重み再hash、旧GPU再評価は行わない。
- 段階1: 新たなGPU診断が必要なら追加学習0、累積GPU120秒以内を目安に事前固定する。必要性と終了条件を定義できなければ開始しない。
- 段階2: 初回は各条件25M〜100M教師の範囲から、検出したい差と過去の立ち上がりを根拠に1つの予算を事前固定する。途中結果で範囲内を総当たりしない。小予算で比較可能でなければ、その理由と別予算を先に文書化する。
- 段階3: pilotの学習・評価・保存時間を別々に実測して見積もる。2Bや10Bを既定にせず、事前の学習曲線と比較目的から決める。
- 段階4〜5: native方式への必要な実装接続を済ませてから各予算を凍結する。既存fullDEV確認のGPU上限3000秒は旧形式の値であり、型を偽装して使ったり暗黙に増やしたりしない。

参考として、今回の追加1,905,839,805教師は評価・保存込みGPU26,060.094秒（約7時間14分）。この平均から100Mあたり約23分と計算できるが、初回compile・再開gate・固定評価・モデル/shape差を分離した学習速度ではなく、次回の所要時間保証には使えない。完成までの暦日数は未確定。

この選定→必要時診断→pilot→本比較の一巡が不採用で終わったら、いったん結果を報告して停止する。次の仮説を自動的に連続起動しない。品質基準は維持し、達成困難ならその事実と追加比較の価値をユーザーと見直す。

## 品質を判断する順序

探索screenとBase採用条件は別。短いpilotのscreenは実験固有の比較目的に合わせて事前定義するが、最終条件を代替しない。

現行固定80の絶対DEV条件は文法2≥56、一貫性2≥27、適切完結≥27、EOS≥37、反復≤18、empty/role/Unicode失敗0。加えて元policyの相対条件（一貫性差≥8・paired CI下限>0、EOS/反復/文字等の非退行、BPB保持）とstrong/cached/historical参照を各実験の指定どおり判定する。[現行policy](../configs/phase6/base_parallel_residual_review.json)、[適用したreviewer](../scripts/review_base_teacher_decay_2b.py)を参照。

独立seed、fullDEV、最終TESTの各条件も省略しない。最終TESTの停止95%等とDEVの37/80を混同しない。[最終TEST実装](../scripts/run_final_base_test.py)、[採否実装](../scripts/review_final_base_test.py)、[評価契約](evaluation_protocol.md)を維持する。新形式を既存runnerへ渡す接続は未完成であり、文書上の計画を実行可能なcommandと扱わない。

## データ増量・学習延長をどう扱うか

データ供給は一般Web準備12.23B等があり、「公開データが少ない」ことと「目的に有効なaccepted TRAINが足りる」ことは異なる。最新比較は既存accepted2B poolであり、新規データ増量ではない。

増量する場合は同source/長さ/文脈/終端を可能な範囲でそろえて教師予算を固定し、既存poolと比べる。学習延長はTRAINを固定して教師予算だけを変える。両方を変えた実験から量だけの因果効果を主張しない。重複や繰り返し学習を新規教材量として足さない。

これまでの結果は「増量は無効」「学習量は十分」「10Mでは不可能」の証明ではない。一方、今回のBPB改善だけを根拠に量を追加する判断も支持しない。次回は改善する失敗の種類を先に決めて比較する。

## 維持する運用条件

Python3.12.7はすべてuv経由、学習はWSL/Linux disk/RTX4090。実processとGPU lockを確認し、長期jobはPID/boot/start、ledger、logs、全state checkpointを永続化する。元UIは必要なGPU実験中だけ停止し、終端で元10Bへ戻す。関係のない全suiteや旧corpus照合を繰り返さない。

本計画は[ロードマップ](15_project_roadmap.md)のPhase6に対応する。Phase7〜10は長期の構想として保持するが、Base完成後もユーザーが再開するまで着手しない。

今回の見出し更新前の全文は[履歴保存一覧](../reports/investigation/documentation_plan_refresh_20261013/baseline.json)に保存した。本文の2B時間実測は当該Base比較の歴史値で、最新Chat比較の所要時間ではない。
