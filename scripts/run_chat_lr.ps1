param(
    [Parameter(Mandatory=$true)][ValidateSet('probe','resume','forecast','train','evaluate')][string]$Mode,
    [ValidateSet('both','parent','S0','S1')][string]$Arm='both',
    [ValidateSet(1,2,3)][int]$Until=1,
    [ValidateSet('t0','t1','t2','t3','all')][string]$Point='t0',
    [ValidateSet('greedy','sampling')][string]$Decoding='greedy',
    [switch]$Worker
)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$config='configs/phase7/chat-lr-20261014.json'
$linuxRepo='/home/aihub_ubuntu/src/japanese-tiny-llm-10m'
$linuxCopy='\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m'
$tag="$Mode-$Arm-$Until-$Point-$Decoding"
$runDir=Join-Path $workspace "reports\phase7\chat-lr-20261014-launcher\$tag"
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if (-not $Worker) {
    $recordPath=Join-Path $runDir 'launcher.json'
    if (Test-Path -LiteralPath $recordPath) {
        $old=Get-Content -LiteralPath $recordPath -Raw | ConvertFrom-Json
        $live=Get-Process -Id $old.windows_pid -ErrorAction SilentlyContinue
        if ($live -and $live.StartTime.ToUniversalTime().ToString('o') -eq $old.started_at) {throw 'Recorded worker is still alive; duplicate launch refused.'}
        if (Test-Path -LiteralPath (Join-Path $runDir 'result.json')) {
            $result=Get-Content -LiteralPath (Join-Path $runDir 'result.json') -Raw | ConvertFrom-Json
            if ($result.status -eq 'complete') {Write-Output 'Completed worker retained.';exit 0}
        }
    }
    $argsList=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Mode',$Mode,'-Arm',$Arm,'-Until',"$Until",'-Point',$Point,'-Decoding',$Decoding,'-Worker')
    $process=Start-Process powershell.exe -ArgumentList $argsList -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    [IO.File]::WriteAllText($recordPath,(@{windows_pid=$process.Id;started_at=$process.StartTime.ToUniversalTime().ToString('o');mode=$Mode;arm=$Arm;until=$Until;point=$Point}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started durable worker '+$process.Id);exit 0
}
Set-Location -LiteralPath $workspace
$prefix=@('-d','Ubuntu','--cd',$linuxRepo,'--','/home/aihub_ubuntu/.local/bin/uv','run','--frozen','--extra','hub','--extra','data','--extra','ml','--extra','export')
if ($Mode -in @('forecast','evaluate')) {
    $evalArm=if($Arm -eq 'both'){'parent'}else{$Arm}
    $points=if($Point -eq 'all'){@('t1','t2','t3')}else{@($Point)}
    $command=@('scripts/evaluate_chat_lr.py','--config',$config,'--mode',$Mode,'--arm',$evalArm,'--points')+$points+@('--decoding',$Decoding)
} elseif ($Mode -eq 'retention') {
    $command=@('scripts/run_chat_lr_retention.py','--config',$config)
} else {
    $command=@('scripts/run_chat_lr.py','--config',$config,'--mode',$Mode,'--arm',$Arm,'--until',"$Until")
}
$result=@{started_at=[DateTime]::UtcNow.ToString('o');status='starting';mode=$Mode;arm=$Arm;until=$Until;point=$Point}
$uiStopped=$false
try {
    & wsl.exe @prefix @command --inspect
    if ($LASTEXITCODE -ne 0) {throw 'Frozen contract preflight failed before any UI/GPU change.'}
    & wsl.exe @prefix scripts/inspect_chat_lr_environment.py
    if ($LASTEXITCODE -ne 0) {throw 'Current process/UI/lock/capacity launch gate failed.'}
    $serverPath=Join-Path $linuxCopy 'reports/local/webui/server.json'
    if (Test-Path -LiteralPath $serverPath) {
        $server=Get-Content -LiteralPath $serverPath -Raw | ConvertFrom-Json
        if ($server.status -eq 'running') {
            & powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'stop_webui.ps1')
            if ($LASTEXITCODE -ne 0) {throw 'UI stop did not verify the saved process identity.'}
            $uiStopped=$true
        }
    }
    & wsl.exe @prefix @command
    $result.exit_code=$LASTEXITCODE
    if ($LASTEXITCODE -ne 0) {throw "Native worker failed with exit $LASTEXITCODE; inspect exact checkpoint and logs before resume."}
    $result.status='complete'
} catch {$result.status='failed';$result.error=$_.Exception.Message}
finally {
    if ($uiStopped) {
        & powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'start_webui.ps1')
        $result.original_UI_restore_exit_code=$LASTEXITCODE
        if ($LASTEXITCODE -ne 0) {$result.status='failed';$result.UI_restore_error='Original UI restore failed; inspect server identity/logs before retry.'}
    }
    $result.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
}
if ($result.status -ne 'complete') {exit 1}
