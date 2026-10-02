# Run from a normal Windows PowerShell session. See docs/windows_handoff.md.
[CmdletBinding()]
param(
    [string]$Distribution = '',
    [switch]$CheckOnly
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$projectRoot = Split-Path -Parent $PSScriptRoot
$reportDir = Join-Path $projectRoot 'reports/phase4'
New-Item -ItemType Directory -Force -Path $reportDir | Out-Null
$observations = [ordered]@{
    observed_at = [DateTime]::UtcNow.ToString('o')
    requested_wsl_package = '3.x'
    status = 'incomplete'
    commands = @()
}

function Invoke-WslObserved {
    param([string[]]$Arguments, [switch]$AllowFailure)
    # WSL management commands emit UTF-16LE; Linux commands generally emit UTF-8.
    # Capture bytes so Windows PowerShell 5.1 also retains Japanese text correctly.
    $quoted = @($Arguments | ForEach-Object {
        # WSL's management parser treats a quoted leading option as a Linux
        # command. Quote only arguments that need Windows command-line escaping.
        if ($_ -ne '' -and $_ -notmatch '[\s"]') {
            $_
        } else {
            '"' + ($_ -replace '(\\*)"', '$1$1\"' -replace '(\\+)$', '$1$1') + '"'
        }
    })
    $startInfo = New-Object System.Diagnostics.ProcessStartInfo
    $startInfo.FileName = (Get-Command wsl.exe).Source
    $startInfo.Arguments = $quoted -join ' '
    $startInfo.UseShellExecute = $false
    $startInfo.CreateNoWindow = $true
    $startInfo.RedirectStandardOutput = $true
    $startInfo.RedirectStandardError = $true
    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $startInfo
    $stdout = New-Object System.IO.MemoryStream
    $stderr = New-Object System.IO.MemoryStream
    try {
        $process.Start() | Out-Null
        $stdoutTask = $process.StandardOutput.BaseStream.CopyToAsync($stdout)
        $stderrTask = $process.StandardError.BaseStream.CopyToAsync($stderr)
        $process.WaitForExit()
        $stdoutTask.GetAwaiter().GetResult()
        $stderrTask.GetAwaiter().GetResult()
        $code = $process.ExitCode
        $parts = @($stdout, $stderr | ForEach-Object {
            $bytes = $_.ToArray()
            $encoding = if ([Array]::IndexOf($bytes, [byte]0) -ge 0) {
                [System.Text.Encoding]::Unicode
            } else { [System.Text.Encoding]::UTF8 }
            $encoding.GetString($bytes).Trim()
        })
        $output = ($parts | Where-Object { $_ }) -join "`n"
    } finally {
        $process.Dispose()
        $stdout.Dispose()
        $stderr.Dispose()
    }
    $observations.commands += @{ command = @('wsl.exe') + $Arguments; exit_code = $code; output = $output }
    if ($output) { Write-Host $output }
    if ($code -ne 0 -and -not $AllowFailure) {
        throw "wsl.exe $($Arguments -join ' ') failed (exit $code). See reports/phase4/wsl_setup.json."
    }
    return $output
}

try {
    if ($CheckOnly) {
        Invoke-WslObserved -Arguments @('--version') -AllowFailure | Out-Null
        Invoke-WslObserved -Arguments @('--list', '--verbose') -AllowFailure | Out-Null
        Invoke-WslObserved -Arguments @('--status') -AllowFailure | Out-Null
        $observations.status = 'observed_only'
    } else {
        Invoke-WslObserved -Arguments @('--update', '--web-download') | Out-Null
        $versionText = Invoke-WslObserved -Arguments @('--version')
        $versionMatch = [regex]::Match($versionText, '\b(\d+)\.\d+\.\d+(?:\.\d+)?\b')
        if (-not $versionMatch.Success -or [int]$versionMatch.Groups[1].Value -ne 3) {
            throw 'WSL package 3.x is required. Use the official Microsoft WSL release installer if the update channel has not delivered it yet.'
        }
        $observations.wsl_package_version = $versionMatch.Value
        $names = Invoke-WslObserved -Arguments @('--list', '--quiet')
        $installed = @($names -split '\r?\n' | ForEach-Object { $_.Trim() } | Where-Object { $_ })
        if ($installed.Count -eq 0) {
            $newDistribution = if ($Distribution) { $Distribution } else { 'Ubuntu-24.04' }
            Invoke-WslObserved -Arguments @('--install', '--distribution', $newDistribution, '--no-launch') | Out-Null
            $observations.status = 'linux_user_setup_required'
            Write-Host "Open 'wsl.exe -d $newDistribution', create your Linux user, then run this script again."
        } else {
            if (-not $Distribution) {
                if ($installed.Count -ne 1) {
                    throw "Several distributions exist: $($installed -join ', '). Run again with -Distribution <name>."
                }
                $Distribution = $installed[0]
            }
            if ($installed -notcontains $Distribution) { throw "Distribution '$Distribution' is not installed." }
            $observations.distribution = $Distribution
            $distroList = Invoke-WslObserved -Arguments @('--list', '--verbose')
            $modePattern = '(?m)^\s*\*?\s*' + [regex]::Escape($Distribution) + '\s+.+?\s+2\s*$'
            if ($distroList -notmatch $modePattern) {
                throw "Distribution '$Distribution' must use WSL 2. Review 'wsl --list --verbose' and convert it with 'wsl --set-version $Distribution 2' before retrying."
            }
            $uid = Invoke-WslObserved -Arguments @('--distribution', $Distribution, '--exec', 'id', '-u')
            if ($uid.Trim() -eq '0') {
                throw "Create/select a non-root Linux user in '$Distribution' before running the Linux setup."
            }
            $linuxRoot = (Invoke-WslObserved -Arguments @('--distribution', $Distribution, '--exec', 'wslpath', '-a', '-u', $projectRoot)).Trim()
            & wsl.exe --distribution $Distribution --exec bash "$linuxRoot/scripts/setup_wsl_environment.sh"
            if ($LASTEXITCODE -ne 0) { throw 'Linux setup did not complete. Review the Linux reports/phase4/setup.log and retry after fixing the reported issue.' }
            $observations.status = 'environment_ready_training_unverified'
        }
    }
} catch {
    $observations.error = $_.Exception.Message
    throw
} finally {
    $observations | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $reportDir 'wsl_setup.json') -Encoding UTF8
}
