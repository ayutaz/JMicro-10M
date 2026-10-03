# 実験台帳と検証結果

`phase0/`にiMacの環境・準備検証・完了監査を記録する。`p0-<name>-<UTC>-<random>/`は学習を実行しない準備runのsnapshotで、`experiments.jsonl`に追記する。大型/機械依存のrun snapshotはGit管理外。

準備runは`kind=preparation,status=prepared,tokens_seen=0`。モデルconfigと学習済みTokenizer artifactを区別し、Phase 2前のTokenizer/data入力hashは`null`で未作成を示す。学習を実施した結果として扱わない。

snapshotにはcode/docs/config/eval/lockfile、各hash、環境、Git commitとdirty状態を含める。未コミット変更もsource snapshotから復元できる。既存runの変更はchecksum検証で検出する。Phase 4の学習runは別の`schemas/training_run.schema.json`を使用する。準備schemaや過去snapshotは書き換えない。

`phase1/`には実データpilotの統計、20件の内容レビュー、全件復元・split検証、再生成比較と完了監査を保存する。本文・原file・Parquet・大きなsplit membershipは`data/phase1/`のGit管理外領域に置き、reportのchecksumと[再生成手順](../data/README.md)から照合する。Phase 0の過去環境・監査を上書きせず、現在の開発検証には`reports/local/`等を使用する。

`phase2/`にはTokenizer契約・全coverage候補・全corpus計数、`phase3/`には両実モデルの契約、native export parity、量子化実型・容量、完了監査とテスト結果を保存する。これらPhase 2〜3のモデル重みはランダム初期化。Phase 4では別途GPU検証学習を実施したが、Base/Chat本学習は未実施。大型Tokenizer/weights/native runtimeは`artifacts/`のGit管理外で、reportのhashを照合する。詳細は[Phase 2](../docs/18_phase2_completion.md)、[Phase 3](../docs/19_phase3_completion.md)。

## Phase 4の実機証拠

`phase4/environment.json`、`handoff_report.json`、`resume_report.json`、`throughput_report.json`、`base_evaluation_contract_report.json`、`resource_budget.md`をGit保存した。handoffは全7 gate成功、全64 tests / skip 0、両モデルの全state resume一致。eager最大batchはT8K 57 / T4K 64、compiled容量は未探索、Flash-onlyの失敗は残す。

rawログ・source snapshot・checkpoint・生成出力はLinux実行コピーの`reports/phase4/gates-20261003/`に保持する。集約reportのraw path/SHAを照合し、Git cloneだけでraw checkpointまで復元できるとは扱わない。Phase 4終了時にはPhase 5は未開始だった。[完了記録](../docs/21_phase4_completion.md)

## Phase 5の実学習・比較証拠

`phase5/`にはoverfit/smoke、4本の100Mのtraining/evaluation audit、凍結plan、共通bytesと固定生成の集約、候補config、採用・棄却理由、独立監査、実測予算と停止確認を保存した。全68 tests / skip 0、4構成のCUDA厳密resume、overfit全5 gate、全比較と補助評価が成功。候補はT4K / NoQK-Norm / LR 0.002。停止・反復・sampling Unicodeの品質目標は未達で、NoNormのHF/GGUF adapterも未実装。[完了記録](../docs/23_phase5_completion.md)

raw evidenceはLinux checkoutの`reports/phase5/run-20261003-docoverfit/`へ保持する。GPU job/launcherは終了済み。自動生成の`candidate_selection.md`と`completion_audit.json`をそのまま保存し、詳細な採否レビューを`candidate_selection_review.md`へ分けた。Phase 6本学習は未開始。

将来のrunを再実行する場合は別directoryへ出力する。既存run/reportやPhase 0〜3のhashを更新で上書きしない。現在の文書検証等は`reports/local/`へ保存する。

## Phase 6①②の完了証拠と文書更新

`phase6/`は[事前の目的・条件](../docs/25_phase6_preparation.md)に対応する。train 756,087,912 unique stream tokensの拡張corpusとWSD stable/独立decayを準備した。[完了記録](../docs/26_phase6_preparation_completion.md)。③の容量/速度・長期Base/Chat・品質達成の証拠ではない。

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
| [documentation_update_20261003.json](phase6/documentation_update_20261003.json) | 今回の文書・残りの計画更新を別監査。旧report/実装/config/lock/eval不変、文書リンク・CLI・WSL同期・停止境界を確認 |

大型dataは`~/jmicro-data/phase6/{raw,expanded-v2}/`、CUDA checkpoints/log/source snapshotsはLinux checkoutの`reports/phase6/preparation-20261003/cuda/`。全jobは終了済みで③以降は停止中。Git clone/Hub bundleだけで拡張data/checkpointsが揃うとは扱わない。既存snapshotと完了reportは当時の証拠として保持し、現在の文書を過去snapshotへ書き戻さない。今後の実行順は[③以降の計画](../docs/27_phase6_remaining_plan.md)。
