# 試行錯誤の詳細台帳

更新: 2026-10-14 JST。現在の依頼は全現行文書の最新化と今後の計画作成。Base/Chatは未完成・未採用。研究・教材準備・診断・生成評価・GPU学習は再開していない。

[最新Base結果144](../144_base_document_balance_results.md) / [前回Chat結果141](../141_chat_lr_comparison_results.md) / [次の計画145](../145_post_rejection_next_plan.md) / [今回更新146](../146_documentation_followup.md)。

固定台帳は生成した当時のGit revisionと実験集合を保持。living入口だけを最新Base144/前回Chat141/計画145へ接続し、fixed coverage/experiment_records/source SHAを現在へ書き換えない。原台帳以後の新しい100Mと未達/blockedを当時の集計へ混ぜない。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

元Base TEST20 promptと元Chat TEST20行は別のCPU解析問題を保存した。学習・GPU TEST採点に使っていないこととCPU未解析は別。将来の有資格最終確認にはreader分離と新しい封印TESTが必要。今回data/TESTを開封・再処理しない。

次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。

## 当時の資料・保存手順

入力Git revision: `2d48062f5e29f7cb4cc9a1eb4352aa304e44827c`。観測UTC: 2026-10-08T16:21:01.897114+00:00。

[全体の説明](../125_project_retrospective.md)から読むと経緯を追いやすい。以下は原記録のキーと値を確認するための詳細。

## 分野別の記録

- [基盤・Tokenizer・保存再開](01_foundations.md): 158 JSON記録
- [教材・供給・品質・量](02_material.md): 1,075 JSON記録
- [学習量・配合・学習順序](03_learning.md): 379 JSON記録
- [学習目的・最適化・正則化](04_objectives.md): 696 JSON記録
- [構成・反復計算・容量](05_architecture.md): 355 JSON記録
- [評価・生成・意味診断](06_evaluation.md): 1,099 JSON記録
- [実行管理・後続準備・その他](07_operations.md): 1,053 JSON記録

## 網羅範囲と保存

- [coverage.json](coverage.json): 対象件数・除外・限界。JSON全件を抽出か明示的除外で説明。
- [全Git保存file一覧](tracked_files.tsv): path、bytes、Git blob SHA1。snapshotやrawを含む。
- [機械可読の抽出値](experiment_records.json): 原キー・値・原SHA256。
- [抽出対象外一覧](exclusions.json): 大型/非object/原source snapshot等。無視・合格扱いではない。
- [原文書一覧](document_map.md): 初期調査から最新計画・全履歴への入口。
- [完了・採否の入口](decisions.md): 完了・review・総合判断の原status一覧。
- [保存テスト結果](verification_ledger.md)、[suite原属性JSON](test_results.json)。
- [WSL reportsのfile一覧](native_reports.tsv): 重み/metrics/rawを含むmetadata。bytesの合計はhardlink重複等を除いた占有量ではない。

この台帳は既存の保存記録の集約であり、新しい実験・再採点・独立監査ではない。記録数を独立実験数とせず、重複したGPU時間や教師数を総計しない。processの歴史的なrunning/next_actionを現在の稼働や開始指示と扱わない。

[保存内容の確認結果](../../reports/publication/documentation_archive_20261009.json)に、原報告のhash、全表示項目、ページ索引、新しいfileリンクの照合結果を記録している。

## 更新と再利用

この台帳は上記revision時点の記録を固定したもの。後続の[モデル公開126](../126_model_archive.md)とそのpublication reportは[文書一覧](../README.md)から参照する。元報告とこのsnapshotを上書きせず、追加の整理は別の保存先へ作成する。

作成スクリプトは[document_project_history.py](../../scripts/document_project_history.py)。全Pythonはuv管理3.12.7で実行する。例えばWSL上のproject rootから、新しい日付の保存先を指定する:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/document_project_history.py --repository /mnt/c/Users/AiHUB/Desktop/japanese-tiny-llm-10m --native-reports /home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports --output docs/retrospective-YYYYMMDD
```

`--output`はdocs直下の新しいdirectoryとする。既存のcoverage.jsonがあれば停止する。`--render-existing`は保存済みexperiment_records.jsonから分野別ページを再描画するための機能で、元の実験・corpus・重みを再実行/検証しない。大きな原報告と配列の全内容は抽出値だけで置き換えず、原記録を参照する。
