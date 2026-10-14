param([switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$launchDir=Join-Path $workspace 'reports/phase6/pseudo-repetition-probe-launcher-v2-20261015'
$linuxCopy='\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m'
$config=Join-Path $workspace 'configs/phase6/pseudo_repetition_probe_20261015.json'
$pin=(Get-FileHash -LiteralPath $config).Hash.ToLowerInvariant()
New-Item -ItemType Directory -Force -Path $launchDir | Out-Null
if(-not $Worker){
    if(Test-Path -LiteralPath (Join-Path $launchDir 'launcher.json')){throw 'Inspect actual worker/job, never duplicate a probe.'}
    $process=Start-Process -FilePath (Get-Process -Id $PID).Path -ArgumentList @('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Worker') -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $launchDir 'stdout.log') -RedirectStandardError (Join-Path $launchDir 'stderr.log')
    [IO.File]::WriteAllText((Join-Path $launchDir 'launcher.json'),(@{windows_pid=$process.Id;started_at=$process.StartTime.ToUniversalTime().ToString('o');config_sha256=$pin}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started owned native probe worker '+$process.Id);exit 0
}
$record=@{status='starting';started_at=[DateTime]::UtcNow.ToString('o');config_sha256=$pin;handoff_observations=@()}
$uiStopped=$false
try{
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- env CUDA_VISIBLE_DEVICES= /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/probe_pseudo_repetition.py inspect --config-sha256 $pin
    if($LASTEXITCODE -ne 0){throw 'Owned probe preflight failed'}
    $uiRecord=Get-Content -LiteralPath (Join-Path $linuxCopy 'reports/local/webui/server.json') -Raw | ConvertFrom-Json
    $ui=Invoke-RestMethod -Uri 'http://127.0.0.1:7860/api/model' -TimeoutSec 2
    if($ui.busy -or $ui.parameters -ne 10001152 -or $ui.checkpoint_sha256 -ne '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290' -or $ui.tokenizer_sha256 -ne 'a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'){throw 'Verified original idle UI required'}
    $record.original_UI=$ui
    $record.original_UI_identity=$uiRecord | Select-Object pid,boot_id,start_ticks
    $uiStopped=$true
    & (Join-Path $PSScriptRoot 'stop_webui.ps1')
    if($LASTEXITCODE -ne 0){throw 'Verified UI stop failed'}
    $handoff=[DateTime]::UtcNow
    do{
        $rows=@(& wsl.exe -d Ubuntu -- nvidia-smi --query-compute-apps=pid --format=csv,noheader)
        if($LASTEXITCODE -ne 0){throw 'GPU peer query failed'}
        $gpuPids=@($rows | Where-Object {$_.Trim()} | ForEach-Object {[int]$_.Trim()})
        $record.handoff_observations+=@{observed_at=[DateTime]::UtcNow.ToString('o');gpu_pids=$gpuPids}
        if(@($gpuPids | Where-Object {$_ -ne [int]$uiRecord.pid}).Count){throw 'Unrelated GPU peer is active; preserve it'}
        if(-not $gpuPids.Count){break}
        if(([DateTime]::UtcNow-$handoff).TotalSeconds -gt 15){throw 'Known UI release exceeded15s; do not repeat launch'}
        Start-Sleep -Milliseconds 250
    }while($true)
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/probe_pseudo_repetition.py run --config-sha256 $pin
    $record.exit_code=$LASTEXITCODE
    $record.status=if($LASTEXITCODE -eq 0){'complete'}else{'failed'}
}catch{$record.status='failed';$record.error=$_.Exception.Message}
finally{
    if($uiStopped){
        & (Join-Path $PSScriptRoot 'start_webui.ps1')
        $record.UI_restore_exit_code=$LASTEXITCODE
        try{
            $record.restored_UI=Invoke-RestMethod -Uri 'http://127.0.0.1:7860/api/model' -TimeoutSec 3
            $record.restored_UI_identity=(Get-Content -LiteralPath (Join-Path $linuxCopy 'reports/local/webui/server.json') -Raw | ConvertFrom-Json) | Select-Object pid,boot_id,start_ticks
        }catch{$record.UI_restore_error=$_.Exception.Message}
    }
    $record.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $launchDir 'result.json'),($record|ConvertTo-Json -Depth 9),[Text.UTF8Encoding]::new($false))
}
if($record.status -eq 'failed'){exit 1}
