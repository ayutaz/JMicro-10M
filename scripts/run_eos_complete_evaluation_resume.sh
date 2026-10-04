#!/usr/bin/env bash
set -euo pipefail
export PATH="${HOME}/.local/bin:${PATH}"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
export CUBLAS_WORKSPACE_CONFIG=:4096:8
cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m
destination=reports/phase6/eos-complete-100m-20261004-r2
exec 9>"$destination/launch.lock"
flock -n 9
exec >>"$destination/pipeline.log" 2>&1
exec uv run --frozen --extra hub --extra data --extra ml --extra export scripts/resume_eos_complete_evaluation.py
