# 実行環境と保存先

更新: 2026-10-18 JST。

Windows/WSL、Python/uv、データとcheckpointの場所、同期と復元の説明を引継ぎへ統合しました。

詳しい説明は[統合先](windows_handoff.md)と[関連する結果・手順](126_model_archive.md)を参照してください。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/JMicro-10M/blob/ed91c002cdfe52c879e275241c58436bfef3e394/docs/07_environment.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="benchmark済みと残る測定"></a>
<a id="imacから学習pcへ切り替える境界"></a>
<a id="ストレージ配置"></a>
<a id="事前tokenizeと実装済みshard"></a>
<a id="作成時点の資料契約"></a>
<a id="実機環境"></a>
<a id="実行環境とデータ配置"></a>
<a id="最大バッチの決め方"></a>
<a id="設計手順の保存記録"></a>
