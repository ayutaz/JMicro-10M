#!/usr/bin/env bash
set -euo pipefail
export PATH="/home/aihub_ubuntu/.local/bin:$PATH"
cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m
mkdir -p /home/aihub_ubuntu/jmicro-data/phase6/ten-billion/raw
exec uv run --frozen --extra hub --extra data --extra ml --extra export scripts/acquire_corpus_10b.py --output /home/aihub_ubuntu/jmicro-data/phase6/ten-billion/raw >> /home/aihub_ubuntu/jmicro-data/phase6/ten-billion/acquisition.log 2>&1
