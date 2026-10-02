# Hugging Face経由での成果物共有

[japanese-data-analyze/japanese-tiny-llm-10m-artifacts](https://huggingface.co/datasets/japanese-data-analyze/japanese-tiny-llm-10m-artifacts)へpublicで公開済み。GitHubのコードリポジトリは非公開のまま、Tokenizerと前処理済みpilotを共有する。

## 確認済みの公開状態

2026-10-02に計27 files、約107MBを公開。Hub commitは`0b1042979bf32899e24da30790e3ae6b239013c3`。認証なしで全25 payload＋manifest/checksum台帳を取得し、サイズ・SHA-256を照合した。移行対象16 filesの復元も確認済み。[公開前の確認](20_publication_review.md)と[実施report](../reports/publication/review.json)を参照。

最初の約107MB候補は自動承認レビューで拒否された。その後、配布元の公開・利用条件と個人情報マスク・公開同意の根拠を照合し、ユーザーがdataset内部の既公開情報を公開対象として問題ないと確認した。新たに付加されたiMacのユーザーpathだけをTokenizerの公開コピーから除去し、更新済みbundleの公開が承認・実行された。元の研究artifactは変更していない。

## 公開内容

| 対象 | 内容 |
|---|---|
| `artifacts/phase2/{4096,8192}/` | model/vocab、special IDs、wrapper、更新したtraining metadata。各5 files |
| `data/phase1/processed/corpus.jsonl` | 採用22,998件の既公開Web本文・会話、固定split |
| `data/phase1/processed/dataset_manifest.parquet` | 採否を含む取得23,000件の出所・hash・canonical本文/会話 |
| `data/phase1/processed/tokenizer_sample.jsonl` | trainのみの共通sample、2,444文書 |
| split manifest・二つのreport | 固定split、旧runの入出力hash、統計 |
| config・Phase 2 report・sanitization report・license資料 | 出所・変更点・利用条件・Tokenizer検証 |
| `artifact_manifest.json`、`SHA256SUMS` | 公開fileのサイズ・SHA-256 |

raw archive、再学習候補、モデル重み、Mac binary、Python source、認証情報は含まない。source別の利用条件をLICENSEとrecordの出所metadataに保持している。公開済みの連絡先・自己紹介候補の検出と、新たな個人情報漏えいを混同しない。機械走査は完全な匿名性の証明ではない。

## Windows/WSL側の取得

private GitHub projectをclone/pullしたrootで:

```sh
uv sync --frozen --extra hub --extra data --extra ml --extra export
uv run --frozen --extra hub scripts/download_hub_artifacts.py
uv run --frozen --extra data --extra ml --extra export pytest -q
```

`hub` extraは`uv add --optional hub huggingface-hub==1.33.0`で管理する。Hub commitとmanifest SHA-256は`configs/hub/artifacts.json`へ固定済み。helperは匿名で全payloadを取得し、checksumを検証してからTokenizer 10 files・processed data 6 filesを元の相対pathへ復元する。READMEやlicense資料をproject rootへ上書きしない。

内容が違う既存fileがある場合は停止する。既に元のPhase 2 modelをコピー済みなら、旧artifactを別directoryへ退避し、公開版を新しい入力として配置する。`artifacts/phase2/`を無条件で削除しない。ダウンロード検証だけなら`--verify-only`を指定する。取得済みbundleはofflineでも確認できる:

```sh
uv run --frozen --extra hub scripts/download_hub_artifacts.py --source /path/to/bundle --verify-only
```

CLIのみで取得する場合もproject rootへREADMEを上書きせず別directoryを使う:

```sh
uv run --frozen --extra hub hf download japanese-data-analyze/japanese-tiny-llm-10m-artifacts --repo-type dataset --revision 0b1042979bf32899e24da30790e3ae6b239013c3 --local-dir artifacts/hub-handoff
uv run --frozen --extra hub scripts/download_hub_artifacts.py --source artifacts/hub-handoff
```

## Tokenizer hashと過去のexport

公開modelは`trainer_spec.model_prefix`だけを除去した。語彙・normalizer・token ID契約は同じだがbyte hashは異なる。公開版のhashはmanifestと更新済みtraining metadataを正とする。過去のPhase 2 reportは元modelの履歴として保存している。

- 4k公開model: `a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318`
- 8k公開model: `35b14c2bf6decb1fd843a6618178155a252af7cf750be305713454b3b7b5b44b`

旧random-weight HF/GGUFは旧Tokenizer hashにbindされている。公開コピーと組み合わせて再検証する時はそのTokenizerでexportし直す。本学習では実際に使う公開版hashをledgerへ記録する。generic AutoTokenizer/raw SentencePieceだけではprotected-byte ID契約が一致しないため、projectの`jmicro.tokenizer.Tokenizer`を使う。

本文・split・sampleのbyte hashは元pilotと同じ。split manifest内の旧lock hashは元runの履歴で、現在のlockで過去runの再生成が済んだという意味ではない。これは学習用shard生成やCUDA検証まで済んだデータではない。次は[Windows/WSL移行](windows_handoff.md)を進める。
