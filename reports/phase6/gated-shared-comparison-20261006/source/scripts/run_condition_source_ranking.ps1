param([switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$runDir=Join-Path $workspace 'reports\phase6\condition-source-ranking-launcher-20261006'
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if(-not $Worker) {
    if(Test-Path -LiteralPath (Join-Path $runDir 'launcher.json')) {throw 'Inspect existing diagnostic process before using -Worker.'}
    $arguments=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Worker')
    $process=Start-Process powershell.exe -ArgumentList $arguments -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    [IO.File]::WriteAllText((Join-Path $runDir 'launcher.json'),(@{windows_pid=$process.Id;started_at=$process.StartTime.ToUniversalTime().ToString('o')}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started durable source-ranking diagnostic worker '+$process.Id);exit 0
}
$result=@{status='starting';started_at=[DateTime]::UtcNow.ToString('o')};$uiStopped=$false
try {
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_condition_source_ranking.py --inspect
    if($LASTEXITCODE -ne 0){throw 'Source-ranking preflight rejected before UI changes.'}
    $nativeJob='\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m\reports\phase6\condition-source-ranking-20261006\job.json'
    if((Test-Path -LiteralPath $nativeJob) -and ((Get-Content -Raw -LiteralPath $nativeJob | ConvertFrom-Json).status -eq 'complete')) {
        $result.status='already_complete';return
    }
    $uiStopped=$true
    & (Join-Path $PSScriptRoot 'stop_webui.ps1')
    if($LASTEXITCODE -ne 0){throw 'UI stop rejected; diagnostic not launched.'}
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_condition_source_ranking.py
    $result.exit_code=$LASTEXITCODE;$result.status=if($LASTEXITCODE -eq 0){'complete'}else{'failed'}
} catch {$result.status='failed';$result.error=$_.Exception.Message}
finally {
    $result.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    if($uiStopped){& (Join-Path $PSScriptRoot 'start_webui.ps1')}
}
