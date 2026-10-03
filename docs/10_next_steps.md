# 次の実装タスク

Phase 6①②の準備を実行中（2026-10-03）: train 756,087,912 unique stream tokensの拡張shardとWSD stable/decay CLI・CUDA全state再開一致を検証。全corpusの独立監査は進行中。③以降の速度/batch探索・本学習は未開始。

この文書は[フェーズ別実行計画](15_project_roadmap.md)の着手checklistである。Phase番号、目的、ゴール、成果物、完了条件、Go/No-Goは同計画を正とし、技術仕様は03〜08と12〜14を参照する。2026-10-02にiMac上のPhase 0を実施した。[完了記録](16_phase0_completion.md)を参照する。Phase 1のcorpus・manifest・split・会話pilotも完了した。[完了記録](17_phase1_completion.md)を参照する。[Phase 2](18_phase2_completion.md)・[Phase 3](19_phase3_completion.md)も完了。本学習は未実施。Windows/WSL実機検証は[Phase 4](21_phase4_completion.md)で完了した。

**現在の境界**: [Phase 5](23_phase5_completion.md)は完了し、Phase 6①②の準備を実行中。今回の①②でcorpusとWSDを準備し、容量/高速化探索は次回へ残す。Phase 4の学習器・評価・保存再開・最大安定batchは完了済み。Pythonは`uv run --frozen`、依存変更は`uv add`。

完成までの時間短縮を優先し、[移行 → 最小学習経路 → 保存再開 → 最大batch/速度実測](15_project_roadmap.md#高速に完成させる進め方)を完了した。新規PCでは[再開手順](windows_handoff.md)に従い、最新コードとGit管理外の固定Tokenizer/pilotを引き継ぐ。復元済みPCでは再取得・Phase 3の再実装は不要。実装時間とGPU計算時間を分け、実測した計算時間に評価・保存・比較・データ処理を加えて見積もる。

## Phase 0: 成功条件・環境・実験管理

- [x] `src/`、`configs/`、`tests/`、`scripts/`と実験台帳の骨格を作る。
- [x] iMac環境とuv管理の依存設定を記録し、Windows/WSL 3.x/Linuxへの移行手順を用意する（GPU実機記録はPhase 4）。
- [x] run/config/artifact schemaとhash記録を決める。
- [x] Base/Chat各100件の独自固定prompt、dev/test、rubric、generation条件、数値誤差の仕様を作る。

## Phase 1: 小規模データと会話pilot

- [x] FineWeb2 Edu JapaneseとRealPersonaChatの候補revision・配布条件・形式を確認し、調査metadataを保存する。
- [x] `uv add --optional data`でデータ処理用依存を登録し、lockする。
- [x] source台帳とdocument/dialogue manifest schemaを作る。
- [x] source/subset/revision・利用条件の証拠を台帳へ固定し、取得範囲・容量上限・保存先をconfigで決める。
- [x] 固定revisionから小規模本文データを取得する（Web20,000文書・会話3,000対話を取得、Web19,998文書と会話全件を採用）。
- [x] 小sampleへraw/canonical hash、品質、duplicate cluster、splitのmanifestを付ける。
- [x] FineWeb2 Edu Japanese等の小subsetをfilter/dedupし、cluster単位のsplitを固定する。
- [x] Tokenizer学習用sampleをtrainから作る。
- [x] 会話候補1k〜10k対話でspeaker/tree/品質と文字ベースの会話長を確認する（1024-token内の割合はPhase 2）。

## Phase 2: Tokenizer 4k/8k

[完了](18_phase2_completion.md)。同じsample、固定語彙数、全corpus round-tripと会話window教師計数を検証した。

- [x] 同じsampleでSentencePiece Unigram + byte fallbackを4096/8192語彙で学習する。
- [x] 正規化、空白/改行、特殊IDと本文/構造IDの区別をgolden例で検証する。
- [x] domain別圧縮率、fallback率、1024超過率を比較する。
- [x] 会話のunique量、総系列tokens、Assistant教師tokensを再計数する。

## Phase 3: Transformer・cache・学習前export

[完了](19_phase3_completion.md)。両実モデル、HFとnative float GGUF、Q8/Q4候補を検証した。

- [x] T8Kから実装し、RMSNorm/RoPE/GQA/QK-Norm/SwiGLU/tied embeddingを検証する。
- [x] T4Kへ展開し、parameter countがT8K 9,772,800、T4K 10,002,816であることを確認する（head間gain共有QK-Norm案）。
- [x] causal mask、padding、finite gradient、prefill/1-token/chunk cache一致を検証する。
- [x] ランダム重みでHF/float GGUF logitsとTokenizer契約を別々に確認する。
- [x] 必要なら外部SentencePiece経路を実装し、EOT停止と量子化型fallbackを確認する。

## Phase 4: 学習器・再開・4090実測

- [x] iMacから別のWindows＋RTX 4090 PCへ切り替え、WSL 3.x/Linuxで同じconfig/Tokenizer/sampleを復元する。
- [x] 実WSL version、distribution実行方式、GPU/driver、PyTorch/CUDAを記録し、hash/ID一致とCUDA動作を確認する。
- [x] `uint16` shards、document index、mmap loaderと消費済み位置の保存を作る。
- [x] AdamW/BF16 autocast、gradient accumulation、scheduler、checkpointを実装する。
- [x] 準備runから学習runへschema/台帳を拡張し、実際のtokens/steps、checkpoint、完了/失敗を記録する。
- [x] 本文NLL、window/stride、BPBとBase生成suiteのrunnerを実装・検証する。
- [x] 連続200 stepsと100 steps→保存→再開100 stepsのtoken列/loss/weightsを比較する。
- [x] syntheticと実shardでeager micro batchを最大安定値まで増やし、backend/compile、VRAM、data wait、速度を測る。
- [x] 100M〜50Bの時間とストレージを実測から見積もる。

[Phase 4実測・制約](21_phase4_completion.md)。Phase 5も完了し、Phase 6①②の準備を実行中。

## Phase 5: 最小pipelineと100M探索

- [x] 100件overfit、10M-token smokeで学習・生成・保存再開を一周する（機械的gateに合格、停止・反復の品質未達はstatusへ記録）。
- [x] 100Mで4k/8k、QK-Norm、LRを一要因ずつ比較する。
- [x] Muon追加の必要性を判断する（AdamW全4比較が安定・改善し候補を選べたため、今回は追加しない）。
- [x] BPB、処理bytes/GPU時間、更新数、生成失敗を比較し、T4K / NoQK-Norm / LR 0.002の1候補を選定する。
- [x] dev/pilotを使い、品質閾値を最終test評価前に固定する（数値を維持し、100M結果前にtargets.statusをfrozenへ変更）。

## Phase 6: 1B〜10B Base v1

[詳細計画と開始条件](24_phase6_plan.md)。以下は次回再開後の作業で、現在はPhase 6①②の準備を実行中。

- [ ] 拡張corpusのsource/revision/取得上限・unique量・配合・反復、held-out評価を固定する。
- [ ] WSD stable/decay分岐を実装し、採用構成で全stateの保存再開を検証する。
- [ ] math/compiled-math等の最大安定batch・速度・厳密resumeを測り、本学習effective batch/LR/予算を凍結する。
- [ ] NoNormのUnicode・反復・自発停止と変換経路を切り分け、固定devで修正/対照を評価する。
- [ ] 実CLI/restart command、永続log/PID/boot/start ticks/checkpoint SHA、枝computeと容量上限を保存する。

- [ ] 500M/1B/2Bで段階評価し、5Bまでに本命1モデルを決める。
- [ ] 検証済みのデータ処理を拡張し、50〜100B master corpus候補を段階整備する。
- [ ] 固定mixture系列と変更系列、継続stable枝と評価decay枝を区別する。
- [ ] 10B Base v1のartifactと固定評価を作り、日本語短文の達成/未達を記録する。

## Phase 7: Chat v1

- [ ] Dialogue mid-trainingのconfig/予算を固定し、Base→SFTの小対照も残す。
- [ ] Assistant本文+EOTのmask、shift、教師0件、turn単位の切り捨てを検証する。
- [ ] SFT累積総系列10M/30M/100M候補を比較し、教師tokens/unique量/反復を併記する。
- [ ] 固定対話で関連性、2〜数ターンの文脈、停止、反復、role、Unicodeを評価する。
- [ ] 固定履歴とは別にモデル生成を戻す複数turn rollout、自動失敗flag、人手評価・一致率を用意する。
- [ ] devで選んだChat v1を独立testで評価する。

## Phase 8: 量子化とローカル実行

- [ ] 学習済みBase/ChatでHF/float GGUF parityと停止を再確認する。
- [ ] Q8/Q4の品質差、tensor実型、weights/全artifact容量、RSS、CPU応答時間を測る。
- [ ] model card、hash、source/帰属、依存、再現/推論手順を揃える。
- [ ] 独立環境でBase completionとChatを起動し、容量/品質目標の達成を確認する。

## Phase 9: 20Bと条件付き50B

- [ ] 20B Base v2を評価し、10Bとの差・信頼区間・追加予算を報告する。
- [ ] 改善継続と予算が成立する場合のみ50Bへ進む。
- [ ] 新BaseをChatへ採用する場合は同じSFT/量子化/配布検証を再実行する。

## Phase 10: 後半研究

- [ ] Layer Sharing、テキスト蒸留、ReLU²、Mamba2/Conv hybrid、規模比較を優先順に検討する。
- [ ] 各proposalで対照条件、改善metric、compute予算、採用基準を先に決める。
- [ ] Vast.aiはローカル検証済みの独立run並列化に限定し、利用時に再見積もりする。

## 完了した最初の一周と次回の境界

```text
Phase 0〜4: データ / Tokenizer / モデル / export / 学習器 / 評価 / GPU再開・実測は完了
  -> Phase 5は完了、Phase 6①②の準備を実行中
  -> 100件overfit / 10M-token smokeは合格
  -> T4K/T8K・Norm・LRの100M比較、補助評価、候補選定も完了
  -> 次回の再開指定後: 拡張corpus / WSD / 容量・高速化の検証
```

この一周は完了した。ユーザーのPhase 6再開指定後に、大規模データ処理と本系列へ進む。会話pilot・評価準備は早期から並行する。具体的な未解決事項と根拠は[追加技術調査](11_technical_research_gaps.md)、会話データは[Tokenizer・会話データ調査](13_tokenizer_dialogue_data_research.md)、推論経路は[評価・配布調査](14_evaluation_deployment_research.md)を参照する。
