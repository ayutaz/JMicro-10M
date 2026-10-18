# 評価とモデル配布

更新: 2026-10-18 JST。

研究モデルの公開は完了しましたが、正式float採用・学習済み量子化品質・独立環境の最終確認は別の未達事項です。評価方法と公開手順へ説明を統合しました。

詳しい説明は[統合先](evaluation_protocol.md)と[関連する結果・手順](126_model_archive.md)を参照してください。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/japanese-tiny-llm-10m/blob/ed91c002cdfe52c879e275241c58436bfef3e394/docs/14_evaluation_deployment_research.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="1-bpbの定義と原文の固定"></a>
<a id="2-同一1024-tokensだけでは比較条件が揃わない"></a>
<a id="3-雑談評価を再現できる形にする"></a>
<a id="4-qk-normありの配布経路"></a>
<a id="5-ffn幅576640とk-quantの制約"></a>
<a id="6-約5mbと実際の配布容量"></a>
<a id="7-cpu応答時間と量子化品質の判定"></a>
<a id="当時の資料保存手順"></a>
<a id="本学習前のexport-gate"></a>
<a id="比較評価量子化ローカル推論の追加調査"></a>
<a id="独自unigramは変換だけで互換にならない"></a>
<a id="自動metricの契約案"></a>
<a id="設計手順の保存記録"></a>
