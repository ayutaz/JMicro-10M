# Tokenizer設計

更新: 2026-10-14 JST。[現在の状態](autonomous_status.md)、[最新結果141](141_chat_lr_comparison_results.md)、[ロードマップ](15_project_roadmap.md)が現在の判断の正本。研究・教材準備・診断・生成評価・学習は停止中。

現系列は固定4096語彙のSentencePiece Unigram + byte fallbackを使用。SHA256 `a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318`。8192版は初期比較として保全し、同bytes/BPBとモデル配分の条件を区別する。再学習・語彙追加・embedding resizeは不要。

特殊IDはPAD0/UNK1/BOS2/EOS3/System4/User5/Assistant6/EOT7。会話本文を個別encodeしrole/EOTは構造IDで挿入する。CRLF/CR→LFとNUL除去以外のUnicodeを保持し、改行・タブ・literal ▁・<の表現は共通wrapperの契約に従う。raw不正UTF8を表示修正で成功扱いにしない。

[Phase2契約](18_phase2_completion.md)・[固定config](../configs/tokenizer/contract.json)・[復元](huggingface_handoff.md)を参照。下は初期方針と当時の候補で、既に完了した学習の再実行指示ではない。

## 作成時点の資料・契約

## 方針

**確定**: 既存LLMのTokenizerは流用せず、日本語コーパスから学習する。Tokenizerアルゴリズム自体を新規発明する意味ではなく、SentencePieceを使って語彙・正規化・特殊tokenをプロジェクト専用に設計する。

**採用済み**: SentencePiece Unigram + byte fallback。

理由:

- 2024年の本人モデルで経験がある
- 未知文字をbyteへ退避でき、`<unk>`依存を抑えられる
- 日本語の文字・語・頻出接辞を柔軟に語彙化できる
- 4k/8kという小語彙で比較しやすい

## 比較する語彙

**実施済み**: 4,096と8,192を同じtrain-only sampleで学習した。品質勝者は未選定。

測定項目:

- chars/token、bytes/token
- 日本語1文あたりtoken数
- Web、Wikipedia、公的文書、会話、SNS調それぞれの圧縮率
- byte fallback率
- unknown token率
- 同一validation bytesでのBPB
- 1024 tokensに収まる実文字量

## 特殊token

**実装済み**: 学習時に以下をID 0〜7へ予約した。

```text
<|pad|>
<|unk|>
<|bos|>
<|eos|>
<|system|>
<|user|>
<|assistant|>
<|eot|>
```

Dialogue SFT開始時に語彙追加とembedding resizeを行わないためである。ID割当はconfigとテストで固定し、変更時はTokenizer artifactのmajor versionを上げる。

**提案（追加調査）**: role／EOTは`control_symbols`として予約し、本文encodeと分けてIDを挿入する。原文中の表記を単一tokenにする`user_defined_symbols`とは異なるため、文字列テンプレート全体を一括encodeしない。[具体的なID・正規化・語彙予算](13_tokenizer_dialogue_data_research.md)を参照する。

## 正規化

**提案**: 雑談で意味を持つ表現を壊さない弱い正規化にする。

実施候補:

- Unicode normalization方式を固定して記録
- NULL、不正制御文字、壊れたUTF-8の除去
- 異常な連続whitespaceの制御
- 改行方針の統一

原則として維持:

```text
ｗｗｗ
（笑）
……
！！！
～～
(´・ω・｀)
```

2024年モデルで使ったneologdn系の強い正規化は、そのまま再利用せず、会話表現への影響をcorpus sampleで評価する。

## 学習用sample

**提案**: Tokenizer学習用corpusは本学習データと同じdomain mixtureを反映する。高品質Webだけに偏らず、会話調、短文、固有名詞、数字、URL、絵文字、記号を含める。source別件数とbyte量をmanifestへ記録する。

## 必須テスト

- `decode(encode(text))`が意味と主要記号を保持する
- 全byte fallback tokenのround-trip
- テンプレートへ挿入した構造token IDが単一で固定され、本文中の同じ表記の扱いが仕様どおりである
- 特殊token IDが固定される
- 空文字、長い連続文字、絵文字、結合文字、異体字でcrashしない
- 4k/8kの比較reportを同じsample setから再生成できる
- Tokenizer model、設定、学習sample manifestのhashを保存する
