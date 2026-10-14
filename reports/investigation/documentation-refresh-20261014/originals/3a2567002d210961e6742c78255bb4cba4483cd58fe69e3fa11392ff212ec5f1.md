# Phase 5 candidate selection

Selected: 100m-no-qknorm. No test used; Phase 6 not started.

| Run | dev BPB | common-window BPB | steady tokens/s | greedy EOS |
|---|---:|---:|---:|---:|
| 100m-no-qknorm | 1.221443 | 1.546589 | 121139 | 0.0% |
| 100m-t4k | 1.231823 | 1.591386 | 111693 | 0.0% |
| 100m-lr001 | 1.235002 | 1.618124 | 121046 | 0.0% |
| 100m-t8k | 1.258861 | 1.650058 | 117119 | 0.0% |

Selection prioritizes held-out common-byte BPB, then paired uncertainty, generation failures, speed and deployment constraints.
Unselected runs remain recorded as measured alternatives. No-QK-Norm requires a separate HF/GGUF adapter; no native export compatibility claim.
100M exposures repeat the small pilot; they do not establish scaling on 100M unique data. Auxiliary byte/time matches are approximate checkpoint budgets.
Existing Base/Chat quality goals remain unchanged. Phase 5 mechanical success is not Japanese conversational quality success.
Muon deferred because AdamW produced stable, improving candidates. For Phase 6, resolve scheduler extension and acquire the next required data, then validate before long training.
