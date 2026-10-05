param([switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$runDir=Join-Path $workspace 'reports\phase6\strategy-baselines-launcher-20261005'
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if (-not $Worker) {
    $record=Join-Path $runDir 'launcher.json'
    if (Test-Path -LiteralPath $record) { throw 'Inspect existing actual baseline job before restart.' }
    $workerArgs=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Worker')
    $process=Start-Process powershell.exe -ArgumentList $workerArgs -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    [IO.File]::WriteAllText($record,(@{windows_pid=$process.Id;start_time=$process.StartTime.ToUniversalTime().ToString('o')}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started durable baseline worker '+$process.Id)
    exit 0
}
Set-Location -LiteralPath $workspace
$outcome=@{started_at=[DateTime]::UtcNow.ToString('o');status='starting'}
try {
    & (Join-Path $PSScriptRoot 'stop_webui.ps1')
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_strategy_baselines.py
    $outcome.exit_code=$LASTEXITCODE
    $outcome.status=if ($LASTEXITCODE -eq 0) {'complete'} else {'failed'}
} catch {$outcome.status='failed';$outcome.error=$_.Exception.Message}
finally {
    $outcome.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($outcome|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    & (Join-Path $PSScriptRoot 'start_webui.ps1')
}
