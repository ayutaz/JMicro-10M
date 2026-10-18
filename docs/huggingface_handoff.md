# Hugging Faceからの取得と復元

更新: 2026-10-18 JST。

モデルは[Base保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive)と[最新SFT保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-chat-research-20261018)で申請・ログイン不要です。最新SFTをCPUで試す手順は[README](../README.md#最新モデルをcpuで試す)へ統合しました。

## モデルと古いpilot bundleを区別する

モデル保存版は重み・Tokenizer・実装・評価記録の保存です。学習データ全体や元samplerの復元には使えません。Base保存版とSFT保存版はフォルダ構成も異なります。[保存範囲](126_model_archive.md)。

初期pilot/Tokenizerのdataset bundleは`japanese-data-analyze/japanese-tiny-llm-10m-artifacts`、固定revisionは`0b1042979bf32899e24da30790e3ae6b239013c3`です。後続10B corpusや最新SFT教材を含むものではありません。欠損時だけ[download helper](../scripts/download_hub_artifacts.py)と[固定設定](../configs/hub/artifacts.json)で復元します。

```sh
uv run --frozen --extra hub scripts/download_hub_artifacts.py --verify-only
```

既存の正しいファイルがある環境で再取得・Tokenizer再学習を繰り返しません。取得先をproject rootにしてREADMEを上書きしないでください。元payloadの検証・配置の詳細は更新前の手順を参照します。

## Tokenizerの互換性

固定4k model SHA256は`a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318`です。独自のprotected-byte契約を含むため、汎用AutoTokenizerだけで置き換えません。過去のrandom-weight exportのhashと、本学習で使った公開Tokenizerのhashを混同しないでください。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/JMicro-10M/blob/ed91c002cdfe52c879e275241c58436bfef3e394/docs/huggingface_handoff.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="hugging-face経由での成果物共有"></a>
<a id="tokenizer-hashと過去のexport"></a>
<a id="windowswsl側の取得"></a>
<a id="公開内容"></a>
<a id="当時の資料保存手順"></a>
<a id="確認済みの公開状態"></a>
<a id="設計手順の保存記録"></a>
