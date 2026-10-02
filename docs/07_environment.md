# 実行環境とデータ配置

## 前提

**確定**:

- 現在の開発・設計環境はiMac。学習開始時に別のWindows PCへ切り替える
- 学習用Windows PCにRTX 4090を搭載
- RTX 4090 24GBを常時利用可能
- ユーザー指定のWSL 3.1上のLinux環境で学習
- 学習用GPUメモリを最大限使い、安定して学習できる最大バッチを実測して使う
- 約8TBのローカルストレージ

WSL 3.1はユーザー指定の採用環境として記録する。実際の導入version、Linux distribution、CUDA、PyTorchの組合せはWindows PCへ切り替えた時に実機で記録する。指定があることを導入確認済みとは扱わない。

**確認済み（追加調査）**: CUDAの公式手順はWSL 2の実行環境を対象とする。WSLパッケージのversionとdistributionのWSL 1／2は別に記録する。Windows側NVIDIA driverを利用し、WSL内へLinux GPU driverを別途入れない。[NVIDIA公式手順](https://docs.nvidia.com/cuda/wsl-user-guide/)、[benchmark・環境記録案](12_training_implementation_research.md)

## iMacから学習PCへ切り替える境界

**確定**: iMacでは設計・調査、コード作成、小sampleの処理、Tokenizer作成、CPUでのモデル・cache・export検証を進める。GPU benchmark、保存再開のGPU検証、100件overfit、10M smoke以降の学習はWindows PCのWSL/Linuxへ切り替えて行う。計画上の切替点はPhase 4の実機検証に入る前とする。学習器自体のコード作成はiMacで先に進めてよい。

**現在地（2026-10-02）**: Phase 0〜3をiMacで完了した。次は完成までの時間短縮を優先してWindows/WSL＋RTX 4090へ切り替え、開発とGPU検証を進める。Phase 3の成果物を引き継ぎ、移行確認に必要な検証を行う。[優先順と時間の見積もり方](15_project_roadmap.md#高速に完成させる進め方)

**提案**: 切替時は次を引き継ぐ。

1. 同じGit commitのコード・docs・configと、Linux環境の依存設定。iMacの仮想環境をそのままコピーせずLinuxで再構築する。
2. 4k/8k Tokenizer、特殊ID、golden例、評価promptとsplit、各artifact hash。
3. 小規模データmanifest、sample、shards、checksum。大規模raw/shardsは学習PC側で取得・処理する。
4. CPU検証reportと、Windows側で実施する検証・実行手順。

切替完了条件: 学習PCで同じconfigからモデルを再構築でき、Tokenizer/sampleのhashとID列が一致し、CUDA forward/backwardがfiniteであること。iMacとCUDAの重み・lossのbitwise一致は要求せず、数値誤差は事前の許容値で判定する。実機環境情報と移行確認結果を`environment.json`、`handoff_report.json`へ記録する。

## 最大バッチの決め方

**確定**: RTX 4090 24GB上で、本学習のmicro batchを安定動作する最大値まで増やす方針。最大値はモデル、context、precision、backend、optimizerごとに実測し、iMac上で数値を決め打ちしない。

**提案**: micro batchを8→16→32→64…と増やし、OOMまたは不安定になる範囲が分かったら中間値で境界を探す。forwardだけでなくloss/backward/optimizer step、実shard、評価・保存を含む運用で確認し、一時メモリ変動への余裕を残した最大安定値を選ぶ。最大容量の候補とtokens/secが最高の候補は両方記録する。

micro batch（GPUへ一度に載せる系列数）とeffective batch（optimizer更新1回の量）を別に記録する。単一GPU・固定長1024なら`effective batch tokens = micro batch × 1024 × gradient accumulation steps`。最大micro batchでも更新量が大きすぎる小探索では、比較目的に応じた小batchを別configにし、その理由を記録する。学習LR、warmup、更新回数も選んだbatchに合わせて検証する。

## 推奨stack

**確定（Python管理）**: Pythonと依存はuvで管理し、プロジェクト依存の追加/変更は`uv add`を使う。Phase 0で`pyproject.toml`、`uv.lock`、`.python-version`を作成済み。[実行手順](../README.md)、[Windowsへの移行](windows_handoff.md)

**提案（学習stack）**:

```text
Windows 11
  -> WSL 3.1（ユーザー指定）/ Linux（Ubuntuは候補）
     -> Python + uv
     -> NVIDIA CUDA対応PyTorch
     -> BF16
     -> torch.compile
     -> SDPA / FlashAttention
     -> Hugging Face datasets / SentencePiece
```

versionを早期固定し、`nvidia-smi`、PyTorch、CUDA runtime、GPU名、driver、OS、WSL versionをrun metadataへ残す。

## ストレージ配置

**提案**: 原データarchiveはWindows側8TB volumeでもよいが、学習時に高頻度アクセスするtokenized shards、index、checkpointはWSLのLinux filesystem側へ置く。

```text
Windows volume
  D:\datasets\jmicro\raw\        raw Parquet / archive

WSL Linux filesystem
  ~/jmicro-data/
    tokenizers/
    tokenized/
    checkpoints/
    eval/
    cache/
    manifests/
```

`/mnt/d/...`越しの大量小file I/Oはbottleneckになり得るため、hot dataをLinux filesystemへ寄せる。

## 事前tokenize

**確定**: 学習中のon-the-fly tokenizationを避ける。

```text
Raw Parquet
  -> filter / dedup
  -> JMicro tokenizer
  -> uint16 token IDs
  -> binary shards
  -> manifest.parquet
```

4k/8k vocabは`uint16`に収まる。純粋なtoken ID本体は、50B tokensで約100GB、100B tokensで約200GB。index、manifest、二つのTokenizer版、一時領域、raw data、checkpointを含めると2〜4TB程度を見込む。8TBで十分だが、空き容量monitorを用意する。

## Shard案

```text
data/tokenized/jmicro8k/
  train/
    shard-000000.bin
    shard-000001.bin
  validation/
    shard-000000.bin
  manifest.parquet
```

**提案**: 1 shard = 100M tokensなら約200MB。50Bで約500 shards。各shardへtoken count、source mixture、checksum、Tokenizer hashを記録する。

## 最初のbenchmark

環境構築後、学習前に以下を測る。

- synthetic token batchでforward/backward tokens/sec
- `torch.compile`の有無
- SDPA backend別
- batch size sweep
- DataLoaderのみのthroughput
- WSL filesystemと`/mnt/d`のsequential/random read差
- checkpoint保存・読込時間

4090での学習所要時間は公開例から決め打ちせず、このbenchmarkの実測値から計算する。
