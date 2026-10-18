# 結果と監査記録の入口

更新: 2026-10-18 JST。

最新の結果は`phase7/chat-two-attribute-20261018/`、公開確認は`publication/chat-sft-public-20261018-v2/`です。大容量checkpoint・optimizer・RNG・samplerはWSLに保全し、Gitには選んだ小記録・全回答・判定理由を収録しています。

| 記録 | 内容 |
|---|---|
| [最新SFT completion](phase7/chat-two-attribute-20261018/completion.json) | 5工程の完了と品質不採用を区別した要件照合 |
| [final_analysis](phase7/chat-two-attribute-20261018/final_analysis.json) | 診断240・回帰1,733・全1,973応答の集計と採否 |
| [全回答CSV](phase7/chat-two-attribute-20261018/all1973_responses.csv) | 実履歴・raw・停止・判定理由 |
| [一つ前の比較](phase7/chat-recovery-20261018/input-structure-main/completion.json) | 入力配置SFTの実行・全3,466主応答・不採用 |
| [SFT公開](publication/chat-sft-public-20261018-v2/SFT_public.json) | 128ファイルのHub hash照合と匿名重み取得 |
| [Base公開](publication/chat-sft-public-20261018-v2/Base_public.json) | 3系列の匿名重み取得・manual gate解除 |
| [GitHub公開](publication/repository-public-20261018.json) | public・Apache-2.0・匿名README/Git確認 |
| [今回の文書棚卸し](investigation/documentation-refresh-20261018/baseline.json) | 全元文書のpath/hash/分類と開始revision |

過去の完了report、source snapshot、失敗、台帳は日付時点の証拠です。現在の結果で過去の採否やhashを上書きせず、当時の相対リンクは元revisionの配置で読みます。文書更新の監査合格はモデルの品質合格ではありません。

[現在の状態](../docs/autonomous_status.md) / [最新SFT結果](../docs/165_chat_two_attribute_diagnosis_results.md) / [公開モデル](../docs/166_public_models_and_oss.md) / [文書一覧](../docs/README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/JMicro-10M/blob/ed91c002cdfe52c879e275241c58436bfef3e394/reports/README.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="500m後の反復eosデータ構成の調査"></a>
<a id="phase-4の実機証拠"></a>
<a id="phase-5の実学習比較証拠"></a>
<a id="phase-6①②の完了証拠と文書更新"></a>
<a id="phase-6③の高速化容量再開証拠"></a>
<a id="phase-6④⑤の検証設定凍結と停止"></a>
<a id="モデル保存公開2026-10-09"></a>
<a id="主系列基盤の保存結果履歴"></a>
<a id="保存結果の履歴2026-10-05"></a>
<a id="実験台帳と検証結果"></a>
<a id="拡張trainの500m学習評価"></a>
<a id="更新前の本文契約当時の記録"></a>
<a id="最新139の保存記録"></a>
<a id="設計手順の保存記録"></a>
<a id="過去の記録の読み方"></a>
