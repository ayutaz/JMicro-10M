# JMicro-10M

日本語の短文生成と数ターンの雑談を目的に、Tokenizerからスクラッチ構築する約10Mの言語モデル。現在のモデルは **10,001,152 parameters**、準備済みtrainデータは **12,225,819,077 tokens**。

2026-10-04現在、主系列5Bと各100M仕上げ比較に続き、**総10,000,007,168 tokensの学習と保存状態19項目の確認を完了した。** WSL2/RTX4090で定常約69.5万tokens/秒、GPU時間約2時間8分。10Bの全文dev/固定400品質評価も完了した。BPB0.954018、固定EOS0/80・反復53/80、raw Unicode0/400。今回は報告・local commitで停止する。[評価結果と残る課題](docs/42_base_10b_quality_evaluation.md)。[10B学習結果と高速化](docs/41_base_10b_training.md)、[現在地](docs/autonomous_status.md)、[次の計画](docs/39_learning_scale_and_generation_plan.md)を参照する。

## 学習結果と残る課題

同じ全文devのBPB（小さいほど良い）と固定80生成で比較した。各5.1Bは別のモデルで、学習量を合算しない。

| 条件 | 全文BPB | 自然EOS / 80 | 反復 / 80 | 全400 raw Unicode失敗 |
|---|---:|---:|---:|---:|
| 元5B | 0.964484 | 0 | 59 | 2 |
| Web仕上げ5.1B | 0.958092 | 0 | 57 | 0 |
| 短文仕上げ5.1B | 0.959011 | 13 | 51 | 2 |
| 新10B | 0.954018 | 0 | 53 | 0 |

短文混合でEOS・反復は改善したが、途中不正UTF8とcap末尾切断が残り、最終採用条件は不合格。表示末尾helperは実装済みでもraw失敗を免除しない。数量・時刻・文脈の誤りも残り、Base/Chatの実用品質は未達。[比較と内容確認](docs/38_eos_5b_finish_results.md)。

## 次の実行

1. **10B設定準備は完了。** 関連14tests、実CUDA16updates/524,288検証tokensの全state/history保存再開一致、保存証拠26項目を確認した。
2. **直接総10B学習と保存確認は完了。** 手元の12.23Bデータを使い、保存stable4.75Bから9.5B stable＋最終decayへ到達した。7.5Bの中間実験と新データ収集は行っていない。
3. **step3: 同じ全文dev/400生成と内容比較は完了。** 本文予測・反復指標は改善したが固定自然EOSは0/80で、意味・数量・否定の誤りが残る。後続の短文仕上げ/UTF8制約/Chat等は別範囲。

中断復旧用のLinux repo内コマンド履歴。今回のrunは完了しているため再起動しない:

```bash
bash scripts/run_base_10b.sh --train
```

引数なしと `--verify-only` は検証専用。準備と本学習は完了しているので保存結果を再利用する。[引き継ぎ手順](docs/windows_handoff.md)で保存先と終了済みprocessを確認する。品質比較入口も実装・検証済みで完了runを再評価しない。

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
