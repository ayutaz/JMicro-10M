# Codex継続作業の現在地

最終更新: 2026-10-03（日本時間）。実測の正本はreportとWSLのrun/data、milestoneは[roadmap](15_project_roadmap.md)。

## 方針と停止境界

Pythonは3.12.7/uv管理、全実行は`uv run --frozen`。依存変更は`uv add`、復元は`uv sync --frozen`。GPU学習はWSL 2 / Ubuntu / RTX 4090。Git local identityは`yousan <ka1357amnbpdr@gmail.com>`、検証済み変更をcommitし、push/公開しない。

**Phase 0〜5とPhase 6①②③は完了。ユーザーが「2まで計画を立てて進める」と指定したため、④生成/変換と⑤長期設定の確定を再開した。④⑤の検証・commit後に停止し、500M以上の本学習は開始しない。** [今回の比較と完了条件](30_phase6_readiness_execution.md)、[③完了記録](29_phase6_performance_completion.md)。

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

②のWSD stable/独立decay CLIとNoNorm/math batch 8の全state再開・分岐完全一致は73 GPU checks / 74 tests、独立55 checksで完了。12 checkpointsとsnapshotをLinux `reports/phase6/preparation-20261003/cuda/`へ保持。[①②完了記録](26_phase6_preparation_completion.md)。新sourceの通常resumeは旧checkpointを拒否する契約を維持し、旧sourceはsnapshotへ保持。旧73 reportsとuv.lockはbyte保持を別監査する。

## 次の具体的な行動

④⑤を[固定計画](30_phase6_readiness_execution.md)に従って実行中。NoNorm HF/Llama・GGUF Q/K row adapter、FP32 CEのbatch評価を実装し、全82 tests成功（失敗初回もLinux `reports/local/readiness_tests.xml`へ保持、成功は`readiness_tests_verified.xml`）。cmake/ninjaと固定native runtimeを構築済み。学習済みGGUFは初回のFP32比較で許容値を超え、元runtime/出力/logを保持してRoPEのFP32逐次乗算による位置依存誤差を診断した。独立周波数計算を使う別runtimeを構築し、許容値を変えず再検証する。Linux空き921,717,997,568 bytesを準備時に確認。準備前commitは`a786f59`、性能証拠は`a7d26e1`。Tokenizer再学習・完了済み比較は繰り返さない。

④⑤のGPU supervisorはLinux `reports/phase6/readiness-20261003/job.json`、Windows launcher12524、Linux supervisor476 / boot `a1175657-f036-4bff-abd9-0326a3f844a3` / start ticks10880、400生成worker513 / start ticks10999が実プロセス確認済み。GPU排他・stage/log・2秒heartbeat・完了更新checkpointで保持する。次はdev全文→LR3候補各2,000更新＋独立100 decay→変更後sourceの400/200+200・decay100/50+50・cold200→400再開。これは有限の準備比較で、本学習を起動しない。再開CLIはjob.jsonへ保存済み、source/config一致と生存プロセス確認後に使用する。別runtime CPUビルドのWindows launcher13528、Linux `artifacts/runtime-precise/build.log`。原runtimeは変更しない。

再開後は④でEOS/反復/Unicodeの400生成診断とNoNorm HF/GGUF adapter、⑤で採用batchに対するLR/effective batch/長期WSD・評価予算を凍結してから500M→1B→2B→5B→10Bを段階評価する。Phase 5のBPB1.221443、greedy EOS0/80・反復54/80、sampling Unicode2/240は未達として維持。Chat trainer/複数source mixture/Muonも未実装。

現在速度から500M約12分・10B約4時間は純学習の算術値。compile/startup/全文dev評価/400生成/保存/decay枝/LR調整を含まず、完成時刻の保証ではない。[今後のgateと予算](24_phase6_plan.md)。以前の状態は[Phase 5当時status](autonomous_status_phase5_20261003.md)と[復旧履歴](autonomous_history_20261003.md)に保持。
