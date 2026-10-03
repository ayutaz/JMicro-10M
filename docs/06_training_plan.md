# 学習計画

Phase 6①②完了（2026-10-03）: train 756,087,912 unique stream tokensの拡張shardとWSD stable/decay CLI・CUDA全state再開一致を検証。全corpus・shardの独立監査も完了。③以降の速度/batch探索・本学習は未開始。

最終更新: 2026-10-03。AdamW＋warmup/cosine・WSD stable/decayは実装済み。Phase 6の長期schedulerはWSDを採用し、stable/decayは実装・CUDA検証済み。Muon・Chat trainerは未実装。train CLIは引数から設定を作り、baseline JSONを自動読込しない。現在のresumeは固定schedule/config/source/dataの変更を拒否するため、予算の延長を同一runの再開として扱わない。50Bは改善と予算条件を満たした場合のみ、外部の有料GPU実行は別途ユーザーの指示が必要。

## 全体像

次回の具体的な準備順・開始条件・段階ごとの判断は[Phase 6計画](24_phase6_plan.md)を参照する。現在の選定候補は1つで、未凍結の長期WSD配分や未測定の本学習batchを確定設定として実行しない。

プロジェクト全体の目的・ゴール・成果物・完了条件は[フェーズ別実行計画](15_project_roadmap.md)を参照する。本書は学習系列の設定とcheckpoint段階を扱う。10B BaseからChatへ分岐し、20B/50Bの終了をChat着手の前提にしない。

**現在地（2026-10-03）**: Phase 0〜5が完了。WSL＋RTX 4090で学習器・shard・BPB/生成評価・保存再開・最大安定batchを検証した。Phase 5のoverfit/smoke・4本の100M比較と独立監査も完了し、T4K / NoQK-Norm / LR 0.002を候補に選定した。Phase 6①②完了で停止中（③以降未開始）。smokeはdev BPBが改善したが、抑制ありgreedy EOS 0/80・反復63/80で、本学習・Base/Chat品質目標は未達。実装時間とGPU計算時間を分け、採用したmath-only/batch 8の実測から予算を見積もる。[詳細計画](22_phase5_plan.md)、[進め方](15_project_roadmap.md#高速に完成させる進め方)

```text
Tokenizer 4k / 8k・Phase 4実測は完了
        -> 100件overfit（合格）
        -> 10M-token smoke（合格）
        -> 100M T4K/T8K・Norm・LR比較（完了、Muon追加不要）
        -> Phase 6①②完了で停止中（③以降未開始）
        -> 再開後: 拡張corpus / WSD分岐・再開 / 容量・高速化 / 予算凍結
        -> 500M / 1B 選定候補の日本語生成と継続価値を評価
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

**Phase 5の決定**: AdamW、LR 0.002を本学習候補へ採用。LR 0.001は同一構成でBPB悪化、0.003は追加せず、Muonは安定したAdamWで候補を選べたため保留。batch/corpus変更後の安定性と長期最適性は未実証で、次回の準備で確認する。

**当初の比較案**:

- baselineはAdamW
- modern比較は2D hidden weightsへMuon、embedding/norm/scalarへAdamW
- 100M-token runでpeak LR `1e-3`, `2e-3`, `3e-3`程度を小さくsweep
- warmup、cosine decay、weight decay、gradient clippingをconfigへ明記
- validation BPB、gradient norm、loss curve、tokens/secで決める

最初からarchitecture、optimizer、data mixtureを同時に変えない。一度に一つの主要因を比較する。

**Phase 5での判断**: 小探索は終点固定cosine、本系列はWSDを採用する方針。継続用stable枝と評価用decay枝を分け、optimizer更新回数、effective batch、枝ごとのtokensとGPU時間を記録する。WSD実装・分岐のCUDA再開検証は①②で完了。長期の数値予算は③以降の測定後に凍結する。Phase 5の100M終点を予算だけ変更して延長しない。[詳細計画](22_phase5_plan.md#長期schedulerの選択と引継ぎ)、[実装・段階学習調査](12_training_implementation_research.md)を参照する。

## Batchとperformance

**確定**: Phase 0〜3のiMac開発からWindows/WSL＋RTX 4090へ移行済み。本学習は最大安定micro batchを実測して設定する。Phase 4のeager/defaultの運用上限はT8K 57 / T4K 64、最高速度の測定点はcompile/default batch 8。Phase 5は厳密resumeのためeager/math、batch 8を採用し、100Mで約12,208更新を確保する。math backendの最大容量は未探索で、本学習前に別途測定する。[移行・batch方針](07_environment.md)

**提案**: RTX 4090ではmodelを載せるためでなく、大きなbatchでGPUを埋めるために24GB VRAMを使う。micro batchを16、32、64、128、256…と増やし、以下を実測する。

- tokens/sec
- GPU utilization
- VRAM usage
- step time
- MFU
- data wait time

OOM境界付近は中間値を試し、loss/backward/optimizerと実shardの運用まで含めて最大安定値を確認する。gradient accumulation後のeffective batch、LR、warmup、更新回数は別に管理する。小探索でbatchを小さくする場合は比較目的と理由をconfig/台帳へ残す。

BF16、default/math SDPA、torch.compile/defaultを実機検証した。Flash-onlyは明示mask非対応で失敗し、現時点の採用経路には含めない。10MモデルではPython overhead、kernel launch、DataLoaderがbottleneckになりやすい。

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

**確定**: 初期のTokenizer学習とモデル実装・CPU検証はiMacで完了。学習器・GPU検証はローカルRTX 4090で完了した。今後の100M〜20B、Dialogue SFTもローカルで進める。

Vast.aiは後半に限定する。

- 4k/8k × 複数architectureの並列化
- 5M/10M/25M/50M/100M scaling比較
- Transformer/Layer Sharing/Mamba/Conv hybridの並列run
- ローカルで有望と判明した設定の再現run

過去会話での上限予算は$1,000だが、価格は変動するため利用時に再見積もりする。目的は「単一runを外へ移す」ことではなく「独立実験を並列化する」こととする。
