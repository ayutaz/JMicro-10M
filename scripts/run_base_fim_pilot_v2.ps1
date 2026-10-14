param([switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$launchDir=Join-Path $workspace 'reports/phase6/base-fim-pilot-launcher-v2-20261015'
New-Item -ItemType Directory -Force -Path $launchDir | Out-Null
if(-not $Worker){
    if(Test-Path -LiteralPath (Join-Path $launchDir 'launcher.json')){throw 'Inspect actual worker/job; never duplicate launch.'}
    $workerProcess=Start-Process powershell.exe -ArgumentList @('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Worker') -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $launchDir 'stdout.log') -RedirectStandardError (Join-Path $launchDir 'stderr.log')
    [IO.File]::WriteAllText((Join-Path $launchDir 'launcher.json'),(@{windows_pid=$workerProcess.Id;started_at=$workerProcess.StartTime.ToUniversalTime().ToString('o')}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started durable FIM pilot v2 worker '+$workerProcess.Id);exit 0
}
$record=@{status='starting';started_at=[DateTime]::UtcNow.ToString('o');handoff_observations=@()}
$uiStopped=$false
try{
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- env CUDA_VISIBLE_DEVICES= /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_base_fim_pilot.py inspect
    if($LASTEXITCODE -ne 0){throw 'Frozen FIM preflight failed'}
    $uiRecord=Get-Content '\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m\reports\local\webui\server.json' -Raw|ConvertFrom-Json
    $ui=Invoke-RestMethod -Uri 'http://127.0.0.1:7860/api/model' -TimeoutSec 2
    if($ui.busy -or $ui.parameters -ne 10001152 -or $ui.checkpoint_sha256 -ne '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'){throw 'Original UI must be verified idle'}
    $uiStopped=$true
    & (Join-Path $PSScriptRoot 'stop_webui.ps1')
    if($LASTEXITCODE -ne 0){throw 'Verified UI stop failed'}
    $handoffStart=[DateTime]::UtcNow
    do{
        $gpuRows=@(& wsl.exe -d Ubuntu -- nvidia-smi --query-compute-apps=pid --format=csv,noheader)
        if($LASTEXITCODE -ne 0){throw 'Actual GPU peer query failed'}
        $gpuPids=@($gpuRows|Where-Object{$_.Trim()}|ForEach-Object{[int]$_.Trim()})
        $record.handoff_observations+=@{observed_at=[DateTime]::UtcNow.ToString('o');gpu_pids=$gpuPids}
        if(@($gpuPids|Where-Object{$_ -ne [int]$uiRecord.pid}).Count){throw 'An unrelated GPU process is active; preserve it'}
        if(-not $gpuPids.Count){break}
        if(([DateTime]::UtcNow-$handoffStart).TotalSeconds -gt 15){throw 'Known UI still releasing GPU after15s; do not relaunch science'}
        Start-Sleep -Milliseconds 250
    }while($true)
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_base_fim_pilot.py run
    $record.exit_code=$LASTEXITCODE
    $record.status=if($LASTEXITCODE -eq 0){'complete'}else{'failed'}
}catch{$record.status='failed';$record.error=$_.Exception.Message}
finally{
    $record.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $launchDir 'result.json'),($record|ConvertTo-Json -Depth 8),[Text.UTF8Encoding]::new($false))
    if($uiStopped){& (Join-Path $PSScriptRoot 'start_webui.ps1')}
}
if($record.status -eq 'failed'){exit 1}
