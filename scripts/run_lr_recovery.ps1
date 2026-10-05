param([switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$runDir=Join-Path $workspace 'reports\phase6\lr-recovery-launcher-20261006'
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if (-not $Worker) {
    $record=Join-Path $runDir 'launcher.json'
    if (Test-Path -LiteralPath $record) { throw 'Inspect actual LR job/checkpoints before restart.' }
    $argsList=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Worker')
    $process=Start-Process powershell.exe -ArgumentList $argsList -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    [IO.File]::WriteAllText($record,(@{windows_pid=$process.Id;started_at=$process.StartTime.ToUniversalTime().ToString('o')}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started durable LR worker '+$process.Id);exit 0
}
Set-Location -LiteralPath $workspace
$result=@{started_at=[DateTime]::UtcNow.ToString('o');status='starting'}
try {
    & (Join-Path $PSScriptRoot 'stop_webui.ps1')
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_lr_recovery.py
    $result.exit_code=$LASTEXITCODE;$result.status=if($LASTEXITCODE -eq 0){'complete'}else{'failed'}
} catch {$result.status='failed';$result.error=$_.Exception.Message}
finally {
    $result.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    & (Join-Path $PSScriptRoot 'start_webui.ps1')
}
