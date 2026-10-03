#!/usr/bin/env bash
set -euo pipefail
export PATH="/home/aihub_ubuntu/.local/bin:$PATH"
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MKL_NUM_THREADS=1
export CUBLAS_WORKSPACE_CONFIG=:4096:8
cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m
printf '%s\n' "$$" > reports/phase6/base_2b_10b_data_pipeline.pid
exec >> reports/phase6/base_2b_10b_data_pipeline.log 2>&1
for operation in stable decay evaluate; do
  uv run --frozen --extra hub --extra data --extra ml --extra export \
    scripts/run_base.py --config configs/phase6/base_2b_10b_data.json \
    --target 2B --output reports/phase6/base-2b-10bdata-20261004 \
    --operation "$operation" --execute
done
