param([switch]$Publish)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$projectRoot = Split-Path -Parent $PSScriptRoot
$env:GIT_TERMINAL_PROMPT = '0'
$env:GCM_INTERACTIVE = 'Never'

# Keep the working Git credential in memory; never write it to a file or log.
$credentialLines = "protocol=https`nhost=github.com`n`n" | git credential fill
if ($LASTEXITCODE -ne 0) { throw 'Git credential lookup failed' }
$credentialFields = @{}
foreach ($credentialLine in $credentialLines) {
    $credentialParts = $credentialLine -split '=', 2
    if ($credentialParts.Count -eq 2) {
        $credentialFields[$credentialParts[0]] = $credentialParts[1]
    }
}
if (-not $credentialFields['password']) { throw 'No GitHub credential available' }
$apiHeaders = @{
    Authorization = 'Bearer ' + $credentialFields['password']
    Accept = 'application/vnd.github+json'
    'User-Agent' = 'JMicro-publication'
    'X-GitHub-Api-Version' = '2022-11-28'
}
$endpoint = 'https://api.github.com/repos/ayutaz/japanese-tiny-llm-10m'
try {
    $before = Invoke-RestMethod -Uri $endpoint -Headers $apiHeaders
    if ($before.full_name -ne 'ayutaz/japanese-tiny-llm-10m') { throw 'Unexpected repository' }
    if (-not $Publish) {
        $before | Select-Object full_name, private, visibility, permissions, license
        return
    }
    if (-not $before.permissions.admin) { throw 'Repository admin permission required' }
    if ($before.private) {
        $null = Invoke-RestMethod -Uri $endpoint -Method Patch -Headers $apiHeaders `
            -ContentType 'application/json' -Body '{"private":false}'
    }
    # An authenticated read cannot prove anonymous accessibility.
    $anonymousHeaders = @{ Accept='application/vnd.github+json'; 'User-Agent'='JMicro-publication' }
    $public = Invoke-RestMethod -Uri ($endpoint + '?publication_check=' + [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()) -Headers $anonymousHeaders
    if ($public.private -or $public.visibility -ne 'public') { throw 'Anonymous public verification failed' }
    $head = (git -C $projectRoot rev-parse HEAD).Trim()
    if ($LASTEXITCODE -ne 0) { throw 'Git HEAD unavailable' }
    $remoteOutput = git -c credential.helper= -c http.extraHeader= ls-remote `
        https://github.com/ayutaz/japanese-tiny-llm-10m.git refs/heads/main
    if ($LASTEXITCODE -ne 0 -or -not $remoteOutput) {
        throw 'Anonymous Git endpoint is unavailable; public API state alone is insufficient'
    }
    $remoteHead = $remoteOutput -split '\s+'
    if ($remoteHead[0] -ne $head) { throw 'Local and remote main differ' }
    $readme = Invoke-RestMethod -Uri ($endpoint + '/readme?ref=' + $head) -Headers $anonymousHeaders
    $remoteReadme = [Convert]::FromBase64String(($readme.content -replace '\s', ''))
    $localReadme = [IO.File]::ReadAllBytes((Join-Path $projectRoot 'README.md'))
    $digest = [Security.Cryptography.SHA256]::HashData($remoteReadme)
    $localDigest = [Security.Cryptography.SHA256]::HashData($localReadme)
    if ([Convert]::ToHexString($digest) -ne [Convert]::ToHexString($localDigest)) {
        throw 'Published README bytes differ from local README'
    }
    $license = Invoke-RestMethod -Uri ($endpoint + '/license?ref=' + $head) -Headers $anonymousHeaders
    if ($license.license.spdx_id -ne 'Apache-2.0') { throw 'Apache-2.0 detection failed' }
    $receipt = [ordered]@{
        status='public_and_anonymously_verified'
        repository=$public.full_name
        url=$public.html_url
        private_at_start_of_verification=$before.private
        private=$public.private
        visibility=$public.visibility
        revision=$head
        license_spdx=$license.license.spdx_id
        README_SHA256=[Convert]::ToHexString($digest).ToLowerInvariant()
        anonymous_README_exact=$true
        anonymous_git_head_exact=$true
        recorded_at_UTC=[DateTime]::UtcNow.ToString('o')
    }
    $destination = Join-Path $projectRoot 'reports/publication/repository-public-20261018.json'
    if (Test-Path -LiteralPath $destination) { throw 'Publication receipt already exists' }
    [IO.Directory]::CreateDirectory((Split-Path -Parent $destination)) | Out-Null
    [IO.File]::WriteAllText($destination, ($receipt | ConvertTo-Json -Depth 8) + "`n", [Text.UTF8Encoding]::new($false))
    $receipt | ConvertTo-Json -Depth 8
}
finally {
    $credentialLines = $null
    $credentialFields.Clear()
    $apiHeaders.Clear()
}
