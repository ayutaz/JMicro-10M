# 未解決の技術課題と追加調査

更新: 2026-10-14 JST。現在の依頼は全現行文書の最新化と今後の計画作成。Base/Chatは未完成・未採用。研究・教材準備・診断・生成評価・GPU学習は再開していない。

[最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md) / [次の計画145](145_post_rejection_next_plan.md) / [今回更新146](146_documentation_followup.md)。

現在の優先課題は、混在DEV/TEST readerの修理、未回答の比較の選定、真にfreshな独立Base全pipeline、native fullDEV/TEST typed接続、全内容レビューの証拠。文書長重みは一貫性2→1/80・反復45→50/80で不採用。データ/目的/最適化の単独原因は未確定。CPU fixturesや準備済みfactoryを品質・独立学習の完了にしない。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

元Base TEST20 promptと元Chat TEST20行は別のCPU解析問題を保存した。学習・GPU TEST採点に使っていないこととCPU未解析は別。将来の有資格最終確認にはreader分離と新しい封印TESTが必要。今回data/TESTを開封・再処理しない。

次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。

## 当時の資料・保存手順

## 結論

**提案**: Transformer、4k/8k、段階学習という大方針を維持し、まずTokenizerの入出力仕様、評価条件、保存・再開、推論形式を固める。10Mの日本語雑談能力は未実証であり、新しい構成を増やすより、短い会話に合ったデータと測定方法を先に用意する。

2026-10-02の調査部分は文献・公式コードの読解と設計上の計算であり、Tokenizer学習、RTX 4090 benchmark、モデル変換、学習実験の実測ではない。新しい推奨値はすべて**提案**で、ユーザーと合意済みの**確定**方針とは区別する。

## 目的から逆算した不足

| 実現したいこと | 既存資料で不足していた判断 | 今回の調査結果／次の判断 | 優先度 | 詳細 |
|---|---|---|---|---|
| 10M以内のmodern Transformer | QK-Normの軸、順序、scale、初期化 | Qwen3式のhead次元RMSNormを第一候補。旧概算との差を再計算 | P0 | [モデル・学習](12_training_implementation_research.md) |
| 数ターンの生成 | KV cache使用時の非正方形causal mask | 学習、1-token decode、chunk decodeでmaskを分ける | P0 | [モデル・学習](12_training_implementation_research.md) |
| 会話記号を保つTokenizer | 既定のNFKC、空白、特殊tokenの種別 | 弱い正規化を明示し、会話構造tokenをIDで挿入 | P0 | [Tokenizer・データ](13_tokenizer_dialogue_data_research.md) |
| 4k語彙で日本語を扱う | 必須文字と256 byte piecesを含む語彙予算 | character coverageとfallback率を同時測定 | P0 | [Tokenizer・データ](13_tokenizer_dialogue_data_research.md) |
| 4k/8kから勝者を選ぶ | BPB分母、文脈量、同一tokensの不公平 | 同一原文・bytes・時間を別々の比較条件として保存 | P0 | [評価・配布](14_evaluation_deployment_research.md) |
| 4090で長く学習する | 小モデルの実際のメモリと速度制約 | logits、AMP、compile、optimizer込みでbenchmark | P0 | [モデル・学習](12_training_implementation_research.md) |
| 中断後の再現性 | worker prefetch、mixture乱数、許容誤差 | 消費済み位置とsampler状態を保存。再現性の対象環境を固定 | P0 | [モデル・学習](12_training_implementation_research.md) |
| 10Bから20B、50Bへ延長 | 終点依存cosineの延長方法 | 小探索はcosine、本系列はWSDを比較候補にする | P1 | [モデル・学習](12_training_implementation_research.md) |
| 自然な短い雑談 | 具体的な日本語複数ターンデータ | RealPersonaChatを有力候補に追加。制約別に他候補も整理 | P1 | [Tokenizer・データ](13_tokenizer_dialogue_data_research.md) |
| Assistant-only SFT | shift後のmask、EOT、途中切断 | 本文とEOTを教師対象にし、役割単位でmaskを構築 | P1 | [Tokenizer・データ](13_tokenizer_dialogue_data_research.md) |
| 5〜10MB級のローカル配布 | custom model、Unigram、QK-Normの互換性 | GGUF変換を学習前のgateに追加 | P0 | [評価・配布](14_evaluation_deployment_research.md) |
| 4bit化 | 576/640幅と量子化blockの整合 | FFN downでK-quantのfallbackが生じ得る。実際の型と容量を確認 | P0 | [評価・配布](14_evaluation_deployment_research.md) |
| 蒸留で能力密度を上げる | teacherとstudentの異なる語彙 | 初回は応答テキスト蒸留。logitsの直接KLは採用しない | P2 | [Tokenizer・データ](13_tokenizer_dialogue_data_research.md) |
| 50〜100B master corpus | 重複、教育scoreの意味、日本語MinHash | 小subsetから開始し、会話適合性と日本語shingleを検証 | P1 | [Tokenizer・データ](13_tokenizer_dialogue_data_research.md) |

P0: 長期学習の前に解決。P1: 100M探索／Chat準備までに解決。P2: baseline成立後。

## 調査で分かった設計上の注意

1. SentencePieceの既定正規化は会話表現保存の方針と整合しない可能性がある。`identity`等を明示し、空白・改行も別途検証する。[公式正規化仕様](https://github.com/google/sentencepiece/blob/master/doc/normalization.md)
2. `control_symbols`は原文内に書いても単一の構造tokenとしてencodeされない。会話テンプレートを単純な文字列としてencodeする実装には変更が必要。[公式特殊token仕様](https://github.com/google/sentencepiece/blob/master/doc/special_symbols.md)
3. SDPAの非正方形`is_causal=True`は左上整列。KV cacheの末尾にあるqueryを正しく扱うmaskとは限らない。[公式SDPA仕様](https://docs.pytorch.org/docs/2.14/generated/torch.nn.functional.scaled_dot_product_attention.html)
4. FineWeb2 Edu Japaneseの`small_tokens`系には既知の重複注意があり、公開token数は独自Tokenizerの数ではない。[配布元のdataset card](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese)
5. llama.cppはQwen3式QK-NormとSentencePieceへの変換経路を持つが、一般的な変換先SPMとUnigramの分割処理は同じではない。FFN downの576／640列には256要素block形式の制約もある。モデル計算とTokenizerの互換性を別々に検証する。[Qwen変換コード](https://github.com/ggml-org/llama.cpp/blob/master/conversion/qwen.py)、[Tokenizerコード](https://github.com/ggml-org/llama.cpp/blob/master/src/llama-vocab.cpp)、[量子化コード](https://github.com/ggml-org/llama.cpp/blob/master/src/llama-quant.cpp)

## 当初の検証案と後続実測

以下は調査時の検証案。Tokenizer・モデル・export・会話pilotと教師token量はPhase 1〜3、GPU保存再開→速度測定はPhase 4で完了した。100M探索・補助予算・候補選定はPhase 5で完了。現在の順序はロードマップを正とする。各成果物にはconfig、入力hash、依存version、失敗例を含める。

| 順番 | 検証 | 成果物 | 通過条件 |
|---:|---|---|---|
| 1 | 会話記号・特殊token・空白・改行 | `tokenizer_contract_report.json` | 正規化の期待値、固定ID、encode/decode仕様が一致 |
| 2 | 最小モデルとcache | `model_contract_report.json` | parameter count、causality、cache一致、finite gradient |
| 3 | ランダム重みでHF／GGUF変換 | `export_parity_report.json` | token IDとfloat logitsが許容誤差内で一致 |
| 4 | 4090でsynthetic／実shard benchmark | `throughput_report.json` | GPU・batch・backend別の実速度とpeak memoryが得られる |
| 5 | 小データのsave/resume | `resume_report.json` | 消費token列が一致し、同一環境でloss／重みが一致 |
| 6 | 4k/8kの100M探索 | `tokenizer_model_comparison.json` | BPB、処理bytes、時間、更新回数、生成失敗率を比較できる |
| 7 | 会話データのpilot | `dialogue_data_report.json` | unique dialogue数、教師token数、split、品質分布が分かる |

## 文献だけでは解決できなかった項目

- 10Mでの日本語雑談能力の上限と、最適なWeb／会話mixture。
- 小予算のT4K NoNorm / LR 0.002選定は完了。math/compiled-math/Flashの容量・速度と厳密/cold再開は③で実証済み。拡張corpus・長期予算での最適性と品質目標は未実証。
- GGUF内蔵Tokenizerは不一致が判明し、外部wrapperで一致を検証済み。汎用CLIの内蔵Tokenizer互換は未達。
- 4090 throughputは測定済み。compiled/math/Flashと採用候補の最大容量も③で測定済み。CPU応答時間分布、学習後の量子化品質は未測定。
- LLM-jp Corpus v4の個別subset manifest・利用条件。公式公開告知の規模は確認できたが、今回の閲覧ではGitLab本文を十分取得できなかった。既存05の個別subset表は引き続き**要検証**。

これらは未調査のままではなく、上記の実験または原本取得を必要とする未解決事項として管理する。既存09の公開モデル一覧全件の再監査と、Mamba／Convのkernel比較は今回の対象外で、後半研究として残す。

## 資料の読み方

各詳細文書は「一次資料で確認した事実」「設計から計算した値」「JMicro向け提案」「実測待ち」を明記する。外部URLの`main`／`master`とWeb版仕様は調査時の参照先であり、採用versionを保証しない。実装開始時に使うrelease／commitを固定して再確認する。

<!-- Original heading aliases retained for historical incoming links. -->
<a id="現在の課題と解決に必要な証拠"></a>
