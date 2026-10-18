# 対話データとTokenizer

更新: 2026-10-18 JST。

Assistant本文+EOT、教材の能力点検、構造tokenと本文の分離を、それぞれの主文書へ統合しました。

詳しい説明は[統合先](../data/README.md)と[関連する結果・手順](03_architecture.md#tokenizer)を参照してください。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/japanese-tiny-llm-10m/blob/ed91c002cdfe52c879e275241c58436bfef3e394/docs/13_tokenizer_dialogue_data_research.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="1-弱い正規化を設定で実現する"></a>
<a id="2-構造tokenは本文とは別に扱う"></a>
<a id="3-4k語彙はbyte-fallback込みで予算を考える"></a>
<a id="4-fineweb2-edu-japaneseの使い方を具体化する"></a>
<a id="5-日本語の重複判定とvalidation"></a>
<a id="6-短い雑談に使える会話データ"></a>
<a id="7-sftのloss停止データ反復"></a>
<a id="8-10m向けデータの能力密度と蒸留"></a>
<a id="pilot案"></a>
<a id="shardに追加すべき情報"></a>
<a id="tokenizer日本語会話データsftの追加調査"></a>
<a id="テンプレート案"></a>
<a id="当時の資料保存手順"></a>
<a id="未解決として残す項目"></a>
<a id="設計手順の保存記録"></a>
