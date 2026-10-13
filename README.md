# JMicro-10M

約1,000万パラメータで、日本語の短い文章を自然に続け、その後に短い会話を行うモデルを目指す研究プロジェクトです。Tokenizer、モデル、学習・評価基盤をスクラッチで構築しました。**10Mの小ささを維持し、元の品質目標も維持します。**

2026-10-14 JST 現行: 低学習率3e-5候補の学習・全28セット/6,132判断/NLL7点・全state/採否/予算監査と条件分岐を完了し、不合格・不採用と判定しました。最終新DEV内容20/80・自己文脈5/24、新内容差+8.75ポイント（95%CI −1.25〜+18.75）で、基準未達です。独立確認は有資格候補なしで未実行・品質未確認。文書整合・保全・ローカルcommit/納品監査が残りgoalは継続中で、追加研究・学習は開始しません。[結果141](docs/141_chat_lr_comparison_results.md)、[計画139](docs/139_chat_lr_comparison_plan.md)、[実行140](docs/140_chat_lr_comparison_execution.md)。以下は前回の終了結果です。

2026-10-13 JST現在、Base/Chatは未完成・未採用です。意味構造と自然な質問を広げた教材候補1件の比較を、全21セット・4,599内容判断・固定NLL7点まで完了しました。候補は不合格・不採用で閉鎖し、追加研究・学習は停止しています。[最終結果138](docs/138_chat_semantic_diversity_results.md)。

## 最新の結果と次の計画

最新D1を対照S0として歴史checkpointを再利用し、新教材S1を同じ元10B親から学習しました。native10,001,152 parameters、Tokenizer、seed42、教師量と学習条件を維持し、S1は3,646更新・1,899,557 Assistant本文+EOT教師で終了しました。全保存点の学習状態・実教師列・最終採否と予算の監査も完了しています。

| 最終品質 | S0 新 | S1 新 | S0 前回 | S1 前回 | S0 元旧 | S1 元旧 | 必要な条件 |
|---|---:|---:|---:|---:|---:|---:|---|
| 文法・関連性をともに満たす返答 /80 | 16 | 19 | 12 | 21 | 15 | 11 | 各56以上 |
| 自分の返答を含む会話の最終文脈保持 /24 | 3 | 3 | 3 | 6 | 1 | 1 | 各15以上 |

新DEVの内容差は+3.75ポイント、95%CI −8.75〜+16.25で、登録した改善条件も未達です。新候補のTRAIN標本NLLは0.008183まで下がりましたが、新DEVへの応答能力は不足しています。新自己生成反復と元旧固定反復も増え、元旧で不正UTF8が1件ありました。判断はCodex非blindで、独立人間の評価ではありません。Base単独原因や10M容量限界は確定していません。

保持・samplingは合格候補がないため未実行・品質未確認です。今回の6段階の比較と報告を終えて停止し、追加教材・LR探索・別seedへ自動移行しません。次の方針は計画135末尾の提案を参照してください。Base復旧を選ぶ場合は124の原品質条件を維持し、証拠を満たすBaseで通知・停止します。

- [最終結果138](docs/138_chat_semantic_diversity_results.md)：品質、全保存点、失敗、NLL、分岐、GPU予算と監査。
- [計画135と次の判断](docs/135_chat_problem_solution_plan.md) / [時点別実行137](docs/137_chat_semantic_diversity_execution.md)。
- [現在の状態](docs/autonomous_status.md) / [ロードマップ](docs/15_project_roadmap.md) / [文書一覧](docs/README.md)。
- [Base復旧計画124](docs/124_base_recovery_plan.md)：未再開の別経路。

## 成立した基盤と残る課題

追跡可能なデータ処理、日本語Tokenizer、10Mモデル、WSL/RTX4090での実学習、全学習状態の保存・再開、日本語を複数の観点で評価する経路を整えました。保存・再開やGPU実行の成功は、生成品質の完成とは別です。

Baseのteacher-decay2B比較はBPB1.1064→1.0903でも、一貫性3/80のまま、適切完結7→5/80で不採用でした。[Base結果123](docs/123_base_teacher_decay_2b_results.md)。元UI10B、別staged約10.6B、teacher-decay2B、後続SFTは異なる重みです。10B・2Bは学習量であり、モデルのパラメータ数ではありません。

直接SFT128は停止や文法を改善しましたが、内容・文脈は未達でした。その後の教材比較131、汎化比較133、意味多様性比較135も不合格で閉じています。[最初のSFT結果129](docs/129_chat_first_sft_execution.md)、[前の教材比較132](docs/132_chat_improvement_execution.md)、[前回結果136](docs/136_chat_generalization_results.md)、[最新結果138](docs/138_chat_semantic_diversity_results.md)。独立学習seed43、人間blind、fullDEV、protectedTESTと正式採用は未確認です。

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
