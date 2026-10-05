param([ValidateSet('Probe','Train')][string]$Mode='Train',[switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$runDir=Join-Path $workspace ('reports\phase6\sequence-objective-'+$Mode.ToLower()+'-launcher-20261006')
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if (-not $Worker) {
    $record=Join-Path $runDir 'launcher.json'
    if (Test-Path -LiteralPath $record) {throw 'Inspect actual process/checkpoints before resuming with -Worker.'}
    $argsList=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Mode',$Mode,'-Worker')
    $process=Start-Process powershell.exe -ArgumentList $argsList -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    [IO.File]::WriteAllText($record,(@{windows_pid=$process.Id;started_at=$process.StartTime.ToUniversalTime().ToString('o');mode=$Mode}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started durable sequence objective '+$Mode+' worker '+$process.Id);exit 0
}
Set-Location -LiteralPath $workspace
$result=@{status='starting';mode=$Mode;started_at=[DateTime]::UtcNow.ToString('o')}
$uiStopped=$false
try {
    $preflight=if($Mode -eq 'Probe'){'--preflight-probe'}else{'--inspect'}
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_sequence_objective_comparison.py $preflight
    if ($LASTEXITCODE -ne 0){throw 'Objective preflight rejected the recipe before UI/GPU changes.'}
    & (Join-Path $PSScriptRoot 'stop_webui.ps1');$uiStopped=$true
    if ($Mode -eq 'Probe') {
        & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_sequence_objective_comparison.py --probe
    } else {
        & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_sequence_objective_comparison.py
    }
    $result.exit_code=$LASTEXITCODE;$result.status=if($LASTEXITCODE -eq 0){'complete'}else{'failed'}
} catch {$result.status='failed';$result.error=$_.Exception.Message}
finally {
    $result.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    if($uiStopped){& (Join-Path $PSScriptRoot 'start_webui.ps1')}
}
