$ErrorActionPreference='Stop'
Set-StrictMode -Version Latest
$workspace=(Resolve-Path (Split-Path -Parent $PSScriptRoot)).Path
Set-Location -LiteralPath $workspace
$repo='\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m'
$relative='reports/phase7/chat-two-attribute-20261018'
function SharedHash([string]$path){
    $stream=[IO.File]::Open($path,[IO.FileMode]::Open,[IO.FileAccess]::Read,([IO.FileShare]::ReadWrite -bor [IO.FileShare]::Delete))
    $sha=[Security.Cryptography.SHA256]::Create()
    try{return ([Convert]::ToHexString($sha.ComputeHash($stream))).ToLowerInvariant()}finally{$sha.Dispose();$stream.Dispose()}
}
$delivery=Get-Content "$relative/delivery.json" -Raw|ConvertFrom-Json
$portable=@(git ls-files -- $relative|Where-Object {$_ -ne "$relative/Git_staging_verification.json"})
$critical=@($delivery.critical_sources|ForEach-Object relative)+@(git ls-files scripts|Where-Object {$_ -match 'two_attribute'})+@('configs/phase7/chat-two-attribute-20261018.json','docs/164_chat_two_attribute_diagnosis_execution.md','docs/165_chat_two_attribute_diagnosis_results.md','tests/test_two_attribute_scope.py')
$checks=@()
foreach($name in @($portable+$critical|Sort-Object -Unique)){
    $raw=git hash-object --no-filters -- $name
    if($LASTEXITCODE -ne 0){throw "Cannot hash Git bytes: $name"}
    $index=git rev-parse ":$name"
    if($LASTEXITCODE -ne 0 -or $raw -ne $index){throw "Index byte mismatch: $name"}
    $winHash=SharedHash (Join-Path $workspace $name)
    if($winHash.Length -ne 64){throw "Invalid SHA256: $name"}
    $mirrorName=$name
    if($name.StartsWith("$relative/launcher/")){$mirrorName=$name.Replace("$relative/launcher/","$relative/launcher_snapshot/")}
    $mirror=Join-Path $repo $mirrorName
    if(-not(Test-Path -LiteralPath $mirror)){throw "Missing WSL mirror: $name"}
    $wslHash=SharedHash $mirror
    if($winHash -ne $wslHash){throw "WSL byte mismatch: $name"}
    $checks+=@{path=$name;sha256=$winHash;git_blob=$raw;Git_index_bytes_exact=$true;WSL_mirror=$mirrorName;WSL_bytes_exact=$true}
}
$value=@{created_at=[DateTime]::UtcNow.ToString('o');checked=$checks;count=$checks.Count;source_sha256=(SharedHash $PSCommandPath);
    completion_sha256=(SharedHash "$relative/completion.json");delivery_sha256=(SharedHash "$relative/delivery.json");
    weights_in_Git=$false;initial_receipt_rejected='Git_staging_initial_rejected.json; null SHA256 values from non-shared log reads';
    all_actual_bytes_verified_with_shared_read=$true}
[IO.File]::WriteAllText((Join-Path $workspace "$relative/Git_staging_verification.json"),($value|ConvertTo-Json -Depth 12),[Text.UTF8Encoding]::new($false))
Copy-Item -LiteralPath "$relative/Git_staging_verification.json" -Destination (Join-Path $repo "$relative/Git_staging_verification.json")
Write-Output "Verified $($checks.Count) actual Windows/WSL/Git byte bindings with nonempty SHA256 hashes."
