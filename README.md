# JMicro-10M

日本語の短文生成と数ターンの雑談を目的に、約10Mの言語モデルをTokenizerからスクラッチ構築する。計画は[フェーズ別実行計画](docs/15_project_roadmap.md)、設計・調査一覧は[docs](docs/README.md)を参照。

Phase 0〜3が完了。データpilot、4k/8k Tokenizer、約10Mモデル、cache、HF/実float GGUF、Q8/Q4候補と推論入口をiMacで検証した。[Tokenizer完了記録](docs/18_phase2_completion.md)、[モデル・export完了記録](docs/19_phase3_completion.md)を参照する。重みはランダム初期化で、本学習は未実施。次のPhase 4ではWindows＋RTX 4090＋ユーザー指定WSL 3.1/Linuxへ切り替え、学習器・保存再開・最大安定batchを検証する。

## 開発環境

TokenizerとpilotデータのHugging Face共有については[公開状態と取得手順](docs/huggingface_handoff.md)を参照する。公開リポジトリは作成済み、payloadのアップロードは公開承認待ち。

Pythonと依存は`uv`で管理する。`.python-version`は今回確認したPython 3.12.7、解決した依存versionと配布file hashは`uv.lock`へ固定。依存変更は`uv add`を使う。

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

`ml` extraにはNumPy、SentencePiece、protobuf、PyTorch、Transformers、datasets、safetensorsを登録済み。Phase 2〜3ではML本体をインストールしてCPU検証した。GGUF作成・検査には`export` extraの公式ggufも使う。データ処理とMLを同時に使う時は`--extra data --extra ml`を指定する。CUDA/driver互換性はWindowsへの切替時に検証する。

## 配置

| ディレクトリ | 内容 |
|---|---|
| `src/jmicro/` | 環境・データ・Tokenizer・モデル・export・推論・検証 |
| `configs/` | source台帳・pilot、T4K/T8K、学習候補、Tokenizer、評価、iMac/WSL設定 |
| `schemas/` | データrecord・準備run・設定・評価例のJSON Schema |
| `scripts/` | `uv run`で実行する入口 |
| `tests/` | 日本語dedup・split・話者対応・取得上限、BPB、前処理、snapshot検証 |
| `eval/` | Base/Chat各100件、dev/test manifest、採点・golden例 |
| `data/` | 小sample用。本文・shardsはGit管理外 |
| `reports/` | 準備run台帳、Phase 0〜3の検証・品質・再生成・export結果 |
| `docs/` | 設計、技術調査、評価仕様、移行手順 |

評価方法は[evaluation_protocol.md](docs/evaluation_protocol.md)、環境切替は[windows_handoff.md](docs/windows_handoff.md)、Phase 0の結果は[完了記録](docs/16_phase0_completion.md)を参照。

データpilotの取得・再生成・検証は[dataの手順](data/README.md)を参照する。過去のPhase 0記録を上書きせず、現在の開発検証は`reports/local/`へ保存する。

## Tokenizer・モデル・ローカル推論

再実行と各backendの起動は[Phase 3完了記録](docs/19_phase3_completion.md#再現と推論入口)を参照する。GGUF内蔵TokenizerはID契約が一致しないため、正式な入口は外部SentencePiece wrapperを使う`uv run --frozen --extra ml --extra export scripts/infer.py`。モデルとTokenizerのhashを照合する。

## 次に進めること

Phase 3の再実装は不要。Windows/WSL＋RTX 4090へ移行し、環境・artifact一致 → 学習器/shard/評価runner → 保存再開 → 最大安定batchと速度測定の順でPhase 4を進める。[高速に完成させる進め方](docs/15_project_roadmap.md#高速に完成させる進め方)と[引継ぎ手順](docs/windows_handoff.md)を参照する。

Gitのpushにはコード・設定・docs・小さな検証reportが含まれる。`data/phase1/processed/`と学習済みTokenizerの`artifacts/phase2/`はGit管理外なので、Windowsへ別途コピーしてhashを照合する。Git cloneだけでは48テストすべての実artifact検証は揃わない。
