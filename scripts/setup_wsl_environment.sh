#!/usr/bin/env bash
# Run as the Linux development user; logs are written into the Linux checkout.
set -euo pipefail

source_root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
project_root=${JMICRO_PROJECT_ROOT:-"$HOME/src/japanese-tiny-llm-10m"}
if [[ $(uname -s) != Linux ]] || [[ $(uname -r) != *[Mm]icrosoft* ]]; then
    echo 'Run this script inside WSL Linux.' >&2
    exit 1
fi
if [[ $(id -u) == 0 ]]; then
    echo 'Run as your non-root Linux development user.' >&2
    exit 1
fi
if [[ "$project_root" != /* || "$project_root" == /mnt/* ]]; then
    echo 'Choose an absolute project directory in the Linux filesystem, rather than /mnt/.' >&2
    exit 1
fi

# A new destination preserves the Windows working tree, including uncommitted code.
# An existing destination is never overwritten by the bootstrap.
if [[ "$project_root" != "$source_root" ]]; then
    if [[ -e "$project_root" ]]; then
        echo "Destination already exists: $project_root" >&2
        echo 'Run its setup script with JMICRO_PROJECT_ROOT set to that checkout, or choose a new destination.' >&2
        exit 1
    fi
    mkdir -p -- "$project_root"
    tar -C "$source_root" --exclude='./.venv' --exclude='./artifacts/tooling' \
        --exclude='./reports/phase4' --exclude='./reports/automation' \
        --exclude='./.pytest_cache' -cf - . | tar -C "$project_root" -xf -
fi
cd -- "$project_root"
mkdir -p reports/phase4
exec > >(tee -a reports/phase4/setup.log) 2>&1
trap 'echo "Setup failed at line $LINENO. Fix the reported issue, then rerun from this Linux checkout."' ERR
echo "Linux checkout: $project_root"
if ! command -v git >/dev/null || ! command -v curl >/dev/null; then
    sudo apt-get update
    sudo apt-get install -y git curl ca-certificates
fi
export PATH="$HOME/.local/bin:/usr/lib/wsl/lib:$PATH"
if ! command -v uv >/dev/null; then
    installer=$(mktemp)
    curl --fail --location --silent --show-error https://astral.sh/uv/install.sh --output "$installer"
    sh "$installer"
    rm -- "$installer"
fi
uv --version
uv python install 3.12.7

# Restore the pilot before installing the much larger GPU dependencies.
uv sync --frozen --python 3.12.7 --extra hub --extra data
uv run --frozen --extra hub --extra data scripts/download_hub_artifacts.py | tee reports/phase4/artifact_restore.json
export JMICRO_DATA_ROOT=${JMICRO_DATA_ROOT:-"$HOME/jmicro-data"}
mkdir -p -- "$JMICRO_DATA_ROOT"
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader | tee reports/phase4/gpu.txt
uv run --frozen --extra hub --extra data python - <<'PY'
import subprocess
rows = subprocess.check_output(['nvidia-smi', '--query-gpu=driver_version', '--format=csv,noheader'], text=True).splitlines()
if not rows or any(int(row.strip().split('.')[0]) < 580 for row in rows):
    raise SystemExit('The locked Linux dependencies use CUDA 13. Update the Windows NVIDIA driver to a current CUDA 13 compatible driver (580+), then rerun. Artifacts are already restored.')
PY

uv sync --frozen --python 3.12.7 --extra hub --extra data --extra ml --extra export
uv run --frozen --extra data scripts/validate_phase0.py --output reports/phase4/phase0_validation.json
uv run --frozen --extra data --extra ml --extra export scripts/experiment.py capture-environment --probe-torch --output reports/phase4/environment.json
uv run --frozen --extra data --extra ml --extra export python - <<'PY'
import json
from pathlib import Path
env = json.loads(Path('reports/phase4/environment.json').read_text())
assert env['platform']['is_wsl'], 'Not a WSL Linux environment'
assert env['torch_probe']['cuda_available'], 'CUDA unavailable; inspect environment.json'
assert env['torch_probe']['bf16_supported'], 'BF16 unavailable; inspect environment.json'
import torch
x = torch.randn(64, 64, device='cuda', requires_grad=True)
with torch.autocast('cuda', dtype=torch.bfloat16):
    loss = (x @ x.T).float().square().mean()
loss.backward()
torch.cuda.synchronize()
assert torch.isfinite(loss) and torch.isfinite(x.grad).all(), 'CUDA forward/backward is not finite'
print('CUDA/BF16 tensor forward/backward passed; full model training/resume is still unverified.')
PY
uv run --frozen --extra data --extra ml --extra export pytest -q -ra --junitxml=reports/phase4/tests.xml
uv run --frozen --extra data --extra ml --extra export python - <<'PY'
import xml.etree.ElementTree as ET
root = ET.parse('reports/phase4/tests.xml').getroot()
suites = [root] if root.tag == 'testsuite' else list(root.iter('testsuite'))
assert sum(int(s.get('skipped', 0)) for s in suites) == 0, 'Skipped tests: review artifact restoration and tests.xml'
PY
run_dir=$(uv run --frozen --extra data --extra ml scripts/experiment.py prepare-run --name phase4-handoff-t8k --output-root reports/phase4 --tokenizer-artifact artifacts/phase2/8192/tokenizer.model --dataset-manifest data/phase1/processed/dataset_manifest.parquet)
uv run --frozen --extra data --extra ml scripts/experiment.py verify-run "$run_dir"
echo "Environment and artifacts checked. Reports: $project_root/reports/phase4"
echo 'Phase 4 training loop, checkpoint resume, and batch benchmarks remain to be implemented.'
