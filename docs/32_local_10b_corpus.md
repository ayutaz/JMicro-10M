# ローカル10Bデータセットの整備

2026-10-03。ユーザー指定「今後のために10bほどローカルに用意」に基づき、学習用データの準備を実行する。完了はT4Kで測ったtrain stream tokensが10,000,000,000以上あり、全件構造監査に通り、ローカルで利用可能なこと。周回、dev/test、上流の別Tokenizerによる推計は10Bへ含めない。これは学習の実行依頼ではなく、モデルは10,001,152パラメータのまま。

## 保存先と容量

bulk dataはすべてWSLのLinux filesystem、`/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/`へ保存する。`/mnt/c`からデータを逐次読む経路を使わない。Windowsコード/Git正本の変更をLinux実行コピーへ同期し、実行前にsource snapshot/hashを保存する。

開始時はWindows C:空き約2.5TB、WSL約1TB/空き835GiB、RAM62GiB、CPU32 logical。raw・SQLite・signature・各bandの親配列・corpus・shards・監査の中間領域を別計上し、開始時の最低空きを450,000,000,000 bytesとする。現在はWSLディスク拡張不要。以後も実容量を監視し、必要なら既存データを保持して拡張する。仮想diskの空きだけでWindows物理diskの余裕を判断しない。

## 取得と構築

[新規config](../configs/phase6/corpus_10b.json)は既存のrevision/quality filter/T4K/32×4 LSH/Jaccard0.85を維持する。まずsmall_tokens_cleanedの先頭128filesを取得し、上流SHA-256と実sizeを確認する。最大160files/raw50GB。既取得の8filesはhash確認後にLinux hardlinkで再利用し、既存ファイルを変更しない。現8files→756Mの収率なら128filesで約12Bが見込まれるが、全体重複除去の収率は未確定。10B未達なら未達として記録し、取得上限内の追加と再構築方法を実測に基づいて判断する。

取得は4並列・stage2時間上限、ネットワーク障害は限定した3回までの再試行。構築は16workers、SQLiteのfile単位transactionとsignatureのfsync後checkpoint。再開時は未commitのsignature末尾だけをcommitted row数へ戻す。raw/旧データ・完了済み出力は保持する。構築の状態JSONはtempへのfsync後にatomic replaceする。取得待機中にこの保存方式を追加し、初期preparedの待機jobを取り込み前に終了確認したうえでprepared-v2へ移行した。初期jobとsnapshotも保持する。

元の巨大in-memory LSHを使わず、同じ128要素MinHashをuint32で保存し、32bandsを一つずつsortして等しい4要素の候補を列挙する。実文字列の5gram Jaccardで確認し、URL/exact/nearの全体connected componentsを作る。全rawを一緒に処理するためfile境界を越えた重複も扱う。band完了ごとのparent checkpointを保持する。LSH候補のrecallが確率的である限界は維持する。

旧pilotの全Web文書と、expanded-v2のdev/test全178,901文書を保護用レコードとして先に登録する。固定評価suiteの混入判定も維持し、それらにつながる検出clusterを新trainから除外する。元trainは先頭8rawに含まれ、追加rawとのexact/near重複を統合処理する。旧corpus/shards/dev/testを上書きせず、新しいcluster単位90/5/5splitを別系列として出力する。旧モデルとの評価には既存devを保持する。

JSONの全indexを巨大listへ溜めず、corpus・uint16 token stream・index JSON arrayを逐次書き出す。Tokenizeは並列、全文のdecode往復/hashを確認する。export中断時は部分出力を保持して別attemptへ再構築する。構築・独立監査の累積実行上限は24時間で、再開しても消費済み時間を引き継ぐ。これは完了時刻の見積りではない。旧8filesの構築652.7秒/監査846.9秒を参考値とし、今回の実データfile処理時間・容量を観測して残り時間を見直す。

## 完了監査と停止

### 並列LSHへの検証済み移行

実1,000,000レコードの固定prefixについて、元の逐次方式と8workersのband並列方式を全32bandsで比較した。[実比較](../reports/phase6/corpus_10b_parallel_probe.json)は524,480候補ペアのcoverage一致、全1Mのcluster/duplicate代表完全一致。reference30.004秒→parallel9.135秒、3.285倍。小fixtureでも旧heldoutのnear除外・元方式との全代表一致・band checkpoint再利用を確認した。これは同じデータ処理の性能/整合性検証で、全10Bの監査結果ではない。

候補・Jaccard0.85・保護対象・splitを変えず、各bandを独立に全候補検証し、最後に全体のconnected componentsを統合する。単一band内ですでに連結したduplicate同士だけを省略し、group-size上限や推定類似度による候補除外は行わない。8workersに制限し、巨大32個のhash mapを作らず、一度に最大8bandsを処理する。bandごとのedge/hashをcheckpointとして保存する。band間で重複するverified link数は逐次方式と異なり得るため、全体代表の一致を検証し、数値のscopeも記録する。元の独立auditは逐次再構築のまま維持する。

移行前のlive ingestion1105089へSIGINTを送り、executor終了・SQLite rollback・終了時累積680.554秒の保存を確認した。完了24raw files/5,630,035レコードのcheckpointを保持し、同じprepared-v2へ新しいexecution v3を起動。データや旧source snapshotを書き換えず、追加実行codeは別snapshotへ保存する。元の24時間予算は引き継ぎ、取り込み済みfileを再処理しない。旧jobは`job-v2-retired.json`へ保持する。

現在の起動/復旧入口は[scripts/run_corpus_10b_parallel.sh](../scripts/run_corpus_10b_parallel.sh)。Windows hidden launcher23824、Linux1106994/boot`0b330ec7-c11f-4bb3-be7c-cae9b868f4af`/start_ticks144729。ログは`ten-billion/preparation-v3.log`、band処理は`prepared-v2/parallel_bands/`、追加sourceは`execution_v3_snapshot/`。元入口は履歴として保持し、再開に使用する前に最新jobの実process identityを確認する。

[独立audit](../scripts/audit_corpus_10b.py)は全raw/hash、source payload、filter、保護判定、全signatureを再構築し、URL/exact/検出near componentsと新splitを再照合する。全採用corpusのmembership/index/BOS-body-EOS/token列/byte数を再encodeとdecode往復で検査し、train10B以上を要求する。test利用は構造検証だけで、モデル採点や選定には使わない。

3個の追加testsは元LSHとの候補一致、transitive代表、file再開・未commit末尾復旧・旧heldoutのexact/near除外・独立auditとtoken破損棄却を検証する。全105tests成功、skip/failure/error0。新config用schemaの追加漏れで最初の全suiteが2件失敗した記録はログへ保持し、schemaを追加して修復した。小fixture成功を実10Bデータの監査成功へ読み替えない。

起動入口は[scripts/acquire_corpus_10b.sh](../scripts/acquire_corpus_10b.sh)と[scripts/run_corpus_10b.sh](../scripts/run_corpus_10b.sh)。どちらもuv/Python3.12.7。hidden Windows wsl.exe launcherを保持し、Linux job.jsonにPID/boot/start_ticks/command/configを保存する。取得を待つ場合は記録のprocess identityを実/procで検証する。排他lockを持つ同じjobを重複起動しない。

確認するファイル:

- `ten-billion/raw/acquire_job.json`、`acquisition.json`、`sources.json`、`acquisition.log`。
- `ten-billion/prepared-v2/job.json`、`source_snapshot.json`、`records.sqlite`、`progress.json`、`ingest_checkpoint.json`。
- `dedup_checkpoint.json`、`manifest.json`、最終`export-NNN/corpus.jsonl`・`shards/`。
- `corpus_audit.json`、`audit_progress.json`、`ten-billion/preparation-v2.log`。

再開は実processが終了したことを確認してから、同じ入口と保存先を使う。source/config変更は通常再開で拒否する。学習・decoder比較・Chat・量子化をこのjobから起動しない。完了後は実tokens/documents/bytes/所要時間/容量・hash・監査・job終了をstatus/reportへ記録し、commitして停止する。

## 学習用ローダーでの最終利用確認

pipelineの全件auditとprocess終了を確認してから、[利用確認CLI](../scripts/check_corpus_10b_ready.py)で実際の未変更`Shard`/`BlockSampler`を使う。trainのstream/index/hashを読み込み、context1024・batch2を作り、語彙範囲・BOS教師mask・body bytes・同じsampler位置からの完全再現を検証する。モデルは作らず、学習更新0。dev/testはローダー試験へ使わない。現在は小fixtureで成功し、未完了job・失敗auditでの拒否も確認済み。実10Bへの適用はpipeline完了待ち。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/check_corpus_10b_ready.py --output /home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2 --report reports/phase6/corpus_10b_loader_ready.json
```

利用確認reportのartifact/shards path、量とhashを引継ぎへ記録する。旧`base_frozen.json`と旧checkpointのshard bindingは保持し、新しいデータを通常resumeへ差し替えない。新データで学習する際は、別系列の設定と全state再開の検証を行う。

## 大groupを保持する監査cacheの検証済み入口

2026-10-03 23:10 JSTに[全件監査v4を起動](../reports/phase6/corpus_10b_cached_audit_start.json)。実train12,225,819,077 tokensの`prepared-v2/export-001/`を保持し、元v3 processの終了後に累積9975.723秒を完全に引き継いだ。監査Linux1170053/boot`0b330ec7-c11f-4bb3-be7c-cae9b868f4af`/start_ticks1074573、logは`ten-billion/preparation-v4.log`、追加codeは`execution_v4_snapshot/`。全件監査と実loaderは未完了で、以下の未起動記録は実装時点の履歴である。

ユーザー指定の[変換・保存の限定比較](../reports/phase6/corpus_10b_export_speed_probe.json)も実施。実train262,144文書/123.5M tokens、16workersを固定し、親で文書ごとにJSON生成/batch128から、worker側JSON生成・batch512のまとまったbyte返却へ変更すると1.353/1.366倍。ABBA4回の本文/token/index全SHAと全件数が一致、42.136秒/180秒上限、事前gate1.2倍を通過。比較はbuffered binary writerを使うtrain限定sampleで、実export全体の速度とは区別する。現行exportはすでに完成しているため再構築せず、[実験code](../reports/phase6/corpus_10b_export_speed_probe.py)と結果を次回の別入口実装用に保持する。現在のauditと旧source snapshotsは変更しない。

3つの大group（6,566/7,077/4,410件）で固定32,920組ずつのscore列が一致し、cache再計算を減らして2.676〜2.899倍。全groupのcharged bytesは約356/399/234MBで2GiB以下。[実1M全32bandsの全score/全代表一致](../reports/phase6/corpus_10b_feature_cache_integration.json)と独立audit fixture/破損棄却を含む全107testsも確認した。小groupでは約2%遅いため、全体を2.7倍高速と断定しない。

[audit専用入口](../scripts/run_corpus_10b_cached_audit.sh)は実train10B以上のexport完了後だけ起動する。実process identityと終了を確認し、元jobをjob-v3-retired.jsonへ保持する。manifestがない時点で元jobを止めない。全候補とtrue Jaccardの原逐次auditは保持し、特徴量memoizationだけを8192 entries/charged bytes2GiB上限へ変更する。旧source snapshotsと累積消費時間は保持し、新codeはexecution_v4_snapshotへ別保存する。原corpus_audit.jsonと追加audit_cache_metrics.jsonを検証する。現時点では新audit jobは未起動。
