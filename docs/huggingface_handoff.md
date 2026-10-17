# Hugging Face経由での成果物共有

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

2026-10-09の主要3Base系列のpublic/manual-gated保存は当時の記録。後続Chat/ScaleGrad/RDrop等の候補を公開した記録ではない。dataset/samplerを除く保存はnative厳密再開の代替ではない。固定pilot/Tokenizerのrevision/hashと欠損時復元手順を維持し、旧push許可を新しい公開の許可にしない。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## 設計・手順の保存記録

以下は作成時点の仕様・調査・復元手順。途中の「最新」「次は」「未実施」やPIDはその時点の記録で、現在の状態は本ページ冒頭と148を参照する。外部サービス/依存の最新仕様は今回再照会していない。

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

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="当時の資料保存手順"></a>
