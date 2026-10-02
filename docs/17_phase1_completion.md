# Phase 1 完了記録

この文書とreportはPhase 1実施時点の履歴。後続の[Phase 2](18_phase2_completion.md)でTokenizer学習と教師token数を計測し、[Phase 3](19_phase3_completion.md)まで完了した。文中の未測定・次の作業は当時の状態を示す。

実施日: 2026-10-02。対象は[Phase 1のデータpilot](15_project_roadmap.md#phase-1-データの小規模pilotと評価split)。iMac上で実データの取得・処理・split・Tokenizer用sampleを作成し、全件の原データ復元と再生成を検証した。Tokenizer学習とGPU学習は未実施。

## 要求と証拠

| 要求 | 作成したもの・検証 |
|---|---|
| source台帳・利用条件・revision | [pilot config](../configs/data/pilot.json)にsource/subset、固定revision、帰属、bucket、URL、原file・条件文書のhash、取得範囲・容量上限 |
| document/dialogue manifestの契約 | [config schema](../schemas/configs/data/pilot.schema.json)、[record schema](../schemas/dataset_record.schema.json)、処理コードのArrow schema |
| 小規模Base corpusと会話pilot | `data/phase1/processed/dataset_manifest.parquet`と`corpus.jsonl`。全取得recordをmanifestへ残し、採用payloadを分ける |
| 出所・raw/canonicalの追跡 | 原file hash、source locator、解析した原rowのJSON hash、canonical本文 hash。verifyで全23,000原recordを復元して照合 |
| filter・日本語向けdedup | 弱い前処理、source言語score・日本語文字比率・品質・長さ。文字5-gram MinHash候補へ実Jaccardを適用。別source間も同じ検査対象 |
| splitと混入検査 | `data/phase1/processed/split_manifest.json`。exact/near、同一URL、長い共有prefixのcluster単位でsplitし、固定`eval/`との混入を検査 |
| trainのみのTokenizer sample | `data/phase1/processed/tokenizer_sample.jsonl`。4k/8kへ渡す同一文書・順序・file hashを保存 |
| 対話の役割と品質 | [会話report](../reports/phase1/dialogue_data_report.json)、[20件の内容レビュー](../reports/phase1/quality_review.json)。対話全体をsplitし、window化は後続 |
| 統計と未検出の限界 | [data report](../reports/phase1/data_pilot_report.json)にsource/bucket/split/domain別bytes、文字数、短文、除外理由、dedupと限界 |
| 再現性と検証 | [全件検証](../reports/phase1/verification.json)、[再生成比較](../reports/phase1/reproducibility.json)、[完了監査](../reports/phase1/completion_audit.json)。二回のoffline buildで6成果物のbytesが一致 |

本文・原file・大きなmanifestはGit管理外。現在の実file、checksum、[再生成手順](../data/README.md)を対応させる。reportと実装・config・schemaはリポジトリで管理する。

## 取得・採用したデータ

| source | 固定revision | 取得範囲 | 採用数 | unique canonical UTF-8 bytes |
|---|---|---|---:|---:|
| FineWeb2 Edu Japanese / small_tokens_cleaned | `180ca004c6a89b590daaad86cb062a07a5353c69` | 最初のtrain shardのrow 10,000〜29,999 | 19,998文書 | 36,367,317 |
| RealPersonaChat | `28d0b6b3865b29cabc26c230a2db37cdf315e937` | archive内からseed 42で選んだ3,000対話 | 3,000対話 | 6,280,509 |
| 合計 | — | 23,000取得record | 22,998 | 42,647,826 |

Web原shardは268,597,958 bytes、会話archiveは25,981,430 bytes。Webは配布元LFSのSHA-256と一致し、会話archiveも取得したhashをconfigへ固定した。Web sourceのREADMEで告知された先頭0〜9,999行と10,000〜19,999行の重複を避け、取得後にも検査した。master候補の全量は取得していない。

Webは`commercial_web`、会話は`sharealike`で分ける。配布条件の表示は[固定README](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese/blob/180ca004c6a89b590daaad86cb062a07a5353c69/README.md)と[固定LICENSE](https://github.com/nu-dialogue/real-persona-chat/blob/28d0b6b3865b29cabc26c230a2db37cdf315e937/LICENSE)を保存した。[ODC-By v1.0](https://opendatacommons.org/licenses/by/1-0/)、[Common Crawl利用条件](https://commoncrawl.org/terms-of-use)、[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)も確認した。個別Web文書の権利や学習重みの公開条件について一括の結論は出しておらず、公開前の確認はPhase 8へ残す。

## split・重複・評価混入

| split | Web | 対話 | 合計 |
|---|---:|---:|---:|
| train | 18,022 | 2,688 | 20,710 |
| dev | 924 | 150 | 1,074 |
| test | 1,052 | 162 | 1,214 |

seed 42とcluster IDのhashで90/5/5の割当を固定したため、件数比は厳密な90/5/5ではない。Phase 0の固定生成suiteとは別のcorpus splitである。

短すぎるWeb 2件を除外。normalized exact重複は0件、LSHの161候補pairのうち実Jaccard 0.85以上は0件だった。同一URLの4 linksはsplit clusterへまとめ、内容が異なる文書を保持した。verifyでは採用22,998件のsignatureを本文から再計算して残存候補を再検査した。日本語の近似重複・cross-source・同一URL・共有会話prefixの動作は、重複を含むfixtureでも検証した。

固定eval混入による除外は0件。検出対象はnormalized全文の一致と24文字以上のeval本文・入力履歴のsubstringで、検出した場合はcluster全体を除外する。短い共通挨拶だけで対話を削除しない。LSHには候補検索の未検出があり、言い換えや短い断片まで漏洩がないことを証明する検査ではない。

## 短文・会話・Tokenizer sample

Webは10,533 domains。本文文字数は平均652.89、p95 1,137、280文字以下は1,440文書。説明文・ブログ・販促文・過去のニュースが混在し、図への参照やSEO風の表現が残る。大規模化時の品質filterとmixtureを判断する材料として記録した。

対話は平均30.086 messages、約15往復相当。Assistant応答は45,051件で、文字数は平均23.11、p50 22、p95 43、最大82、空応答0件。末尾Assistantは2,844対話、末尾Userは156対話で、後続のwindow/mask処理で扱う。先頭話者をUser、他方をAssistantとして対話内で固定し、連続した同じ話者の発話は改行で連結した。原utterance IDと話者対応を保持し、persona metadataは入力から省略した。採用sourceは線形会話なのでtree復元は不要。

Web 10件・会話10件の全文をCodexが読んで確認した。独立した人手評価ではなく、全件の品質保証でもない。会話は短い相づち・質問返し・話題継続を含む一方、本文中の個人的な自己開示は残る。会話単位のsplitであり、話者を独立させたsplitではない。

Tokenizer sampleはtrainの2,444文書・対話。Web 3,999,867 bytes、会話499,822 bytes、合計4,499,689 canonical本文bytesを、文書を途中で切らずに選んだ。JSONL fileは4,974,751 bytes、SHA-256は`2bd5f104d0931e883a891f64bbcd0392cabd7259d3cfc5cd8a693f7f1acf54e6`。4k/8kはこの同じfile・順序を使う。

4k/8kのcorpus tokens、Assistant教師tokens、1024-token内の割合は未測定のため`null`。sourceが提供するtoken countを本プロジェクトのtoken数として使わない。100M探索の累積tokensとunique量・反復は後続で区別し、unique 100M tokensを取得したとは扱わない。

## 検証と次の作業

`uv run --frozen --extra data --offline pytest -q`で34件成功。`uv lock --check --offline`、全config・Phase 0評価契約の検証、既存54-file準備snapshotの検証も成功し、過去のPhase 0環境・監査を上書きしていない。

次はPhase 2。iMac上で同一sampleからSentencePiece Unigram + byte fallbackの4k/8kを学習し、特殊ID・round-trip・圧縮率・fallbackと会話token量を比較する。モデル/cache/exportはPhase 3、Windows/WSL・RTX 4090への切替と最大安定batchの実測はPhase 4。
