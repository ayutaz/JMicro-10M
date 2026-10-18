# JMicro-10M development and training

## Current scope 2026-10-18

The active user goal is to update ALL documentation, consolidate overlapping explanations, delete unnecessary documents, and push the verified changes. GitHub and all four published models are already public/ungated. Original code is Apache-2.0; model weights, Tokenizer artifacts, external datasets and third-party code retain their separate conditions.

Latest diagnostic SFT: 483 updates/250003 teachers; TRAIN64 exact, unseen values30/32, structure15/32 (two fields0/16), own final9/16; public100 task3/100. All1973 reviewed. Five-step execution COMPLETE; candidate REJECTED. Formal Base/Chat adoption, independent whole pipeline, required fullDEV/all440/new sealedTEST remain unachieved. This documentation goal does not restart any research/training/evaluation or switch the UI model.

Read [current state](docs/autonomous_status.md), [remaining work](docs/10_next_steps.md), [latest fixed results](docs/165_chat_two_attribute_diagnosis_results.md), [publication](docs/166_public_models_and_oss.md), and [documentation catalog](docs/document_catalog.md). Preserve frozen scientific sources/configs/results/weights, dataset boundaries, negative decisions and all historical costs. Dated active/live/next statements are historical, not current authorization. Do not reopen a closed job or use a small memorization result as Base/Chat qualification.

The full preceding instructions and progress chronology are preserved at [the pre-refresh Git revision](https://github.com/ayutaz/japanese-tiny-llm-10m/blob/ed91c002cdfe52c879e275241c58436bfef3e394/AGENTS.md). Documentation-maintenance summaries142/146/148 are consolidated into167 and removed from the current tree; original scientific records and their source snapshots remain intact.

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
- Use repository-local Git identity `yousan <ka1357amnbpdr@gmail.com>`. Commit appropriate milestones; push/publication requires explicit user authorization, which is present for this documentation goal. Windows is the authoritative Git workspace; mirror execution files to WSL with appropriate line endings and preserve frozen hashes.

For non-interactive runners return the requested JSON. `continue` means useful authorized work remains; `needs_user` means an external action is needed; `complete` requires actual evidence that the requested scope is achieved. Documentation completion does not mean Base or overall project completion.

The previous instruction text and progress history are preserved in `docs/agents_history_20261008.md`. Its old continuation instructions do not override this current scope.


<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="current-scope--2026-10-14-jst-rejected-base-comparison-closeout"></a>
<a id="current-scope--2026-10-15-jst-four-item-base-resumption"></a>
<a id="previous-documentation-only-scope"></a>
<a id="previous-documentation-only-scope--completed-2026-10-17-jst"></a>
<a id="prior-resumption-and-historical-scope"></a>
