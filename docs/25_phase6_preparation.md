# Phase 6の①データ拡充・②長時間学習準備

状態: 全完了条件を実データとCUDAで検証し完了。実量・全監査・保存先・実CLIは[完了記録](26_phase6_preparation_completion.md)。現在は③の探索前で停止中。

更新: 2026-10-03。ユーザー指定「phase6の1,2を目的とゴールを明確にして最後まで」に対応する実行計画。番号は会話で説明した①データ拡充と②長時間学習準備を指し、24の開始前gate番号とは区別する。

## 目的と今回の境界

①はpilotの反復から離れ、最初の500M本学習で少なくとも500M unique train stream tokensを使える日本語corpusを作る。②は長期系列を終点に依存せず継続でき、評価用decay枝を独立に作成・保存・再開できる学習器を実装する。両方の検証・記録・コミットまで行い、速度/最大batch探索と500M以上の本学習へは進まない。既存の品質目標・Phase 0–5 report・Tokenizerを維持する。

## ①のゴールと完了証拠

- FineWeb2 Edu Japaneseのpilotと同じ固定revisionから段階取得。まず8 train Parquet、足りなければ同revisionの次のfileを追加し最大16 files / raw 4.4GBとする。巨大master全量取得はしない。
- 原資料・source/subset/revision・上流SHA-256・取得容量・帰属・利用条件を保存。会話/ShareAlikeは混ぜず、初期配合は高品質Web 100%。将来の配合は別改訂として扱う。
- pilotの全split、固定Base/Chat suiteを保護。canonical/normalized exact、URL grouping、5-gram MinHash 128 / 32 bands / verified Jaccard 0.85の近似重複を処理し、splitは文書cluster単位で決定する。LSHの検出限界を明記する。
- T4K公開Tokenizerのhashを検証し、train/dev/testのuint16 shard・source情報・unique docs/bytes/body/stream tokens・反復見積もりを保存。train streamは500M以上、dev/testは独立に存在し、評価や選定へtestを使用しない。
- rawからの再構成、重複/混入audit、shard hashと内容/件数/Tokenizer round-tripの照合、内容サンプルの確認を行う。検証reportに実量・所要時間・保存先を記録する。予定量や少数fixtureを実corpusの証拠にしない。

## ②のゴールと完了証拠

- cosine互換を保ちWSD warmup/stableを実装。stableの学習率は将来の終点に依存しない。凍結runの予算やdataを通常resumeで変更しない。
- 完了updateのstable checkpointから別directoryへdecay枝を作る明示CLIを実装。branch元SHA、継承した学習履歴、枝の追加update/tokens、schedule、stateを記録する。decayは枝の追加予算でcosineに下げる。stable元や元runのmetrics/latestを変更しない。
- model/optimizer/scheduler/RNG/sampler/consumed tokens・bytes・digestを保存する。再開時にsource/config/data hashの変更を拒否する。分岐の変更は通常resumeと分け、WSD stableからだけ許可する。
- selected T4K NoNorm、拡張実shard、WSL RTX 4090、BF16/mathでstable連続200 vs 100+100、decay連続100 vs 50+50を**全state/loss/token列完全一致**で検証。warmup/stable/decay境界のLR列と、評価/枝作成前後のstable継続一致を確認する。これは小予算の準備検証で、本学習や品質達成ではない。
- 永続jobのPID/boot/start ticks、排他lock、log、source snapshot、checkpoint SHA、終了状態と実CLI/restart commandを保存する。関連CPU/CUDA testsも実行し、破損・禁止変更の棄却を確認する。

## 成果物と停止

`configs/phase6/preparation.json`、固定source一覧、拡張corpus/shard manifest、corpus検証report、WSD/branch CLIとtests、CUDA resume/branch report、準備の独立完了audit、status/handoff更新、Git commitを残す。大きいraw/shards/checkpointsはWSL data/runへ保持し、小さい証拠だけGitへ保存する。全条件が揃うまで完了にせず、足りない取得容量や認証等は正確なblockerとして記録する。
