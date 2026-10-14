# Phase 4 measured resource budget

Measurements are specific to RTX 4090 / WSL / PyTorch 2.14.1 / CUDA 13.0, context 1024, FP32 parameters + BF16 autocast.

Maximum stable batch refers to eager/default SDPA with a 94% CUDA allocator ceiling and three 200-update confirmations, including evaluation/save. It is an operational bound, not indefinite stability or a global maximum across every compile/backend configuration.

| Model | Stable micro batch | Effective batch tokens | Median tokens/s | Confirmation range |
|---|---:|---:|---:|---|
| t8k | 57 | 58368 | 225169 | [225145.80247779458, 225371.79276034213] |
| t4k | 64 | 65536 | 218411 | [218391.2704597771, 218488.6181529074] |

The fastest measured batch/configuration is separately recorded in throughput_report.json; compile cold start is excluded from steady throughput. Capacity is established for the eager baseline; compiled capacity was not searched.

The explicit Flash-only backend rejected the model's non-null attention mask. This unsupported candidate is retained as a failed raw probe; default SDPA, math-only and compile/default have successful measurements. It is not a successful Flash benchmark. A mask-free causal training path would be a separate future optimization and is not implemented here.

| Tokens | T8K compute hours | T4K compute hours |
|---:|---:|---:|
| 100,000,000 | 0.12 | 0.13 |
| 1,000,000,000 | 1.23 | 1.27 |
| 10,000,000,000 | 12.34 | 12.72 |
| 20,000,000,000 | 24.67 | 25.44 |
| 50,000,000,000 | 61.68 | 63.59 |

Capacity probes measured 9.97 s total subset evaluation time. Checkpoint save range: 0.169–0.727 s. Full dev evaluation elapsed times are recorded in handoff_report.json. Add each planned full evaluation, checkpoint, comparison and cold compile to the compute-only estimates; no claim that the table is total project time.

## Measured storage bytes

```json
{
  "raw": 0,
  "processed_pilot": 106523144,
  "shards_both": 45069218,
  "phase4_reports_checkpoints_snapshots": 1469791503,
  "uv_download_cache": 19272829896,
  "virtual_environment": 6072792110,
  "free_linux_bytes": 980811743232
}
```

These are apparent file sizes; shared uv hardlinks are not deduplicated. Pilot unique train body bytes are 32,774,150 for both tokenizers; streams are 6,884,183 / 8,398,329 tokens including BOS/EOS. Fixed-length sampling omits the final incomplete train block; sampler blocks/cursor and actually consumed tokens/bytes are checkpointed. Longer budgets require explicitly reported repetition or staged corpus expansion. Master corpus is not acquired. uint16 shard projection is 2 bytes/token per tokenizer, before indexes/raw/temporary files/checkpoints.

Stop boundary: Phase 4 complete. Do not launch Phase 5 until the user resumes.
