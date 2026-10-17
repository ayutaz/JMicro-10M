param([switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$linuxRepo='/home/aihub_ubuntu/src/japanese-tiny-llm-10m'
$runDir=Join-Path $workspace 'reports/phase7/chat-answer-learning-20261017-launcher/diagnostic'
New-Item -ItemType Directory -Force -Path $runDir|Out-Null
if(-not $Worker){
    $recordPath=Join-Path $runDir 'launcher.json'
    if(Test-Path -LiteralPath $recordPath){throw 'A diagnostic launch exists; inspect its exact identity and terminal record. Duplicate refused.'}
    $tag=[DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfff')
    $argsList=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Worker')
    $process=Start-Process powershell.exe -ArgumentList $argsList -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir "stdout-$tag.log") -RedirectStandardError (Join-Path $runDir "stderr-$tag.log")
    [IO.File]::WriteAllText($recordPath,(@{windows_pid=$process.Id;started_at=$process.StartTime.ToUniversalTime().ToString('o');stdout="stdout-$tag.log";stderr="stderr-$tag.log"}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output "Started durable diagnostic worker $($process.Id)"
    exit 0
}
Set-Location -LiteralPath $workspace
$prefix=@('-d','Ubuntu','--cd',$linuxRepo,'--','/home/aihub_ubuntu/.local/bin/uv','run','--frozen','--extra','hub','--extra','data','--extra','ml','--extra','export')
$result=@{started_at=[DateTime]::UtcNow.ToString('o');status='starting'}
$uiStopped=$false
try{
    & wsl.exe @prefix scripts/answer_diagnostic.py inspect
    if($LASTEXITCODE -ne 0){throw 'Frozen diagnostic preflight failed.'}
    & wsl.exe @prefix scripts/inspect_answer_diagnostic.py
    if($LASTEXITCODE -ne 0){throw 'Original UI/resource observation failed.'}
    & powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'stop_webui.ps1')
    if($LASTEXITCODE -ne 0){throw 'Original UI identity refused stopping.'}
    $uiStopped=$true
    & wsl.exe @prefix scripts/answer_diagnostic.py run
    $result.exit_code=$LASTEXITCODE
    if($LASTEXITCODE -ne 0){throw "Diagnostic exit $LASTEXITCODE; preserve original condition."}
    $result.status='complete'
}catch{$result.status='failed';$result.error=$_.Exception.Message}
finally{
    if($uiStopped){
        & powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'start_webui.ps1')
        $result.original_UI_restore_exit_code=$LASTEXITCODE
        if($LASTEXITCODE -ne 0){$result.status='failed';$result.UI_restore_error='Original UI restoration requires inspection.'}
    }
    $result.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
}
if($result.status -ne 'complete'){exit 1}
