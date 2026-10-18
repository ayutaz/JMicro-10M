# 評価データと利用上の境界

更新: 2026-10-18 JST。

評価の現在の説明は[評価方法](../docs/evaluation_protocol.md)、最新の全件結果は[165](../docs/165_chat_two_attribute_diagnosis_results.md)へ統合しました。固定v1の[protocol](../configs/evaluation/protocol.json)は過去の契約として保持し、後続実験の生成長や抑制IDで書き換えません。

最新診断の240応答と回帰1,733応答は別の分母で、合計1,973応答を個別に確認しています。公開100ケースは、最終100回答と全200回答の集計を区別します。

TRAIN/DEV/TESTのfamily分離、専用DEV artifact、manifest、実履歴とraw bytesを保持します。旧Base TEST20 promptとChat TEST20行にはCPU解析履歴があるため、未開封とは呼べません。学習やGPU TEST採点には使っていませんが、正式な最終評価には新しい封印TESTが必要です。

今回の文書更新では評価データ本文の解析、新TEST作成、生成・再採点を行いません。ファイル名が存在することやCPU fixtureの合格を、実モデルの品質確認へ読み替えないでください。

[現在の状態](../docs/autonomous_status.md) / [最新SFT結果](../docs/165_chat_two_attribute_diagnosis_results.md) / [公開モデル](../docs/166_public_models_and_oss.md) / [文書一覧](../docs/README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/JMicro-10M/blob/ed91c002cdfe52c879e275241c58436bfef3e394/eval/README.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="v1固定入力の契約"></a>
<a id="固定評価データと現在の利用状況"></a>
<a id="更新前の本文契約当時の記録"></a>
<a id="未参照と利用済みを区別する"></a>
<a id="設計手順の保存記録"></a>
