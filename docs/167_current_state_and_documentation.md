# 最新の研究状態と全文書の整理

更新: 2026-10-18 JST。

最新SFTの実行・全1,973応答の判定と品質不採用、Base 3系列/最新SFTの申請不要公開、GitHubのpublic化とApache-2.0を、現行文書へ反映しました。追加学習を繰り返す根拠は弱く、新しい研究は開始していません。

## 最新の結果

64教材の全文再現は64/64、未知値30/32、質問構造15/32（二項目0/16）、実会話最終9/16。固定100ケースのタスク成立は3/100で、旧混合教材SFTの19/100を下回りました。主SFT条件は非発動で、試行完了と品質採用を区別します。[原結果165](165_chat_two_attribute_diagnosis_results.md)。

重みは[Base保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive)と[最新SFT](https://huggingface.co/japanese-data-analyze/JMicro-10M-chat-research-20261018)で公開。全4モデルの匿名取得を確認済みです。コードのApache-2.0は、モデル重みや外部データへの新たな一括許諾ではありません。[公開の証拠166](166_public_models_and_oss.md)。

## 統合と削除

構成・Tokenizer・学習を03、データをdata/README、評価をevaluation_protocol、残課題と再開条件を10、環境と保存をwindows_handoff、モデル入手を126へまとめました。旧入口14文書は短い案内へ置き換え、外部からの旧見出しリンクを保持しています。初期の長い調査本文は更新前のGit revisionで読めます。

重複する文書更新報告142/146/148は現行treeから削除し、この更新記録へ統合しました。これらは2026-10-14/17の文書棚卸し・当時の最新結果を報告する文書で、今の状態を示すものではありません。元の報告・監査JSON、当時のGit本文・hash・件数は保持しています。削除前の全文はカタログの固定revisionリンクから取得できます。

## 全件の扱い

[全件カタログ](document_catalog.md)はGit管理のMarkdown/RST/TXT等、ライセンス、source snapshot、原文copyも含みます。現在の説明は本文とリンクを更新し、凍結した科学記録・原文・ライセンスはbyte一致を確認して保持します。現在のリンク検証と、過去snapshot内で当時の配置を前提とするリンクを区別します。

更新前は1,056文書。34の現行入口を点検し、新しい主文書167を追加、保守報告3文書を削除しています。更新前の全path/hash/分類は[baseline](../reports/investigation/documentation-refresh-20261018/baseline.json)、本文・リンク・不変記録・同期の照合は[監査結果](../reports/investigation/documentation-refresh-20261018/coverage_audit.json)へ記録します。

独立全工程、必要な実全文DEV/全440、新封印TEST、正式採用は未達として残しています。この文書作業で学習、生成、TEST準備、モデル差替えは行いません。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)
