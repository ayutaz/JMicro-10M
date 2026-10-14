# JMicro-10M development and training

Read `docs/autonomous_status.md`, `docs/15_project_roadmap.md`, and `docs/windows_handoff.md` before continuing. Current evidence is in result141; document coverage and update evidence are in docs/142_documentation_refresh.md and docs/document_catalog.md. Plans124 and future proposals are not execution authorization.

## Current scope — 2026-10-14 JST: documentation only

The user requested "ドキュメントをすべて最新にして". Update all current documentation, inventory every document, preserve dated reports/frozen histories and scientific evidence, verify references and Windows/WSL copies, and commit the documentation delivery locally. This does not resume research, diagnostics, data preparation, evaluation, GPU training or old jobs. No automatic push, publication, quantization or deployment.

The previous three-step goal was completed with the LR3e-5 candidate rejected:3646 updates/1899557 Assistant teachers, all28 suites/6132 judgments/7 fixed NLL points, full-state/stream/ledger audits and all seven conditional decisions. Final S1 content20/18/19/15 of80 and own context5/5/5/1 of24 fail the original56/80 and15/24 gates; new improvement CI lower−1.25pp, repetition regressions and new own-history Unicode failure also remain. Result commit89275a8 and receipt commit09f338e were verified; this is scientific comparison and delivery completion, not model quality completion.

All qualified-only branches (Base retention, sampling, fresh trained seed43, human blind, fullDEV, sealed TEST, adoption) are unexecuted, passed=false and quality-unconfirmed. Base/Chat remain unfinished and unadopted. No extra LR/seed/budget/data/architecture or Base intervention is authorized. For any later Base-only resumption, finish an evidence-qualified Base, notify the user and stop; do not automatically move to Chat/SFT/quantization.

Preserve the original Chat TEST20-row preparation parsing exposure and its correction. It was not used for learning or GPU selection, but cannot be called untouched. Any future qualified final Chat confirmation requires fresh sealed cases. Original Base TEST was not parsed in that incident.

Keep original10B WebUI available. Latest stored scientific observation2026-10-13T16:54:20Z: PID309447, boot4052bfc5-3850-44e4-9123-d34a9e19f36e, start55170810, HTTP parent/Tokenizer/10M and idle state, kernel lock verified. Recorded identity is not current/future liveness proof. Do not start GPU or relaunch jobs during documentation work.

Frozen scientific reports, manifests and dated histories describe their captured revision. Verify their original Git revision/snapshots when living docs change; do not rewrite old completion/receipt records to make current document hashes appear historical. The original operative texts are preserved byte-for-byte in the documentation-refresh baseline.

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
