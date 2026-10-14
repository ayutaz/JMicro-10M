# Phase 6①②の完了記録

完了: 2026-10-03。ユーザー指定の①データ拡充と②長時間学習準備を、[事前の目的・完了条件](25_phase6_preparation.md)に従って完了した。Phase 6全体のBase/品質目標の達成とは区別する。③の最大batch/高速化探索・500M以上の本学習へ進まず停止する。

## ① データ拡充

目的はpilot反復から離れ、最初の500M本学習に500M以上のunique train stream tokensを用意すること。FineWeb2 Edu Japaneseの固定revisionから8 Parquet / 2,152,539,810 bytesを取得し、全上流SHA-256と条件資料を確認した。初期配合は高品質Web 100%、会話/ShareAlikeは混ぜない。

| split | 文書数 | unique stream tokens | canonical body bytes |
|---|---:|---:|---:|
| train | 1,604,292 | 756,087,912 | 2,946,200,160 |
| dev | 89,416 | 42,182,766 | 164,344,743 |
| test | 89,485 | 42,230,751 | 164,539,509 |

train bodyは752,879,328 tokens。streamには文書ごとのBOS/EOSを含む。全raw文書を再構成し、canonical/normalized hash、URL、全MinHash signature・LSH候補・真のJaccard edgeとconnected componentsを独立に再構築した。pilot全Web splitと固定suiteの検出された混入clusterを除外し、全採用1,783,193文書についてTokenizer encode/decodeの往復・全token列・index・bytesを照合した。testの使用は構造検証のみで、モデル評価・候補選定へは使っていない。

near-dedupは5-gram / MinHash 128 / 32×4 bands / Jaccard 0.85。大量処理では明示legacy schemeとvectorized Unicode rolling hashを使い、LSH候補を実文字列のJaccardで検証する。LSHの候補検出は確率的で、意味的な全重複/汚染不在まで保証しない。全hashのscalar照合と小さい統合fixtureの破損棄却も成功した。

first 500Mのstream露出は約0.66回、1Bは約1.32回、10Bは約13.23回。これは最初の500M開始用の段階拡張で、50〜100B master全量ではない。追加corpusを作る際は現在のdev/testも保護し、データを変更した系列を通常resumeとして扱わない。24 train文書の先頭最大420文字をCodexが内容確認し、販促、ナビゲーション、見出し反復、翻訳調、古い事実情報等を記録した。品質の網羅的な人手判定やBase能力達成の証拠にはしない。

大きい成果物: WSL `~/jmicro-data/phase6/raw/`、`~/jmicro-data/phase6/expanded-v2/`。小さい証拠: [corpus manifest](../reports/phase6/corpus_manifest.json)、[全corpus監査](../reports/phase6/corpus_audit.json)、[内容確認](../reports/phase6/quality_review.json)。

## ② 長時間学習準備

目的は終点によらないWSD stable継続と、独立したdecay評価枝を安全に保存・再開すること。cosine互換を保ち`--scheduler wsd`、`--branch-from`、`--decay-updates`、`--minimum-lr-ratio`を実装した。完了updateからmodel/optimizer/scheduler/RNG/samplerと消費tokens/bytes/digestを継承し、枝の元checkpoint SHA、継承履歴と追加update/tokensを分ける。通常resumeはsource/config/data変更を拒否し、明示decay作成はstable WSDからのみ許可する。

採用T4K NoNorm、実拡張shard、WSL RTX 4090、FP32 parameters/BF16、math、context 1024、batch 8で、stable連続200 vs 100+100と、decay連続100 vs 50+50を全state/loss/LR/token列完全一致で確認した。枝実行中に元stableのcheckpoint/metrics/latest/runは不変で、その後のstable継続も連続結果と一致した。実CUDA dev採点前後のRNG/モデル/学習mode保全も成功。73 GPU checks、全74 tests / skip・failure・error 0。これは計4,915,200 input tokensの準備検証で、長期学習や生成品質の証拠ではない。

runはWSL checkout `reports/phase6/preparation-20261003/`。全source snapshots、12 checkpoints、PID/boot/start ticks、排他lock、metricsとlogを保存。4本の現在runはcomplete、data builder/audit/GPU supervisor/readiness supervisorは全て終了。小さい証拠は[WSD再開](../reports/phase6/wsd_resume_report.json)、[評価分離](../reports/phase6/evaluation_isolation.json)、[独立完了監査](../reports/phase6/completion_audit.json)。初回datasketch scheme失敗とschema不足は[失敗記録](../reports/phase6/preparation_failures.json)へ保持し、条件を緩めず修正した。

## 実CLIと再開

以下は**準備検証**の中断復旧用で、完了済みjobを重複起動しない。supervisorは有効checkpointから中断stageを再開し、既存GPU process/lockを検査する。通常の次回作業は③の別測定である。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_phase6_preparation.py --raw /home/aihub_ubuntu/jmicro-data/phase6/raw --data /home/aihub_ubuntu/jmicro-data/phase6/expanded-v2 --output reports/phase6/preparation-20261003
```

読み取りの完了監査を再実行する形式:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/audit_phase6_preparation.py --data /home/aihub_ubuntu/jmicro-data/phase6/expanded-v2 --run reports/phase6/preparation-20261003 --windows-root /mnt/c/Users/AiHUB/Desktop/japanese-tiny-llm-10m --output reports/local/phase6-preparation-reaudit.json
```

stable新規runは`--scheduler wsd --schedule-updates N`、通常resumeは元引数と出力先を維持して`--resume`を追加する。decay新規runは別出力先に`--branch-from checkpoint.pt --decay-updates D`を追加し、`--schedule-updates`を分岐元update＋Dにする。decay再開では`--scheduler wsd`と凍結されたglobal budgetを維持し、`--branch-from`を再指定しない。

## 次の作業と未達

ユーザーの再開指定後にmath最大安定batch・compiled/math・厳密resume・3×200更新と評価/saveの容量/速度を測る。Unicode/反復/EOSとNoNorm HF/GGUF経路の課題を切り分け、本学習effective batch/LR/WSD数値配分/予算を凍結する。500M本学習は新規初期化し、Phase 5終端cosineの予算を変更して延長しない。Base/Chat能力・量子化・20B/50Bは未実施/未達のまま維持する。
