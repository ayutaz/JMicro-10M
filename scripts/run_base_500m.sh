#!/usr/bin/env bash
# Run exactly the authorized 500M milestone; each stage resumes valid checkpoints.
set -euo pipefail
export PATH="${HOME}/.local/bin:${PATH}"
command -v uv >/dev/null
cd "$(dirname "${BASH_SOURCE[0]}")/.."
mkdir -p reports/local
exec 9>reports/local/base-500m-pipeline.lock
flock -n 9 || { echo '500M pipeline already active'; exit 1; }
state=reports/local/base-500m-pipeline.state
stage=preflight
record() {
  printf 'status=%s\nstage=%s\npid=%s\nboot_id=%s\nstart_ticks=%s\nat=%s\n' \
    "$1" "$stage" "$$" "$(cat /proc/sys/kernel/random/boot_id)" \
    "$(awk '{print $22}' /proc/$$/stat)" "$(date -u +%FT%TZ)" >"${state}.tmp"
  mv -f "${state}.tmp" "$state"
}
trap 'record failed' ERR
record running
for stage in stable decay evaluate; do
  record running
  uv run --frozen --extra hub --extra data --extra ml --extra export \
    scripts/run_base.py --config configs/phase6/base_frozen.json \
    --target 500M --output reports/phase6/base-20261003 \
    --operation "$stage" --execute
  cp reports/phase6/base-20261003/supervisor.json "reports/phase6/base-20261003/supervisor-${stage}-500M.json"
done
stage=training-and-machine-evaluation-finished
record complete
echo '500M stages complete; review results and commit before stopping. 1B was not started.'
