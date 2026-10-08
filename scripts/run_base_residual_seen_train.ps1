param([switch]$Worker)
$ErrorActionPreference='Stop'
$taskWorkspace=Split-Path -Parent $PSScriptRoot
$taskRunDir=Join-Path $taskWorkspace 'reports/phase6/base-residual-seen-train-launcher-20261008'
New-Item -ItemType Directory -Force -Path $taskRunDir | Out-Null
if(-not $Worker) {
    if(Test-Path -LiteralPath (Join-Path $taskRunDir 'launcher.json')) {throw 'Inspect existing actual diagnostic; no duplicate launcher.'}
    $taskProcess=Start-Process powershell.exe -ArgumentList @('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Worker') -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $taskRunDir 'stdout.log') -RedirectStandardError (Join-Path $taskRunDir 'stderr.log')
    [IO.File]::WriteAllText((Join-Path $taskRunDir 'launcher.json'),(@{windows_pid=$taskProcess.Id;started_at=$taskProcess.StartTime.ToUniversalTime().ToString('o')} | ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started durable six-case diagnostic worker '+$taskProcess.Id)
    exit 0
}
$taskResult=@{status='starting';started_at=[DateTime]::UtcNow.ToString('o')}
$taskUIStopped=$false
try {
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- env CUDA_VISIBLE_DEVICES= /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_base_residual_seen_train.py --inspect
    if($LASTEXITCODE -ne 0) {throw 'Six-case preflight failed before UI change.'}
    $taskUIStopped=$true
    & (Join-Path $PSScriptRoot 'stop_webui.ps1')
    if($LASTEXITCODE -ne 0) {throw 'Original UI stop failed; no diagnostic started.'}
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- env CUDA_VISIBLE_DEVICES= /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_base_residual_seen_train.py --wait-ui
    if($LASTEXITCODE -ne 0) {throw 'Actual UI process has not exited; no diagnostic started.'}
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_base_residual_seen_train.py
    $taskResult.exit_code=$LASTEXITCODE
    $taskResult.status=if($LASTEXITCODE -eq 0){'complete'}else{'failed'}
} catch {$taskResult.status='failed';$taskResult.error=$_.Exception.Message}
finally {
    if($taskUIStopped) {
        try {
            & (Join-Path $PSScriptRoot 'start_webui.ps1')
            if($LASTEXITCODE -ne 0) {throw 'Original10B UI restoration failed.'}
            $taskResult.UI_restore_command_succeeded=$true
        } catch {$taskResult.status='failed';$taskResult.UI_restore_error=$_.Exception.Message}
    }
    $taskResult.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $taskRunDir 'result.json'),($taskResult | ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    $taskNativeLauncher='\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m\reports\phase6\base-residual-seen-train-launcher-20261008'
    New-Item -ItemType Directory -Force -Path $taskNativeLauncher | Out-Null
    Get-ChildItem -LiteralPath $taskRunDir -File | ForEach-Object {Copy-Item -LiteralPath $_.FullName -Destination (Join-Path $taskNativeLauncher $_.Name)}
}
if($taskResult.status -eq 'failed') {exit 1}
