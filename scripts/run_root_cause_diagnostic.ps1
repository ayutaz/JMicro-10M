param([switch]$Worker,[switch]$Precision)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$runDir=Join-Path $workspace 'reports\phase6\root-cause-launcher-20261005'
if ($Precision) { $runDir=Join-Path $workspace 'reports\phase6\root-cause-precision-launcher-20261005' }
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if (-not $Worker) {
    $recordPath=Join-Path $runDir 'launcher.json'
    if (Test-Path -LiteralPath $recordPath) { throw 'Launcher record exists. Audit actual process and saved job before restarting.' }
    $arguments=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Worker')
    if ($Precision) { $arguments+='-Precision' }
    $process=Start-Process powershell.exe -ArgumentList $arguments -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    $record=@{windows_pid=$process.Id;start_time=$process.StartTime.ToUniversalTime().ToString('o');script_sha256=(Get-FileHash -LiteralPath $PSCommandPath -Algorithm SHA256).Hash.ToLower();linux_job='/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/root-cause-20261005/job.json'}
    [IO.File]::WriteAllText($recordPath,($record|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Launched durable diagnostic worker '+$process.Id)
    exit 0
}
Set-Location -LiteralPath $workspace
$outcome=@{started_at=[DateTime]::UtcNow.ToString('o');status='starting'}
try {
    & (Join-Path $PSScriptRoot 'stop_webui.ps1')
    if ($Precision) {
        & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/probe_root_cause_precision.py
    } else {
        & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_root_cause_diagnostic.py --run
    }
    $outcome.exit_code=$LASTEXITCODE
    $outcome.status=if ($LASTEXITCODE -eq 0) {'complete'} else {'failed'}
} catch {
    $outcome.status='failed'
    $outcome.error=$_.Exception.Message
} finally {
    $outcome.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($outcome|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    & (Join-Path $PSScriptRoot 'start_webui.ps1')
}
