# JMicro-10M

約1,000万パラメータで、日本語の短い文章を自然に続けられるモデルを目指した研究プロジェクトです。Tokenizerからモデル、学習・評価の仕組みまでスクラッチで構築しました。**10Mの小ささを維持すること**を大切にしています。

元のBaseを会話データで3周追加学習し、学習前後の動作確認まで完了しました。**短い日本語・停止・反復は改善しましたが、関連性と複数ターンの文脈保持は基準未達で、この条件を不合格として終了しています。** Base/Chatは未採用、追加学習は停止中です。[結果129](docs/129_chat_first_sft_execution.md)。

これまでの成果と失敗は、将来の改善検討に使えるよう保存しています。

- [調査・検証・学習の全体記録](docs/125_project_retrospective.md)：何を試し、何が改善し、何が解決しなかったか。
- [作り直す前の調査](docs/127_rebuild_investigation.md)：Akebono-10M-chatとの比較、前回の失敗原因と未確定事項、再構築の順序。
- [SFT後の問題点と改善方法](docs/130_chat_failure_improvement_investigation.md)：流暢でも答えが合わない原因候補、教材・履歴・実装の確認、公開研究、改善の優先順位。追加学習は未開始。
- [課題への対策と段階計画](docs/131_chat_improvement_execution_plan.md)：教材の2条件比較、同教師量の学習、未使用評価、合格・停止条件、後続の履歴回復と効率改善。今回は計画作成まで。
- [現在のBaseをChat学習して検証する計画](docs/128_chat_first_sft_plan.md)：元10Bから直接SFTを最大3周、学習前後の会話・自生成履歴・Base保持を比較する。[再開後の実行・評価記録](docs/129_chat_first_sft_execution.md)。
- [詳細な実験台帳](docs/retrospective/README.md)：保存済み報告の数値・設定・失敗・採否と原記録へのリンク。
- [現在の状態](docs/autonomous_status.md) / [文書一覧](docs/README.md)。

## できたことと、残った課題

追跡可能なデータ処理、日本語Tokenizer、10,001,152パラメータのモデル、WSL・RTX4090での学習、学習状態の保存・再開、日本語を複数の観点から評価する仕組みを整えました。

教材の配合などで停止や反復が改善した条件もありました。一方、予測損失が下がっても、読みやすい文章になるとは限りませんでした。最新の同条件2B比較は次の結果です。生成評価は各80件、Codexによる非blind採点です。

| 指標 | 対照 | 改善候補 |
|---|---:|---:|
| BPB：次の文字列の予測損失。低いほど良い | 1.1064 | 1.0903 |
| 内容に一貫性がある | 3 / 80 | 3 / 80 |
| 適切に完結する | 7 / 80 | 5 / 80 |
| 反復が発生する | 27 / 80 | 27 / 80 |

この候補は不採用です。別の約10.6B学習系列では一貫性23/80・適切完結26/80まで達しましたが、そちらも採用基準には届いていません。最新候補、過去の比較的良かった系列、元WebUIのモデルはそれぞれ別の重みです。[最新結果の詳細](docs/123_base_teacher_decay_2b_results.md)。

現状から「10Mではこれ以上改善できない」とは断定できません。元10Bからの直接SFTでは次の改善が得られました。学習前後を同じChat形式で比較した結果で、上の2B Base比較とは別の実験です。

| Chat形式の評価 | 学習前 | 3周SFT後 |
|---|---:|---:|
| 文法と関連性をともに満たす返答 | 0 / 80 | 17 / 80（必要56） |
| 自然に停止する返答 | 4 / 80 | 77 / 80（必要76） |
| 反復する返答 | 56 / 80 | 4 / 80 |
| 自分の返答を含む複数ターンで文脈を保持 | 0 / 24 | 2 / 24（必要15） |

4保存点の全876返答をCodex非blindで確認しました。単に流暢に止まることと、訂正・否定・条件を守って返すことには差が残ります。全候補が不合格のため、事前計画どおり追加のsampling・Base保持・候補との手動5会話は省略しました。[計画128](docs/128_chat_first_sft_plan.md)、[実行・全結果129](docs/129_chat_first_sft_execution.md)、[完了監査](reports/phase7/chat-first-sft-20261010/completion.json)。追加実験や量子化へ進まず停止し、Base復旧の[条件付き計画](docs/124_base_recovery_plan.md)も保持します。

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
