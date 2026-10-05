param([switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$runDir=Join-Path $workspace 'reports\phase6\textbook-coverage-save-cadence-launcher-20261006'
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if(-not $Worker) {
    if(Test-Path -LiteralPath (Join-Path $runDir 'launcher.json')) {throw 'Inspect previous cadence measurement before retrying.'}
    $arguments=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Worker')
    $process=Start-Process powershell.exe -ArgumentList $arguments -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    [IO.File]::WriteAllText((Join-Path $runDir 'launcher.json'),(@{windows_pid=$process.Id;started_at=[DateTime]::UtcNow.ToString('o')}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started cadence measurement worker '+$process.Id);exit 0
}
$result=@{status='starting';started_at=[DateTime]::UtcNow.ToString('o')};$uiStopped=$false
try {
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_textbook_coverage.py --preflight-probe
    if($LASTEXITCODE -ne 0){throw 'Cadence preflight rejected.'}
    & (Join-Path $PSScriptRoot 'stop_webui.ps1');$uiStopped=$true
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/measure_textbook_coverage_speed.py
    $result.exit_code=$LASTEXITCODE;$result.status=if($LASTEXITCODE -eq 0){'complete'}else{'failed'}
} catch {$result.status='failed';$result.error=$_.Exception.Message}
finally {
    $result.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    if($uiStopped){& (Join-Path $PSScriptRoot 'start_webui.ps1')}
}
