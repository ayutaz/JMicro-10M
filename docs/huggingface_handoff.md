# Hugging Face経由での成果物共有

公開先は[japanese-data-analyze/japanese-tiny-llm-10m-artifacts](https://huggingface.co/datasets/japanese-data-analyze/japanese-tiny-llm-10m-artifacts)。GitHubのコードリポジトリは非公開のまま、固定成果物をpublic dataset repositoryで共有する。

## 現在の公開状態

2026-10-02時点で公開リポジトリを作成済み。公開用bundleはローカルの`artifacts/hub-publication/`に用意したが、約107MBの具体的なpayloadの公開について自動承認レビューが拒否したため、ファイルのアップロードは未実施。採用・不採用本文の混合データ、ライセンス条件、個人情報を含む可能性が理由として示された。ユーザーの具体的な公開承認を待つ。

`configs/hub/artifacts.json`の`revision`は未公開を表す`null`。公開後にHub commitを固定し、匿名ダウンロードのchecksum検証を終えてから移行用commandを有効にする。アップロード済みとして扱わない。

## 公開予定の内容

| 対象 | 内容 |
|---|---|
| `artifacts/phase2/{4096,8192}/` | model/vocab、special IDs、wrapper設定、training metadata。各5 file |
| `data/phase1/processed/corpus.jsonl` | 採用22,998件のWeb本文・会話、固定split |
| `data/phase1/processed/dataset_manifest.parquet` | 採否を含む取得23,000件の出所・hash・canonical本文/会話 |
| `data/phase1/processed/tokenizer_sample.jsonl` | trainのみの共通Tokenizer sample、2,444文書 |
| `data/phase1/processed/split_manifest.json`、二つのreport | split、旧runの入出力hash、統計 |
| config、Phase 2 report、README、license資料 | 固定source、Tokenizer検証、取得方法、出所・変更点・利用条件 |
| `artifact_manifest.json`、`SHA256SUMS` | 原fileのサイズ・SHA-256 |

payload 23 filesで106,968,939 bytes。manifestとchecksum台帳を加えて25 filesを公開予定。復元対象はTokenizer 10 filesとprocessed data 6 files。raw archive、再学習候補、モデル重み、Mac binary、Python source、認証情報はbundleに含めない。

FineWeb2 Edu JapaneseのWeb recordはODC-By 1.0のdatabase licenseとCommon Crawl条件を維持し、RealPersonaChat由来の会話はCC BY-SA 4.0として配布する。source別の条件・出所・変更点を`LICENSE.md`と各recordのmanifestに保持する。Tokenizer artifactの公開条件も同fileに記録する。コードのライセンス変更は行わない。

## 公開後のWindows/WSL側の取得

以下は**公開完了とrevision固定後**に実行する。private GitHub repositoryをcloneしたrootで:

```sh
uv sync --frozen --extra hub --extra data --extra ml --extra export
uv run --frozen --extra hub scripts/download_hub_artifacts.py
uv run --frozen --extra data --extra ml --extra export pytest -q
```

`hub` extraは`uv add --optional hub huggingface-hub==1.33.0`で管理する。Hub commitとmanifest hashを`configs/hub/artifacts.json`へ固定する。helperは全payloadのSHA-256/サイズを検証してから元の相対pathへ復元し、内容の違う既存artifactがあれば上書きせず停止する。READMEやlicense資料をproject rootへ上書きしない。公開fileの取得に認証は不要。

取得済みbundleをofflineで確認する場合:

```sh
uv run --frozen --extra hub scripts/download_hub_artifacts.py --source /path/to/bundle --verify-only
```

Tokenizerの利用にはprojectの`jmicro.tokenizer.Tokenizer`が必要。generic AutoTokenizer/raw SentencePieceのみでは保護byteのID契約が一致しない。split manifest内の旧lock hashは履歴であり、現在のlockで過去runの再生成が済んだことを意味しない。
