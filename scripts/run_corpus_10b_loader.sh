#!/usr/bin/env bash
set -euo pipefail
export PATH="/home/aihub_ubuntu/.local/bin:$PATH"
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MKL_NUM_THREADS=1
cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m
printf '%s\n' "$$" > reports/phase6/corpus_10b_loader_launch.pid
exec uv run --frozen --extra hub --extra data --extra ml --extra export \
  scripts/check_corpus_10b_ready.py --user-reduced-validation \
  --output /home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2 \
  --report reports/phase6/corpus_10b_loader_ready.json \
  >> reports/phase6/corpus_10b_loader_ready.log 2>&1
