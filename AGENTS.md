# JMicro-10M development and training

Read docs/autonomous_status.md, docs/15_project_roadmap.md and docs/windows_handoff.md before continuing. Actual latest Base evidence is result144; next plan is docs/145_post_rejection_next_plan.md; document coverage and delivery are in docs/146_documentation_followup.md and docs/document_catalog.md. Plans are not execution authorization.

## Current scope — 2026-10-14 JST: documentation and planning only

The user cleared the blocked, unachieved "6まで進めてください" goal and requested updating all documentation and planning the next work. Inventory every Markdown/RST including provenance copies, update all living explanations, preserve frozen/dated evidence and original bytes, verify local links/Windows-WSL/Git delivery, and commit locally. No research implementation, diagnostics, data/TEST preparation, inference/evaluation, GPU training, old-job restart, dependency/environment work, push/publication or quantization is resumed. Do not repeat the superseded research-resumption question during this documentation goal.

Latest document-length-weighting Base pilot144 completed exact100M/17698 updates, all80 individually reasoned DEV outputs, common-byte/Japanese evaluations, complete-state/update/weight/source/sampler/budget checks and rejected the recipe. Model quality and the former six-stage goal remain unachieved. Main extension, genuinely fresh trainedseed43, fullDEV/400+40, sealedTEST and adoption are unexecuted, passed=false, quality-unconfirmed. Source result1901564/receipt fc1a3fc were verified; stored records describe those revisions, not current living-document hashes.

Preserve the separate original Base TEST20-prompt CPU parsing exposure and prior Chat TEST20-row preparation exposure. Neither was used for learning or GPU TEST scoring, but cannot be called CPU-unopened. Base TEST shards were not opened here. Future qualified final verification requires isolated DEV/TEST readers and fresh sealed cases; do not prepare/parse replacements during documentation or with no eligible candidate.

Original10B WebUI was last verified2026-10-14T07:30:16Z as PID338403/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start60473641, correct parent/Tokenizer/10M/idle. This is recorded evidence, not current liveness. Preserve native full weights/samplers/metrics and all older lineages in WSL; datasets/weights/samplers are not copied into Git. Never relaunch rejected or completed jobs.

Any future Base resumption follows plan145: first repair evaluation reading boundaries, define one evidence-grounded independent comparison and its approved scope/budget. If explicitly authorizing multiple bounded comparisons, continue routine authorized work without renewed approval; otherwise obey the frozen failure boundary. Preserve10M, original quality/domain, independent fresh learning/fullDEV/finalTEST. Finish a qualified Base, notify and stop; Chat/SFT/quantization/publication need separate resumption.

Original operative documents and all current source/provenance paths are preserved in reports/investigation/documentation-followup-20261014/baseline.json. Dated reports and scientific receipts must not be rewritten to make them describe later document changes.

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

<!-- Original heading aliases retained for historical incoming links. -->
<a id="current-scope--2026-10-14-jst-rejected-base-comparison-closeout"></a>
<a id="prior-resumption-and-historical-scope"></a>
