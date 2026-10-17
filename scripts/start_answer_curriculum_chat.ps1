param([ValidateSet('C0','C1')][string]$Arm='C1',[int]$Port=0)
$ErrorActionPreference='Stop'
if($Port -eq 0){$Port=if($Arm -eq 'C1'){7864}else{7865}}
if($Port -lt 1024 -or $Port -gt 65535){throw 'Invalid port'}
$workspace=Split-Path -Parent $PSScriptRoot
$linuxRepo='/home/aihub_ubuntu/src/japanese-tiny-llm-10m'
$mirror='\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m'
$configSHA='e9172f65215fe44f2a94f5c0e9f1429175a27917b3d32b3e09c848cb318e9e46'
try{
    $model=Invoke-RestMethod "http://127.0.0.1:$Port/api/model" -TimeoutSec 2
    if($model.config_sha256 -eq $configSHA -and $model.arm -eq $Arm){Write-Output "Already running: http://127.0.0.1:$Port";exit 0}
    throw 'Another service occupies this port'
}catch [System.Net.Http.HttpRequestException]{}catch [System.OperationCanceledException]{}catch [System.Net.WebException]{}
$runDir=Join-Path $workspace "reports/local/chat-answer-$Arm"
New-Item -ItemType Directory -Force -Path $runDir|Out-Null
Copy-Item -LiteralPath (Join-Path $PSScriptRoot 'answer_curriculum_chat_demo.py') -Destination "$mirror/scripts/answer_curriculum_chat_demo.py"
$arguments=@('-d','Ubuntu','--cd',$linuxRepo,'--','/home/aihub_ubuntu/.local/bin/uv','run','--frozen','--extra','hub','--extra','data','--extra','ml','--extra','export','scripts/answer_curriculum_chat_demo.py','--arm',$Arm,'--port',"$Port")
$tag=[DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfff')
$stdout=Join-Path $runDir "stdout-$tag.log";$stderr=Join-Path $runDir "stderr-$tag.log"
$worker=Start-Process wsl.exe -ArgumentList $arguments -WindowStyle Hidden -PassThru -RedirectStandardOutput $stdout -RedirectStandardError $stderr
@{windows_pid=$worker.Id;started_at=$worker.StartTime.ToUniversalTime().ToString('o');arm=$Arm;url="http://127.0.0.1:$Port";stdout=$stdout;stderr=$stderr;CPU_only=$true}|ConvertTo-Json|Set-Content (Join-Path $runDir 'launcher.json') -Encoding utf8
for($attempt=0;$attempt -lt 40;$attempt++){
    Start-Sleep -Seconds 1;$worker.Refresh();if($worker.HasExited){throw "New trial UI exited; inspect $stderr"}
    try{
        $model=Invoke-RestMethod "http://127.0.0.1:$Port/api/model" -TimeoutSec 1
        if($model.config_sha256 -eq $configSHA -and $model.arm -eq $Arm){Write-Output "Ready: http://127.0.0.1:$Port ($Arm / CPU / default32)";exit 0}
    }catch [System.Net.Http.HttpRequestException]{}catch [System.OperationCanceledException]{}catch [System.Net.WebException]{}
}
throw 'UI observation timeout. Inspect this same saved process; do not blindly restart.'
