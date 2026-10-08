# JMicro-10M development and training

Read `docs/autonomous_status.md`, `docs/15_project_roadmap.md`, and `docs/windows_handoff.md` before continuing. Status records actual evidence; the roadmap and `docs/124_base_recovery_plan.md` define the current plan. Historical progress is in dated reports and archives, not in this instruction file.

## Current scope — 2026-10-09 JST

- The user requested stopping at a sensible boundary. The cumulative2B teacher-normalized decay experiment and all80 individual reviews finished; the condition was rejected and closed. Base remains unfinished and unadopted.
- The subsequent request authorizes updating documentation and plans only. It does not resume research execution, data preparation, diagnostics or GPU training. Await explicit user resumption for those actions.
- Preserve the future Base-only boundary: finish an evidence-qualified Base, notify the user and stop. Do not start Chat/Dialogue/SFT, quantization or deployment unless the user resumes those stages.
- Independent trained seed43, fullDEV, final continuation suites, protectedTEST and adoption remain pending. CPU seed preparation is not learning or quality evidence.
- Keep the original10B local WebUI available. Recorded process identities are observations, not proof of current liveness. Do not relaunch completed pilots or2B runs.
- User-authorized archival publication (2026-10-09): three major model lineages, numerical training state excluding samplers, Tokenizer, implementation/configs/docs and stored evaluation metadata were uploaded to `japanese-data-analyze/JMicro-10M-research-archive` as public with manual gating. Datasets are excluded. See `docs/126_model_archive.md`. This does not resume training/research or the previously paused documentation/GitHub-push task, and does not authorize unrelated publication.

## Fixed model-size requirement — user clarification, 2026-10-08 JST

Maintaining the 10M size is a core project requirement and its intended advantage. Keep total trainable parameters within the existing approximately10M budget (9.5M–10.1M; current10,001,152). Do not switch to a larger model to meet quality targets or launch a larger-model comparison without a separate explicit user request. Prioritize data quality, training objectives, optimization and architecture allocation within that same budget. Preserve quality criteria and the Japanese Base goal; do not silently narrow the target domain or lower thresholds. This clarification does not resume paused training/research execution.

## Project rules

The user authorizes autonomous implementation, repair, local GPU work and required WSL preparation within the active requested scope. Continue routine authorized decisions without renewed permission. Authorization cannot override tool permissions or the current pause.

- Target WSL package3.x, WSL2 Linux and RTX4090. Use Python3.12.7 and uv; dependency changes use `uv add`. Preserve Phase0–3 reports and all historical experimental evidence.
- Run all Python through `uv run --frozen ...`, including probes, tests, automation and one-offs. Standard WSL extras are `--extra hub --extra data --extra ml --extra export`. Install Python with `uv python install 3.12.7`; restore dependencies with `uv sync --frozen` and required extras. Never use system python/python3/py directly or pip. Python children may reuse `sys.executable` when the parent was launched through uv. Record inaccessible pinned dependencies as blockers.
- Recover pinned public pilot/Tokenizer and verify hashes when restoration is necessary. Do not repeat Tokenizer training, Phase3 export, environment benchmarks or closed comparisons without new evidence.
- Preserve the native10,001,152-parameter model as the current reference. Existing `src/jmicro/model.py` SHA256 is `298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83`. Architecture changes require a separate explicit proposal and comparison; do not silently replace frozen sources.
- Follow environment→shards/trainer/evaluation→save/resume→stable batch, then Base→Chat→quantization. Implement missing commands before execution. Research and20B/50B require defined comparisons, measured budgets, advancement and stop conditions.
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
