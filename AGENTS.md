# JMicro-10M development and training

更新: 2026-10-17 JST。ユーザーの現在の依頼は次のSFT計画作成。docs/149_chat_sft_next_plan.mdに、公開会話/短い質問応答の新しい教材recipeと従来教材対照、同10M/元10B親・各100万Assistant教師の最初の比較案を保存する。今回は計画・一次資料確認・文書保存のみで、新教材/評価本文の処理、重み読取り、GPU推論/学習は開始しない。設定は未凍結の提案。Baseの正式品質未達だけをChat SFTの禁止理由にしない。Base/Chatの正式採用は未達。

The existing first SFT Chat UI and all five practical conversations were delivered at 216a636f. This turn prepares the next SFT plan only. Reuse the completed Base pretraining, keep the original 10M/native sources and all prior negative results, and do not restart a closed condition. The first proposed comparison tests a broader public conversational data recipe with a matched fresh control, not another template-slot expansion or a rescue of the old low-LR run. Data availability, split isolation, numerical feasibility and run contracts remain to be fixed before execution.

The documentation-only goal was completed at 645b3d09. The latest user instruction authorizes Chat/SFT exploration and practical chat verification; it overrides the previous documentation-only scope below. Immediate work serves the existing first SFT model on CPU at a separate loopback port, with bounded actual conversation checks. Preserve original Base UI, all frozen training records and native sources; do not relaunch an old scientific condition. No paid cloud, external publication, model-size increase or TEST preparation is authorized. Do not ask again whether to resume chat verification.

[SFT計画149](docs/149_chat_sft_next_plan.md) / [Baseの残課題145](docs/145_post_rejection_next_plan.md) / [文書一覧](docs/README.md) / [全件カタログ](docs/document_catalog.md)。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。今回のチャット動作確認は、新しいユーザー指示に基づく。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## Previous documentation-only scope — completed 2026-10-17 JST

Inventory all Markdown/RST, including source snapshots and provenance copies. Update all living descriptions and plans, preserve dated/frozen scientific evidence and pre-edit bytes, verify links and Windows/WSL/Git delivery, then commit locally. The user cleared the unachieved four-item Base goal; do not mark it achieved or active. Documentation completion is separate from Base/Chat completion.

No research implementation, data/TEST preparation, runtime diagnostics, model inference/evaluation, new GPU training, old-job relaunch, dependency work, push/publication or external messages is authorized by this documentation request. The prior unlimited cumulative local GPU authorization remains valid for future authorized research; no repeat budget-cap question is required. Each future experiment still needs finite prospective teachers/timeouts, control, full-quality gates and stop conditions.

Latest scientific evidence is the rejected first RDrop25M run at commit cf113068. Its scientific process and Windows worker exited; original UI restoration is timestamped evidence, not current liveness. Full numerical histories, weights/Adam/RNG/sampler remain in WSL. Do not rehash/load model weights or scan corpora for documentation. Preserve every old closed condition and all carried GPU costs.

## Fixed model-size requirement — user clarification, 2026-10-08 JST

Maintaining the 10M size is a core project requirement and its intended advantage. Keep total trainable parameters within the existing approximately10M budget (9.5M–10.1M; current10,001,152). Do not switch to a larger model to meet quality targets or launch a larger-model comparison without a separate explicit user request. Prioritize data quality, training objectives, optimization and architecture allocation within that same budget. Preserve quality criteria and the Japanese Base goal; do not silently narrow the target domain or lower thresholds. This clarification does not resume paused training/research execution.

## Project rules

The user authorizes autonomous implementation, repair, local GPU work and required WSL preparation within the active requested scope. Continue routine authorized decisions without renewed permission. Authorization cannot override tool permissions or the current pause.

- Target WSL package3.x, WSL2 Linux and RTX4090. Use Python3.12.7 and uv; dependency changes use `uv add`. Preserve Phase0–3 reports and all historical experimental evidence.
- Run all Python through `uv run --frozen ...`, including probes, tests, automation and one-offs. Standard WSL extras are `--extra hub --extra data --extra ml --extra export`. Install Python with `uv python install 3.12.7`; restore dependencies with `uv sync --frozen` and required extras. Never use system python/python3/py directly or pip. Python children may reuse `sys.executable` when the parent was launched through uv. Record inaccessible pinned dependencies as blockers.
- Recover pinned public pilot/Tokenizer and verify hashes when restoration is necessary. Do not repeat Tokenizer training, Phase3 export, environment benchmarks or closed comparisons without new evidence.
- Preserve the native10,001,152-parameter model as the current reference. Existing `src/jmicro/model.py` SHA256 is `298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83`. Architecture changes require a separate explicit proposal and comparison; do not silently replace frozen sources.
- Follow environment→shards/trainer/evaluation→save/resume→stable batch, then Base→Chat→quantization. The bounded Chat-first diagnostics128/131/133/135/139 are closed and rejected; final results are136/138/141. New comparisons require explicit resumption and a separate frozen contract. Implement missing commands before execution. Research and20B/50B require defined comparisons, measured budgets, advancement and stop conditions.
- Use TRAIN for learning; keep DEV/TEST and fixed suites separate. Compare Tokenizers with common-byte BPB and labeled token/byte/GPU-time budgets. Chat loss supervises Assistant body plus EOT. CPU random-weight checks and display repairs are not GPU training or model quality evidence.
- Save optimizer/scheduler/RNG/sampler position and consumed counters at completed updates. Verify continuous versus resumed execution before long runs; use measured stable batches and finite CUDA/BF16 forward/backward.
- Persist long jobs, logs, checkpoint paths and actual PID/boot/start ticks. Inspect processes, run records and GPU locks before launch. Avoid duplicate jobs; resume valid interrupted checkpoints under the same frozen conditions.
- Reuse accepted data/build/loader evidence. Skip redundant whole-corpus scans, deduplication and old GPU evaluations. Do relevant checks for actual changes; retain incomplete independent corpus audits as incomplete.
- After meaningful work, run relevant checks, fix failures, update status with evidence/decisions/active jobs/next action and commit verified milestones. Never weaken acceptance gates. Preserve raw EOS/repetition/Unicode failures; constrained decoding is a separate policy.
- Stop for missing credentials, OS elevation/restart, inaccessible hardware or exhausted capacity; record the exact blocker and restart command. Do not repeat identical transient retries.
- Work within this project and documented WSL/data environments. External publication, messages to others and paid cloud jobs require separate authorization. Do not expose secrets.
- Use repository-local Git identity `yousan <ka1357amnbpdr@gmail.com>`. Commit appropriate milestones; do not automatically push or publish. Windows is the authoritative Git workspace; mirror execution files to WSL with appropriate line endings and preserve frozen hashes.

For non-interactive runners return the requested JSON. `continue` means useful authorized work remains; `needs_user` means an external action is needed; `complete` requires actual evidence that the requested scope is achieved. Documentation completion does not mean Base or overall project completion.

The previous instruction text and progress history are preserved in `docs/agents_history_20261008.md`. Its old continuation instructions do not override this current scope.

The complete pre-refresh AGENTS progress chronology is byte-preserved through reports/investigation/documentation-refresh-20261017/baseline.json. Older “latest/live/active” paragraphs describe their own timestamps and do not override this scope.

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="current-scope--2026-10-14-jst-rejected-base-comparison-closeout"></a>
<a id="current-scope--2026-10-15-jst-four-item-base-resumption"></a>
<a id="previous-documentation-only-scope"></a>
<a id="prior-resumption-and-historical-scope"></a>
