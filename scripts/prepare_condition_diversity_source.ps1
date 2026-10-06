param([switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$runDir=Join-Path $workspace 'reports\phase6\condition-diversity-source-launcher-20261006'
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if(-not $Worker){
    if(Test-Path -LiteralPath (Join-Path $runDir 'launcher.json')){throw 'Inspect existing preparation; no automatic resampling.'}
    $arguments=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Worker')
    $process=Start-Process powershell.exe -ArgumentList $arguments -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    [IO.File]::WriteAllText((Join-Path $runDir 'launcher.json'),(@{windows_pid=$process.Id;started_at=$process.StartTime.ToUniversalTime().ToString('o')}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started durable CPU source preparation '+$process.Id);exit 0
}
& wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/prepare_condition_diversity_source.py
$result=@{exit_code=$LASTEXITCODE;ended_at=[DateTime]::UtcNow.ToString('o');status=$(if($LASTEXITCODE -eq 0){'complete'}else{'failed'})}
[IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
