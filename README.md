# JMicro-10M

日本語の短文生成と数ターンの雑談を目的に、Tokenizerからスクラッチ構築する約10Mの言語モデル。現在のモデルは **10,001,152 parameters**、準備済みtrainデータは **12,225,819,077 tokens**。

2026-10-04現在、主系列の5B学習と、同じ5B親からWeb/短文20%を各100M追加する比較を完了した。**直接10Bへ継続する設定と実GPU保存再開検証は準備済みで、本学習10Bは未開始。** 現在の文書更新は学習の起動を伴わない。[現在地](docs/autonomous_status.md)、[次の計画](docs/39_learning_scale_and_generation_plan.md)、[10B準備結果](docs/40_base_10b_preparation.md)を参照する。

## 学習結果と残る課題

同じ全文devのBPB（小さいほど良い）と固定80生成で比較した。各5.1Bは別のモデルで、学習量を合算しない。

| 条件 | 全文BPB | 自然EOS / 80 | 反復 / 80 | 全400 raw Unicode失敗 |
|---|---:|---:|---:|---:|
| 元5B | 0.964484 | 0 | 59 | 2 |
| Web仕上げ5.1B | 0.958092 | 0 | 57 | 0 |
| 短文仕上げ5.1B | 0.959011 | 13 | 51 | 2 |

短文混合でEOS・反復は改善したが、途中不正UTF8とcap末尾切断が残り、最終採用条件は不合格。表示末尾helperは実装済みでもraw失敗を免除しない。数量・時刻・文脈の誤りも残り、Base/Chatの実用品質は未達。[比較と内容確認](docs/38_eos_5b_finish_results.md)。

## 次の実行

1. **10B設定準備は完了。** 関連14tests、実CUDA16updates/524,288検証tokensの全state/history保存再開一致、保存証拠26項目を確認した。
2. **次は直接総10B学習。** 手元の12.23Bデータを使い、保存stable4.75Bから9.5B stable＋最終decayへ進む。7.5Bの中間実験と新データ収集は省く。
3. **同じ全文dev/400生成で比較し、報告・commitして停止。** 本文予測とEOS・反復・文字化け・内容を分けて評価する。後続の短文仕上げ/UTF8制約/Chat等は別範囲。

次段階を実行する場合のLinux repo内コマンド:

```bash
bash scripts/run_base_10b.sh --train
```

引数なしと `--verify-only` は検証専用。準備は完了しているので再学習・再検証せず結果を再利用する。学習・比較の目安は145〜165分、実装・内容確認は別。[引き継ぎ手順](docs/windows_handoff.md)で保存先と起動前のprocess確認を行う。

## 環境と保存先

Pythonはuv管理3.12.7。WSL2/RTX4090/Torch2.14.1+cu130で実GPU検証済み。Pythonは一時スクリプト・tests・自律runnerもすべて `uv run --frozen`、依存変更は `uv add`。通常のWSL復元には全extrasを維持する。

```bash
uv python install 3.12.7
uv sync --frozen --extra hub --extra data --extra ml --extra export
```

Git/コード/docsの正本はWindows workspace、Linux実行コピーは `/home/aihub_ubuntu/src/japanese-tiny-llm-10m`、大容量データは `/home/aihub_ubuntu/jmicro-data`。重み・shards・大きなraw evidenceはGit管理外なので、別PCには別途引き継ぐ。固定HubはpilotとTokenizerの復元用で、学習済み重みや12.23Bデータは含まない。[公開成果物の取得](docs/huggingface_handoff.md)。

準備完了コードは `4c3fbaf` でlocal commit済み。今回pushは実行しない。Linux側のGit HEADだけで実行コードを判断せず、凍結source/config hashを確認する。

## 文書と成果物

[docs一覧](docs/README.md)、[作業ルール](AGENTS.md)、[原ロードマップと品質条件](docs/15_project_roadmap.md)、[評価仕様](docs/evaluation_protocol.md)、[自律runner](docs/codex_automation.md)。過去の現在地メモは [履歴](docs/autonomous_history_20261004.md) に移し、Phase0〜3を含むhistorical report/weightsは保持する。

| 保存領域 | 内容 |
|---|---|
| src/jmicro・scripts | Tokenizer/model/training/evaluation/export/inferenceと実行入口 |
| configs・schemas | 凍結設定、入力とrun契約 |
| tests・eval | 実装checksと保護された固定suite |
| reports | 小さな結果・判断・監査。大型run/checkpointはLinux側に保持 |
| docs | 現在の計画・状態・引き継ぎと設計/完了履歴 |

Phase0〜5とPhase6の基盤・データ・学習比較は完了済み。過去の48/64/68/90/99等のテスト件数は各時点の証拠で、現在の全suite件数を表すものではない。今回の14件は10B準備に関連するchecksで、品質合格ではない。完了済みTokenizer学習・Phase3 export・GPU study・全データ照合を再実行する必要はない。
