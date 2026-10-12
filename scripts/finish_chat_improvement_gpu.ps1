param([switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$runDir=Join-Path $workspace 'reports/phase7/chat-improvement-20261012-launcher/remainder-chain'
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
$recordPath=Join-Path $runDir 'launcher.json'
if(-not $Worker){
    if(Test-Path -LiteralPath $recordPath){
        $prior=Get-Content -LiteralPath $recordPath -Raw | ConvertFrom-Json
        $process=Get-Process -Id $prior.windows_pid -ErrorAction SilentlyContinue
        if($process -and $process.StartTime.ToUniversalTime().ToString('o') -eq $prior.started_at){throw 'Remainder chain already alive'}
        throw 'Existing remainder chain retained; inspect its result before any retry'
    }
    $argsList=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Worker')
    $process=Start-Process powershell.exe -ArgumentList $argsList -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    [IO.File]::WriteAllText($recordPath,(@{windows_pid=$process.Id;started_at=$process.StartTime.ToUniversalTime().ToString('o');source_sha256=(Get-FileHash -Algorithm SHA256 $PSCommandPath).Hash.ToLowerInvariant()}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started remaining-GPU chain '+$process.Id);exit 0
}
Set-Location -LiteralPath $workspace
$linuxRepo='/home/aihub_ubuntu/src/japanese-tiny-llm-10m'
$prefix=@('-d','Ubuntu','--cd',$linuxRepo,'--','/home/aihub_ubuntu/.local/bin/uv','run','--frozen','--extra','hub','--extra','data','--extra','ml','--extra','export')
$result=@{started_at=[DateTime]::UtcNow.ToString('o');status='waiting_existing_training';quality_or_adoption_complete=$false}
function Wait-RecordedWorker([string]$tag){
    $directory=Join-Path $workspace ('reports/phase7/chat-improvement-20261012-launcher/'+$tag)
    $launcher=Get-Content -LiteralPath (Join-Path $directory 'launcher.json') -Raw | ConvertFrom-Json
    while($true){
        $process=Get-Process -Id $launcher.windows_pid -ErrorAction SilentlyContinue
        $live=$process -and $process.StartTime.ToUniversalTime().ToString('o') -eq $launcher.started_at
        if(-not $live){
            $path=Join-Path $directory 'result.json'
            if(-not (Test-Path -LiteralPath $path)){throw "Recorded $tag worker ended without final result"}
            $ended=Get-Content -LiteralPath $path -Raw | ConvertFrom-Json
            if([DateTime]$ended.started_at -lt [DateTime]$launcher.started_at){throw "Stale result for $tag"}
            if($ended.status -ne 'complete' -or $ended.exit_code -ne 0 -or $ended.original_UI_restore_exit_code -ne 0){throw "Recorded $tag failed; exact logs/state retained, automatic retry refused"}
            return
        }
        Start-Sleep -Seconds 2
    }
}
try{
    Wait-RecordedWorker 'train-both-3-t0'
    $result.status='training_audits'
    foreach($arm in @('C0','C1')){
        & wsl.exe @prefix scripts/audit_chat_improvement_training.py --arm $arm
        if($LASTEXITCODE -ne 0){throw "Full-state/consumption audit failed for $arm; no further GPU evaluation"}
    }
    foreach($arm in @('C0','C1')){
        $result.status="evaluating-$arm"
        & powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot 'run_chat_improvement.ps1') -Mode evaluate -Arm $arm -Point all
        if($LASTEXITCODE -ne 0){throw "Frozen evaluation launch failed for $arm"}
        Wait-RecordedWorker "evaluate-$arm-1-all"
    }
    $result.status='GPU_generation_and_training_audits_complete_pending_all_reviews'
    $result.exit_code=0
}catch{$result.status='failed';$result.error=$_.Exception.Message;$result.exit_code=1}
finally{
    $result.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
}
exit $result.exit_code
