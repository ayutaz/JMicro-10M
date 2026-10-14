# 現在の状態

更新: 2026-10-15 JST。文書更新は結果32b8f58/receipt d44b8a0で完了し、ユーザーが目標を解除。その後「4まで進めてください」で直前の4項目（評価分離修理→新同10M比較→合格候補の独立学習/全文DEV→新封印TEST/採用）が明示再開された。Base/Chatは未完成・未採用。Chat/SFT・量子化・大型化・公開は範囲外。

**最新終端: fresh FIM pilotは不採用で閉鎖。** [completion](../reports/phase6/base-fim-pilot-20261015/completion.json) / [全80採否](../reports/phase6/base-fim-pilot-20261015/review.json)で実10000更新・正確94160195教師、同native初期化/元抽出/quota/EOS/bytes/full sampler/original stream digest/actual schedule、DEV256と全80個別raw-bound notesを確認。対照→候補は文法28→31、一貫性2→2、適切完結3→2、EOS13→14、反復49→51（各80）。BPB1.2902028921801718→1.2924141763731125、一貫性差0/95%CI[-.0375,.0375]でpilot screen未達。Unicode/role/empty/FIM marker漏出0。科学GPU1527.822099743993＋技術9.153451952966861＝1536.9755516969599秒、科学2519/総3600内。評価openはDEV manifest/casesとDEV shard4ファイルの6種類のみ。実PID1343は終了、元UI実PID3223/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start64296679とHTTP元親/Tokenizer/10M/idleへ復帰を確認。最終checkpoint SHA5328bca46dbbbd88b1756c3cf7d177c0539c72a25c76ba66caadb9bd1dc7034d、全weights/Adam/RNG/sampler/metricsはWSL保全。再launch/延長/FIM率・marker・span・horizon・seed・decoder救済をしない。独立学習/fullDEV/新TEST/採用0、4項目目標未達のままactive。次は別の根拠ある比較選定で、閉鎖を目標完了に読み替えない。以下の稼働記述は当時の観測。

[終端10000 CPU監査](../reports/phase6/fim-feasibility-20261015/checkpoint10000_CPU_audit.json)も完了。旧auditorは演算順の違いで5更新のLRに4.3368e-19差を出したが、[診断](../reports/phase6/fim-feasibility-20261015/LR_audit_expression_diagnosis.json)で実native scheduleと全10000ログの差0を確認。phaseを先に計算する正しい順へauditorのみ修理し、exact比較を緩めず全state/metrics auditを通した。科学sources/学習結果は変更していない。Codex非blind/既知DEV・未成熟fresh1seedの1条件で、FIM一般や10M容量限界の証明ではない。

稼働中の別CPU作業: [2000更新checkpoint監査](../reports/phase6/fim-feasibility-20261015/checkpoint2000_CPU_audit.json)で18836429教師・全更新実LR・FIM会計・finite native/Adam/clockの整合を確認。追加学習/GPU/品質評価0。将来のfixed diagnosticsは[入力export](../reports/phase6/fim-feasibility-20261015/Japanese_diagnostic_export.json)で保存済みDEV-only記録からsemantics192/JBLiMP331/JCQA1119の入力/選択肢/元gold labelのみを投影し、新reader13 CPU checks passed。予測・scores・creditを移さず、混在suite/TEST/元corpusを開かない。payloadはWSL data rootのみ、manifest SHA06fcf2c18f086ee57c4f615e5ae765f568024912148bf94be891b1581e7edadd。既知診断の隔離であり未知DEV/封印TEST/品質改善の証拠ではない。JBLiMPは既知public固定benchmarkのproject DEV-roleで、新しい排他的DEV splitを発見したとは記載しない。稼働中FIMのfrozen sources/条件/評価へ接続・変更していない。

**最新: fresh FIM pilotの科学学習が稼働中。** [起動観測](../reports/phase6/fim-feasibility-20261015/science_launch_observation.json)で実WSL PID1343/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start64143474、GPU lock/Windows worker34484を確認。観測675更新/6352596教師は途中値で完了値ではない。[凍結科学契約](../configs/phase6/base_fim_pilot_20261015.json) SHA c514ac4a944e7ca5974879585d902f0276a7ab544bf4ad9f226d971f48a61198はfresh native42/batch80/元2B schedule/TRAIN、10000更新/正確94160195教師、科学GPU2519秒/技術含む総上限3600秒。永続CLI・DEV256/隔離greedy80評価・notes/reviewerと13 CPU checksを完成。Python open監視でDEV評価allowlistを守り、旧混在Base/Japanese readerを呼ばない。初回Windows worker35328はUI停止直後のGPU解放待ち不足で科学開始前に安全停止し、原ログを保存。別v2 launcherが既知UI PIDだけ最大15秒待ち、凍結science sources/条件/予算を変更せず開始した。元UIは学習中だけ停止、終端でlauncherが元10Bを復帰する。現在の生存は再観測する。品質評価/全80内容review/資格/独立学習/fullDEV/新TEST/採用は未達。下の「科学0/未凍結」は開始前の履歴。

最新は[fresh FIM pilotの準備](../reports/phase6/fim-feasibility-20261015/protocol_readiness.json)。同native10M・元TRAIN・batch80/seed42/元2B schedule、既存fresh対照の10000更新/94160195教師を使う1条件を[prospective案](../reports/phase6/fim-feasibility-20261015/fresh_FIM_pilot_proposal.json)として選定。元抽出/quota maskの後に文書内PSMを適用し、marker labelsを-100、body+EOS<=512のcomplete unit以外は元ARの全窓を維持する。trainer/sampler16 CPU checks、probe workflow9 checks、実10M zero weights/Adam/schedule/training RNGと各2560行の元抽出・material RNG一致を確認。[専用CUDA結果](../reports/phase6/base-fim-probe-20261015/result.json)は40技術更新/383190教師、4対2+2全state/history一致、80x1024/32 timings、GPU9.153451952966861秒。pilot予測2519秒は提案総上限3600秒以内。**科学学習/品質評価0、科学契約未凍結**。永続science CLI・隔離DEV256/80評価・notes/reviewerがまだ必要。元UIは実PID520/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start63915576、HTTP元親/Tokenizer/10M/idleへ復帰確認。記録時の観測で、次起動前に再確認する。元model/frozen sources/閉じたrecipeは変更していない。

下の24文書監査と未選定メモは、このprospective選定前の証拠。CPU/CUDA準備を品質改善・独立学習・fullDEV・新TEST・採用に読み替えない。旧Japanese `build_tasks`もsemantic全行解析後のDEV filterと全manifest source hash読みがあるため、新しい安全なDEV経路へそのまま呼ばない。新TEST内容の確認は行っていない。[参考モデルの公開metadata](../reports/phase6/fim-feasibility-20261015/reference_model_metadata.json)はrevision74b3a173…でカードの会話3/40・長会話0/12を確認し、今回のBase基準達成例と扱わない。外部weights/Tokenizerの取得・実行・学習素材の移入なし。

次案調査で[FIMの固定24 TRAIN CPU監査](../reports/phase6/fim-feasibility-20261015/actual_TRAIN_serialization_audit.json)を完了。新serializerのCPU20 checks passed、既存accepted TRAINから各genre8文書を固定抽出し、元token/bytesとEOS identityを保存、全24がcontext1024内。原4096 codecでordinary markerは計35token、標本の元教師位置に対する追加入力26.2746%。新教材作成・元本文export・実model生成・科学学習・GPU・DEV/TEST読取り0。literal markerは原論文special sentinelと異なり、EOSは復元middleの終端になる。[選定メモ](../reports/phase6/fim-feasibility-20261015/selection_assessment.json)で成熟親100M FIMの自動開始を見送り、fresh比較の通常Baseへの転移根拠、marker教師/mask、長文処理、対照、horizonと実測予算を未確定として残す。新科学recipeは未選定で、独立学習/全文DEV/新TEST/採用も未達。CPU実装可能性を品質改善や全目標完了に読み替えない。

[評価分離修理147](147_evaluation_boundary_repair.md)でDEV専用manifest/readerと新生成/review境界を実装。CPU21 checks passed、既に保存したDEV80から入力のみをexportし実read-setを3ファイルに限定した。元混在suite/TESTは開いていない。生成答えの教材化0・実モデル評価/GPU0・品質改善の証拠0。旧frozen sources/事故/全結果は保全。次は既存証拠から新介入と対照/予算/必要CLIを定義し、隔離済み経路で比較する。独立学習/全文DEV/TESTは候補資格が成立してから。

[最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md) / [次の計画145](145_post_rejection_next_plan.md) / [今回更新146](146_documentation_followup.md)。

前の「6まで」は未達でblockedとなり、ユーザーが解除。その後の文書/計画目標は完了し、現在は別の「4まで」の再開目標。以前のblocked countや再開質問を新目標へ引き継がない。

最新の[文書長重み比較144](144_base_document_balance_results.md)は17,698更新・正確100M教師・全80理由付き内容・共通DEV256/Japanese192/331/1119・全state/元文書重み/対照全samplerとdigestを確認して**不採用で閉鎖**。文法44→23、一貫性2→1、適切完結2→2、EOS19→20、反復45→50（各80）。BPB0.998487→1.000710、一貫性差CI−3.75〜0ポイントで原品質・保持未達。

CPU21 checks、有限192 TRAIN診断、実CUDA47技術更新/273,521教師は別証拠。新GPUは科学1,474.808693＋技術8.721357＝1,483.530050秒、科学上限3,855/技術込み上限4,800以内。[数値監査](../reports/phase6/base-document-balance-comparison-20261014/numeric_completion_audit.json)、[全採否](../reports/phase6/base_document_balance_comparison_review.json)、[閉鎖・条件分岐](../reports/phase6/base_document_balance_comparison_completion.json)。

本比較延長・fresh独立学習seed43・fullDEV/400＋40・封印TEST・採用は有資格候補なしで未実行・passed=false・品質未確認。6段階すべての実施、Base完成とは記載しない。計画143/124の不合格時の報告停止条件でこの1比較を終了。追加の研究・学習を自動起動しない。

元Base TEST20 promptも既存greedy80がDEV抽出前にCPU構文解析していたことを確認。学習・GPU TEST採点0、TEST shard未開封だが、元TEST promptを未参照とは呼べない。[問題と訂正](../reports/phase6/base-document-balance-comparison-20261014/original_TEST_prompt_exposure.json)。将来の有資格Base最終確認は別artifactのDEV/TEST readerと新しい封印TESTが必要。今回は候補なしで代替TEST未準備・未採点。

科学PID337424/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start60325743は終了。元10B UIはPID338403/start60473641で復帰、HTTP元親/Tokenizer/10M/idleを確認。最新Base候補はWSL `reports/phase6/base-document-balance-comparison-20261014/document_balance/checkpoint-00017698.pt`、SHA `d89caf23bd7d2d8d81f298cb6f1fcbfe5fbd581105f91be1c3cfc18cefc9f86b`。重み・全sampler・全metricsはWSL保全。結果commit1901564/receipt fc1a3fc、93Git内容・40保全file・232local linksの納品照合は完了。元UI確認は当時の観測で現在保証ではない。

## 前回Chatの完了結果

[低学習率比較141](141_chat_lr_comparison_results.md)で、計画139の介入選定・同10M比較・有資格候補だけの独立確認への分岐を完了し、候補S1を不採用で閉鎖した。元10B親、同accepted TRAIN/Tokenizer/seed42/教師量/schedule/paddingでpeak LR1e-4→3e-5を比較。S0は138のS1の歴史state、新学習0。

| 項目 | 実際の証拠 |
|---|---|
| 固定参照 | native10,001,152 parameters、Tokenizer4096、context1024。9.5M〜10.1Mを維持 |
| 教材 | TRAIN41,529 target、660,109教師/周。280sample QAを再利用。新教材・新QA0 |
| S1学習 | 3,646更新・1,899,557 Assistant本文+EOT教師、許容内超過2。全3state・全update入力/label digest確認 |
| 全評価 | 28セット・6,132理由付き内容判断・共通NLL7点×2,634 target。既知12セット2,628判断は出典付き再利用 |
| 技術確認 | CUDA probe9＋連続/保存再開16の25検証更新。品質や本学習へ数えない |
| 資源 | 新GPU2,658.673158秒/33,600秒。過去の学習やCPUレビュー時間と別 |
| 保存 | 結果commit89275a8、納品commit09f338eの360ファイル保存・Git内容を確認。push/公開なし |

| 最終セット | S0内容 /80 | S1内容 /80 | S0自己文脈 /24 | S1自己文脈 /24 |
|---|---:|---:|---:|---:|
| 新DEV | 13 | 20 | 3 | 5 |
| 138 DEV | 19 | 18 | 3 | 5 |
| 133 DEV | 21 | 19 | 6 | 5 |
| 元旧DEV | 11 | 15 | 1 | 1 |

原条件は全セット内容56/80以上、自己生成文脈15/24以上など。新内容差+8.75ポイント、95%CI −1.25〜+18.75も改善条件未達。反復非退行・停止の条件も不成立、新自己生成Unicode失敗1を保存。低LRでDEV NLLが対照より低くても品質合格ではない。

[科学監査](../reports/phase7/chat-lr-20261014/completion.json)、[採否](../reports/phase7/chat-lr-20261014/selection.json)、[納品記録](../reports/phase7/chat-lr-20261014/final_delivery_checks.json)。

## 完了したことと未確認

前の「3まで進めてください」は比較・採否・条件分岐・報告・保全・ローカル納品まで完了した。Base保持、sampling、fresh学習seed43、人間blind、fullDEV、封印TEST、採用の7分岐は候補なしで未実行・passed=false・品質未確認。独立確認を実行した、モデルが完成したとは記載しない。

判断はCodex非blind、QAは標本、対照は歴史state。独立corpus監査・正式Base/Chat採用も未確認。Base単独原因・10M容量限界は確定していない。

元Chat TEST20行を準備時にCPU構文解析した事故を[141](141_chat_lr_comparison_results.md)へ保存。学習・GPU評価への使用0だが、未参照の主張は取り消した。将来の有資格Chat最終確認には新たな封印TESTが必要。元Base TESTは事故では解析していない。

## 次の判断と停止境界

[比較143/結果144](144_base_document_balance_results.md)は不採用で閉鎖。今回の文書・計画・保存検証を完了して通知する。次の研究の順序と終了範囲は計画145を正とし、再開は別の明示指示。原品質・10M・独立確認を維持し、閉じた条件の係数/seed/親/予算延長で救済しない。Chat・量子化・公開へ自動移行しない。Base/Chatと全体projectは未完成。

## UI・保存先・履歴

最後の納品観測2026-10-14T07:30:16Zは元10B UI PID338403/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start60473641、元親/Tokenizer/10M/idleを確認。現在の生存保証ではない。文書更新では再診断・再起動していない。

前回Chat S1はWSL `reports/phase7/chat-lr-20261014/S1/checkpoint-00003646.pt`、SHA `f7e8bb8b1569cb45ac399108455a66c5922f64d7898e8ab6b4931ba13c856018`。重み・samplerを含む全state・教材はWSL、Git正本はWindows。[引継ぎ](windows_handoff.md)。

Base結果[123](123_base_teacher_decay_2b_results.md)、教材汎化[136](136_chat_generalization_results.md)、意味多様性[138](138_chat_semantic_diversity_results.md)、最新LR[141](141_chat_lr_comparison_results.md)は別runの閉鎖済み証拠。元UI10B・別staged約10.6B・teacher-decay2B・後続SFTの学習量を合算しない。

[公開保存版126](126_model_archive.md)は2026-10-09の主要3系列保存で、dataset/samplerを除外。後続Chat重みは公開していない。当時のpush許可は当時の納品に限る。

旧運用全文と全311文書のhashは[更新前baseline](../reports/investigation/documentation-refresh-20261014/baseline.json)に保全。[全体125](125_project_retrospective.md)と[固定台帳](retrospective/README.md)は当時のrevisionを保持する。
