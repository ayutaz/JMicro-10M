# Tokenizer・日本語会話データ・SFTの追加調査

**実装状況**: 以下は調査時点の提案。調査後に[Phase 1のデータ取得・pilot](17_phase1_completion.md)、[Phase 2のTokenizer学習・文字復元・会話教師token計数](18_phase2_completion.md)を実施済み。後続のSFT学習・品質比較は未実施。

調査日: 2026-10-02。[Tokenizer](04_tokenizer.md)と[データ設計](05_dataset.md)に残っていた、入出力仕様と短い雑談向けデータの不足を扱う。件数・ライセンスは参照先の表示、配合・閾値はJMicro向けの**提案**。今回はデータ全件の取得・集計は行っていない。

## 1. 弱い正規化を設定で実現する

**確認済み**: SentencePieceは既定で`nmt_nfkc`を使い、正規化後の文章から語彙を学習する。`identity`を指定しても、dummy prefixや余分なwhitespace除去等は別設定である。[正規化仕様](https://github.com/google/sentencepiece/blob/master/doc/normalization.md)、[NormalizerSpec](https://github.com/google/sentencepiece/blob/master/src/sentencepiece_model.proto)

**提案**: corpus側で改行CRLF→LF、必要な制御文字の除去等を実施し、Tokenizer側は以下を初期候補にする。

```yaml
model_type: unigram
byte_fallback: true
normalization_rule_name: identity
add_dummy_prefix: false
remove_extra_whitespaces: false
vocab_size: 4096 # 同じsampleで8192も作る
```

`ｗｗｗ`、`！！！`、全角スペース、顔文字、結合文字、絵文字、先頭／末尾空白、複数空白、タブ、改行を固定例として比較する。Unicode NFCの採用は別の前処理候補であり、identityと同義ではない。

**要検証**: 上記だけで任意の改行・タブが完全保存されるとは断定しない。学習用の1行1文fileでは行区切りそのものが学習本文に含まれない。document単位iteratorによる学習、未知改行のbyte fallback、decode後の空白復元を小sampleで確認する。既存04の「意味を保持」だけでは曖昧なので、前処理が変更する文字と、Tokenizerがそのまま復元すべき文字をgolden testへ分ける。

## 2. 構造tokenは本文とは別に扱う

**確認済み**: SentencePieceの`control_symbols`は原文中の表記を直接単一tokenとして認識せず、構造として別挿入する用途。`user_defined_symbols`は原文に出現すれば単一tokenになる。control tokenは通常のdecodeで本文として復元されない。[特殊token仕様](https://github.com/google/sentencepiece/blob/master/doc/special_symbols.md)

**提案**: 会話のrole／EOTはcontrol symbolsとして予約し、テンプレート構築時にIDを挿入する。本文は各messageごとに通常encodeする。これによりユーザー本文中の`<|assistant|>`という文字列と、実際のAssistant開始IDを区別できる。

| ID案 | piece | 種別／用途 |
|---:|---|---|
| 0 | `<\|pad\|>` | 組み込みpad、lossから除外 |
| 1 | `<\|unk\|>` | 組み込みunk |
| 2 | `<\|bos\|>` | 組み込みbos、系列先頭 |
| 3 | `<\|eos\|>` | 組み込みeos、Base文書終端 |
| 4 | `<\|system\|>` | custom control、system開始 |
| 5 | `<\|user\|>` | custom control、user開始 |
| 6 | `<\|assistant\|>` | custom control、assistant開始 |
| 7 | `<\|eot\|>` | custom control、発話終端 |

ID 0〜3はtrainer引数、4〜7は予約順を指定した上でartifactの実IDを検査する。順番を期待するだけでなく、`special_tokens.json`とテストで固定する。外部Tokenizer wrapperがspecial tokenを再登録する場合もIDとencode動作を確認する。

既存04の「特殊tokenが分割されない」は、「本文中の表記が常にatomic」から「テンプレートが挿入した構造IDは単一で固定」へ具体化する必要がある。user-defined方式を選ぶ場合は、本文中の同じ表記を構造として解釈するかescapeするかを別途決める。

### テンプレート案

```text
[BOS] [USER] encode(user_text) [EOT]
      [ASSISTANT] encode(assistant_text) [EOT]
      [USER] encode(next_user_text) [EOT]
      [ASSISTANT]
```

この図の空白は説明用で、delimiterとして本文へ追加しない。推論は最後のAssistant開始IDまでを入力し、EOTまたはEOSで停止する。Chatの主停止tokenはEOT、Baseの主停止tokenはEOSとする案。role ID、PAD、BOS、UNKは通常の本文生成では抑制し、抑制設定も評価条件として保存する。

## 3. 4k語彙はbyte fallback込みで予算を考える

**確認済み**: 特殊tokenも語彙上限に含まれ、byte fallbackは256個のbyte piecesを追加する。[trainer実装](https://github.com/google/sentencepiece/blob/master/src/trainer_interface.cc)

**設計からの計算**: 8特殊token＋256 byte piecesなら、通常piecesに残る枠は4kで3,832、8kで7,928。その枠へ必須文字とsubwordを一緒に収める。

**提案**: 同じ固定sampleでcharacter coverage `0.9995/0.999/0.995`等を試す。日本語の必須文字数が予算を超える場合はcoverageを下げ、欠けた文字をbyte fallbackへ退避する。語彙を暗黙に縮小する設定で成功扱いにせず、piece数が4096／8192であることを確認する。

測るものは、総piece数、alphabet／byte／special／通常subword数、平均／p95 chars/token、fallback token率、fallbackが発生した文字の率、domain別tokens/document、1024-token超過率。fallbackを含むencodeは可能でも、生成で有効UTF-8 byte列を出せる保証はない。

Tokenizer学習sampleはtrainからのみ選ぶ。短文・会話・Web等のdomain比率はbytesと件数の両方で記録し、4k/8kで同じdocument集合を使う。sample順、SentencePiece version、trainer引数、model／sample hashを固定する。再学習のbitwise一致は確認するまでは保証しない。

## 4. FineWeb2 Edu Japaneseの使い方を具体化する

**確認済み**: 配布元は教育score 2.5以上の約120M文書を提供し、`sample_10BT`、512 tokens以下の`small_tokens`、ノイズ除去版`small_tokens_cleaned`を持つ。token数はModernBERT-Ja-130MのTokenizerによる値。短文subsetには先頭範囲の既知の重複注意がある。[dataset card](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese)

**提案**:

- 最初は`sample_10BT`等から小規模に取得し、独自Tokenizerで再計数する。「10BT」をJMicroの10B tokensとして扱わない。
- `small_tokens_cleaned`は短文pilot候補。重複注意への対処に加え、実際の本文hashで検査する。配布版更新で行番号が変わる可能性もあるのでrevisionを固定する。
- 教育scoreと会話適合性は別指標。高scoreだけを抽出する案と、会話／日常文体を補う案をpilotで比較する。
- 元の`id/url/dump/date/score`にsource revision、raw／canonical text hashを加える。短文のみのsubsetからmaster corpus全体の圧縮率を推定しない。

## 5. 日本語の重複判定とvalidation

**確認済み**: DataTroveにはMinHash・文単位dedup等のpipelineがある。MinHash実装は言語を指定して単語tokenizerを使い、既定languageはEnglish。[DataTrove](https://github.com/huggingface/datatrove)、[MinHashコード](https://github.com/huggingface/datatrove/blob/main/src/datatrove/pipeline/dedup/minhash.py)

**提案**: 日本語は空白splitのn-gramで処理しない。日本語tokenizerを明示したword shinglesと、文字n-gramの候補を小sampleで比較し、重複ペア／非重複ペアを人手確認する。MinHashのnormは重複探索専用とし、学習本文の強い正規化へ流用しない。

validationのdocument候補を早期に確保し、exact／near duplicate cluster全体を同一splitへ割り当てる。同一URLのcrawl差分、翻訳元の共通instruction、対話treeの共有prefixも追跡する。最初にvalidationを確保した後でtrainへ新sourceを追加する場合もvalidationとの重複を再検査する。

短い「こんにちは」等の一致を理由に、異なる会話全体を削除しない。短文はdocument／dialogue全体と文脈を基準にし、長いWeb文書とは別のdedup規則にする。

### Shardに追加すべき情報

**提案**: token IDsの`uint16`だけでは文書境界、loss mask、元bytesへ戻れないため、次のsidecarを用意する。

```text
document index: doc_id, shard_id, start_token, length, canonical_utf8_bytes
shard manifest: endian=little, dtype=uint16, checksum, tokenizer_hash
split manifest: source_revision, cluster_id, split, preprocessing_hash
SFT index: dialogue_id, message roles, assistant spans, source/provenance
```

Baseは文書末尾EOS付き連結streamを初期案にする。ただしEOSだけでは他文書へのattentionを遮断しない。block diagonal attentionを試す場合は別条件とし、mask変更によるbackend／速度差も記録する。SFTは初回は1系列1対話＋paddingとし、packingはlossとattentionの両方が正しいことを確認してから導入する。

## 6. 短い雑談に使える会話データ

既存05には「会話・QA 5B」という量の案はあったが、その量を用意できる具体的な会話sourceが不足していた。以下はダウンロード可能性や表示条件の調査であり、採用済みではない。

| 候補 | 確認できた内容 | 表示条件 | JMicro向け判断 |
|---|---|---|---|
| [RealPersonaChat](https://github.com/nu-dialogue/real-persona-chat) | 公開版13,583対話、408,619発話。話者ID、発話、評価、persona情報 | CC BY-SA 4.0 | 短い日本語雑談の有力候補。`sharealike`で分離し、会話単位split |
| [OpenAssistant/oasst2](https://huggingface.co/datasets/OpenAssistant/oasst2) | 多言語のmessage tree。`lang/role/parent_id/rank/deleted`等 | Apache-2.0 | 日本語の良質な枝だけ抽出する補助候補。日本語件数／教師tokensは未集計 |
| [LLM-jp Dolly日本語版](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja) | 約15k instruction、context、response、category | CC BY-SA 3.0 | 短いQA補助。雑談の中心にはしない |
| [ichikara公開版](https://liat-aip.sakura.ne.jp/wp/llmのための日本語インストラクションデータ作成/llmのための日本語インストラクションデータ-公開/) | 公開ページの003系列等。版によって重複・改訂あり | 公開ページではCC-BY-NC-SA。商用は別提供 | 初期の公開可能モデル系列へ自動混入しない。版・契約確認後の別候補 |
| [JPersonaChat／JEmpatheticDialogues入口](https://github.com/nttcslab/japanese-dialog-transformers) | 会話データと評価コードの入口 | モデル規約と個別データ条件を分けて確認が必要 | 内容は目的に近いが、入口のモデル制約からdataset条件を推定しない。取得前確認を残す |
| [KokoroChat](https://github.com/UEC-InabaLab/KokoroChat) | 日本語の長いカウンセリング対話 | CC BY-NC-ND 4.0 | 用途・条件が今回の配布baselineに合わず、初期候補から外す |

ライセンス欄は配布元の表示を記録したもので、学習重みへの条件適用についての結論ではない。既存のbucket管理を維持し、source単位の表示や契約を保存する。LLM-jpモデルが公開されていることを、その学習に使われた全datasetを同じ条件で使える根拠にしない。

### Pilot案

**提案**: 使用条件を満たす候補から1k〜10k対話のpilotを作り、全量前に確認する。独自の短文会話例も100〜500件用意し、最小pipelineと評価に使う。次をsource別に集計する。

- unique dialogues、unique canonical bytes、4k／8k総tokens、Assistant教師tokens。
- 発話数、応答文字数の平均／p95、context 1024へ収まる割合。
- persona依存、長い説明、空応答、引用、翻訳調、同じ応答の頻度。
- 役割の向き、複数候補応答の品質、train／validation間の共有prefix。

RealPersonaChatのspeaker A／Bはそのままassistant／userではない。どちらをassistantに割り当てるか決めて一対話内で固定し、人格情報を入力するか省略するかも別条件にする。対話windowを作る前にsplitし、同じ対話の窓を別splitへ分散させない。話者を分離した追加testも検討する。

OASSTは`parent_id`を辿ってrootからの会話を復元し、日本語・非削除・品質条件を満たす枝を選ぶ。枝を先に平坦化してからsplitせず、`message_tree_id`単位でsplitする。OASST1／2を併用するならmessage／text重複も検査する。

## 7. SFTのloss・停止・データ反復

**確認済み**: TRLの`assistant_only_loss=True`は対応chat templateのgeneration区間等に依存する。flagだけで独自テンプレートのmaskが正しくなる保証はない。[TRL SFT仕様](https://huggingface.co/docs/trl/sft_trainer)

**提案**: v1はrole metadataからtoken span maskを明示的に作る。Assistant本文とその直後EOTをloss対象にし、User／System本文、role開始、paddingは`-100`で除外する。すべてのAssistant発話を対象にするか最後だけかもconfigへ保存する。

```text
tokens: [BOS, USER, u1, EOT, ASSISTANT, a1, a2, EOT]
labels: [-100,-100,-100,-100,-100,     a1, a2, EOT]
```

causal lossはlogits `[:-1]`からlabels `[1:]`を予測する。よってAssistant開始位置のlogitが最初の本文`a1`を、`a2`位置のlogitがEOTを予測する。maskとshiftを別々に可視化し、停止tokenが教師対象から落ちないことを確認する。

長すぎる対話は古い完了turnを削除し、本文途中を切ってEOTを付ける処理は避ける。Assistant教師tokenが0件になったsampleは除外する。PADをattentionとlossから除外し、role開始tokenを本文の一部に混ぜない。

10M／30M／100M SFT tokensは「uniqueデータ量」ではなく「累積学習量」の候補。総系列tokensとAssistant教師tokensの両方を報告し、同じ小datasetを何epoch反復したかを明記する。validation悪化、role混同、短すぎる応答、Base BPB悪化を追い、予算達成前でも最良checkpointを選べるようにする。

Dialogue mid-trainingを省略したBase→SFTも小さい対照実験として残す。mid-trainingとSFTの効果を一つの改善として混ぜない。

## 8. 10M向けデータの能力密度と蒸留

**確認済み**: TinyStoriesは語彙・内容を限定した合成英語短編で、10M未満でも一貫した生成を示した研究。日本語雑談の直接的な性能保証ではない。[TinyStories](https://arxiv.org/abs/2305.07759)

**推論・提案**: 容量を短い日常語、応答関連性、質問返し、2〜数turnの訂正へ集中させるデータ案には根拠がある。ただし教育Web全体のBPBが良いモデルが、雑談でも良いとは限らない。日常短文を増やしたmixtureと既存mixtureを、同じunique bytes／同じ時間で比較する。

蒸留には、teacher応答をstudent Tokenizerで再encodeするテキスト蒸留と、teacher分布へ合わせるlogits蒸留がある。[蒸留の原論文](https://arxiv.org/html/1503.02531v1)

**設計上の推論**: teacherの語彙が50k〜150k等、studentが独自4k／8kなら、同じindexのlogitsは同じ事象を表さない。token時刻の境界も異なるため、直接のtoken-wise KLは定義できない。初回は短い応答のテキスト蒸留を候補にし、byte／sequenceレベルの分布整合は後半研究へ回す。

合成会話はteacher名／revision、生成prompt、sampling、生成日、出所、採否理由を保存し、corpus-only baselineと分ける。短い返答だけを増やすと定型応答に偏るため、同じ意味の多様な表現、相づち、質問返し、否定／訂正を別categoryで管理する。評価promptそのものを合成学習へ入れない。

## 未解決として残す項目

- 各候補の日本語unique量と、4k／8kでのAssistant教師tokens。
- 弱い正規化と改行保持の最終契約、GGUF側との一致。
- 10Mに適した会話mixture、SFTのLR／epoch数、mid-trainingの必要性。
- LLM-jp Corpus v4の個別subset条件・manifest。公式告知の日本語688B tokensは確認済みだが、[GitLab原本](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-v4)の本文取得が不十分で、既存05の詳細値は今回確定していない。[公式公開告知](https://llmc.nii.ac.jp/topics/llm-jp-corpus-v4/)
