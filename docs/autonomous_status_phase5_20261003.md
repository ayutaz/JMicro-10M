# Codex継続作業の現在地

最終更新: 2026-10-03（日本時間）。今後の担当は実作業・実測結果が変わるたびに更新する。

## ユーザー方針

環境整備から学習・評価・改善までCodexに継続して任せる。WSLパッケージ3.x、RTX 4090、uv管理を使用する。正式なmilestoneと条件は`15_project_roadmap.md`、手順は`windows_handoff.md`を正とする。

2026-10-03の追加指定: Python実行は環境確認・自律runner・テスト・一時スクリプトも含め`uv run --frozen`経由に統一する。Pythonは3.12.7、導入は`uv python install`、依存復元は`uv sync --frozen`、依存変更は`uv add`。system Pythonを直接呼ばず、固定環境が取得できない場合も代替しない。rootの`AGENTS.md`に恒久ルールとして追記した。

2026-10-03にユーザーがPhase 5の計画から完了までを指示し、Phase 4での停止を解除した。今回の区切りはPhase 5完了。Phase 6の本学習は起動しない。Git identityはlocalの`yousan <ka1357amnbpdr@gmail.com>`。

## 実際の状態

**最新: Phase 5完了。全比較・補助評価・独立監査が終了し、Phase 6前で停止中。** [詳細計画](22_phase5_plan.md)と`configs/phase5/plan.json`へ目的・合格条件・予算を固定した。固定blockの失敗を保持し、文書単位samplerへ修復した`34d932d`では全68 tests / skip 0と、新sourceのT8K/T4K/文書samplerのCUDA 200 vs 100+100全state一致が成功した。NoQK-NormのT4Kも全state完全一致を通過し、4構成のresume証拠を`reports/phase5/resume_report.json`へ保存した。100件overfitは6,000更新後、本文NLL/token **0.01277**、teacher accuracy **99.712%**、16-token continuation exact **100%**、EOS argmax/実生成停止 **100%**で全5 gateに合格した。raw証拠は`reports/phase5/overfit_report.json`に保存済み。品質目標の数値を維持した凍結は`5d6b72e`へ保存済み。公開25 payloadの固定revision/hash検証も成功済み。

10M smokeは600更新で保存・再開し、1,221更新 / **10,002,432 tokens**で終了。全更新・weights・optimizerの有限値、凍結設定、loss低下を独立に監査した。dev 924文書 / 1,633,458 bytesのBPBは初期**2.74787 → 1.41697**。固定dev 80件×5条件の400生成を実施し、IDから全flagを再計算して一致した。抑制ありgreedyはEOS **0/80**、反復 **63/80**、Unicode/role/emptyは各0/80で、Base/Chat品質目標は未達。文書末尾からの暗記EOS 100%と自発的な短文停止は区別する。smoke評価に約354秒を要した。`reports/phase5/smoke_report.json`と二つのsmoke auditへ保存済み。

T8Kの100M学習は**12,208更新 / 100,007,936 tokens**で終了し、最終checkpoint SHA `a9dbdc35b5212a899cc3d6e6aad58a8338d50944a83d94f7497a5555dc6f035e`を保存した。全更新・weights・optimizer有限、source snapshot/hash・shard binding・予算一致を独立に確認。first/last 100更新の平均loss **7.7029 → 2.8532**、定常中央値 **117,119 tokens/s**、学習workerの実時間約14分26秒。全dev BPB **1.25886**でsmokeの1.41697から改善、共通短文windowと固定400生成も終了してID/flagを独立に照合した。抑制ありgreedyはEOS **0/80**、反復 **54/80**、Unicode/role/empty各0/80。文書末尾EOS argmaxは19.81%。`reports/phase5/100m-t8k_training_audit.json`と`100m-t8k_evaluation_audit.json`へ保存。smoke対100Mのpaired CIは文書不確実性を測り、学習seedの変動やbudget/schedule以外を揃えた純粋なscaling証明とはしない。候補の採用判断は全比較後に完了した。

T4Kの100M学習も**12,208更新 / 100,007,936 tokens**で終了し、checkpoint SHA `71a1a3bf6e057ad6e290047fb3db0f8ec8723f7c54839a51d50f58d89206cfec`を保存した。学習workerの実時間約15分11秒。全更新/weights/optimizer有限・source snapshot・shard/予算一致を独立監査し、`reports/phase5/100m-t4k_training_audit.json`へ保存。全dev BPB **1.23182**、抑制ありgreedyのEOS **0/80**・反復 **53/80**・Unicode/role/empty各0/80。400生成ID/flagを再計算して一致し、evaluation auditを保存した。T8K BPB−T4K BPBは**0.02704、95% CI 0.02481〜0.02939**。共通短文BPBはT8K **1.65006** / T4K **1.59139**。Norm比較は有望なT4Kで実施した。baseline比較を`reports/phase5/tokenizer_baseline_comparison.json`へ保存。model familyは語彙以外のarchitecture寸法も異なり、純粋な語彙のみの因果比較とはしない。処理body bytesはT8K **476,090,448** / T4K **390,286,307**と異なり、同一token予算と同一bytes予算は区別する。近いcheckpoint予算の補助評価も完了した。

T4KのQK-Normなし100M学習も**12,208更新 / 100,007,936 tokens**で終了。checkpoint SHA `e5583927efc5aa2041648bcae23f1b618b70f002be334c3581dea23472447d07`、消費token digest **92e575d3…**はT4K baselineと完全一致し、supervised tokens/body bytesも同じ。学習worker実時間約13分58秒。全更新/weights/optimizer有限・source snapshot・shard/予算一致を独立監査し、`reports/phase5/100m-no-qknorm_training_audit.json`に保存。全dev BPB **1.22144**、共通短文BPB **1.54659**。抑制ありgreedy EOS **0/80**・反復 **54/80**・Unicode/role/empty各0/80。全400生成ID/flagを再計算して一致した。Normありとの差は **0.01038 BPB、95% CI 0.00850〜0.01226**で、定常速度は約8.5%向上。比較を`reports/phase5/norm_comparison.json`、生成監査をevaluation auditへ保存。NoQK-NormのHF/GGUF adapterは未実装で、採否理由に変換リスクを記載した。最後のLR 0.001も同構成で終了し、BPB 1.23500で棄却した。

最後のT4K NoQK-Norm / LR 0.001も**12,208更新 / 100,007,936 tokens**で学習終了。checkpoint SHA `8f0d43540380bb174efa046bae5625ccf980814693dfa4e07e3de67fd8ce4631`、消費digest・supervised tokens/body bytesはT4Kの他2構成と同一。全更新/weights/optimizer有限・snapshot/source/data/予算を独立監査し、`reports/phase5/100m-lr001_training_audit.json`へ保存した。first/last 100更新の平均loss **7.2980 → 2.5904**、定常中央値 **121,046 tokens/s**、学習worker実時間約14分。全dev BPB 1.23500、共通短文1.61812。400生成のID/flagも独立照合し、greedy EOS0/80・反復52/80。LR 0.002よりBPBが0.01356悪く棄却した。

以下は完了済みPhase 4の証拠（2026-10-03 01:58 JST監査成功）。[完了記録](21_phase4_completion.md)とGit保存の`reports/phase4/handoff_report.json`を参照する。

- T8K/T4Kともsource-boundの連続200 vs 100+100で消費列digest / loss / weights / optimizer / scheduler / RNG / samplerが完全一致。64 tests / skip 0、CUDA評価RNG保全、共通bytes・本文一度採点・共通短文window、compile BF16 logitsの既定許容差内一致を監査した。
- dev 924文書 / 共通1,633,458 bytes、固定dev 80 prompt × 5 decoding条件を各モデルで評価。test未使用。検証checkpointのEOS停止0/80で、Base/Chat能力目標は未達と明記した。
- eager/default SDPA、FP32 parameters/BF16 autocast、context 1024、CUDA allocator 94%上限で、最大安定micro batchはT8K **57**（58 OOM）/ T4K **64**（65 OOM）。各3×200更新と評価/保存を通過。定常中央値225,169 / 218,411 tokens/s。
- 測定点の最高速度はcompile / batch 8で439,656 / 448,601 tokens/s。compile容量は未探索。Flash-onlyはnon-null mask非対応でraw失敗を保持し、成功と扱わない。default/math/compile-defaultは実測成功。
- 100M〜50Bのcompute時間と実ストレージを`reports/phase4/resource_budget.md`に保存。T8K eager最大batchの10B computeは約12.34h、評価/save/比較・取得処理は別加算。master corpus・Base/Chatの長期本学習は未実施。
- Linuxの`reports/phase4/gates-20261003/`に全ログ・snapshot・checkpointを保持。小さい集約reportをWindowsへコピーしGitへ保存。Phase 4 GPU jobは終了済み。Phase 4完了時点ではPhase 5は未開始だった。

## 実装と保存先

VRAM/高速化に関する現在の回答を[実測記録](../reports/phase5/performance_status.md)へ保存した。学習はWSL 2 / Ubuntu上でuv経由。今回のmath / batch 8比較は学習ピークallocated VRAM約3.9〜4.5 GiB、速度約11〜12万tokens/sで、VRAM最大活用・高速化完了ではない。Phase 4のcompile/default約44〜45万tokens/sは測定済みだが、Phase 5の厳密resumeに失敗したため採用しない。mathの最大安定batchとcompiled/mathは未検証。今回の凍結比較を途中変更せず完了し、本学習前の追加検証をPhase 6引継ぎへ残す。

Windowsの正本: `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`。Linux実行コピー: `/home/aihub_ubuntu/src/japanese-tiny-llm-10m`。LinuxのGit HEADは元の移行時のものを含み、実際の実行sourceはrun snapshotとimplementation hashで特定する。WindowsのPhase 4保存コミットは`3168d79`と`9cc4a75`、Phase 5完了コミットは`c3b857c`。最近のコミットはpushしていない。

- `scripts/train.py`: `build-shards` / `train` / `evaluate`を実装済み。trainはCLI引数を使い、baseline JSONの自動読込はしない。
- AdamW、FP32 parameters/BF16 autocast、gradient accumulation、warmup/cosine、mmap sampler、atomic checkpointを実装。Muon・WSD・Chat trainer・複数source mixtureは未実装。
- Web trainだけのpilot shardを`~/jmicro-data/shards/t8k-pilot`と`t4k-pilot`へ保存。T8K train 18,022文書 / 6,884,183 stream tokens / 32,774,150 body bytes。各split一本のuint16 binとJSON index/manifestを使用し、最終の不完全train blockは使わない。
- checkpointは完了updateでweights/optimizer/scheduler/Python・NumPy・torch・CUDA RNG/sampler/消費token・bytes/digest/config/data/source hashを保存する。環境・Git/PID・source snapshotはrun側へ保存する。

## 終了済みジョブと永続成果物

Phase 5の修復runは23 stageを完了し、Linux supervisor / GPU worker / Windows launcherは終了を確認した。停止証拠は`reports/phase5/process_completion.json`。raw runはLinux checkoutの`reports/phase5/run-20261003-docoverfit/`。Windows hidden wsl.exe PID **17168**、Linuxの実PID/boot ID/start ticks/active_stageは同directoryの`job.json`を正とする。起動前に旧supervisorとGPU workerの終了を確認した。

command: `bash scripts/run_phase4_job.sh scripts/run_phase5.py --output reports/phase5/run-20261003-docoverfit`。wrapperはuv/extras/data rootを設定する共通起動処理。Windowsにも同名directoryにlauncher.json/supervisor.logを保存する。supervisorとGPUの排他lockを使う。

棄却run `run-20261003`（compile/default）と`run-20261003-eager`（eager/default）はterminal failed、Windows PID 6688/24632は終了済み。消費列/RNGは一致したが重み・optimizer・lossが一致しなかった。6更新の切り分けではdefaultの重み差約3.9e-5、math-onlyは0。閾値を緩めずbackendを変更し、math-onlyのT8K 200 vs 100+100全state一致が成功した。raw失敗・checkpoint・診断を保持する。

`run-20261003-math`はT8K/T4Kの200 vs 100+100全state一致と初期評価を通過後、overfit-evaluationでterminal failed。Windows PID 15036 / Linux PID 437は終了済み。6,000更新のtrain loss約0.002に対し、文書単独のNLL/token 3.2063、teacher accuracy 65.40%、16-token exact 2%、EOS 69%。固定した連結blockの文脈に依存した疑いがある。raw失敗・checkpointを保持し、文書単位windowを使う修復runを新規初期化した。この修復runは同じ閾値で全5 gateに合格済み。予算6,000更新と全閾値は維持し、padding input slotsと実教師token数を分ける。通常のsmoke/100Mのblock samplerは変えない。

終了済みjobの記録: Windows supervisor PID 35316、Linux PID 404。Linux checkoutの`reports/phase4/gates-20261003/job.json`にboot ID/start ticks/stage、同directoryに全ログ・snapshot・checkpointを保持。Windows側にはlauncher/logと小さい集約reportを保存。GPU排他は`~/jmicro-data/gpu.lock`。再開時はPIDだけでなくboot ID/start ticksとcheckpointを照合する。

## 今回の完了と次回の境界

文書更新の[検証記録](../reports/phase5/documentation_update_20261003.json)を保存した。全current文書のリンク/anchorと既存CLI helpを確認し、Phase 0〜5の実験report 55 files、学習コード・lock・凍結protocol/Phase 5 planを維持した。Phase 6は起動していない。

ドキュメント更新（2026-10-03）: 目的・architecture・評価・研究課題に残っていたPhase 4停止/QK-Normなし未実装/100M未開始等の記述を実測へ更新した。次回のcorpus・WSD・再開/分岐・容量/高速化・生成/変換課題・段階評価と暫定見積もりを[Phase 6計画](24_phase6_plan.md)へ整理した。文書更新はPhase 6開始の承認ではなく、停止境界を維持する。

[Phase 5完了記録](23_phase5_completion.md)、[候補の採否理由](../reports/phase5/candidate_selection_review.md)、[独立監査](../reports/phase5/independent_audit.json)を保存した。候補はT4K / NoQK-Norm / LR 0.002の1つ。全68 tests / failure・error・skip 0、4構成のCUDA厳密resume、overfit全5 gate、smokeの実保存再開、4本の100Mと4補助checkpointの全dev/短文評価、各400固定生成のID/flag再照合が成功した。testとChat suiteは未使用。

主予算の全dev BPBはT8K 1.25886、T4K Norm 1.23182、T4K NoNorm 1.22144、NoNorm低LR 1.23500。近いbytesではT8Kが僅かに良く、近い時間ではT4Kが良い。予算依存・architecture寸法・cosine位置・1 seedという比較の限界も明記した。候補のgreedy EOS0/80・反復54/80、sampling Unicode2/240・EOS2/240で能力目標は未達。NoNormのHF/GGUF adapterは未実装。

実測worker時間は100M学習4本57.57分、smokeと4本の生成評価29.07分。修復runの成果物は約8.13 GiB / checkpoint73 files。古い失敗runは保持した。独立監査ではsource/data/hash、全更新・checkpointの有限値、単一要因、近似予算の最も近い実checkpoint、teacher/EOS集計とoverfit targetを検証した。部分監査の22項目も実reportと破損棄却で確認済み。過去Phase 0〜3 reportを変更しない。

今回の境界はPhase 5完了で停止。ユーザーがPhase 6を再開した場合は、拡張train corpus、WSDのstable/decay分岐・再開一致、math/compile/batchの容量/速度を検証して本学習予算を凍結する。100M cosine終端へ予算だけを足さず、選定した構成を次のcorpusで新規初期化する。Unicode退行・反復・停止・変換adapterも明示的な引継ぎ事項。Muonは安定したAdamW比較で候補を選べたため、今回は追加しない。Phase 6 jobは起動していない。

overfit用shardは作成・検証済み。以下は新規環境で必要な場合だけの形式（完了した比較を重複起動しない）:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py build-shards --tokenizer artifacts/phase2/8192/tokenizer.model --limit 100 --output "$HOME/jmicro-data/shards/t8k-overfit100"
```

`--limit 100`は各splitの上限で、train/dev/testを別々に保つ。train以外をoverfitへ混ぜない。実装済みCLIと再開条件は[引継ぎ手順](windows_handoff.md#6-実装済みcliと次回の再開)、未達の品質目標と20B/50B条件は[計画](15_project_roadmap.md)を参照する。

## 履歴

Full access反映前のアクセス拒否、旧driver、runnerによる復元、実装途中の観測は[履歴](autonomous_history_20261003.md)へ分離した。現在は会話内からWSL/network/CUDAへアクセスでき、ユーザー側でrunnerを起動し直す必要はない。
