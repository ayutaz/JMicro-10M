param([switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$launchDir=Join-Path $workspace 'reports/phase6/base-fim-pilot-launcher-20261015'
New-Item -ItemType Directory -Force -Path $launchDir | Out-Null
if(-not $Worker){
    if(Test-Path -LiteralPath (Join-Path $launchDir 'launcher.json')){throw 'Inspect actual FIM worker/job; never duplicate launch.'}
    $workerProcess=Start-Process powershell.exe -ArgumentList @('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Worker') -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $launchDir 'stdout.log') -RedirectStandardError (Join-Path $launchDir 'stderr.log')
    [IO.File]::WriteAllText((Join-Path $launchDir 'launcher.json'),(@{windows_pid=$workerProcess.Id;started_at=$workerProcess.StartTime.ToUniversalTime().ToString('o')}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started durable FIM pilot worker '+$workerProcess.Id);exit 0
}
$record=@{status='starting';started_at=[DateTime]::UtcNow.ToString('o')}
$uiStopped=$false
try{
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- env CUDA_VISIBLE_DEVICES= /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_base_fim_pilot.py inspect
    if($LASTEXITCODE -ne 0){throw 'Frozen FIM preflight failed'}
    $ui=Invoke-RestMethod -Uri 'http://127.0.0.1:7860/api/model' -TimeoutSec 2
    if($ui.busy -or $ui.checkpoint_sha256 -ne '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'){throw 'Original UI must be verified idle before GPU handoff'}
    $uiStopped=$true
    & (Join-Path $PSScriptRoot 'stop_webui.ps1')
    if($LASTEXITCODE -ne 0){throw 'Verified UI stop failed'}
    $peers=& wsl.exe -d Ubuntu -- nvidia-smi --query-compute-apps=pid --format=csv,noheader
    if($LASTEXITCODE -ne 0 -or ($peers -and $peers.Trim())){throw 'GPU still has another compute process; do not launch'}
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_base_fim_pilot.py run
    $record.exit_code=$LASTEXITCODE
    $record.status=if($LASTEXITCODE -eq 0){'complete'}else{'failed'}
}catch{$record.status='failed';$record.error=$_.Exception.Message}
finally{
    $record.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $launchDir 'result.json'),($record|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    if($uiStopped){& (Join-Path $PSScriptRoot 'start_webui.ps1')}
}
if($record.status -eq 'failed'){exit 1}
