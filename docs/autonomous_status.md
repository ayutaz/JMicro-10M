# Codex継続作業の現在地

最終更新: 2026-10-03（日本時間）。今後の担当は実作業・実測結果が変わるたびに更新する。

## ユーザー方針

環境整備から学習・評価・改善までCodexに継続して任せる。WSLパッケージ3.x、RTX 4090、uv管理を使用する。正式なmilestoneと条件は`15_project_roadmap.md`、手順は`windows_handoff.md`を正とする。

2026-10-03の追加指定: Python実行は環境確認・自律runner・テスト・一時スクリプトも含め`uv run --frozen`経由に統一する。Pythonは3.12.7、導入は`uv python install`、依存復元は`uv sync --frozen`、依存変更は`uv add`。system Pythonを直接呼ばず、固定環境が取得できない場合も代替しない。rootの`AGENTS.md`に恒久ルールとして追記した。

2026-10-03にユーザーがPhase 5の計画から完了までを指示し、Phase 4での停止を解除した。今回の区切りはPhase 5完了。Phase 6の本学習は起動しない。Git identityはlocalの`yousan <ka1357amnbpdr@gmail.com>`。

## 実際の状態

**最新: Phase 5を再開して実GPU検証中。** [詳細計画](22_phase5_plan.md)と`configs/phase5/plan.json`へ目的・合格条件・予算を固定した。QK-Normなし候補、batched本文/EOS評価、paired bootstrap、永続supervisorを実装。全67 tests / skip 0と公開25 payloadの固定revision/hash検証が成功した。

以下は完了済みPhase 4の証拠（2026-10-03 01:58 JST監査成功）。[完了記録](21_phase4_completion.md)とGit保存の`reports/phase4/handoff_report.json`を参照する。

- T8K/T4Kともsource-boundの連続200 vs 100+100で消費列digest / loss / weights / optimizer / scheduler / RNG / samplerが完全一致。64 tests / skip 0、CUDA評価RNG保全、共通bytes・本文一度採点・共通短文window、compile BF16 logitsの既定許容差内一致を監査した。
- dev 924文書 / 共通1,633,458 bytes、固定dev 80 prompt × 5 decoding条件を各モデルで評価。test未使用。検証checkpointのEOS停止0/80で、Base/Chat能力目標は未達と明記した。
- eager/default SDPA、FP32 parameters/BF16 autocast、context 1024、CUDA allocator 94%上限で、最大安定micro batchはT8K **57**（58 OOM）/ T4K **64**（65 OOM）。各3×200更新と評価/保存を通過。定常中央値225,169 / 218,411 tokens/s。
- 測定点の最高速度はcompile / batch 8で439,656 / 448,601 tokens/s。compile容量は未探索。Flash-onlyはnon-null mask非対応でraw失敗を保持し、成功と扱わない。default/math/compile-defaultは実測成功。
- 100M〜50Bのcompute時間と実ストレージを`reports/phase4/resource_budget.md`に保存。T8K eager最大batchの10B computeは約12.34h、評価/save/比較・取得処理は別加算。master corpus・Base/Chatの長期本学習は未実施。
- Linuxの`reports/phase4/gates-20261003/`に全ログ・snapshot・checkpointを保持。小さい集約reportをWindowsへコピーしGitへ保存。GPU jobは終了済み。Phase 5は開始していない。

## 実装と保存先

Windowsの正本: `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`。Linux実行コピー: `/home/aihub_ubuntu/src/japanese-tiny-llm-10m`。LinuxのGit HEADは元の移行時のものを含み、実際の実行sourceはrun snapshotとimplementation hashで特定する。WindowsのPhase 4保存コミットは`3168d79`と`9cc4a75`。最近のコミットはpushしていない。

- `scripts/train.py`: `build-shards` / `train` / `evaluate`を実装済み。trainはCLI引数を使い、baseline JSONの自動読込はしない。
- AdamW、FP32 parameters/BF16 autocast、gradient accumulation、warmup/cosine、mmap sampler、atomic checkpointを実装。Muon・WSD・Chat trainer・複数source mixtureは未実装。
- Web trainだけのpilot shardを`~/jmicro-data/shards/t8k-pilot`と`t4k-pilot`へ保存。T8K train 18,022文書 / 6,884,183 stream tokens / 32,774,150 body bytes。各split一本のuint16 binとJSON index/manifestを使用し、最終の不完全train blockは使わない。
- checkpointは完了updateでweights/optimizer/scheduler/Python・NumPy・torch・CUDA RNG/sampler/消費token・bytes/digest/config/data/source hashを保存する。環境・Git/PID・source snapshotはrun側へ保存する。

## 実行中ジョブ

Phase 5の採用runはLinux checkoutの`reports/phase5/run-20261003-math/`。Windows hidden wsl.exe PID **15036**、Linuxの実PID/boot ID/start ticks/active_stageは同directoryの`job.json`を正とする。起動前に旧supervisorとGPU workerの終了を確認した。

command: `bash scripts/run_phase4_job.sh scripts/run_phase5.py --output reports/phase5/run-20261003-math`。wrapperはuv/extras/data rootを設定する共通起動処理。Windowsにも同名directoryにlauncher.json/supervisor.logを保存する。supervisorとGPUの排他lockを使う。

棄却run `run-20261003`（compile/default）と`run-20261003-eager`（eager/default）はterminal failed、Windows PID 6688/24632は終了済み。消費列/RNGは一致したが重み・optimizer・lossが一致しなかった。6更新の切り分けではdefaultの重み差約3.9e-5、math-onlyは0。閾値を緩めずbackendを変更し、math-onlyのT8K 200 vs 100+100全state一致が成功した。raw失敗・checkpoint・診断を保持する。

終了済みjobの記録: Windows supervisor PID 35316、Linux PID 404。Linux checkoutの`reports/phase4/gates-20261003/job.json`にboot ID/start ticks/stage、同directoryに全ログ・snapshot・checkpointを保持。Windows側にはlauncher/logと小さい集約reportを保存。GPU排他は`~/jmicro-data/gpu.lock`。再開時はPIDだけでなくboot ID/start ticksとcheckpointを照合する。

## 次の具体的な作業

実プロセスとjob/logを確認し、変更後のmath-only CUDA保存再開 → 100件overfit → 10M smoke → T4K/T8K 100M比較 → QK-Norm/LR比較 → 候補選定・監査を進める。失敗したgateはraw結果を保持して修復し、閾値を緩めない。Phase 6には進まない。文書更新は`aa932bb`へ保存済み。

Phase 5の設定・実装を検証済みの区切りでコミットし、最後に実測reportと候補config・採否理由を保存する。Tokenizer再学習・Phase 3全作業・完了済みPhase 4測定は繰り返さない。

overfit用shardはsupervisorが必要な場合のみ作成する。手動準備の形式（重複実行しない）:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py build-shards --tokenizer artifacts/phase2/8192/tokenizer.model --limit 100 --output "$HOME/jmicro-data/shards/t8k-overfit100"
```

`--limit 100`は各splitの上限で、train/dev/testを別々に保つ。train以外をoverfitへ混ぜない。実装済みCLIと再開条件は[引継ぎ手順](windows_handoff.md#6-実装済みcliと次回の再開)、未達の品質目標と20B/50B条件は[計画](15_project_roadmap.md)を参照する。

## 履歴

Full access反映前のアクセス拒否、旧driver、runnerによる復元、実装途中の観測は[履歴](autonomous_history_20261003.md)へ分離した。現在は会話内からWSL/network/CUDAへアクセスでき、ユーザー側でrunnerを起動し直す必要はない。
