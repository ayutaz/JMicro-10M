# 学習計画

## 全体像

プロジェクト全体の目的・ゴール・成果物・完了条件は[フェーズ別実行計画](15_project_roadmap.md)を参照する。本書は学習系列の設定とcheckpoint段階を扱う。10B BaseからChatへ分岐し、20B/50Bの終了をChat着手の前提にしない。

**現在地（2026-10-02）**: 4k/8k Tokenizerと両モデル/cache/HF/native GGUFのPhase 3まで完了。本学習は未実施。次はWindows/WSL＋RTX 4090上のPhase 4で学習器・shard・評価runner・保存再開・最大安定batchを検証する。完成までの時間短縮を優先し、実装時間とGPU計算時間を分けて実測から見積もる。[進め方](15_project_roadmap.md#高速に完成させる進め方)

```text
Tokenizer 4k / 8k
        -> 10M-token smoke
        -> 100M architecture/LR/optimizer比較
        -> 1B 候補を絞る
        -> 2B 過去355Mモデルとの比較点
        -> 5B 本命を1つに決定
        -> 10B Base v1
             |-> Dialogue mid-training -> SFT -> Chat v1 -> 量子化/ローカル実行
             |-> 20B Base v2 -> 改善継続時のみ50B
                   -> 有望なら同じChat手順で再比較
```

## Checkpoint段階

**確定**: 少なくとも100M、500M、1B、2B、5B、10B、20B、50B tokensで保存する。10M-token smokeは本番系列とは分けてもよい。

| 段階 | 目的 | Go/No-Go |
|---:|---|---|
| 10M | pipeline、loss低下、生成、保存再開 | overfit/smokeが通る |
| 100M | 4k/8k、QK-Norm、LR、optimizer比較 | 発散せずBPB改善 |
| 500M | early scaling確認 | repetitionが悪化しない |
| 1B | 日本語生成の立ち上がり | 候補を最大2つへ |
| 2B | 過去の約2B-token経験との比較 | 継続価値を判定 |
| 5B | 本命architecture決定 | 1モデルへ集約 |
| 10B | Base v1完成 | 固定評価とartifact保存 |
| 20B | Base v2、本命 | 10Bとの差を統計比較 |
| 50B | 過学習/容量限界の研究 | 20Bでも改善時のみ |

## Optimizerとlearning rate

**提案**:

- baselineはAdamW
- modern比較は2D hidden weightsへMuon、embedding/norm/scalarへAdamW
- 100M-token runでpeak LR `1e-3`, `2e-3`, `3e-3`程度を小さくsweep
- warmup、cosine decay、weight decay、gradient clippingをconfigへ明記
- validation BPB、gradient norm、loss curve、tokens/secで決める

最初からarchitecture、optimizer、data mixtureを同時に変えない。一度に一つの主要因を比較する。

**提案（追加調査）**: 小探索は終点固定cosine、本系列の延長はWSDを比較候補にする。継続用stable枝と評価用decay枝を分け、optimizer更新回数、effective batch、枝ごとのtokensとGPU時間を記録する。Muonには補助AdamWと別LRを設定する。[実装・段階学習調査](12_training_implementation_research.md)を参照する。

## Batchとperformance

**確定**: 設計・実装は現在のiMacで進め、学習時は別のWindows PCのRTX 4090へ切り替え、ユーザー指定WSL 3.x上のLinuxで実行する。本学習は24GB VRAMを最大限使う最大安定micro batchを実測して設定する。[移行・batch方針](07_environment.md)

**提案**: RTX 4090ではmodelを載せるためでなく、大きなbatchでGPUを埋めるために24GB VRAMを使う。micro batchを16、32、64、128、256…と増やし、以下を実測する。

- tokens/sec
- GPU utilization
- VRAM usage
- step time
- MFU
- data wait time

OOM境界付近は中間値を試し、loss/backward/optimizerと実shardの運用まで含めて最大安定値を確認する。gradient accumulation後のeffective batch、LR、warmup、更新回数は別に管理する。小探索でbatchを小さくする場合は比較目的と理由をconfig/台帳へ残す。

`torch.compile`、PyTorch SDPA/FlashAttention、BF16を基準にする。10MモデルではPython overhead、kernel launch、DataLoaderがbottleneckになりやすい。

## Dialogue mid-trainingとSFT

**確定**: Chat版はBase完成後に作る。

形式案:

```text
<|user|>
今日は仕事疲れた
<|eot|>
<|assistant|>
お疲れさま。今日は忙しかった？
<|eot|>
```

**提案**: SFTは10M、30M、100M dialogue tokensを比較し、lossはAssistant部分だけへ適用する。過剰なinstruction tuningでBaseの日本語流暢性を崩さないか確認する。

**提案（追加調査）**: 上記tokensは累積学習量であり、uniqueデータ量とは区別する。総系列tokensとAssistant教師tokensを両方記録し、Assistant本文直後のEOTも教師対象とする。データ候補、role割当、maskのshift、反復回数の扱いは[会話データ・SFT調査](13_tokenizer_dialogue_data_research.md)を参照する。

## Distillation

**提案**: scratch pretrainingのbaselineを先に完成し、その後teacher logitsまたは高品質synthetic responseによるdistillationを比較する。Distillationを使ってもstudent weightsがrandom initializationから学習される点は変わらないが、「純粋なcorpus-only scratch」とは結果を分けて報告する。

## Vast.ai

**確定**: 初期のTokenizer学習とモデル実装・CPU検証はiMacで完了。今後の学習器・GPU検証、100M〜20B、Dialogue SFTはローカルRTX 4090で進める。

Vast.aiは後半に限定する。

- 4k/8k × 複数architectureの並列化
- 5M/10M/25M/50M/100M scaling比較
- Transformer/Layer Sharing/Mamba/Conv hybridの並列run
- ローカルで有望と判明した設定の再現run

過去会話での上限予算は$1,000だが、価格は変動するため利用時に再見積もりする。目的は「単一runを外へ移す」ことではなく「独立実験を並列化する」こととする。
