# 学習実装の確認事項

更新: 2026-10-18 JST。

数学・最大shape・全state再開の技術確認はモデル構成へ、OOMや費用閉鎖・品質失敗の経過は研究総覧へ統合しました。

詳しい説明は[統合先](03_architecture.md#学習と保存再開)と[関連する結果・手順](125_project_retrospective.md)を参照してください。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/japanese-tiny-llm-10m/blob/ed91c002cdfe52c879e275241c58436bfef3e394/docs/12_training_implementation_research.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="1-qk-normの仕様を固定する"></a>
<a id="2-kv-cacheとcausal-mask"></a>
<a id="3-初期化optimizerprecision"></a>
<a id="4-tokensだけでなくoptimizer更新回数を管理する"></a>
<a id="5-終点を延長できる学習率"></a>
<a id="6-10mでもlogitsは大きい"></a>
<a id="7-4090-benchmarkと時間見積もり"></a>
<a id="8-再開時の一致を成立させる"></a>
<a id="9-過学習とデータ反復"></a>
<a id="parameter-countの再計算"></a>
<a id="モデル実装段階学習実行環境の追加調査"></a>
<a id="当時の資料保存手順"></a>
<a id="設計手順の保存記録"></a>
