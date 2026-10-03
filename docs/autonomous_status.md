# Codex継続作業の現在地

最終更新: 2026-10-03（日本時間）。実測の正本はreportとWSLのrun/data、milestoneは[roadmap](15_project_roadmap.md)。

## 最新の調査: 反復退行・EOS・データ構成の調査完了、停止

ユーザー指定の反復悪化調査を[事前計画](../reports/phase6/repetition_diagnosis_plan.json)に沿って完了した。[判断と全比較](../reports/phase6/repetition_diagnosis_review.md)、[数値・binding・20項目監査](../reports/phase6/repetition_diagnosis_review.json)、[既存225 files保持](../reports/phase6/repetition_preservation.json)、[終了・同期・停止の監査](../reports/phase6/repetition_completion_audit.json)。学習更新0、GPU推論249.75秒/900秒上限、全102 tests成功/skip0。1B・新data・新trainerの学習・次回案を開始していない。

同じ80greedy反復は旧100M48→stable131M69→328M70→stable500M70→decay66。旧→最終は24件新規・6件解消、stable→decayは4件新規・8件解消。拡張モデルは131Mから反復が多く、decayが全体悪化の発生源という結果ではない。EOS教師はstable1,061,096回/0.2127%、旧0.2151%とほぼ同じで、BOSだけのmaskと実sampler/countersが完全一致する。全文同一devのEOS平均NLL3.00827→2.53698、同じ256文書末尾のEOS argmax30→35と改善する一方、80短prefix直後のEOS argmaxは0、最終の平均確率0.00247%。

全文trainの平均body464→469tokens、固定2,048文書/512文字sampleのregex反復は両方42（主に記号）。長さやsample反復の増加を主因にできない。拡張trainはWeb/commercial_web100%、128tokens以下は0.8505%。短い完結文の教師分布とgreedyの候補集中を有力な仮説として残すが、データ・露出・token予算・batch・schedule/backendが同時に変わる旧新比較で原因を確定しない。8case×旧/最終の生成IDsは完全再現、短FP32 full/cacheの全16probeは元許容内。BF16にはargmax差が各1位置あり、精度の影響と全context/backend同値は未解決として保持する。

Linux raw evidenceは`reports/phase6/repetition-diagnosis-20261003/`。CPU511/GPU570、Windows launcher23056/3468は完了し、jobのPID/boot/start_ticks・source/plan hash・log・sample/trace/testsを保持する。次の行動は停止。次回案は同じ重みのdecoder対照（最大640outputs/GPU15分）、必要なら短文mixtureの各25M-token対照（別loader/trainer実装と再開gate必須）で、元の品質基準・凍結codeを維持する。量不足が主因とは結論せず、1Bへ自動延長しない。

資源についてはWSL側で実測確認した。学習は速度優先のbatch32/Flash/compile/BF16/fused AdamW、約695k tokens/s、driver peak約7.5GiB。最大容量batch111はVRAM97.64%でも約650k tokens/sと遅く、32を採用する。data wait約0.5%でCPU入力供給が主要制約という証拠はない。使用容量を100%にする方針ではなく、検証した範囲で最速を採用している。調査推論は逐次greedy中心で学習と資源使用条件が異なる。

## 最新の結果: 500M学習・評価完了

2026-10-03: 拡張trainの500M stable＋独立763更新decayと全文dev/400生成評価を完了。同一dev BPB 1.244126→1.022491、抑制greedy EOS 0/80→0/80、反復48/80→66/80。全99 tests成功。人手blind採点・test・Chat・新重みの量子化は未実施。1B前で停止。

ユーザー指定の計画1〜5を実施した。[学習・評価監査と比較](../reports/phase6/base_500m_review.json)、[全80 greedy生成例](../reports/phase6/base_500m_review.md)、[preflight](../reports/phase6/base_500m_preflight.json)、[99 tests](../reports/phase6/base_500m_tests.json)。本文一度採点・同一89,416文書/164,344,743 bytes・FP32 CE・windowを検証した。document paired改善95% CIは[0.221163593157386, 0.22214939473619974]。これはdev文書のsampling不確実性で、学習seed変動やデータ量だけの因果効果ではない。

[指定範囲の完了監査](../reports/phase6/base_500m_completion_audit.json)で起動条件・実stable/decay・全文dev/400生成・過去証拠保持・job終了・停止境界を11項目照合した。学習/比較の独立監査25項目も通過した。生成退行は品質未達の結果として保持し、技術検証の成功へ混同しない。

stableは15,259更新/500,006,912 input tokens、decayは追加763更新/25,001,984 tokens。全state checkpointを保持し、parent SHA不変・全更新の有限値・保存間隔を監査した。stable SHA `775b14be60b755153fcfa03633e8a3a489fcddc6508db69f759b5547df57fbbf`、decay SHA `0a64cfc3ac18d411d0d2144d9d9c8185e7010872baf5247612dd365bd619514e`。Linux出力は`reports/phase6/base-20261003/`、stable/decay/evaluateのsupervisor・log・source snapshot・全checkpoint・raw評価を保持する。元のstableから同じglobal305,176更新のまま継続できる。

Windows launcher16200 / Linux pipeline465と各GPU stageは終了。`supervisor-{stable,decay,evaluate}-500M.json`・pipeline stateを保持し、完了した500Mを再起動しない。初回の非login shell uv PATH不足はGPU起動前の失敗で、専用入口へuser uv PATHを設定して修復した。失敗log/stateを`reports/local/`へ保持する。比較用の旧small reportはWindows正本からLinuxへ同期し、元のdeep evidenceは変更していない。

生成はgreedy反復48/80→66/80、sampling反復6/240→11/240、Unicode0/400→1/400で退行した。sampling EOSは0/240→1/240で、greedy EOSは0/80のまま。Unicode1件は64-token上限でmulti-byte列が途中終了したものだが、凍結metricの失敗として残す。[Codexによる20件の内容点検](../reports/phase6/base_500m_content_review.json)でも意味のある続きを展開せず反復する例を確認した。これはblind人手採点ではない。

次の行動は停止。1Bへの単純拡大は現時点で推奨せず、EOS教師量・文書長と短文promptの違い・反復傾向・greedy/sampling差を既存artifactで点検し、対照/予算/終了条件を定義してから次の実験を提案する。生成品質の未達・人手評価未実施を保持する。今回の結果をBase v1/Chat完成や新学習重みのexport/量子化合格にしない。以下の未起動/再開待ちは以前の準備・計画作成時点の履歴である。

## 以前の準備・計画作成記録（履歴）

文書・計画の更新依頼に基づき、README/実装checklist/技術状況/引継ぎと[残りの計画](27_phase6_remaining_plan.md)を93c7d1dの検証結果へ揃えた。次回は500M stable→独立decay→全文dev/400生成評価から開始し、1B/2B/5B/10Bを段階判断する。必要なpaired CI・人手採点の集約は未統合として明記した。今回の更新では学習・実験を開始せず、凍結code/config/protocol・過去report/snapshotを保持する。

[文書更新の監査](../reports/phase6/documentation_refresh_readiness_20261003.json)で25文書のWSL同期、実CLIと凍結値の一致、内部リンク、247の既存fileの保持と本学習未起動を確認する。

## 方針と停止境界

最新の依頼は次回計画の作成。[次回の500M計画](27_phase6_remaining_plan.md#次回の一区切り-拡張データで500mを学習評価する)に、約90倍へ拡張済みのtrain、新規500M stable・独立decay・同じdevでの比較、終了成果物を記載した。次回は500M評価/report/commitで停止する計画を提案し、1B以降は後続段階とする。データ不足は未確定の仮説で、学習量やscheduleも変わる比較をデータ量だけの因果効果にしない。今回は文書だけを更新し、学習は未起動。

Pythonは3.12.7/uv管理、全実行は`uv run --frozen`。依存変更は`uv add`、復元は`uv sync --frozen`。GPU学習はWSL 2 / Ubuntu / RTX 4090。Git local identityは`yousan <ka1357amnbpdr@gmail.com>`、検証済み変更をcommitし、push/公開しない。

**Phase 0〜5とPhase 6①〜⑤の準備は検証済み。ユーザー指定の「1.生成/変換確認、2.本学習設定確定」を実施し、最終監査37 checksを通過し、`93c7d1d`へcommitして停止済み。500M以上の本学習は未開始で、次の再開指定を待つ。** [今回の比較と完了条件](30_phase6_readiness_execution.md)、[③完了記録](29_phase6_performance_completion.md)。

## ③の実測と採用

採用はT4K NoNorm / 10,001,152 parameters、Flash＋torch.compile reduce-overhead / fullgraph・static / deterministic、context 1024、batch 32・accumulation 1、FP32 parameters＋BF16、fused AdamW、WSD。入力32,768 tokens/update。3×200完了更新の定常中央値は**694,521 tokens/s**、最速reference/math batch 16（127,772）比**5.436倍**。

最速設定のsave/小sample評価込みpeakはallocated 5.73 GiB、reserved 6.59 GiB、driver 7.53 GiB。data wait 0.55%。測定条件の最大安定batchは**111、112 OOM**。111は3×200・厳密再開・保存/評価を通過し、driver peak 23.42/23.99 GiB（97.64%）、速度649,563 tokens/s。VRAM容量上限と最高速度を分け、運用候補はより速い32を採用する。allocator cap 94%、固定shapeの有限探索であり、任意設定の理論最高性能を保証しない。

9設定のstable 200 vs 100+100・decay 100 vs 50+50はmodel/optimizer/scheduler/RNG/sampler、token/bytes/digest、loss/LR履歴、親の不変性・元継続が完全一致。6最速/容量設定の各3×200確認も完了。**独立監査1286 checks全成功、採用設定の空compiler cache再開26 checks完全一致、全79 tests / skip・failure・error 0**。小sample評価は4 dev文書＋1 prompt×2 greedy outputs/各最大8 tokensで、全文品質評価ではない。

v3のunique raw metricsは10,005 completed updates / 414,298,112 input tokens、cold再開は追加100 updates / 3,276,800 input tokens。別々の性能runで、一つの長期Baseではない。未完了OOM更新、診断v1/v2をこの台帳へ含めない。

- [全結果](../reports/phase6/batch_performance_report.json)、[採用理由](../reports/phase6/batch_choice.md)、[速度・資源・token要約](../reports/phase6/performance_summary.json)。
- [独立監査](../reports/phase6/performance_completion_audit.json)、[cold再開](../reports/phase6/performance_cold_resume_report.json)、[79 tests](../reports/phase6/performance_tests.xml)、[文書・旧成果保持監査](../reports/phase6/performance_documentation_audit.json)。
- [v1/v2失敗保持](../reports/phase6/performance_failures.json)、[監査初回の生成output数誤判定](../reports/phase6/performance_audit_initial_failure.json)。backend別cacheと実compiled code/呼び出し検証を修正した。監査は既存APIの2 greedy outputsを正しく確認し、GPU条件を変更していない。

## 保存先と終了したjob

Windowsコード/Git正本は`C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`、Linux実行コピーは`/home/aihub_ubuntu/src/japanese-tiny-llm-10m`。Linuxの古いGit HEADだけで識別せず、snapshot/hashで照合する。

- v3: Linux `reports/phase6/performance-20261003-v3`、job terminal complete。Windows launcher 24452、Linux supervisor 426 / boot `37666cd9-cd78-41c1-a0cb-39c21d108047` / start ticks 78847は終了確認済み。
- cold再開: Linux `reports/phase6/performance-cold-resume-20261003`、terminal complete。Windows launcher 17308、Linux supervisor 620 / 同boot / start ticks 361156は終了確認済み。
- v1/v2はinvalidatedで診断snapshot/log/checkpointを保持し、launcher 18088/23060も終了。GPU compute processなし。完了したjobを再起動しない。
- raw metrics/requests/results/checkpoints/compiled code/snapshotは各runに保持。通常cacheはLinux `artifacts/compile-cache`、cold cacheはcold runの`empty-cache`。

## ①②と過去の成果を保持

①の固定FineWeb2 Edu Japaneseは8 files / 2,152,539,810 raw bytes。T4K train 1,604,292 docs / **756,087,912 unique stream tokens** / 2,946,200,160 body bytes、dev89,416/test89,485 docs。全raw/clusterとretained 1,783,193 docsのtoken/index/文字往復を独立監査済み。初期Web 100%、first500M約0.66回露出。巨大master全量の証拠ではない。rawは`~/jmicro-data/phase6/raw/`、corpus/shards/全監査は`~/jmicro-data/phase6/expanded-v2/`。

②のWSD stable/独立decay CLIとNoNorm/math batch 8の全state再開・分岐完全一致は73 GPU checks / 74 tests、独立55 checksで完了。12 checkpointsとsnapshotをLinux `reports/phase6/preparation-20261003/cuda/`へ保持。[①②完了記録](26_phase6_preparation_completion.md)。新sourceの通常resumeは旧checkpointを拒否する契約を維持し、旧sourceはsnapshotへ保持。旧73 reportsとuv.lockのbyte保持は総合監査で確認済み。

## 今回の④⑤: 検証済み・本学習前で停止

**固定の短/1024入力・元のcache分割・全12数値比較が成功し、本学習設定をversion2として再凍結した。** [変換結果](../reports/phase6/nonorm_export_parity_report.json)、[独立した実CLI/重み監査149 checks](../reports/phase6/readiness_export_audit.json)、[全90 tests / skip・failure・error 0](../reports/phase6/readiness_precision_tests.xml)。

採用したCPU推論profileは `cpu-f32-f64-accumulation-v1`。FP32の重み・activation・cache・logitsを維持し、Linear/attentionの積和、RMSNorm分散、softmaxの和をFP64で累積する。SiLU/default RoPEのtrigも精度を上げる。Torch/HFの通常実行とcacheは完全一致、native1024の最大差0.0000124574は固定atol1e-5＋rtol1e-4以内。成果物metadataから実推論CLIも同じprofileを適用し、対応しないstock runtimeを拒否する。runtimeはLinux `artifacts/runtime-stable-f32-v2`、archive/patch chain/binary/shared librariesをhashで照合する。CPU精度優先の経路で、stock FP32やCUDAの同精度を保証する結果ではない。

旧stock FP32の失敗、RoPE周波数だけを修復した失敗、CPU8設定とCUDA参照の失敗を保持する。第1層q_projからの誤差増幅を[159 stageで追跡](../reports/phase6/nonorm_cache_precision_trace.json)した。2つ目の修復案で累積精度を上げ、途中版の4要素の未達はtrig丸めの差を修復して解消した。[修復の採否と保持](../reports/phase6/nonorm_precision_repair_report.json)。許容値・入力・必要な比較・学習済み重みを変更して通過扱いにしていない。

GPU学習coreのmodel/shards/training/uv.lockとreadiness worker/evaluatorは変更していない。高速CUDA/BF16経路にはCPU profileを適用せず、LR比較・保存再開の実測を維持する。LR0.001/0.002/0.003は各2,000 stable＋独立100 decayで完了、固定dev256文書BPBは1.18776153/1.18404703/1.18739314。0.002を採用。新sourceのstable400/200+200・decay100/50+50は50 checks完全一致、cold200→400は25 checks完全一致、親全file不変・元継続も成功。[GPU独立106 checks](../reports/phase6/readiness_gpu_audit.json)。合計7,500 updates / 245,760,000 input tokensは複数の準備runの台帳で、本学習系列ではない。

400生成は360.684秒、Unicode0/400、greedy EOS0/80・反復48/80で品質未達。全文dev89,416文書 / 164,344,743 bytes / 42,003,934 body tokensを336.292秒で採点しBPB1.2441264716、scalar/batch差0.0000330177（事前許容0.001以内）。旧pilotの直接改善量や人手文法評価の合格にしない。新CPU profileのcontrollerは実argmaxからのEOS/EOT停止と3 backendのgreedy IDsを実CLIで検証し、合成停止fixtureをモデル品質へ数えない。

[本学習設定version2](../configs/phase6/base_frozen.json)はbatch32・accum1・context1024、32,768 input tokens/update、LR0.002、warmup200、seed42、Flash/compile reduce-overhead/fullgraph/static/deterministic、WSD global305,176更新（10B丸め）、各観測点5%独立decay・floor0.1。save1,000更新ごと・全checkpoint保持、推定347件/41,702,694,225 bytes、run上限100 GiB・最低空き200 GiB。[起動/復旧計画](../reports/phase6/base_launch_plan.json)。`launch_enabled=true`は技術gateの成立を示すが、今回は起動しない。先の起動不可設定は[version1](../configs/phase6/base_frozen_blocked_v1.json)と[実起動拒否証拠](../reports/phase6/base_launch_guard_report.json)へbyte保持した。

Linux deep evidenceは `reports/phase6/readiness-20261003/`、最終exportは同runの `export-stable-f32/`、source snapshot/logs/raw logits/weightsを保持する。GPU準備とCPU8設定のsupervisorはterminal complete、精度build/probe/正式検証/CLI/テストも終了。`93c7d1d`のcommit後にGPU compute processなし・Git cleanを確認した。完了したjobを再起動しない。

**次の行動は停止。ユーザーが再開した後に、凍結source/data/runtimeを照合し、既存process/checkpointを確認して500Mの新規Base学習から始める。** prepareが既定で、復旧は同じglobal予算のまま行う。500M/1B/2B/5B/10Bの段階評価、Chat trainer、mixture、Muon、学習後量子化品質は今回の範囲外・未実施として維持する。外部権限やdriver更新のblockerはない。

現在速度から500M約12分・10B約4時間は純学習の算術値。compile/startup/全文dev評価/400生成/保存/decay枝を含め、完成時刻の保証にしない。[予算](24_phase6_plan.md)。以前の状態は[Phase 5当時status](autonomous_status_phase5_20261003.md)と[復旧履歴](autonomous_history_20261003.md)に保持。
