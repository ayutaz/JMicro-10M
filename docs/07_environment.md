# 実行環境とデータ配置

## 前提

**確定**:

- Windows PC
- RTX 4090 24GBを常時利用可能
- WSL上のLinux環境で学習
- 約8TBのローカルストレージ

WSLの実version、Ubuntu、CUDA、PyTorchの組合せは実装開始時に実機で記録する。会話中の「WSL 3.x」は目標環境であり、ドキュメントだけで導入済みとみなさない。

**確認済み（追加調査）**: CUDAの公式手順はWSL 2の実行環境を対象とする。WSLパッケージのversionとdistributionのWSL 1／2は別に記録する。Windows側NVIDIA driverを利用し、WSL内へLinux GPU driverを別途入れない。[NVIDIA公式手順](https://docs.nvidia.com/cuda/wsl-user-guide/)、[benchmark・環境記録案](12_training_implementation_research.md)

## 推奨stack

**提案**:

```text
Windows 11
  -> WSL / Ubuntu
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
