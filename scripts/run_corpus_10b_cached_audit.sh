#!/usr/bin/env bash
set -euo pipefail
export PATH="/home/aihub_ubuntu/.local/bin:$PATH"
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MKL_NUM_THREADS=1
cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m
exec uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_corpus_10b_cached_audit.py --raw /home/aihub_ubuntu/jmicro-data/phase6/ten-billion/raw --output /home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2 >> /home/aihub_ubuntu/jmicro-data/phase6/ten-billion/preparation-v4.log 2>&1
