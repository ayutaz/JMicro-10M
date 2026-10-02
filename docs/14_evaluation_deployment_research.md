# 比較評価・量子化・ローカル推論の追加調査

**実装状況**: 以下は調査時点のgate・候補。調査後に[Phase 3](19_phase3_completion.md)で両モデルのHF/native float GGUF、Q8/Q4、停止、実容量・fallbackを検証済み。内蔵Tokenizerの不一致を測定し、外部SentencePiece経路を採用した。学習後の品質、BPB、RSS・CPU応答速度の評価は後続フェーズで実施する。

調査日: 2026-10-02。目標は「4k/8kを選べる」「数turnの短い日本語応答を測れる」「5〜10MB級の配布候補を作れる」。評価式・gate・閾値は**提案**であり、実測結果ではない。

## 1. BPBの定義と原文の固定

**確認済み**: token-level perplexityはTokenizerに依存する。また、context制約下では独立chunkと重なりのあるwindowで得られる値が異なる。[Hugging Faceの評価説明](https://huggingface.co/docs/transformers/perplexity)

**提案**: 原文、共通前処理後のcanonical text、UTF-8 bytes、splitと各hashを固定する。4k／8kだけで異なる正規化を使わない。BPBは次で定義する。

```text
BPB_text = sum(本文tokenのnegative log probability [自然対数])
           / (ln(2) * 本文canonical UTF-8 bytesの総数)
```

score対象の本文をすべてちょうど1回予測し、BOSを条件として最初の本文tokenも含める。PAD、BOS、role、EOT、EOSの損失は`BPB_text`の分子から外す。EOS予測lossは別metricへ記録する。文書ごとのBPBの単純平均ではなく、NLL総和／bytes総和を主値とし、domain別も報告する。

canonicalizationで削除した原文bytesを分母に足さない。既存08の「同一raw bytes」は、同一原文集合と共通変換を固定した「同一canonical bytes」の実装へ具体化する。rawとcanonicalのbyte量は両方保存する。

このBPBはdeterministicなtoken分割に対するモデルの符号長指標。すべての可能なUnigram分割を周辺化した厳密な文字列確率ではない。byte表現やtoken境界が違うモデルを比較する際の運用指標として用いる。

## 2. 同一1024 tokensだけでは比較条件が揃わない

**設計上の推論**: 8kの圧縮率が良ければ、同じ1024-token contextで長い原文履歴を使える。同じ100M training tokensでも読んだraw bytesは異なる。T4K／T8Kは層数とFFN幅も異なるため、全体比較は「Tokenizerだけの因果効果」ではない。

**提案**: 次の条件を分けてreportする。

| 比較 | 揃えるもの | 解釈 |
|---|---|---|
| 運用時の比較 | 同一評価文書、context 1024 tokens | 圧縮率を含めた最終システムの比較 |
| 原文条件を揃える短文比較 | 両Tokenizerで1024以内の共通text window、同じBOS | 同じ内容・履歴を使ったBPB比較 |
| 学習tokens固定 | 同一tokens seen、主要設定 | 既存の段階学習に沿う比較。bytes差を併記 |
| 学習bytes固定 | 同じ文書順・canonical bytes | 同じ原文露出量の比較。tokens／更新／時間差を併記 |
| 計算予算固定 | 同じGPU時間、同じhardware | 4090での実用的な予算効率 |

共通短文windowはTokenizerごとに切り詰めず、両方が収まる文字境界を先に決めてmanifestへ保存する。短文だけの選択による偏りを隠さず、長文の運用評価も残す。

長文はstride・window長・採点開始位置を記録し、重なり部分を二重採点しない。共通bytes分母に対してTokenizer別に未採点の先頭／末尾がある実装は不可。厳密な共通履歴評価が必要なら、共通text windowsへ分割して各windowをBOSから評価する条件を追加する。

4k/8kの純粋なTokenizer効果を見る補助実験は、同じhidden／層数／FFNで行う。ただしparameter budgetは異なるので、10M予算内のT4K対T8K比較とは別名で記録する。

## 3. 雑談評価を再現できる形にする

**提案**: 外部知識benchmarkだけに依存せず、独自に作成した固定100〜500 promptを以下のcategoryへ分ける。

| Category | 主な確認 |
|---|---|
| 挨拶・相づち | 不要な長文や定型文の反復がない |
| 感情への短い応答 | 入力に関連した応答が成立 |
| 日常の質問返し | 内容に合った質問で続けられる |
| 2〜数turnの文脈 | 直前の話題・条件を保持 |
| 否定・訂正 | 古い情報を繰り返さず更新 |
| 曖昧な発話 | 不自然な断定を避け、会話を継続 |
| 記号・byte fallback | 顔文字等とUnicode生成が破綻しない |
| role／停止 | EOTで止まり、User役を続けない |

人手rubricは文法、関連性、文脈維持を各0／1／2で採点する案。2は成立、1は部分的、0は破綻。反復・役割混同・停止失敗は独立したbinary flagにする。長さは品質得点へ自動加点せず、文字数とtoken数の分布を保存する。

モデル名を伏せた比較を行い、同一prompt／seedで対応づける。できれば複数評価者で一部を重複評価し、一致率を記録する。LLM judgeは補助で、judge名／version／promptを保存する。長い返答への好みが短文目標を上書きしないよう、人手の少数sampleで確認する。

### 自動metricの契約案

- 停止成功率: max new tokensに達する前にEOT／EOSで停止した割合。空応答も別計数。
- role漏出率: 出力へ禁止role開始IDが出現した割合。decoderがcontrol tokenを隠す前のID列で測る。
- 反復率: 同じ文字列の連続反復や文字n-gram重複。挨拶の通常の繰り返しと区別できる例を付ける。
- Unicode破綻率: decode時のreplacement文字だけでなく、生byte列が不正UTF-8となった割合。入力自体のU+FFFDと区別する。
- 空応答率、文字数／tokens分布、直前条件の保持率。

greedyの固定suiteと、temperature／top-p／複数seedのsampling suiteを分ける。generation抑制の有無も設定として固定する。BPBが改善しても関連性やrole失敗が悪化したrunは、自動的にChatの勝者にしない。

20B対10BのBPB差はdocument単位、会話差はdialogue／prompt単位でpaired bootstrapする案。tokenを独立sample扱いしない。95%信頼区間と効果量を保存し、devで選んだ条件の最終testを別に残す。

## 4. QK-Normありの配布経路

**確認済み**: llama.cppのQwen3実装はhead次元のQ/K RMSNorm、RoPE、GQA、SwiGLUを持ち、output weightがない場合にtoken embeddingを使う処理がある。converterのQwen3はQwen2経路を継承し、SentencePieceを先に試す経路もある。[推論実装](https://github.com/ggml-org/llama.cpp/blob/master/src/models/qwen3.cpp)、[変換実装](https://github.com/ggml-org/llama.cpp/blob/master/conversion/qwen.py)

**推論・提案**: [12のQwen3式仕様](12_training_implementation_research.md)に合わせると、モデル計算を既存runtimeへ写す候補になる。Tokenizerの互換性は別問題。独自のQK-Norm、回転layout、role処理を入れるほどadapterが必要になる。モデル名を`Qwen3ForCausalLM`へ変えるだけでは互換性は証明できない。

配布候補の優先順は以下。

| 経路 | 用途 | 実装上のgate |
|---|---|---|
| 独自PyTorch FP32／BF16 | 正しさの基準、研究 | config、Tokenizer、cacheを復元できる |
| Transformers互換artifact | 再利用、GGUF変換入口 | ランダム初期化の参照モデルとtensor／logits一致 |
| GGUF float→Q8→Q4候補 | CPUローカル配布 | token IDs、float推論一致、量子化後の品質・容量 |
| ONNX／Web向け形式 | 対象端末が決まった後 | 対象execution providerでcacheと量子化が動く |

HF形式にはweights、config、Tokenizer modelとwrapper設定、special token IDs、chat template、generation configを含める。Tokenizerを独自Unigramに置き換えるので、Qwen既定BPEのwrapper／chat templateをそのまま使わない。構造tokenを本文encodeから分ける契約をHFとGGUFでも再現する。

### 独自Unigramは変換だけで互換にならない

**確認済み（公式コードの読解）**: 調査時のconverterの`_set_vocab_sentencepiece()`はTokenizer種別を`llama`として出力する。runtimeのSPM処理はpiece scoreによる隣接merge、UGM処理はViterbiで最良分割を求める別実装である。UGMの確認した未知文字処理にはUNKへの分岐があり、JMicroのbyte fallbackとの一致も保証できない。[converter本体](https://github.com/ggml-org/llama.cpp/blob/master/conversion/base.py)、[runtime Tokenizer](https://github.com/ggml-org/llama.cpp/blob/master/src/llama-vocab.cpp)

**推論・提案**: `tokenizer.model`を渡して変換が成功しても、学習時と推論時のtoken IDsが一致するとは限らない。Unigramの日本語・未知文字・空白を含むgolden corpusで検査し、合格しない場合は次を選ぶ。

- 第一の代替案: SentencePieceを外部で使い、生成するinput IDsと構造IDをllama.cppのtoken入力APIへ渡す。出力IDsのdecodeもSentencePiece側で行う。GGUF内蔵Tokenizerを使う汎用CLIとの互換性は別の未達項目として残す。[token入力のC API](https://github.com/ggml-org/llama.cpp/blob/master/include/llama.h)
- 内蔵Tokenizerを使う案: Unigram、byte fallback、normalizer metadataを扱うconverter／runtime adapterを追加し、encode／decode一致を検証する。Tokenizer種別名を変えるだけで成功扱いにしない。
- BPEを比較する案: 新たにTokenizerを学習する別実験。学習後のUnigramを無断でBPEへ差し替えない。

`<|eot|>`も調査時のruntimeのEOT自動検出名には含まれない。GGUFの明示的なEOT ID metadataまたは呼び出し側の停止IDで指定し、EOTを生成した後の停止を確認する。control tokenとして登録しただけでは停止仕様が成立しない。

### 本学習前のexport gate

**提案**: 学習済みcheckpointを待たず、ランダム重みで以下を確認する。

1. 独自モデル→同じ構成のHF参照モデルへweight mappingする。projectionの向き、Q/K norm、RoPE、共有Embeddingが一致する。
2. 両者で同じtoken IDsを入力し、全位置logitsをFP32／float条件で比較する。
3. float GGUFへ変換し、日本語・記号・空白・改行・特殊tokenのencode IDsとdecodeを比較する。内蔵Tokenizerが不一致なら外部SentencePiece経路を明示し、同じID列でモデル計算を検証する。
4. llama.cppとのfloat logits、prefill／cached decodeを比較する。runtime間の数値誤差の許容値を記録する。
5. Q8／Q4へ変換し、型fallback、実file容量、読み込みと生成を確認する。

ランダム重みでは変換・数値・形状は検証できるが、量子化後の会話品質は判定できない。学習後に同じgateを再実行する。

## 5. FFN幅576／640とK-quantの制約

**確認済み**: GGMLのK-quantには256要素blockがある。llama.cpp quantizerはtensorの列数がblock幅で割り切れなければ、形式に応じたfallbackを選ぶ。たとえばQ4_K→Q5_0、Q6_K→Q8_0の分岐がある。tied embeddingをoutput側の精度選択として扱うコードもある。[block定義](https://github.com/ggml-org/llama.cpp/blob/master/ggml/src/ggml-common.h)、[quantizer](https://github.com/ggml-org/llama.cpp/blob/master/src/llama-quant.cpp)

**設計からの計算**:

- FFN downはPyTorchで`[256,576]`または`[256,640]`。GGMLの列方向は576／640。
- 576は256で割ると余り64、640は余り128。どちらも32では割り切れる。
- したがって、全tensorを同じK-quantで保存できる前提は置けない。設定とtensor categoryによってdown projectionが別形式になり得る。
- FFN幅を512／768へ丸めるだけでは、SwiGLU予算が変わる。T8KのFFNを768へすると12層分で約1.77M増え、10M予算を超える。

**提案**: 576／640の設計を直ちに変更せず、float、Q8_0、Q4_0、Q4_K_M等の候補で各tensorの実型・fallback log・容量・品質・速度を記録する。K-quantを優先してarchitectureを変える案は別モデルとして比較する。

## 6. 「約5MB」と実際の配布容量

**設計からの計算**: head間gain共有のT8Kは9,772,800 parameters。全parameterを一様に保存した理想値は以下。MBは10進、MiBは2進。

| dtypeの理想値 | bytes | MB | MiB |
|---|---:|---:|---:|
| BF16／FP16、2 bytes | 19,545,600 | 19.55 | 約18.64 |
| INT8、1 byte | 9,772,800 | 9.77 | 約9.32 |
| INT4、0.5 bytes | 4,886,400 | 4.89 | 約4.66 |

これはweightsの理想下限目安であり、scale／zero point、精度を残したNorm／Embedding、量子化fallback、Tokenizer、config、GGUF metadata、alignmentを含まない。共有Embeddingがfile内で二重保存されていないかも検査する。既存01の5／10／20MBは目標目安で、実file容量としての保証ではない。

KV cacheは別メモリ。T8K、batch 1、1024 tokens、2 KV heads、head dim64、K/VともBF16なら、`2*12*1024*2*64*2 = 6,291,456 bytes`で6MiB。T4Kは13層なので6.5MiB。cache以外のactivation、buffer、runtime、TokenizerもRSSへ加算される。

**提案**: weights file、全artifact、peak RSS、cache設定を別々にreportし、「5MBモデルだから5MB RAMで動く」と説明しない。

## 7. CPU応答時間と量子化品質の判定

**提案**: 対象CPU／OS／threadsを記録し、batch1でprompt 32／128／512／1024 tokens、生成64 tokens等を比較する。1024上限では生成分も含めた長さ管理を実装し、prefill＋decodeで上限を超えない条件を作る。

測定はload時間、初回token時間、prefill tokens/sec、decode tokens/sec、64-token応答総時間、p50／p95、peak RSS。tokenize／decodeを含むユーザー体感時間と、model計算だけの時間を分ける。10Mでは少数threadが有利かもしれないが、実測で選ぶ。

量子化前後は同じprompt・seed・samplingで評価し、BPB増分、関連性、role／停止失敗、Unicode破綻を比較する。低精度でlogitsが変わるため、greedy文字列の完全一致を品質の必須条件にはしない。Q4が劣化する場合はQ8またはEmbedding高精度の混合形式を候補にし、サイズ目標と品質のtradeoffを報告する。

採用閾値はfloat baselineの性能を見て決め、今回の文献調査だけで「BPB増分0.1なら許容」等を確定しない。最終配布物にmodel／Tokenizer／dataset manifest hash、runtime commit、量子化設定、評価reportを添える。
