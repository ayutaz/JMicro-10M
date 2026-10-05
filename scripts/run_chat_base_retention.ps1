param(
    [Parameter(Mandatory=$true)][ValidatePattern('^[A-Za-z0-9_./-]+\.json$')][string]$SftConfig,
    [ValidatePattern('^[A-Za-z0-9_./-]+\.json$')][string]$ReferenceConfig='configs/phase6/amount_learning_comparison.json',
    [Parameter(Mandatory=$true)][ValidateSet('mid-training','sft')][string]$Stage,
    [Parameter(Mandatory=$true)][ValidatePattern('^[A-Za-z0-9_./-]+$')][string]$Output,
    [switch]$Worker
)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
foreach ($entry in @(@($SftConfig,'configs\phase7'),@($ReferenceConfig,'configs\phase6'),@($Output,'reports\phase7'))) {
    $resolved=[IO.Path]::GetFullPath((Join-Path $workspace $entry[0]))
    $root=[IO.Path]::GetFullPath((Join-Path $workspace $entry[1]))+[IO.Path]::DirectorySeparatorChar
    if (-not $resolved.StartsWith($root,[StringComparison]::OrdinalIgnoreCase)) { throw 'Use repository configs/phase7, configs/phase6 and reports/phase7 paths.' }
}
if (-not (Test-Path -LiteralPath (Join-Path $workspace $SftConfig)) -or -not (Test-Path -LiteralPath (Join-Path $workspace $ReferenceConfig))) { throw 'Frozen adopted-Base and native reference recipes are required.' }
$runDir=(Join-Path $workspace $Output)+'-launcher'
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if (-not $Worker) {
    $record=Join-Path $runDir 'launcher.json'
    if (Test-Path -LiteralPath $record) { throw 'Inspect actual evaluation process before resuming with -Worker.' }
    $argsList=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-SftConfig',$SftConfig,'-ReferenceConfig',$ReferenceConfig,'-Stage',$Stage,'-Output',$Output,'-Worker')
    $process=Start-Process powershell.exe -ArgumentList $argsList -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    [IO.File]::WriteAllText($record,(@{windows_pid=$process.Id;started_at=$process.StartTime.ToUniversalTime().ToString('o');config=$SftConfig;stage=$Stage;output=$Output}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started durable Base retention evaluation '+$process.Id);exit 0
}
Set-Location -LiteralPath $workspace
$result=@{started_at=[DateTime]::UtcNow.ToString('o');status='starting';config=$SftConfig;stage=$Stage}
$uiStopped=$false
$evalArgs=@('run','--frozen','--extra','hub','--extra','data','--extra','ml','--extra','export','scripts/run_chat_base_retention.py','--sft-config',$SftConfig,'--reference-config',$ReferenceConfig,'--stage',$Stage,'--output',$Output)
try {
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv @evalArgs --inspect
    if ($LASTEXITCODE -ne 0) { throw 'Retention preflight rejected control/source/shape before UI/GPU changes.' }
    & (Join-Path $PSScriptRoot 'stop_webui.ps1');$uiStopped=$true
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv @evalArgs
    $result.exit_code=$LASTEXITCODE;$result.status=if($LASTEXITCODE -eq 0){'complete'}else{'failed'}
} catch {$result.status='failed';$result.error=$_.Exception.Message}
finally {
    $result.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    if ($uiStopped) { & (Join-Path $PSScriptRoot 'start_webui.ps1') }
}
