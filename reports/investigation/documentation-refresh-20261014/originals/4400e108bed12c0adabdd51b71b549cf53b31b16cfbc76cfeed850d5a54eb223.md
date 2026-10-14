# 2026-10-05文書整理前の保存履歴

計画58完了・文書更新前の原文を保存する。以下の当時の「最新」「実行中」「次に実行」は現在の指示ではない。現在は[status](autonomous_status.md)、最新結果は[結果60](60_dataset_expansion_results.md)、次回の提案は[計画61](61_condition_preservation_next_plan.md)を参照する。既存の2026-10-03/04履歴・実験report/source/rawは変更しない。

## AGENTS.md

更新前file SHA256: `eb81cc738daf5dd8df98fcf24324deb8db893762d4f1dcc97ef3f85896c73508`

````markdown
# JMicro-10M development and training

Read `docs/autonomous_status.md`, `docs/15_project_roadmap.md`, and `docs/windows_handoff.md` before continuing. The status records actual results; `docs/57_matched_story_and_learning_budget_results.md` records the completed current scope. Older authorizations and dated progress notes are history and do not authorize a new experiment after the current stop boundary.

## Current state and scope

- Current stop boundary (2026-10-05 JST): plan58 stages1–3 complete. Short-story pool expanded from59,963,449 to200,000,192 tokens with140,036,743 new translated-story tokens. Both arms completed matched additional1,000,013,824 tokens with shared stable/decay schedule. Japanese diagnostics and all160 individual content reviews completed;35 primary evidence checks and20 completion checks passed. JCQA35.031→38.561% improved, but EOS34→25/coherence15→9/appropriate20→19 (each80); unchanged adoption gates fail, so candidate rejected and conditional full not launched. Source/length/EOS density changed; no amount-only causal claim. Scientific2,000,027,648/verification262,144 separate. Scientific239609 exited; original10B UI359102 actual process and HTTP parent SHA/tokens/busy=false restored. Report docs/60_dataset_expansion_results.md and portable evidence saved. Finish local delivery and stop; no new data/GPU/20B/50B/Chat/protected test/push/publication. Further diagnostics are proposals only. Older authorizations/stops/progress below are history.

- Latest user authorization (2026-10-05 JST): execute plan58 stages1–3: expand the short complete-text pool toward200M tokens, compare old/new pools at matched additional1B each, then Japanese/content evaluation, unchanged adoption gates, report/local commit/original10B UI restore and stop. Inspect actual source supply; disclose changes in source/length/EOS density and do not call them a pure amount effect. Respect the plan's preparation failure branch if200M cannot be supplied. Prior plan56 stop is completed history. No20B/50B/Chat/protected test/push/publication.

- Current stop boundary (2026-10-05 JST): plan56 stages1–3 complete. Matched content each500M and required retained-data constant-LR continuous1B/500M midpoint comparison, full Japanese diagnostics/all320 individual content reviews, judgment/report/31 final checks/original10B UI restoration are complete. Content condition rejected; learning amount improved semantics/repetition/BPB and coherence11 to19, but all primary/practical adoption conditions remain unmet. Conditional full not entered for either study. Scientific2,000,027,648/verification524,288 separate. GPU jobs234687/236557 and builder234279 exited. Original UI237483 is live. Save local delivery and stop; no new GPU/data/20B/50B/Chat/protected test/push/publication. The small semantic-learning diagnostic and LR-decay comparison in report57 are proposals, not launch instructions. Older authorizations/progress/stop boundaries below are history.

- Latest user authorization (2026-10-05 JST): execute stages1–3 of docs/56_matched_story_and_learning_budget_plan.md: matched story-content pools and each500M comparison, then selected fixed-data continuous1B study with constant-LR500M/1B checkpoints, Japanese/content evaluations and conditional full gates, judgment/report/local commit/original UI restore and stop. Stage2 remains required if stage1 candidate fails (use retained accepted story pool). No20B/50B/Chat/protected test/push/publication. Older plan54/52 stop boundaries are completed history and do not prevent this newly resumed scope.

- Current stop boundary (2026-10-05 JST): plan54 stages1–4 complete;110,000,202-token whole-document pool, one500M arm, complete Japanese diagnostics/all80 content review and judgment in docs/55_complete_document_500m_results.md. New condition rejected: EOS17/repetition31/coherence9/appropriate8 versus saved story37/18/19/19. Effective story fraction changed20percent to5.4531percent and EOS teacher density fell; this is not an amount-only effect. CPU12/CUDA25/primary22/completion51 checks passed. Ineligible conditional full was not launched. Original final10B UI restored; scientific232272 and builders exited. Save final local delivery and stop. Report55 next proposal is not authorization for new data/GPU work. No1B/20B/50B/Chat/protected test/push/publication. Older stop boundaries and authorizations below are history.

- Latest user authorization (2026-10-05 JST): execute stages1–4 of the newly presented fixed500M whole-short-document data comparison; see docs/54_complete_document_500m_execution.md. Prepare100–120M train-only improved whole-document pool, freeze actual sources/content/config, run one500M candidate with saved Web/story500M controls, evaluate under unchanged gates, report/commit/restore original UI and stop. Failed data readiness or selection follows the documented report-and-stop branch. Old plan52 is complete. No1B/20B/50B/Chat/protected test/push/publication.

- Current stop boundary (2026-10-05 JST): plan52 stages1–4 are complete, including20% lowerLR100M, its eligible full evaluation, prepared59,963,449-token pool with disclosed reuse, actual paired500M arms, all320 content diagnoses, eligible500M full/long, judgment and next proposal in report53. Primary37/full30 evidence checks pass;500M passes unchanged comparison gates and is a research candidate, while Base/Chat quality remains unmet. Scientific1,100,021,760/verification524,288 separate. All scientific/evaluation jobs exited and original final10B UI was restored. Save/verify final local delivery and stop. New pool, another500M/each1B/20B/50B/Chat/protected test/push/publication require a resumed user task; report53 is a proposal, not a launch instruction. Older authorizations below are history.

- Latest user authorization (2026-10-05 JST): execute stages1–4 of `docs/52_story20_low_lr_execution.md` following proposal51. Run one20% lowerLR100M arm with immutable saved matched Web control; evaluate eligible full/long only when original gates pass; run matched500M arms only if all full gates pass; otherwise judge the failure and propose the next diagnostic/content action. Finish judgment/report/local commit, restore original final10B UI and stop. No1B/20B/50B/Chat/test/push/publication. Prior completed stop-boundary bullets below are history and do not prevent this newly requested scope.

- Current stop boundary (2026-10-05 JST): plan49 stages1–3 are complete through the prespecified failure branch: normalLR10%100M, matched lowerLRWeb/10%100M, all240 content reviews, actual state/metrics/diagnostics checks, judgment and proposal in `docs/51_story10_judgment_and_next_proposal.md`. Both candidates fail the unchanged coherence gain8 gate (4/6), so conditional full/long and500M/pool expansion were not entered. Scientific300,023,808/verification524,288 tokens separate. Jobs139467/140216 exited; UI restored to original final10B. Save final report/local commit, then stop.20%lowerLR/500M/1B/20B/Chat/test/publication remain future proposals. Base/Chat quality targets remain unmet. Following authorization/progress bullets preserve history, not a new launch instruction.

- Latest user authorization (2026-10-05 JST): execute stages1–3 of `docs/49_next_mixture_and_training_budget_plan.md`, judge results and propose the next step. This resumes work beyond the earlier completed stop boundary. Execute the 10%100M fork with saved matched controls; if all adoption gates pass, prepare the required pool and run matched500M arms; otherwise run one bounded matched lower-LR comparison as planned. Then report/judge/propose, locally commit, restore the original UI and stop. No1B/20B/50B/Chat/test/publication. Record actual work in `docs/50_story10_and_budget_execution.md`. Prior completed jobs must not be restarted.

- Current stop boundary (2026-10-05 JST): requested stages1–3 are complete, including bounded data/EOS inspection,25,000,067-token candidate pool, three matched100,007,936-token arms from final10B,240 content reviews and prespecified eligible full/long evaluation. Primary35/full43 evidence checks pass. New-story EOS/repetition improved but parent BPB regression+0.001746 exceeds+0.001; candidate is not adopted and Base/Chat quality targets remain unmet. Save final report/local commit, then stop. No500M/1B/20B/50B, Chat, protected test or publication. Scientific/evaluation jobs exited; UI restored to original final10B. See `docs/48_complete_text_10b_comparison.md` and completion record.

- Model: 10,001,152 parameters; prepared Web train data:12,225,819,077 tokens; experimental story pool:25,000,067 tokens. Main Web training reached10,000,007,168 tokens; three comparison branches each reached10,100,015,104. Existing UI serves original final10B. Base/Chat quality targets remain unmet. The following dated bullets preserve earlier milestone history and do not supersede the stop boundary above.
- Direct10B preparation is complete at code commit `4c3fbaf`: frozen `configs/phase6/base_10b.json`, schema, dedicated runner/launcher,14 CPU tests and actualCUDA16-update/524288-token exact stable/decay save-resume verification. See `docs/40_base_10b_preparation.md` and `reports/phase6/base_10b_preparation_review.json`.
- Scientific10B training completed on 2026-10-04 at11:43:52Z: total10,000,007,168tokens/update305176; additional scientific tokens5,249,990,656 from saved4.75B stable parent. Stable9.5B plus final decay and all saved states/metrics passed19 CPU review checks. Linux427/Windows30148 exited. Verification tokens are separate. See `docs/41_base_10b_training.md` and `reports/phase6/base_10b_training_review.json`.
- Current stop boundary (2026-10-04): requested step3 final10B quality evaluation is complete: same full dev89,416/fixed400, all80 content and9 natural-stop review,23 CPU evidence checks. BPB0.954018 / fixed EOS0 / repetition53 / all400 raw Unicode0; original growth gate passes, Base/Chat quality remains unmet. Finish report/local commit, then stop. No further training, EOS finishing, decoder experiments, test selection, Chat,20B/50B or publication. See `docs/42_base_10b_quality_evaluation.md`.
- Training recovery entry: `bash scripts/run_base_10b.sh --train`; the current run is complete and must not be relaunched for more learning. Shell default and `--verify-only` perform preparation verification only; completed verification is reused. Do not restart completed old launchers.
- User request after evaluation (2026-10-04): implement and launch a local Web UI for the current final10B checkpoint. This permits local inference serving only; the training/experiment stop boundary above remains. See `docs/43_local_webui.md`. The WSL UI holds the GPU lock while serving; inspect its actual process and stop it before any separately authorized GPU job.
- Latest user scope (2026-10-04): implement additional Japanese Base evaluations and measure final10B. Completed: native likelihood scorer, pinned public data, semantic dev192, JBLiMP/JCommonsenseQA/JNLI/JCoLA official available evaluation data, JSQuAD100, external-body100, greedy128/512 twenty prompts each, CPU statistics, all160 Codex content scores and9 natural-stop diagnoses. See `docs/45_japanese_base_evaluation_v2.md`, `docs/46_japanese_base_evaluation_v2_results.md`, `reports/phase6/japanese_base_v2_review.json`. Eight CPU tests and15 evidence checks pass. GPU full320.820s; unique-context semantic revision1.686s. Preserve original raw/source snapshots; use corrected v2.1 report. Independent human blind/public Base reference/JMMLU remain unperformed/planned. UI restored. Evaluation/report/local commit is the current stop boundary; no training, protected test, publication or redundant benchmark reruns.

## Project rules

Plan49 stages1–3 completed in reports50/51; plan52 stages1–4 completed in report53 including its entered paired500M/full branch. Preserve original adoption gates and all saved evidence. Do not restart completed jobs or execute report53's future data proposal automatically. Stop after verified final local delivery and original UI restoration until the user resumes work.

The user has authorized autonomous implementation, repair, local GPU work, and required WSL preparation within the requested scope. Continue routine decisions and authorized milestone transitions without renewed permission. Authorization cannot change execution sandbox or managed policy.

- Target WSL package3.x, WSL2 Linux, RTX4090. Use pinned Python3.12.7 and uv; dependency changes use `uv add`. Preserve historical Phase0–3 reports and all prior checkpoints/results.
- Run every Python command through `uv run --frozen ...`, including probes, tests, automation and one-offs. Standard WSL extras are `--extra hub --extra data --extra ml --extra export`. Install Python with `uv python install 3.12.7`, restore dependencies with `uv sync --frozen` and required extras. Never invoke system python/python3/py directly or use pip. Python children may reuse `sys.executable` from a uv-launched parent. Record inaccessible pinned dependencies as blockers instead of falling back.
- Recover pinned public pilot/Tokenizer and verify hashes when restoration is necessary. Do not repeat completed Tokenizer training, Phase3 export, environment benchmarks, or GPU comparisons without new evidence.
- Follow the roadmap environment/shards/trainer/evaluation/save-resume/stable-batch requirements, then Base→Chat→quantization.20B/50B and other research require measured budgets, defined comparisons and completion conditions. Implement missing commands before executing them.
- Use train for learning; protect dev/test and fixed suites. Compare Tokenizers with common-byte BPB and labeled token/byte/GPU-time budgets. Chat loss supervises Assistant body plus EOT. Proposed settings, random CPU weights, and display repair are not GPU learning or quality evidence.
- Save optimizer/scheduler/RNG/sampler position and consumed counters at completed updates. Verify continuous vs resumed execution before long runs; retain measured stable batch and finite CUDA/BF16 forward/backward.
- Persist long jobs, logs, checkpoint paths and actual PID/boot/start ticks. Inspect actual processes/run records/GPU locks before launch; avoid duplicate jobs and resume valid checkpoints after interruption.
- Follow the user's preference for quick progress to learning: reuse accepted loader/build evidence, skip redundant full-corpus scans, deduplication and old GPU re-evaluations. Preserve the explicitly incomplete independent corpus audit as incomplete. Perform checks required by actual changes and checkpoint integrity.
- After meaningful work, run relevant checks, fix failures, update status with evidence/decisions/active jobs/next action, and commit appropriate milestones. Do not weaken acceptance gates. Preserve raw EOS/repetition/Unicode failures; constrained decoding is a separate policy and cannot repair the original learned raw gate.
- Stop for genuinely missing credentials, OS elevation/restart, inaccessible hardware or exhausted capacity; record the exact blocker/restart command. Do not repeat identical retries for transient failures.
- Work within this project and documented WSL/data environments. External publication, messages to other people and paid cloud jobs require separate authorization. Never expose credentials/secrets.
- Use repository-local Git identity `yousan <ka1357amnbpdr@gmail.com>`. Do not automatically push/publish. Windows is the authoritative Git workspace; sync execution files to Linux with LF and verify frozen source hashes.

For the non-interactive runner, return the requested JSON. `continue` means useful authorized work remains; `needs_user` means an external action is necessary; `complete` requires evidence that the requested scope is achieved, not merely a code change or overall project completion.
````

## README.md

更新前file SHA256: `cab0e0753041f1ee28883ad83e6d49ec7d098de9fc621881989e26e10752929d`

````markdown
# JMicro-10M

日本語の短文生成と数ターンの雑談を目的に、Tokenizerからスクラッチ構築する約10Mの言語モデル。現在のモデルは **10,001,152 parameters**、準備済みtrainデータは **12,225,819,077 tokens**。

最新（2026-10-05）: [教材内容と学習量の比較57](docs/57_matched_story_and_learning_budget_results.md)まで完了し停止。量/長さ/EOS位置を一致させた教材二組各500Mでは一貫性11→11/80で追加選別を不採用。従来教材固定・一定LRの500M→1Bでは一貫性11→19/80、反復21→10/80、意味60.4→66.1%と改善したが、原採用条件とBase/Chat品質は未達。科学計2Bは別枝の合計で、最長枝の累積は11B。全320内容/日本語診断/最終31checksを保存し元10B UIへ復帰。新GPU/20B/Chat等は未開始。[現在地](docs/autonomous_status.md)、[最終確認](reports/phase6/matched_story_completion.json)。以下は以前の結果と停止記録。

最新（2026-10-05）: [計画52](docs/52_story20_low_lr_execution.md)段階1〜4の学習・評価・判断を完了。物語20%条件は共通scheduleの100M→500MでEOS22→37、反復29→18、一貫性/適切完結9→19/80に改善した。500M全文BPB0.948798、Web対照比+0.888%・元10Bより改善、全文/長文とCPU30項目も成功し、原比較基準を通過した研究候補として採用する。意味・常識の改善とBase/Chat品質目標は未達。物語pool59,963,449 tokensを約1.667周使用し、新規unique100Mとは扱わない。[最終判断と次案53](docs/53_story20_low_lr_judgment.md)、[現在地](docs/autonomous_status.md)。報告/local commit・元final10B UI復帰で停止し、次のデータ構成比較は提案のみ。以下の旧結果・停止記録は履歴。

2026-10-04現在、主系列5Bと各100M仕上げ比較に続き、**総10,000,007,168 tokensの学習と保存状態19項目の確認を完了した。** WSL2/RTX4090で定常約69.5万tokens/秒、GPU時間約2時間8分。10Bの全文dev/固定400品質評価も完了した。BPB0.954018、固定EOS0/80・反復53/80、raw Unicode0/400。今回は報告・local commitで停止する。[評価結果と残る課題](docs/42_base_10b_quality_evaluation.md)。[10B学習結果と高速化](docs/41_base_10b_training.md)、[現在地](docs/autonomous_status.md)、[次の計画](docs/39_learning_scale_and_generation_plan.md)を参照する。

## ローカルで試す

現在の学習済み10Bモデルを使うWeb UI: **[http://127.0.0.1:7860](http://127.0.0.1:7860)**。文章の書き出しから続きを生成でき、生成量・Temperature・Top Pの調整、停止、コピーに対応する。推論はWSL/RTX4090で実行する。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/start_webui.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/stop_webui.ps1
```

[使い方と実行記録](docs/43_local_webui.md)。現在はBaseモデルで、Chat調整は未実施。

日本語Base追加評価を実装し、現在10Bモデルを実測した。JBLiMP sample SLOR74.62%、常識5択30.38%、独自意味診断59.38%。文法的な候補の選好はあるが、意味の両文脈正答・自由生成の展開・停止は弱い。[実施計画](docs/45_japanese_base_evaluation_v2.md)、[結果と評価の制限](docs/46_japanese_base_evaluation_v2_results.md)、[当初の棚卸し](docs/44_japanese_base_evaluation_audit.md)。独立人手blindと公式testは未実施。BPBや実装checks成功を、自然な文章生成の合格とは扱わない。

## 学習結果と残る課題

同じ全文devのBPB（小さいほど良い）と固定80生成で比較した。各5.1Bは別のモデルで、学習量を合算しない。

| 条件 | 全文BPB | 自然EOS / 80 | 反復 / 80 | 全400 raw Unicode失敗 |
|---|---:|---:|---:|---:|
| 元5B | 0.964484 | 0 | 59 | 2 |
| Web仕上げ5.1B | 0.958092 | 0 | 57 | 0 |
| 短文仕上げ5.1B | 0.959011 | 13 | 51 | 2 |
| 新10B | 0.954018 | 0 | 53 | 0 |

短文混合でEOS・反復は改善したが、途中不正UTF8とcap末尾切断が残り、最終採用条件は不合格。表示末尾helperは実装済みでもraw失敗を免除しない。数量・時刻・文脈の誤りも残り、Base/Chatの実用品質は未達。[比較と内容確認](docs/38_eos_5b_finish_results.md)。

## 次の実行

1. **10B設定準備は完了。** 関連14tests、実CUDA16updates/524,288検証tokensの全state/history保存再開一致、保存証拠26項目を確認した。
2. **直接総10B学習と保存確認は完了。** 手元の12.23Bデータを使い、保存stable4.75Bから9.5B stable＋最終decayへ到達した。7.5Bの中間実験と新データ収集は行っていない。
3. **step3: 同じ全文dev/400生成と内容比較は完了。** 本文予測・反復指標は改善したが固定自然EOSは0/80で、意味・数量・否定の誤りが残る。後続の短文仕上げ/UTF8制約/Chat等は別範囲。

中断復旧用のLinux repo内コマンド履歴。今回のrunは完了しているため再起動しない:

```bash
bash scripts/run_base_10b.sh --train
```

引数なしと `--verify-only` は検証専用。準備と本学習は完了しているので保存結果を再利用する。[引き継ぎ手順](docs/windows_handoff.md)で保存先と終了済みprocessを確認する。品質比較入口も実装・検証済みで完了runを再評価しない。

## 環境と保存先

Pythonはuv管理3.12.7。WSL2/RTX4090/Torch2.14.1+cu130で実GPU検証済み。Pythonは一時スクリプト・tests・自律runnerもすべて `uv run --frozen`、依存変更は `uv add`。通常のWSL復元には全extrasを維持する。

```bash
uv python install 3.12.7
uv sync --frozen --extra hub --extra data --extra ml --extra export
```

Git/コード/docsの正本はWindows workspace、Linux実行コピーは `/home/aihub_ubuntu/src/japanese-tiny-llm-10m`、大容量データは `/home/aihub_ubuntu/jmicro-data`。重み・shards・大きなraw evidenceはGit管理外なので、別PCには別途引き継ぐ。固定HubはpilotとTokenizerの復元用で、学習済み重みや12.23Bデータは含まない。[公開成果物の取得](docs/huggingface_handoff.md)。

準備完了コードは `4c3fbaf` でlocal commit済み。今回pushは実行しない。Linux側のGit HEADだけで実行コードを判断せず、凍結source/config hashを確認する。

## 文書と成果物

[docs一覧](docs/README.md)、[作業ルール](AGENTS.md)、[原ロードマップと品質条件](docs/15_project_roadmap.md)、[評価仕様](docs/evaluation_protocol.md)、[自律runner](docs/codex_automation.md)。過去の現在地メモは [履歴](docs/autonomous_history_20261004.md) に移し、Phase0〜3を含むhistorical report/weightsは保持する。

| 保存領域 | 内容 |
|---|---|
| src/jmicro・scripts | Tokenizer/model/training/evaluation/export/inferenceと実行入口 |
| configs・schemas | 凍結設定、入力とrun契約 |
| tests・eval | 実装checksと保護された固定suite |
| reports | 小さな結果・判断・監査。大型run/checkpointはLinux側に保持 |
| docs | 現在の計画・状態・引き継ぎと設計/完了履歴 |

Phase0〜5とPhase6の基盤・データ・学習比較は完了済み。過去の48/64/68/90/99等のテスト件数は各時点の証拠で、現在の全suite件数を表すものではない。今回の14件は10B準備に関連するchecksで、品質合格ではない。完了済みTokenizer学習・Phase3 export・GPU study・全データ照合を再実行する必要はない。
````

## docs/autonomous_status.md

更新前file SHA256: `32a7d37031b34ed13906d634c58eaeda14a696f2edd205f5785a857e7cdb2400`

````markdown
# Codex継続作業の現在地

計画58段階1〜3完了・停止（2026-10-05 JST）: 旧59,963,449から200,000,192-token物語poolへ拡張（新140,036,743）、同じ元final10Bから旧/新各追加1,000,013,824tokens・共通stable29,000/decay1,518を完了。全160生成の個別診断、意味192/JBLiMP331/常識1119/dev256、一次35・最終要求別20checks成功。旧→新BPB0.977154548→0.977322093、EOS34→25/反復15→14/一貫性15→9/適切完結20→19（各80）。JCQA35.031→38.561%は対応95%+1.877〜+5.139ppで改善、意味と文法の差の区間は0を含む。原一貫性/EOS・実用条件が未達で候補不採用、条件付き全文は未開始。source/長さ/EOS密度が変わるので量だけの効果ではない。科学2,000,027,648/検証262,144別、GPU3129.607秒、CPU5+LR2tests・実CUDA25成功。凍結v1のLR時点照合を独立v2で修正し、科学/採用条件は不変。結果はdocs/60_dataset_expansion_results.md、Windows dataset_expansion_{result,review,annotations,categories,judgment,completion}.json。科学239609は終了、元10B UI actual359102/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks7216365/ready08:29:21.306388Z、HTTP親SHA410f975d…/tokens10,000,007,168/busy=falseを確認。両11B checkpointと全metrics/source/rawはLinux runへ保持。Base/Chat未達、独立全corpus監査/人手blind未実施。local commitで今回停止し、次の条件保持・長さ/EOS密度を一致させる診断は提案のみ。新GPU/data/20B/50B/Chat/test/push/publicationは開始しない。以下は実行当時の履歴。

計画58段階2両1B完了・段階3 GPU評価中（2026-10-05 JST）: 新200M条件も追加1,000,013,824/総11,000,020,992/update335694を1464.648秒で保存（2026-10-05T08:26:23.459877Z、SHA7932c04d905c0903eee338f08da2b3c44f5bde8fffc8dae237381de1f15c9391を実ファイルと照合）。両枝Web800,063,488/short199,950,336で科学計2,000,027,648、検証262,144別。EOS教師新Web1,693,843/short1,161,577対旧short2,210,250で実密度差を保持。actual239609が両終端のdev256/80生成/日本語192・331・1119を実行中、stderr空。全160個別内容・CPU v2 evidence/gate判断・必要時全文、report/local commit/元UI復帰は未完了。科学学習を追加・再起動しない。

計画58段階2・新教材500M中間保存（2026-10-05 JST）: actual239609が新200M条件の追加500,006,912/総10,500,014,080/update320435を732.937秒で保存（2026-10-05T08:14:11.748544Z、SHA4e98847ed502ba86afeb137a9254558ed1f9446aa58d437139efb1b74a7ccd19を実ファイルと照合）。Web400,031,744/short99,975,168を対照と一致、EOS教師Web846,893/short578,635で短文EOS数は旧1,105,092の約52.36%。新sourceと長さ差の影響をそのまま保持する。実PID38分経過・stderr空で1Bへ継続中。対照1Bは完成、旧1B全30,518更新の実使用LRと保存後LRはv2 CPU照合で成功。新終端・両終端評価/160内容・採否・必要時全文・report/local commit/元UI復帰が残る。

計画58段階2・対照1B完了／新教材学習中（2026-10-05 JST）: actual239609が対照追加1,000,013,824/総11,000,020,992/update335694を1479.136秒で保存（2026-10-05T08:01:57.826188Z、SHA fd10dc1b358327bdbd8d3d58118c2cb096fc53d02b036f070e453911edf2b82aを実ファイルと照合）。Web800,063,488/short199,950,336、EOS教師Web1,693,843/short2,210,250。元final10Bから新200M条件へ同一jobで移り、actualPID稼働・stderr空を確認。metric.lrは使用した率、saved scheduler/optimizer.lrは次更新の率であり、旧CPU reviewerの照合に1更新ずれを発見。凍結した旧source/config/学習は変えず、別reviewer v2で使用率(step−1)と保存後率(step)を厳密照合し、実CPU scheduler境界と誤率拒否の2tests成功。品質gateは不変。新条件1B・両終端日本語/160内容・原gate判断・必要時全文/report/local commit/元UI復帰は未完了。

計画58段階2・対照500M中間保存（2026-10-05 JST）: actual239609が500,006,912追加/総10,500,014,080/update320435を745.994秒で保存。`control/checkpoint-00320435.pt` SHA c5658fc5891f30ebb007e58427d1453fcf9cb47687222411ae8078a0ff1344f3を実ファイルと照合成功。Web400,031,744/short99,975,168、EOS教師Web846,893/short1,105,092。07:50:05Z時点で15700更新へ続行、実psで同一PID/13分経過を確認しstderr空。科学ジョブは止めていない。段階3未完了、対照1B→新200M教材1B→両終端の日本語/全160内容・採否と条件付き全文、report/local commit/元UI復帰まで追跡する。観測用functionsセル2370は終了したがGPUジョブとは別プロセス。

計画58段階2開始（2026-10-05 JST）: 凍結commit03346a7。hidden Windows21040からwrapperを起動、actual Linux239609/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6902884を実psで確認。元UI停止、科学は新poolによる実CUDA保存再開を開始したところ。Linux reports/phase6/dataset-expansion-1b-20261005/screen-job.jsonとWindows同run stdout/stderr/launchを追跡し、再起動しない。旧60M/新200M各追加1Bの終端、日本語全診断・全160内容と採否、report/local commit/元UI復帰が未完了。

計画58段階1完了・段階2凍結（2026-10-05 JST）: 新pool200,000,192tokens/1,161,923全文（旧59,963,449＋新TinyStories日本語訳140,036,743）。元sourceの選別緩和やコピー増量ではなく、別公開trainを追加。準備145.021秒/1800秒、40全文の個別診断で弱例18を開示、CPU5tests成功。平均長88.462→170.129/EOS密度11.054→5.810で量だけの比較ではないとGPU前に具体化した。docs/59_dataset_expansion_execution.md・新config/schema/runner/reviewerを凍結。次は実CUDA stable/decay保存再開→旧/新各追加1B（同じ20%/stable29000・decay1518）→全日本語・160内容/原gate判断・必要時全文→report/local commit/元UI復帰で停止。科学はまだ未開始。Linux教材builder238695終了、元UI237483を保持。

計画58段階1〜3を再開（2026-10-05 JST）: ユーザーが「3まで進めてください」を指示。200M教材供給の実確認・必要分準備→旧/新各追加1Bの同条件学習→日本語/全160内容と原条件の採否判断、report/local commit/元UI復帰で停止する。actual process確認で科学学習なし、元UI237483稼働、WSL空き490GiB。新TinyStories日本語訳と合成教科書の公開train供給をpinして確認する。旧source現条件60M枯渇を避けるためだけのコピー・選別緩和はしない。新sourceの実量/長さ/EOS密度が変わる場合は開始前に比較条件を具体化して開示する。科学未開始、20B/Chat/protected test/pushは対象外。

教材増量の次回比較案（2026-10-05 JST）: ユーザーのデータセット増量提案を受け、既存Web12,225,819,077/物語59,963,449 tokensと供給枯渇の記録を確認。docs/58_dataset_expansion_proposal.mdに短い完結教材200M目標・旧60Mとの各追加1B/同じ20%配合/共通減衰比較を具体化した。別source・長さ・EOS密度が変われば量だけの効果とはしない。新200M供給の成立は未確認、取得・構築・GPUは未開始。結果57・原採用基準と完了ジョブは保持する。今回行った作業は次回案の保存のみで、計画56完了の停止状態と元10B UIを変更していない。次の具体作業案は未使用train供給を1,800秒以内で調査し、目標量・長さ/EOS密度・内容の成立を凍結すること。

計画56段階1〜3完了・停止（2026-10-05 JST）: matched教材各22,977,241tokens/253,119全文の各500M比較を完了。対照→追加選別はEOS39→44/反復16→17/一貫性11→11/適切完結14→15（各80）で不採用。段階2も省略せず旧59,963,449-token物語固定/一定LR0.0001で連続1Bを完了し、500M→1BはBPB0.982953243→0.981611241/EOS31→35/反復21→10/一貫性11→19/適切完結15→20。意味60.417→66.146%（対応95%+1.563〜+10.417pp）と複数指標は改善したが、一貫性95%下限0、EOS35<37、内容各27未達、Web BPB比+1.0335%で原採用条件未達。両条件付き全文は未開始。CPU10tests/実CUDA25・13/一次32・29/最終要求別31checks成功、全320内容保存。科学2,000,027,648/検証524,288別、一次GPU3331.359秒。元final10B UI actual237483/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6728695/ready07:08:04.599378Z、HTTP親SHA410f975d…/tokens10,000,007,168/busy=falseとactual process確認。科学234687/236557/教材234279は終了し再起動しない。結果と提案はdocs/57_matched_story_and_learning_budget_results.md、最終確認reports/phase6/matched_story_completion.json。11B checkpoint・両run全raw/metrics/source/annotationsをLinuxへ保存。追加学習の効果を否定せずBase/Chat未達、次の小規模条件保持教材診断/LR減衰/新data/GPU/20B/50B/Chat/protected test/pushは提案のみで未開始。local commitで今回停止し、以下は実行当時の履歴。


計画56段階2・500M中間保存／連続1B学習中: actual236557が500,006,912追加/総10,500,014,080/update320435を746.529秒で中間保存（SHA 17cb40a158c51a52e93ff31ba492067fff9c9cbebaa784da167fe036da60aad0）。Web400031744/story99975168、EOS教師Web846893/story1105092、一定LR0.0001。評価を挟まず同じ学習を1Bまで続行中。500Mを新たな科学枝として重複計上しない。新一定LRの実CUDA13checks成功/検証262,144別。1B終端/両地点日本語・160内容/最終判断は未完了。


計画56段階2実行中: hidden Windows34216/actual Linux236557/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6560977。旧59,963,449-token物語を固定、一定LR0.0001/30518更新/科学1,000,013,824tokens、500M中間と1B終端を保存し1B後に両地点評価する。新一定LRの実CUDA保存再開を実行中、科学は未完了。Linux reports/phase6/story-constant-lr-1b-20261005/screen-job.json・fixed20/metrics.jsonl/latest.json と Windows同runログを追跡。段階1科学234687終了・32evidencechecks成功/内容改善未達、commit04acf40。段階2全160内容/必要時全文/最終判断/report/commit/UI復帰まで進め停止する。


計画56段階1完了／段階2凍結: matched各22,977,241-token教材で各500,006,912追加tokens、実EOS教師Web846,893/story1,101,267を一致。GPU1659.584秒・科学1,000,013,824/検証262,144別。dev/日本語全完了・全160個別内容・CPU32evidencechecks成功。対照→候補BPB0.979944438→0.980233205、EOS39→44/反復16→17/一貫性11→11/適切完結14→15（各80）、対応95%−8.75〜+8.75ppで改善条件未達・不採用。条件付き全文は開始しない。次は旧採用59,963,449-token物語pool固定、元10Bから一定LR0.0001で追加連続1,000,013,824tokens、500M中間/1B終端を保存して両地点評価。段階1科学234687終了、元UI235943へ復帰確認済み。段階2config/schema/sourceを凍結したが新科学はまだ未開始。


計画56段階1・対照500M学習完了／候補学習中: actual234687が対照500,006,912追加tokens/総10,500,014,080/update320435を745.075秒で終端保存（SHA d6d3009c23870ffcefba93afade16107840cc4eaa2d4a836f1960384b1dc0971）。Web400031744/story99975168、EOS教師Web846893/story1101267。同じ元final10Bから候補500Mへ移った。一次評価/全160内容/条件付き全文/段階2固定1B/最終判断は未完了。同じ実行を追跡し重複起動しない。


計画56段階1〜3実行中（2026-10-05 JST）: 二組各22,977,241tokens/253,119全文、body平均88.7764（旧88.4621）、同じ長さ並び/BOS/EOS位置。CPU抽出11.146秒、random40各に弱例14/12を個別明記してbounded比較を受入。CPU10tests成功・凍結commit a8215aa。2026-10-05 06:09頃、hidden Windows34620/actual Linux234687/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6377461で教材二条件各500Mを開始。実CUDA25checks通過、対照学習中。Linux reports/phase6/matched-story-content-500m-20261005/screen-job.json と Windows同run screen.stdout.log/stderr.logを追跡。UIはGPU中停止/finally復帰。段階1未達でも段階2の固定教材・一定LR連続1B（500M中間/1B終端）は必要。全320内容と日本語評価・事前条件付き全文、判断/report/local commit/元UI復帰で停止。科学・一次結果は未確定、20B/Chat/test/pushは開始しない。


新計画56段階1〜3をユーザーが再開許可: 量/長さ/EOS数を一致させた物語教材二組各500M→選択教材で一定LR連続1Bの500M/1B比較→日本語/内容診断と判断/report/commit/UI復帰で停止。教材候補未達でも学習量比較を省略せず旧採用poolを使う。1Bは今回範囲、20B/Chat/test/pushは開始しない。既存GPUjobなし・元UI232991のみ。実装/教材準備中、科学GPU未開始。

2026-10-05 JST・新計画54段階1〜4完了: train全文pool110,000,202 tokens（物語30M/Web80M）、一様ランダム40全文の弱例8を明記して受入、12CPUtests/実CUDA25save-resume/一次CPU22/最終要求別51項目成功。同じ元10Bから一条件500,006,912科学tokens（検証262,144別）、学習745.510秒・一次GPU853.678秒。BPB0.972888865/EOS17/反復31/一貫性9/適切完結8（各80）、日本語192/331/1119全完了・全80個別Codex診断。保存物語500MのEOS37/反復18/一貫性・完結19から悪化し、新改善条件未達で不採用、条件付き全文/400/長文は未開始。物語実比率20%→5.4531%、short EOS教師約111万→約61万で、増量だけの効果ではない。データ量・学習量不足を否定せず、次案は実物語比率/長さ/EOS密度を揃えた内容比較として報告55に保存（未実行）。科学232272/教材231819・231975は終了。元final10B UI actual232991/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6169021、HTTP親SHA410f975d…/tokens10,000,007,168/busy=falseとactual processを確認。報告/判断/要求別確認/local commitで停止。Base/Chat品質未達、1B/20B/50B/Chat/protected test/push/publicationは未開始。以下は当時の履歴で旧jobを再起動しない。

計画54・科学500M完了/一次評価中: actual232272がwhole20の追加500,006,912/総10,500,014,080/update320435を745.510秒で学習し終端を保存した。Web400,031,744/short99,975,168、EOS教師Web846,893/short607,745（旧物語short1,105,092より少ない）。同じjobがdev256/80生成/日本語192・331・1119を実行中。科学と検証262,144は別会計。80内容の個別採点・実CPUreview/条件付き全文・段階4採否/report/commit/UI復帰は未完了。重複学習や旧対照の再実行をしない。

計画54・段階2実行中: hidden Windows32072/actual Linux232272/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6083120、2026-10-05T05:20:28.697566Z起動。新110M教材を使う実CUDA exact save/resume25checks通過、検証262,144tokens別会計、whole20追加500Mの学習中。Linux reports/phase6/complete-document-500m-20261005/screen-job.json、Windows同run screen.stdout.log/screen.stderr.logとcheckpoint/latest.jsonを追跡。一次1800秒、必要時保存checkpointから同じ凍結条件で再開し、重複起動しない。UIはGPU中停止・wrapper finallyで元final10B復帰。一次評価/全80内容診断・条件付き全文・判断/報告/commit/停止は未完了。データと凍結実装のlocal commit aa53975。

計画54・段階1完了: 新pool110,000,202 tokens=story30,000,063/Web80,000,139、668,680全文、抽出累計73.340秒。最初4Bで量未達後、原条件を維持して未走査範囲だけ6.84Bまで継続し必要量で停止。一様ランダム40全文に弱例8を明記してbounded研究比較として受入、独立意味/事実/unique認証ではない。CPU12tests成功、実量/config/schema/source/対照を凍結。次に新データ実save/resumeと一条件500Mを1800秒以内で実行し一次評価・全80内容診断へ進む。旧対照の再学習なし。

2026-10-05 JST・新計画54の段階1〜4をユーザーが再開承認: 固定500Mで短文データ構成/準備量を改善する一条件を実行する。目標110M=低反復物語30M+短いWeb文書全文80M、trainのみ、CPU1800秒/Web最大4Bの必要分だけ抽出、無作為40全文を開始前確認。段階1教材builder/選別を実装し関連tests後に起動する。元UI231106のみ稼働、旧科学/evaluationは終了済み。保存Web/物語500M対照を再利用し、原条件を維持して採否/report/local commit/元UI復帰まで進め停止する。旧計画52の完了境界は履歴で新計画を阻まない。

2026-10-05 JST・計画52段階1〜4の実験/評価/判断完了: 20%低LR100Mと全文通過後の各500M・四地点一次・全320内容診断・500M全文/400/長文を完了した。500M一次CPU37/全文CPU30項目成功、候補は全文BPB0.948798235（親より−0.005220237、Web比+0.887930%）、固定EOS37/反復18/一貫性・適切完結19（各80）、全400 EOS179/反復36/Unicode・role・empty全0、長文128/512はEOS各12/20・文再出現各6・UTF-8失敗0で原条件を全通過。研究候補として採用するが文法38/80・停止37/80等のBase/Chat品質目標は未達。[最終判断/次案53](53_story20_low_lr_judgment.md)に同量500Mで短文教材構成/準備量を変える一条件を提案し、今回は実行しない。物語準備量59,963,449/消費99,975,168は約1.667周、科学計1,100,021,760/検証524,288別会計、GPU計6,007.147秒。実科学143237/174280・全文143904/177987・教材173735は完了して終了。元final10B UIがactual231106 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4964393 / ready02:14:01.602203Zで復帰し、HTTP SHA410f975d…/tokens10,000,007,168/busy=falseとactual processを確認した。判断JSON・要求別最終確認・local commitを保存して停止する。新pool/別500M/各枝1B/20B/50B/Chat/protected test/pushは未開始。以下の実行中・未完了記録は当時の履歴で、旧jobを再起動しない。

500M全文・Web側完了／候補側全文中: Web全文BPB0.940447718183、固定80 EOS0/反復62、全400 EOS10/反復128/Unicode・role・empty全0。長文128/512各20はEOS0/0、文再出現9/11、4gram反復0.839971/0.959310、raw失敗0。実source/hashとこの途中結果を`reports/phase6/story20_budget_full_progress.json`へ保存し、候補の合否はnullのままにした。actual177987が`coherent20-full`へ移り、起動約18分38秒で本文53,248/213,432 windows、stderr空、actual process存在を再確認。最終全文合否・段階4・UI復帰は未完了。320内容の対応変化も保存し、一貫性改善12/喪失2件、EOS新規18/喪失3件、適切完結率は実EOS中40.9%→51.4%。旧100Mに対する全品質の優位や意味能力改善は主張せず、結果を報告53へ追記した。同じ177987の完了を待ち、実CPU全文reviewと最終判断/報告/確認/local commit・元UI復帰まで進めて停止する。

500M全文の途中実測: Web対照の89,416文書/164,344,743本文bytes/42,003,934本文tokensを採点し、全文BPB0.940447718183を保存した。actual Linux177987のforward_callsが進み、生成評価を継続中（起動約8分21秒でactual process再確認、stderr空）。候補側・長文・原全文条件はまだ未確定。320採点のカテゴリ集計を`story20_content_categories.json`へ保存、物語一貫性は短い物語0→4/8、描写0→3/8、数字0→0/8。各8件の記述的集計で新gateではない。判断53に同量500Mで短文教材の構成/準備量を変える次案を準備し、今回のfull結果後に確定する。新pool/追加学習は未開始。最終確認runnerに別凍結full plan/source snapshotと具体的次案/report hashの確認を加え、uv構文確認済みだが最終実行はfullと段階4完成後に行う。次は同じ177987の完了→実CPU全文review→採否/報告/最終確認/local commit/UI復帰で停止する。

段階3・全320内容診断と一次review完了／500M全文・長文評価中: 全四条件80件ずつのrawを個別確認・採点し、実CPU37項目をすべて通過した。Web中間/終端の一貫性2点・適切完結は0/0、物語は9/19（各80）。物語の100M→500M差は+12.5pp、対応95%区間[+3.75,+21.25]。意味−1.042pp・常識−0.357ppはいずれも区間が0を含み、JBLiMP+3.021ppは[+0.302,+6.042]。終端の元一次条件を全通過したため、追加学習0の全文89,416/固定400/長文20prefix128・512を2026-10-05 01:41:50.837298Zに永続起動した。hidden Windows34068 / actual Linux177987 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4771336、actual process存在を確認。Linux`reports/phase6/story20-low-lr-10b-500m-20261005/full/full-job.json`とWindows同run`full.stdout.log`/`full.stderr.log`を追跡する。上限3,000秒、元親の保存結果を再利用。UIはこの評価中だけ停止し、finallyで元final10Bへ戻す。最終全文合否・段階4採否/次案/報告/local commitは未完了。同じ177987を追跡し、完了済み科学174280や旧100M全文を再起動しない。以下のpartial160/320等は履歴。

段階3・科学/一次GPU完了／内容160/320保存済み: 新しい二枝各500Mと四地点のdev256/greedy80/意味192/JBLiMP331/常識1119評価を終了した。GPU1,878.712秒、科学1,000,013,824/検証262,144は別会計、actual Linux174280は終了。Web中間→終端はBPB0.978642327→0.971570249/EOS0→0/反復55→62、物語は0.985129409→0.979911453/EOS22→37/反復29→18（各80、raw失敗全0）。物語意味63.021%→61.979%、JBLiMP75.529%→78.550%、常識33.870%→33.512%で一律の能力改善とはしない。Web160件を全文確認・個別採点し、二つの`story20_budget_annotations_web_*.json`へ保存、Linux`annotations.json`はpartial160/320。物語160件の個別内容診断・全320CPU review/原gate判定・条件付き全文/長文・段階4判断/次案/完成報告は未完了。元final10B UIはactual176353/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe、start ticksはserver.jsonと`story20_budget_result.json`の現在identityを参照、HTTP SHA410f975d…/tokens10,000,007,168/busy=falseを確認した。科学jobは再起動せず、残る内容診断から続ける。

段階3・二枝各500M学習完了／一次評価中: actual Linux174280が起動約25分3秒時点で`web-greedy80`へ移ったことを確認。物語枝は追加500,006,912/総10,500,014,080/update320435、Web400,031,744・short99,975,168、学習735.280秒、終端SHA f336806bee562cf11fe29506f833deae45de228c4b8acb1b942c7df21c82daac。保存short samplerはepoch1/position39074/blocks58558で、一周完了＋第二周の一部を実際に使用した。Web枝は747.396秒、二枝の科学計1,000,013,824で、一つのモデルの累積に足さない。各100M中間も保存済み。一次四条件のBPB/80生成/日本語診断→全320内容採点→原gate条件付き全文→段階4採否・次案・報告・local commit・元UI復帰が残る。新しい科学GPUを起動せず、同じjobの評価を追跡する。

段階3・Web500M学習完了／物語20%学習中: actual Linux174280が起動約13分5秒時点で`coherent20-train`400更新へ移ったことを確認、stderr空。Web枝は15259更新/追加500,006,912/総10,500,014,080/update320435を747.396秒で学習し、終端SHA d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4を保存した。物語枝は同じ元final10Bから別に学習中。中間/終端の一次評価・320内容診断・条件付き全文・段階4採否/次案は未完了。[判断53](53_story20_low_lr_judgment.md)は100M実測と残要件を保存した途中原稿。元UIはGPU中のみ停止し、finally復帰予定。科学174280の同じ実行を追跡し、重複起動しない。

段階3実行中・Web中間100M保存済み: actual Linux174280を起動約3分8秒時点で再確認した。実CUDA保存再開25checksすべて成功、検証262,144 tokensは科学会計と分離。Web枝は3300更新/追加108,134,400 tokensまで進み、100,007,936地点のupdate308228/総10,100,015,104 checkpointを保存した（SHA0813da0970485ec58d480f04f19b8dc92750421ce7086bef86232529f0626365）。GPU89%/VRAM7690MiB、stderr空。二枝の科学学習はまだ未完了、320内容診断/条件付き全文/段階4も未実施。新しい最終確認`scripts/review_story20_completion.py`は構文確認のみで、完了証拠としてまだ実行していない。job/metrics/latest/checkpointとactual identityを追跡し、同じrunを重複起動しない。README/roadmap/handoffに現52の再開状態を反映、local commit4f7260c。

段階3の各500M比較を永続起動: 準備commit742ec45、2026-10-05 00:56:22.906739Z、hidden Windows33908 / actual Linux174280 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4498545。actual process存在を確認した。Linux run`reports/phase6/story20-low-lr-10b-500m-20261005`の`screen-job.json`/arm metrics/checkpoint、Windows同run`screen.stdout.log`/`screen.stderr.log`を追跡する。CUDA実保存再開→二枝各500M→中間/終端の一次評価→全320内容診断→原gate条件付き全文/長文→段階4判断・report・local commit・元UI復帰で停止。起動済み同じjobを確認し、重複起動しない。

段階3・各500M条件凍結済み、起動前: 固定train4filesの構築は59,963,449 tokens/662,857文書で完了、source exhausted/120M目標未達を記録。99,975,168物語inputには約1.66727周を使う。40全文サンプルと14弱例、非ランダムsample・synthetic・広域重複未確認の限界を`reports/phase6/story20_budget_pool_content_review.json`へ保存し、限定比較として使用する。26関連CPU tests、凍結config/schema/probe成功。各500,006,912科学tokensと共通schedule中間100Mの実比較を開始し、320内容診断・原gate条件付き全文→段階4判断/report/local commit・元UI復帰で停止する。[現計画52](52_story20_low_lr_execution.md)。旧完了jobは再起動しない。

段階2合格・段階3データ準備中: 物語20%低LR100Mは全文BPB0.952080670、元親0.954018473より改善し、同LR Web0.945960821比+0.647%。固定EOS23/反復22、一貫性12/適切完結12（各80）、全400 EOS127/反復45/raw失敗0。長文128/512各20でEOS9/9、文再出現8/8、4gram反復0.474/0.586。GPU全文1,940.030秒、CPU原条件30checks全成功。実科学143237/評価143904終了、元UI復帰を確認。条件付き各500Mへ進むため、データ準備を2026-10-05 00:46:47Zに永続起動した。hidden Windows21332 / actual Linux173735 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4440874。`~/jmicro-data/phase6/simple-stories-ja-budget-20261005/job.json`とWindows`reports/phase6/story20-low-lr-10b-500m-20261005/prepare.*.log`を追跡。途中約45Mまで構築、500M config未凍結・科学GPU未開始。26関連CPU tests成功、元親/共通pool/共通schedule100M中間・500M終端/反復実数の実装を準備済み。次は実source量/40sample確認・必要epoch明記→config凍結・永続GPU起動→320内容診断/条件付き全文→段階4判断/report/commit・元UI復帰で停止。以下は準備/起動履歴で、現行状態は本段落を正とする。

段階1/一次内容診断完了、段階2全文/長文を永続起動: 物語20%・peak0.0001は100,007,936 tokens追加、学習159.277秒・一次GPU262.543秒。固定80でEOS23/反復22/raw失敗0、一貫性2点12/80・適切完結12、同LR Web対照は0/59/0。元mixtureと一貫性差8/paired下限>0を全通過し、全文/長文へ進む。新科学143237は終了、UI復帰確認後、hidden Windows30472 / actual Linux143904 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticksはfull launch記録を正とする、2026-10-05 00:11:52Zに段階2開始。追加学習0、GPU上限3,000秒、同LR Webと候補の未測定全文/400/長文だけ測る。原親BPB+0.001/全raw条件が通るまで500Mへ進まない。同一jobを追跡し、終了後のCPU確認→条件分岐→判断/report/commit・元UI復帰が残る。

物語20%・低LR100Mを永続起動: 準備commitca5dac0、20関連testsと実親/参照確認済み。hidden Windows30420、actual Linux143237 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4192785、開始2026-10-05 00:05:25Z。run`reports/phase6/story20-low-lr-10b-100m-20261005`へjob/source/metrics/checkpoint/rawを保存する。実CUDA保存再開→新条件100M/一次評価→80内容診断→事前条件付き全文/各500M→段階4判断/report/commit・元UI復帰で停止。同じactual jobを追跡し、重複起動しない。

2026-10-05 JST・段階1〜4を再開: ユーザー「4まで進めて」。[実行計画52](52_story20_low_lr_execution.md)に物語20%・低LR100M→有望時のみ全文/長文→全条件合格時のみ各500M→判断/次案/report/local commit・元UI復帰で停止の条件を保存した。保存済み同LR Web対照と25M poolを再利用し、原gateは不変。専用runner/config/schema凍結、20関連CPU tests成功、CPU実親finite/hash/元state・凍結参照確認済み、科学GPUは未開始。実process確認では既存UI140800のみ、旧科学job終了。次は準備commit後の永続起動。以下は過去の完了/起動履歴であり、現在の状態は本段落を正とする。

2026-10-05 JST・計画49段階1〜3完了: 通常LR物語10%100M→事前失敗時分岐の低LR Web/物語10%各100M→[判断と次案51](51_story10_judgment_and_next_proposal.md)を完了した。[実行50](50_story10_and_budget_execution.md)。通常LR10%はEOS17/反復40/一貫性4、低LR Webは0/59/0、低LR10%は16/36/6（各固定80）。両候補は事前一貫性差8件未達で未採用、全文/長文・500M/pool拡張の開始条件を満たさず未実施。常識5択の低LR配合対照差+3.038pp・95%区間+0.894〜+5.004は診断上の改善で、基本意味の対照差は負、幅広い理解能力・Base/Chat品質達成とはしない。科学300,023,808/検証524,288別会計、GPU775.522秒、CPU14/16 tests、実CUDA保存再開各25項目成功、追加全240出力内容診断済み。[要求別確認](../reports/phase6/story10_execution_completion.json)。科学139467/140216は終了。UIは元final10BでHTTP応答/busy=false、復帰時Linux140800 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks1468219。次案は20%・peak0.0001一条件100Mを保存済み同LR Web対照と比較する提案で、今回は開始しない。report/local commitで停止。500M/1B/20B/50B/Chat/test/push未実施、独立人手/全12.23B監査/広域混入確認は未実施のまま。

以下は今回の準備・起動履歴。最新状態と停止境界は上記を正とする。

低LRの同量比較を永続起動: 準備commitd3b762a、16関連CPU tests、peak0.0001/10%/Web対照各100Mの専用config/schemaを凍結。hidden Windows28816、actual Linux140216 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks1416619、開始2026-10-04 16:22:41Z。run`reports/phase6/story10-low-lr-10b-100m-20261005`とWindows`screen.*.log`へ永続保存。現在Web対照学習中、二枝評価と160内容診断→事前条件付き全文→段階3判断/次案が残る。UIはfinally復帰。科学140216のactual processを確認して同じjobを追跡、重複起動しない。

計画49段階1を完了し、段階2の低LR分岐へ: 物語10%/100MはGPU264.370秒、EOS17・反復40・raw0（固定80）。全80をCodex採点し、一貫性2点4/80で事前の対照差8件を満たさず未採用。元mixture条件は全通過だが内容条件を緩めない。全文/長文は未実施、500Mへ進めず、同じ親・10%・同量でpeak0.0001のWeb/物語各100M比較を一つ凍結した。[記録50](50_story10_and_budget_execution.md)。16関連CPU tests成功。先のLinux139467は終了、UIは元final10Bで復帰を確認。次は低LR二枝の科学200,015,872（検証262,144別）→160内容診断→条件付き全文→段階3判断/提案/report/local commit・UI復帰で停止。1B/20B/Chat/test/pushは開始しない。

計画49段階1のGPU比較を永続起動: 準備commit70304d6、14関連CPU tests成功、専用config/schema凍結。hidden Windows34152、actual Linux139467 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks1364277、開始2026-10-04 16:13:58Z。実CUDA保存再開後、物語10%の100M学習を実行中。run`reports/phase6/story10-10b-100m-20261005`、`screen-job.json`とWindows`screen.*.log`へ保存。GPU中のみUI停止、finallyで元final10Bへ戻す。80内容診断・採用判定→条件付き各500Mまたは低LR比較→最終判断/提案が残るためgoalはactive。actual processを確認し、同じjobを重複起動しない。

2026-10-05 JST・計画49段階1〜3を実行再開: ユーザー「3までを進めて判断をして提案をしてください」。[実行記録50](50_story10_and_budget_execution.md)へ条件を保存し、物語10%/100Mの専用runner・launcher・testsを準備中。既存25M poolと保存済みWeb/20%対照を再利用し、原gateは不変。採用条件を通る場合は各500M比較、未達なら一つの低LR同量比較→判断/提案/report/local commit・UI復帰で停止する。1B/20B/50B/Chat/test/pushは開始しない。現在科学GPU未開始、actual GPU processは既存UI49746のみ。過去完了runを再起動しない。

2026-10-05 JST・次回計画のみ: 前回結果を踏まえた[配合・学習量計画49](49_next_mixture_and_training_budget_plan.md)を作成。最初は同じfinal10B親・同じLRで新物語10%を100M学習し、保存済みWeb/20%結果と比較する提案。既存25M poolで足り、新source取得は不要。原採用条件を通る場合のみ、pool約60MとWeb/物語10%各500Mの同量比較を別予算で計画する。学習不足仮説と10B対20B案を残す。BPB悪化上限は緩めず、未採用20%枝を自動延長しない。今回は計画保存/local commitで停止、GPU学習/評価・新data取得/構築は未開始、既存UIを維持する。前回段階1〜3の完了commitは6d0ab0c。

2026-10-05 JST・段階1〜3完了: 限定data/EOS確認、SimpleStories-JA候補25,000,067 tokens、同じfinal10BからWeb/既存短文20%/新物語20%を各100,007,936 tokens学習し、一次240内容診断と事前条件付き全文/長文評価まで完了した。[最終報告48](48_complete_text_10b_comparison.md)、[全文/長文結果](../reports/phase6/complete_text_10b_full_result.json)、[要求別完了記録](../reports/phase6/complete_text_10b_comparison_completion.json)。一次35・全文43証拠checks、38関連tests・修復15 tests・実CUDA全state保存再開成功。新物語は固定EOS0→24/80、反復60→24/80、Codex一貫性2点0→10/80へ改善したが、全文BPB0.955765は元親0.954018より+0.001746で既存+0.001上限を超え、正式採用は見送る。理解改善の確証・独立人手品質合格・Base/Chat品質目標達成とはしない。GPU合計2,731.428秒、追加科学300,023,808 / 検証262,144 tokensは別会計。科学Linux17951、旧失敗19791、修復37818はいずれも終了。UIは元final10Bへ復帰しHTTP応答/busy=false、Linux49746 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks1043870を実確認。最終report/local commitで停止する。次の具体的行動は新しい依頼が来るまで追加学習を開始しないこと。500M/1B/20B/50B/Chat/test/pushは未開始。

以下は当時の進捗履歴。現行状態と停止境界は上記を正とする。

2026-10-05 JST: conditional読み込みを修復しr1を再開。初回Linux19791はWeb全文/400保存後の`read_json(str)`型エラーで終了、UI復帰を確認。旧job/source/config/rawを保持し、15CPU tests（Path回帰含む）成功。Web全文/400をhash・同条件・raw IDから確認して明示的に再利用、既消費GPU831.355秒を元3,000秒予算に含め、学習/評価仕様/gateを変更しない。新run`reports/phase6/complete-text-10b-100m-20261004/conditional-full-r1`、hidden Windows33788、Linux37818 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks930807のactual processを確認。現在Web長文中、Windows`full-r1.*.log`、終端job/resultが揃ってから`scripts/review_complete_text_full.py`を実行する。三条件学習/240内容診断は完了、goalは最終評価/report/commit/UI復帰が残るためactive。重複起動しない。

条件付き評価のWeb対照全文本文を完了: dev89,416文書 / 164,344,743 bytes、BPB0.948957324851、本文評価389.088秒。現在は同じ対照の固定400生成中、Linux19791は実在。新物語の全文/長文結果と最終CPU確認・報告・UI復帰が残るのでgoalは未完了。全240一次採点と各枝100Mは完了済みで再学習しない。保存result/長文を原IDから確認する`scripts/review_complete_text_full.py`を準備した。中断は同一conditional jobの保存済みstageを再利用し、completed primary job17951を再起動しない。

条件付き全文/長文評価を2026-10-04 14:43:42Zに永続起動した。hidden Windows34244、Linux19791 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks822481、actual process実在。Linux `reports/phase6/complete-text-10b-100m-20261004/conditional-full/job.json`、Windows`full.stdout.log`/`full.stderr.log`。現在Web全文本文を評価中、追加学習0、上限3,000秒。準備と一次比較結果はlocal commit7e3b6cdへ保存。終端を確認するまで重複起動しない。UIはこの評価中のみ停止しlauncher finallyで元final10Bへ復帰する。stage3は条件付き評価と完了報告/commitが残るため未完了。

一次比較完了・条件付き評価へ: 三条件GPU774.624秒で完了し、全240をCodex内容採点、35証拠checks成功。Web/既存短文/新物語のEOS0/3/24、反復60/55/24、raw失敗0、Codex一貫性2点0/1/10（各80）。新物語は適切完結9/80、関連性2点23/80で対照26/80より減少し、元品質目標未達。一次の事前gateを全て通ったため、新物語とWebのみ原全文dev/400と20prefix128/512へ進む。専用conditional runner/config/schemaと14CPU testsを準備した。追加学習0、予算3,000秒。GPU科学process17951は終了、UIは元final10BでHTTP応答確認済み。次は条件付き評価の実行→結果確認→report/local commit・UI復帰で停止する。

三条件の科学学習は各100,007,936 tokensを完了し、各枝総10,100,015,104 tokens/update308228の終端checkpointを保存した。学習時間はWeb159.169秒、既存短文148.389秒、新物語148.383秒。Linux17951は実在し、最後の新物語条件の一次評価中。WebのEOS0/反復60/文字破損0、既存短文のEOS3/反復55/文字破損0（各固定80、全文評価ではない）。新物語結果は未確定。終了後に240出力内容診断とCPU証拠確認、UI復帰・report/local commitで停止する。

段階3のGPU比較を2026-10-04 14:23:05Zに起動した。hidden Windows28068、Linux17951 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks698774。actual processを確認済み、現在は実CUDA保存再開gate中。runは`reports/phase6/complete-text-10b-100m-20261004`、Windowsログ`gpu.stdout.log`/`gpu.stderr.log`、Linux`job.json`と各枝checkpoint/metricsへ永続化。準備commit05b450d、UIを一時停止しlauncher finallyで復帰する。重複起動せず、このprocessを追跡する。比較後に内容240件を診断・証拠を確認し、report/local commitで停止する。

段階2完了・三条件GPU比較の起動準備: 新公開物語pool25,000,067 tokens / 276,369全文 / 108,582親familyを82.876秒で構築し、100例をCodex確認。合成語・弱い展開・未解決末尾などの残る例を[標本記録](../reports/phase6/complete_text_data_review.json)へ明記した。全例意味保証や独立人手認定ではなく、元gateを保持した実験用候補として採用。両Web候補は未採用のまま保存。38関連CPU tests成功、同じfinal10Bから各100,007,936 tokensのconfig/schemaを凍結。GPU科学学習はまだ未開始、既存UI482のみ実在。次はUIを一時停止し、実CUDA保存再開→三条件の学習/一次評価→内容240件採点→報告/local commitで停止する。

段階2の内容確認により学習前に方針を修正: Web r2も30,235,206 tokensまで232.351秒で準備したが、無作為100例に意味の崩れ・前文依存が残り未採用。初回とr2は保存。公開SimpleStories-JAの作者MIT表記・revision `d25370316dd77ec0ee4fd9db57bfe57075cf4b90`・train parquet hash/サイズを固定し、必要な25M tokensの物語全文を準備中（hidden Windows33712、`prepare-stories.*.log`）。Cは2〜8文/32〜128tokensとなり、旧短文との長さ一致は学習前に撤回してsource/長さ/EOS密度を含む配合全体の比較と明示した。[改訂条件48](48_complete_text_10b_comparison.md)。原モデル/学習量/LR/gateは不変、関連38 CPU tests成功。現在もGPU科学学習は未開始、UI維持。

段階1を完了し、[実行記録48](48_complete_text_10b_comparison.md)へ保存。Web/既存短文各100の限定抽出、EOS/BOS/shift四条件成功、本文special混入0、句読点末尾63/100と100/100。句読点だけでは前文依存・意味の崩れを除けない。初回候補30,230,920 tokensを215.570秒で構築したが、無作為100例の前文依存・説明予告を確認して学習前に選別を修正。旧候補は保持し、r2をWSL12CPU workersで構築中（Linux17005、hidden Windows33952、ログ`reports/phase6/complete-text-10b-100m-20261004/prepare-r2.*.log`）。新しい選別・分岐と既存EOS/尤度/契約/評価メモリの関連36 CPU tests成功。科学GPU学習はまだ未開始、UI継続。次は修正poolの100例確認→凍結→UI停止→新poolの実CUDA保存再開と三条件各100M。

実行再開（ユーザー「3まで進めてください」）: 計画の段階1〜3、限定data/EOS確認→25M〜50M完結文pool→同じfinal10BからWeb/既存短文20%/新完結文20%各100Mの実学習と比較を開始する。以前の計画のみの停止境界はこの範囲で更新。まず実装・既存train/poolと実processを確認中。現在UIのLinuxPID482は実在し、GPU学習processなし、Linux空き526GiB。GPU開始時のみUI停止・完了時復帰。段階4の500M〜1B、20B/50B、Chat、公開は開始せず、三条件の評価・報告・local commitで停止する。

計画補足（2026-10-04、質問「学習量が足りない可能性」）: **学習量不足は未棄却で、収束を証明していない。** [計画47](47_post_evaluation_training_plan.md)へ、各100Mは配合screenであり総10Bに対して約1%に留まること、安全なA/Cを同量500M〜1Bまで比較する別段階案と、Web10B対20Bの直接比較案を追記した。100Mで内容が改善しないことを増量無効の証明にしない。旧品質gateは保持し、延長は別予算・終了点を先に凍結する提案。今回もGPU/data作業は未開始、UIを維持し、計画補足のlocal commitで停止する。

最新依頼（2026-10-04）は追加評価に基づく次回計画と「データセット量を増やすべきか」の判断。[データ・学習改善計画](47_post_evaluation_training_plan.md)を保存した。推奨は意味の通る完結文poolをまず25M〜50M tokens準備し、同じfinal10B親からWeb100%/既存短文20%/新完結文20%を各100Mで比較する案。EOSだけでなく生成一貫性・適切な完結・反復・条件保持を測り、有望ならpool100M以上と追加500Mへ段階拡張する。新規source量と既存dataの再選別・学習tokensを分ける。元gateは保持し、数値・予算は次回凍結する提案。**今回は計画のみで、新data取得/構築・GPU推論/学習・suite変更は未開始。UIは維持し、local commitで停止する。**

最新の評価追加依頼（2026-10-04、棚卸し後の実装再開）を完了した。[実施計画](45_japanese_base_evaluation_v2.md)、[結果と制限](46_japanese_base_evaluation_v2_results.md)、[15 evidence checksの集計](../reports/phase6/japanese_base_v2_review.json)、[終了・UI復帰記録](../reports/phase6/japanese_base_v2_completion.json)。新しいnative scorer/実行入口・8 CPU testsを追加し、既存契約/評価メモリと合わせた21 tests成功。WSL/RTX4090で現在の10M/総10Bモデルを実測した。JBLiMP sample SLOR74.62%、JCommonsenseQA30.38%、独自意味dev59.38%。意味の両文脈正答23/96＝23.96%でrandom期待25%を超える証拠はない。JNLI/JCoLAはlabel prior・多数派対照を含めると判別力が弱く、Base品質合格にはしない。

保存済み80×2の全160をCodexで文法/関連性/一貫性各0/1/2採点。10Bは文法2点38/80、関連性2点25/80、一貫性2点0/80。独立人手blindは未実施で、元70%人手目標へ代入しない。追加greedy128/512は各20件で自然EOS0、char4-gram反復83.26%/95.76%。元の自然EOS9件の適切な内容完結はCodex診断1/9。JSQuAD事前固定dev100は独自EM0%、文字F1 12.69%、外部Wikipedia100本文51,362 bytesのBPB1.335143。詳細は結果文書を正とする。

GPU初回pilot7.505秒、本評価320.820秒、語彙family重複を直した意味診断192件のみのrevision1.686秒で完了。元のraw/source/configを保持し、cluster CIの問題重みとJNLI image groupingは保存値からCPU修正した。追加学習0、公式test未取得/未採点、旧v1/学習コード/重み不変。rawとsourceはLinux `reports/phase6/japanese-base-v2-20261004/{pilot,full,cpu}`、修正版意味診断は`reports/phase6/japanese-base-v2-20261004-r1/pilot`。評価jobは終了し、Web UIを http://127.0.0.1:7860 へ復帰した（LinuxPID482 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks275771、ready13:12Z）。終了記録を確認し、完了GPU runを再起動しない。**今回はlocal commitで停止する。追加学習・test・参照重み・JMMLUは開始しない。**

以下は直前の棚卸し・実行履歴。現行の評価追加状況は上記を正とする。

最新依頼（2026-10-04）は日本語Base評価の追加に向けた「まず現行評価と改善部分を洗い出す」。**コード・固定suite・保存結果の棚卸しと公開日本語評価の調査を完了し、[評価改善案](44_japanese_base_evaluation_audit.md)へまとめた。** [CPU inventory](../reports/phase6/base_eval_inventory_20261004.json): dev80のchecksは全件共通の説明文、保存400のhuman_scoresは全null、400出力は80入力×5条件。BPB/EOS/raw flagsは測定済みでも、文法・関連性・一貫性の定量採点と公開日本語benchmark成績は未実施。

P0は既存結果から内容採点/category/反復/CIを追加し、否定・数量・時刻等の基本意味診断を設計する。P1はJBLiMP（原論文SLORと独自尤度診断を区別）・JCommonsenseQA・JNLI・domain別本文予測。次はv2の取得version/template/score/split/予算と新規基準を凍結し、Base向け候補尤度scorerを実装する案。今回は実装・GPU新評価・追加学習・参照重み取得・test採点を開始していない。旧protocol/gate/checkpoints/結果は不変。Web UIは維持する。

直前の追加依頼（2026-10-04）は「現モデルを試すローカルWeb UIの作成・起動」。**実装・実モデルAPI・Edgeブラウザの生成/停止確認を完了し、WSL/RTX4090の推論サーバーを http://127.0.0.1:7860 で稼働したまま引き渡す。** 起動/停止は `scripts/start_webui.ps1` / `scripts/stop_webui.ps1`。[操作説明](43_local_webui.md)、[確認記録](../reports/phase6/local_webui_review.json)。追加学習0、既存checkpoint/評価結果は保持。後続のEOS/Chat/20B実験の停止境界は維持する。

Web UI稼働中は `~/jmicro-data/gpu.lock` を保持する。次のGPU jobを開始する前はUIを停止し、WSL `reports/local/webui/server.json` のactual PID/boot/start ticksを確認する。Windows側launcher/process/logは `reports/local/webui/`。GPU推論はBF16/math attention＋KV cache。関連11 CPU tests、実モデルseed再現、旧greedy64 ID一致、切断後のlock解放/再生成、ブラウザdesktop/mobile生成と停止を確認済み。

最終更新: 2026-10-04。**ユーザーが再開したstep3「10bの品質評価」を完了した。** 同条件の全文dev89,416文書・固定400生成、旧5B/最良Web5.1B比較、全固定80と自然停止9件の内容確認、CPU証拠確認23項目を完了。BPB0.954018 / 固定EOS0・反復53 / raw Unicode0。元増量gateは合格、Base/Chat品質目標は未達。report/local commitで停止する。[品質結果](42_base_10b_quality_evaluation.md)、[本学習の結果と速度](41_base_10b_training.md)。

専用 `scripts/compare_base_10b.py` / `.sh` と凍結 `configs/phase6/base_10b_comparison.json` を用意し、関連23 CPU tests成功。初回は過去EOS設定5件のschema欠落で既存契約tests2件が失敗したため、元configを変更せず厳密const schemaを追加して修復した。[修復記録](../reports/phase6/base_10b_comparison_schema_repair.json)。GPU空きと既存job終了を確認済み。評価GPU上限1,800秒。旧結果・学習source/checkpointsを保持し、追加学習や後続実験は開始しない。

評価jobは2026-10-04 11:56Z開始、12:09Zにcomplete。LinuxPID442 / boot0f175ee3-e772-41f7-8f7a-76387be1f2e4 / start_ticks14858、hidden WindowsPID31900は実process終了を確認済み。[起動記録](../reports/phase6/base_10b_comparison_launch.json)、[完了記録](../reports/phase6/base_10b_comparison_completion.json)。GPU時間786.881秒（全文376.052秒・生成409.008秒）、上限1,800秒以内。Linux `reports/phase6/base-10b-comparison-20261004/` にjob/log/文書別NLL/400生成/result/比較packet/sourceを保持する。完了済みの評価・旧学習launcherを再起動しない。

完了CPU reviewer `scripts/review_base_10b_comparison.py` を実際の保存結果と内容診断へ適用し、23項目成功。生成IDから全raw flags、全文BPB、元安全gate、旧reference hash、評価隔離、実process終了を確認した。[review](../reports/phase6/base_10b_comparison_review.json)、[全80と自然停止の内容診断](../reports/phase6/base_10b_content_review.json)。追加学習tokens0、旧結果はGPU再評価せず再利用。独立人手blind/test/Chat/量子化は未実施。

[現在の計画](39_learning_scale_and_generation_plan.md)、[10B準備結果](40_base_10b_preparation.md)、[原ロードマップと品質条件](15_project_roadmap.md)、[引き継ぎ](windows_handoff.md)。過去の実行中メモ・停止境界・7.5B案は[2026-10-04までの履歴](autonomous_history_20261004.md)へ移した。旧メモのPIDやコマンドを現在の起動指示にしない。

## 実際に完了したこと

| 対象 | 実状態と証拠 |
|---|---|
| モデル | T4K / NoQK-Norm / 10,001,152 parameters。規模は10Mのまま |
| データ | train12,225,819,077 tokens整備済み。[受け入れ記録](../reports/phase6/corpus_10b_ready_review.json)。構築時確認・raw再構築・実loader成功、独立全件auditはユーザー指定で未完了 |
| 主系列学習 | 総5,000,003,584 input tokens。[学習確認](../reports/phase6/base_5b_review.json)、[全文と生成比較](36_base_5b_comparison.md) |
| 仕上げ比較 | 同じ5B親からWeb/短文20%を各100,007,936 tokens、各累積5,100,011,520。別モデルの消費を合算しない。[結果](38_eos_5b_finish_results.md) |
| UTF8表示 | 共通helper実装済み。上限の未完成末尾だけを表示から保留し、raw失敗と停止理由は保持 |
| 10B準備 | 専用config/schema/launcher凍結。14tests、実CUDA16updates/524,288検証tokensの全state/history一致、保存証拠26項目成功。[準備確認](../reports/phase6/base_10b_preparation_review.json) |
| 10B本学習 | stable9,500,000,256＋decay500,006,912＝総10,000,007,168 tokens。追加科学5,249,990,656 tokens。[保存状態19checks成功](../reports/phase6/base_10b_training_review.json) |
| 10B品質評価 | 同条件dev/400・全固定80と自然停止9件の内容確認、CPU証拠確認23項目成功。[品質結果](42_base_10b_quality_evaluation.md) |
| 品質と後続 | Base/Chat品質未達。独立人手blind採点・test・Chat学習・新重みの量子化品質は未実施 |

## 現在の評価結果

同じ保護dev89,416文書/164,344,743本文bytesのBPB、固定dev80のgreedy64-token上限。BPBは小さいほど良い。

| モデル | 全文BPB | 固定自然EOS | 固定反復 | 全400 raw Unicode失敗 |
|---|---:|---:|---:|---:|
| 元2B | 0.982882 | 0/80 | 60/80 | 0/400 |
| 元5B | 0.964484 | 0/80 | 59/80 | 2/400 |
| Web仕上げ5.1B | 0.958092 | 0/80 | 57/80 | 0/400 |
| 短文仕上げ5.1B | 0.959011 | 13/80 | 51/80 | 2/400 |
| 新10B | 0.954018 | 0/80 | 53/80 | 0/400 |

短文の全400自然EOS129/反復103、Web13/121。短文の全文BPB悪化は対照比+0.095894%で許容内だが、raw Unicode2により最終採用gate不合格。1件は途中不正UTF8、1件はcap末尾切断。短文重みは診断用として保持する。Webの増量数値gateは合格、両モデルとも意味・数量・時刻・否定条件の誤りが残る。自然停止増加を正答率・実用品質の達成にしない。2B→5BにはLR曲線差もあり、全差を学習量だけの因果効果とは断定しない。

## 保存先と実行状態

コード/Git正本はWindows `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`、Linux実行コピーは `/home/aihub_ubuntu/src/japanese-tiny-llm-10m`。大容量データは `/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards`。固定Tokenizerは `artifacts/phase2/4096/tokenizer.model`。Pythonはuv管理3.12.7、WSL2/RTX4090/Torch2.14.1+cu130。

主要checkpointはLinux repo相対で次に保存されている。hashの正本は凍結configと各review。

- 長期継続用stable4.75B: `reports/phase6/base-5b-20261004/stable/checkpoint-00144959.pt`、SHA `916c4105ba7ab62597334a059cd34839d675fde29bb82b6fca6d30f889df6be5`。
- final5B: `reports/phase6/base-5b-20261004/decay/checkpoint-00152588.pt`。
- Web/短文5.1B: `reports/phase6/eos-5b-finish-100m-20261004/{web,short20}/checkpoint-00155640.pt`。
- 10B準備: `reports/phase6/base-10b-20261004/` のpreparation-job/preparation/cuda-resume-gate/environment/source/logとverification checkpoints。

10B準備jobはcomplete、検証GPU時間19.217秒。旧Linux459/Windows29620は終了履歴。科学jobは2026-10-04 09:36Z起動、11:43:52Zにcomplete。Windows30148、Linux427（boot86a59ddc-4594-4dfb-81df-a4f1439c52b0/start_ticks3212）は実process終了を確認済み。[launcher記録](../reports/phase6/base_10b_launch.json)は起動時の履歴、[完了記録](../reports/phase6/base_10b_training_completion.json)が現在の終端状態。runのjob/result/metrics/log/sourceと科学checkpoint163個を保持した。pushはしない。

新10Bの継続用stableは `reports/phase6/base-10b-20261004/stable/checkpoint-00289917.pt`、評価用finalは `reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt`。[実hashと容量](41_base_10b_training.md)を参照。両終端のmodel/Adam/scheduler/RNG/sampler/digest/counterと全科学metricsをCPUで確認した。

高速化はFlash＋compile reduce-overhead・BF16・fused AdamW・batch32で対応済み。今回の定常速度はstable695,339 / decay694,288 tokens/s。準備を含むGPU lock時間7,657.678秒（約2時間8分）で上限9,000秒以内。以前の最速reference比5.436倍、最大VRAMのbatch111はbatch32より遅く、data waitは既存測定0.55%。追加速度実験は未実施。

## 次に行うことと終了点

直前チャットの番号に揃える。前回step2の学習・保存確認は完了し、commit1344b4eで停止した。今回ユーザーはstep3の品質評価を再開した。評価・内容確認・報告とcommitで停止する。

1. **実行設定準備: 完了。** 専用設定と保存再開確認を再実行する必要はない。
2. **本学習と保存確認: 完了。** 保存stable4.75Bから9.5B stable＋15,259-update decayで総10,000,007,168/update305176へ到達。追加科学5,249,990,656 tokens、7.5B中間実験・追加収集なし。専用CPU reviewer19項目成功。
3. **同じ評価と内容比較: 完了。** 新10Bだけ全文dev/400を測り、旧5B/最良Web5.1Bを再利用した。全文BPBはWeb比−0.425169%、固定反復57→53、raw Unicode0。固定EOS0のまま、数量・時刻・否定・因果誤りと局所退行が残る。元増量gateは合格し、次の仕上げ候補として保持する。実用品質達成とはしない。
4. **報告・local commit・停止。** 原raw品質条件を保持し、改善と残る課題を明示する。EOS仕上げ/UTF8制約は別の後続候補で、現在未起動。

以下は中断復旧用のWSL repo内コマンド履歴。今回のrunは完了しているため再起動しない:

```bash
bash scripts/run_base_10b.sh --train
```

将来別のrunを起動する前はactual PID/boot/start ticksとGPU lockを確認する。科学学習GPU上限9,000秒、評価上限1,800秒はともに予算内で完了。次の具体的な候補は、ユーザーがEOS仕上げを再開した場合に保存final10B親の単一Web/短文20%各100M比較を整えること。元raw採用gateを保持し、20B/50B/Chat/UL/sweepへ自動移行しない。

## 前回の文書整理の検証（起動前の履歴）

[文書更新記録](../reports/phase6/documentation_refresh_20261004.json)に元13文書の完全保存、270内部リンク、凍結10B設定・学習source/lockの不変性、Windows/WSLの現行文書一致、科学run未開始を記録した。過去のreport6件はWindows正本に存在し、Linuxコピーに不足することも記録する。移行時はGit管理reportと大型raw evidenceの両方を引き継ぐ。文書整理当時はGPU学習・評価を実行せず、local commitで停止した。その後ユーザーがstep2を再開した。
````

## docs/15_project_roadmap.md

更新前file SHA256: `54e65784eb3c62165b6312021d68d6ed74cf612f7f0ec8fdd45bd4ee75435e0c`

````markdown
# JMicro-10M フェーズ別実行計画

計画56段階1〜3完了・停止（2026-10-05 JST）: matched教材各22,977,241tokens/253,119全文の各500M比較を完了。対照→追加選別はEOS39→44/反復16→17/一貫性11→11/適切完結14→15（各80）で不採用。段階2も省略せず旧59,963,449-token物語固定/一定LR0.0001で連続1Bを完了し、500M→1BはBPB0.982953243→0.981611241/EOS31→35/反復21→10/一貫性11→19/適切完結15→20。意味60.417→66.146%（対応95%+1.563〜+10.417pp）と複数指標は改善したが、一貫性95%下限0、EOS35<37、内容各27未達、Web BPB比+1.0335%で原採用条件未達。両条件付き全文は未開始。CPU10tests/実CUDA25・13/一次32・29/最終要求別31checks成功、全320内容保存。科学2,000,027,648/検証524,288別、一次GPU3331.359秒。元final10B UI actual237483/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6728695/ready07:08:04.599378Z、HTTP親SHA410f975d…/tokens10,000,007,168/busy=falseとactual process確認。科学234687/236557/教材234279は終了し再起動しない。結果と提案はdocs/57_matched_story_and_learning_budget_results.md、最終確認reports/phase6/matched_story_completion.json。11B checkpoint・両run全raw/metrics/source/annotationsをLinuxへ保存。追加学習の効果を否定せずBase/Chat未達、次の小規模条件保持教材診断/LR減衰/新data/GPU/20B/50B/Chat/protected test/pushは提案のみで未開始。local commitで今回停止し、以下は実行当時の履歴。


計画56段階1完了／段階2凍結: matched各22,977,241-token教材で各500,006,912追加tokens、実EOS教師Web846,893/story1,101,267を一致。GPU1659.584秒・科学1,000,013,824/検証262,144別。dev/日本語全完了・全160個別内容・CPU32evidencechecks成功。対照→候補BPB0.979944438→0.980233205、EOS39→44/反復16→17/一貫性11→11/適切完結14→15（各80）、対応95%−8.75〜+8.75ppで改善条件未達・不採用。条件付き全文は開始しない。次は旧採用59,963,449-token物語pool固定、元10Bから一定LR0.0001で追加連続1,000,013,824tokens、500M中間/1B終端を保存して両地点評価。段階1科学234687終了、元UI235943へ復帰確認済み。段階2config/schema/sourceを凍結したが新科学はまだ未開始。


計画56段階1〜3実行中（2026-10-05 JST）: 二組各22,977,241tokens/253,119全文、body平均88.7764（旧88.4621）、同じ長さ並び/BOS/EOS位置。CPU抽出11.146秒、random40各に弱例14/12を個別明記してbounded比較を受入。CPU10tests成功・凍結commit a8215aa。2026-10-05 06:09頃、hidden Windows34620/actual Linux234687/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6377461で教材二条件各500Mを開始。実CUDA25checks通過、対照学習中。Linux reports/phase6/matched-story-content-500m-20261005/screen-job.json と Windows同run screen.stdout.log/stderr.logを追跡。UIはGPU中停止/finally復帰。段階1未達でも段階2の固定教材・一定LR連続1B（500M中間/1B終端）は必要。全320内容と日本語評価・事前条件付き全文、判断/report/local commit/元UI復帰で停止。科学・一次結果は未確定、20B/Chat/test/pushは開始しない。


作成日: 2026-10-02。最終更新: 2026-10-05（10Bと各100M/500M比較・日本語評価の実状態へ更新）。根拠は[プロジェクト目的](01_project_goal.md)、[設計](03_architecture.md)、[技術調査](11_technical_research_gaps.md)、[Phase 0完了記録](16_phase0_completion.md)、[Phase 1完了記録](17_phase1_completion.md)。既存の**確定**方針から逆算した計画であり、将来の成果物名・未凍結の実行値は**提案**である。品質目標・評価契約はPhase 5で凍結済みで、結果を見て緩めない。

## 最終的に実現すること

約10Mパラメータの日本語専用モデルをランダム初期化から学習し、日本語短文生成と2〜数ターンの雑談をローカルで実行する。コーパス選別、独自Tokenizer、Base事前学習、Dialogue mid-training、Assistant-only SFT、量子化までを再現可能なpipelineとして残す。

最終成果物は次の三つに分ける。

1. `JMicro-10M-Base`: 日本語短文生成の基準モデルと評価結果。
2. `JMicro-10M-Chat`: 関連した短い返答、話題継続、文脈維持、停止を評価した会話モデル。
3. 再現・利用一式: 学習コード、config、Tokenizer、データmanifest、再開可能checkpoint、量子化artifact、ローカル実行手順、実験台帳。

目標規模は9.5M〜10.1M parameters、初期contextは1024 tokens。5〜10MB級は量子化配布の目標であり、Tokenizer等を含む実容量、推論メモリ、品質を測って達成を判断する。高度な推論・コード生成・長文RAGは今回の成功条件へ加えない。

## 現在地と計画の使い方

最新完了（2026-10-05 JST）: [計画58](58_dataset_expansion_proposal.md)段階1〜3を[結果60](60_dataset_expansion_results.md)へ保存。短い物語pool約60M→200M、旧/新各追加1B、同条件日本語・全160内容、原gate判断と一次35/最終20項目確認を完了。常識35.031→38.561%は改善したが、EOS34→25/一貫性15→9で不採用、条件付き全文は未開始。量・新source・長さ・EOS密度の複合比較で、データ量の一般的な効果や容量限界を確定しない。科学2,000,027,648/検証262,144別、元UI復帰・local commitで停止。Base/Chat未達。次の教材診断は未実行の提案で、新GPU/20B/Chat/test/pushは開始しない。以下の旧現在地は履歴、現在の実状態はstatusを正とする。

最新完了（2026-10-05 JST）: 新計画54の段階1〜4を[結果55](55_complete_document_500m_results.md)へ保存した。110M全文pool/一条件500M/日本語診断・80内容/一次22・最終51項目確認を完了。新構成は保存物語候補より停止・反復・一貫性が悪化し不採用、原事前分岐により条件付き全文は未実施。実物語比率とEOS密度も変わったためデータ量だけの否定ではない。元UI復帰・local commitで停止し、report55の新案は未実行。Base/Chat未達。以下の計画52等は履歴。

最新完了（2026-10-05 JST）: ユーザー「4まで進めて」に従い[計画52](52_story20_low_lr_execution.md)段階1〜4の学習・評価・判断を完了した。100M/全文通過後の各500M、四地点一次評価、全320内容診断、条件付き全文/400/長文を実施し、CPU37/全文30項目が成功。物語500Mは全文BPB0.948798/固定EOS37/反復18/一貫性・適切完結19（各80）で元比較条件を全通過し、研究候補として採用。物語source59,963,449 tokensを約1.667周使用し、新規unique100Mとは扱わない。基本意味・常識の改善とBase/Chat品質目標は未達。[判断/次案53](53_story20_low_lr_judgment.md)・report/local commit・元final10B UI復帰で停止する。科学174280/評価177987は終了、再起動しない。次の同量500Mデータ構成比較は提案のみ。保護test・各枝1B/20B/Chat・pushは今回対象外。以下の旧記録は履歴で、現在は[status](autonomous_status.md)を正とする。

最新追加比較（2026-10-05 JST）: [計画49の実行50](50_story10_and_budget_execution.md)を未達時分岐まで完了し、[判断/次案51](51_story10_judgment_and_next_proposal.md)へ保存。物語10%/低LR各100MでEOS/反復は改善したが、一貫性差4/6は事前8件に届かず、条件付き全文と500Mは未実施。科学三枝300,023,808/検証524,288を分け、元final10B UIへ復帰しreport/local commitで停止。Phase 6 Base/Chat品質未達、20%低LRや20Bは次の提案のみ。

最新（2026-10-05 JST）: ユーザー指定の改善計画段階1〜3を[完結文比較48](48_complete_text_10b_comparison.md)で完了した。25M物語pool、同じfinal10B親から各100M三条件と事前条件付き全文/長文評価を実施。新物語はEOS/反復を改善したが親BPB悪化上限を超え未採用。Phase 6のBase品質目標は引き続き未達で、Phase 7へ自動移行しない。report/local commit・UI復帰で停止し、500M/1B/20B/50B/Chatは開始しない。以下は以前のmilestone記録として保持する。

2026-10-04の追加依頼で[日本語Base評価v2.1の実装・実測](46_japanese_base_evaluation_v2_results.md)も完了した。基本意味・公開benchmarks・生成内容と長文反復を追加したが、元のBase/Chat品質条件は不変で未達。独立人手blind・test・公開Base参照・JMMLUは未実施。今回は評価/report/local commitで停止し、追加学習は再開しない。

Phase 0〜5とPhase 6①〜⑤、主要Web総5,000,003,584 tokens、同じ5B親からWeb/短文20%を各100,007,936 tokens追加した比較を完了。モデルは10,001,152 parameters、準備済みtrain12,225,819,077 tokens。独立全12.23B監査は未完了で、その事実を保持する。[実状態](autonomous_status.md)、[5B結果](35_base_5b_execution.md)、[仕上げ結果](38_eos_5b_finish_results.md)を参照する。

直接10Bの専用config/schema/launcher、14関連tests、実CUDA全state保存再開と26 review checksは[準備完了](40_base_10b_preparation.md)。科学学習step2とCPU保存確認19項目は完了、専用品質評価step3も完了。[学習結果](41_base_10b_training.md)、[品質結果](42_base_10b_quality_evaluation.md)。ユーザーがstep3の品質評価を再開し、今回その評価・内容確認まで完了した。報告・commitで停止し、後続実験は始めない。7.5B専用枝、再収集、20B/50Bへ自動移行しない。

本文BPBは5B0.964484、Web5.1B0.958092、短文5.1B0.959011。短文は固定EOS13/80と反復51/80へ改善したがraw Unicode2/400で最終採用不合格。Base/Chat品質、独立人手blind/test、新重みの量子化品質は未達・未実施。結果を見て元の品質条件を緩めない。

Pythonはuv管理3.12.7、依存変更はuv add。WSLでは `uv run --frozen --extra hub --extra data --extra ml --extra export ...`、不足する環境だけuv syncで復元する。データはLinux diskを使う。別PCでは[引き継ぎ](windows_handoff.md)からWindows最新local commitとLinux data/checkpoint/sourceを移す。Git/Hubだけで学習済みweightsと12.23B shardsが復元できるとは扱わない。

以下の各Phaseは元の目的と完了条件を保持する。過去の段階案と当時の指示は[保存履歴](autonomous_history_20261004.md)へ分離し、現行実行値は[専用10B設定](../configs/phase6/base_10b.json)を正とする。追加科学学習5,249,990,656 tokensは約126分、評価込み145〜165分の見積もり。上限は科学9,000秒（準備19.217秒含む）＋評価1,800秒。実装・内容確認時間は別。

## 全体の順序

| Phase | 状態 | 実行環境 | 目的 | フェーズ終了時のゴール | 前提 |
|---:|---|---|---|---|---|
| 0 | 完了 | iMac | 成功条件と実験の契約を固める | 設定・記録・評価仕様を作成し検証済み | [完了記録](16_phase0_completion.md) |
| 1 | 完了 | iMac | 目的に合うデータを追跡可能にする | 小規模Base corpusと会話pilot、独立した評価splitを用意する | [完了記録](17_phase1_completion.md) |
| 2 | 完了・[証拠](18_phase2_completion.md) | iMac | 日本語を小語彙で安定して表現する | 同じsampleで学習した4k/8k Tokenizerが契約を満たす | 1のsample・split |
| 3 | 完了・[証拠](19_phase3_completion.md) | iMac / CPU | 10Mモデルと推論経路を成立させる | 正しいモデル・cache・HF/float GGUF経路を確認する | 2 |
| 4 | 完了・[実機証拠](21_phase4_completion.md) | Windows/WSL＋RTX 4090 | 長時間学習の再現性と実行可能性を確かめる | 保存再開・実shard学習・4090速度と予算を検証した | 1〜3 |
| 5 | 完了 | Windows/WSL・RTX 4090 | 小予算で有望な候補を選ぶ | overfit、10M smoke、100M比較から最大2候補を選ぶ | 4 |
| 6 | 5B/10B・各100M/500M比較と日本語追加評価完了、品質目標未達 | Windows/WSL・RTX 4090 | 日本語Baseの能力を段階的に伸ばす | 学習量・配合・生成/意味診断を比較し、Base品質を別判定する | 5、[準備証拠](30_phase6_readiness_execution.md)、[最新判断53](53_story20_low_lr_judgment.md) |
| 7 | 未着手 | Windows/WSL・RTX 4090 | Baseを短文雑談モデルへ仕上げる | mid-trainingとSFTの効果を分離し、Chat v1を評価する | 6、1の会話pilot |
| 8 | 未着手 | 学習PC・独立したローカル検証環境 | ローカルで使える成果物を完成させる | Base/Chatと量子化版を独立環境で実行・再現できる | 7、3のexport経路 |
| 9 | 未着手・50Bは条件付き | Windows/WSL・RTX 4090 | 追加学習に継続価値があるか検証する | 20B、条件付き50Bの効果と限界を報告する | 6、追加予算の見積もり |
| 10 | 未着手・後半研究 | ローカル中心、後半にVast.ai並列比較 | baselineを越える追加研究を行う | 共有・蒸留・hybrid・規模比較の採否を証拠で決める | 8、固定したbaseline |

Phase 0〜8を最初の完結した開発系列とする。Phase 9は20Bの評価と、改善継続時のみ50Bへ進む系列。Phase 10は後半研究であり、最初のChat完成を待たせない。

Phase 1の会話pilotは準備済みで、拡張と評価準備をBase学習と並行して進める。Phase 6で10B Baseが成立すればPhase 7へ進め、20B・50BをChat開始の前提にしない。単一4090ではGPU実験を順番に実施し、CPUでのデータ整理・評価準備を並行する。

**確定（実行場所）**: Phase 0〜3はiMacで実施し、Phase 4からWindows/WSL＋RTX 4090へ移行済み。Phase 4のNorm/default eager運用上限はT8K 57 / T4K 64。Phase 6③ではNoNormのreference/math最大45、compiled/math最大53、compiled Flash最大111を検証。最速はFlash＋compile reduce-overhead batch 32、694,521 tokens/sで、容量上限と最高速度を分ける。[高速化完了記録](29_phase6_performance_completion.md)、[移行成果物・確認条件](07_environment.md)

## 高速に完成させる進め方

**確定（優先方針）**: ユーザーは完成までの時間短縮を優先する。Windows/WSLへの切替とPhase 4は完了した。Phase 5の候補選定まで完了し、Phase 6①〜⑤、5Bと各100M比較、10B準備が完了。本10B科学学習・保存確認・同条件品質評価は完了し、Base/Chat品質目標は未達。Phase 3をGPUで最初からやり直すことは移行の前提にしない。

Phase 3の最終検証一式はM1 iMac上で24.62秒。これは実装後の検証時間で、コード作成・修正、Tokenizer学習、runtime初回build、docs更新を含まない。作業全体の約25分と区別し、GPUへの変更で実装時間まで短縮すると見積もらない。[実測report](../reports/phase3/export_parity_report.json)

Phase 4は以下の順で実施済み。新規環境への移行・実装変更時にもこの検証順を使う。すべてのPhase 4完了条件は維持する。

1. **移行・CUDA確認**: GitのコードとGit管理外のTokenizer/pilotを引き継ぎ、hash/ID一致、GPU/driver/PyTorch/BF16を確認する。Macのnative binaryや仮想環境はコピーしない。
2. **最小の学習経路**: 検証済みモデルを使い、AdamW/BF16、uint16 shard、本文NLL/BPB・生成評価、checkpointを実装する。まず小batchでfiniteな1 stepまで成立させる。
3. **保存再開の検証**: 同じ環境で連続200 stepsと100→保存→再開100 stepsを比較し、消費token列・loss・weightsを確認する。
4. **速度と最大batchの実測**: batchを倍増して境界を見つけ、中間値で最大安定値を測る。compile初回と定常速度、backend、syntheticと実shardのI/O、評価・保存時のVRAMも記録する。最大安定batchと最高速度のbatchは両方残す。

変更した箇所と関連gateを検証し、関係のないPhase 1取得・Tokenizer再学習・CPU GGUF全検証を繰り返さない。artifactを変更した場合、移行先で数値差が出た場合、学習済みモデルを配布する場合は対応する検証を再実行する。

最初のChat完成に必要なPhase 0〜8を優先し、20B/条件付き50B、Muon等の追加比較、hybrid、クラウド並列研究はbaseline成立後に進める。小探索では主要因を一つずつ比較し、総当たりを前提にしない。データは次の段階で使う量から準備し、master corpus全量取得を学習開始の条件にしない。

**時間見積もり**: 「学習開始まで1〜2日、初版Chatまで1〜3週間」は会話中の粗い仮見積もりで、確定scheduleへ採用しない。実装作業時間とGPU計算時間を別々に記録する。変更後の採用設定で検証済みのPhase 6③のtokens/secから`残りtokens / tokens/sec + 評価・保存・比較runの時間`を計算し、段階ごとに更新する。品質の修正が必要な場合は追加実験を別に見積もる。

## Phase 0: 成功条件・環境・実験管理

**状態**: 完了。詳細な実path・検証範囲は[完了記録](16_phase0_completion.md)と[完了監査](../reports/phase0/completion_audit.json)を参照する。以下は実施した内容で、Windowsの実機確認はPhase 4へ残す。

実施時点のhashとsnapshotは履歴として保存する。計画やREADMEの更新で現fileが変わった場合も、過去runのsnapshotと監査を上書きしない。Tokenizer/data入力のartifact hashは作成前のため`null`で、各フェーズの完成後に実fileを記録する。

**目的**: 学習できたことと、狙った短文対話が成立したことを区別して判定できるようにする。

**ゴール**: runを再構築できる記録形式と、結果を見る前に固定した評価仕様がある。

作業:

- リポジトリ骨格、依存version固定、run ID、artifact naming、seed管理、config schemaを作る。
- iMac側の環境を記録し、Windows/WSL用の依存設定と移行手順を用意する。WSL 3.xの実導入version、GPU、driver、OS、PyTorch/CUDA、ストレージの実機確認は切替時に行う。
- Base評価、Chat評価、tokenizer契約、数値誤差、停止ID、公開対象のデータbucketを仕様化する。
- Base completionとChat各100件の独自prompt suiteを作成し、各dev 80件・最終test 20件へ分けた。Chatは挨拶、感情応答、質問返し、訂正、2〜数ターンの文脈を含む。

**成果物（作成済み）**: [experiment schema](../schemas/experiment_schema.json)、[iMac環境記録](../reports/phase0/environment.json)、[評価仕様](evaluation_protocol.md)、[固定promptとsplit](../eval/README.md)、[実行入口](../scripts/experiment.py)、`pyproject.toml`・`uv.lock`・`.python-version`。

**完了条件**: 同じrun IDからcode commit、config、依存環境、データ/Tokenizer hashを特定できる。Chat rubric、BPB分母、generation設定、dev/testの用途が明記される。評価例を手で採点し、ルールの曖昧さを修正する。

**次へ進む判断**: iMac上の設計・データpilot・Tokenizer・CPU実装検証は進められる。4090の実機記録は移行時のgateとし、Phase 4のGPU検証と学習開始前に確認する。

## Phase 1: データの小規模pilotと評価split

**状態**: 完了。[実施結果・実path・限界](17_phase1_completion.md)、[全件検証](../reports/phase1/verification.json)、[再生成一致](../reports/phase1/reproducibility.json)を参照する。Phase 0の共通前処理を使い、[処理コード](../src/jmicro/data.py)と[実行入口](../scripts/prepare_phase1.py)を作成した。

**目的**: 日本語短文・雑談へ容量を使い、出所不明の混合や評価漏洩を避ける。

**ゴール**: 100M探索まで使う小規模corpusと、Chatに使える会話候補の実量・品質が分かる。

取得に使用したsource:

| source | 確認したrevision・条件 | pilotでの扱い |
|---|---|---|
| FineWeb2 Edu Japanese / `small_tokens_cleaned` | revision `180ca004c6a89b590daaad86cb062a07a5353c69`。配布READMEにODC-By v1.0とCommon Crawl利用条件を記載 | 小規模Web pilotに採用。READMEで先頭0〜9,999行と10,000〜19,999行の重複を告知しているため、先頭10,000行を避け、取得後にも重複を検査する |
| RealPersonaChat | revision `28d0b6b3865b29cabc26c230a2db37cdf315e937`。LICENSEはCC BY-SA 4.0 | 会話pilotに採用。Webとは別bucketで出所・条件を記録し、persona・人口統計metadataは学習入力へ含めない |

根拠: [FineWeb2 Edu Japaneseの固定revision README](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese/blob/180ca004c6a89b590daaad86cb062a07a5353c69/README.md)、[RealPersonaChatの固定revision LICENSE](https://github.com/nu-dialogue/real-persona-chat/blob/28d0b6b3865b29cabc26c230a2db37cdf315e937/LICENSE)。取得済みmetadata・形式確認用previewは`data/phase1/source_metadata/`に保存した（Git管理外）。調査metadataは処理入力へ流用せず、固定revision原fileを取得してpilotとsplitを作成した。証拠のURL・revision・取得file hashはsource台帳へ固定済み。

**実施した取得範囲**: [config](../configs/data/pilot.json)へschema、保存先、容量上限、選択方法を固定し、Web 20,000文書、会話3,000対話を取得した。採用はWeb 19,998文書、会話3,000対話、合計42,647,826 canonical UTF-8 bytes。取得数とfilter後の採用数を分け、unique量・反復回数・実際の学習tokensを別に報告する。100M tokensの探索に不足する場合は取得範囲の拡張または明示した反復で対応し、unique 100M tokensを取得済みとは扱わない。

実施項目:

1. source台帳とdocument/dialogue manifestのschemaを作り、source/subset/revision・利用条件・raw/canonical hash・cluster・splitを記録できるようにする。
2. 確認済みrevisionを台帳へ固定し、少量sampleの取得範囲・容量上限・保存先を決めて本文を取得する。viewer previewのrevisionと固定revisionを混同しない。巨大データ全量の取得は先行しない。
3. sampleを共通前処理、filter、dedupへ通し、train/dev/testを固定する。Phase 0の`eval/`はモデルの固定生成suiteであり、新しいcorpus splitとは別管理する。
4. trainだけからTokenizer学習sampleを選ぶ。4k/8kで同じdocument集合・順序・hashを使えるようにする。
5. 使用条件を満たす短文会話候補で1k〜10k対話のpilotを作り、件数・応答長・turn数・品質をreportする。教師tokensはPhase 2で実計数する。

作業:

- [データ設計](05_dataset.md)に従ってsource/subset/revision、利用条件、raw/canonical hash、品質、splitを持つmanifestを作る。未確認sourceは採用を保留する。
- FineWeb2 Edu Japanese等から小subsetを取り、弱い前処理、言語・品質filter、日本語向けexact/near/cross-dataset dedupをpilotする。
- duplicate cluster単位でtrain/dev/testを分離してからTokenizer学習sampleを選ぶ。
- 使用条件を満たす候補から1k〜10k対話のpilotを作る。speakerの向き、personaの扱い、tree復元、window化前のsplitを確認する。
- domain別bytes、短文比率、会話長、品質のsample目視を記録する。会話の定型挨拶を文書重複と同じ基準で一律削除しない。

**成果物（作成済み）**: `data/phase1/processed/`の`dataset_manifest.parquet`、`split_manifest.json`、`corpus.jsonl`、`tokenizer_sample.jsonl`。data/dialogue report・レビュー・検証・再生成比較は`reports/phase1/`。[詳細・checksum・再生成手順](17_phase1_completion.md)

**完了条件**: 任意の採用文書・対話をsourceとsplitへ追跡できる。既知重複とtrain/eval間の検出重複を除外し、未検出の限界も記録する。対話件数、unique bytes、応答文字数、turn数の分布が分かる。1024-token内に収まる割合と教師token数はPhase 2で計測・追記する。

**次へ進む判断**: 会話候補が不足する場合は独自会話例でmask/評価の開発を進めつつ候補を追加する。量の不足を、同じ少数対話を反復した見かけのtokensで解決したことにしない。

## Phase 2: 4k/8k Tokenizerと会話形式

**状態**: 完了。[実施結果・artifact・再現手順](18_phase2_completion.md)。同一sampleで全6coverage候補が合格し、両語彙で0.9995を採用。外部codecのgolden・全corpus round-tripと会話token量を実計数した。

**目的**: 小語彙でも日本語・記号を扱い、学習とローカル推論で同じID列を使う。

**ゴール**: 語彙4096/8192の二つのSentencePiece Unigram + byte fallback artifactと、共通の入出力契約がある。

作業:

- 同じtrain sampleでcoverage候補を比較し、必須文字・256 byte pieces・8特殊tokenを含む予算を確認する。
- 正規化、空白、改行、タブ、結合文字、顔文字、未知文字のgolden例を固定する。
- role/EOTを構造IDとして挿入し、本文中の同じ文字列表記と区別する。学習後の語彙追加を避ける。
- domain別chars/token、bytes/token、fallback率、context超過率と会話の総/教師tokensを測る。

**成果物**: 4k/8kの`tokenizer.model`、設定・sample hash、`special_tokens.json`、`tokenizer_contract_report.json`、`tokenizer_comparison.json`。

**完了条件**: piece数と特殊IDが期待値と一致し、golden例が定義したcanonical textへround-tripする。全byte piecesと異常入力を検証する。同じartifactでencode結果が再現でき、再学習時の一致範囲も記録される。

**次へ進む判断**: 圧縮率だけで勝者を決めず、両候補をPhase 5へ渡す。4kが予算内で成立しない場合はcoverage/前処理を再検討し、語彙数を黙って変更しない。[詳細仕様](13_tokenizer_dialogue_data_research.md)

## Phase 3: モデル・cache・学習前export

**状態**: 完了。[実施結果・artifact・再現手順](19_phase3_completion.md)。両モデルの実parameter数・forward/backward・1024までのcache、公式HF・native float GGUF、Q8/Q4の読込生成を検証。内蔵Tokenizerに不一致があるため外部SentencePiece経路を採用した。

**目的**: 10M予算と正しい因果生成を満たし、長期学習後に推論形式で詰まるのを防ぐ。

**ゴール**: T8K/T4Kがforward/backward・cache生成・保存読込でき、配布経路の計算とTokenizerを検証できる。

作業:

- RMSNorm、RoPE、GQA、head間gain共有QK-Norm、SwiGLU、tied embeddingを実装する。
- parameter count、未来参照遮断、GQA mapping、padding、finite gradientを検証する。
- prefill、1-token decode、chunk decode、長さの違うcacheで全系列logitsとの一致を検証する。
- ランダム重みをHF参照モデル、float GGUFへ写し、同じ入力IDsでlogits/cacheを比較する。
- 内蔵Tokenizerのgolden parityとEOT停止を検証する。不一致なら外部SentencePieceでencode/decodeする呼び出し経路を実装する。
- Q8/Q4候補で読込・生成、tensor別量子化型、FFN幅576/640でのfallbackと実容量を確認する。

**成果物**: T4K/T8K config、`model_contract_report.json`、`export_parity_report.json`、実行可能な推論入口。

**完了条件**: 提案仕様のQK-NormありでT8K=9,772,800、T4K=10,002,816 parameters。cache/因果性の検証が通り、floatの数値差が事前定義した許容値内。選んだ配布経路で学習時と同じTokenizer契約を再現できる。

**次へ進む判断**: 外部SentencePiece経路ならその依存も配布計画へ含める。汎用GGUF CLIへの互換性は別項目として記録する。ランダム重みの量子化成功は会話品質の成功を意味しない。[モデル仕様](12_training_implementation_research.md)、[export仕様](14_evaluation_deployment_research.md)

## Phase 4: 学習器・shard・再開・4090 benchmark

**状態**: 2026-10-03に完了。WSL 3.0.1.0 / Ubuntu WSL 2 / RTX 4090でCUDA/BF16確認と64 tests / skip 0、両モデルの200 vs 100+100完全一致、全dev・固定生成suite、最大batch・backend/compile・予算を実測・監査した。[完了記録と測定の制約](21_phase4_completion.md)を参照する。Phase 5も[完了](23_phase5_completion.md)し、Phase 6①〜⑤、5Bと各100M比較、10B準備が完了。本10B科学学習・保存確認・同条件品質評価は完了し、Base/Chat品質目標は未達。

**目的**: 長期runを失わず、実際の計算・ストレージ予算に収める。

**ゴール**: 実shardでの学習・中断再開が成立し、以降の実験時間を実測から見積もれる。

作業:

- `uint16` shard、document index、checksum、mmap loader、決定的shuffle/mixture samplerを作る。
- GPU実機検証の前にWindows PCのWSL 3.x/Linuxへ切り替え、同じcommit/config、Tokenizer、sample、hashを引き継いでCUDA動作を確認する。
- AdamW、FP32 parameter + BF16 autocastを基準にloss、gradient accumulation、schedulerを実装する。
- model/optimizer/scheduler/RNG、消費済みデータ位置、tokens/steps、全hashを保存する。optimizer更新境界で保存し、一時fileからのatomic renameを行う。
- Phase 0の準備run記録を基に、学習runの開始/完了/失敗、checkpoint、metricsのschemaと台帳を追加する。準備runの`tokens_seen=0`を学習結果として流用しない。
- Baseの本文NLL取得、window/strideの採点、BPBと生成suiteの実行を実装する。共通bytes・本文を一度だけ採点することを検証し、Phase 5の比較前に評価runnerを使えるようにする。
- 連続200 stepsと100 steps→保存→再開100 stepsを同一環境で比較する。
- T4K/T8Kのsynthetic/実shardでmicro batchを最大安定値まで増やし、compile、backend、data wait、peak VRAM、保存時間を測る。micro batchとeffective batchを区別する。

**成果物**: 実機`environment.json`、`handoff_report.json`、`resume_report.json`、`throughput_report.json`、`base_evaluation_contract_report.json`、`resource_budget.md`、復元可能checkpoint。

**完了条件**: Windows/WSLへ移行済みで、CUDA動作と引継ぎartifactの一致を確認する。再開前後の消費token列が一致し、loss/weightsが同一環境で許容誤差内。累積lossの正規化、shard境界、評価によるRNG干渉を検証済み。BPB runnerの本文一度採点・共通bytes分母と固定生成suiteの実行を確認する。compile初回と定常速度を分け、実shardで運用できる最大安定batchと速度が分かる。

**次へ進む判断**: `予定tokens / 実測tokens/sec + 評価・保存・停止・分岐の時間`で100M/1B/10B/20B/50Bを見積もる。raw、一時領域、4k/8k shards、checkpointの容量を合算する。予算外ならまずbatch/I/O/探索本数を調整し、実験条件を台帳へ記録する。

## Phase 5: overfit・10M smoke・100M比較

**状態**: 2026-10-03に完了。4本の100Mと補助予算を評価し、T4K / NoQK-Norm / LR 0.002を1候補に選定。全68 tests / skip 0、CUDA厳密resumeと独立監査が成功。品質の未達も[完了記録](23_phase5_completion.md)へ保存し、Phase 6①〜⑤、5Bと各100M比較、10B準備が完了。本10B科学学習・保存確認・同条件品質評価は完了し、Base/Chat品質目標は未達。

**目的**: 実装不備を小予算で見つけ、長期学習へ渡す候補を根拠で選ぶ。

**ゴール**: 100M時点で発散しない候補を最大2つ選べる。

作業:

- 小データ100件のoverfitでloss低下と学習例の再現を確認し、別runで10M-token smokeを行う。
- 100MでT4K/T8Kを比較する。次にQK-Norm有無、LR、必要ならMuon+AdamWを、一度に一つの主要因だけ変えて比較する。全組合せの総当たりは前提にしない。
- 同じvalidation文書のBPB、共通短文window、生成失敗、実時間、処理bytes、更新回数を保存する。
- 同一tokens、同一学習bytes、同一GPU時間の条件を区別する。補助比較は対応するcheckpointまたは別runで行い、条件が揃わない結果へ同じラベルを付けない。

**成果物**: `smoke_report.json`、`tokenizer_model_comparison.json`、候補config、`candidate_selection.md`。

**完了条件**: finite loss/gradient、保存再開、EOS生成の検証が通る。BPBの改善と失敗率の推移を比較でき、候補選定理由・棄却理由を記録する。100Mで自然な雑談が完成することは要求しない。

**次へ進む判断**: 候補がすべて発散・悪化する場合はデータ、mask、LR、batchを切り分けてPhase 2〜4へ戻る。BPB差が小さい場合は速度・fallback・生成失敗・推論互換性を含めて最大2候補を残す。

## Phase 6: 500M〜10B Base v1

**状態**: 主要Web5Bと各100M仕上げ比較、直接10Bの[専用準備](40_base_10b_preparation.md)、総10,000,007,168 tokensの[本学習と保存確認](41_base_10b_training.md)を完了。10B同条件品質評価も完了（BPB0.954018 / 固定EOS0・反復53 / raw Unicode0）。最速設定はFlash＋compile reduce-overhead / batch32、今回の実学習も約694〜695k tokens/s。過去の[準備①②](26_phase6_preparation_completion.md)、[高速化](29_phase6_performance_completion.md)、[④⑤](30_phase6_readiness_execution.md)を保持し、完了済みstudyを繰り返さない。

**目的**: 約10Mで日本語短文生成がどこまで成立するかを測り、Chatの土台を作る。

次回の一区切りは[直接10Bの学習・同条件評価・報告と停止](39_learning_scale_and_generation_plan.md)。stable4.75B親から9.5Bへ継続し、独立decayで10Bへ到達する。既存5B/Web5.1B評価を再利用し、新10Bだけ評価する。step2学習に続くstep3品質評価も完了した。今回はreport/commitで停止し、後続学習は開始しない。

**ゴール**: 選定済み10M候補を直接10Bまで学習・評価し、10Bの`JMicro-10M-Base-v1`と固定評価を残す。

| 累積tokens | 目的・判断 | 残すもの |
|---:|---|---|
| 500M | 初期改善と反復悪化の確認 | checkpoint、BPB/生成/速度 |
| 1B | 日本語生成の立ち上がり、候補最大2つ | 比較表、候補更新理由 |
| 2B | 過去355M/約2B経験との観察点整理 | 規模・Tokenizer・データ差を明記した記録 |
| 5B | 本命1つの決定 | 選定reportと継続config |
| 10B | Base v1の固定評価 | weights、Tokenizer、model card、全評価 |

作業（500M〜10Bの学習・同条件評価は完了。品質未達は保持）:

- 既存12.23B trainを使う。50〜100B master候補全量の取得を先行せず、実量と目標を混同しない。
- 各段階に必要なshardsから用意し、未使用全量の処理を10B開始の前提にしない。
- BPB、短文品質、反復、EOS、Unicode、追加GPU時間を段階ごとに記録する。
- 固定mixtureのscaling系列を残す。目的に合わせたmixture変更は別条件として記録する。
- Phase 5でWSDを採用し、Phase 6②でstable/decayの実装・CUDA全state再開/分岐完全一致を確認済み。現在のbatch/backend/数値配分は[直接10B専用設定](../configs/phase6/base_10b.json)へ凍結済み。従来version2は保持する。継続stable枝と評価decay枝を区別して追加computeも計上する。StableExtensionTrainerの明示forkは実装・10B準備検証済み。20B/50Bには新しい予算・履歴・再開確認が必要で、通常resumeでは予算を変更しない。

**成果物**: 段階checkpoint、`base_scaling_report.json`、`base_v1_evaluation.md`、継続用checkpoint、master corpus manifest。

**完了条件**: 本命の10B checkpointを再構築・再開でき、固定suiteとheld-out corpusの結果がある。短文の文法・関連性と破綻例を人手で確認し、[品質目標](#品質目標と判断ルール)の達成/未達を明示する。過去モデルのartifactがない場合は直接比較を未実施と明記する。

**次へ進む判断**: Baseの日本語生成が成立すればPhase 7へ進む。成立しない場合は量だけを増やさず、日常短文mixture等の対照実験を行う。修正後も未達なら容量・データの限界として報告し、成功扱いにしない。

## Phase 7: Dialogue mid-trainingとAssistant-only SFT

**目的**: 流暢な続きを生成するBaseから、入力に関連した短い応答で会話を続けるChatへ移す。

**ゴール**: 文法・関連性・2〜数ターンの文脈・停止を評価した`JMicro-10M-Chat-v1`を作る。

作業:

- Phase 1の会話pilotを拡張し、sourceごとのunique対話/bytes/総tokens/Assistant教師tokens/反復回数を固定する。
- Dialogue mid-trainingのmixture、loss範囲、LR、pilot予算と拡張上限を開始前にconfigへ記録する。
- 主系列はBase→mid-training→SFT。小規模なBase→SFT対照を残し、mid-trainingの効果を分離する。
- role metadataからAssistant本文+EOTの教師maskを作る。shift、PAD、教師0件、長い対話の古い完了turn切り捨てを検証する。
- SFTの累積総系列10M→30M→100M tokensを候補とし、毎段階devで比較する。教師token数とunique量は別記録し、悪化時は100Mまで強制継続しない。
- Base、mid-training後、SFT後を同じ固定prompt/seedで比較する。greedyと複数seed sampling、人手rubricと自動失敗率を分ける。
- Phase 0の固定履歴suiteに加え、モデル生成を履歴へ戻す2〜数ターンのrolloutと自動失敗flagを実装する。モデル名を伏せた人手評価と評価者一致率を記録する。

**成果物**: 会話manifest、`assistant_mask_report.json`、各段階checkpoint、`chat_ablation_report.json`、`chat_v1_evaluation.md`。

**完了条件**: mask/停止の検証が通り、独立した対話splitで評価済み。採用checkpointがdev上で関連性・文脈を改善し、反復・役割混同・空応答・停止失敗・Base流暢性の退行を報告する。最後に未使用testで品質目標を判定する。

**次へ進む判断**: 最良checkpointを選びPhase 8へ。未達なら応答長/品質/mixture/LR/反復回数を一要因ずつ見直す。蒸留を使う場合はcorpus-only baselineと別系列にする。

## Phase 8: 量子化・ローカル実行・再現手順

**目的**: 学習結果を手元で使える形にし、容量と品質の実際のtradeoffを示す。

**ゴール**: Base/Chatのfloat版と採用量子化版を、学習環境以外でも手順から起動できる。

作業:

- 学習済み重みでPhase 3のHF/float GGUF parityとcache/停止を再実行する。
- Q8とQ4候補を比較し、tensor別実型、file容量、Tokenizer込み全artifact、RSS、cacheメモリを測る。
- 対象CPU/OS/threadsを明記し、load、初回token時間、prefill/decode、応答総時間のp50/p95を測る。context1024は生成分も含めて管理する。
- floatとの差をBPB、人手関連性/文脈、Unicode、反復、role/停止で確認する。
- model card、採用source一覧、帰属、既知の限界、hash、runtime commit、量子化設定、実行/再現コマンドを揃える。

**成果物**: Base/Chat artifacts、`quantization_report.json`、`local_inference_report.json`、`reproduction_guide.md`、配布manifest。

**完了条件**: 独立環境でBase completionと2〜数ターンのChatが動く。学習時と同じencode/decode、EOT/EOS停止が成立し、量子化の退行を品質条件内に収める。全容量・速度・必要依存を実測値として提示する。

**次へ進む判断**: Q4が品質を満たさなければQ8/混合精度も比較する。5〜10MB級へ収まらない場合はサイズ目標未達を明記し、形式/precisionの追加検証を残す。artifactを用意したことと品質・容量目標達成を区別する。外部公開・Hub uploadはこの文書作成では実行しない。

## Phase 9: 20Bと条件付き50Bのscaling

**目的**: 固定10Mモデルへ追加学習する価値と、容量/データ反復の限界を確認する。

**ゴール**: 10B対20Bの差を測ってBase v2を評価し、50Bへの進行/停止を根拠で決める。

作業:

- 実装済みstable予算延長forkについて新20Bの固定条件・履歴・全state検証を確認してから継続用checkpointで20Bへ進み、固定mixture・同じ評価条件で10Bと比較する。通常resumeで終端budgetを変更しない。
- document単位のpaired bootstrapでBPB差と95%信頼区間を記録し、短文品質、失敗率、uniqueデータ露出と追加GPU時間を併記する。
- 50Bは20Bでも改善継続があり、生成失敗が悪化せず、追加時間/ストレージが予算内の場合のみ進む。
- 新Baseが有望なら同じChat手順を適用してv1と比較し、Phase 8の学習済みexport/量子化評価も再実行する。

**成果物**: `base_v2_evaluation.md`、`scaling_extension_decision.md`、実施した場合の50B checkpointと限界report。

**完了条件**: 20Bの比較と50B Go/No-Goを記録する。50Bを実施した場合は評価まで完了する。実施しない判断にも改善量、信頼区間、失敗率、予算の証拠を付ける。

**次へ進む判断**: 小さい改善しか残らない/悪化する場合は停止し、データ適合性またはPhase 10の比較へ移る。decay済み評価枝とstable継続枝の履歴を混同しない。

## Phase 10: 追加研究とVast.ai並列比較

**目的**: 完成したTransformer baselineと比較して、能力密度・計算効率をさらに改善する。

**ゴール**: 変更ごとに同じ目的・評価条件で採用/棄却を判断できる。

優先順はLayer Sharing（12 unique/24 logical）、teacher応答テキスト蒸留、ReLU²、Mamba2+Attention、Conv+Attention、5M/10M/25M/50M/100M規模比較。各実験では「改善したいmetric、parameter/compute予算、同一条件、採用基準」を先に記録する。異なるTokenizer間のlogitsをindexで直接KL比較しない。

Vast.aiはローカルで検証済みの独立runを並列化する後半用途に限定する。利用時の価格で再見積もりし、既存方針の上限$1,000に対して実験別計算時間・storage・失敗時費用を計上する。この計画作成で課金jobを開始しない。

**成果物**: 追加研究proposal、対照run、`research_comparison.md`、費用/速度/品質の台帳。

**完了条件**: 実施した各変更をbaselineと比較し、採否・限界を記録する。採用案は再現性、Chat評価、export、量子化まで再検証する。候補全部の実施を最初のBase/Chat完成条件にはしない。

**次へ進む判断**: 品質または速度が事前の採用基準を満たす変更だけを次の比較へ進める。改善が不明確な変更は結果を保存して保留し、追加computeで得られる情報と費用から再実験の優先度を決める。

## 品質目標と判断ルール

技術的完了と能力目標を別に管理する。Phase 8までのartifact・検証が揃っても、以下が未達なら「目的を達成した」とは記載せず、未達metricと次の対照実験を残す。

以下の数値はPhase 5の100M候補の結果を見る前に、初期提案を維持して**凍結済み**。10Mで達成できると実証した値ではない。Phase 0でsuiteと採点例を定め、Phase 5のdev/pilot評価では未達もそのまま記録する。変更理由と旧値を記録し、最終testを見て閾値を下げない。量子化の退行幅はfloat dev評価後、量子化候補選定前に別途固定する。[凍結の記録](22_phase5_plan.md#公平な評価と候補選定)

| 目的 | 判定方法・初期目標 | 判定するフェーズ |
|---|---|---|
| 日本語短文生成 | Base completionの文法2/2が70%以上。文字/記号の破綻と反復も別集計 | 6 |
| 入力に関連する短い雑談 | Chatの文法・関連性が両方2/2の応答が70%以上。文字数分布も併記 | 7 |
| 2〜数ターンの文脈維持 | 2〜4ターンsuiteで直前の条件/訂正を保持し、文脈2/2が60%以上 | 7 |
| 会話の停止と役割 | 停止成功95%以上、空応答5%以下、役割漏出1%以下、Unicode破綻は固定suiteで0件 | 7・8 |
| 量子化して使える | 全artifact容量5〜10MB級を目標に、floatとのBPB/品質/失敗率差を報告。許容退行幅はfloat dev評価後、量子化候補選定前に固定 | 8 |
| 長期学習の継続価値 | BPB改善幅（10B BPB − 20B BPB）の95%信頼区間の下限が0を越え、生成失敗に重大退行がなく追加予算内なら50B候補 | 9 |

停止等の失敗率はgeneration抑制設定を併記し、ID列で測る。人手評価はモデル名を伏せ、文法/関連性/文脈を各0/1/2で採点する。率は分母とsample数を付け、全体だけでなくcategory別も報告する。関連性が伸びても反復が増える等の重大退行は採用判断へ反映する。

品質条件はdevで選定し、独立testで最終確認する。testで未達なら結果を報告し、次の改訂では新たな未使用testを用意する。[評価の詳細](14_evaluation_deployment_research.md)

## 横断して残す記録と最初の着手順

全runでcode commit、config、依存version、Tokenizer/data hash、seed、tokens seen、unique docs/bytes/tokens、更新数、micro/effective batch、wall time、失敗理由を残す。SFTでは総系列tokensとAssistant教師tokens、WSDでは分岐ごとの履歴を分ける。比較する条件を変えたら別run IDにする。

Phase 0〜4の骨格・データpilot・Tokenizer・両モデル/cache/export・Windows/WSL移行・学習器・評価・保存再開・実機速度は完了済み。Phase 5のoverfit/smoke・4本の100M比較・候補選定が完了し、Phase 6①〜⑤、5Bと各100M比較、10B準備が完了。本10B科学学習・保存確認・同条件品質評価は完了し、Base/Chat品質目標は未達。巨大コーパス全量取得、50B開始、追加hybridを先行しない。

具体的な着手checklistは[次の実装タスク](10_next_steps.md)、各技術判断の根拠と実測待ち項目は[追加調査](11_technical_research_gaps.md)を参照する。
````

## docs/windows_handoff.md

更新前file SHA256: `1924ce960547458da728c7eda0a47ab0ca25db9223cef71a1490bce11b05a9e3`

````markdown
# Windows/WSL引き継ぎ

最新・計画58段階1〜3完了・停止（2026-10-05 JST）: [結果60](60_dataset_expansion_results.md)。教材200,000,192tokens/新140,036,743、旧/新各追加1B、日本語192/331/1119・dev256・全160個別内容、一次35/最終20checks完了。常識は改善したがEOS34→25/一貫性15→9等で候補不採用、条件付き全文未開始。科学2,000,027,648/検証262,144別、GPU3129.607秒。actual239609は終了し、完成screenを追加学習として再起動しない。元UI actual359102/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks7216365/ready08:29:21.306388Z、HTTP親SHA410f975d…/tokens10,000,007,168/busy=false復帰確認。引継ぎはLinux `reports/phase6/dataset-expansion-1b-20261005/` の両終端・500M中間checkpoint/metrics/source/全評価raw/160annotations/review/judgment/completion/jobと、`~/jmicro-data/phase6/dataset-expansion-20261005/` の200M shards/manifest/ready/content-review/新source pin・README/receipt、旧60M source・元10B/既存run、Windows正本最新local commitを含む。Git/Hubだけでこのデータとweightsを復元できない。primary reviewは別v2でLR記録時点を厳密修正、凍結v1/科学source/品質gate不変。新source/長さ/EOS密度差・独立corpus監査/人手blind未完了を保持し、量だけの効果としない。新data/GPU/20B/50B/Chat/test/push/publicationは今回対象外。以下の実行中identityや旧停止は履歴。

最新・計画58段階1〜3実行中（2026-10-05 JST）: 教材200,000,192 tokens（旧59,963,449＋新公開TinyStories日本語訳140,036,743）準備、40全文レビューで弱例18開示、CPU5tests、config/schema/source凍結commit03346a7。平均長/EOS密度も変わるため量だけの比較ではない。hidden Windows21040/actual Linux239609/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6902884で旧/新各追加1Bを実行中。実CUDA保存再開25checks成功/検証262,144別、旧pool対照学習中。Linux `reports/phase6/dataset-expansion-1b-20261005/screen-job.json`・各枝metrics/latest/checkpointとWindows同run stdout/stderr/launchを追跡し、actual liveなら新起動しない。元UIはGPU中停止、wrapper finallyで元10Bへ復帰する。終了後、同じ日本語192/331/1119・dev256・全160内容と原採否条件、必要時だけ全文/400/長文、report/local commit/復帰確認まで必要。教材 `~/jmicro-data/phase6/dataset-expansion-20261005/` と新source pinned README/receipt/全raw、旧60M source・元10B/既存全runを移す。中断復旧コマンドは `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/run_dataset_expansion.ps1 -Mode screen`、actual process終端と有効checkpointを先に確認する。20B/50B/Chat/protected test/pushは対象外。以下の計画56停止は完了履歴。

計画56段階1〜3完了・停止（2026-10-05 JST）: matched教材各22,977,241tokens/253,119全文の各500M比較を完了。対照→追加選別はEOS39→44/反復16→17/一貫性11→11/適切完結14→15（各80）で不採用。段階2も省略せず旧59,963,449-token物語固定/一定LR0.0001で連続1Bを完了し、500M→1BはBPB0.982953243→0.981611241/EOS31→35/反復21→10/一貫性11→19/適切完結15→20。意味60.417→66.146%（対応95%+1.563〜+10.417pp）と複数指標は改善したが、一貫性95%下限0、EOS35<37、内容各27未達、Web BPB比+1.0335%で原採用条件未達。両条件付き全文は未開始。CPU10tests/実CUDA25・13/一次32・29/最終要求別31checks成功、全320内容保存。科学2,000,027,648/検証524,288別、一次GPU3331.359秒。元final10B UI actual237483/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6728695/ready07:08:04.599378Z、HTTP親SHA410f975d…/tokens10,000,007,168/busy=falseとactual process確認。科学234687/236557/教材234279は終了し再起動しない。結果と提案はdocs/57_matched_story_and_learning_budget_results.md、最終確認reports/phase6/matched_story_completion.json。11B checkpoint・両run全raw/metrics/source/annotationsをLinuxへ保存。追加学習の効果を否定せずBase/Chat未達、次の小規模条件保持教材診断/LR減衰/新data/GPU/20B/50B/Chat/protected test/pushは提案のみで未開始。local commitで今回停止し、以下は実行当時の履歴。


計画56段階1完了／段階2凍結: matched各22,977,241-token教材で各500,006,912追加tokens、実EOS教師Web846,893/story1,101,267を一致。GPU1659.584秒・科学1,000,013,824/検証262,144別。dev/日本語全完了・全160個別内容・CPU32evidencechecks成功。対照→候補BPB0.979944438→0.980233205、EOS39→44/反復16→17/一貫性11→11/適切完結14→15（各80）、対応95%−8.75〜+8.75ppで改善条件未達・不採用。条件付き全文は開始しない。次は旧採用59,963,449-token物語pool固定、元10Bから一定LR0.0001で追加連続1,000,013,824tokens、500M中間/1B終端を保存して両地点評価。段階1科学234687終了、元UI235943へ復帰確認済み。段階2config/schema/sourceを凍結したが新科学はまだ未開始。


計画56段階1〜3実行中（2026-10-05 JST）: 二組各22,977,241tokens/253,119全文、body平均88.7764（旧88.4621）、同じ長さ並び/BOS/EOS位置。CPU抽出11.146秒、random40各に弱例14/12を個別明記してbounded比較を受入。CPU10tests成功・凍結commit a8215aa。2026-10-05 06:09頃、hidden Windows34620/actual Linux234687/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6377461で教材二条件各500Mを開始。実CUDA25checks通過、対照学習中。Linux reports/phase6/matched-story-content-500m-20261005/screen-job.json と Windows同run screen.stdout.log/stderr.logを追跡。UIはGPU中停止/finally復帰。段階1未達でも段階2の固定教材・一定LR連続1B（500M中間/1B終端）は必要。全320内容と日本語評価・事前条件付き全文、判断/report/local commit/元UI復帰で停止。科学・一次結果は未確定、20B/Chat/test/pushは開始しない。


最新完了（2026-10-05 JST）: [計画54](54_complete_document_500m_execution.md)段階1〜4を[結果55](55_complete_document_500m_results.md)まで完了、新110M完結文500M条件は不採用、CPU一次22/最終51項目成功。条件付き全文は未開始。元final10B UI actual232991/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6169021/ready05:34:47Z、HTTP SHA410f975d…/tokens10,000,007,168/busy=false。科学232272/教材231819・231975は終了し再起動しない。Linux reports/phase6/complete-document-500m-20261005/のcheckpoint/metrics/source/全raw/80annotations/review/source-origin-diagnosis/judgment/completion/jobと、~/jmicro-data/phase6/complete-documents-20261005/のfirst4B job・継続job・110M shards/index/manifest/ready/random40/content-reviewを引継ぐ。Windowsのcomplete_document_*.json/実装/config/schema/最終report/local commitを保存して停止。次案は未実行で、新GPU/1B/20B/Chat/test/pushは自動開始しない。以下の旧現在地・identityは履歴。

最新完了（2026-10-05 JST）: [計画52段階1〜4](52_story20_low_lr_execution.md)の学習・評価・判断を完了し、[最終判断/次案53](53_story20_low_lr_judgment.md)・local commitで停止する。各500M/四地点一次/全320内容診断/条件付き全文・400・長文を実施、CPU37/全文30項目成功、候補は原比較条件を全通過した研究候補。品質目標は未達。科学174280/全文177987は完了・終了、旧runを再起動しない。元final10B UIがLinux231106 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks4964393 / ready2026-10-05 02:14:01.602203Zで復帰し、actual processとHTTP SHA410f975d…/tokens10,000,007,168/busy=falseを確認した。引継ぎには100M run全raw、500M runの四checkpoint/全metrics/四地点raw/320annotations/primary reviewとfull全raw/source/job/result/review、`~/jmicro-data/phase6/simple-stories-ja-budget-20261005/`のsource/shards/content-reviewを含める。物語pool59,963,449 tokens/約1.667周使用。科学1,100,021,760/検証524,288別会計。次のデータ構成比較は提案のみで、今回未開始。要求別確認は`reports/phase6/story20_execution_completion.json`。以下の旧停止境界は履歴として保持する。

最終更新: 2026-10-05 JST。[現在地](autonomous_status.md)と[最新比較48](48_complete_text_10b_comparison.md)を最初に読む。改善計画段階1〜3の学習・評価を完了し、最終report/local commit・UI復帰で停止する。以下の旧milestone記録は履歴として保持する。以前の停止境界・process情報・移行履歴は[2026-10-04保存履歴](autonomous_history_20261004.md)、初期復旧は[2026-10-03履歴](autonomous_history_20261003.md)に残す。

最新の移行対象: Linux `reports/phase6/complete-text-10b-100m-20261004/`（三枝checkpoint/metrics/raw240内容採点/source、旧失敗`conditional-full/`、完了`conditional-full-r1/`全文/400/長文rawを含む）と`~/jmicro-data/phase6/simple-stories-ja-20261004/`（固定source metadata/二つのtrain parquet/25,000,067-token shards）。Windowsの最終review/result/completionと最新local commitも移す。Linux17951/19791/37818は終了、再実行しない。新物語は親BPB悪化上限を超え未採用、Base/Chat品質目標は未達。UIは元final10B SHA410f975d…へ復帰、復帰時Linux49746 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks1043870、HTTP応答確認済み。現在のUI identityは`reports/local/webui/server.json`とactual processを照合する。完了比較の再開commandを追加学習に流用しない。

さらに新しい計画49の実行は[50](50_story10_and_budget_execution.md)/[判断51](51_story10_judgment_and_next_proposal.md)。Linux`reports/phase6/story10-10b-100m-20261005/`と`story10-low-lr-10b-100m-20261005/`のcheckpoints/metrics/source/raw generation/全240 annotations/tests/job/result/reviewも引き継ぐ。両10%枝は一貫性差4/6で未採用、全文と500Mは条件により未実施、科学139467/140216は終了。完了runnerを再起動しない。最新復帰時UI140800 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks1468219、元final10BでHTTP応答。次案20%低LR100Mは未実行で、今回はreport/local commitで停止する。

追加した日本語Base評価v2.1は[実施計画](45_japanese_base_evaluation_v2.md)/[実測結果](46_japanese_base_evaluation_v2_results.md)と`reports/phase6/japanese_base_v2_review.json`を参照する。移行時はLinux `reports/phase6/japanese-base-v2-20261004/`のraw/source/cpu、`japanese-base-v2-20261004-r1/pilot`の修正版意味診断、`~/jmicro-data/evaluation-v2`の公開評価cache/manifestも保存する。完了runのGPU再実行は不要。UIは評価後に復帰済み。新規評価の一括入口は`scripts/run_japanese_evaluation.ps1`で、UIを停止・finally復帰する。

## 引継ぎ先と現在地

| 項目 | 現在の内容 |
|---|---|
| コード・docs・lock正本 | Windows `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m` |
| Linux実行コピー | `/home/aihub_ubuntu/src/japanese-tiny-llm-10m` |
| Linux data | `/home/aihub_ubuntu/jmicro-data` |
| repository | [private GitHub](https://github.com/ayutaz/japanese-tiny-llm-10m)。移行時はWindowsの最新local commitも引き継ぐ。remoteだけを最新と仮定しない |
| 実測済み環境 | WSL package 3.0.1.0 / Ubuntu WSL 2 / RTX 4090 / Windows driver 616.92 |
| Python / PyTorch | uv Python 3.12.7 / PyTorch 2.14.1、CUDA 13.0 |
| モデル・データ | 10,001,152 parameters / 準備済みtrain12,225,819,077 tokens |
| 学習・比較 | 主要Web10B、100M配合/LR比較、計画52の20%低LR100Mと各500M・一次/全文/長文評価完了。500M枝各総10.5B、物語pool59.96M。Base/Chat品質は未達 |
| 次の行動 | 判断53・要求別確認・local commitを保存して停止。次の新pool/500Mデータ構成比較・各枝1B/20B/50B/Chatはユーザー再開まで開始しない |

現在のPCは復元・CUDA検証済み。setup、Tokenizer学習、完了済みGPU studyを再実行しない。ユーザー指定step2の総10B学習と保存結果確認は完了。再開されたstep3品質評価も完了した。[品質結果](42_base_10b_quality_evaluation.md)。今回はreport/local commitで停止する。[本学習結果と速度](41_base_10b_training.md)。

## 現モデルをローカルで試す

2026-10-04の追加依頼で、学習済みfinal10BのWeb UIを起動した。Windowsのブラウザから `http://127.0.0.1:7860`。再起動は `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/start_webui.ps1`、停止は `scripts/stop_webui.ps1`。WSL/RTX4090で推論し、稼働中はGPU lockを保持する。[操作・保存先](43_local_webui.md)。学習・後続実験は再開していない。

## 1. Windows側でWSLとGPUを確認

新規PCや環境変更時にPowerShellで `wsl --version`、`wsl -l -v`、`nvidia-smi` を確認する。WSL package 3.xとdistributionのWSL 2は別の値。Windows driverでWSL CUDAを利用し、WSLへLinux display driverを追加しない。現在の固定構成は実CUDA/BF16学習で動作確認済み。

新規PCの準備が必要な場合のみ `powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\setup_windows_wsl.ps1` を使う。既存treeを上書きせず、OS昇格・再起動・初回Linuxユーザー作成が必要ならその外部操作をblockerとして記録する。

## 2. Linux側でコードとuvを準備

新規PCではprivate repositoryの認証・取得後、Windowsの最新local変更を保持して引き継ぐ。Macのvenv/native binaryは移さない。project rootで不足する環境だけ復元する。

```sh
uv python install 3.12.7
uv sync --frozen --python 3.12.7 --extra hub --extra data --extra ml --extra export
git config --local user.name yousan
git config --local user.email ka1357amnbpdr@gmail.com
```

すべてのPythonは `uv run --frozen --extra hub --extra data --extra ml --extra export ...`。依存変更は `uv add`。system Python/pipへ切り替えず、固定依存にアクセスできなければblockerを記録する。

## 3. Hugging FaceからTokenizerとデータを復元

固定[公開pilot/Tokenizer](https://huggingface.co/datasets/japanese-data-analyze/japanese-tiny-llm-10m-artifacts)は約107MB、25 payload。commit `0b1042979bf32899e24da30790e3ae6b239013c3`、manifest SHA256 `8072bd218be26637a51c7c11540f1c8c636392c3b1a91f805a5e317e6ca55a09` を使う。新規PCで不足する場合のみ実行する。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/download_hub_artifacts.py
```

hash確認後に `artifacts/phase2/{4096,8192}/` と `data/phase1/processed/` へ復元する。内容が異なる既存fileは上書きしない。[詳細](huggingface_handoff.md)。Hubには学習重み・12.23B shards・大型checkpointは含まれない。

## 4. 契約とCUDA環境を確認

新規環境・runtime変更時に必要な環境gateと関連testsを新しい `reports/local/handoff/` 等へ保存する。既存の完了reportを上書きせず、CPU成功をGPU成功に数えない。current runtimeの変更がなければ完了済み全suite・GPU比較を再実行しない。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/experiment.py capture-environment --probe-torch --output reports/local/handoff/environment.json
```

最新10B準備は[14 CPU testsと実CUDA全state一致、26 review checks](40_base_10b_preparation.md)で確認済み。旧Phase 4/5/6準備の証拠は各完了記録を保持する。

## 5. 入力・run・checkpointを引き継ぐ

Linux dataの `phase6/ten-billion/prepared-v2/export-001/shards`、必要なraw、Tokenizer、以下のrunとsource snapshot/log/checkpointを別途コピーする。Git/Hubだけでは復元できない。

- `reports/phase6/base-5b-20261004/`: stable親 `stable/checkpoint-00144959.pt`（4,750,016,512 tokens）とfinal5B `decay/checkpoint-00152588.pt`。
- `reports/phase6/eos-5b-finish-100m-20261004/`: Web/short20の `checkpoint-00155640.pt`、raw生成・評価。
- `reports/phase6/base-10b-20261004/`: 準備検証と科学job完了。stable9.5B/final10Bの両checkpoint、metrics/source/log/resultを保持。[保存結果](41_base_10b_training.md)。
- `reports/phase6/base-10b-comparison-20261004/`: 完了した同条件品質評価の全文文書別NLL、400 raw生成、固定80比較packet、自然停止9件、job/result/log/sourceを保持。[品質結果](42_base_10b_quality_evaluation.md)。評価Linux442/Windows31900は終了済み。
- 過去Phase 0〜5とPhase 6準備のreport、weights、native runtimeは保持する。

checkpointはmodel/optimizer/scheduler/RNG/sampler位置/消費tokensを完了updateで保存する。通常resumeでschedule/config/source/dataを変更しない。4.75B親SHAと各重みSHAは[status](autonomous_status.md)および保存reportを参照する。

長GPU jobはhidden Windows supervisorとLinuxのactual PID/boot ID/start ticks/stage/logを保存し、`~/jmicro-data/gpu.lock`で排他する。10B準備のLinux PID459・Windows PID29620は終了済みの履歴で、現在のjobではない。起動前に実process・GPU一覧・既存runを確認し、有効checkpointから再開する。

## 6. 実装済みCLIと次回の再開

AdamW、WSD stable/decay、StableExtensionTrainer、EOS短文mixture、学習/BPB/生成、表示helperは実装済み。Chat trainerとUTF8制約decoderは未実装・未適用。新10B専用品質比較は実装・実行済みで、同条件dev/400と内容確認を完了。学習完了CPU reviewは実装し、実際の終端保存stateと全metricsの19項目を確認済み。準備reviewを科学完了に流用しない。

中断復旧用コマンド履歴（今回のrunは完了しているため再起動しない）:

```sh
bash scripts/run_base_10b.sh --train
```

引数なし/`--verify-only`は準備確認だけで、完了済みならGPU検証を繰り返さない。旧5BやPhase 5 launcherを新10Bのcommandとして起動しない。学習後、新10Bだけ全文dev/固定400で評価し、既存5B・Web5.1B結果を再利用する。今回はstep3評価も完了し報告・commitで停止する。後続実験は別の再開依頼で進める。[残りの手順](27_phase6_remaining_plan.md)

## 次の担当へ渡す文面

```text
AGENTS.md、docs/autonomous_status.md、docs/15_project_roadmap.md、docs/windows_handoff.md、docs/39_learning_scale_and_generation_plan.mdを読んでください。
主要Web5Bと追加各100M仕上げ比較、直接10Bの準備が完了しています。10B科学学習step2とCPU保存確認19項目は完了、同条件品質評価step3も完了しています。
現在の指定step3も完了です。BPB0.954018 / 固定EOS0・反復53 / raw Unicode0、元増量gate合格と品質未達を保持してください。完了runを再起動せず、後続EOS/UTF8/Chat/20Bは新しい実行依頼に従ってください。
完了済みGPU study、旧5B比較、Tokenizer学習、大型全corpus照合を繰り返さないでください。
Pythonはuv、Linux dataを使用してください。actual process/lock/checkpointを確認して二重起動を避け、失敗証拠と未達品質を保持してください。
Windows正本の最新local commitとLinuxのsource/hashを確認してください。自動pushはしないでください。
```

## この手順の検証範囲

記載環境は現在のPCで動作確認済み。10B準備の実CUDA16更新/524,288検証tokensは科学学習tokensとは別会計。独立全12.23B監査は未完了。10Bの同条件自動評価と内容診断は完了、独立人手blind/test、Chat、新重みの量子化品質は未検証。品質基準を緩めず、新規環境では必要な変更部分を検証する。
````

## docs/README.md

更新前file SHA256: `df07a3230c5d4f8372142d8348149be9c0a702b6fa55dc2d29e0c676e85747c2`

````markdown
# JMicro-10M 設計・調査ノート

最終更新: 2026-10-05 JST。現在地は[status](autonomous_status.md)、完了した最新比較は[完結文比較48](48_complete_text_10b_comparison.md)、全体の品質目標は[roadmap](15_project_roadmap.md)を参照する。段階1〜3完了で停止する。

日本語Base追加評価は[計画・仕様v2.1](45_japanese_base_evaluation_v2.md)と[現在10Bの実測結果](46_japanese_base_evaluation_v2_results.md)。文法/常識/含意/容認度/読解・基本意味・長文反復・Codex内容診断を追加し、独立人手と品質合格は別に扱う。

評価後の提案は[データ・学習改善計画](47_post_evaluation_training_plan.md)。ユーザーが再開した段階1〜3の実行は[完結文配合の三条件100M比較](48_complete_text_10b_comparison.md)に記録する。追加500M〜1B/20Bは次回以降。

比較後の最新提案は[配合・学習量計画49](49_next_mixture_and_training_budget_plan.md)。新物語10%・100Mを先に比較し、安全条件を通ればpool60Mと各500Mの学習量比較を検討する。今回は計画のみで、追加学習は開始しない。

最新実行は[計画49の実行50](50_story10_and_budget_execution.md)、[判断・次案51](51_story10_judgment_and_next_proposal.md)。物語10%と失敗時の低LR同量比較を完了した。一貫性差4/6で8件基準に達せず、全文/500Mを開始せず停止。次案20%・低LR100Mは提案のみ。UIは元final10Bを維持する。

## 現在の要約

モデルは10,001,152 parameters、T4K / NoQK-Norm / AdamW / context1024。主要Web総10Bと、同じ親からWeb/既存短文20%/新物語20%各100Mの比較を完了した。新物語poolは25,000,067 tokens。固定EOS0/3/24、反復60/55/24（各80）、新物語の全文BPB0.955765は元親0.954018からの悪化上限を超え未採用。一次35/全文43証拠checks成功、UIは元final10Bを維持。準備済みWeb trainは12,225,819,077 tokens、独立全corpus監査は未完了。Phase 0〜5・Phase 6準備は完了済み。

直接10Bの専用準備は完了（14関連tests、実CUDA全state保存再開、26 review checks）。本10B科学学習とCPU保存確認19項目、再開された同条件品質評価とCPU確認23項目も完了。BPB0.954018・固定反復53・Unicode0、固定EOS0の課題は残る。今回はreport/commitで停止する。

本文BPBは改善したが、自然停止・反復・意味品質は不足。以前の5B親での短文20%は固定EOS13/80へ改善したが全400 raw Unicode2件で最終採用不合格。表示helperの採用をraw品質成功とは扱わない。独立人手blind/test、Chat、新重みの量子化品質は未検証。

学習はWSL2/RTX4090/Linux disk、Python3.12.7をuvから実行する。容量最大batch111と最速batch32（約694k tokens/s）を区別する。Tokenizer/モデルと学習前export、GPU学習器・評価・保存再開は実装済み。完成したBase/Chat・配布品質とは別である。

## 文書内のラベル

- **確定**: 合意した方針・凍結条件。
- **確認済み**: 保存した実装・測定・一次資料に証拠がある内容。
- **提案/要検証**: 将来の比較候補。実行済みや品質達成とは扱わない。

過去の調査・完了記録は当時の証拠。旧500M/2B/7.5B計画と指示は[保存履歴](autonomous_history_20261004.md)へ分離した。現在の指示はAGENTS.mdとstatusを正とする。[Windows/WSL引き継ぎ](windows_handoff.md)、[残りの作業](27_phase6_remaining_plan.md)、[checklist](10_next_steps.md)を入口にする。

## 文書一覧

1. [01_project_goal.md](01_project_goal.md) — 目的、成功条件、過去モデルとの位置付け
2. [02_research_summary.md](02_research_summary.md) — 調査結果と採否の要約
3. [03_architecture.md](03_architecture.md) — モデル仕様、パラメータ予算、派生案
4. [04_tokenizer.md](04_tokenizer.md) — 4k/8k Tokenizer、特殊token、正規化
5. [05_dataset.md](05_dataset.md) — データ候補、ライセンス、50〜100B master corpus
6. [06_training_plan.md](06_training_plan.md) — 段階学習、SFT、Vast.ai方針
7. [07_environment.md](07_environment.md) — RTX 4090、WSL、8TB、shard配置
8. [08_evaluation.md](08_evaluation.md) — 評価、checkpoint、TDD、再現性
9. [09_prior_art_and_baselines.md](09_prior_art_and_baselines.md) — 25M/100M configと100M以下の公開モデル
10. [10_next_steps.md](10_next_steps.md) — フェーズ別計画に対応した実装checklist
11. [11_technical_research_gaps.md](11_technical_research_gaps.md) — 追加調査の入口、未解決課題、優先順位、検証gate
12. [12_training_implementation_research.md](12_training_implementation_research.md) — QK-Norm仕様、cache、parameter再計算、段階学習、4090 benchmark
13. [13_tokenizer_dialogue_data_research.md](13_tokenizer_dialogue_data_research.md) — 正規化、特殊token、4k語彙予算、会話データ候補、SFT、蒸留
14. [14_evaluation_deployment_research.md](14_evaluation_deployment_research.md) — BPBの実装、公平な比較、雑談評価、GGUF、量子化、CPU推論
15. [15_project_roadmap.md](15_project_roadmap.md) — 目標から逆算したフェーズ別計画、目的・ゴール・成果物・完了条件・進行判断
16. [16_phase0_completion.md](16_phase0_completion.md) — Phase 0の実施結果、要求ごとの証拠、検証範囲、次の着手
17. [17_phase1_completion.md](17_phase1_completion.md) — 実データpilot、manifest・split、会話品質、Tokenizer sample、再生成・完了監査
18. [18_phase2_completion.md](18_phase2_completion.md) — Tokenizer学習・入出力・会話tokensの実測
19. [19_phase3_completion.md](19_phase3_completion.md) — モデル/cache/HF/native GGUF/量子化の実測
20. [20_publication_review.md](20_publication_review.md) — 当時の公開前確認、ローカル情報除去
21. [21_phase4_completion.md](21_phase4_completion.md) — WSL/CUDA・学習器・保存再開・評価・容量・速度の実機証拠
22. [22_phase5_plan.md](22_phase5_plan.md) — Phase 5の目的・条件・予算・scheduler判断
23. [23_phase5_completion.md](23_phase5_completion.md) — overfit/smoke/100M比較・候補選定・品質未達・独立監査
24. [24_phase6_plan.md](24_phase6_plan.md) — 実学習5B・仕上げ結果と直接10Bの現在地・予算
25. [25_phase6_preparation.md](25_phase6_preparation.md) — ①②の事前の目的、凍結条件と停止境界
26. [26_phase6_preparation_completion.md](26_phase6_preparation_completion.md) — ①②の実量、全corpus/CUDA監査、保存先、実CLI
27. [27_phase6_remaining_plan.md](27_phase6_remaining_plan.md) — 直接10Bの残る作業、EOS/UTF8後続候補、Chat・量子化・条件付き拡張
28. [28_phase6_performance.md](28_phase6_performance.md) — ③の実GPU高速化・backend実効確認・容量と厳密再開の比較
29. [29_phase6_performance_completion.md](29_phase6_performance_completion.md) — ③の採用速度・最大容量・厳密/cold再開・独立監査と停止記録
30. [30_phase6_readiness_execution.md](30_phase6_readiness_execution.md) — ④⑤の限定比較、CPU精度修復、正式検証・凍結設定・commitと停止記録


- [32_local_10b_corpus.md](32_local_10b_corpus.md) — 大規模corpus構築の履歴。現行量・利用確認と独立監査の範囲はstatusを正とする
- [35_base_5b_execution.md](35_base_5b_execution.md) — 主要5B学習の実行記録
- [36_base_5b_comparison.md](36_base_5b_comparison.md) — 主要5Bの固定評価比較
- [37_eos_repetition_utf8_improvement_plan.md](37_eos_repetition_utf8_improvement_plan.md) — EOS・反復・UTF8改善の事前計画
- [38_eos_5b_finish_results.md](38_eos_5b_finish_results.md) — Web/短文比較の結果と採用不合格
- [39_learning_scale_and_generation_plan.md](39_learning_scale_and_generation_plan.md) — 現行の直接10B・評価・報告と後続候補
- [40_base_10b_preparation.md](40_base_10b_preparation.md) — 完了した専用10B準備。科学学習の完了ではない
- [41_base_10b_training.md](41_base_10b_training.md) — 総10B学習・保存確認の完了時の記録、実測速度。品質比較は後続42へ
- [42_base_10b_quality_evaluation.md](42_base_10b_quality_evaluation.md) — 同条件dev/400品質比較、生成内容、元gateと未達課題
- [43_local_webui.md](43_local_webui.md) — 学習済み10BモデルのローカルUI、起動・停止と実操作確認
- [44_japanese_base_evaluation_audit.md](44_japanese_base_evaluation_audit.md) — 現行評価の不足、日本語Baseの追加benchmark/意味診断、v2実装案
運用文書: [最新状態](autonomous_status.md)、[復旧履歴](autonomous_history_20261003.md)、[Windows/WSL引継ぎ](windows_handoff.md)、[固定Hub復元](huggingface_handoff.md)、[自律runner](codex_automation.md)、[評価仕様](evaluation_protocol.md)。[data](../data/README.md)、[eval](../eval/README.md)、[reports](../reports/README.md)に各保存領域の手順を記載する。

実行時の仕様は[評価仕様](evaluation_protocol.md)と[Windows/WSL移行手順](windows_handoff.md)を参照する。データとTokenizerの[Hugging Face公開版の取得手順](huggingface_handoff.md)も利用できる。

## 追加調査の要点（2026-10-02）

未実装のまま残っていた技術判断を、一次資料と公式コードから補足した。最初は[追加調査の入口](11_technical_research_gaps.md)を読む。

- **提案**: QK-NormをQwen3式のhead次元RMSNormとして具体化すると、T8Kは9,772,800、T4Kは10,002,816 parametersとなる。旧概算との差はgainの共有方式による。
- **提案**: SentencePieceの正規化と構造tokenの挿入方式を固定し、本文中の役割表記と構造IDを区別する。
- **提案**: BPBに加え、同一原文bytesと同一GPU時間での比較条件を用意する。
- **提案**: 長期学習前にランダム重みでHF／GGUF互換性を確認する。FFN幅576／640ではK-quantの型fallbackを確認する。
- **確認済み**: llama.cppの一般的なSentencePiece変換経路と独自Unigramの分割方式は同一ではない。内蔵Tokenizerへの互換性を検証し、必要なら外部SentencePieceでIDを作る経路を使う。
- **現在の判断**: 4090速度はPhase 4、会話教師token量はPhase 2で実測済み。Phase 5の候補選定は完了。雑談品質・学習後の量子化品質と、拡張corpus/長期予算での優位性は未達・未実証。

追加調査は学習・推論実験を実施した結果ではない。既存の確定方針を維持し、実装候補と検証条件を追加している。

## 重要な注意

公開データの「商用利用可能」は、データセット配布ライセンスだけで最終判断しない。Common Crawl由来データでは、データベースライセンスと各Web文書の著作権は別問題である。公開・販売前に、採用した各source subsetの利用条件、帰属表示、ShareAlike条件、削除要求対応を再確認する。本書は法的助言ではない。

最終更新: 2026-10-04。外部資料の調査日は各文書へ残し、研究候補と実装・実測結果を区別する。
## 完結文比較の完了

[完結文配合の三条件100M比較](48_complete_text_10b_comparison.md): 限定data/EOS確認、25M候補pool、同じfinal10Bからの三条件学習・内容/全文/長文評価を完了。採用条件未達を保持し、report/local commitで停止。各500M〜1B/20Bは未開始。
````

## docs/10_next_steps.md

更新前file SHA256: `d5da88228a5afe2d6bdc23bb96b8719fc6030f4e58cb952310faff8983600624`

````markdown
# 次に進める作業

2026-10-04更新。[現在地](autonomous_status.md)と[具体的な計画](39_learning_scale_and_generation_plan.md)に合わせる。**総10B学習step2とCPU保存確認19項目を完了。今回は報告とcommitで停止する。** ユーザーが再開した同条件品質評価step3も完了。[評価結果](42_base_10b_quality_evaluation.md)。[結果と速度](41_base_10b_training.md)。

## 完了していること

- [x] Phase0〜5の環境・Tokenizer・モデル・GPU学習器・評価・保存再開・候補選定。
- [x] 既存12.23B train tokens整備。独立全件auditの未完了は保持し、再照合を繰り返さない。
- [x] 主系列総5B学習と同じdev/生成比較。
- [x] final5BからWeb対短文20%各100Mと条件付き全文評価・内容確認。短文はraw Unicodeで採用不合格。
- [x] UTF8表示末尾helperを実装し、raw失敗・IDs・bytes・停止理由を保持。
- [x] 直接10B専用config/schema/launcher、14tests、実CUDA全state/history再開一致。[準備証拠](40_base_10b_preparation.md)。

## 次の実行区切り

- [x] 保存stable4.75Bから総10,000,007,168 tokens/update305176へ継続。実Linux/Windows processの終了を確認した。
- [x] stable9.5Bと最終decay checkpoint、連続/有限更新、Adam/scheduler/RNG/cursor/消費counterを専用CPU reviewerで確認した。
- [x] step3の専用品質比較入口とCPU reviewerを実装し、関連23tests成功。旧reportは保持。
- [x] 新10Bだけ全文dev89,416/本文164,344,743bytesと400生成を評価し、5B/最良Web5.1Bを再利用した。
- [x] BPB/EOS/反復/raw flagsと全固定80・自然停止9件の内容を比較。CPU保存確認23項目成功。元増量gateは合格、Base/Chat品質未達を報告し、local commitで停止する。

既存12.23Bを使用し、7.5B専用decay/中間全文評価、新しい収集、旧GPU比較、全コーパス再監査は追加しない。学習GPU上限9,000秒（準備19.217秒を含む）、別評価予約1,800秒。見積もり145〜165分、実装と内容確認は別。

## その後の候補

10Bの改善と元raw増量安全条件を満たした場合、同じ新親のWeb/短文20%各100Mを一対だけ比較する。途中不正UTF8と未完成末尾には保存重みの単一制約decoderを別policyとして比較する案がある。これらは現在未実装・未起動で、元raw失敗を合格に書き換えない。

Base/Chat品質条件、人手blind評価、未使用test、Assistant body＋EOT学習、量子化/local品質は[ロードマップ](15_project_roadmap.md)の条件を維持する。20B/50B、Chat、unlikelihood、parameter sweep、外部出版・有料cloudは現在の作業範囲に含めない。

古い500M/1B前停止や未着手記録は [履歴](autonomous_history_20261004.md) に保存した。
````

## docs/27_phase6_remaining_plan.md

更新前file SHA256: `ad814758e0b711913c2f30c6dd10712d339c82530b2be4c7d4197fd66196b886`

````markdown
# Phase 6以降に残る作業

最終更新: 2026-10-04。実際の現在地は[status](autonomous_status.md)、今回の数値・採否条件は[直接10B計画](39_learning_scale_and_generation_plan.md)を正とする。以前の500M、2Bデータ拡張、7.5B案と当時の指示は[履歴](autonomous_history_20261004.md)へ保存した。

## 完了した範囲

Phase 0〜5、Phase 6①〜⑤、主要Webの総5,000,003,584 tokens学習、同じ5B親からWeb100%と短文20%を各100,007,936 tokens追加する比較を完了した。各仕上げモデルの累積は5,100,011,520 tokens。モデルは10,001,152 parametersであり、Bは学習tokensを表す。

準備済みtrainは12,225,819,077 tokens。builder/raw再構成/実loaderで利用を確認したが、独立全corpus監査は未完了のまま記録する。新規取得や全件再照合を10B学習の前提にしない。

[10B専用準備](40_base_10b_preparation.md)は完了。関連14 CPU tests、stable/decayの実CUDA連続対保存再開16更新、保存review26 checksが成功した。これは準備の証拠であり、ユーザー指定step2の科学学習とCPU保存確認19項目も完了した。[本学習結果](41_base_10b_training.md)。再開された同条件品質評価も完了。[品質結果](42_base_10b_quality_evaluation.md)。

## 直接10Bの学習・品質評価の完了状況

1. 実行設定の準備は完了。既存process、GPU lock、runとcheckpointを読み取り確認して二重起動を避ける。
2. 保存済みstable4.75B親から専用設定で9.5Bまで継続し、独立decayで総10,000,007,168 tokensへ到達済み。追加科学学習は5,249,990,656 tokens。7.5B専用decay・評価は省く。
3. 新10Bだけ同じ全文devと固定400生成で評価し、元5Bおよび最良Web5.1Bの保存評価と比較する。専用品質比較入口を実装し、同条件dev/400と全固定80・自然停止9件の内容確認を完了。CPU評価確認23項目成功。学習完了CPU reviewはscripts/review_base_10b_training.pyに実装し、実行中jobを完了扱いしないguardを確認済み。実際の終端保存stateと全科学metricsへ適用し、19項目成功した。
4. BPB、EOS、反復、raw Unicode、内容の誤り、学習量とGPU時間を報告してcommitし、停止する。到達tokensとBase品質達成を別に判定する。

中断復旧用コマンド履歴はWSL project rootで `bash scripts/run_base_10b.sh --train`。引数なし/`--verify-only`は準備確認で、科学学習を開始しない。今回のstep2学習と保存結果確認は完了し、report/commitで停止する。完了runを再起動しない。ユーザーが再開したstep3の全文/生成品質評価も完了し、追加学習は開始しない。

科学学習GPU上限9,000秒（準備検証19.217秒を含む）、評価予約1,800秒、合計10,800秒。学習区間約126分、評価込み145〜165分の見積もりで、実装・内容確認は別。[専用設定](../configs/phase6/base_10b.json)を変更せず、通常resumeで終端budgetを変更しない。

## EOS・反復・UTF8の後続候補

短文20%は固定EOS 0→13/80、反復57→51/80へ改善したが、全400 raw Unicode失敗2件で最終採用不合格だった。表示helperは採用済みで、raw失敗を成功に数えない。[比較結果](38_eos_5b_finish_results.md)

10Bが本文BPB改善と元の安全条件を満たした場合だけ、新10B親からWeb/短文20%を各100Mで一対比較する候補がある。完了済み5B比較を繰り返さず、比率/LR sweepを先行しない。UTF8制約付き推論は別条件として未実装で、元方式と同じ400生成・上限・seedで比較する。詳細は[計画](39_learning_scale_and_generation_plan.md)。これらは10B結果報告後の判断対象であり、今回の文書更新で開始しない。

## Base品質からChat・量子化へ

本文BPB改善だけで文法・意味・自然停止の合格とはしない。独立人手blind採点、保護test、Chat品質、新しい重みの量子化品質は未実施。[roadmapの品質目標](15_project_roadmap.md#品質目標と判断ルール)を維持する。

Baseの短文生成が成立したらDialogue mid-trainingとAssistant本文＋EOTだけを教師にするSFTを実装し、効果を分けて比較する。Chat trainerは未実装。Chat後に量子化・実容量・CPU速度・独立環境での品質を検証する。既存のNoNorm CPU精度profileの変換成功を、未評価の新重みの配布品質へ流用しない。

## 20B・50Bと追加研究

20B/50Bは現在の実行範囲に含めない。StableExtensionTrainerの明示forkは実装済みだが、新しい予算・data・履歴・再開検証を固定してから使う。50Bは20BのBPB改善差の95%信頼区間下限が0を超え、重大な生成退行がなく、実測追加予算内の場合だけ候補にする。

Tokenizer再学習、Muon、unlikelihood、architecture sweep、クラウド比較は先行しない。追加研究は比較対象・予算・終了条件を定め、有料クラウド、公開、他者への連絡には個別の指示が必要。Pythonはすべてuv、WSL/Linux data、checkpointと失敗証拠を保持し、local commitを行う。自動pushはしない。
````

## docs/codex_automation.md

更新前file SHA256: `7c93bfea3b56f5dc2c70983deeb4460d082c40f81ea4a998ccd6b37ce1e7936e`

````markdown
# Codexによる環境整備・学習・改善の自動化

現在地（2026-10-04）: Phase 0〜5、Phase 6準備、主要Web5B、各100M仕上げ比較、直接10B専用準備は完了。10B科学学習step2とCPU保存確認19項目は完了、同条件品質評価step3も完了。[品質結果](42_base_10b_quality_evaluation.md)。[学習結果](41_base_10b_training.md)。現在の指定範囲は再開された10B品質評価で、評価・内容確認を完了しreport/local commitで停止。[最新状態](autonomous_status.md)、[直接10B計画](39_learning_scale_and_generation_plan.md)、[準備証拠](40_base_10b_preparation.md)を参照する。

Full accessは既に実効policyへ反映済みで、ユーザー側のrunner起動を学習開始条件にしない。起動前にAGENTS.mdの範囲とactual job/lock/checkpointを確認する。completeはその時の指定範囲を証拠で完了したことを示し、Base/Chat完成とは区別する。科学jobはユーザーのstep2再開指示で実行・完了し、実processも終了済み。完了runを再起動せず、今回のreport/local commitで停止する。

以下のCLI 0.159.3・アプリ設定・公式資料の説明は2026-10-03に確認した履歴で、今回の文書更新では製品設定を再調査・変更していない。旧作業の指示は[保存履歴](autonomous_history_20261004.md)を参照する。

## このアプリで続ける

初回にモードが表示されない場合はSettings → General → Permissionsで有効化し、その後に入力欄下の権限メニューで選択する。[公式のモード選択](https://learn.chatgpt.com/docs/permission-modes)。入力欄下に選択肢がある場合は**Full access**へ変更する。公式の対応設定は`approval_policy = "never"`と`sandbox_mode = "danger-full-access"`。[OpenAI公式の権限説明](https://learn.chatgpt.com/docs/sandboxing)

Workのnetwork設定が提供されている場合は、Settings → Data controls → Work network accessでAllow public internet accessを有効にする。管理対象の環境で選択肢が無効な場合は管理者側のpolicy変更が必要。ユーザー設定は管理policyを上書きできない。変更が反映された実行環境で続きを進める。

当初の制限された会話ではグローバル設定を変更できなかった。2026-10-03にユーザーのFull access選択が実効policyへ反映され、会話内からWSL・network・CUDAにアクセスできた。グローバルconfigは変更していない。project内の設定fileは実行中セッションの権限を変更しない。

## CLIのプロジェクト用profile

通常のPowerShellでproject rootから実行:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install_codex_autonomous_profile.ps1
codex --profile jmicro_autonomous --cd . "AGENTS.mdとdocs/autonomous_status.mdに従い、環境整備から学習・評価・改善まで継続してください"
```

installerは既存グローバルconfigを変更せず、`$CODEX_HOME/jmicro_autonomous.config.toml`（未指定時は`%USERPROFILE%\.codex\`）へproject専用profileを作成する。同名profileが異なる場合はbackupを残す。今回確認したCLI 0.159.3の`--profile`は`<name>.config.toml`を重ねる仕様。既存のmodel選択・ログインを引き継ぐ。実際のCLI helpと[公式設定説明](https://learn.chatgpt.com/docs/config-file/config-reference)を再開時にも確認する。

CLIの設定はアプリの既存会話を変更しない。管理policyやWindowsの管理者権限を回避するものでもない。WSL導入/driver更新のOS側昇格、再起動、Linux初回ユーザー作成、初回ログインは外部操作として残る場合がある。

## 無人の継続runner

Codex CLIと保存済みログインを利用する。通常端末で:

```powershell
uv run --frozen scripts/run_codex_autonomous.py --max-turns 20
```

WSL内でCLIを利用できる場合はLinuxコピーで:

```sh
uv run --frozen scripts/run_codex_autonomous.py --max-turns 20
```

runnerはprofileのinstallなしでも、起動するCodexに`approval_policy=never`と`danger-full-access`を指定する。制限された会話から権限拡張用に起動する手段には使わない。Full accessが反映された環境または通常端末から実行する。表示だけの確認は`--dry-run`。

各回のCodexが実装・学習・検証を行い、`continue`なら次の回を開始する。`complete`、外部操作が必要な`needs_user`、CLIエラー、20回の起動上限で終了する。上限終了はproject完了を意味しない。無制限retryや無制限の改善探索は行わず、同じcommandで状態fileから続けられる。1回の作業時間やCodex accountの利用上限はrunnerが解除できない。[公式non-interactive実行](https://learn.chatgpt.com/docs/non-interactive-mode)

`reports/automation/<UTC-id>/`に各回のprompt、JSONL events、stderr、最終JSON、最新resultを保存する。exit codeは0=要求達成、2=runner/CLIエラー、3=外部操作待ち、4=起動回数上限。`runner.lock`で二重runnerを防ぐ。強制終了後にlockが残った場合は記録されたPIDの終了を確認してから除去する。学習jobの二重起動はagentがcheckpoint/run記録とPIDを確認して避ける。

コードの継続runnerと、長時間GPU学習のcheckpoint/監視/再開は別の機能。GPU側はPhase 4で排他lock、PID/boot ID/start ticks、stage/run記録、atomic checkpointとhashを実装し、hiddenのWindows `wsl.exe` supervisorで検証jobを保持した。スリープ・再起動・ログイン切れで永続実行は保証せず、中断時はcompleted-update checkpointから再開する。

Pythonの実行はrunner・テスト・一時スクリプトを含め`uv run --frozen`経由に統一する。Python 3.12.7が未導入なら`uv python install 3.12.7`で導入し、依存は`uv sync --frozen`で復元する。固定環境を取得できない場合はblockerを記録し、system Pythonへ切り替えない。

## 実施した検証

`uv run --frozen python -m unittest discover -s tests -p test_codex_automation.py -v`で再実行できる5件のstubテストが成功。実Codexを呼ばないローカルstub subprocessで、継続結果の引継ぎ、終了条件、CLI失敗時の診断、二重起動防止を確認した。dry-run/profile previewと各fileの構文も確認。このstub結果だけでは実Codex/GPU成功を証明しない。後続のPhase 4では全64 tests / skip 0と実GPU学習・保存再開・評価・容量測定を完了した。[実機証拠](21_phase4_completion.md)。

初回stub検証はuv統一前の履歴。現在の再実行は`uv run --frozen python -m unittest discover -s tests -p test_codex_automation.py -v`を使う。
````

## reports/README.md

更新前file SHA256: `a5da103705ae6c536dd585727578e52c666e5f0cdad0c43cb2df639545e98999`

````markdown
# 実験台帳と検証結果

## 現在の結果（2026-10-04）

| 保存report | 実際に確認したこと |
|---|---|
| [corpus_10b_ready_review.json](phase6/corpus_10b_ready_review.json) | train12,225,819,077 tokensをbuilder/raw再構成/実loaderで受け入れ。独立全corpus auditは未完了 |
| [base_5b_review.json](phase6/base_5b_review.json)、[比較review](phase6/base_5b_comparison_review.json) | 主要Web5,000,003,584 tokensの実学習・保存・全文dev/固定400評価 |
| [eos_5b_finish_review.json](phase6/eos_5b_finish_review.json)、[Unicode原因確認](phase6/eos_5b_finish_unicode_review.json) | 同じ5B親から各100,007,936追加。Web BPB0.958092、短文0.959011、短文EOS13/80・反復51/80へ改善。ただしraw Unicode2/400で最終採用不合格 |
| [base_10b_preparation_review.json](phase6/base_10b_preparation_review.json)、[14tests](phase6/base_10b_tests.xml) | 専用10B準備完了、26保存checksと実CUDA全state再開一致。16更新/524,288検証tokensは科学学習と別。準備時の科学学習は0tokens |
| [base_10b_training_review.json](phase6/base_10b_training_review.json)、[終了記録](phase6/base_10b_training_completion.json) | 科学学習総10,000,007,168 tokens完了、終端state/全metrics等19checks成功。実process終了、GPU7,657.678秒。当時は品質評価未実施で、後続comparison reviewに評価結果を保存 |
| [base_10b_comparison_review.json](phase6/base_10b_comparison_review.json)、[内容確認](phase6/base_10b_content_review.json)、[終了確認](phase6/base_10b_comparison_completion.json) | 同条件全文dev/400完了、CPU23checks成功。BPB0.954018 / EOS0・反復53 / Unicode0、元増量gate合格、実用品質未達。GPU786.881秒 |
| [documentation_refresh_20261004.json](phase6/documentation_refresh_20261004.json) | 現行文書と計画の整理、元13文書の履歴保存、内部リンク・凍結条件・WSL同期の確認。GPU jobは開始しない |

科学10Bの専用品質比較入口・同条件dev/400・全固定80と自然停止9件の内容確認も完了。[品質結果](../docs/42_base_10b_quality_evaluation.md)。学習完了CPU reviewerは実際の終端stateと全科学metricsへ適用し、19項目成功。起動時のlaunchとrunning reviewは進捗履歴として保持する。[学習結果と速度](../docs/41_base_10b_training.md)、[status](../docs/autonomous_status.md)、[後続の同条件評価計画](../docs/39_learning_scale_and_generation_plan.md)。今回は報告・local commitで停止する。Base/Chat品質、独立人手blind/test、新重みの量子化品質は未達・未検証。

## 過去の記録の読み方

以下は各段階完了時の証拠で、当時の停止境界や未開始の記述を現在の実行指示にしない。旧原文は[保存履歴](../docs/autonomous_history_20261004.md)にも保持する。完了reportやsnapshotは上書きしない。

`phase0/`にiMacの環境・準備検証・完了監査を記録する。`p0-<name>-<UTC>-<random>/`は学習を実行しない準備runのsnapshotで、`experiments.jsonl`に追記する。大型/機械依存のrun snapshotはGit管理外。

準備runは`kind=preparation,status=prepared,tokens_seen=0`。モデルconfigと学習済みTokenizer artifactを区別し、Phase 2前のTokenizer/data入力hashは`null`で未作成を示す。学習を実施した結果として扱わない。

snapshotにはcode/docs/config/eval/lockfile、各hash、環境、Git commitとdirty状態を含める。未コミット変更もsource snapshotから復元できる。既存runの変更はchecksum検証で検出する。Phase 4の学習runは別の`schemas/training_run.schema.json`を使用する。準備schemaや過去snapshotは書き換えない。

`phase1/`には実データpilotの統計、20件の内容レビュー、全件復元・split検証、再生成比較と完了監査を保存する。本文・原file・Parquet・大きなsplit membershipは`data/phase1/`のGit管理外領域に置き、reportのchecksumと[再生成手順](../data/README.md)から照合する。Phase 0の過去環境・監査を上書きせず、現在の開発検証には`reports/local/`等を使用する。

`phase2/`にはTokenizer契約・全coverage候補・全corpus計数、`phase3/`には両実モデルの契約、native export parity、量子化実型・容量、完了監査とテスト結果を保存する。これらPhase 2〜3のモデル重みはランダム初期化。Phase 4当時はGPU検証学習までで、Base/Chat本学習は未実施だった。現在の実績は上表を参照。大型Tokenizer/weights/native runtimeは`artifacts/`のGit管理外で、reportのhashを照合する。詳細は[Phase 2](../docs/18_phase2_completion.md)、[Phase 3](../docs/19_phase3_completion.md)。

## Phase 4の実機証拠

`phase4/environment.json`、`handoff_report.json`、`resume_report.json`、`throughput_report.json`、`base_evaluation_contract_report.json`、`resource_budget.md`をGit保存した。handoffは全7 gate成功、全64 tests / skip 0、両モデルの全state resume一致。eager最大batchはT8K 57 / T4K 64、compiled容量は未探索、Flash-onlyの失敗は残す。

rawログ・source snapshot・checkpoint・生成出力はLinux実行コピーの`reports/phase4/gates-20261003/`に保持する。集約reportのraw path/SHAを照合し、Git cloneだけでraw checkpointまで復元できるとは扱わない。Phase 4終了時にはPhase 5は未開始だった。[完了記録](../docs/21_phase4_completion.md)

## Phase 5の実学習・比較証拠

`phase5/`にはoverfit/smoke、4本の100Mのtraining/evaluation audit、凍結plan、共通bytesと固定生成の集約、候補config、採用・棄却理由、独立監査、実測予算と停止確認を保存した。全68 tests / skip 0、4構成のCUDA厳密resume、overfit全5 gate、全比較と補助評価が成功。候補はT4K / NoQK-Norm / LR 0.002。停止・反復・sampling Unicodeの品質目標は未達で、Phase 5当時はNoNormのHF/GGUF adapterが未実装だった。現在は④でCPU精度profileによる学習済み変換を検証済み（下記④⑤）。[完了記録](../docs/23_phase5_completion.md)

raw evidenceはLinux checkoutの`reports/phase5/run-20261003-docoverfit/`へ保持する。GPU job/launcherは終了済み。自動生成の`candidate_selection.md`と`completion_audit.json`をそのまま保存し、詳細な採否レビューを`candidate_selection_review.md`へ分けた。Phase 5終了当時はPhase 6本学習未開始だった。

将来のrunを再実行する場合は別directoryへ出力する。既存run/reportやPhase 0〜3のhashを更新で上書きしない。現在の文書検証等は`reports/local/`へ保存する。

## Phase 6①②の完了証拠と文書更新

以下の①②reportは[事前の目的・条件](../docs/25_phase6_preparation.md)に対応する。train 756,087,912 unique stream tokensの拡張corpusとWSD stable/独立decayを準備した。[完了記録](../docs/26_phase6_preparation_completion.md)。③の容量/速度・長期Base/Chat・品質達成の証拠ではない。

| report | 確認したこと |
|---|---|
| [sources.json](phase6/sources.json)、[acquisition.json](phase6/acquisition.json) | 固定revisionの条件資料・取得上限、8 filesの上流SHAとraw 2,152,539,810 bytes |
| [corpus_manifest.json](phase6/corpus_manifest.json)、[corpus_audit.json](phase6/corpus_audit.json) | 全1,803,712 raw、signature/cluster・split、全retained 1,783,193文書の本文/token/index/文字往復。manifestは作成時ラベルを保持し、監査結果はauditを正とする |
| [quality_review.json](phase6/quality_review.json) | 24 train文書の先頭最大420文字を確認。品質リスク・確認範囲を記録 |
| [wsd_resume_report.json](phase6/wsd_resume_report.json)、[evaluation_isolation.json](phase6/evaluation_isolation.json) | CUDA/BF16/math/batch 8、stable 200 vs 100+100・decay 100 vs 50+50の全state完全一致、元枝不変性とdev評価状態保全。73 GPU checks |
| [tests.xml](phase6/tests.xml)、[completion_audit.json](phase6/completion_audit.json) | 全74 tests / skip・failure・error 0、独立監査55 checks、12 checkpoints・336 snapshot files、過去report 57 filesとlock不変 |
| [preparation_failures.json](phase6/preparation_failures.json) | 初回scheme失敗・schema不足と修復。条件を緩めず失敗履歴を保持 |
| [hub_artifacts_verification.json](phase6/hub_artifacts_verification.json)、[process_completion.json](phase6/process_completion.json) | 公開25 payload照合/restored 0、launcher終了と停止確認 |
| [documentation_audit.json](phase6/documentation_audit.json)、[final_package_audit.json](phase6/final_package_audit.json) | ①②完了時点の43 Markdown / 393内部リンク、Windows/WSL 91 source filesの同期、包装監査13 checks |
| [documentation_update_20261003.json](phase6/documentation_update_20261003.json) | ①②後の文書・残りの計画更新を別監査した当時の記録。旧report/実装/config/lock/eval不変、文書リンク・CLI・WSL同期・停止境界を確認 |

大型dataは`~/jmicro-data/phase6/{raw,expanded-v2}/`、CUDA checkpoints/log/source snapshotsはLinux checkoutの`reports/phase6/preparation-20261003/cuda/`。①〜⑤のjobは終了済みで、当時は本学習前で停止した。Git clone/Hub bundleだけで拡張data/checkpointsが揃うとは扱わない。既存snapshotと完了reportは当時の証拠として保持し、現在の文書を過去snapshotへ書き戻さない。今後の実行順は[本学習以降の計画](../docs/27_phase6_remaining_plan.md)。

## Phase 6③の高速化・容量・再開証拠

③は`a7d26e1`でcommit済み。[完了記録](../docs/29_phase6_performance_completion.md)。Flash＋compile reduce-overhead / batch 32=694,521 tokens/s、最大安定111/112 OOM。以下は①②のreportとは別の実測で、品質達成・長期Baseの証拠ではない。

| report | 確認したこと |
|---|---|
| [batch_performance_report.json](phase6/batch_performance_report.json)、[batch_choice.md](phase6/batch_choice.md)、[performance_summary.json](phase6/performance_summary.json) | 最速・容量・保存/評価込みVRAM・速度比・unique metricsのtoken台帳 |
| [performance_completion_audit.json](phase6/performance_completion_audit.json)、[performance_cold_resume_report.json](phase6/performance_cold_resume_report.json)、[performance_tests.xml](phase6/performance_tests.xml) | 独立1286 checks、空cache再開26 checks、79 tests / skip・failure・error 0 |
| [performance_failures.json](phase6/performance_failures.json)、[performance_audit_initial_failure.json](phase6/performance_audit_initial_failure.json) | 初回cache/backend・観測不足・監査のoutput数誤判定を保持 |
| [performance_documentation_audit.json](phase6/performance_documentation_audit.json) | ③完了時の文書/CLI/WSL同期・旧73 reports/lock保持と実装/report binding |
| [plan_update_20261003.json](phase6/plan_update_20261003.json) | 今回の最新計画・完了チェック・算術予算・文書同期と旧成果/コード保持の監査 |

raw logs/requests/compiled code/source snapshots/checkpointsはLinux `reports/phase6/performance-20261003-v3/`と`performance-cold-resume-20261003/`に保持する。④生成/変換と⑤長期設定凍結は完了した。当時の次段階は500M評価で、現在は5B/仕上げ比較まで完了した。

## Phase 6④⑤の検証・設定凍結と停止

④⑤は`93c7d1d`へcommit済み。[実施記録](../docs/30_phase6_readiness_execution.md)。

| report / config | 確認したこと |
|---|---|
| [generation_diagnostics.json](phase6/generation_diagnostics.json)、[expanded_dev_baseline.json](phase6/expanded_dev_baseline.json) | 固定dev400生成と拡張dev89,416文書の全文採点、BPB/時間/未達品質、本文一度採点・EOS分離 |
| [nonorm_export_parity_report.json](phase6/nonorm_export_parity_report.json)、[readiness_export_audit.json](phase6/readiness_export_audit.json) | CPU精度profileで学習済み短/1024・full/cacheの全12比較、13契約、実CLI/全119 GGUF重みの独立149 checks |
| [nonorm_precision_repair_report.json](phase6/nonorm_precision_repair_report.json)、[stock失敗](phase6/nonorm_export_stock_fp32_failure.json) | 精度修復の採否、途中/stock/CPU8設定/CUDA参照の失敗保持。GPU学習coreと重みは不変 |
| [readiness_stability_report.json](phase6/readiness_stability_report.json)、[readiness_gpu_audit.json](phase6/readiness_gpu_audit.json) | LR3候補×2,000 stable＋100独立decay、LR0.002採用、厳密50/cold25完全一致、独立106 checks |
| [readiness_precision_tests.xml](phase6/readiness_precision_tests.xml)、[readiness_gate_audit.json](phase6/readiness_gate_audit.json) | 全90 tests / skip・failure・error 0、指定範囲の6要求と停止境界の37 checks。Base品質合格ではない |
| [base_frozen.json](../configs/phase6/base_frozen.json)、[base_launch_plan.json](phase6/base_launch_plan.json) | version2のmodel/data/source/runtime、batch32/LR0.002/WSD global305,176更新、独立decay5%、保存/容量/実起動・再開CLI |
| [旧version1](../configs/phase6/base_frozen_blocked_v1.json)、[base_launch_guard_report.json](phase6/base_launch_guard_report.json) | 修復前の起動不可設定と実起動拒否をbyte保持 |
| [documentation_refresh_readiness_20261003.json](phase6/documentation_refresh_readiness_20261003.json) | ④⑤完了後の25文書・残りの計画更新。凍結条件/CLI/算術予算、内部リンク、WSL同期、旧実装/設定/証拠の保持と停止を検証 |

raw logs/checkpoints/weights/logits/snapshotsはLinux `reports/phase6/readiness-20261003/`、正式exportは同runの`export-stable-f32/`。専用CPU runtimeは`artifacts/runtime-stable-f32-v2`。Git/Hubだけでは復元できず、Windowsコードとともに引き継ぐ。当時の`launch_enabled=true`は技術gate成立を示し、当時は本学習前で停止した。現行10Bは専用configを使う。


## 拡張trainの500M学習・評価

2026-10-03: 拡張trainの500M stable＋独立763更新decayと全文dev/400生成評価を完了。同一dev BPB 1.244126→1.022491、抑制greedy EOS 0/80→0/80、反復48/80→66/80。全99 tests成功。人手blind採点・test・Chat・新重みの量子化は未実施。1B前で停止。

- [学習/評価/paired CI/全checkpoint監査](phase6/base_500m_review.json)、[全80 greedy生成例](phase6/base_500m_review.md)。
- [起動前照合](phase6/base_500m_preflight.json)、[全99 tests](phase6/base_500m_tests.json)。
- [固定20件の内容点検](phase6/base_500m_content_review.json)はCodexによる定性的な確認で、blind人手採点ではない。予測BPB改善と生成退行を分け、1B前で停止する。

raw evidenceと18 checkpointsはLinux `reports/phase6/base-20261003/`へ保持する。今回の新しい重みのexport/量子化は未実施。

## 500M後の反復・EOS・データ構成の調査

- [当時のローカル10Bデータ整備計画](../docs/32_local_10b_corpus.md)。WSL保存、全件重複/heldout保護/token監査を行い学習前で停止する。全105tests成功。この計画作成当時は実構築・監査未完了。現在は12.23Bを利用確認済み、独立全corpus監査未完了。
- [LSH性能のprefix probe](phase6/corpus_10b_cost_probe.json)、[実1M・全32bandsでの並列比較](phase6/corpus_10b_parallel_probe.json)。候補coverageと全代表が一致、30.004→9.135秒（3.285倍）。取り込みcheckpointを保持したexecution v3へ移行した。全10Bの監査完了ではない。
- [実ローダー利用確認の手順](../docs/32_local_10b_corpus.md#学習用ローダーでの最終利用確認)。Shard/BlockSamplerでtrain batch/mask/bytes/replayを検証する。小fixtureは当時成功。現在の実loader確認と独立監査の範囲は上表を参照。
- [以前の2B/5B計画](../docs/autonomous_history_20261004.md)は10Bの実行依頼へ更新した。
- [保留したdecoder比較の計画](phase6/repetition_decoder_plan.json)、[以前の作業順序](../docs/autonomous_history_20261004.md)、[当時の計画の16項目照合](phase6/repetition_decoder_plan_audit.json)。同じ10Mパラメータの重みで640outputs/GPU15分上限を比較する案。監査は当時の計画を確認した記録で、現在の優先作業や実行結果ではない。
- [事前計画](phase6/repetition_diagnosis_plan.json)、[判断と比較](phase6/repetition_diagnosis_review.md)、[数値/binding/20項目監査](phase6/repetition_diagnosis_review.json)、[225既存files保持](phase6/repetition_preservation.json)、[終了・同期監査](phase6/repetition_completion_audit.json)。
- EOS教師欠落は確認されず、文書末尾予測は改善。反復は拡張131Mから多く、decayで70/80→66/80。全文の文書長と固定sample反復に大幅増加はない。短prefix/greedyと学習分布の違いを次の比較候補とし、因果未分離・精度差を残す。
- 全102 tests成功。GPU推論249.75秒、学習更新0、1B未開始。Linux raw evidenceは`reports/phase6/repetition-diagnosis-20261003/`。次回案を開始せずcommit後停止する。
````
