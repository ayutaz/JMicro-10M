# Tokenizerの仕様

更新: 2026-10-18 JST。

語彙4096、protected-byte処理、特殊ID、固定hashはモデル構成のTokenizer節へ統合しました。取得と互換性はHub手順で説明します。

詳しい説明は[統合先](03_architecture.md#tokenizer)と[関連する結果・手順](huggingface_handoff.md)を参照してください。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/JMicro-10M/blob/ed91c002cdfe52c879e275241c58436bfef3e394/docs/04_tokenizer.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="tokenizer設計"></a>
<a id="作成時点の資料契約"></a>
<a id="学習用sample"></a>
<a id="必須テスト"></a>
<a id="方針"></a>
<a id="正規化"></a>
<a id="比較する語彙"></a>
<a id="特殊token"></a>
<a id="設計手順の保存記録"></a>
