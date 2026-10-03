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

④⑤のGPU準備比較は終了し、設定と証拠を保存した。**学習済み1024 logits/cacheの固定数値gateは未合格で、④⑤の総合完了は未達。固定1024系列の全stage追跡を完了し、最初の差は第1層のq_proj（FP32行列積）であると確認した。[全stage](../reports/phase6/nonorm_cache_precision_trace.json)。次はLinear/attentionの推論演算精度を修復し、元の短/1024・prefill/cacheの全12比較を再検証する。** 許容値・入力・必要な比較を削って通過扱いにしない。CPUのMKL分岐/threads8設定も終了し成功0、追加sweepしない。CUDA FP32参照の同じ12比較も終了し、短系列6件は成功、1024の5件は未合格。CPUだけの問題とは断定できず、[結果](../reports/phase6/nonorm_cuda_reference_report.json)を保持する。[今回の条件と全結果](30_phase6_readiness_execution.md)。

400生成は360.684秒、Unicode0/400、greedy EOS0/80・反復48/80で品質未達。全文dev89,416文書 / 164,344,743 bytes / 42,003,934 body tokensを336.292秒で採点しBPB1.2441264716、scalar/batch差0.0000330177（事前許容0.001以内）。旧pilotの直接改善量にしない。NoNorm HF/Llama・GGUF/Llamaの実greedy IDsと本物のargmaxからのEOS/EOT停止は成功したが、数値parityは未合格。[数値監査](../reports/phase6/nonorm_export_precision_failure.json)、[CPU8設定](../reports/phase6/nonorm_cpu_precision_report.json)。別runtimeは `artifacts/runtime-precise`、receiptに元archive/patcher/原・修正source/実binaryのSHAを保存。原runtimeと全失敗を保持する。

LR0.001/0.002/0.003の各2,000 stable＋独立100 decayは有限で完了し、固定dev256文書BPBは1.18776153/1.18404703/1.18739314。0.002を採用。新sourceのstable400/200+200・decay100/50+50・cold200→400のmodel/optimizer/scheduler/RNG/sampler/token/bytes/digest・全履歴が完全一致、親全file不変・元継続も成功。[結果](../reports/phase6/readiness_stability_report.json)、[独立106 checks](../reports/phase6/readiness_gpu_audit.json)、[全86 tests / skip・failure・error 0](../reports/phase6/readiness_tests.xml)。unique raw metrics7,500 updates / 245,760,000 input tokensは複数の有限準備runの合計で、本学習ではない。

[保存した本設定](../configs/phase6/base_frozen.json)はbatch32・accum1・context1024、32,768 input tokens/update、LR0.002、warmup200、seed42、Flash/compile reduce-overhead/fullgraph/static/deterministic、WSD global305,176更新（10B丸め）、各観測点5%独立decay・floor0.1。save1,000更新ごと・checkpoint全保持、推定347件/41,702,694,225 bytes、run上限100 GiB・最低空き200 GiB。[起動/復旧計画](../reports/phase6/base_launch_plan.json)。`launch_enabled=false`で保存し、CLIは未達gateで実行を拒否する。500M以上のBaseは開始していない。

Linux deep evidenceは `reports/phase6/readiness-20261003/`。GPU supervisor job terminal complete、Windows launcher12524、Linux supervisor476 / boot `a1175657-f036-4bff-abd9-0326a3f844a3` / start ticks10880は終了確認済み。CPU8設定supervisor21703 / start ticks114774もterminal complete。実GPU compute一覧と関連processなしを確認済み。完了したjobを再起動せず、logs/requests/checkpoints/source snapshotを保持する。環境はcmake/ninja/native runtime構築済み、blockerは外部権限・driverではない。実装と途中証拠は`7349470`・`dec6626`へcommit済み。

変換数値gateの修復・再検証と今回の④⑤の総合検証・commit後に停止する。500M→1B→2B→5B→10Bは次回再開後の段階評価で、今回は起動しない。Phase 5のBPB1.221443、greedy EOS0/80・反復54/80、sampling Unicode2/240は未達として維持。Chat trainer/複数source mixture/Muonも未実装。

現在速度から500M約12分・10B約4時間は純学習の算術値。compile/startup/全文dev評価/400生成/保存/decay枝/LR調整を含まず、完成時刻の保証ではない。[今後のgateと予算](24_phase6_plan.md)。以前の状態は[Phase 5当時status](autonomous_status_phase5_20261003.md)と[復旧履歴](autonomous_history_20261003.md)に保持。
