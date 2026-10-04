# JMicro-10M development and training

Read `docs/autonomous_status.md`, `docs/15_project_roadmap.md`, and `docs/windows_handoff.md` before continuing. The status records actual results; `docs/39_learning_scale_and_generation_plan.md` is the current execution plan. Historical authorizations and progress notes are in `docs/autonomous_history_20261004.md` and do not define the current task.

## Current state and scope

- Model: 10,001,152 parameters; prepared train data: 12,225,819,077 tokens. Main Web training reached5B, and independent Web/short20 finishing branches each reached5.1B. Base/Chat quality targets remain unmet.
- Direct10B preparation is complete at code commit `4c3fbaf`: frozen `configs/phase6/base_10b.json`, schema, dedicated runner/launcher,14 CPU tests and actualCUDA16-update/524288-token exact stable/decay save-resume verification. See `docs/40_base_10b_preparation.md` and `reports/phase6/base_10b_preparation_review.json`.
- Scientific10B training completed on 2026-10-04 at11:43:52Z: total10,000,007,168tokens/update305176; additional scientific tokens5,249,990,656 from saved4.75B stable parent. Stable9.5B plus final decay and all saved states/metrics passed19 CPU review checks. Linux427/Windows30148 exited. Verification tokens are separate. See `docs/41_base_10b_training.md` and `reports/phase6/base_10b_training_review.json`.
- Current stop boundary (2026-10-04): requested step3 final10B quality evaluation is complete: same full dev89,416/fixed400, all80 content and9 natural-stop review,23 CPU evidence checks. BPB0.954018 / fixed EOS0 / repetition53 / all400 raw Unicode0; original growth gate passes, Base/Chat quality remains unmet. Finish report/local commit, then stop. No further training, EOS finishing, decoder experiments, test selection, Chat,20B/50B or publication. See `docs/42_base_10b_quality_evaluation.md`.
- Training recovery entry: `bash scripts/run_base_10b.sh --train`; the current run is complete and must not be relaunched for more learning. Shell default and `--verify-only` perform preparation verification only; completed verification is reused. Do not restart completed old launchers.

## Project rules

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
