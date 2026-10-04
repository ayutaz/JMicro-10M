#!/usr/bin/env bash
set -euo pipefail
export PATH="${HOME}/.local/bin:${PATH}"
cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m
destination=reports/phase6/eos-diagnosis-2b-20261004-r1
mkdir -p "$destination"
exec 9>"$destination/launch.lock"
flock -n 9
exec >>"$destination/run.log" 2>&1
exec uv run --frozen --extra hub --extra data --extra ml --extra export scripts/investigate_eos_2b.py
