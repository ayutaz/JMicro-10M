# Phase 4完了: WSL・学習器・再開・4090実測

2026-10-03に実機の完了条件を通過した。ユーザー指定に従い、この区切りで停止する。Phase 5のoverfit / 10M smoke / 100M比較は開始していない。

## 完了証拠

- [監査・handoff](../reports/phase4/handoff_report.json): WSL package 3.0.1.0 / Ubuntu WSL 2、RTX 4090、Windows driver 616.92、Python 3.12.7 / uv、PyTorch 2.14.1 / CUDA 13.0。公開25 filesの固定revision/hash検証、CUDA/BF16 finite forward/backward、全64 tests / skip 0。
- [保存再開](../reports/phase4/resume_report.json): T8K/T4Kとも実shard・context 1024・micro batch 2で連続200と100+100を比較。各系列409,600 tokens。消費列digest、loss、weights、optimizer、scheduler、RNG、samplerが完全一致。atomic checkpointとsource/data/config hashを記録。
- [評価契約](../reports/phase4/base_evaluation_contract_report.json): dev 924文書 / 1,633,458共通canonical bytesを本文一度ずつ採点し、EOS NLLを分離。共通短文32 window、CUDA評価によるRNG干渉なしを検証。固定Base dev 80 promptについてgreedy・抑制なし診断・sampling 3 seedsの400出力を各モデルで取得。testは未使用。
- [速度・容量](../reports/phase4/throughput_report.json): 倍増と中間値で境界を探し、最大batchで200更新を3回、評価・生成・保存まで通過。synthetic / 実shard、default / math backend、compileのcold初回と定常速度を分離して測定。
- [予算](../reports/phase4/resource_budget.md): 100M / 1B / 10B / 20B / 50Bのcompute時間、評価/saveの追加時間、実ストレージを記録。長期runは起動していない。

## 実測結果

FP32 parameters + BF16 autocast、context 1024、gradient accumulation 1。CUDA allocator 94%上限でWindows desktopと評価/saveの余裕を残したeager/default SDPAの運用上限である。

| モデル | 最大安定micro batch | effective batch tokens | 次のOOM batch | 定常速度（3回の中央値） |
|---|---:|---:|---:|---:|
| T8K | 57 | 58,368 | 58 | 225,169 tokens/s |
| T4K | 64 | 65,536 | 65 | 218,411 tokens/s |

最大容量と最高速度を区別する。測定点の最高速度はcompileのbatch 8でT8K 439,656 / T4K 448,601 tokens/s。compile済み経路の最大容量は未探索で、全backendの理論的最大batchとは扱わない。compileとeagerの実GPU BF16 logitsは既定の`atol=0.05, rtol=0.02`で一致（最大絶対差0.0625、判定は両許容差の合成）。

明示的なFlash-only backendは現モデルのnon-null attention maskに対応せず、失敗したraw probeを保持している。default、math-only、compile/defaultは実測成功。mask不要のcausal training専用経路は将来の別改善候補であり、今回実装・採用していない。

Phase 4の小さい検証checkpointでdev BPBはT8K 2.09299、T4K 2.27757。greedyのEOS自発停止は両方0/80。これは評価処理の診断であり、日本語Base/Chatの能力目標達成ではない。人手の文法・関連性・文脈評価は未実施。

## 再現・保存先

コードの正本はWindows workspace、実行はLinuxコピー`/home/aihub_ubuntu/src/japanese-tiny-llm-10m`。shardは`/home/aihub_ubuntu/jmicro-data/shards/{t8k,t4k}-pilot/`、実ログ・snapshot・checkpointはLinuxの`reports/phase4/gates-20261003/`に保持する。Windowsにも小さいreportをコピーしてGitに保存する。過去Phase 0〜3は保持した。

すべてのPython入口は`uv run --frozen`、今回のextrasは`hub,data,ml,export`。実装は`src/jmicro/shards.py`、`training.py`、入口は`scripts/train.py`。新規shardの例:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py build-shards \
  --tokenizer artifacts/phase2/8192/tokenizer.model --output "$HOME/jmicro-data/shards/new-t8k"
```

既存shard directoryは上書きしない。checkpoint再開では元のsource/data/configとscheduler予算を維持する。`--resume`時に保存済み更新より先の未保存metricsがあれば履歴を退避してcheckpoint境界から再開する。準備runの`tokens_seen=0`と学習runの台帳/schemaを分離する。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export pytest -q -ra
```

GPU排他は`~/jmicro-data/gpu.lock`。長い検証jobはhiddenのWindows `wsl.exe` supervisorで保持し、PID/boot ID/start ticks・command・stage・run/checkpointを保存した。完了後はGPU学習jobを終了した。

次の再開では既存job/checkpointを確認し、Phase 5の100件overfitから進める。ユーザーが再開するまでは新しいGPU実験を開始しない。
