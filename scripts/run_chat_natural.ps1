param([Parameter(Mandatory=$true)][ValidateSet('probe','pipeline','evaluate')][string]$Mode,[switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$linuxRepo='/home/aihub_ubuntu/src/japanese-tiny-llm-10m'
$linuxCopy='\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m'
$runDir=Join-Path $workspace "reports/phase7/chat-natural-sft-20261017-launcher/$Mode"
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if (-not $Worker) {
    $recordPath=Join-Path $runDir 'launcher.json'
    if (Test-Path -LiteralPath $recordPath) {
        $old=Get-Content -LiteralPath $recordPath -Raw | ConvertFrom-Json
        $live=Get-Process -Id $old.windows_pid -ErrorAction SilentlyContinue
        if ($live -and $live.StartTime.ToUniversalTime().ToString('o') -eq $old.started_at) {throw 'Owned worker is still alive; duplicate refused.'}
        throw 'A prior launch exists. Inspect its result and exact process/checkpoints before resuming.'
    }
    $argsList=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Mode',$Mode,'-Worker')
    $tag=[DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfff')
    $process=Start-Process powershell.exe -ArgumentList $argsList -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir "stdout-$tag.log") -RedirectStandardError (Join-Path $runDir "stderr-$tag.log")
    [IO.File]::WriteAllText($recordPath,(@{windows_pid=$process.Id;started_at=$process.StartTime.ToUniversalTime().ToString('o');mode=$Mode;stdout="stdout-$tag.log";stderr="stderr-$tag.log"}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output "Started durable $Mode worker $($process.Id)"
    exit 0
}
Set-Location -LiteralPath $workspace
$prefix=@('-d','Ubuntu','--cd',$linuxRepo,'--','/home/aihub_ubuntu/.local/bin/uv','run','--frozen','--extra','hub','--extra','data','--extra','ml','--extra','export')
$command=@('scripts/run_chat_natural.py','--mode',$Mode)
$result=@{started_at=[DateTime]::UtcNow.ToString('o');status='starting';mode=$Mode}
$uiStopped=$false
try {
    & wsl.exe @prefix @command --inspect
    if ($LASTEXITCODE -ne 0) {throw 'Frozen preflight failed before any UI or CUDA change.'}
    & wsl.exe @prefix scripts/inspect_chat_natural_environment.py
    if ($LASTEXITCODE -ne 0) {throw 'Actual process/UI/lock/capacity gate failed.'}
    & powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'stop_webui.ps1')
    if ($LASTEXITCODE -ne 0) {throw 'Original UI identity guard refused stopping.'}
    $uiStopped=$true
    & wsl.exe @prefix @command
    $result.exit_code=$LASTEXITCODE
    if ($LASTEXITCODE -ne 0) {throw "Worker exit $LASTEXITCODE; preserve logs and condition before diagnosis."}
    $result.status='complete'
} catch {$result.status='failed';$result.error=$_.Exception.Message}
finally {
    if ($uiStopped) {
        & powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'start_webui.ps1')
        $result.original_UI_restore_exit_code=$LASTEXITCODE
        if ($LASTEXITCODE -ne 0) {$result.status='failed';$result.UI_restore_error='Original UI restore failed; inspect saved identity.'}
    }
    $result.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
}
if ($result.status -ne 'complete') {exit 1}
