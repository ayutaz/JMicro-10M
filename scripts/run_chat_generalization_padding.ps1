param([switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$linuxRepo='/home/aihub_ubuntu/src/japanese-tiny-llm-10m'
$linuxCopy='\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m'
$runDir=Join-Path $workspace 'reports/phase7/chat-generalization-20261013-launcher/padding'
New-Item -ItemType Directory -Path $runDir -Force | Out-Null
if(-not $Worker){
    $recordPath=Join-Path $runDir 'launcher.json'
    if(Test-Path -LiteralPath $recordPath){
        $old=Get-Content -LiteralPath $recordPath -Raw|ConvertFrom-Json
        $live=Get-Process -Id $old.windows_pid -ErrorAction SilentlyContinue
        if($live -and [Math]::Abs(($live.StartTime.ToUniversalTime()-[DateTime]::Parse($old.started_at).ToUniversalTime()).TotalMilliseconds) -lt 10){throw 'Existing padding worker is live'}
        if(Test-Path -LiteralPath (Join-Path $runDir 'result.json')){
            $result=Get-Content -LiteralPath (Join-Path $runDir 'result.json') -Raw|ConvertFrom-Json
            if($result.status -eq 'complete'){Write-Output 'Completed padding worker retained';exit 0}
        }
    }
    $taskArgs=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Worker')
    $process=Start-Process powershell.exe -ArgumentList $taskArgs -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    [IO.File]::WriteAllText($recordPath,(@{windows_pid=$process.Id;started_at=$process.StartTime.ToUniversalTime().ToString('o')}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started durable padding worker '+$process.Id);exit 0
}
Set-Location -LiteralPath $workspace
$prefix=@('-d','Ubuntu','--cd',$linuxRepo,'--','/home/aihub_ubuntu/.local/bin/uv','run','--frozen','--extra','hub','--extra','data','--extra','ml','--extra','export')
$command=@('scripts/chat_generalization_padding.py','--mode','gpu')
$result=@{started_at=[DateTime]::UtcNow.ToString('o');status='starting'}
$uiStopped=$false
try {
    & wsl.exe @prefix @command --inspect
    if($LASTEXITCODE -ne 0){throw 'Padding CPU contract preflight failed'}
    & wsl.exe @prefix scripts/check_chat_generalization_launch.py
    if($LASTEXITCODE -ne 0){throw 'Current process/UI/lock/capacity launch gate failed'}
    $serverPath=Join-Path $linuxCopy 'reports/local/webui/server.json'
    if(Test-Path -LiteralPath $serverPath){
        $server=Get-Content -LiteralPath $serverPath -Raw|ConvertFrom-Json
        if($server.status -eq 'running'){
            & powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'stop_webui.ps1')
            if($LASTEXITCODE -ne 0){throw 'Original UI identity stop failed'}
            $uiStopped=$true
        }
    }
    & wsl.exe @prefix @command
    $result.exit_code=$LASTEXITCODE
    if($LASTEXITCODE -ne 0){throw 'Padding GPU diagnostic failed; inspect original records before retry'}
    $result.status='complete'
} catch {$result.status='failed';$result.error=$_.Exception.Message}
finally {
    if($uiStopped){
        & powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'start_webui.ps1')
        $result.original_UI_restore_exit_code=$LASTEXITCODE
        if($LASTEXITCODE -ne 0){$result.status='failed';$result.UI_restore_error='Inspect original UI state and logs'}
    }
    $result.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
}
if($result.status -ne 'complete'){exit 1}
