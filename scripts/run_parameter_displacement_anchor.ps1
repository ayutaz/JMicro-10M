param([ValidateSet('Probe','Train')][string]$Mode='Probe',[switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$runDir=Join-Path $workspace ('reports\phase6\parameter-displacement-anchor-'+$Mode.ToLower()+'-launcher-20261006')
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if(-not $Worker){
    if(Test-Path -LiteralPath (Join-Path $runDir 'launcher.json')){throw 'Inspect actual process before resuming with -Worker.'}
    $arguments=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Mode',$Mode,'-Worker')
    $process=Start-Process powershell.exe -ArgumentList $arguments -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    [IO.File]::WriteAllText((Join-Path $runDir 'launcher.json'),(@{windows_pid=$process.Id;started_at=$process.StartTime.ToUniversalTime().ToString('o');mode=$Mode}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started durable parameter anchor '+$Mode+' worker '+$process.Id);exit 0
}
$result=@{status='starting';mode=$Mode;started_at=[DateTime]::UtcNow.ToString('o')};$uiStopped=$false
try{
    $preflight=if($Mode -eq 'Probe'){'--preflight-probe'}else{'--inspect'}
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_parameter_displacement_anchor.py $preflight
    if($LASTEXITCODE -ne 0){throw 'Parameter anchor preflight rejected before UI/GPU changes.'}
    $jobPath='\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m\reports\phase6\parameter-displacement-anchor-20261006'
    if($Mode -eq 'Probe'){$jobPath=Join-Path $jobPath 'probe'}
    $jobPath=Join-Path $jobPath 'job.json'
    if((Test-Path -LiteralPath $jobPath) -and ((Get-Content -Raw -LiteralPath $jobPath|ConvertFrom-Json).status -eq 'complete')){
        $result.status='already_complete';return
    }
    $uiStopped=$true
    & (Join-Path $PSScriptRoot 'stop_webui.ps1')
    if($LASTEXITCODE -ne 0){throw 'UI stop rejected.'}
    if($Mode -eq 'Probe'){
        & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_parameter_displacement_anchor.py --probe
    }else{
        & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_parameter_displacement_anchor.py
    }
    $result.exit_code=$LASTEXITCODE;$result.status=if($LASTEXITCODE -eq 0){'complete'}else{'failed'}
}catch{$result.status='failed';$result.error=$_.Exception.Message}
finally{
    $result.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    if($uiStopped){& (Join-Path $PSScriptRoot 'start_webui.ps1')}
}
if($result.status -eq 'failed'){exit 1}
