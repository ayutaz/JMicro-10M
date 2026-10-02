# iMacからWindows/WSL学習PCへの移行

この手順はPhase 0で用意する引継ぎ仕様。実施はPhase 4に入り、Windows＋RTX 4090＋ユーザー指定WSL 3.1上のLinuxへ切り替える時。Windows機への接続、インストール、GPU検証はまだ実施していない。

**現在地**: Phase 0〜3は完了。次はこの移行を行う。完成までの時間短縮を優先し、まず同じTokenizer/pilotを使ったCUDA検証へ進む。Phase 3のTokenizer再学習やnative CPU全検証を移行の前提にしない。[Phase 4の優先順](15_project_roadmap.md#高速に完成させる進め方)

## iMac側で引き継ぐもの

1. コード、docs、config、`.python-version`、`pyproject.toml`、`uv.lock`、固定eval/schemaを同じGit commitに揃える。未コミット変更が必要なら準備runのsource snapshotとledgerも一緒に引き継ぐ。
2. Phase 2で作成済みの`artifacts/phase2/{4096,8192}/`、special IDs、wrapper設定、golden例、artifact hash。再学習せず同じmodelをコピーする。
3. 小sample、データ/split manifest、必要なshardsとchecksum。大規模raw/shards/checkpointはWindows側のデータ領域で管理する。
4. Phase 2・3のCPU検証report。ランダム重みでの再検証には`artifacts/phase3/{t4k,t8k}/`を使う。`.venv`、Python実行file、Mac native binaryはコピーせずLinuxで再構築する。[実行・runtime build手順](19_phase3_completion.md#再現と推論入口)

準備runは次で作る。snapshotはコード・設定・lockfileを含み、ledgerにchecksumを記録する。Tokenizer/data入力がまだないPhase 0では入力hashは`null`。存在する場合は実fileを渡す。

```sh
uv run --frozen scripts/experiment.py prepare-run --name handoff
uv run --frozen scripts/experiment.py prepare-run --name handoff-with-inputs --tokenizer-artifact /path/to/tokenizer.model --dataset-manifest /path/to/manifest.parquet
```

snapshotをコピーする場合は`reports/<run_id>/`と親の`experiments.jsonl`を一緒に持ち込み、`verify-run`で改変を検出する。

## 最初の移行で別途コピーするfile

Git clone/pullではGit管理外のデータとTokenizerは取得できない。repo内の同じ相対pathへ次をコピーする。

| 相対path | 用途 |
|---|---|
| `artifacts/phase2/4096/`、`artifacts/phase2/8192/` | 学習済みTokenizer、wrapper/special設定、trainer metadata |
| `data/phase1/processed/corpus.jsonl` | splitとbucketを持つpilot本文・会話 |
| `data/phase1/processed/dataset_manifest.parquet` | 出所・本文hash・採否・splitの追跡 |
| `data/phase1/processed/split_manifest.json` | 入出力checksumと固定split |
| `data/phase1/processed/tokenizer_sample.jsonl` | 共通sampleのhash/ID確認 |

Tokenizer modelの期待hashは[Phase 2 contract report](../reports/phase2/tokenizer_contract_report.json)、データの期待hashはコピーした`split_manifest.json`と[Phase 1完了監査](../reports/phase1/completion_audit.json)で照合する。相対pathを保ち、Windows側の絶対pathへMacのpathを流用しない。

原データを復元検証する時は`data/phase1/raw/`も必要。ランダム重みのnative GGUFを再比較する時は`artifacts/phase3/`も必要だが、最初のCUDA確認には不要。`.venv`、Mac native build、大きなlogits、再学習候補・停止fixtureは最初の転送対象から外してよい。

## Windows/WSL側の環境構築

WSL 3.1は指定されたパッケージversionとして記録し、distributionのWSL実行方式とは別に確認する。PowerShellで`wsl --version`、`wsl -l -v`を記録し、Linux側でOS/GPU/driverを確認する。Windows側NVIDIA driverを利用する構成とし、詳細は[環境資料](07_environment.md)を参照する。

Linuxへリポジトリを配置し、`uv`を使用する。uv導入は[公式手順](https://docs.astral.sh/uv/getting-started/installation/)に従う。以降はLinux shellで実行する。

```sh
uv python install 3.12.7
uv sync --frozen --extra data --extra ml --extra export
uv run --frozen --extra data scripts/validate_phase0.py --output reports/phase4/phase0_validation.json
uv run --frozen --extra data --extra ml --extra export pytest -q
uv run --frozen --extra data --extra ml --extra export scripts/experiment.py capture-environment --probe-torch --output reports/phase4/environment.json
```

`ml` extraはPyPI経由の依存をロックしているが、4090/driverとのCUDA互換性は未検証。`torch_probe.cuda_available`、`cuda_runtime`、`bf16_supported`と`nvidia_smi`の実結果を確認する。CUDA build/indexの変更が必要なら[PyTorch公式選択手順](https://pytorch.org/get-started/locally/)を使い、`uv add`で変更し、更新したlockfileと環境を別の検証結果として残す。`--frozen`のまま別wheelへ差し替えたことにしない。

このrepoのTokenizerテストはartifactがない場合skipする。Phase 3完了時は48 tests、skip 0だった。移行側で成功数だけを見ず、Tokenizerのコピー後にskipがないことを確認する。この`pytest`はCPU契約の確認であり、CUDAのforward/backward、GPU再開、速度実測の代わりにはならない。

## データpathと最大バッチ

```sh
export JMICRO_DATA_ROOT="$HOME/jmicro-data"
```

この変数で学習PC側のdata/Tokenizer/shards/checkpoint領域を指定する。hot dataはLinux filesystemを候補にし、Windows volumeとのI/O差を実測する。

Phase 4でmicro batch 8→16→32→64…と増やし、境界の中間値も測る。loss/backward/optimizer、実shard、評価・保存まで含めて最大安定値を選ぶ。peak VRAM、定常tokens/sec、最大容量と最高速度の候補を保存する。effective batch、LR、warmup、更新回数は別設定とし、小探索で小batchを使う時は理由を明記する。

初期のコード動作確認は小batchで先に行う。保存再開が成立した後にbatch/compile/backendの比較を進め、最大安定batchと実throughputを本学習設定へ反映する。学習器・shard・評価runnerは未実装なので、上の環境構築commandだけでは本学習は開始しない。

## 移行完了のgate

- 同じcommit/config、Tokenizer/sample hashとencode ID列が一致する。
- CUDAでfinite forward/backwardが成立する（モデル実装後）。
- prefill/cache、保存再開、消費token列の検証がGPUで通る。
- 実shardの最大安定バッチ、速度、メモリ、保存時間を確認する。
- `environment.json`、`handoff_report.json`、`resume_report.json`、`throughput_report.json`を残す。

Phase 0のCPU検証やCUDA可否probeだけでこのgateを完了扱いにしない。以降のoverfit/10M smokeと本学習はWindows側で実行する。
