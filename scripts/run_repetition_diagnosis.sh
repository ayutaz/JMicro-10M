#!/usr/bin/env bash
# Persist read-only diagnostic output across conversation disconnects.
set -euo pipefail
export PATH="${HOME}/.local/bin:${PATH}"
cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m
phase="${1:?cpu or gpu required}"
case "$phase" in cpu|gpu) ;; *) exit 2 ;; esac
destination=reports/phase6/repetition-diagnosis-20261003
mkdir -p "$destination"
exec 9>"$destination/launch-$phase.lock"
flock -n 9
exec >>"$destination/$phase.log" 2>&1
exec uv run --frozen --extra hub --extra data --extra ml --extra export scripts/investigate_repetition.py --phase "$phase"
