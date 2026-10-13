# 2B teacher-normalized weight-decay comparison: results and user pause

2026-10-08 JST. The user requested a stop at a sensible boundary and a report of current learning results. The cumulative 2B experiment, native evaluation and individual review of all 80 continuations are complete. **The condition is rejected; Base is unfinished and unadopted. Work is paused until explicit user resumption.** No further training, research, independent-seed run, Chat/SFT or quantization is authorized during this pause.

## What was compared

The existing accepted 2B-token TRAIN pool and the original native 10,001,152-parameter model were retained. Web/textbook/story supervised-token quotas are 75%/20%/5%. This is a weight-decay experiment, not a dataset expansion. Both scientific conditions consumed exactly 2,000,000,000 supervised tokens with identical stream, sampler, scheduler and final counters. The original 2B control and its original 80 content ratings were reused without rerating.

The candidate scales decoupled weight decay by the supervised-token count of each update, keeping the native Adam update and learning-rate schedule. It continued the same 94,160,195-token pilot with its actual optimizer, scheduler, RNG and sampler, without reset or reheating. New continuation learning was 1,905,839,805 supervised tokens. Actual CUDA continuous-versus-resumed verification passed all 15 checks; its 8 updates/71,464 verification teachers were accounted separately and its weights discarded.

## Evaluation results

BPB uses the same 256 DEV documents, 472,055 original bytes and 122,343 body tokens; lower is better. Content and generation counts below are out of 80. Content ratings are Codex nonblind ratings, not independent human blind evidence.

| Metric | Original native 2B | Teacher-normalized decay 2B |
|---|---:|---:|
| BPB ↓ | 1.106386 | 1.090316 |
| Grammar score 2 ↑ | 23 | 22 |
| Prompt relevance score 2 ↑ | 30 | 16 |
| Semantic coherence score 2 ↑ | 3 | 3 |
| Appropriate completion ↑ | 7 | 5 |
| Actual EOS stop ↑ | 20 | 23 |
| Automatic repetition ↓ | 27 | 27 |
| Invalid UTF-8 ↓ | 0 | 1 |
| Role leakage / empty ↓ | 0 / 0 | 0 / 0 |
| Japanese semantics accuracy ↑ | 56.771% | 56.250% |
| JBLiMP accuracy ↑ | 78.852% | 80.060% |
| JCQA accuracy ↑ | 38.293% | 37.131% |

BPB improved by approximately 1.45%. The byte-weighted paired document difference is −0.0160695, with bootstrap 95% CI [−0.0209552, −0.0118732]. This predictive-loss improvement did not become better coherent continuations. Coherence count difference is zero, with paired fraction CI [−0.0375, 0.0375]. EOS increased by three outputs, repetition stayed unchanged, and appropriate completions decreased. The invalid UTF-8 output (base-070) is retained as a failure; no tail trimming was used to pass evaluation.

All six original absolute screens failed: grammar ≥56, coherence ≥27, appropriate completion ≥27, EOS ≥37, repetition ≤18, and no empty/role/Unicode failures. Comparisons against the separate strong staged and cached-CE references and historical Web-retention requirements also did not all pass. The candidate is ineligible for final Base validation. The fixed condition is closed; no automatic coefficient/reference/LR/seed/budget rescue or 10B extension follows.

For perspective, the earlier staged run at approximately 10.6B supervised tokens had grammar 65, coherence 23, appropriate completion 26, EOS 76 and repetition 2 out of 80, but still missed the coherence/completion adoption thresholds. Its training history differs, so it is not a matched control for this experiment. The latest candidate does not replace it or the original WebUI checkpoint. Across the project, lowering BPB alone has not reliably solved semantic repetition and coherence.

## Saved evidence and runtime closeout

- [Completion and decision](../reports/phase6/base_teacher_decay_2b_completion.json), SHA256 `f2e9878652d76f13e59bedc12e52ca7db9eb784b19a49a3355f2a634f334291e`.
- [All 80 individual raw-bound reviews](../reports/phase6/base_teacher_decay_2b_candidate_notes.json), SHA256 `c066394e33f58a411c022eb5c2722a0e759324d5400850f0e5089d9a156757b2`.
- [Final science result](../reports/phase6/base-teacher-decay-2b-20261008/result.json), [training record](../reports/phase6/base-teacher-decay-2b-20261008/train-result.json), [evaluation result](../reports/phase6/base-teacher-decay-2b-20261008/evaluation/candidate/evaluation/result.json), and [original generated outputs](../reports/phase6/base-teacher-decay-2b-20261008/evaluation/candidate/evaluation/generation.json).
- [Terminal process, final counters and pause record](../reports/phase6/base_teacher_decay_2b_active_job.json).

The scientific process PID 118881 / boot `4052bfc5-3850-44e4-9123-d34a9e19f36e` / start_ticks `8215874` exited. Windows worker 38176 completed with exit code 0. Continuation GPU time was 26,060.094 seconds (7h14m20s), below its 37,536-second cap. Including the previous pilot, total GPU time was 27,475.228 seconds (7h38m). The GPU ledger is closed.

Final counters are update 212095 and exactly 2,000,000,000 supervised tokens. Terminal job.json preserves its last periodic heartbeat at update 212080 / 1,999,868,016 tokens; the final result, training record and checkpoint contain the authoritative completed counters. This is not unfinished learning.

The resumable final checkpoint remains on WSL at `/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-teacher-decay-2b-20261008/latest.pt`, SHA256 `03ebf266853541759054ee7100903fa175815adfcfc8e62e559ccdb1ce657442`. Weights and large per-update metrics are retained there, not added to Git. Small raw evaluation artifacts and records are copied to the Windows repository without modifying their bytes.

The original local WebUI was restored and verified idle at <http://127.0.0.1:7860>. Its process is PID 120460 / same boot / start_ticks `10822295`; its model is the original 10,000,007,168-token checkpoint SHA256 `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`, not this rejected candidate. Leave the local server available.

## What remains unresolved

Semantic coherence, repetition, appropriate completion and reliable stopping remain below Base requirements. This one-seed, repeatedly inspected DEV experiment does not establish generalization or the cause of those failures. Independent trained seed 43, full DEV, the final continuation suites, protected TEST and adoption have not been completed. Seed preparation is CPU-only and supplies no quality evidence. Base, the wider five-item objective and later stages must not be marked complete.

On explicit user resumption, first read the latest pause/status records and review the closed conditions before proposing a bounded next comparison. Do not relaunch this completed job, repeat its review or begin Chat/quantization automatically.
