# データ領域

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](../docs/148_latest_base_and_documentation.md) / [現在の計画145](../docs/145_post_rejection_next_plan.md) / [文書一覧](../docs/README.md) / [全件カタログ](../docs/document_catalog.md)。

accepted TRAINはWeb75%・textbook20%・story5%の既存poolを再利用。最新RDropの教師25Mは追加のuniqueデータ25Mではない。2回のdecoderでhardgold CE評価50M/整合対25Mとなる。入力・教師・source・bytes・EOS・digestの元streamを対照と照合した。dataset/samplerの実体はWSLに保全する。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## 設計・手順の保存記録

以下は作成時点の仕様・調査・復元手順。途中の「最新」「次は」「未実施」やPIDはその時点の記録で、現在の状態は本ページ冒頭と148を参照する。外部サービス/依存の最新仕様は今回再照会していない。

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

## Phase 4の実装済みshard

入力は公開`corpus.jsonl`と公開Tokenizer。入口は`scripts/train.py build-shards`、実装は`src/jmicro/shards.py`。WSLの`~/jmicro-data/shards/{t8k-pilot,t4k-pilot}`へ各split一本のlittle-endian uint16 bin、index/token-byte JSON、hash付きmanifestを保存した。T8K train 6,884,183 / dev 345,044 / test 408,733 stream tokens、T4Kは8,398,329 / 420,053 / 497,374。同じ文書とbody bytesで、BOS/EOSはstream countに含む。

固定長blockを文書を跨いでpackし、BOS targetsをmaskする。最終の不完全train blockを落とす。samplerはseed/epoch/block位置とRNGを保存し、再開で同じ消費列を復元する。このpilot段階では複数file/source mixtureへの拡張は未実装だった。rawがなくても固定processed payloadとhashからshardを生成できる。[再開時の制約](../docs/windows_handoff.md#明示的な実行再開後の順序)

## Phase 6拡張corpusと全件監査

採用sourceはFineWeb2 Edu Japanese / `small_tokens_cleaned`、revision `180ca004c6a89b590daaad86cb062a07a5353c69`。固定8 files、実raw 2,152,539,810 bytes、Web 100%。[source台帳](../reports/phase6/sources.json)、[取得receipt](../reports/phase6/acquisition.json)、[凍結条件](../configs/phase6/preparation.json)、[完了証拠](../docs/26_phase6_preparation_completion.md)。

| split | 文書数 | stream tokens（BOS/EOS込み） | body tokens | body bytes |
|---|---:|---:|---:|---:|
| train | 1,604,292 | 756,087,912 | 752,879,328 | 2,946,200,160 |
| dev | 89,416 | 42,182,766 | 42,003,934 | 164,344,743 |
| test | 89,485 | 42,230,751 | 42,051,781 | 164,539,509 |

WSL `~/jmicro-data/phase6/raw/`にParquet/条件資料/receipt、`expanded-v2/`に`corpus.jsonl`、`records.sqlite`、`signatures.bin`、`manifest.json`、`corpus_audit.json`を保存する。`expanded-v2/shards/`にはsplit別uint16 `.bin`、`.index.json`、`token_bytes.json`、shard manifestがある。公開T4K model SHA-256は`a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318`。本文・DB・raw・shardsはGit管理外で、[corpus manifest](../reports/phase6/corpus_manifest.json)と[全件監査](../reports/phase6/corpus_audit.json)へbindする。manifestの`built_not_audited`は作成時ラベルのまま保存し、監査成功は別reportを正とする。

全1,803,712 raw recordsを独立復元し、全signature、検出されたnear/URL edges・connected components、split分離、全retained 1,783,193文書の本文・token/index・文字往復を確認した。NFKC/casefold/空白まとめは重複検出専用で、学習本文には適用しない。pilot全Web splitと固定suiteの検出された混入clusterを除外した。LSH候補のrecallは確率的で、意味的な全重複/汚染排除は保証しない。testは構造監査のみでモデル評価・選定未使用。24 train文書の先頭最大420文字の内容確認は、網羅的な人手品質採点ではない。

現在の756Mは最初の500M開始用で、10Bでは約13.23回露出する。追加corpusを作る時は現在のPhase 6 dev/testの保護・provenanceを実装してから取得上限と新runを固定する。現builderの保護入力はPhase 1 pilotであり、追加構築時にPhase 6 heldoutが自動継承される機能は未実装。通常resumeでdata hashを変更しない。[残る計画](../docs/27_phase6_remaining_plan.md)

既存reportを保持して準備の読み取り監査を行う場合は、WSL checkoutから**別出力**を指定する:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/audit_phase6_preparation.py --data /home/aihub_ubuntu/jmicro-data/phase6/expanded-v2 --run reports/phase6/preparation-20261003 --windows-root /mnt/c/Users/AiHUB/Desktop/japanese-tiny-llm-10m --output reports/local/phase6-preparation-reaudit.json
```

この監査は学習を起動しない。全corpus再構築監査用の`scripts/audit_phase6_data.py`はoutput内の監査reportを更新するため、保存済み①②の証拠を上書きする目的で再実行しない。取得/buildの再実行も通常の再開では不要。

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="当時の資料保存手順"></a>
