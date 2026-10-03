# JMicro-10M

Phase 5完了（2026-10-03）: overfit・10M smoke・4本の100M比較・補助評価・候補選定・独立監査が終了。[完了記録](docs/23_phase5_completion.md)を参照。Phase 6本学習は開始せず停止中。

日本語の短文生成と数ターンの雑談を目的に、約10Mの言語モデルをTokenizerからスクラッチ構築する。計画は[フェーズ別実行計画](docs/15_project_roadmap.md)、設計・調査一覧は[docs](docs/README.md)を参照。

Phase 0〜5が完了。データpilot、4k/8k Tokenizer、約10Mモデル、cache、HF/実float GGUFをiMacで検証し、WSL＋RTX 4090で学習器・保存再開・最大安定batch・評価を実測した。[Tokenizer完了記録](docs/18_phase2_completion.md)、[モデル・export完了記録](docs/19_phase3_completion.md)、[Phase 4完了記録](docs/21_phase4_completion.md)を参照する。Phase 4は小さいGPU検証runで、Base/Chatの本学習と能力目標は未達。Phase 5の候補選定と独立監査も終了し、Phase 6前で停止中。

**別PCで続きを進める場合は[Windows/WSL＋RTX 4090の再開手順](docs/windows_handoff.md)から始める。** 固定成果物の復元、uv環境・CUDA確認、実装済みCLIと引継ぎ条件をまとめている。最近のPhase 4コミットはローカル保存で、GitHubへpushしていない。新規cloneだけで最新コードが揃うとは限らない。

環境整備・学習・評価・改善をCodexへ継続して任せる場合は[自律実行の設定とrunner](docs/codex_automation.md)を参照する。次の担当の現在地は[継続作業の状態](docs/autonomous_status.md)、作業ルールは[AGENTS.md](AGENTS.md)。2026-10-03にFull accessが反映され、WSL・公開成果物復元・CUDA/BF16確認を通過した。

## 開発環境

TokenizerとpilotデータのHugging Face共有については[公開状態と取得手順](docs/huggingface_handoff.md)を参照する。[ライセンス・個人情報確認](docs/20_publication_review.md)を終え、出所・利用条件を付けた公開版の匿名取得・checksum検証が完了した。

Pythonと依存は`uv`で管理する。Pythonの実行は環境確認・自律runner・テスト・一時スクリプトも含め、必要なextraを付けた`uv run --frozen ...`に統一する。systemの`python`・`python3`・`py`を直接実行しない。`.python-version`は今回確認したPython 3.12.7、解決した依存versionと配布file hashは`uv.lock`へ固定。Python導入は`uv python install 3.12.7`、依存復元は`uv sync --frozen`、依存変更は`uv add`を使う。

```sh
uv sync --frozen --extra data --extra ml --extra export
uv run --frozen --extra data scripts/validate_phase0.py --output reports/local/phase0_validation.json
uv run --frozen --extra data --extra ml --extra export pytest -q
uv run --frozen --extra data scripts/experiment.py capture-environment --output reports/local/environment.json
uv run --frozen --extra data scripts/experiment.py prepare-run --name development
```

最後のcommandが表示するrunディレクトリを指定して検証する。

```sh
uv run --frozen --extra data scripts/experiment.py verify-run reports/<run_id>
```

新しい依存は用途に応じて追加する。

```sh
uv add <package>
uv add --dev <test-package>
uv add --optional data <data-package>
uv add --optional ml <ml-package>
```

`data` extraにはPyArrow、datasketch、fsspec、aiohttpを登録済み。Phase 1のデータ処理では`uv sync --frozen --extra data`と`uv run --frozen --extra data ...`を使う。

`ml` extraにはNumPy、SentencePiece、protobuf、PyTorch、Transformers、datasets、safetensorsを登録済み。GGUF作成・検査には`export` extraも使う。WSLではPython 3.12.7、PyTorch 2.14.1 / CUDA 13.0、Windows driver 616.92でCUDA/BF16を検証済み。環境を保持する通常のWSL実行では`--extra hub --extra data --extra ml --extra export`を付ける。

## 配置

| ディレクトリ | 内容 |
|---|---|
| `src/jmicro/` | 環境・データ・Tokenizer・モデル・shards・学習・評価・export・推論 |
| `configs/` | source台帳・pilot、T4K/T8K、学習候補、Tokenizer、評価、iMac/WSL設定 |
| `schemas/` | データrecord・準備run・学習run・設定・評価例のJSON Schema |
| `scripts/` | `uv run --frozen`で実行する入口 |
| `tests/` | 日本語dedup・split・話者対応・取得上限、BPB、前処理、snapshot検証 |
| `eval/` | Base/Chat各100件、dev/test manifest、採点・golden例 |
| `data/` | 小sample用。本文・shardsはGit管理外 |
| `reports/` | 準備run台帳、Phase 0〜5の検証・再生成・export・GPU学習・比較結果 |
| `docs/` | 設計、技術調査、評価仕様、移行手順 |

評価方法は[evaluation_protocol.md](docs/evaluation_protocol.md)、環境切替は[windows_handoff.md](docs/windows_handoff.md)、Phase 0の結果は[完了記録](docs/16_phase0_completion.md)を参照。

データpilotの取得・再生成・検証は[dataの手順](data/README.md)を参照する。過去のPhase 0記録を上書きせず、現在の開発検証は`reports/local/`へ保存する。

## Tokenizer・モデル・ローカル推論

再実行と各backendの起動は[Phase 3完了記録](docs/19_phase3_completion.md#再現と推論入口)を参照する。GGUF内蔵TokenizerはID契約が一致しないため、正式な入口は外部SentencePiece wrapperを使う`uv run --frozen --extra ml --extra export scripts/infer.py`。モデルとTokenizerのhashを照合する。

## 次に進めること

Phase 5の100件overfit → 10M smoke → 100M比較・候補選定が完了し、Phase 6前で停止中。[完了記録](docs/23_phase5_completion.md)を参照する。Tokenizer再学習・成果物再取得・完了済みPhase 4測定を繰り返す必要はない。[実測と制約](docs/21_phase4_completion.md)、[次の作業](docs/10_next_steps.md)を参照する。

Git管理対象はコード・設定・docs・小さな検証report。本文・Tokenizer・checkpointは管理外なので固定Hub成果物とLinux保存先を引き継ぐ。Phase 4では実artifact付きの全64テストが成功した。新規cloneにはartifactを別途復元する。

学習入口は`scripts/train.py`の`build-shards` / `train` / `evaluate`。`train`はCLI引数から設定を作り、`configs/training/baseline.json`を自動読込しない。AdamW＋warmup/cosineは実装済み、Muon・WSD・Chat trainerは未実装。[利用例と保存再開](docs/windows_handoff.md#6-実装済みcliと次回の再開)を参照する。
