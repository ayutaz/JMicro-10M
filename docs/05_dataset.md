# データ設計

現在地（2026-10-03）: 固定pilotは採用22,998件（Web 19,998 / 会話3,000）。Phase 4 Base shardはWebのみのtrain 18,022 / dev 924 / test 1,052文書。dev/testと固定evalは学習から除外し、会話/sharealikeは別系列へ保つ。[復元とshard](../data/README.md)。Phase 5の100Mはこのpilotの反復（T8K約14.53 / T4K約11.91倍のstream-token曝露）であり、unique 100M corpusの実測ではない。50〜100B master corpusは未取得。次回は[段階取得と開始条件](24_phase6_plan.md#開始前に揃える条件)に従って必要な範囲から拡張する。以下の外部規模・条件は2026-10-02の候補調査値で、拡張時に固定revisionの原資料を再確認する。

Phase 6①では同revisionの8 train filesを取得し、train 1,604,292文書 / 756,087,912 stream tokens / 2,946,200,160 body bytes、dev 89,416文書、test 89,485文書の拡張shardを作成した。初期配合はFineWeb2 Edu Japanese 100%、pilotの全Web splitと固定suiteを保護してcluster分割する。独立全件監査は進行中。これは500M開始用の段階拡張で、50〜100B master全量ではない。初回500Mはstream約0.66回分、10Bは約13.23回分となり、後続stageでは追加取得・配合の判断を行う。[今回の条件](25_phase6_preparation.md)

## 基本方針

**確定**: 収集可能量をそのまま学習量にしない。50〜100B tokens相当のmaster corpus候補を構築し、実学習は100M → 1B → 2B → 5B → 10B → 20B → 50Bと段階的に進める。

10Mモデルでは容量不足が先に来る可能性があるため、雑多なデータ量より、日本語短文生成・対話に寄与する品質とmixtureを重視する。

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
