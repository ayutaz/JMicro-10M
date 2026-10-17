# 試行錯誤の詳細台帳

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](../148_latest_base_and_documentation.md) / [現在の計画145](../145_post_rejection_next_plan.md) / [文書一覧](../README.md) / [全件カタログ](../document_catalog.md)。

固定台帳は入力revision2d48062f5e29f7cb4cc9a1eb4352aa304e44827cの集合を維持する。今回living入口だけを最新RDrop/計画145へ接続し、当時のcoverage/experiment_records/source SHAへ後続実験を混ぜない。最新までの追加概要は148と全体総覧125を参照する。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## 設計・手順の保存記録

以下は作成時点の仕様・調査・復元手順。途中の「最新」「次は」「未実施」やPIDはその時点の記録で、現在の状態は本ページ冒頭と148を参照する。外部サービス/依存の最新仕様は今回再照会していない。

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

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="当時の資料保存手順"></a>
