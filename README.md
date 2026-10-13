# JMicro-10M

約1,000万パラメータで、日本語の短い文章を自然に続け、その後に短い会話を行うモデルを目指す研究プロジェクトです。Tokenizer、モデル、学習・評価基盤をスクラッチで構築しました。**10Mの小ささを維持し、元の品質目標も維持します。**

2026-10-13 JST現在、Base/Chatは未完成・未採用です。前回の教材汎化比較は不採用で閉鎖しました。ユーザーの「6まで進めてください」により新しい意味構造の教材候補1件を比較し、3,646更新・1,899,557 Assistant教師の本学習と全state/消費列の監査を完了しました。全評価は13/21セットまで確認し、残り8セットと最終採否を継続中です。[実行記録137](docs/137_chat_semantic_diversity_execution.md)。

## 最新の結果と次の計画

同じ元10B親、native10,001,152 parameters、Tokenizer、学習seed、Assistant教師量scheduleで、旧教材D0とfirst-turn/直接回答を増やしたD1を比較しました。D0は一致する歴史checkpointを再利用し、D1は1,899,562 Assistant本文+EOT教師まで実学習しました。親と3保存点の新旧全14セット・3,066内容判断・固定NLL7点を確認しています。

| 最終品質 | D0 新 | D1 新 | D0 旧 | D1 旧 | 必要な条件 |
|---|---:|---:|---:|---:|---|
| 文法・関連性をともに満たす返答 | 16/80 | 12/80 | 18/80 | 15/80 | 各56/80以上 |
| 自分の返答を含む会話の最終文脈保持 | 5/24 | 3/24 | 4/24 | 1/24 | 各15/24以上 |

両条件とも不合格です。D1は自然停止と反復の基準を通りましたが、未知の質問への正答と条件保持が不足しました。判断はCodex非blindで、独立した人間の評価ではありません。比較の差と95%CIから改善は実証できず、10Mの容量限界やBaseだけが原因とも断定していません。

誤履歴回復は開始条件不成立で未実行・効果未確認。保持とsamplingも合格候補がなく未確認です。動的paddingは短期実測で約5.57倍高速でしたが、固定paddingとの数値一致基準に不合格のため採用していません。元10B WebUIの復帰は終了時に確認済みで、その記録は将来の生存保証ではありません。

現在の比較は、意味構造と自然な質問の多様性を広げた教材を最新D1と比較する候補1件です。同親・10M・教師量・学習条件を維持し、新DEVと既知2セットの全21評価・4,599判断、固定NLL7点、有資格候補だけの保持・sampling、結果報告と停止まで進めます。独立学習seed43、最終TEST、正式採用、量子化・公開は今回の範囲外です。以下の表と136は前回の確定結果で、新候補の結果ではありません。

- [最終結果136](docs/136_chat_generalization_results.md)：品質、失敗例、NLL、分岐、効率、完了監査。
- [最新の改善計画135](docs/135_chat_problem_solution_plan.md)：次の仮説、教材仕様、同条件比較、進行・停止条件。
- [現在の状態](docs/autonomous_status.md) / [ロードマップ](docs/15_project_roadmap.md) / [文書一覧](docs/README.md)。
- [Base復旧計画124](docs/124_base_recovery_plan.md)：Base復旧を選ぶ場合の別経路。Base完成で通知・停止。

## 成立した基盤と残る課題

追跡可能なデータ処理、日本語Tokenizer、10Mモデル、WSL/RTX4090での実学習、全学習状態の保存・再開、日本語を複数の観点で評価する経路を整えました。保存・再開やGPU実行の成功は、生成品質の完成とは別です。

Baseのteacher-decay2B比較はBPB1.1064→1.0903でも、一貫性3/80のまま、適切完結7→5/80で不採用でした。[Base結果123](docs/123_base_teacher_decay_2b_results.md)。元UI10B、別staged約10.6B、teacher-decay2B、後続SFTは異なる重みです。10B・2Bは学習量であり、モデルのパラメータ数ではありません。

直接SFT128は停止や文法を改善しましたが、内容・文脈は未達でした。その後の教材比較131、汎化比較133も不合格で閉じています。[最初のSFT結果129](docs/129_chat_first_sft_execution.md)、[前の教材比較132](docs/132_chat_improvement_execution.md)、[最新結果136](docs/136_chat_generalization_results.md)。独立学習seed43、人間blind、fullDEV、protectedTESTと正式採用は未確認です。

調査・失敗・採否は[全体記録125](docs/125_project_retrospective.md)、[固定revisionの詳細台帳](docs/retrospective/README.md)、[作り直す前の調査127](docs/127_rebuild_investigation.md)、[課題調査130](docs/130_chat_failure_improvement_investigation.md)に保存しています。旧READMEや運用文書の全文は[今回の履歴保存一覧](reports/investigation/documentation_plan_refresh_20261013/baseline.json)へ保全しました。

## 保存したモデル

[Hugging Faceの研究モデル保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive)に、主要3系列を公開しています。**ダウンロード申請は手動承認です。**

| 保存名 | 内容 |
|---|---|
| `web-10b` | 元のローカルWebUIで使う10B学習モデル |
| `staged-10p6b` | 文章品質が比較的良かった約10.6Bの研究系列 |
| `teacher-decay-2b` | 最後の教師量正規化weight decay比較の2Bモデル |

いずれもモデル規模は10Mです。10B・2Bは各系列の学習量を表し、パラメータ数ではありません。正確な入力量と教師量は個々のprovenanceに記録しています。

重み・Tokenizer・数値学習状態・実装・設定・評価要約・試行錯誤の記録を保存し、**データセットとsamplerは含めていません。** 全ファイルの照合と、3モデルの再ダウンロード確認は完了しています。[保存内容と読み込み手順](docs/126_model_archive.md)。

## ローカルで試す

既存のWindows/WSL環境では、[http://127.0.0.1:7860](http://127.0.0.1:7860)で文章の続きを試せます。元の10Bモデルを使用します。サーバーが停止している場合は、プロジェクトrootから次を実行します。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/start_webui.ps1
```

[WebUIの操作方法](docs/43_local_webui.md)。Git cloneだけでは学習済み重みは入りません。新しいPCでは、保存版のモデル取得と環境の復元が必要です。

## 開発環境

学習環境はWSL2・RTX4090・Linux disk、Pythonは3.12.7をuvで管理します。全Pythonコマンドを`uv run --frozen`から実行し、依存の変更には`uv add`を使います。

```sh
uv python install 3.12.7
uv sync --frozen --python 3.12.7 --extra hub --extra data --extra ml --extra export
```

復元先・チェックポイント・データの所在は[Windows/WSL引継ぎ](docs/windows_handoff.md)、実行時のルールは[AGENTS.md](AGENTS.md)を参照してください。元の重みや大容量データはGit外に保持しています。過去の失敗記録と凍結した実験条件は変更せず残します。
