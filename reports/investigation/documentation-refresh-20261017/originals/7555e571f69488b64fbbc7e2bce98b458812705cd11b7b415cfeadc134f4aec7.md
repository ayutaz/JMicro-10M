# データ設計

更新: 2026-10-14 JST。現在の依頼は全現行文書の最新化と今後の計画作成。Base/Chatは未完成・未採用。研究・教材準備・診断・生成評価・GPU学習は再開していない。

[最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md) / [次の計画145](145_post_rejection_next_plan.md) / [今回更新146](146_documentation_followup.md)。

accepted TRAINとDEV/TESTの分離、元source/manifest/Token量・重複/反復の区別を維持。最新Base100Mは既存accepted2B poolの再利用で、新しい100M教材を増やした実験ではない。全件独立corpus auditは未完了。評価readerの混在TEST解析とcorpus split品質は別の課題で、同じ未開封フラグでは代用しない。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

元Base TEST20 promptと元Chat TEST20行は別のCPU解析問題を保存した。学習・GPU TEST採点に使っていないこととCPU未解析は別。将来の有資格最終確認にはreader分離と新しい封印TESTが必要。今回data/TESTを開封・再処理しない。

次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。

## 作成時点の資料・契約

## 中心候補

| データ | 会話中に確認した規模 | 配布上の表示 | 用途 | 注意 |
|---|---:|---|---|---|
| [FineWeb2 Edu Japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) | 約120M文書、約89.3B tokens、約518GB | ODC-BY | 高品質Webの中心 | Common Crawl由来。各Web文書の権利が一括許諾される意味ではない |
| [LLM-jp Corpus v4](https://llmc.nii.ac.jp/topics/llm-jp-corpus-v4/) | 日本語688B tokens | subsetごとに異なる | 一般Web、公的文書、特許、Wikipedia等 | source・licenseをsubset単位で管理する |
| Wikipedia日本語 | 約1B tokens級 | CC BY-SA系 | 百科事典的文章 | ShareAlike、帰属表示を別bucket管理 |
| 特許・KAKEN・国会・e-Gov・WARP/SIP | 合計で数十B以上の候補 | 会話調査ではCC BY 4.0中心 | 公的・技術的文章 | 文体偏りが大きい。混合比率を抑える |
| 青空文庫 | 約0.1B tokens級 | 作品ごとの権利確認 | 文学・長文日本語 | 著作権切れ作品とメタデータ条件を確認 |

公開値のtokenizerは本プロジェクトの4k/8kと異なるため、最終token数は必ず再計測する。

## LLM-jp v4の会話内調査値

**要検証**: 以下は会話内で整理した概数。download前に公式manifestとライセンスを再確認する。

| subset | 概数 |
|---|---:|
| ja_fineweb-2 | 236B |
| ja_cc | 223B |
| ja_patent | 68B |
| ja_warp_pdf | 58B |
| ja_sip_comprehensive_pdf | 30B |
| ja_nwc2010 | 16B |
| ja_sip_comprehensive_html | 11B |
| Wikipedia | 約1B |
| KAKEN | 約0.9B |
| 国会議事録 | 約0.8B |
| WARP HTML | 約0.8B |
| 青空文庫 | 約0.1B |
| e-Gov | 約0.08B |

`ja_fineweb-2`と`ja_cc`はともにCommon Crawl由来であり、単純加算しない。異なるdatasetを混合した後、cross-dataset dedupを実施する。

## Master Corpus案

**提案**: まず100B候補を管理可能な形で作り、runごとにsampleする。

```text
FineWeb2 Edu JP                 60B
一般Web（重複除去済み）         20B
Wikipedia / 政府 / KAKEN / WARP  5B
特許・技術                       5B
会話・QA・instruction寄り         5B
その他の高品質日本語              5B
-------------------------------------
候補                            100B
```

この比率は固定ではない。10Mモデルに特許68Bを大量投入するなど、目的と異なる文体で容量を消費しない。

## 学習stageのmixture

**提案**:

Stage A、0〜10B tokens:

```text
70% 高品質Web
15% Wikipedia・公的・技術文書
10% 一般Web
 5% 会話的文章
```

Stage B、10〜20B tokens:

```text
50% 高品質一般日本語
20% 会話的文章
15% QA
10% 説明・要約系
 5% instruction-like
```

## ライセンス管理

**確定**: document単位、最低でもsubset単位で以下を保持する。

```text
doc_id
source
source_subset
license
url
crawl_date
quality_score
exact_hash
minhash
token_count_4k
token_count_8k
```

bucket案:

- `commercial_strict`: 明示的なCC BY 4.0等を中心とする
- `commercial_web`: ODC-BY/Common Crawl由来を含む
- `sharealike`: CC BY-SA系を分離
- `excluded`: 条件不明、非商用、再配布不可、削除対象

**重要**: ODC-BYはデータベースの利用条件であり、収録Web本文の全著作権を許諾するものではない。モデル公開前にrisk reviewを行う。本書は法的助言ではない。

## 処理pipeline

```text
raw archive
  -> source/license metadata付与
  -> UTF-8 cleanup / language filter
  -> quality filter
  -> exact dedup
  -> MinHash near-dedup
  -> cross-dataset dedup
  -> train/validation contamination check
  -> 4k/8k tokenize
  -> uint16 binary shards + manifest
```

<!-- Original heading aliases retained for historical incoming links. -->
<a id="受入データの現在の範囲"></a>
