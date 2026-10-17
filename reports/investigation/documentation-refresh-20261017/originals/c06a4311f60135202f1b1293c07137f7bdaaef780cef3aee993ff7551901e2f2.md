# Hugging Face経由での成果物共有

更新: 2026-10-14 JST。現在の依頼は全現行文書の最新化と今後の計画作成。Base/Chatは未完成・未採用。研究・教材準備・診断・生成評価・GPU学習は再開していない。

[最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md) / [次の計画145](145_post_rejection_next_plan.md) / [今回更新146](146_documentation_followup.md)。

2026-10-09の主要3Base系列の公開保存は126の当時の記録。後続SFTや文書長重み100Mは未公開。dataset/samplerを含まない公開保存はnative完全再開の代替ではない。最新localBase納品は1901564/fc1a3fcで、旧push許可を今回は引き継がない。pinned pilot/Tokenizerのrevision/hash・復元条件は維持する。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

元Base TEST20 promptと元Chat TEST20行は別のCPU解析問題を保存した。学習・GPU TEST採点に使っていないこととCPU未解析は別。将来の有資格最終確認にはreader分離と新しい封印TESTが必要。今回data/TESTを開封・再処理しない。

次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。

## 当時の資料・保存手順

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

本文・split・sampleのbyte hashは元pilotと同じ。split manifest内の旧lock hashは元runの履歴で、現在のlockで過去runの再生成が済んだという意味ではない。公開bundleにはshard/checkpointを含まない。WSLではこの固定payloadからPhase 4 shardを生成し、CUDA/BF16・保存再開・評価・速度を検証済み。[実機結果](21_phase4_completion.md)。復元済みPCで再取得やTokenizer再学習は不要。
