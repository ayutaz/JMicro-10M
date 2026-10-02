# Execute from a normal PowerShell session, outside the restricted agent session.
[CmdletBinding()]
param([switch]$Preview)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$source = Join-Path $projectRoot 'configs/runtime/codex_autonomous.config.toml'
$profileHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
$destination = Join-Path $profileHome 'jmicro_autonomous.config.toml'
if ($Preview) {
    Write-Output "Profile destination: $destination"
    Get-Content -LiteralPath $source
    return
}
New-Item -ItemType Directory -Force -Path $profileHome | Out-Null
if (Test-Path -LiteralPath $destination) {
    if ((Get-FileHash -LiteralPath $source).Hash -eq (Get-FileHash -LiteralPath $destination).Hash) {
        Write-Output "Profile already matches: $destination"
        return
    }
    $backup = "$destination.$([DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfffffffZ')).bak"
    Copy-Item -LiteralPath $destination -Destination $backup
    Write-Output "Previous profile backed up to: $backup"
}
Copy-Item -LiteralPath $source -Destination $destination
Write-Output "Installed project profile: $destination"
Write-Output "Start with: codex --profile jmicro_autonomous --cd `"$projectRoot`""
