param([ValidateSet('diagnostic','compare','expand')][string]$Stage='diagnostic',[switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$runDir=Join-Path $workspace ('reports\phase6\natural-learning-launcher-20261005\'+$Stage)
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if (-not $Worker) {
    $record=Join-Path $runDir 'launcher.json'
    if (Test-Path -LiteralPath $record) { throw 'Existing launcher: inspect actual job and saved checkpoints before restarting.' }
    $args=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Stage',$Stage,'-Worker')
    $process=Start-Process powershell.exe -ArgumentList $args -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    [IO.File]::WriteAllText($record,(@{windows_pid=$process.Id;start_time=$process.StartTime.ToUniversalTime().ToString('o');stage=$Stage}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started durable '+$Stage+' worker '+$process.Id);exit 0
}
Set-Location -LiteralPath $workspace
$outcome=@{started_at=[DateTime]::UtcNow.ToString('o');stage=$Stage;status='starting'}
try {
    & (Join-Path $PSScriptRoot 'stop_webui.ps1')
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_natural_learning.py --mode run --stage $Stage
    $outcome.exit_code=$LASTEXITCODE;$outcome.status=if ($LASTEXITCODE -eq 0) {'complete'} else {'failed'}
} catch {$outcome.status='failed';$outcome.error=$_.Exception.Message}
finally {
    $outcome.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($outcome|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    & (Join-Path $PSScriptRoot 'start_webui.ps1')
}
