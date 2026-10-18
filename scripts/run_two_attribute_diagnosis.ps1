param([switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$linuxRepo='/home/aihub_ubuntu/src/japanese-tiny-llm-10m'
$runDir=Join-Path $workspace 'reports/phase7/chat-two-attribute-20261018/launcher'
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if(-not $Worker){
    $recordPath=Join-Path $runDir 'launcher.json'
    if(Test-Path -LiteralPath $recordPath){throw 'Existing launcher: audit actual identity and terminal state; duplicate refused.'}
    $arguments=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Worker')
    $childProcess=Start-Process pwsh.exe -ArgumentList $arguments -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    [IO.File]::WriteAllText($recordPath,(@{windows_pid=$childProcess.Id;started_at=$childProcess.StartTime.ToUniversalTime().ToString('o')}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output "Started durable two-attribute worker $($childProcess.Id)"
    exit 0
}
Set-Location -LiteralPath $workspace
$prefix=@('-d','Ubuntu','--cd',$linuxRepo,'--','/home/aihub_ubuntu/.local/bin/uv','run','--frozen','--extra','hub','--extra','data','--extra','ml','--extra','export')
$result=@{started_at=[DateTime]::UtcNow.ToString('o');status='starting'}
$uiStopped=$false
try{
    & wsl.exe @prefix scripts/run_two_attribute_diagnosis.py inspect
    if($LASTEXITCODE -ne 0){throw 'Frozen contract preflight failed.'}
    & wsl.exe @prefix scripts/inspect_two_attribute_diagnosis.py
    if($LASTEXITCODE -ne 0){throw 'Actual original Base UI/resource guard failed.'}
    & pwsh.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'stop_webui.ps1')
    if($LASTEXITCODE -ne 0){throw 'Original UI identity refused stopping.'}
    $uiStopped=$true
    & wsl.exe @prefix scripts/run_two_attribute_diagnosis.py run
    $result.exit_code=$LASTEXITCODE
    if($LASTEXITCODE -ne 0){throw "Experiment exit $LASTEXITCODE; preserve failed condition."}
    $result.status='complete_raw_pending_review'
}catch{$result.status='failed';$result.error=$_.Exception.Message}
finally{
    if($uiStopped){
        & pwsh.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'start_webui.ps1')
        $result.original_UI_restore_exit_code=$LASTEXITCODE
        if($LASTEXITCODE -ne 0){$result.status='failed';$result.UI_restore_error='Inspect original UI restoration.'}
    }
    $result.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
}
if($result.status -eq 'failed'){exit 1}
