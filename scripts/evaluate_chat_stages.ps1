param(
    [Parameter(Mandatory=$true)][ValidatePattern('^[A-Za-z0-9_./-]+\.json$')][string]$SftConfig,
    [Parameter(Mandatory=$true)][ValidateSet('base','mid-training','sft')][string]$Stage,
    [ValidateSet('greedy','sampling')][string]$Decoding='greedy',
    [Parameter(Mandatory=$true)][ValidatePattern('^[A-Za-z0-9_./-]+$')][string]$Output,
    [switch]$Worker
)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$configPath=[IO.Path]::GetFullPath((Join-Path $workspace $SftConfig))
$configRoot=[IO.Path]::GetFullPath((Join-Path $workspace 'configs\phase7'))+[IO.Path]::DirectorySeparatorChar
$outputPath=[IO.Path]::GetFullPath((Join-Path $workspace $Output))
$reportRoot=[IO.Path]::GetFullPath((Join-Path $workspace 'reports\phase7'))+[IO.Path]::DirectorySeparatorChar
if (-not $configPath.StartsWith($configRoot,[StringComparison]::OrdinalIgnoreCase) -or -not $outputPath.StartsWith($reportRoot,[StringComparison]::OrdinalIgnoreCase)) { throw 'Use configs/phase7 and reports/phase7 paths.' }
if (-not (Test-Path -LiteralPath $configPath)) { throw 'Frozen adopted-Base SFT recipe is missing.' }
$runDir=$outputPath+'-launcher'
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if (-not $Worker) {
    $record=Join-Path $runDir 'launcher.json'
    if (Test-Path -LiteralPath $record) { throw 'Inspect actual process and saved cases before resuming with -Worker.' }
    $argsList=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-SftConfig',$SftConfig,'-Stage',$Stage,'-Decoding',$Decoding,'-Output',$Output,'-Worker')
    $process=Start-Process powershell.exe -ArgumentList $argsList -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    [IO.File]::WriteAllText($record,(@{windows_pid=$process.Id;started_at=$process.StartTime.ToUniversalTime().ToString('o');config=$SftConfig;stage=$Stage;decoding=$Decoding;output=$Output}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started durable stage evaluation worker '+$process.Id);exit 0
}
Set-Location -LiteralPath $workspace
$result=@{started_at=[DateTime]::UtcNow.ToString('o');status='starting';config=$SftConfig;stage=$Stage;decoding=$Decoding}
$uiStopped=$false
$evalArgs=@('run','--frozen','--extra','hub','--extra','data','--extra','ml','--extra','export','scripts/evaluate_chat_stages.py','--sft-config',$SftConfig,'--stage',$Stage,'--decoding',$Decoding,'--output',$Output)
try {
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv @evalArgs --inspect
    if ($LASTEXITCODE -ne 0) { throw 'Stage/checkpoint preflight failed before UI/GPU changes.' }
    & (Join-Path $PSScriptRoot 'stop_webui.ps1');$uiStopped=$true
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv @evalArgs
    $result.exit_code=$LASTEXITCODE;$result.status=if($LASTEXITCODE -eq 0){'complete'}else{'failed'}
} catch {$result.status='failed';$result.error=$_.Exception.Message}
finally {
    $result.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    if ($uiStopped) { & (Join-Path $PSScriptRoot 'start_webui.ps1') }
}
