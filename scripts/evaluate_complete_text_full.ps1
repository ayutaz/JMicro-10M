$ErrorActionPreference = 'Stop'
$recordPath = '\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m\reports\local\webui\server.json'
$restoreUi = (Test-Path $recordPath) -and ((Get-Content $recordPath -Raw | ConvertFrom-Json).status -eq 'running')
try {
  if ($restoreUi) { & (Join-Path $PSScriptRoot 'stop_webui.ps1') }
  & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/evaluate_complete_text_full.py
  if ($LASTEXITCODE -ne 0) { throw 'Conditional evaluation failed; inspect persisted job before resuming.' }
} finally {
  if ($restoreUi) { & (Join-Path $PSScriptRoot 'start_webui.ps1') }
}
