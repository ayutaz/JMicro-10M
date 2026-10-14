---
license: apache-2.0
language:
- ja
tags:
- text-generation
- experimental
- custom-code
- safetensors
pipeline_tag: text-generation
---

# Akebono-10M-chat — モデルカード草案

**公開前の配布候補です。自作モデル重み・tokenizer・自作コードの配布ライセンスはApache-2.0です。**

本人会話、Opus側、その他データ・コードの利用条件はユーザー確認済みです。追加調査は終了しました。配布ライセンスはユーザーがApache-2.0を選択しました。残るのは最終公開承認です。

表示名: **Akebono-10M-chat**。予定リポジトリ名: `hisakata-ai/akebono-10m-chat`。リポジトリは作成していません。
Hugging Faceへのアップロード、リポジトリ作成、公開は実施していません。

約10Mパラメータの実験的な日本語decoderモデルです。今回の比較で元v19を維持する判断がされました。完成した汎用会話AIや、総合最良モデルの認定ではありません。誤答、反復、履歴の取り違え、短い問いかけへの不適切な返答があります。

## 構造と保存形式

| 項目 | 値 |
|---|---:|
| パラメータ数 | 9,965,824 |
| SentencePiece語彙数 | 12,288 |
| hidden dimension | 256 |
| decoder layers | 8 |
| attention heads | 4 |
| feed-forward dimension | 768 |
| context上限 | 512 tokens |
| 正規化 / 位置表現 / 活性化 | RMSNorm / RoPE / SwiGLU |
| embedding / 出力射影 | 同じweightを使用 |
| 配布weight | FP32 `model.safetensors`、50テンソル |

独自のPyTorch実装です。Transformersの`AutoModel`・`from_pretrained`互換や、Hugging Face Inference API対応は提供していません。

元v19はNEW320の1巡目、50更新のcheckpointです。配布weightは元checkpointのmodel stateのみを損失なく変換しました。optimizer、RNG、訓練データ、元checkpointのpickleを配布ファイルへ含めていません。

元checkpointのSHA256（同定用）:
`2d9abf9fb9b5d773222f99ddcc83819d332582cf07ba456f9347f8e54a476b4b`

SentencePieceモデルから訓練入力パスとmodel prefixを除去しています。このため元tokenizerとはファイルSHA256が異なりますが、全12,288語彙のpiece・スコア、符号化、復号、試験した会話のtoken IDsは一致します。配布ファイルのSHA256は`SHA256SUMS`と`MANIFEST.json`に記録しています。

## ローカルCPUで使う

Python 3.11以上が必要です。以下は依存導入の手順で、配布準備作業では追加インストールを実施していません。

```sh
python -m venv .venv
# 作成した仮想環境を有効にしてから:
python -m pip install -r requirements.txt
python -B -X utf8 chat.py
```

Windowsでは依存導入済みのPythonをPATHに置くと`run_chat.bat`も使えます。別の作業ディレクトリからは、`python <package_directory>/chat.py`を実行してください。ファイルはスクリプトの所在を基準に読み込むため、起動時の作業ディレクトリに依存しません。

```sh
python -B -X utf8 chat.py --threads 2
python -B -X utf8 chat.py --model-dir ./another_local_bundle
```

`--threads`は1〜8、既定は2です。推論はCPU FP32に固定しており、GPU実行、サーバー、ネットワークアクセスは使いません。起動時にweight名とSHA256を表示します。

日本語を1行入力してEnterで送信します。

| 操作 | 内容 |
|---|---|
| `/status` | モデル識別、往復数、保存トークン数 |
| `/reset` | 履歴初期化 |
| `/help` | 操作説明 |
| `/quit` または `/exit` | 終了 |

履歴はこのプロセスのメモリにのみ保持し、終了時に消えます。APIとして使う場合は同じフォルダの`chat.py`にある`Chat`を読み込み、`Chat().send("こんにちは。")`、`reset()`、`status()`を呼べます。

## 会話形式と生成設定

system文:
`あなたは日本語で話すAIです。自然で簡潔に返答してください。`

会話は`BOS SYSTEM 文 END / USER 文 END ASSISTANT 回答 END`の形式です。特殊token IDsはPAD=0、UNK=1、BOS=2、EOS=3、SYSTEM=4、USER=5、ASSISTANT=6、END=7、NEWLINE=8です。

元デモと同じgreedy argmaxで、反復ペナルティ、token禁止、回答の書換えは追加していません。回答は最大128生成tokens、復号160文字目安です。END/EOSで終了し、文字数・context・token上限による途中停止は理由を表示します。

512tokensにはsystem・役割・入力・回答・履歴を含みます。回答用16tokensを確保し、長すぎる入力は履歴を変更せず拒否します。履歴を自動で削ったり切り捨てたりしません。回答は実際に生成したtoken IDsのまま履歴へ保持します。生成上限まで止まらない場合にも、定型文へ置き換えません。

## 学習データの由来（祖先checkpointを含む）

別担当の権利確認で、元v19は以下の由来を祖先の学習から継承していることが確認されました。この表は必要な出典と制約の要約です。全文データ、個人素材、教師ログ、未サニタイズの内部報告は収録していません。この配布準備で権利や法的適用を独立に再監査したものではありません。

| 由来 | v19との関係と、確認報告での条件表示 |
|---|---|
| [The SimpleStories Project / SimpleStories-JA](https://huggingface.co/datasets/SimpleStories/SimpleStories-JA) | 初期学習・replayの公開合成物語。取得版の表示はMIT。上流で生成された合成データを含みます。 |
| [LLM-jp / magpie-sft-v1.0](https://huggingface.co/datasets/llm-jp/magpie-sft-v1.0) | 散文学習・replay等の公開合成データ。取得版の表示はApache-2.0。dataset card作者はHirokazu Kiyomaru、Takashi Kodama。質問/回答はcalm3/Qwen系モデルで生成されています。 |
| [Wikipedia contributors / Wikimedia Japanese 20231101 snapshot](https://huggingface.co/datasets/wikimedia/wikipedia) | 祖先のcycle5学習へ含まれます。取得資料の表示はCC BY-SA 3.0/GFDL等で、一部はCCのみです。元資料の帰属と条件表示を保持します。データ利用条件はユーザー確認済みです。 |
| [Sanae Yamashitaほか / RealPersonaChat](https://github.com/nu-dialogue/real-persona-chat) | 祖先の学習に公開マスク済み会話を使用。条件表示はCC BY-SA 4.0。元著者の帰属と条件表示を保持します。データ利用条件はユーザー確認済みです。 |
| 保存済みのローカルQwen系教師出力 | 祖先C8の会話targetへ含まれます。教師weight/tokenizerの移植ではありません。教師出力を含むデータ利用条件はユーザー確認済みです。 |
| Codexセッションで作成・編集した架空会話/anchors | プロジェクトの会話targetにOpenAI出力を含みます。すべてを人間執筆の会話と表示しません。これらのデータ・コードの利用条件はユーザー確認済みです。 |
| 本人提供の私的会話とOpus由来と記録された返答 | v19の直接追加データだけでなく、祖先の学習に含まれます。原文・整理データ・個人識別情報は添付しません。今回のモデルへの本人会話利用とOpus側の利用条件はユーザー確認済みです。これは原会話自体を配布する許可へ拡張しません。 |

上流の条件を列挙することは、このweightや推論コードへ同じライセンスを付与することではありません。祖先の学習を継承しているため、訓練データを添付しないだけでその由来や条件が消えるとは扱いません。本人名、私的ファイル名、素材本文は帰属欄へ追加していません。原作者・機関による本モデルの推薦を意味しません。

SentencePieceソフトウェアのライセンスと、プロジェクトで学習した`tokenizer.model`へのライセンス付与は区別します。ユーザーの選択により、自作weight、学習済みtokenizer、自作推論コードにApache-2.0を付与します。データ・コードの利用条件確認はユーザー確認で終了しました。第三者資料・依存ライブラリの既存ライセンスと帰属表示を保持し、Apache-2.0へ上書きしません。

## 既存評価と制約

以下は選定時に親作業から報告された目的別比較の値です。今回の配布準備で再評価・再学習はしていません。

| 元v19の確認項目 | 報告値 |
|---|---:|
| 通常の全会話成立 | 3/40 |
| 長会話の全会話成立 | 0/12 |
| END終了 | 168/168 |

追加SFTのLOWE1/E2は正答改善がなく、通常全会話成立が1/40・2/40だったため、元v19維持が選ばれました。これらは限定された比較の記述値で、一般的な成功率や独立品質監査を示しません。ENDで止まることと、内容が正しいことは別です。確認済みの由来は上記に記載しています。要約の根拠範囲は`EVALUATION_SUMMARY.json`を参照してください。

長い文脈の保持、否定、日付や対象との結合、問いに応じた回答は信頼できる水準に達していません。学習素材の由来とユーザーによる利用条件確認は上記のとおりです。素材本文・個人識別情報は配布ファイルへ添付していません。

## 今回のCPU動作検証

50テンソルの値が元weightと完全一致し、元デモとの3生成について入力・raw/body token IDs、返答、停止理由、形式監査が一致しました。別フォルダへコピーし、別の作業ディレクトリから日本語会話・履歴・reset・終了を確認しました。長い入力の拒否、token/文字上限の停止経路も検証しました。

全3返答を選別せず記録した例:

1. `こんにちは。` → `こんにちは。今日は少し休もう。`
2. reset後、`猫が好き。` → `いつも見かける所？`
3. `何が好き？` → `猫が好き。`

すべてENDで終了しました。2番目の応答は的確とは言えず、動作一致は会話能力の実証ではありません。

検証環境はWindowsの既存Python環境、PyTorch `2.9.1+rocm7.2.1`、SentencePiece `0.2.2`、safetensors `0.8.0`です。GPUは初期化していません。プロジェクトのソースやデモを読み込まない配布コードで確認しましたが、依存は既存環境を使っており、空の環境への新規インストールや他OS・他CPUでの動作は未検証です。詳細は`VERIFICATION.json`を参照してください。

## ライセンスと公開前の確認

**ユーザーの選択により、自作モデル重み・tokenizer・自作コードの配布ライセンスをApache License 2.0（Apache-2.0）に設定しました。**

Copyright 2026 Akebono-10M-chat contributors.
Licensed under the Apache License, Version 2.0. You may obtain a copy in [`LICENSE`](LICENSE) or from the [Apache Software Foundation](https://www.apache.org/licenses/LICENSE-2.0.txt).

対象は`model.safetensors`、プロジェクトで学習した`tokenizer.model`、`modeling_japanesechat10m.py`、`tokenizer.py`、`output_integrity.py`、`chat.py`、および付随する自作設定・文書・起動補助です。`LICENSE`は公式全文をそのまま収録しています。第三者の既存表示・帰属・ライセンスには変更を加えず、第三者の資料や依存ライブラリへApache-2.0を付与するものではありません。

本人会話、Opus側、その他データ・コードの利用条件はユーザー確認済みで、追加調査は終了しています。学習元CC BY-SAの重みへの適用は独立に確認しておらず、ユーザーが条件確認済みという前提で配布候補を整えています。このライセンス設定は独立した法的保証ではありません。第三者資料の元の帰属・条件表示は保持します。

残るのは最終公開承認です。公開禁止の指示は継続しており、Hubへのアップロード、リポジトリ作成、認証、公開はしていません。原会話、整理データ、教師ログ、内部の権利報告は配布ファイルに含めていません。

`LICENSE_STATUS.md`に現在の選択と対象範囲を記録しています。`VERIFICATION.json`のCPU検証記録は保持し、ライセンス・公開状態・表示名のmetadataのみ更新しています。

## ファイル

- `model.safetensors`: model weightのみ
- `tokenizer.model`: ローカル訓練パスを除去したSentencePieceモデル
- `config.json`, `runtime.json`: モデル構造、会話/生成設定、weight/tokenizer SHA
- `modeling_japanesechat10m.py`, `tokenizer.py`, `output_integrity.py`, `chat.py`: 独自CPU推論実装
- `requirements.txt`, `run_chat.bat`: 依存一覧、Windows起動補助
- `EVALUATION_SUMMARY.json`, `VERIFICATION.json`: 既存報告値と配布動作検証
- `LICENSE`: Apache License 2.0の公式全文
- `README.md`, `LICENSE_STATUS.md`: モデルカード、現在のライセンス選択と対象範囲
- `MANIFEST.json`, `SHA256SUMS`: ファイル容量と整合性確認情報

`MANIFEST.json`は自身と`SHA256SUMS`を除くファイルを記録し、`SHA256SUMS`は自身を除くファイルを記録します。
