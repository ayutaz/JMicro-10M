# データ領域

ここにはPhase 1以降の小sampleとmanifestを置く。本文・shardsはGit管理外。大規模データとcheckpointは学習PCの外部データ領域で管理し、configから場所を指定する。

`eval/`の固定評価例は学習用データへ混ぜない。raw/canonical hash、source/subset/revision、利用条件、duplicate cluster、splitを記録してから採用する。

## Phase 1 pilotの再生成

source台帳と取得・処理条件は[configs/data/pilot.json](../configs/data/pilot.json)、契約は[config schema](../schemas/configs/data/pilot.schema.json)と[record schema](../schemas/dataset_record.schema.json)。固定revisionの最初のWeb shardと会話archiveを取得する。Web全datasetを取得しない。会話はarchive内の全対話fileからseed 42で3,000件を選び、personaのmetadata fileは読まない。

```sh
uv sync --frozen --extra data
uv run --frozen --extra data scripts/prepare_phase1.py fetch
uv run --frozen --extra data scripts/prepare_phase1.py build
```

`fetch`だけがネットワークを使用する。取得上限はWeb 300,000,000 bytes、会話80,000,000 bytes。原fileと配布条件のSHA-256を検証し、完了した取得のreceiptを保存する。`build`と`verify`は原fileからofflineで実行できる。

| 保存先 | 内容 |
|---|---|
| `phase1/raw/` | 固定revision原file、README/LICENSE、`acquisition.json` |
| `phase1/processed/dataset_manifest.parquet` | 全取得recordの出所、hash、品質、採否、cluster、split、canonical本文・会話payload |
| `phase1/processed/corpus.jsonl` | 採用recordのみ。`kind`と`bucket`を保ち、Base/会話学習への選択は後続configで指定 |
| `phase1/processed/split_manifest.json` | split membership、code/config/lock/eval/input/output hash |
| `phase1/processed/tokenizer_sample.jsonl` | trainのみの文書集合・順序・本文。4k/8kに同じfileを使用 |
| `phase1/processed/data_pilot_report.json` | source/bucket/split/domain別件数・bytes、短文、除外・dedup結果 |
| `phase1/processed/dialogue_data_report.json` | 対話・turn・応答長・定型応答の頻度と役割方針 |

raw row hashは解析した原recordのsort-key JSON（UTF-8、compact形式）のSHA-256。原fileそのもののhashとsource locatorも保存する。canonical本文はPhase 0の弱い前処理を使用する。NFKC・casefold・空白まとめは**重複検出専用**で、学習本文へ適用しない。MinHashは日本語の文字5-gram、128 permutations、seed 42、32 bands × 4 rows。候補に対して実Jaccard 0.85以上を確認し、exact/nearの連結成分では代表1件を残す。同じURLや十分長い共有会話prefixはsplitを共有させるが、内容が違う文書は保持する。

品質確認は[記録した20件のレビュー](../reports/phase1/quality_review.json)のID・hashに対応する全文を確認する。再生成した同じpilotでレビュー記録を再利用する場合:

```sh
uv run --frozen --extra data python -c "import shutil; shutil.copyfile('reports/phase1/quality_review.json', 'data/phase1/processed/quality_review.json')"
uv run --frozen --extra data scripts/prepare_phase1.py verify
```

レビューはCodexによる内容確認で、独立した人手評価ではない。source/configを変えた場合は新しい内容レビューが必要。`verify --without-review`は処理確認用の途中検証で、完了証拠に使わない。検証では全23,000原recordの復元、採用本文・MinHash signatureの再計算、split/URL/prefixの越境、検出範囲内の評価混入、corpus payloadとTokenizer sampleを確認する。

処理を再実行して一致を確認する時は別directoryへ出力する。

```sh
uv run --frozen --extra data scripts/prepare_phase1.py build --output data/phase1/rebuild
```

`dataset_manifest.parquet`、`corpus.jsonl`、`split_manifest.json`、`tokenizer_sample.jsonl`、二つのdata reportの計6 fileをchecksumで比較する。rawと本文をGitへ追加せず、比較結果と小さなreportを`reports/phase1/`へ残す。

会話は窓へ分割する前に対話全体をsplitする。先頭話者をUser、他方をAssistantとして固定し、同じ話者の連続発話は改行で連結して原utterance IDを保持する。末尾Userの対話も原形を保持する。4k/8k token量・教師tokens・1024-token内の割合とwindow/maskは[Phase 2](../docs/18_phase2_completion.md)で計測・検証済み。元のPhase 1 reportの`null`は履歴として保持し、実計数は`reports/phase2/tokenizer_comparison.json`を参照する。

## 過去の検証と現在の依存lock

Phase 1のmanifestは作成時の`uv.lock` hashを固定している。Phase 2〜3で依存を追加したため、現在のlockで過去の`data/phase1/processed/`をそのまま`verify`すると`Processing input modified`になる。元の全件検証・再生成結果は[Phase 1監査](../reports/phase1/completion_audit.json)と当時のsource snapshotに対応し、更新で上書きしない。

現在のlockで新しい処理runを検証する場合は、`build --output data/phase1/rebuild-current`で別directoryへ作成し、同じ本文であることを確認してレビューをコピーした後、`verify --output data/phase1/rebuild-current`を使う。lockを含む入力台帳のhashは旧runと異なるものとして記録する。最初のWindows移行では既存の固定artifactをコピーしてhashを照合し、再取得・再処理を前提にしない。
