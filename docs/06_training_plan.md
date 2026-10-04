# 学習計画

最終更新: 2026-10-04。主要Web5Bと同じ5B親から各100MのWeb/短文仕上げ比較は完了。trainは12,225,819,077 tokens、モデルは10,001,152 parameters。直接10Bの準備・本学習・CPU保存確認19項目は完了、品質評価は未開始。[学習結果と速度](41_base_10b_training.md)。[現在地](autonomous_status.md)、[直接10B計画](39_learning_scale_and_generation_plan.md)を実行値の正本とする。

AdamW、warmup/cosine、WSD stable/decay、stable予算の明示forkは実装済み。Muon・Chat trainerは未実装。通常resumeでは固定schedule/config/source/dataの変更を拒否するため、予算延長を同一runの再開として扱わない。依存変更はuv add、すべてのPythonはuv run --frozen、WSL/Linux dataを使用する。

## 全体像

Phase 0〜5とPhase 6①〜⑤、5B主系列、各100M仕上げ、10B準備まで完了。本文BPBは改善したが、自然停止、反復、意味と文字の問題が残り、Base/Chat品質目標は未達。短文20%は固定EOS13/80へ改善したがraw Unicode失敗2/400で採用不合格だった。

```text
Tokenizer・モデル・GPU学習器・保存再開・候補選定（完了）
  -> train12.23B利用準備（独立全corpus監査は未完了）
  -> 主要Web5B / 同じ親から各100M仕上げ（完了）
  -> 直接10B専用設定・CUDA保存再開（準備完了）
  -> stable4.75B親から9.5B -> 独立decay -> 総10B（学習・保存確認完了）
  -> 同じ全文dev/400生成比較 -> 報告・commitと停止
  -> 結果に応じEOS仕上げ / 別UTF8推論方式を判断
  -> Base品質判定 -> Dialogue/SFT -> Chat -> 量子化/独立ローカル検証
  -> 実測改善・予算条件を満たす場合だけ20B/50B
```

現在の10B実行値は[専用config](../configs/phase6/base_10b.json)。従来のbase_frozen.jsonは歴史的主系列設定として保持する。準備済みpoolで足りるため追加収集を先行せず、7.5B専用のdecay・評価を省く。学習区間約126分、評価込み145〜165分の見積もり。科学学習上限9,000秒（準備19.217秒を含む）、評価予約1,800秒、実装・内容確認は別。今回はユーザー指定step2のGPU学習を実行し、総10Bと保存結果確認・report/commitで停止する。品質評価は未実施の後続step3。

[roadmap](15_project_roadmap.md)の品質条件と[残る作業](27_phase6_remaining_plan.md)を維持する。10Bという到達量だけでBase完成とせず、Chat開始に20B/50B完了を要求しない。

## Checkpoint段階

当初の段階設計を以下に残す。100M〜5Bと仕上げの実績はstatusを参照。次は直接10Bで比較し、7.5B専用枝を追加しない。20B/50Bは条件付きの将来計画。

| 段階 | 目的 | Go/No-Go |
|---:|---|---|
| 10M | pipeline、loss低下、生成、保存再開 | overfit/smokeが通る |
| 100M | 4k/8k、QK-Norm、LR、optimizer比較 | 発散せずBPB改善 |
| 500M | early scaling確認 | repetitionが悪化しない |
| 1B | 日本語生成の立ち上がり | 現在の1候補を継続。対照追加は理由・予算を固定し最大2つ |
| 2B | 過去の約2B-token経験との比較 | 継続価値を判定 |
| 5B | 本命architecture決定 | 1モデルへ集約 |
| 10B | Base v1候補の固定評価 | artifact保存と品質の達成/未達を別に判定 |
| 20B | Base v2、本命 | 10Bとの差を統計比較 |
| 50B | 過学習/容量限界の研究 | 20Bでも改善時のみ |

## Optimizerとlearning rate

**Phase 5の決定**: AdamW、LR 0.002を本学習候補へ採用。LR 0.001は同一構成でBPB悪化、0.003は追加せず、Muonは安定したAdamWで候補を選べたため保留。変更後のbatch/corpusでは5Bと100M仕上げが有限値で完了し、10Bの保存再開準備も通過した。全長期予算でLRが最適とは断定しない。

**当初の比較案**:

- baselineはAdamW
- modern比較は2D hidden weightsへMuon、embedding/norm/scalarへAdamW
- 100M-token runでpeak LR `1e-3`, `2e-3`, `3e-3`程度を小さくsweep
- warmup、cosine decay、weight decay、gradient clippingをconfigへ明記
- validation BPB、gradient norm、loss curve、tokens/secで決める

最初からarchitecture、optimizer、data mixtureを同時に変えない。一度に一つの主要因を比較する。

**Phase 5での判断**: 小探索は終点固定cosine、本系列はWSDを採用する方針。継続用stable枝と評価用decay枝を分け、optimizer更新回数、effective batch、枝ごとのtokensとGPU時間を記録する。WSD実装・分岐のCUDA再開検証は①②で完了。③の速度・容量測定は完了。④⑤の診断・安定性確認と主系列凍結は完了し、現在の直接10B値は専用configへ凍結済み。Phase 5の100M終点を予算だけ変更して延長しない。[詳細計画](22_phase5_plan.md#長期schedulerの選択と引継ぎ)、[実装・段階学習調査](12_training_implementation_research.md)を参照する。

## Batchとperformance

**確定**: Phase 0〜3のiMac開発からWindows/WSL＋RTX 4090へ移行済み。本学習は容量上限と速度を測り、厳密再開を通過した最速micro batchを候補にする。Phase 4のeager/defaultの運用上限はT8K 57 / T4K 64、最高速度の測定点はcompile/default batch 8。Phase 5は厳密resumeのためeager/math、batch 8を採用し、100Mで約12,208更新を確保する。③でreference/math最大45、compiled/math最大53、compiled Flash最大111を検証し、最速のFlash＋compile reduce-overhead batch 32を採用した。32,768 input tokens/updateで、長期LR0.002/WSDは⑤でversion2へ凍結済み。[③の実測](29_phase6_performance_completion.md)。[移行・batch方針](07_environment.md)

**③で実施済み**: RTX 4090でmicro batchを倍増・境界探索し、容量上限と最高速度を別に確認した。batch 111のdriver peakは97.64%、batch 32の速度が最も高く、運用候補は32を選択した。以下の観測値をreportに保存した。

- tokens/sec
- GPU utilization
- VRAM usage
- step time
- GPU使用率の時系列（MFUは未測定で別項目）
- data wait time

OOM境界付近は中間値を試し、loss/backward/optimizerと実shardの運用まで含めて最大安定値を確認する。gradient accumulation後のeffective batch、LR、warmup、更新回数は別に管理する。小探索でbatchを小さくする場合は比較目的と理由をconfig/台帳へ残す。

Phase 4〜5のFlash-only/mask失敗は保持した。③で固定長・PADなし学習専用のmaskなしcausal経路とbackend別compile cacheを実装し、Flash＋reduce-overheadを実GPU検証した。選択設定のdata waitは0.55%。最大安定容量と最速設定は各3×200・保存/小sample評価・厳密再開を通過し、採用設定のcold-cache再開も完全一致。推論/cacheには従来の明示mask経路を使う。

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

**確定**: 初期のTokenizer学習とモデル実装・CPU検証はiMacで完了。学習器・GPU検証はローカルRTX 4090で完了した。10B学習はローカルで完了し、将来のDialogue SFTもローカルで進める。20Bは改善・実測予算条件を満たす場合だけ判断する。

Vast.aiは後半に限定する。

- 4k/8k × 複数architectureの並列化
- 5M/10M/25M/50M/100M scaling比較
- Transformer/Layer Sharing/Mamba/Conv hybridの並列run
- ローカルで有望と判明した設定の再現run

過去会話での上限予算は$1,000だが、価格は変動するため利用時に再見積もりする。目的は「単一runを外へ移す」ことではなく「独立実験を並列化する」こととする。

WSD stable予算の明示延長forkはStableExtensionTrainerで実装済み、直接10B準備の全state保存再開検証も完了。通常resumeでは終端budget・source・dataを変更できない。20B/50Bやmixture変更には新しい凍結条件・履歴・対応する厳密再開検証が必要。[継続の契約](27_phase6_remaining_plan.md)
