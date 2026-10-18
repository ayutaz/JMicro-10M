$ErrorActionPreference='Stop'
$workspace=(Resolve-Path (Split-Path -Parent $PSScriptRoot)).Path
$linuxRoot='\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m'
$relative='reports/phase7/chat-two-attribute-20261018'
$sourceRun=Join-Path $linuxRoot $relative
$targetRun=Join-Path $workspace $relative
if(Test-Path -LiteralPath (Join-Path $targetRun 'delivery.json')){throw 'Completed delivery receipt already exists; inspect instead of overwriting.'}
function SharedHash([string]$path){
    $stream=[IO.File]::Open($path,[IO.FileMode]::Open,[IO.FileAccess]::Read,([IO.FileShare]::ReadWrite -bor [IO.FileShare]::Delete))
    $sha=[Security.Cryptography.SHA256]::Create()
    try{return ([Convert]::ToHexString($sha.ComputeHash($stream))).ToLowerInvariant()}finally{$sha.Dispose();$stream.Dispose()}
}
function SharedCopy([string]$source,[string]$target){
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $target)|Out-Null
    $inputStream=[IO.File]::Open($source,[IO.FileMode]::Open,[IO.FileAccess]::Read,([IO.FileShare]::ReadWrite -bor [IO.FileShare]::Delete))
    try{$outputStream=[IO.File]::Open($target,[IO.FileMode]::Create,[IO.FileAccess]::Write,[IO.FileShare]::Read);try{$inputStream.CopyTo($outputStream)}finally{$outputStream.Dispose()}}finally{$inputStream.Dispose()}
}
$config=Get-Content (Join-Path $linuxRoot 'configs/phase7/chat-two-attribute-20261018.json') -Raw|ConvertFrom-Json
$terminal=Get-Content (Join-Path $targetRun 'windows_terminal_observation.json') -Raw|ConvertFrom-Json
if(-not $terminal.matching_worker_absent -or $terminal.launcher_result.exit_code -ne 0){throw 'Matching worker terminal proof required.'}
$current=Get-CimInstance Win32_Process -Filter "ProcessId=$($terminal.expected_worker.windows_pid)"
if($null -ne $current -and $current.CreationDate.ToUniversalTime() -eq ([DateTime]$terminal.expected_worker.started_at).ToUniversalTime()){throw 'Original worker remains live.'}
$data='\\wsl.localhost\Ubuntu\home\aihub_ubuntu\jmicro-data\phase7\chat-two-attribute-20261018'
foreach($file in Get-ChildItem -LiteralPath $data -File){
    $target=Join-Path $sourceRun ('data_snapshot/'+$file.Name)
    if(Test-Path -LiteralPath $target){if((SharedHash $file.FullName) -ne (SharedHash $target)){throw 'Existing authored data snapshot differs.'}}else{SharedCopy $file.FullName $target}
}
foreach($name in 'stdout.log','stderr.log','launcher.json','result.json'){
    $target=Join-Path $sourceRun ('launcher_snapshot/'+$name)
    if(-not(Test-Path -LiteralPath $target)){SharedCopy (Join-Path $targetRun ('launcher/'+$name)) $target}
}
$files=@()
foreach($file in Get-ChildItem -LiteralPath $sourceRun -File -Recurse){
    if($file.Extension -in '.pt','.npz','.bin','.safetensors' -or $file.FullName -match '__pycache__'){continue}
    $rel=[IO.Path]::GetRelativePath($sourceRun,$file.FullName).Replace('\','/')
    $target=Join-Path $targetRun $rel
    SharedCopy $file.FullName $target
    $hash=SharedHash $file.FullName
    if($hash -ne (SharedHash $target)){throw "Portable bytes differ: $rel"}
    $files+=@{relative=$rel;sha256=$hash;bytes=$file.Length}
}
$configRelative='configs/phase7/chat-two-attribute-20261018.json'
SharedCopy (Join-Path $linuxRoot $configRelative) (Join-Path $workspace $configRelative)
$critical=@()
foreach($p in $config.source_sha256.PSObject.Properties){
    $win=Join-Path $workspace $p.Name;$linux=Join-Path $linuxRoot $p.Name
    if((SharedHash $win) -ne $p.Value -or (SharedHash $linux) -ne $p.Value){throw "Critical source differs: $($p.Name)"}
    $critical+=@{relative=$p.Name;sha256=$p.Value}
}
if((SharedHash (Join-Path $linuxRoot $configRelative)) -ne (SharedHash (Join-Path $workspace $configRelative))){throw 'Config bytes differ'}
$receipt=@{created_at=[DateTime]::UtcNow.ToString('o');portable_files=$files;critical_sources=$critical;source_script='scripts/sync_two_attribute_delivery.ps1';
    config_sha256=(SharedHash (Join-Path $workspace $configRelative));all_Windows_WSL_bytes_equal=$true;weights_Adam_RNG_sampler_remain_WSL=$true;
    launcher_logs='Observed terminal log bytes, copied with shared read access; original Windows logs preserved';completion_sha256=(SharedHash (Join-Path $targetRun 'completion.json'))}
[IO.File]::WriteAllText((Join-Path $targetRun 'delivery.json'),($receipt|ConvertTo-Json -Depth 12),[Text.UTF8Encoding]::new($false))
SharedCopy (Join-Path $targetRun 'delivery.json') (Join-Path $sourceRun 'delivery.json')
Write-Output "Delivered $($files.Count) portable artifacts; $($critical.Count) critical source hashes exact. Model states remain in WSL."
