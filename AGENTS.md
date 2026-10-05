# JMicro-10M development and training

Read `docs/autonomous_status.md`, `docs/15_project_roadmap.md`, and `docs/windows_handoff.md` before continuing. Completed latest scope: plan61's preparation-failure branch, `docs/63_condition_preservation_preparation_results.md`. Original plan61 is preserved as its pre-execution contract. Status is actual state; proposals are not evidence or launch instructions. Historical progress is archived in dated experiment reports.

## Current state and scope

- Latest scope (2026-10-05 JST) completed: plan61 stages1–4 through its explicit preparation-failure branch. Saved failure diagnosis and same-source/quantity/length/EOS-matched each20,000,028-token pools completed; fixed40 each weak21/12, candidate12>10 readiness gate failed. All80 raw-bound specific reviews,101 evidencechecks,10 completionchecks and CPU4tests passed. New scientific/verification/GPU evaluation0; each100M/primary/full not launched. Report63/judgment/original10B UI proof saved. No500M/1B continuation,20B/50B/Chat,protected test,push/publication.
- Plan58 stages1–3 completed at local commit `afad164`: story pool59,963,449→200,000,192tokens; both arms additional1,000,013,824tokens; Japanese diagnostics and all160 individual content reviews;35 primary and20 completion evidence checks passed. JCQA35.031→38.561% improved, EOS34→25/coherence15→9/appropriate20→19(each80); candidate rejected under unchanged gates. Conditional full not launched. Source/length/EOS density changed; no amount-only causal claim. Scientific2,000,027,648/verification262,144 separate; Base/Chat quality remains unmet.
- Training PID239609 exited. Original final10B UI was restored and rechecked at PID359102/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks7216365, HTTP parent SHA410f975d…/training_tokens10,000,007,168/busy=false. Revalidate actual identity and HTTP for later work; recorded PID alone is not current process evidence.
- Current stop boundary: plan61 preparation-failure branch is complete; stop after verified local commit. Do not restart completed builders/plan58 jobs, adapt the selector to the inspected40, draw replacement samples or start new GPU jobs. A next proposal in report63 needs a resumed task; it is not authorization to launch.

## Project rules


Plan58 stages1–3 are delivered at local commit afad164, documentation refresh at d8a8f95. Plan61 preparation-failure branch is delivered in report63. Preserve all original adoption gates, frozen reports/source/raw/checkpoints and verification evidence. Stop; old progress and proposals do not authorize extra jobs.

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
