#!/usr/bin/env bash
# Keep this foreground supervisor in a detached Windows wsl.exe process.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.."
export PATH="$HOME/.local/bin:/usr/lib/wsl/lib:$PATH"
export JMICRO_DATA_ROOT="$HOME/jmicro-data"
exec uv run --frozen --extra hub --extra data --extra ml --extra export "$@"
