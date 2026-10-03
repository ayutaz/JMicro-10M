#!/usr/bin/env bash
set -euo pipefail
export PATH="/home/aihub_ubuntu/.local/bin:$PATH"
cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m
exec uv run --frozen --extra hub --extra data --extra ml --extra export scripts/prepare_corpus_10b.py --raw /home/aihub_ubuntu/jmicro-data/phase6/ten-billion/raw --output /home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2 --wait-for-acquisition >> /home/aihub_ubuntu/jmicro-data/phase6/ten-billion/preparation-v2.log 2>&1
