# Codex継続作業の現在地

最終更新: 2026-10-03（日本時間）。実測の正本はreportとWSLのrun/data、今後のmilestoneは[roadmap](15_project_roadmap.md)。

## ユーザー方針と停止境界

Pythonは必ず3.12.7/uv管理で`uv run --frozen`から実行する。依存変更は`uv add`、復元は`uv sync --frozen`、system Python/pipへ代替しない。実学習はWSL 2 / Ubuntu / RTX 4090、WSL package 3.x。Git local identityは`yousan <ka1357amnbpdr@gmail.com>`、意味のある検証済み変更をcommitし、push/公開しない。

ユーザーがPhase 5の完了後に「phase6の1,2を目的とゴールを明確にして最後まで」を指定した。①データ拡充と②長時間学習準備は全証拠を揃えて完了した。[目的・完了条件](25_phase6_preparation.md)、[完了記録](26_phase6_preparation_completion.md)。**現在は①②完了で停止中。③の容量/速度探索と500M以上の本学習は、ユーザーが再開するまで起動しない。Phase 6全体の完了ではない。**

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

## 次の具体的な行動

今は停止する。再開後の目的・実装入口・探索予算案・完了条件を[③以降の実行計画](27_phase6_remaining_plan.md)へ具体化した。ユーザーが③以降を再開したら、まず採用NoNorm・拡張shard・WSDに対応する測定/厳密再開入口を実装・適応し、[Phase 6 gate](24_phase6_plan.md)のmath/compiled-math容量・速度・全state再開/分岐を確認する。既存Phase 4 benchmarkのNorm/pilot/cosineをそのまま流用しない。固定devでUnicode/反復/EOSと変換adapterを確認し、本学習予算・設定を凍結してから拡張corpusの新規初期化500Mへ進む。過去のTokenizer学習・Phase 3 export・Phase 5比較を重複実行しない。

準備の中断復旧/読み取り監査の**実CLI**は[完了記録](26_phase6_preparation_completion.md#実cliと再開)。完了済みjobを再起動しない。以前のPhase 5状態と全履歴は[当時のstatus](autonomous_status_phase5_20261003.md)、[Phase 5完了記録](23_phase5_completion.md)、[復旧履歴](autonomous_history_20261003.md)に保持した。

## 文書・計画更新（2026-10-03）

①②の完了証拠に合わせてREADME・roadmap・data/reports/eval・WSL handoff・研究/学習/評価文書を整合させた。WSD未実装という古い記述を修正し、実在する準備artifactと将来の本学習artifact、Phase 4 Norm/default容量と採用NoNorm/math未測定容量、pilotと拡張devの評価母集団を分けた。③容量/速度→④生成/変換→⑤本学習設定凍結の目的・有限探索・完了条件を明示した。stable予算延長forkと将来のPhase 6 heldout継承は未実装として残す。

文書更新の検証は[別監査report](../reports/phase6/documentation_update_20261003.json)に保存する。旧Phase 0〜6 report・実装/config/schema/tests・uv.lock・機械可読評価protocol・固定suite・過去status/完了記録を保持し、更新文書をWSL実行コピーと照合する。この作業ではGPU学習・データ再取得/再構築を起動しない。停止境界は①②完了のまま維持する。
