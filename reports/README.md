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
