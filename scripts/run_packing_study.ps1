$ErrorActionPreference='Stop'
$share='\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m'
$recordPath=Join-Path $share 'reports/local/webui/server.json'
$uvArgs=@('-d','Ubuntu','--cd','/home/aihub_ubuntu/src/japanese-tiny-llm-10m','--',
  '/home/aihub_ubuntu/.local/bin/uv','run','--frozen','--extra','hub','--extra','data','--extra','ml','--extra','export')
& wsl.exe @uvArgs scripts/run_packing_study.py --mode probe
if($LASTEXITCODE -ne 0){throw 'Frozen config invalid or actual job live; UI retained.'}
$restoreUi=(Test-Path $recordPath) -and ((Get-Content $recordPath -Raw | ConvertFrom-Json).status -eq 'running')
try {
  if($restoreUi){& (Join-Path $PSScriptRoot 'stop_webui.ps1')}
  & wsl.exe @uvArgs scripts/run_packing_study.py --mode run
  if($LASTEXITCODE -ne 0){throw 'Packing study failed; inspect actual process and checkpoint before resuming.'}
} finally {if($restoreUi){& (Join-Path $PSScriptRoot 'start_webui.ps1')}}
