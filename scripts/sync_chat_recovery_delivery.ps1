param()
$ErrorActionPreference='Stop'
$workspace=Split-Path -Parent $PSScriptRoot
$linuxMirror='\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m'
$relative='reports/phase7/chat-recovery-20261018'
$scientificRun='input-structure-main'
$completion=Get-Content -LiteralPath (Join-Path $linuxMirror "$relative/$scientificRun/completion.json") -Raw|ConvertFrom-Json -Depth 100
if($completion.status -ne 'four_requested_steps_complete'){throw 'Full four-step evidence must pass before final delivery'}
$portable=@()
function Shared-Read-Digest([string]$Path){
    $stream=[IO.File]::Open($Path,[IO.FileMode]::Open,[IO.FileAccess]::Read,([IO.FileShare]::ReadWrite -bor [IO.FileShare]::Delete))
    $hasher=[Security.Cryptography.SHA256]::Create()
    try{return ([BitConverter]::ToString($hasher.ComputeHash($stream))).Replace('-','').ToLowerInvariant()}
    finally{$hasher.Dispose();$stream.Dispose()}
}
$sourceRoot=Join-Path $linuxMirror $relative
foreach($file in Get-ChildItem -LiteralPath $sourceRoot -Recurse -File){
    if($file.Extension -notin @('.json','.jsonl','.tsv','.csv','.png','.txt','.log','.xml','.py','.ps1')){continue}
    $suffix=$file.FullName.Substring($sourceRoot.Length).TrimStart('\','/')
    if($suffix -eq "$scientificRun/delivery.json" -or $suffix -eq "$scientificRun\delivery.json"){continue}
    $destination=Join-Path (Join-Path $workspace $relative) $suffix
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $destination)|Out-Null
    Copy-Item -LiteralPath $file.FullName -Destination $destination
    $left=Shared-Read-Digest $file.FullName
    $right=Shared-Read-Digest $destination
    if($left -ne $right){throw "Portable bytes differ: $suffix"}
    $portable+=@{relative_path="$relative/$suffix";sha256=$left;bytes=$file.Length;shared_read=$true}
}
Set-Location -LiteralPath $workspace
$config=Get-Content -LiteralPath configs/phase7/chat-input-structure-20261018.json -Raw|ConvertFrom-Json -Depth 100
$aux=@(git ls-files scripts | Where-Object {$_ -match '(chat_recovery|chat_recovery_sft|chat_recovery_browser)'})
$critical=@($config.source_sha256.PSObject.Properties.Name)+$aux+@('docs/160_chat_input_structure_sft_comparison.md','configs/phase7/chat-input-structure-20261018.json')
$sources=@()
foreach($name in ($critical|Select-Object -Unique)){
    $left=(Get-FileHash -LiteralPath (Join-Path $workspace $name)).Hash.ToLowerInvariant()
    $right=(Get-FileHash -LiteralPath (Join-Path $linuxMirror $name)).Hash.ToLowerInvariant()
    if($left -ne $right){throw "Windows/WSL source differs: $name"}
    $raw=git hash-object --no-filters -- $name
    if($LASTEXITCODE -ne 0){throw "Cannot hash actual source: $name"}
    $staged=git rev-parse ":$name"
    if($LASTEXITCODE -ne 0 -or $raw -ne $staged){throw "Git index does not preserve actual source bytes: $name"}
    $sources+=@{path=$name;sha256=$left;Git_blob=$raw;Windows_WSL_Git_bytes_exact=$true}
}
$target=Join-Path $workspace "$relative/$scientificRun/delivery.json"
if(Test-Path -LiteralPath $target){throw 'Delivery receipt already exists; keep it immutable'}
$value=@{status='all_portable_evidence_and_critical_source_bytes_verified';created_at=[DateTime]::UtcNow.ToString('o');completion_sha256=(Get-FileHash -LiteralPath (Join-Path $workspace "$relative/$scientificRun/completion.json")).Hash.ToLowerInvariant();portable=$portable;critical_sources=$sources;weights_Adam_RNG_sampler_remain_in_WSL=$true;model_training_or_generation_by_this_check=$false;source_sha256=(Get-FileHash -LiteralPath $PSCommandPath).Hash.ToLowerInvariant()}
[IO.File]::WriteAllText($target,($value|ConvertTo-Json -Depth 100),[Text.UTF8Encoding]::new($false))
Copy-Item -LiteralPath $target -Destination (Join-Path $linuxMirror "$relative/$scientificRun/delivery.json")
Write-Output "Verified $($portable.Count) portable artifacts and $($sources.Count) critical source files. Full numerical states remain in WSL."
