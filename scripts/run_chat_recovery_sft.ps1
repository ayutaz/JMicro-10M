param([switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$linuxRepo='/home/aihub_ubuntu/src/japanese-tiny-llm-10m'
$runDir=Join-Path $workspace 'reports/phase7/chat-recovery-20261018/launcher'
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if(-not $Worker){
    $recordPath=Join-Path $runDir 'launcher.json'
    if(Test-Path -LiteralPath $recordPath){throw 'Existing launch: inspect its actual identity and terminal state; duplicate refused.'}
    $tag=[DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfff')
    $arguments=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Worker')
    $worker=Start-Process powershell.exe -ArgumentList $arguments -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir "stdout-$tag.log") -RedirectStandardError (Join-Path $runDir "stderr-$tag.log")
    [IO.File]::WriteAllText($recordPath,(@{windows_pid=$worker.Id;started_at=$worker.StartTime.ToUniversalTime().ToString('o');stdout="stdout-$tag.log";stderr="stderr-$tag.log"}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output "Started durable input-structure SFT worker $($worker.Id)"
    exit 0
}
Set-Location -LiteralPath $workspace
$prefix=@('-d','Ubuntu','--cd',$linuxRepo,'--','/home/aihub_ubuntu/.local/bin/uv','run','--frozen','--extra','hub','--extra','data','--extra','ml','--extra','export')
$result=@{started_at=[DateTime]::UtcNow.ToString('o');status='starting'}
$uiStopped=$false
try{
    & wsl.exe @prefix scripts/run_chat_recovery_sft.py inspect
    if($LASTEXITCODE -ne 0){throw 'New contract preflight failed.'}
    & wsl.exe @prefix scripts/inspect_chat_recovery_sft.py
    if($LASTEXITCODE -ne 0){throw 'Current Base UI/resource observation failed.'}
    & powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'stop_webui.ps1')
    if($LASTEXITCODE -ne 0){throw 'Original UI identity refused stopping.'}
    $uiStopped=$true
    & wsl.exe @prefix scripts/run_chat_recovery_sft.py run
    $result.exit_code=$LASTEXITCODE
    if($LASTEXITCODE -ne 0){throw "New comparison exit $LASTEXITCODE; preserve failed condition."}
    $result.status='complete_raw_pending_content_and_browser'
}catch{$result.status='failed';$result.error=$_.Exception.Message}
finally{
    if($uiStopped){
        & powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'start_webui.ps1')
        $result.original_UI_restore_exit_code=$LASTEXITCODE
        if($LASTEXITCODE -ne 0){$result.status='failed';$result.UI_restore_error='Inspect original UI restoration.'}
    }
    $result.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
}
if($result.status -eq 'failed'){exit 1}
