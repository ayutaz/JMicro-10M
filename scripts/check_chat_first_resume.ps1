param([Parameter(Mandatory=$true)][ValidatePattern('^[A-Za-z0-9_./-]+\.json$')][string]$Config,[switch]$Worker)
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$configPath=[IO.Path]::GetFullPath((Join-Path $workspace $Config))
$configRoot=[IO.Path]::GetFullPath((Join-Path $workspace 'configs\phase7'))+[IO.Path]::DirectorySeparatorChar
if (-not $configPath.StartsWith($configRoot,[StringComparison]::OrdinalIgnoreCase)) { throw 'Use a repository configs/phase7 JSON recipe.' }
if (-not (Test-Path -LiteralPath $configPath)) { throw 'Frozen SFT recipe is missing; prepare diagnostic/data evidence first.' }
$stem=[IO.Path]::GetFileNameWithoutExtension($configPath)+'-resume-gate'
$runDir=Join-Path $workspace ('reports\phase7\'+$stem+'-launcher')
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
if (-not $Worker) {
    $record=Join-Path $runDir 'launcher.json'
    if (Test-Path -LiteralPath $record) { throw 'Inspect actual SFT process/checkpoint before resuming with -Worker.' }
    $argsList=@('-NoProfile','-ExecutionPolicy','Bypass','-File',('"'+$PSCommandPath+'"'),'-Config',$Config,'-Worker')
    $process=Start-Process powershell.exe -ArgumentList $argsList -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'stderr.log')
    [IO.File]::WriteAllText($record,(@{windows_pid=$process.Id;started_at=$process.StartTime.ToUniversalTime().ToString('o');config=$Config}|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    Write-Output ('Started durable SFT worker '+$process.Id);exit 0
}
Set-Location -LiteralPath $workspace
$result=@{started_at=[DateTime]::UtcNow.ToString('o');status='starting';config=$Config}
$uiStopped=$false
try {
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/check_chat_first_resume.py --config $Config --inspect
    if ($LASTEXITCODE -ne 0) { throw 'SFT preflight rejected the recipe before UI/GPU changes.' }
    & (Join-Path $PSScriptRoot 'stop_webui.ps1');$uiStopped=$true
    & wsl.exe -d Ubuntu --cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m -- /home/aihub_ubuntu/.local/bin/uv run --frozen --extra hub --extra data --extra ml --extra export scripts/check_chat_first_resume.py --config $Config
    $result.exit_code=$LASTEXITCODE;$result.status=if($LASTEXITCODE -eq 0){'complete'}else{'failed'}
} catch {$result.status='failed';$result.error=$_.Exception.Message}
finally {
    $result.ended_at=[DateTime]::UtcNow.ToString('o')
    [IO.File]::WriteAllText((Join-Path $runDir 'result.json'),($result|ConvertTo-Json),[Text.UTF8Encoding]::new($false))
    if ($uiStopped) { & (Join-Path $PSScriptRoot 'start_webui.ps1') }
}
