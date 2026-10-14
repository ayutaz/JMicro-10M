# JMicro-10M

約1,000万パラメータで、日本語の短い文章を自然に続け、その後に短い会話を行うモデルを目指す研究プロジェクトです。Tokenizer・モデル・学習評価基盤をスクラッチで構築し、10Mの小ささと元の品質目標を維持します。

2026-10-15最新結果: [cross-GQA signed-map100M比較](reports/phase6/cross-gqa-map-science-20261015/completion.json)は学習・保存状態照合・生成80件の個別内容確認まで完了し、不採用になりました。文法合格は対照44→60/80ですが、一貫性2→2、適切完結2→2、EOS停止19→18、反復45→47で品質基準を満たしていません。元モデルは10,001,152、候補は52個の係数を追加した10,001,204パラメータです。元10B WebUIは復帰を確認しました。次は別の根拠ある同10M比較を選定します。独立学習・全文DEV・全440生成・新しい最終TEST・Base採用は未完了です。以下の進行中記述は起動時点の履歴です。

2026-10-15進行中: [cross-GQA signed-map100M比較](configs/phase6/cross_gqa_map_science_20261015.json)を開始しました。元10,001,152パラメータを参照し、追加52個の係数を持つ10,001,204パラメータの別構造案を、元のデータ・教師予算・品質基準で検証します。GPU保存再開とメモリ・速度の技術検証は通りましたが、生成品質は未判定です。独立学習・全文DEV・最終TEST・Base採用は未完了です。

2026-10-15最新結果: [TRAIN全句copyの確率減衰100M比較](reports/phase6/pseudo-repetition-science-20261015/completion.json)は学習・全状態照合・生成80件の個別内容確認まで完了し、不採用になりました。反復は対照45→31/80に減りましたが、一貫性2/80、適切完結3/80、EOS22/80で原基準未達です。次は別の根拠ある同10M介入を選定します。独立学習・全文DEV・最終TEST・Base採用は未完了で、元10B WebUIを復帰しています。以下の「進行中」は起動時点の記録です。

2026-10-15進行中: [TRAIN全句copyの確率減衰100M比較](configs/phase6/pseudo_repetition_science_20261015.json)を、元の10Mモデル・教師列と品質基準を維持して開始しました。保存再開・有限gradient・メモリと速度の技術検証は完了しましたが、生成品質はまだ未判定です。Base採用、独立学習・全文DEV・最終TESTは未完了です。最新の実状態は[状態記録](docs/autonomous_status.md)に保存します。

2026-10-15最新: Base完成までの4項目を再開し、DEV/TEST reader分離を修理しました。最新[context likelihood100M比較](reports/phase6/context-likelihood-science-20261015/completion.json)は学習・数値監査・生成80件の個別内容確認まで完了しましたが、不採用です。一貫性1/80、適切完結1/80、EOS22/80、反復50/80で原基準を満たしていません。次は別の根拠ある同10M介入を検討します。独立学習・全文DEV・最終TEST・Base採用は未完了です。Chat/SFT・量子化・大型化・公開へは進みません。以下の2026-10-14記述は前回の納品時点の履歴です。

更新: 2026-10-14 JST。現在の依頼は全現行文書の最新化と今後の計画作成。Base/Chatは未完成・未採用。研究・教材準備・診断・生成評価・GPU学習は再開していない。

[最新Base結果144](docs/144_base_document_balance_results.md) / [前回Chat結果141](docs/141_chat_lr_comparison_results.md) / [次の計画145](docs/145_post_rejection_next_plan.md) / [今回更新146](docs/146_documentation_followup.md)。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。

## 最新Baseの結果

文書長重み候補は文法23/80、一貫性1/80、適切完結2/80、EOS20/80、反復50/80で元基準未達。共通byte BPBも対照0.998487→1.000710と退行しました。17,698更新の全教師・重み・保存状態と対照の全sampler/digestを確認し、科学と技術GPUは合計約24分44秒でした。詳細は[144](docs/144_base_document_balance_results.md)、凍結計画は[143](docs/143_base_document_balance_plan.md)。

既存DEV抽出処理が元Base TEST20 promptもCPU構文解析していた問題を別記録しました。学習・GPU TEST採点には使っていませんが、将来の有資格Baseには別artifactのDEV/TEST readerと新しい封印TESTが必要です。未実施を合格とせず、原品質と10Mを維持します。

## 前回のChat比較（141）

同じ元10B親・TRAIN・Tokenizer・学習seed42・教師量・schedule・固定paddingで、peak LR1e-4の歴史対照S0と3e-5の新候補S1を比較しました。native10,001,152 parametersを維持し、S1は3,646更新・1,899,557 Assistant本文+EOT教師で終了しました。全updateの実入力/教師digestと全3保存状態も監査しました。

| 最終評価セット | S0内容 /80 | S1内容 /80 | S0自己文脈 /24 | S1自己文脈 /24 |
|---|---:|---:|---:|---:|
| 新DEV | 13 | 20 | 3 | 5 |
| 前回138 DEV | 19 | 18 | 3 | 5 |
| 以前133 DEV | 21 | 19 | 6 | 5 |
| 元旧DEV | 11 | 15 | 1 | 1 |

必要条件は各セットの内容56/80以上・自己生成文脈15/24以上などで、全4セットとも未達です。新DEVの内容差は+8.75ポイント、95%CI −1.25〜+18.75で、改善の統計条件も成立しません。低LRは未知DEVの損失を対照より抑えましたが、反復・停止の退行と新実履歴での不正UTF8が残りました。流暢さや学習損失だけでは会話能力の完成を示せません。

評価はCodex非blindです。Base保持・sampling・独立学習seed43・人間blind・fullDEV・封印TEST・採用の全7分岐は、候補なしで未実行・passed=false・品質未確認。元Chat TEST20行を準備で構文解析した事故も保存しており、将来の有資格Chat最終確認には新たな封印TESTが必要です。Base単独原因や10M容量限界は確定していません。

Base復旧124の後に143/144を実行し不採用で閉鎖しました。次は[計画145](docs/145_post_rejection_next_plan.md)で、今回の文書依頼は研究の再開ではありません。既存証拠から介入を1件選定し、原品質と10Mを維持して比較する方針を残します。証拠を満たすBaseが完成したら通知して停止し、Chatや量子化には自動移行しません。

- [結果141](docs/141_chat_lr_comparison_results.md)：全保存点・失敗・NLL・採否・資源・限界。
- [計画139](docs/139_chat_lr_comparison_plan.md) / [実行140](docs/140_chat_lr_comparison_execution.md)：凍結条件と時点別履歴。
- [状態](docs/autonomous_status.md) / [ロードマップ](docs/15_project_roadmap.md) / [文書一覧](docs/README.md) / [全文書カタログ](docs/document_catalog.md) / [更新142](docs/142_documentation_refresh.md)。
- [保存一覧](reports/phase7/chat-lr-20261014/final_archive.json) / [納品確認](reports/phase7/chat-lr-20261014/final_delivery_checks.json)：科学監査とローカル納品の証拠を区別。

## 成立した基盤と残る課題

追跡可能なデータ処理、日本語Tokenizer、10Mモデル、WSL/RTX4090での実学習、全学習状態の保存・再開、日本語を複数の観点で評価する経路を整えました。保存・再開やGPU実行の成功は、生成品質の完成とは別です。

Baseのteacher-decay2B比較はBPB1.1064→1.0903でも、一貫性3/80のまま、適切完結7→5/80で不採用でした。[Base結果123](docs/123_base_teacher_decay_2b_results.md)。元UI10B、別staged約10.6B、teacher-decay2B、後続SFTは異なる重みです。10B・2Bは学習量であり、モデルのパラメータ数ではありません。

直接SFT128は停止や文法を改善しましたが、内容・文脈は未達でした。その後の教材比較131、汎化比較133、意味多様性比較135も不合格で閉じています。[最初のSFT結果129](docs/129_chat_first_sft_execution.md)、[前の教材比較132](docs/132_chat_improvement_execution.md)、[前回結果136](docs/136_chat_generalization_results.md)、[前回教材結果138](docs/138_chat_semantic_diversity_results.md)。独立学習seed43、人間blind、fullDEV、protectedTESTと正式採用は未確認です。

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
