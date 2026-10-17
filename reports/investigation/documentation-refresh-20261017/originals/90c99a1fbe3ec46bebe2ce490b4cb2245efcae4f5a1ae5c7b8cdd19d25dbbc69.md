# 先行例とベースライン

更新: 2026-10-14 JST。現在の依頼は全現行文書の最新化と今後の計画作成。Base/Chatは未完成・未採用。研究・教材準備・診断・生成評価・GPU学習は再開していない。

[最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md) / [次の計画145](145_post_rejection_next_plan.md) / [今回更新146](146_documentation_followup.md)。

外部model card/論文は2026-10-02等の調査時点の記録。今回最新revision/規模/利用条件を再調査していない。外部model名の10Mや内部block規模を総trainable予算と混同せず、同条件品質比較は未実施のまま。10M維持、領域/品質維持を前提に、closed比較の機序を原実装まで確認して新案を選ぶ。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

元Base TEST20 promptと元Chat TEST20行は別のCPU解析問題を保存した。学習・GPU TEST採点に使っていないこととCPU未解析は別。将来の有資格最終確認にはreader分離と新しい封印TESTが必要。今回data/TESTを開封・再処理しない。

次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。

## 当時の資料・保存手順

## 添付された25M / 100M Llama系config

**確認済み**: 会話に添付された2つの`config.json`は、いずれも`LlamaForCausalLM`、語彙8,192、context 512、RMSNorm、RoPE、GQA、biasなし、untied embeddingだった。

| 項目 | 25M config | 100M config |
|---|---:|---:|
| 概算parameters | 25,765,248 | 100,685,568 |
| vocab | 8,192 | 8,192 |
| hidden | 384 | 768 |
| layers | 12 | 14 |
| attention heads | 8 | 12 |
| KV heads | 4 | 4 |
| intermediate | 1,024 | 2,048 |
| context | 512 | 512 |
| tied embedding | No | No |

25M版ではinput embedding + LM headが約6.29M、全体の約24%を占める。今回の10Mでは同じuntied設計を使わず、weight tyingで約2.1Mを節約し、depthへ回す。

この2モデルから確認できるのはarchitecture configであり、Tokenizerのアルゴリズム、学習コーパス、training tokens、対話性能まではconfigだけでは証明できない。

## 日本語対応・100M以下の公開生成モデル

調査対象は自己回帰型Text Generation。BERT、Embedding専用、分類、ASRは除外する。公開時期はmodel cardまたはHugging Face上で確認できた時期であり、厳密な初回公開日が不明なものは断定しない。

| モデル | 公開時期 | Params | Architecture / Tokenizer | 学習・特徴 | Chat | License | Link |
|---|---|---:|---|---|---|---|---|
| rinna Japanese GPT-2 xsmall | 2021-08-25 | 43.7M | GPT-2、6層/512、SentencePiece | CC-100 + Wikipedia、8×V100約4日 | Base | MIT | [HF](https://huggingface.co/rinna/japanese-gpt2-xsmall) |
| KU-NLP GPT-2 Small Japanese Char | 2023年公開 | 約90M | GPT-2、character-level | Wikipedia + CC-100 + OSCAR、計171GB、A100 80GBで約3か月 | Base | CC BY-SA 4.0 | [HF](https://huggingface.co/ku-nlp/gpt2-small-japanese-char) |
| zhuojing-huang JP/EN GPT-2群 | 2025〜2026 | 92.9M級 | GPT-2、日英語彙配分比較 | 日本語専用ではなくbilingual研究 | Base中心 | 要確認 | [HF例](https://huggingface.co/zhuojing-huang/gpt2-japanese20k-english10k-configA-1) |
| GeneLab 3LM-MLX系 | 2026年確認 | 35.7M | 6層/512/8head、SP Unigram 32k、RoPE/RMSNorm/SwiGLU、tied | 約367.6M tokens、FineWeb2 + 青空系、SFT派生あり | 派生Chatあり | Apache-2.0 | [HF](https://huggingface.co/GeneLab/3LM-MLX-GAL) |
| HinoMoto-100M-v7 | 2026-04-26 | 100M | Llama-style、12層/512/8head、Byte-BPE 9,506、context 512 | architecture/tokenizer/weights/corpusをscratch構築 | 軽い会話寄り学習あり | Apache-2.0 | [HF](https://huggingface.co/FiShota/hinomoto-100m-v7) |
| makellm-ja-char-75m-chat | 2026年確認 | HF表示82.2M、作者表記約75M | GPT-2、10層/768/12head、文字語彙7,210、context 256 | 約4.8B characters + 39,591会話、assistant-only loss | Chat | CC BY-SA 4.0 | [HF](https://huggingface.co/Sido/makellm-ja-char-75m-chat) |
| Hourai2-50m-base | 2026年確認 | 47.9M | Qwen3Next系 | 日本語Wikipedia 30k rows、RTX 3060約12時間 | Base | Apache-2.0 | [HF](https://huggingface.co/WariHima/hourai2-50m-base) |

### 読み取り

- 100M以下の日本語生成モデルは少なく、特に10〜20M級の公開例は空いている。
- `makellm-ja-char-75m-chat`は「短い自然な雑談は可能だが事実性は期待しない」という目的が近い。
- GeneLabの35.7Mはmodern Transformer + tied embedding + SP Unigramの参考になる。
- rinna/KU-NLPは古典的GPT-2 baselineとして重要。
- HinoMotoは個人GPUでTokenizerから一式を構築するpipelineの参考になる。
- Hourai2は少量計算で最新系architectureを縮小する実験だが、学習量が小さく性能上限とはみなさない。

## 海外10M級ベースライン

| モデル | Params | 構成 | Training | 用途 | Link |
|---|---:|---|---:|---|---|
| Ant-10M | 9.9M | Llama-style、12層、hidden 256、4Q/2KV、vocab 4,096、tied | 約2.98B tokens、T4で約9.63時間と報告 | JMicro-T4Kに近いTransformer比較 | [HF](https://huggingface.co/GODELEV/Ant-10M) |
| Pebble-10M | HF表示11.1M | 6 Mamba2 + 2 Attention、hidden 384、vocab 2,048 | 約25B tokens | Hybrid候補、custom runtime依存の比較 | [HF](https://huggingface.co/basically-ai/Pebble-10M) |

## 参考研究

- [MobileLLM](https://arxiv.org/abs/2402.14905): deep-thin、embedding sharing、GQA、block sharing。
- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388): GQA、SwiGLU、RoPE、RMSNorm、QK-Norm、段階的pretraining。
- [Mamba-2](https://arxiv.org/abs/2405.21060): structured state space dualityと効率的sequence modeling。
- [LFM2 Technical Report](https://arxiv.org/abs/2511.23404): gated short convolution + GQA、edge hardwareを意識した探索。

## 情報の扱い

モデルカードの自己申告、Hugging Faceの表示parameter数、論文の査読済み結果は区別する。実装へ採用する値は、可能ならweights/config/source codeを再確認し、比較表へ確認日とcommit hashを追加する。
