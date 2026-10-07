param([switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$runDir=Join-Path $workspace 'reports/phase6/base-sigsoftmax-probe-launcher-20261007'
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if(-not $Worker){
    if(Test-Path -LiteralPath (Join-Path $runDir 'launcher.json')){throw 'Inspect actual process; no duplicate sigsoftmax probe.'}
    $process=Start-Process powershell.exe -ArgumentList @('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Worker') -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    [IO.File]::WriteAllText((Join-Path $runDir 'launcher.json'),(@{windows_pid=$process.Id;started_at=$process.StartTime.ToUniversalTime().ToString('o')}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started durable sigsoftmax probe '+$process.Id); exit 0
}
$result=@{status='starting';started_at=[DateTime]::UtcNow.ToString('o')}
$uiStopped=$false
try{
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- env CUDA_VISIBLE_DEVICES= /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/probe_base_sigsoftmax.py --inspect
    if($LASTEXITCODE -ne 0){throw 'Frozen sigsoftmax probe preflight failed'}
    $uiStopped=$true
    & (Join-Path $PSScriptRoot 'stop_webui.ps1')
    if($LASTEXITCODE -ne 0){throw 'UI stop failed'}
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/probe_base_sigsoftmax.py
    $result.exit_code=$LASTEXITCODE
    $result.status=if($LASTEXITCODE -eq 0){'complete'}else{'failed'}
}catch{$result.status='failed';$result.error=$_.Exception.Message}
finally{
    $result.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    if($uiStopped){& (Join-Path $PSScriptRoot 'start_webui.ps1')}
}
if($result.status -eq 'failed'){exit 1}
