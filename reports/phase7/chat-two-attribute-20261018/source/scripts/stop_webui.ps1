$ErrorActionPreference = 'Stop'
$serverRecord = '\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m\reports\local\webui\server.json'
if (-not (Test-Path -LiteralPath $serverRecord)) { Write-Output 'No saved UI process.'; exit 0 }
$record = Get-Content -LiteralPath $serverRecord -Raw | ConvertFrom-Json
if ($record.status -ne 'running') { Write-Output "UI status: $($record.status)"; exit 0 }
$serverPid = [int]$record.pid
$bootId = [string]$record.boot_id
$startTicks = [long]$record.start_ticks
# Values are constrained to numeric fields and a UUID; do not kill a recycled PID.
if ($bootId -notmatch '^[0-9a-f-]{36}$' -or $serverPid -lt 1 -or $startTicks -lt 1) { throw 'Invalid saved process identity' }
$command = "test ""`$(cat /proc/sys/kernel/random/boot_id)"" = '$bootId' && test ""`$(awk '{print `$22}' /proc/$serverPid/stat)"" = '$startTicks' && kill -TERM $serverPid"
& wsl.exe -d Ubuntu -- bash -lc $command
if ($LASTEXITCODE -ne 0) { throw 'Saved process identity differs or UI already exited; no other process was stopped.' }
Write-Output 'Local UI stop requested.'
