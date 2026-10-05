# JMicro-10M

日本語短文生成と数ターンの雑談を目指す、Tokenizerからスクラッチ構築した10,001,152パラメータの言語モデル。現在はBaseで、Chat調整と実用品質目標は未達。

最新（2026-10-05）: [短い物語60M→200Mの比較結果60](docs/60_dataset_expansion_results.md)まで完了し、実験を停止した。二枝を同じ追加1B tokensで学習し、常識問題35.0→38.6%は改善したが、EOS34→25/80・一貫性15→9/80で新条件不採用。文章長・EOS密度も変わったため、増量だけの因果効果とはしない。[現在地](docs/autonomous_status.md)、[次回計画61・提案](docs/61_condition_preservation_next_plan.md)を参照する。

## 準備量・学習量・品質

| 項目 | 現在の値 |
|---|---|
| モデル規模 | 10,001,152 parameters。10Mは重みの数 |
| 一般Web train準備量 | 12,225,819,077 tokens |
| 短い物語準備量 | 200,000,192 tokens（旧59,963,449＋新140,036,743） |
| 主系列とUIの学習量 | 10,000,007,168 tokens、元final10Bを配信 |
| 最新比較枝の学習量 | 元10Bから各追加1,000,013,824、各累積11,000,020,992 tokens |
| 品質 | Base/Chat未達。候補比較の合格と実用品質の達成を区別する |

別枝の学習tokensを足して一つのモデルの学習量とは扱わない。一般Webの独立全corpus混入・重複監査、人手blind、保護test評価は未完了。

## ローカルで試す

元final10BモデルのWeb UI: **[http://127.0.0.1:7860](http://127.0.0.1:7860)**。書き出しから続きを生成し、生成量・Temperature・Top P・停止・コピーを操作できる。推論はWSL/RTX4090で実行する。今回の11B候補へ重みを差し替えていない。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/start_webui.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/stop_webui.ps1
```

[操作・保存先](docs/43_local_webui.md)。開始前に既存processを確認する。UIはGPU lockを保持するため、別途再開されたGPU実験中だけ停止し、終了後に元10Bへ戻す。

## 最新の同条件評価

同じdev256本文BPBと固定80生成、各追加1Bの終端比較。全文dev BPBとは分母が異なるため数値を直接比較しない。

| 指標 | 旧60M教材 | 新200M教材 |
|---|---:|---:|
| dev256 BPB（低いほどよい） | 0.977154548 | 0.977322093 |
| EOS / 反復（各80） | 34 / 15 | 25 / 14 |
| 一貫性 / 適切完結（各80） | 15 / 20 | 9 / 19 |
| JCommonsenseQA | 35.031% | 38.561% |

日本語の[評価仕様v2.1](docs/45_japanese_base_evaluation_v2.md)、元10Bの[追加評価46](docs/46_japanese_base_evaluation_v2_results.md)、[教材と学習量比較57](docs/57_matched_story_and_learning_budget_results.md)、最新の[結果60](docs/60_dataset_expansion_results.md)を参照する。BPBや実装checksだけで自然な日本語生成の合格とは判断しない。

## 次回の計画

[計画61](docs/61_condition_preservation_next_plan.md)は「保存した失敗の診断→同じsourceで品質・長さ・EOS条件をそろえる→同量各100M比較→条件付き全文と採否」。準備に失敗した場合と一次不合格の場合の停止分岐、実測に基づく予算を記載した。現在は文書更新だけで、新しいデータ・GPU jobを開始していない。20B/50B/Chat/test/publicationへ自動移行しない。

計画58段階1〜3の実験完了はlocal commit `afad164`。旧runは完成しているので再起動しない。次の実行は再開された依頼の範囲で進める。

## 環境と保存先

Pythonはuv管理3.12.7。すべてのPython（一時スクリプト・tests・runner含む）は`uv run --frozen`、依存変更は`uv add`。学習はWSL2/RTX4090/Linux diskで実施済み。新PCで不足する環境だけ復元する。

```bash
uv python install 3.12.7
uv sync --frozen --extra hub --extra data --extra ml --extra export
```

正本はWindows `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`、Linux実行コピーは`/home/aihub_ubuntu/src/japanese-tiny-llm-10m`、大容量データは`/home/aihub_ubuntu/jmicro-data`。重み・shards・大型rawはGit管理外で、別PCへ別途引き継ぐ。固定HubはpilotとTokenizer用で、学習済み重みと12.23Bは含まない。[引き継ぎ手順](docs/windows_handoff.md)、[固定公開成果物](docs/huggingface_handoff.md)。local Git identityは`yousan <ka1357amnbpdr@gmail.com>`、自動pushなし。

## 文書と証拠

[文書一覧](docs/README.md)、[作業ルール](AGENTS.md)、[原ロードマップと品質条件](docs/15_project_roadmap.md)、[チェックリスト](docs/10_next_steps.md)、[評価契約](docs/evaluation_protocol.md)、[実験台帳](reports/README.md)。旧現在地は[2026-10-05保存履歴](docs/autonomous_history_20261005.md)へ分離し、凍結した実験報告・source・raw・Phase0〜3成果物は変更しない。
