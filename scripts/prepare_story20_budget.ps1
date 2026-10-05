$ErrorActionPreference = 'Stop'
$workspace = Split-Path -Parent $PSScriptRoot
$run = Join-Path $workspace 'reports/phase6/story20-low-lr-10b-500m-20261005'
$job = '\\wsl.localhost\Ubuntu\home\aihub_ubuntu\jmicro-data\phase6\simple-stories-ja-budget-20261005\job.json'
if (Test-Path $job) { throw 'Inspect existing actual builder identity before launching another.' }
[IO.Directory]::CreateDirectory($run) | Out-Null
$uvArgs = @('-d','Ubuntu','--cd','/home/aihub_ubuntu/src/japanese-tiny-llm-10m','--',
  '/home/aihub_ubuntu/.local/bin/uv','run','--frozen','--extra','hub','--extra','data','--extra','ml','--extra','export','scripts/prepare_story20_budget.py')
$process = Start-Process -FilePath wsl.exe -ArgumentList $uvArgs -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $run 'prepare.stdout.log') -RedirectStandardError (Join-Path $run 'prepare.stderr.log')
$record = [ordered]@{windows_pid=$process.Id;started_at=[DateTime]::UtcNow.ToString('o');scope='conditional public train-only story preparation; UI retained';linux_job='/home/aihub_ubuntu/jmicro-data/phase6/simple-stories-ja-budget-20261005/job.json'}
[IO.File]::WriteAllText((Join-Path $workspace 'reports/phase6/story20_budget_data_launch.json'),($record|ConvertTo-Json)+"`n",[Text.UTF8Encoding]::new($false))
$record | ConvertTo-Json
