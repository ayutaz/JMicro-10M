# 実験台帳と検証結果

## 最新の保存結果（2026-10-05）

最新は[selector v2準備結果65](../docs/65_condition_selector_v2_preparation_results.md)。別train32の[開発比較](phase6/condition_v2_calibration_review.json)後に凍結し、同source各20M/未確認全80を診断したが弱例対照12/候補14で両内容gate未達。新GPUなし、準備失敗分岐完了で停止。[全80原文付きdata review](phase6/condition_v2_data_review.json)、[notes](phase6/condition_v2_source_notes.json)、[ready](phase6/condition_v2_ready.json)、[prepare job](phase6/condition_v2_prepare_job.json)、[judgment](phase6/condition_v2_judgment.json)、[completion/UI](phase6/condition_v2_completion.json)、[CPU5tests](phase6/condition_v2_selector_tests.xml)を保存。旧結果63とcondition_preservation証拠は保持。

以下は最新科学学習の[結果60](../docs/60_dataset_expansion_results.md)。旧60M/新200Mの各追加1B、全160内容・日本語診断・不採用判断・UIを保持。今回の教材診断とモデル評価を区別する。

| 保存report | 内容 |
|---|---|
| [dataset_expansion_result.json](phase6/dataset_expansion_result.json) | 両追加1Bの実tokens・checkpoint/比較結果、科学2,000,027,648/検証262,144別 |
| [dataset_expansion_review.json](phase6/dataset_expansion_review.json) | 一次35evidencechecks、同条件指標と原gate、full不適格 |
| [dataset_expansion_annotations.json](phase6/dataset_expansion_annotations.json) / [categories](phase6/dataset_expansion_categories.json) | 全160個別理由・カテゴリ。一人のCodex非blindで独立人手ではない |
| [dataset_expansion_judgment.json](phase6/dataset_expansion_judgment.json) / [completion](phase6/dataset_expansion_completion.json) | 不採用・条件付き全文未起動と最終20checks/元UI実確認 |
| [documentation_update_20261005.json](phase6/documentation_update_20261005.json) | 今回の文書更新のリンク・実量・旧原文/凍結証拠保持・同期確認。GPU学習/品質checksではない |

大型weights/source/raw/jobはLinux `reports/phase6/dataset-expansion-1b-20261005/`、200M教材は`~/jmicro-data/phase6/dataset-expansion-20261005/`へ保持。Gitだけでは復元できない。[移行一覧](../docs/windows_handoff.md)。実験完了commit `afad164`、今回pushなし。

## 主系列・基盤の保存結果（履歴）

| 保存report | 実際に確認したこと |
|---|---|
| [corpus_10b_ready_review.json](phase6/corpus_10b_ready_review.json) | train12,225,819,077 tokensをbuilder/raw再構成/実loaderで受け入れ。独立全corpus auditは未完了 |
| [base_5b_review.json](phase6/base_5b_review.json)、[比較review](phase6/base_5b_comparison_review.json) | 主要Web5,000,003,584 tokensの実学習・保存・全文dev/固定400評価 |
| [eos_5b_finish_review.json](phase6/eos_5b_finish_review.json)、[Unicode原因確認](phase6/eos_5b_finish_unicode_review.json) | 同じ5B親から各100,007,936追加。Web BPB0.958092、短文0.959011、短文EOS13/80・反復51/80へ改善。ただしraw Unicode2/400で最終採用不合格 |
| [base_10b_preparation_review.json](phase6/base_10b_preparation_review.json)、[14tests](phase6/base_10b_tests.xml) | 専用10B準備完了、26保存checksと実CUDA全state再開一致。16更新/524,288検証tokensは科学学習と別。準備時の科学学習は0tokens |
| [base_10b_training_review.json](phase6/base_10b_training_review.json)、[終了記録](phase6/base_10b_training_completion.json) | 科学学習総10,000,007,168 tokens完了、終端state/全metrics等19checks成功。実process終了、GPU7,657.678秒。当時は品質評価未実施で、後続comparison reviewに評価結果を保存 |
| [base_10b_comparison_review.json](phase6/base_10b_comparison_review.json)、[内容確認](phase6/base_10b_content_review.json)、[終了確認](phase6/base_10b_comparison_completion.json) | 同条件全文dev/400完了、CPU23checks成功。BPB0.954018 / EOS0・反復53 / Unicode0、元増量gate合格、実用品質未達。GPU786.881秒 |
| [documentation_refresh_20261004.json](phase6/documentation_refresh_20261004.json) | 現行文書と計画の整理、元13文書の履歴保存、内部リンク・凍結条件・WSL同期の確認。GPU jobは開始しない |

科学10Bの専用品質比較入口・同条件dev/400・全固定80と自然停止9件の内容確認も完了。[品質結果](../docs/42_base_10b_quality_evaluation.md)。学習完了CPU reviewerは実際の終端stateと全科学metricsへ適用し、19項目成功。起動時のlaunchとrunning reviewは進捗履歴として保持する。[学習結果と速度](../docs/41_base_10b_training.md)、[status](../docs/autonomous_status.md)、[後続の同条件評価計画](../docs/39_learning_scale_and_generation_plan.md)。今回は報告・local commitで停止する。Base/Chat品質、独立人手blind/test、新重みの量子化品質は未達・未検証。

## 過去の記録の読み方

以下は各段階完了時の証拠で、当時の停止境界や未開始の記述を現在の実行指示にしない。旧原文は[保存履歴](../docs/autonomous_history_20261004.md)にも保持する。完了reportやsnapshotは上書きしない。

`phase0/`にiMacの環境・準備検証・完了監査を記録する。`p0-<name>-<UTC>-<random>/`は学習を実行しない準備runのsnapshotで、`experiments.jsonl`に追記する。大型/機械依存のrun snapshotはGit管理外。

準備runは`kind=preparation,status=prepared,tokens_seen=0`。モデルconfigと学習済みTokenizer artifactを区別し、Phase 2前のTokenizer/data入力hashは`null`で未作成を示す。学習を実施した結果として扱わない。

snapshotにはcode/docs/config/eval/lockfile、各hash、環境、Git commitとdirty状態を含める。未コミット変更もsource snapshotから復元できる。既存runの変更はchecksum検証で検出する。Phase 4の学習runは別の`schemas/training_run.schema.json`を使用する。準備schemaや過去snapshotは書き換えない。

`phase1/`には実データpilotの統計、20件の内容レビュー、全件復元・split検証、再生成比較と完了監査を保存する。本文・原file・Parquet・大きなsplit membershipは`data/phase1/`のGit管理外領域に置き、reportのchecksumと[再生成手順](../data/README.md)から照合する。Phase 0の過去環境・監査を上書きせず、現在の開発検証には`reports/local/`等を使用する。

`phase2/`にはTokenizer契約・全coverage候補・全corpus計数、`phase3/`には両実モデルの契約、native export parity、量子化実型・容量、完了監査とテスト結果を保存する。これらPhase 2〜3のモデル重みはランダム初期化。Phase 4当時はGPU検証学習までで、Base/Chat本学習は未実施だった。現在の実績は上表を参照。大型Tokenizer/weights/native runtimeは`artifacts/`のGit管理外で、reportのhashを照合する。詳細は[Phase 2](../docs/18_phase2_completion.md)、[Phase 3](../docs/19_phase3_completion.md)。

## Phase 4の実機証拠

`phase4/environment.json`、`handoff_report.json`、`resume_report.json`、`throughput_report.json`、`base_evaluation_contract_report.json`、`resource_budget.md`をGit保存した。handoffは全7 gate成功、全64 tests / skip 0、両モデルの全state resume一致。eager最大batchはT8K 57 / T4K 64、compiled容量は未探索、Flash-onlyの失敗は残す。

rawログ・source snapshot・checkpoint・生成出力はLinux実行コピーの`reports/phase4/gates-20261003/`に保持する。集約reportのraw path/SHAを照合し、Git cloneだけでraw checkpointまで復元できるとは扱わない。Phase 4終了時にはPhase 5は未開始だった。[完了記録](../docs/21_phase4_completion.md)

## Phase 5の実学習・比較証拠

`phase5/`にはoverfit/smoke、4本の100Mのtraining/evaluation audit、凍結plan、共通bytesと固定生成の集約、候補config、採用・棄却理由、独立監査、実測予算と停止確認を保存した。全68 tests / skip 0、4構成のCUDA厳密resume、overfit全5 gate、全比較と補助評価が成功。候補はT4K / NoQK-Norm / LR 0.002。停止・反復・sampling Unicodeの品質目標は未達で、Phase 5当時はNoNormのHF/GGUF adapterが未実装だった。現在は④でCPU精度profileによる学習済み変換を検証済み（下記④⑤）。[完了記録](../docs/23_phase5_completion.md)

raw evidenceはLinux checkoutの`reports/phase5/run-20261003-docoverfit/`へ保持する。GPU job/launcherは終了済み。自動生成の`candidate_selection.md`と`completion_audit.json`をそのまま保存し、詳細な採否レビューを`candidate_selection_review.md`へ分けた。Phase 5終了当時はPhase 6本学習未開始だった。

将来のrunを再実行する場合は別directoryへ出力する。既存run/reportやPhase 0〜3のhashを更新で上書きしない。現在の文書検証等は`reports/local/`へ保存する。

## Phase 6①②の完了証拠と文書更新

以下の①②reportは[事前の目的・条件](../docs/25_phase6_preparation.md)に対応する。train 756,087,912 unique stream tokensの拡張corpusとWSD stable/独立decayを準備した。[完了記録](../docs/26_phase6_preparation_completion.md)。③の容量/速度・長期Base/Chat・品質達成の証拠ではない。

| report | 確認したこと |
|---|---|
| [sources.json](phase6/sources.json)、[acquisition.json](phase6/acquisition.json) | 固定revisionの条件資料・取得上限、8 filesの上流SHAとraw 2,152,539,810 bytes |
| [corpus_manifest.json](phase6/corpus_manifest.json)、[corpus_audit.json](phase6/corpus_audit.json) | 全1,803,712 raw、signature/cluster・split、全retained 1,783,193文書の本文/token/index/文字往復。manifestは作成時ラベルを保持し、監査結果はauditを正とする |
| [quality_review.json](phase6/quality_review.json) | 24 train文書の先頭最大420文字を確認。品質リスク・確認範囲を記録 |
| [wsd_resume_report.json](phase6/wsd_resume_report.json)、[evaluation_isolation.json](phase6/evaluation_isolation.json) | CUDA/BF16/math/batch 8、stable 200 vs 100+100・decay 100 vs 50+50の全state完全一致、元枝不変性とdev評価状態保全。73 GPU checks |
| [tests.xml](phase6/tests.xml)、[completion_audit.json](phase6/completion_audit.json) | 全74 tests / skip・failure・error 0、独立監査55 checks、12 checkpoints・336 snapshot files、過去report 57 filesとlock不変 |
| [preparation_failures.json](phase6/preparation_failures.json) | 初回scheme失敗・schema不足と修復。条件を緩めず失敗履歴を保持 |
| [hub_artifacts_verification.json](phase6/hub_artifacts_verification.json)、[process_completion.json](phase6/process_completion.json) | 公開25 payload照合/restored 0、launcher終了と停止確認 |
| [documentation_audit.json](phase6/documentation_audit.json)、[final_package_audit.json](phase6/final_package_audit.json) | ①②完了時点の43 Markdown / 393内部リンク、Windows/WSL 91 source filesの同期、包装監査13 checks |
| [documentation_update_20261003.json](phase6/documentation_update_20261003.json) | ①②後の文書・残りの計画更新を別監査した当時の記録。旧report/実装/config/lock/eval不変、文書リンク・CLI・WSL同期・停止境界を確認 |

大型dataは`~/jmicro-data/phase6/{raw,expanded-v2}/`、CUDA checkpoints/log/source snapshotsはLinux checkoutの`reports/phase6/preparation-20261003/cuda/`。①〜⑤のjobは終了済みで、当時は本学習前で停止した。Git clone/Hub bundleだけで拡張data/checkpointsが揃うとは扱わない。既存snapshotと完了reportは当時の証拠として保持し、現在の文書を過去snapshotへ書き戻さない。今後の実行順は[本学習以降の計画](../docs/27_phase6_remaining_plan.md)。

## Phase 6③の高速化・容量・再開証拠

③は`a7d26e1`でcommit済み。[完了記録](../docs/29_phase6_performance_completion.md)。Flash＋compile reduce-overhead / batch 32=694,521 tokens/s、最大安定111/112 OOM。以下は①②のreportとは別の実測で、品質達成・長期Baseの証拠ではない。

| report | 確認したこと |
|---|---|
| [batch_performance_report.json](phase6/batch_performance_report.json)、[batch_choice.md](phase6/batch_choice.md)、[performance_summary.json](phase6/performance_summary.json) | 最速・容量・保存/評価込みVRAM・速度比・unique metricsのtoken台帳 |
| [performance_completion_audit.json](phase6/performance_completion_audit.json)、[performance_cold_resume_report.json](phase6/performance_cold_resume_report.json)、[performance_tests.xml](phase6/performance_tests.xml) | 独立1286 checks、空cache再開26 checks、79 tests / skip・failure・error 0 |
| [performance_failures.json](phase6/performance_failures.json)、[performance_audit_initial_failure.json](phase6/performance_audit_initial_failure.json) | 初回cache/backend・観測不足・監査のoutput数誤判定を保持 |
| [performance_documentation_audit.json](phase6/performance_documentation_audit.json) | ③完了時の文書/CLI/WSL同期・旧73 reports/lock保持と実装/report binding |
| [plan_update_20261003.json](phase6/plan_update_20261003.json) | 今回の最新計画・完了チェック・算術予算・文書同期と旧成果/コード保持の監査 |

raw logs/requests/compiled code/source snapshots/checkpointsはLinux `reports/phase6/performance-20261003-v3/`と`performance-cold-resume-20261003/`に保持する。④生成/変換と⑤長期設定凍結は完了した。当時の次段階は500M評価で、現在は5B/仕上げ比較まで完了した。

## Phase 6④⑤の検証・設定凍結と停止

④⑤は`93c7d1d`へcommit済み。[実施記録](../docs/30_phase6_readiness_execution.md)。

| report / config | 確認したこと |
|---|---|
| [generation_diagnostics.json](phase6/generation_diagnostics.json)、[expanded_dev_baseline.json](phase6/expanded_dev_baseline.json) | 固定dev400生成と拡張dev89,416文書の全文採点、BPB/時間/未達品質、本文一度採点・EOS分離 |
| [nonorm_export_parity_report.json](phase6/nonorm_export_parity_report.json)、[readiness_export_audit.json](phase6/readiness_export_audit.json) | CPU精度profileで学習済み短/1024・full/cacheの全12比較、13契約、実CLI/全119 GGUF重みの独立149 checks |
| [nonorm_precision_repair_report.json](phase6/nonorm_precision_repair_report.json)、[stock失敗](phase6/nonorm_export_stock_fp32_failure.json) | 精度修復の採否、途中/stock/CPU8設定/CUDA参照の失敗保持。GPU学習coreと重みは不変 |
| [readiness_stability_report.json](phase6/readiness_stability_report.json)、[readiness_gpu_audit.json](phase6/readiness_gpu_audit.json) | LR3候補×2,000 stable＋100独立decay、LR0.002採用、厳密50/cold25完全一致、独立106 checks |
| [readiness_precision_tests.xml](phase6/readiness_precision_tests.xml)、[readiness_gate_audit.json](phase6/readiness_gate_audit.json) | 全90 tests / skip・failure・error 0、指定範囲の6要求と停止境界の37 checks。Base品質合格ではない |
| [base_frozen.json](../configs/phase6/base_frozen.json)、[base_launch_plan.json](phase6/base_launch_plan.json) | version2のmodel/data/source/runtime、batch32/LR0.002/WSD global305,176更新、独立decay5%、保存/容量/実起動・再開CLI |
| [旧version1](../configs/phase6/base_frozen_blocked_v1.json)、[base_launch_guard_report.json](phase6/base_launch_guard_report.json) | 修復前の起動不可設定と実起動拒否をbyte保持 |
| [documentation_refresh_readiness_20261003.json](phase6/documentation_refresh_readiness_20261003.json) | ④⑤完了後の25文書・残りの計画更新。凍結条件/CLI/算術予算、内部リンク、WSL同期、旧実装/設定/証拠の保持と停止を検証 |

raw logs/checkpoints/weights/logits/snapshotsはLinux `reports/phase6/readiness-20261003/`、正式exportは同runの`export-stable-f32/`。専用CPU runtimeは`artifacts/runtime-stable-f32-v2`。Git/Hubだけでは復元できず、Windowsコードとともに引き継ぐ。当時の`launch_enabled=true`は技術gate成立を示し、当時は本学習前で停止した。現行10Bは専用configを使う。


## 拡張trainの500M学習・評価

2026-10-03: 拡張trainの500M stable＋独立763更新decayと全文dev/400生成評価を完了。同一dev BPB 1.244126→1.022491、抑制greedy EOS 0/80→0/80、反復48/80→66/80。全99 tests成功。人手blind採点・test・Chat・新重みの量子化は未実施。1B前で停止。

- [学習/評価/paired CI/全checkpoint監査](phase6/base_500m_review.json)、[全80 greedy生成例](phase6/base_500m_review.md)。
- [起動前照合](phase6/base_500m_preflight.json)、[全99 tests](phase6/base_500m_tests.json)。
- [固定20件の内容点検](phase6/base_500m_content_review.json)はCodexによる定性的な確認で、blind人手採点ではない。予測BPB改善と生成退行を分け、1B前で停止する。

raw evidenceと18 checkpointsはLinux `reports/phase6/base-20261003/`へ保持する。今回の新しい重みのexport/量子化は未実施。

## 500M後の反復・EOS・データ構成の調査

- [当時のローカル10Bデータ整備計画](../docs/32_local_10b_corpus.md)。WSL保存、全件重複/heldout保護/token監査を行い学習前で停止する。全105tests成功。この計画作成当時は実構築・監査未完了。現在は12.23Bを利用確認済み、独立全corpus監査未完了。
- [LSH性能のprefix probe](phase6/corpus_10b_cost_probe.json)、[実1M・全32bandsでの並列比較](phase6/corpus_10b_parallel_probe.json)。候補coverageと全代表が一致、30.004→9.135秒（3.285倍）。取り込みcheckpointを保持したexecution v3へ移行した。全10Bの監査完了ではない。
- [実ローダー利用確認の手順](../docs/32_local_10b_corpus.md#学習用ローダーでの最終利用確認)。Shard/BlockSamplerでtrain batch/mask/bytes/replayを検証する。小fixtureは当時成功。現在の実loader確認と独立監査の範囲は上表を参照。
- [以前の2B/5B計画](../docs/autonomous_history_20261004.md)は10Bの実行依頼へ更新した。
- [保留したdecoder比較の計画](phase6/repetition_decoder_plan.json)、[以前の作業順序](../docs/autonomous_history_20261004.md)、[当時の計画の16項目照合](phase6/repetition_decoder_plan_audit.json)。同じ10Mパラメータの重みで640outputs/GPU15分上限を比較する案。監査は当時の計画を確認した記録で、現在の優先作業や実行結果ではない。
- [事前計画](phase6/repetition_diagnosis_plan.json)、[判断と比較](phase6/repetition_diagnosis_review.md)、[数値/binding/20項目監査](phase6/repetition_diagnosis_review.json)、[225既存files保持](phase6/repetition_preservation.json)、[終了・同期監査](phase6/repetition_completion_audit.json)。
- EOS教師欠落は確認されず、文書末尾予測は改善。反復は拡張131Mから多く、decayで70/80→66/80。全文の文書長と固定sample反復に大幅増加はない。短prefix/greedyと学習分布の違いを次の比較候補とし、因果未分離・精度差を残す。
- 全102 tests成功。GPU推論249.75秒、学習更新0、1B未開始。Linux raw evidenceは`reports/phase6/repetition-diagnosis-20261003/`。次回案を開始せずcommit後停止する。
