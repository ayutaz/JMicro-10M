param([int]$Port = 7860)
$ErrorActionPreference = 'Stop'
$workspace = Split-Path -Parent $PSScriptRoot
$linuxRepo = '/home/aihub_ubuntu/src/japanese-tiny-llm-10m'
$linuxCopy = '\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m'
$runDir = Join-Path $workspace 'reports\local\webui'
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
try {
    $model = Invoke-RestMethod -Uri "http://127.0.0.1:$Port/api/model" -TimeoutSec 2
    if ($model.name -eq 'JMicro-10M') {
        Write-Output "Already running: http://127.0.0.1:$Port"
        exit 0
    }
} catch { }
$files = @('scripts/webui.py', 'src/jmicro/webui.py', 'webui/index.html', 'webui/style.css', 'webui/app.js')
$utf8 = New-Object System.Text.UTF8Encoding($false)
foreach ($relative in $files) {
    $source = Join-Path $workspace $relative
    $target = Join-Path $linuxCopy $relative
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $target) | Out-Null
    $content = [IO.File]::ReadAllText($source).Replace("`r`n", "`n")
    [IO.File]::WriteAllText($target, $content, $utf8)
}
$arguments = @('-d', 'Ubuntu', '--cd', $linuxRepo, '--', '/home/aihub_ubuntu/.local/bin/uv', 'run', '--frozen', '--extra', 'hub', '--extra', 'data', '--extra', 'ml', '--extra', 'export', 'scripts/webui.py', '--port', "$Port")
$process = Start-Process -FilePath 'wsl.exe' -ArgumentList $arguments -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runDir 'stdout.log') -RedirectStandardError (Join-Path $runDir 'server.log')
$record = @{windows_pid=$process.Id; started_at=[DateTime]::UtcNow.ToString('o'); url="http://127.0.0.1:$Port"; command='uv run --frozen --extra hub --extra data --extra ml --extra export scripts/webui.py'; linux_record="$linuxRepo/reports/local/webui/server.json"}
[IO.File]::WriteAllText((Join-Path $runDir 'launcher.json'), ($record | ConvertTo-Json), $utf8)
for ($attempt = 0; $attempt -lt 40; $attempt++) {
    Start-Sleep -Seconds 1
    $process.Refresh()
    if ($process.HasExited) { throw "Server exited. See $runDir\server.log" }
    try {
        $model = Invoke-RestMethod -Uri "http://127.0.0.1:$Port/api/model" -TimeoutSec 1
        if ($model.name -eq 'JMicro-10M') {
            Write-Output "Ready: http://127.0.0.1:$Port ($($model.device))"
            exit 0
        }
    } catch { }
}
throw "Startup did not finish within 40 seconds. Inspect $runDir\server.log and the saved Linux process before retrying."
