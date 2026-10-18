# 参考モデルとの比較と文献の扱い

更新: 2026-10-18 JST。

参考モデルAkebonoは、固定revision `74b3a1739e6d16883177c6021b3c03a7d517c7fb`の重みと配布コードを照合してCPU実行しています。実parameter数9,965,824、語彙12,288、context512です。

同じ既知20問で、公式128token条件と別driverの32token条件はともに内容成立5/20、最初のJMicro SFTは4/20、当時のJMicro C1は1/20でした。全80応答を確認し、Akebonoの2条件では実ID・本文・停止が同じでした。[結果152](152_answer_learning_diagnosis_results.md)。

固有Tokenizer、対話形式、学習履歴、system文、抑制IDが異なるため、一般的な優劣や、同じ32tokenが同じ日本語長だという結論にはしません。これは固定した少数質問の非blind比較で、最新JMicro SFTとの新しい同条件比較ではありません。

初期に調べた小型モデル一覧や論文の採否は、更新前の本文と[研究総覧](125_project_retrospective.md)へ保存しています。過去の公開時期・製品情報・外部モデルrevisionを、今回再調査した現在情報として再掲しません。10Mモデル全般の不可能や容量限界は証明していません。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/JMicro-10M/blob/ed91c002cdfe52c879e275241c58436bfef3e394/docs/09_prior_art_and_baselines.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="先行例とベースライン"></a>
<a id="参考研究"></a>
<a id="当時の資料保存手順"></a>
<a id="情報の扱い"></a>
<a id="日本語対応100m以下の公開生成モデル"></a>
<a id="海外10m級ベースライン"></a>
<a id="添付された25m--100m-llama系config"></a>
<a id="設計手順の保存記録"></a>
<a id="読み取り"></a>
