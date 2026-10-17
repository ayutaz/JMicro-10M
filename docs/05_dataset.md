# データ設計

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

最新RDropは既存accepted TRAINの同25M教師/同source quotaであり、新規corpus作成ではない。TRAINとDEV/TESTを分離し、unique量と反復露出を区別する。既存受入・manifest・split証拠を再利用するが、独立の全corpus内容監査が完了したとは記載しない。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## 設計・手順の保存記録

以下は作成時点の仕様・調査・復元手順。途中の「最新」「次は」「未実施」やPIDはその時点の記録で、現在の状態は本ページ冒頭と148を参照する。外部サービス/依存の最新仕様は今回再照会していない。

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

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="受入データの現在の範囲"></a>
