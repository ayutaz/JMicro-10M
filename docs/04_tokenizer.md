# Tokenizer設計

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

固定4096 Tokenizer、構造ID0〜7、保護byteのencode/decode契約を維持する。SHA256はa7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318。モデル比較は同Tokenizer/common-byte BPB。既存4k/8k比較・Phase3変換を繰り返さず、不正UTF8のraw bytesを保存する。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## 設計・手順の保存記録

以下は作成時点の仕様・調査・復元手順。途中の「最新」「次は」「未実施」やPIDはその時点の記録で、現在の状態は本ページ冒頭と148を参照する。外部サービス/依存の最新仕様は今回再照会していない。

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
