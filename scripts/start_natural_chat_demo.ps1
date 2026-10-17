param([ValidateSet('C0','C1')][string]$Arm='C1',[int]$Port=0)
$ErrorActionPreference='Stop'
if ($Port -eq 0) {$Port=if($Arm -eq 'C1'){7862}else{7863}}
if ($Port -lt 1024 -or $Port -gt 65535) {throw 'Invalid port'}
$workspace=Split-Path -Parent $PSScriptRoot
$linuxRepo='/home/aihub_ubuntu/src/japanese-tiny-llm-10m'
$linuxCopy='\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m'
try {
    $model=Invoke-RestMethod "http://127.0.0.1:$Port/api/model" -TimeoutSec 2
    if ($model.name -eq "JMicro-10M $Arm" -and $model.config_sha256 -eq 'ec0b61b2961ef9294cb840cb86ad6f5ba291ea1c4a0213d0404e9fa87cdb464d') {
        Write-Output "Already running: http://127.0.0.1:$Port";exit 0
    }
    throw 'Another service occupies this port'
} catch [System.Net.Http.HttpRequestException] { } catch [System.OperationCanceledException] { }
$runDir=Join-Path $workspace "reports/local/chat-natural-$Arm"
New-Item -ItemType Directory -Force $runDir | Out-Null
foreach($file in @('scripts/natural_chat_demo.py','src/jmicro/natural_chat_demo.py','src/jmicro/chat_demo.py','webui/chat/index.html','webui/chat/app.js','webui/chat/style.css')) {
    Copy-Item -LiteralPath (Join-Path $workspace $file) -Destination (Join-Path $linuxCopy $file)
}
$arguments=@('-d','Ubuntu','--cd',$linuxRepo,'--','/home/aihub_ubuntu/.local/bin/uv','run','--frozen','--extra','hub','--extra','data','--extra','ml','--extra','export','scripts/natural_chat_demo.py','--arm',$Arm,'--port',"$Port")
$tag=[DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfff')
$stdout=Join-Path $runDir "stdout-$tag.log";$stderr=Join-Path $runDir "stderr-$tag.log"
$worker=Start-Process wsl.exe -ArgumentList $arguments -WindowStyle Hidden -PassThru -RedirectStandardOutput $stdout -RedirectStandardError $stderr
@{windows_pid=$worker.Id;started_at=$worker.StartTime.ToUniversalTime().ToString('o');arm=$Arm;url="http://127.0.0.1:$Port";stdout=$stdout;stderr=$stderr;CPU_only=$true}|ConvertTo-Json|Set-Content (Join-Path $runDir 'launcher.json') -Encoding utf8
for($attempt=0;$attempt -lt 40;$attempt++) {
    Start-Sleep -Seconds 1
    $worker.Refresh();if($worker.HasExited){throw "Trial UI exited; inspect $stderr"}
    try {
        $model=Invoke-RestMethod "http://127.0.0.1:$Port/api/model" -TimeoutSec 1
        if($model.name -eq "JMicro-10M $Arm" -and $model.config_sha256 -eq 'ec0b61b2961ef9294cb840cb86ad6f5ba291ea1c4a0213d0404e9fa87cdb464d') {
            Write-Output "Ready: http://127.0.0.1:$Port ($Arm / CPU / default32)";exit 0
        }
    } catch [System.Net.Http.HttpRequestException] { } catch [System.OperationCanceledException] { }
}
throw "Trial UI startup timed out; inspect $stderr and saved process identity"
