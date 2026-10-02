# 次の実装タスク

## Phase 0: リポジトリと環境

1. WSL、Ubuntu、NVIDIA driver、CUDA、PyTorch、Python、`torch.compile`の実versionを記録する。
2. `src/`、`configs/`、`tests/`、`scripts/`、`data/`の骨格を作る。
3. run configとartifact naming規則を決める。
4. synthetic batchでRTX 4090のthroughput benchmarkを作る。

追加調査の参照: [QK-Norm・precision・cache・benchmark仕様](12_training_implementation_research.md)。正確な依存versionと採用commitを固定し、micro batchとeffective batchを別に記録する。

完了条件: 同じconfigから同じ小モデルを構築し、forward/backward、save/loadが動く。

## Phase 1: データmanifest

1. source、subset、license、URL、hash、quality scoreを持つschemaを決める。
2. `commercial_strict`、`commercial_web`、`sharealike`を分離する。
3. FineWeb2 Edu Japaneseの10B sampleを最初の候補として取得計画へ入れる。
4. validationをdocument単位で先に固定する。

完了条件: 任意のdocumentが出所・ライセンス・splitまで追跡できる。

## Phase 2: Tokenizer 4k / 8k

1. Tokenizer学習用sample mixtureを作る。
2. SentencePiece Unigram + byte fallbackを4k/8kで学習する。
3. 特殊token IDを固定する。
4. round-trip、byte fallback、特殊token、異常Unicodeのテストを書く。
5. domain別chars/token、bytes/token reportを生成する。

完了条件: 同一sampleから再現可能な4k/8k artifactと比較reportが得られる。

## Phase 3: Modern Transformer

1. RMSNorm、RoPE、GQA、QK-Norm、SwiGLU、block、modelを小単位で実装する。
2. causal mask、GQA mapping、tied embedding、parameter countのテストを書く。
3. KV cacheとcached/non-cached一致テストを書く。
4. T4KとT8K configを作る。

完了条件: T4K約10.00M、T8K約9.77Mで全unit testが通る（head間gain共有のQK-Norm案）。

**提案（追加gate）**: head間gain共有のQK-NormならT4K 10,002,816、T8K 9,772,800を期待値にする。本学習前にランダム重みでHF／float GGUFのtoken IDs・logits一致と量子化fallbackを確認する。[計算式](12_training_implementation_research.md)、[export gate](14_evaluation_deployment_research.md)

## Phase 4: DataLoaderとcheckpoint

1. `uint16` shard writerとmemory-mapped loaderを作る。
2. shard boundary、shuffle、data position resumeをテストする。
3. model、optimizer、scheduler、RNG、data offset、hashを保存する。
4. 100 step save/resume equivalence testを作る。

完了条件: 中断後に同じtoken位置から再開し、連続runと一致する。

## Phase 5: Smokeと100M探索

1. 小データ100件をoverfitする。
2. 10M-token smoke runを実施する。
3. 100M tokensで4k/8k、QK-Norm、LRを比較する。
4. AdamW baseline後にMuon+AdamWを比較する。
5. BPB、repetition、EOS、throughputをreport化する。

完了条件: 発散せず、比較表から1Bへ進める候補を最大2つ選べる。

## Phase 6: Scaling

1. 1Bで候補を絞る。
2. 2Bで過去モデルとの観察点を記録する。
3. 5Bで本命を1つ決定する。
4. 10Bで`JMicro-10M-Base-v1`を固定評価する。
5. 20Bで`Base-v2`を評価する。
6. 改善が続く場合のみ50Bへ進む。

## Phase 7: Chat

1. Dialogue-oriented mid-training mixtureを作る。
2. 10M/30M/100M dialogue-token SFTを比較する。
3. Assistant-only lossを検証する。
4. 固定100〜500 promptで人手・自動評価する。
5. `JMicro-10M-Chat`を作る。

## Phase 8: 追加研究

優先順:

1. Layer Sharing 12 unique / 24 logical
2. teacher distillation
3. ReLU²
4. Mamba2 + Attention hybrid
5. LFM2風Conv + Attention
6. 5M/10M/25M/50M/100M scaling
7. Vast.aiで独立runを並列化

## 最初に実装する最小単位

```text
環境情報採取
  -> Tokenizerの最小sample
  -> 正規化・特殊token・4k/8k語彙予算の検証
  -> T8K model
  -> unit tests
  -> ランダム重みでHF/GGUF exportとcache一致確認
  -> synthetic benchmark
  -> 100件overfit
  -> save/resume test
  -> 10M-token smoke
```

この最小単位が安定してから、巨大datasetのdownloadと50〜100B master corpus構築へ進む。

未解決事項と優先順位の全体表は[追加技術調査](11_technical_research_gaps.md)を参照する。会話データ候補の取得・pilotは[Tokenizer・会話データ調査](13_tokenizer_dialogue_data_research.md)に沿って進める。実測待ちの項目を文献確認済みとして扱わない。
