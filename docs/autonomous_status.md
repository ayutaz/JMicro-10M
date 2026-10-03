# Codex継続作業の現在地

最終更新: 2026-10-03（日本時間）。実測の正本はreportとWSLのrun/data、今後のmilestoneは[roadmap](15_project_roadmap.md)。

## ユーザー方針と停止境界

Pythonは必ず3.12.7/uv管理で`uv run --frozen`から実行する。依存変更は`uv add`、復元は`uv sync --frozen`、system Python/pipへ代替しない。実学習はWSL 2 / Ubuntu / RTX 4090、WSL package 3.x。Git local identityは`yousan <ka1357amnbpdr@gmail.com>`、意味のある検証済み変更をcommitし、push/公開しない。

①データ拡充と②長時間学習準備は完了した。[目的・完了条件](25_phase6_preparation.md)、[完了記録](26_phase6_preparation_completion.md)。その後、ユーザーが資源/VRAMの最大活用・torch.compile等の高速化の確認と不足対応を指定したため、**③の実装・測定・厳密再開を再開する。完了してcommit後、④以降と500M以上の本学習の前で停止する。Phase 6全体の完了ではない。** [今回の比較・完了条件](28_phase6_performance.md)。

## 実際の状態

Phase 0〜5は完了済み。Phase 6①で固定FineWeb2 Edu Japaneseの8 files / 2,152,539,810 raw bytesを取得し、T4K train **1,604,292 docs / 756,087,912 unique stream tokens / 2,946,200,160 body bytes**を作成した。dev 89,416 / test 89,485 docsを分離。全raw records、signature/near・URL edge/cluster、全retained **1,783,193** docsのtoken/index/文字往復を独立監査した。pilot全Web splitと固定suiteの検出された混入clusterを保護し、testは構造検証のみ。初期配合はWeb 100%、first 500Mは約0.66回露出。巨大master全量や新規10B unique corpusの証拠ではない。

Phase 6②でWSD stable/独立decay CLIと履歴を実装。採用T4K NoNorm / LR 0.002、実shard、CUDA/BF16/math、context 1024/batch 8でstable 200 vs 100+100、decay 100 vs 50+50のloss/LR/token列/model/optimizer/scheduler/RNG/sampler全stateが完全一致した。枝が元stable checkpoint/metrics/latest/runを変更せず、元継続結果も一致する。CUDA dev評価のRNG/model/mode保全を確認。**73 GPU checks / 74 tests、skip・failure・error 0**、最終独立監査は**55 checks**成功し、12 checkpoint・全snapshotと過去report 57 filesを確認した。準備GPU入力は計4,915,200 tokensで、生成品質や本学習の証拠にはしない。

Phase 5候補のBPB 1.221443、greedy EOS0/80・反復54/80、sampling Unicode2/240は未達として維持。NoNorm HF/GGUF adapter、Chat trainer/複数source mixture/Muonは未実装。math最大batch、compiled/math、本学習effective batch/LR/長期WSD配分は未測定/未凍結。Phase 4のcompile/default約44万tokens/sはPhase 5の厳密resumeに失敗して採用していない。

## 保存先・終了したjob

- Windowsのコード/Git正本: `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`。Linux実行コピー: `/home/aihub_ubuntu/src/japanese-tiny-llm-10m`。Linux Git HEADだけでsourceを識別せず、snapshotとimplementation hashを照合する。
- fixed raw/source/terms/receipt: `~/jmicro-data/phase6/raw/`。
- corpus/SQLite/signatures/uint16 shards/全監査: `~/jmicro-data/phase6/expanded-v2/`。
- GPU checkpoints/logs/source snapshots: Linux checkout `reports/phase6/preparation-20261003/cuda/`。
- data build/audit/readiness/CUDA jobは全てterminal complete・process identityの消滅確認済み。GPU compute processなし。Windows launcher 9960/23648も終了。新jobを起動する前に再検査する。
- 準備の[data manifest](../reports/phase6/corpus_manifest.json)、[corpus監査](../reports/phase6/corpus_audit.json)、[WSD report](../reports/phase6/wsd_resume_report.json)、[最終独立監査](../reports/phase6/completion_audit.json)、[内容確認](../reports/phase6/quality_review.json)、[失敗保持](../reports/phase6/preparation_failures.json)。

初回`expanded-v1`のdatasketch scheme失敗は保持し、明示legacy scheme＋scalar/LSH testで修正。schema不足も固定500M/容量/検証条件のschemaを追加して修正した。条件は緩めない。CPU小fixtureのfork警告2件はreportに残し、実data workerの全終了と全件監査は別に確認した。本文previewでは販促・navigation・見出し反復・翻訳調・古い情報を記録しており、品質の保証としない。

## 高速化の初回測定と修正（2026-10-03）

v1の短い比較ではreference/math約120k、compiled/math約273k、reduce-overhead/math約282k tokens/sだった。しかしcompiled Flashがmathと40更新loss・全model tensorsまで一致し、共用Inductor cacheにFlash ATen演算がなかったため、backendの実効を証明できずv1を採用証拠から除外した。v1のsnapshot/log/checkpoint/検査結果は保持。基準batch 8の53項目の厳密再開・枝検証は通過したが、全studyの完了ではない。workerのterminal OOM後にsupervisorを終了し、GPU compute processなしを確認した。

backend別cache namespaceとin-memory reset、実CUDA updateのATen operator検証、compiled Flash/reduce-overhead比較、最速math/Flash両方の容量探索を追加した。全79 tests / skip・failure・error 0を確認。v2のcompiled default Flashは実Flash演算を通過して約433k tokens/sを測ったが、reduce-overheadのCUDA Graph replayが内側のCPU hookを省略し、検査が誤って失敗した。v2も保持し、workerのterminal完了後にsupervisorを終了。CPU hookに加えてworkerが出力したcompiled code/backend call/SHAと実compiled graph呼び出しを確認するv3へ移った。[失敗記録](../reports/phase6/performance_failures.json)。

実行中study: Linux `reports/phase6/performance-20261003-v3`、Windows hidden launcher PID 24452。Linux `job.json`のPID/boot/start ticks・worker・stage/log/heartbeatと、各checkpoint/SHAから状態を確認する。同じGPU jobを二重起動しない。新しい採用設定・最大batchの判定は未完了。旧①②reportとsnapshot、uv.lockは保持する。

v3の7設定は実演算・有限値・小sample評価を通過した。[短い比較](../reports/phase6/performance_initial_probes.json)ではreference約120.5kに対してcompiled Flash/reduce-overhead約520.8k tokens/s（4.321倍）、batch 8のtraining peak約1.53 GiB。採用には厳密再開/容量/3×200が必要で、まだ採用しない。実装はcommit `1aa0d4d`。現在の文書45件/内部link 484件、全79 tests、旧73 reportsとuv.lockのbyte保持を別監査で確認した。

## 次の具体的な行動

③のpersistent performance studyを実行する。[実装・比較と実CLI](28_phase6_performance.md)。causalの学習専用経路、compile mode/fullgraph/static shape、決定的カーネルを実装し、全78 tests / skip・failure・error 0を確認した。新sourceなので旧①②checkpointの通常resumeは拒否する契約を維持し、旧snapshotとreportを保持する。新規probe/厳密再開/分岐/3×200の実測を保存し、最速と容量を別に選定する。③の完了後は停止し、④以降は[残る実行計画](27_phase6_remaining_plan.md)へ残す。過去のTokenizer学習・Phase 3 export・Phase 5比較を重複実行しない。

準備の中断復旧/読み取り監査の**実CLI**は[完了記録](26_phase6_preparation_completion.md#実cliと再開)。完了済みjobを再起動しない。以前のPhase 5状態と全履歴は[当時のstatus](autonomous_status_phase5_20261003.md)、[Phase 5完了記録](23_phase5_completion.md)、[復旧履歴](autonomous_history_20261003.md)に保持した。

## 文書・計画更新の履歴（③再開前、2026-10-03）

①②の完了証拠に合わせてREADME・roadmap・data/reports/eval・WSL handoff・研究/学習/評価文書を整合させた。WSD未実装という古い記述を修正し、実在する準備artifactと将来の本学習artifact、Phase 4 Norm/default容量と採用NoNorm/math未測定容量、pilotと拡張devの評価母集団を分けた。③容量/速度→④生成/変換→⑤本学習設定凍結の目的・有限探索・完了条件を明示した。stable予算延長forkと将来のPhase 6 heldout継承は未実装として残す。

文書更新の検証は[別監査report](../reports/phase6/documentation_update_20261003.json)に保存する。旧Phase 0〜6 report・実装/config/schema/tests・uv.lock・機械可読評価protocol・固定suite・過去status/完了記録を保持し、更新文書をWSL実行コピーと照合する。この作業ではGPU学習・データ再取得/再構築を起動しない。停止境界は①②完了のまま維持する。
