# 現在の研究と公開の状態

更新: 2026-10-18 JST。

最新のSFT試行は完了しましたが、一般会話の品質が低下したため不採用です。Base 3系列と最新SFTの重みは申請・ログイン不要で公開し、GitHubのコードはApache-2.0にしました。文書の更新・整理は完了し、現在の作業はJMicro-10Mへの名称統一と関連リンクの更新です。新しい学習や評価は開始していません。

## 最新SFTの結果

元の10B Baseから64教材を483更新、250,003 Assistant教師tokenで学習しました。教材の全文再現64/64、未知値30/32に対し、質問構造の変更15/32（二項目0/16）、実会話最終9/16でした。主SFTへ進む条件に届かず、追加の主比較は行っていません。

既存7組は全て内容成立が低下し、固定100ケースのタスク成立も直前の別SFTの19/100から3/100へ低下しました。教材構成・教師量も異なる歴史的比較です。全1,973応答をCodexで非blind判定しており、独立人手評価ではありません。[全結果165](165_chat_two_attribute_diagnosis_results.md)。

## 完了したことと残る課題

- モデル・Tokenizer・学習・保存再開・評価・ローカル画面の基盤、複数のBase/SFT比較、最新候補の全件判定は完了。
- GitHubをpublicへ変更し、Apache-2.0と読みやすいREADMEを反映。Hugging Faceの4モデルの匿名取得を確認。
- 実用的な一般会話、正式Base/Chat採用、親の事前学習からの独立した全工程再現、必要な実全文DEV/全440件・新封印TESTは未達。

10Mの限界や単独の失敗原因を証明した結果ではありません。現在の追加SFTを繰り返す根拠は弱く、既存の固定条件は終了しています。[残課題と再開条件](10_next_steps.md)。

## 保存と実行状態

最終checkpointはWSLの`reports/phase7/chat-two-attribute-20261018/model/checkpoint-00000483.pt`。SHA256は`44128809acccf45fbfddcd8863a72af5a029d43a660e10b06ed73e4157aff553`です。全model/Adam/RNG/samplerはWSLに保持し、公開保存版には重み・Tokenizer・native実装を収録しています。

最新SFTの科学process/Windows workerは正常終了し、2026-10-18 02:40 UTCの記録で元Base UIの復帰を確認しました。この日時付き記録は現在のprocess生存保証ではありません。起動や停止が必要なら[運用手順](windows_handoff.md)で実状態を照合します。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/JMicro-10M/blob/ed91c002cdfe52c879e275241c58436bfef3e394/docs/autonomous_status.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="ui保存先履歴"></a>
<a id="以下は過去時点の経過記録"></a>
<a id="前回chatの完了結果"></a>
<a id="完了したことと未確認"></a>
<a id="完了した検証"></a>
<a id="実行状態と保存"></a>
<a id="未達事項"></a>
<a id="次の判断と停止境界"></a>
<a id="現在の状態"></a>
<a id="現在の目標と次の行動"></a>
<a id="現在試せるchat"></a>
