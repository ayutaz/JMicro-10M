# JMicro-10M

約1,000万パラメータの日本語言語モデルを、事前学習からチャット向けの追加学習まで調べた研究プロジェクトです。モデル本体、Tokenizer、学習・推論コード、評価結果を公開しています。

**現在のモデルは研究用です。短い定型課題は学習できますが、一般会話・訂正・継続会話の品質は実用水準に達していません。** 成功した例だけでなく、改善しなかった実験と実際の回答も残しています。

## モデルをダウンロードする

Hugging Faceで公開しています。アクセス申請・ログインは不要です。GitHubのcloneにモデルの重みや学習データは含まれません。

| 保存先 | 内容 |
|---|---|
| [Baseモデルの研究保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive) | 元の10B入力token、段階学習の約10.6B入力token、2B教師tokenの3系列 |
| [最新SFT研究モデル](https://huggingface.co/japanese-data-analyze/JMicro-10M-chat-research-20261018) | 64件の教材で追加学習した最終重み。評価・読み込みコード付き。一般会話の品質不採用 |

10Mはパラメータ数、10Bや2Bは各系列の学習量です。どちらの保存先もnative PyTorch形式で、Hugging Face Transformersの`AutoModelForCausalLM`へ直接読み込む形式ではありません。

## 最新モデルをCPUで試す

[Git](https://git-scm.com/)と[uv](https://docs.astral.sh/uv/)を用意して実行します。学習やGPUは不要です。

```sh
git clone https://github.com/ayutaz/JMicro-10M.git
cd JMicro-10M
uv python install 3.12.7
uv sync --frozen --python 3.12.7 --extra ml --extra hub
uv run --frozen --extra hub hf download japanese-data-analyze/JMicro-10M-chat-research-20261018 --local-dir artifacts/latest-chat
uv run --frozen --extra ml --extra hub python artifacts/latest-chat/inspect_model.py --prompt 'こんにちは。' --max-new-tokens 32
```

本文と停止理由をJSONで表示します。既定はgreedy・最大32tokenです。`--prompt`で質問を変更できます。短くしても、内容の正しさや会話の安定性は保証されません。

専用Tokenizerは改行や特殊文字を保つための処理を含みます。モデルと一緒に保存した`jmicro.tokenizer.Tokenizer`を使ってください。ブラウザー画面や従来のWSL環境で試す場合は[ローカルWebUI](docs/43_local_webui.md)と[環境の引継ぎ](docs/windows_handoff.md)を参照してください。

## どこまでできたか

2026年10月18日の最新SFTでは、元Baseから64件の教材を250,003 Assistant教師token、483更新で学習しました。

| 評価 | 結果 |
|---|---:|
| 学習教材の回答を全文再現 | 64/64 |
| 同じ質問形式で未知の値に回答 | 30/32 |
| 質問表現・配置を変えた回答 | 15/32（二項目回答は0/16） |
| 自分の過去の返答を含む会話の最終回答 | 9/16 |
| 固定した100ケースでのタスク成立 | 3/100（直前の別SFTモデルは19/100） |

限定課題の学習は成立しましたが、質問の言い換えへの転用が弱く、既存7組の評価でも内容成立が減りました。今回の候補は不採用です。同じ返答への固定、空応答、過去の情報を訂正できない問題が残っています。

上の結果はBF16/math・greedy最大32tokenでの固定DEV評価です。全1,973応答をCodexで非blind判定しており、独立した人手評価や一般利用全体の精度ではありません。旧モデルとの比較は教材と学習量が異なり、単独要因の因果実験ではありません。CPU FP32の試用と評価時の数値条件も異なります。

- [最新の学習条件と評価結果](docs/165_chat_two_attribute_diagnosis_results.md)
- [全1,973応答と判定理由のCSV](reports/phase7/chat-two-attribute-20261018/all1973_responses.csv)
- [一つ前のSFT比較と全3,466応答](docs/162_chat_input_structure_sft_results.md)
- [Base学習からの研究総覧](docs/125_project_retrospective.md)

## モデルの構成

| 項目 | 値 |
|---|---|
| パラメータ数 | 10,001,152 |
| Transformer層数 | 13 |
| hidden / FFN | 256 / 640 |
| Attention | GQA、4 query heads / 2 key-value heads |
| 語彙数 / context | 4,096 / 1,024 token |
| 実装 | PyTorch、専用SentencePiece Tokenizer |
| 元の学習環境 | WSL2 / RTX 4090 / Python 3.12.7 / uv |

## コードと研究記録を読む

文書の入口は[読む順序と主要文書](docs/README.md)、整理・統合・削除の記録は[全文書更新167](docs/167_current_state_and_documentation.md)です。

| 場所 | 内容 |
|---|---|
| [src/jmicro](src/jmicro) | モデル、Tokenizer、学習、推論、評価の実装 |
| [scripts](scripts)・[configs](configs) | 各実験の実行コードと条件 |
| [tests](tests) | 数式・保存再開・データ境界などの検証 |
| [docs](docs/README.md) | 実験の方針・結果・運用手順 |
| [reports](reports/README.md) | 保存した評価・監査記録。Git管理対象の記録を収録 |

過去の文書にある「実行中」「次に行う」は、その文書の日付時点の記録です。実験完了と品質改善を区別し、正式なBase品質認定・独立した全工程の再現・新しい封印TESTによる最終評価は未達として残しています。10Mモデル全般の限界を証明した結果ではありません。

コードを変更する場合は、[AGENTS.md](AGENTS.md)の運用ルールと関連する実験条件を確認してください。終了した実験の設定・結果を上書きせず、改善案は別の比較として残します。

## ライセンス

プロジェクトのコードは[Apache License 2.0](LICENSE)で公開しています。第三者コードの帰属と既存ライセンスは[NOTICE](NOTICE)および[src/jmicro/_vendor](src/jmicro/_vendor)を参照してください。

モデル重み・Tokenizer・外部データには、このコードライセンスを一括して適用していません。各保存先の説明と元データの条件を確認してください。リポジトリのpublic設定と、各成果物の利用許諾は別です。

<!-- Preserve links from historical documents. -->
<a id="前回のchat比較141"></a>
<a id="成立した基盤と残る課題"></a>
<a id="最新baseの結果"></a>
