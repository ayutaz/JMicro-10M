# 公開モデルの保存内容と入手方法

更新: 2026-10-18 JST。

Base 3系列と最新SFTをHugging Faceでpublic・ungatedにしています。アクセス申請もログインも不要です。2026-10-18に既存Base保存先のmanual gateを解除しました。

## 保存先

| モデル | リポジトリとフォルダ |
|---|---|
| 元Base | [Base保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive)の`models/web-10b` |
| source-order Base | 同保存版の`models/staged-10p6b` |
| teacher-decay Base | 同保存版の`models/teacher-decay-2b` |
| 最新二情報SFT | [SFT研究保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-chat-research-20261018)のルート |

全てnative10,001,152 parameters、語彙4096、context1024です。Base保存版の10B/10.6B/2Bは各系列の学習量であり、パラメータ数ではありません。最新SFTは一般会話の品質不採用です。

## 読み込みと保存範囲

最新SFTは`model.safetensors`、`jmicro_config.json`、`tokenizer/`、`src/`、`inspect_model.py`、出所・評価・hash一覧を含みます。[READMEのCPU実行手順](../README.md#最新モデルをcpuで試す)を使い、native loaderと専用Tokenizerを組み合わせてください。標準AutoModel/AutoTokenizer形式ではありません。

最新SFTに元checkpoint pickle、optimizer、RNG、sampler、学習データは含めていません。古いBase保存版には数値学習状態がありますが、data/samplerを含まないため元と厳密に同じ状態からの再開の代替ではありません。

## 公開の確認

最新SFTの128ファイル・41,732,706 bytesをHubのサイズとhashで照合し、全128ファイルを匿名で取得しました。Base 3系列も重み全体を匿名取得しhashを照合しています。詳細は[公開記録166](166_public_models_and_oss.md)です。

Baseの`archive_manifest.json`と`SHA256SUMS`は2026-10-09の保存revision `853d52d2323653331b610249912fbe25615615fc`に対応します。その後のREADME変更を元のhash一覧で検証しないでください。

コードのApache-2.0と、モデル重み・Tokenizer・外部データの利用条件は別です。公開設定の変更は、重み等への新たな一括ライセンス付与ではありません。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/japanese-tiny-llm-10m/blob/ed91c002cdfe52c879e275241c58436bfef3e394/docs/126_model_archive.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="保存する3系列"></a>
<a id="含めるものと含めないもの"></a>
<a id="将来確認するとき"></a>
<a id="当時の資料保存手順"></a>
<a id="研究モデルのhugging-face保存"></a>
<a id="確認方法"></a>
<a id="設計手順の保存記録"></a>
