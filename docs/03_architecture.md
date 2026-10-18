# モデル構成と学習方式

更新: 2026-10-18 JST。

JMicro-10Mは独自Tokenizerを使う日本語のdecoder-only Transformerです。最新Base/SFTの参照構成は10,001,152 parametersで、一般会話の品質は未達です。

## 構成

| 項目 | 固定した参照値 |
|---|---|
| 層数 / hidden / FFN | 13 / 256 / 640 |
| query / key-value heads | 4 / 2、head dimension 64 |
| 語彙 / context | 4096 / 1024 token |
| FFN / 正規化 | SwiGLU / RMSNorm、QK-Normなし |
| RoPE | half-split、theta 10000 |
| embedding / output | weight tying |
| 推論dropout | 0 |

実装は[src/jmicro/model.py](../src/jmicro/model.py)。共有重みにより、119 unique parameter tensorsに対してstate辞書には120 entriesがあります。公開safetensorsは共有outputの重複保存を省き、native loaderで結び直します。

## Tokenizer

語彙4096のSentencePiece unigramとprotected-byte処理を併用します。改行・タブ・文字`▁`・`<`を保護して、本文の文字と構造tokenを区別します。

| ID | 構造 |
|---|---|
| 0 / 1 / 2 / 3 | PAD / UNK / BOS / EOS |
| 4 / 5 / 6 / 7 | System / User / Assistant / EOT |

Tokenizer SHA256は`a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318`。`jmicro.tokenizer.Tokenizer`を使い、raw SentencePieceや汎用AutoTokenizerだけで置き換えません。

## 学習と保存再開

Baseは本文の次token予測、Chat SFTはAssistant本文とEOTを教師とします。直前までのUser/Assistant履歴は入力であり、最新SFTでは最後のAssistantだけを教師にしています。教師を途中で切断せず、入力・教師・paddingの量を分けて記録します。

最新の64教材診断は元Base/fresh optimizer、seed42、LR1e-4、BF16/math、32×1024で483更新・250,003教師。正確な条件は[固定契約164](164_chat_two_attribute_diagnosis_execution.md)、結果は[165](165_chat_two_attribute_diagnosis_results.md)です。この終了済み条件を延長する計画はありません。

長い実験の前に最大shapeの有限逆伝播、連続実行と保存再開の全state一致、実測費用を確認します。保存はcompleted updateで行い、model、optimizer、scheduler、RNG、sampler、消費量、履歴を保持します。技術合格と品質合格は別です。[データ](../data/README.md) / [評価](evaluation_protocol.md)。

## 実装上の不変条件

日本語Base/短いChatの目標と約10Mの要件（9.5M〜10.1M）を維持します。勝手な大型化、Tokenizer/精度/decoder/親/教師量の変更、品質条件の緩和で失敗を救済しません。新しい構成変更は別の根拠・対照・契約が必要です。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/JMicro-10M/blob/ed91c002cdfe52c879e275241c58436bfef3e394/docs/03_architecture.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="attention"></a>
<a id="ffn"></a>
<a id="layer-sharing版"></a>
<a id="アーキテクチャ設計"></a>
<a id="作成時点の資料契約"></a>
<a id="初期baseline-jmicro-10m-t8k"></a>
<a id="後半候補"></a>
<a id="比較-jmicro-10m-t4k"></a>
<a id="現在の固定参照"></a>
<a id="設計手順の保存記録"></a>
