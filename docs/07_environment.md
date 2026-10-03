# 実行環境とデータ配置

Phase 5完了（2026-10-03）: overfit・10M smoke・4本の100M比較・補助評価・候補選定・独立監査が終了。[完了記録](23_phase5_completion.md)を参照。Phase 6本学習は開始せず停止中。

最終更新: 2026-10-03。[Phase 4監査](../reports/phase4/handoff_report.json)で確認した実機環境を記載する。Phase 5も完了し、Phase 6前で停止中。

## 実機環境

| 項目 | 確認結果 |
|---|---|
| Windows / WSL package | Windows build 26100.6584 / WSL 3.0.1.0 |
| Linux distribution / 実行方式 | Ubuntu / WSL 2、user `aihub_ubuntu` |
| GPU / Windows driver | RTX 4090、24,564 MiB / 616.92 |
| Python / Linux uv | 3.12.7 / 0.9.0 |
| PyTorch / CUDA | 2.14.1 / 13.0、lock runtime 13.0.96 |
| precision | FP32 parameters/optimizer、BF16 autocast |
| 検証 | CUDA/BF16 finite forward/backward、全64 tests / skip 0 |

WSL packageの3.xとdistributionのWSL 2は別のversion。NVIDIA driverはWindows側のものを使用し、WSLへLinux display driverを追加しない。[NVIDIA公式手順](https://docs.nvidia.com/cuda/wsl-user-guide/)。Linuxのnvidia-smi表示にはツール版615.71.08もあるが、driverの観測値は616.92。

## iMacから学習PCへ切り替える境界

Phase 0〜3はM1 iMac上の履歴。コードと公開pilot/TokenizerをWindows/WSLへ引き継ぎ、Phase 4で実GPU検証を完了した。Macの仮想環境・native binaryは移していない。新規PCの復元は[引継ぎ手順](windows_handoff.md)、復元済みPCの再開は[現在の状態](autonomous_status.md)を読む。

Python実行は一時スクリプトも`uv run --frozen`。導入は`uv python install 3.12.7`、依存復元は`uv sync --frozen`、変更は`uv add`。通常のWSL実行は`--extra hub --extra data --extra ml --extra export`を付けて固定環境を保持する。

## 最大バッチの決め方

本学習では最大安定micro batchを実測して使う方針。Phase 4はcontext 1024、accumulation 1、eager/default SDPA、fused AdamW、CUDA allocator 94%上限で測定した。

| モデル | 最大安定micro batch | effective tokens/update | 次のOOM batch | 定常中央値 |
|---|---:|---:|---:|---:|
| T8K | 57 | 58,368 | 58 | 225,169 tokens/s |
| T4K | 64 | 65,536 | 65 | 218,411 tokens/s |

倍増と境界の中間値を探し、最大値を3×200更新、評価・保存込みで確認した。測定点の最高速度はcompile batch 8で439,656 / 448,601 tokens/s。compile経路の最大容量は未探索。最大容量と最高速度を区別し、backend/context/precision/optimizerを変える場合は新しい設定で検証する。小探索のeffective batchと更新数は別に固定する。

default、math-only、compile/defaultは成功。Flash-onlyはnon-null attention mask非対応で失敗を保持している。Flash対応のmask変更は未実装の改善候補。[実測詳細](21_phase4_completion.md)

## ストレージ配置

Windowsコード正本は`C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`、Linux実行コピーは`/home/aihub_ubuntu/src/japanese-tiny-llm-10m`。

```text
~/src/japanese-tiny-llm-10m/
  artifacts/phase2/{4096,8192}/   公開Tokenizer
  data/phase1/processed/         固定pilot、manifest、sample
  reports/phase4/gates-20261003/ ログ、source snapshot、検証checkpoint
~/jmicro-data/
  shards/{t8k-pilot,t4k-pilot}/   実学習入力
  gpu.lock                      単一GPU job排他
```

ユーザーの約8TBストレージ計画とWSL内の実容量は別。監査時のLinux空きは980,811,743,232 bytesで、VHDの上限は約1TB。8TB全体がLinuxから使えることは未確認。uv cache約19.27GB、venv約6.07GB、Phase 4成果物約1.47GBはapparent bytesで、hardlinkを重複排除していない。[実容量と予算](../reports/phase4/resource_budget.md)

## 事前tokenizeと実装済みshard

学習中のon-the-fly tokenizationを避け、公開corpusのWeb trainを共通wrapperでencodeする。会話/sharealikeはBase系列へ混ぜていない。各split一本のlittle-endian uint16 `.bin`、document index、token-byte情報、hash付きJSON manifestを保存する。現在のpilot実装は複数shard/source mixtureの大規模loaderではない。

T8K trainは18,022 docs / 6,884,183 stream tokens / 32,774,150 body bytes、T4Kは同じ文書・bytesで8,398,329 tokens。stream countはBOS/EOSを含む。固定長blockをseed/epochでshuffleし、文書を跨いでpackする。BOS targetsをmaskし、最後の不完全train blockは使用しない。dev/testは文書単位で別評価する。[データ手順](../data/README.md)

50B tokensのID本体は約100GB、100Bは約200GBという算術値。二つのTokenizer版、raw、index、checkpoint、一時領域は別加算。50〜100B master corpusは未取得で、実容量を計測してから拡張する。

## benchmark済みと残る測定

synthetic/実shard、eager/compile、backend、batch、peak VRAM、data wait、評価/save時間を測定済み。Windows volumeとLinux filesystemのI/O比較、DataLoader単体、厳密なMFU、compiled容量探索は未実施。これらをPhase 4の成功として記載しない。

長期予算は実測tokens/sから計算し、評価/save/compile初回/データ処理/比較runを加える。T8K eager最大batchの10B computeは約12.34h。品質改善に必要な総期間の保証ではなく、20B/50B着手はロードマップの条件に従う。
