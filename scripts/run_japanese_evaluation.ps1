$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$linuxRoot = '/home/aihub_ubuntu/src/japanese-tiny-llm-10m'
$linuxShare = '\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m'
$runtimeFiles = @('scripts/prepare_japanese_evaluation.py', 'scripts/evaluate_japanese_base.py',
  'src/jmicro/japanese_evaluation.py', 'configs/evaluation/japanese_base_v2.json',
  'schemas/configs/evaluation/japanese_base_v2.schema.json', 'eval/japanese_semantics_v2_1.jsonl')
foreach ($file in $runtimeFiles) {
  $target = Join-Path $linuxShare $file
  [IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($target)) | Out-Null
  [IO.File]::WriteAllText($target, [IO.File]::ReadAllText((Join-Path $repoRoot $file)).Replace("`r`n", "`n"), (New-Object Text.UTF8Encoding($false)))
}
$config = Get-Content (Join-Path $repoRoot 'configs/evaluation/japanese_base_v2.json') -Raw | ConvertFrom-Json
$uiRecordPath = Join-Path $linuxShare 'reports/local/webui/server.json'
$restoreUi = (Test-Path $uiRecordPath) -and ((Get-Content $uiRecordPath -Raw | ConvertFrom-Json).status -eq 'running')
$uvArgs = @('-d','Ubuntu','--cd',$linuxRoot,'--','/home/aihub_ubuntu/.local/bin/uv','run','--frozen',
  '--extra','hub','--extra','data','--extra','ml','--extra','export')
try {
  if ($restoreUi) { & (Join-Path $PSScriptRoot 'stop_webui.ps1') }
  & wsl.exe @uvArgs scripts/prepare_japanese_evaluation.py
  if ($LASTEXITCODE -ne 0) { throw 'Evaluation data preparation failed.' }
  & wsl.exe @uvArgs scripts/evaluate_japanese_base.py --pilot
  if ($LASTEXITCODE -ne 0) { throw 'Evaluation pilot failed; inspect persisted logs/job.' }
  $pilot = Get-Content (Join-Path $linuxShare "$($config.output)/pilot/result.json") -Raw | ConvertFrom-Json
  if (-not $pilot.complete) { throw 'Pilot budget exhausted; full evaluation was not started.' }
  & wsl.exe @uvArgs scripts/evaluate_japanese_base.py
  if ($LASTEXITCODE -ne 0) { throw 'Evaluation failed; saved chunks can be resumed with the same binding.' }
  $result = Get-Content (Join-Path $linuxShare "$($config.output)/full/result.json") -Raw | ConvertFrom-Json
  if (-not $result.complete) { throw 'Evaluation budget exhausted; incomplete results retained.' }
} finally {
  if ($restoreUi) { & (Join-Path $PSScriptRoot 'start_webui.ps1') }
}
