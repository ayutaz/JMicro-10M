param([string]$Tag='')
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$root=Join-Path $workspace 'reports/phase7/chat-lr-20261014-launcher'
$rows=@()
foreach($file in (Get-ChildItem -LiteralPath $root -Recurse -File -Filter launcher.json)) {
    if($Tag -and $file.Directory.Name -ne $Tag){continue}
    $record=Get-Content -Raw -LiteralPath $file.FullName | ConvertFrom-Json
    $process=Get-Process -Id $record.windows_pid -ErrorAction SilentlyContinue
    $expected=([DateTime]$record.started_at).ToUniversalTime()
    $live=$false
    $actual=$null
    if($process){$actual=$process.StartTime.ToUniversalTime();$live=$actual.Ticks -eq $expected.Ticks}
    $resultPath=Join-Path $file.Directory.FullName 'result.json'
    $terminal=$null
    if(Test-Path -LiteralPath $resultPath){$terminal=Get-Content -Raw -LiteralPath $resultPath|ConvertFrom-Json}
    $rows += [ordered]@{tag=$file.Directory.Name;pid=$record.windows_pid;record_start_ticks=$expected.Ticks;actual_start_ticks=if($actual){$actual.Ticks}else{$null};currently_alive_with_same_birth=$live;terminal_result=$terminal}
}
$output=[ordered]@{observed_at=[DateTime]::UtcNow.ToString('o');observer='Windows PID and exact UTC ticks; avoids PS7 automatic-DateTime/string comparison';workers=$rows;goal_complete=$false}
$directory=Join-Path $workspace 'reports/phase7/chat-lr-20261014/windows_observations'
New-Item -ItemType Directory -Force -Path $directory|Out-Null
$name='observation-'+[DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfffffff')+'.json'
[IO.File]::WriteAllText((Join-Path $directory $name),($output|ConvertTo-Json -Depth 7)+"`n",[Text.UTF8Encoding]::new($false))
$output|ConvertTo-Json -Depth 7
