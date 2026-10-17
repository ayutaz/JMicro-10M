param([ValidateSet('C0','C1')][string]$Arm='C1',[int]$Port=0)
$ErrorActionPreference='Stop'
if($Port -eq 0){$Port=if($Arm -eq 'C1'){7866}else{7867}}
if($Port -notin @(7866,7867)){throw 'Only dedicated new CPU ports are allowed'}
$workspace=Split-Path -Parent $PSScriptRoot
$linuxRepo='/home/aihub_ubuntu/src/japanese-tiny-llm-10m'
$configSHA='29a5fa2541f321a8de26f4f54ee98879bfc2245f232ebfe5246d09069d65f075'
try{
    $model=Invoke-RestMethod "http://127.0.0.1:$Port/api/model" -TimeoutSec 2
    if($model.config_sha256 -eq $configSHA -and $model.arm -eq $Arm){Write-Output "Already running: http://127.0.0.1:$Port";exit 0}
    throw 'Another service occupies the port'
}catch [System.Net.Http.HttpRequestException]{}catch [System.OperationCanceledException]{}catch [System.Net.WebException]{}
$runDir=Join-Path $workspace "reports/local/chat-input-structure-$Arm"
New-Item -ItemType Directory -Path $runDir -Force | Out-Null
if(Test-Path (Join-Path $runDir 'launcher.json')){throw 'Prior launch exists; inspect its actual process before any new start'}
$arguments=@('-d','Ubuntu','--cd',$linuxRepo,'--','/home/aihub_ubuntu/.local/bin/uv','run','--frozen','--extra','hub','--extra','data','--extra','ml','--extra','export','scripts/chat_recovery_demo.py','--arm',$Arm,'--port',"$Port")
$tag=[DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfff')
$stdout=Join-Path $runDir "stdout-$tag.log";$stderr=Join-Path $runDir "stderr-$tag.log"
$ownedProcess=Start-Process wsl.exe -ArgumentList $arguments -WindowStyle Hidden -PassThru -RedirectStandardOutput $stdout -RedirectStandardError $stderr
@{windows_pid=$ownedProcess.Id;started_at=$ownedProcess.StartTime.ToUniversalTime().ToString('o');arm=$Arm;url="http://127.0.0.1:$Port";stdout=$stdout;stderr=$stderr;CPU_only=$true}|ConvertTo-Json|Set-Content (Join-Path $runDir 'launcher.json') -Encoding utf8
for($attempt=0;$attempt -lt 40;$attempt++){
    Start-Sleep -Seconds 1;$ownedProcess.Refresh();if($ownedProcess.HasExited){throw "New CPU UI exited; inspect $stderr"}
    try{
        $model=Invoke-RestMethod "http://127.0.0.1:$Port/api/model" -TimeoutSec 1
        if($model.config_sha256 -eq $configSHA -and $model.arm -eq $Arm){Write-Output "Ready: http://127.0.0.1:$Port ($Arm / CPU / default32)";exit 0}
    }catch [System.Net.Http.HttpRequestException]{}catch [System.OperationCanceledException]{}catch [System.Net.WebException]{}
}
throw 'Observation timeout: inspect this SAME saved process; never assume exit or relaunch'
