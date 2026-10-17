param([int]$Port = 7861)
$ErrorActionPreference = 'Stop'
if ($Port -lt 1024 -or $Port -gt 65535) { throw 'Invalid port' }
$workspace = Split-Path -Parent $PSScriptRoot
$linuxRepo = '/home/aihub_ubuntu/src/japanese-tiny-llm-10m'
$linuxCopy = '\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m'
$runDir = Join-Path $workspace 'reports/local/chat-webui'
try {
    $existing = Invoke-RestMethod "http://127.0.0.1:$Port/api/model" -TimeoutSec 2
    if ($existing.name -eq 'JMicro-10M Chat' -and $existing.checkpoint_sha256 -eq '1c79692f71efacecf5444a6be250518a4603248ee2b2811b531e566f2cfc2f24') {
        Write-Output "Already running: http://127.0.0.1:$Port"
        exit 0
    }
    throw 'Another service occupies this port.'
} catch [System.Net.Http.HttpRequestException] { }
New-Item -ItemType Directory -Force -Path $runDir | Out-Null
$files = @('scripts/chat_demo.py', 'src/jmicro/chat_demo.py', 'webui/chat/index.html', 'webui/chat/app.js', 'webui/chat/style.css')
foreach ($relative in $files) {
    $source = Join-Path $workspace $relative
    $target = Join-Path $linuxCopy $relative
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $target) | Out-Null
    Copy-Item -LiteralPath $source -Destination $target
}
$arguments = @('-d', 'Ubuntu', '--cd', $linuxRepo, '--', '/home/aihub_ubuntu/.local/bin/uv', 'run', '--frozen', '--extra', 'hub', '--extra', 'data', '--extra', 'ml', '--extra', 'export', 'scripts/chat_demo.py', '--port', "$Port")
$tag = [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfff')
$stdout = Join-Path $runDir "stdout-$tag.log"
$stderr = Join-Path $runDir "stderr-$tag.log"
$worker = Start-Process -FilePath 'wsl.exe' -ArgumentList $arguments -WindowStyle Hidden -PassThru -RedirectStandardOutput $stdout -RedirectStandardError $stderr
$record = [ordered]@{windows_pid=$worker.Id; windows_started_at=$worker.StartTime.ToUniversalTime().ToString('o'); url="http://127.0.0.1:$Port"; stdout=$stdout; stderr=$stderr; command='uv run --frozen scripts/chat_demo.py'; training_launched=$false; CPU_only=$true}
$record | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $runDir 'launcher.json') -Encoding utf8
for ($attempt = 0; $attempt -lt 40; $attempt++) {
    Start-Sleep -Seconds 1
    $worker.Refresh()
    if ($worker.HasExited) { throw "Chat server exited. Inspect $stderr before retrying." }
    try {
        $model = Invoke-RestMethod "http://127.0.0.1:$Port/api/model" -TimeoutSec 1
        if ($model.name -eq 'JMicro-10M Chat' -and $model.checkpoint_sha256 -eq '1c79692f71efacecf5444a6be250518a4603248ee2b2811b531e566f2cfc2f24') {
            Write-Output "Ready: http://127.0.0.1:$Port ($($model.kind), $($model.device))"
            exit 0
        }
    } catch [System.Net.Http.HttpRequestException] { }
}
throw "Chat startup timed out. Inspect $stderr and the saved process before retrying."
