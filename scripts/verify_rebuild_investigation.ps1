param()
$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$investigationRoot = Join-Path $repoRoot 'reports/investigation/rebuild_20261010'
$sourceGroups = @(
    @{directory='reference'; repository='https://huggingface.co/hisakata-ai/akebono-10m-chat'; revision='74b3a1739e6d16883177c6021b3c03a7d517c7fb'; api='https://huggingface.co/api/models/hisakata-ai/akebono-10m-chat'},
    @{directory='reference_space'; repository='https://huggingface.co/spaces/hisakata-ai/akebono-10m-chat'; revision='aba003926d78f088a010192f51a28ff04e45dfab'; api='https://huggingface.co/api/spaces/hisakata-ai/akebono-10m-chat'}
)
$external = @()
foreach ($group in $sourceGroups) {
    $directory = Join-Path $investigationRoot $group.directory
    $manifest = Get-Content (Join-Path $directory 'MANIFEST.json') -Raw | ConvertFrom-Json
    $checksumMap = @{}
    foreach ($line in Get-Content (Join-Path $directory 'SHA256SUMS')) {
        if ($line -match '^([a-f0-9]{64})\s+(.+)$') { $checksumMap[$Matches[2]] = $Matches[1] }
    }
    foreach ($file in Get-ChildItem -LiteralPath $directory -File) {
        $digest = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash.ToLower()
        $entry = @($manifest.files | Where-Object file -eq $file.Name)
        if ($entry.Count -gt 0 -and ($entry[0].sha256 -ne $digest -or $entry[0].bytes -ne $file.Length)) {
            throw "Manifest mismatch: $($group.directory)/$($file.Name)"
        }
        if ($checksumMap.ContainsKey($file.Name) -and $checksumMap[$file.Name] -ne $digest) {
            throw "SHA256SUMS mismatch: $($group.directory)/$($file.Name)"
        }
        $url = if ($file.Name -eq 'hub_metadata.json') { $group.api } else {
            "$($group.repository)/resolve/$($group.revision)/$($file.Name)"
        }
        $external += [ordered]@{
            path="$($group.directory)/$($file.Name)"; url=$url
            revision=$(if ($file.Name -eq 'hub_metadata.json') { $null } else { $group.revision })
            bytes=$file.Length; sha256=$digest
            published_manifest_match=$(if ($entry.Count -gt 0) { $true } else { $null })
            published_SHA256SUMS_match=$(if ($checksumMap.ContainsKey($file.Name)) { $true } else { $null })
        }
    }
}
$docPath = Join-Path $repoRoot 'docs/127_rebuild_investigation.md'
$localInputs = @(
    'src/jmicro/model.py', 'src/jmicro/shards.py', 'src/jmicro/training.py', 'src/jmicro/tokenizer.py',
    'scripts/base_parallel_residual_trainer.py', 'scripts/base_kv_allocation_trainer.py',
    'scripts/base_teacher_decay_trainer.py', 'scripts/seeded_textbook_trainer.py',
    'scripts/start_webui.ps1', 'configs/phase6/base_frozen.json', 'reports/phase6/base_model.json',
    'reports/phase6/base_teacher_decay_2b_candidate_notes.json',
    'reports/phase6/base_learning_decision_table_20261008.json', 'pyproject.toml'
)
foreach ($match in [regex]::Matches([IO.File]::ReadAllText($docPath), '\]\(([^)]+)\)')) {
    $target = $match.Groups[1].Value
    if ($target -match '^[a-zA-Z]+:' -or $target.StartsWith('#')) { continue }
    $full = [IO.Path]::GetFullPath((Join-Path (Split-Path $docPath -Parent) ($target -split '#')[0]))
    $relative = [IO.Path]::GetRelativePath($repoRoot, $full).Replace('\', '/')
    if ($relative.StartsWith('reports/investigation/')) { continue }
    if (-not (Test-Path -LiteralPath $full -PathType Leaf)) { throw "Missing local link: $target" }
    $localInputs += $relative
}
$localSources = @(foreach ($relative in ($localInputs | Sort-Object -Unique)) {
    $file = Get-Item -LiteralPath (Join-Path $repoRoot $relative)
    [ordered]@{path=$relative; bytes=$file.Length; sha256=(Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash.ToLower()}
})
$modelSha = (Get-FileHash (Join-Path $repoRoot 'src/jmicro/model.py') -Algorithm SHA256).Hash.ToLower()
if ($modelSha -ne '298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83') {
    throw 'Frozen model source changed'
}
$c = Get-Content (Join-Path $investigationRoot 'reference/config.json') -Raw | ConvertFrom-Json
$j = Get-Content (Join-Path $repoRoot 'reports/phase6/base_model.json') -Raw | ConvertFrom-Json
$jParts = [ordered]@{
    embedding=$j.vocab_size*$j.hidden_size
    attention=$j.num_hidden_layers*(2*$j.hidden_size*$j.hidden_size+2*$j.hidden_size*$j.num_key_value_heads*$j.head_dim)
    FFN=$j.num_hidden_layers*3*$j.hidden_size*$j.intermediate_size
    norm=$j.num_hidden_layers*2*$j.hidden_size+$j.hidden_size
}
$aParts = [ordered]@{
    embedding=$c.vocab_size*$c.dim; attention=$c.layers*4*$c.dim*$c.dim
    FFN=$c.layers*3*$c.dim*$c.ff_dim; norm=$c.layers*2*$c.dim+$c.dim
}
$jTotal = ($jParts.Values | Measure-Object -Sum).Sum
$aTotal = ($aParts.Values | Measure-Object -Sum).Sum
if ($jTotal -ne $j.expected_parameter_count -or $aTotal -ne $c.expected_parameters) {
    throw 'Parameter formula mismatch'
}
$baseline = (& git -C $repoRoot rev-parse '8f50c47^{commit}').Trim()
if ($LASTEXITCODE -ne 0) { throw 'Missing investigation baseline commit' }
$evidence = [ordered]@{
    status='public_source_and_existing_evidence_static_investigation_complete'
    verified_UTC=[DateTime]::UtcNow.ToString('o'); local_source_commit=$baseline
    external_files=$external; local_evidence=$localSources
    parameter_arithmetic=@{
        JMicro=@{parts=$jParts; total=$jTotal; method='config_and_source_matrix_shapes_no_model_execution'}
        Akebono=@{parts=$aParts; total=$aTotal; method='config_and_source_matrix_shapes_no_model_execution'}
    }
    primary_literature=@(
        'https://arxiv.org/abs/2305.07759', 'https://arxiv.org/abs/2402.14905',
        'https://arxiv.org/abs/2203.15556', 'https://arxiv.org/abs/1908.04319',
        'https://arxiv.org/abs/1904.09751', 'https://huggingface.co/docs/transformers/main/en/chat_templating',
        'https://huggingface.co/datasets/SimpleStories/SimpleStories-JA',
        'https://huggingface.co/datasets/llm-jp/magpie-sft-v1.0'
    )
    access_limits=@{
        github_anonymous='HTTP404'; github_existing_gh_authentication='HTTP401 Bad credentials'
        github_remote_HEAD_confirmed=$false
        reference_web_tool_access='failed; direct HTTP pinned-source retrieval succeeded'
        reference_total_training_recipe='not published'; user_specific_failure_logs='not supplied'
        runtime_liveness='not checked'
    }
    scope=@{
        new_training_tokens=0; new_GPU_seconds=0; new_inference_or_quality_evaluation=$false
        data_preparation=$false; weights_downloaded=$false; tokenizer_binary_downloaded=$false
        reference_code_executed=$false; new_ratings=0; new_intervention_selected=$false
        new_intervention_frozen=$false; external_publication=$false; Base_complete=$false; Base_adopted=$false
    }
    limits=@(
        'Published small-file hash consistency is not independent model quality evidence.',
        'Original reports and frozen sources were read; the whole corpus and all reports were not reaudited.',
        'Reference capability numbers are publisher-reported and not comparable to the local Base DEV80.',
        'CPU/GPU model execution and active process checks were not performed.'
    )
}
$utf8 = [Text.UTF8Encoding]::new($false)
[IO.File]::WriteAllText((Join-Path $investigationRoot 'evidence.json'), ($evidence | ConvertTo-Json -Depth 15)+[Environment]::NewLine, $utf8)
$documents = @('README.md', 'docs/README.md', 'docs/127_rebuild_investigation.md',
    'docs/autonomous_status.md', 'docs/15_project_roadmap.md', 'docs/windows_handoff.md',
    'reports/investigation/rebuild_20261010/README.md')
$links = 0
foreach ($relative in $documents) {
    $path = Join-Path $repoRoot $relative
    foreach ($match in [regex]::Matches([IO.File]::ReadAllText($path), '\]\(([^)]+)\)')) {
        $target = $match.Groups[1].Value
        if ($target -match '^[a-zA-Z]+:' -or $target.StartsWith('#')) { continue }
        # verification.json is written only after this check finishes.
        if ($relative -eq 'reports/investigation/rebuild_20261010/README.md' -and $target -eq 'verification.json') { continue }
        $full = [IO.Path]::GetFullPath((Join-Path (Split-Path $path -Parent) ($target -split '#')[0]))
        if (-not (Test-Path -LiteralPath $full)) { throw "Missing local link in ${relative}: $target" }
        $links += 1
    }
}
$jsonFiles = @(Get-ChildItem -LiteralPath $investigationRoot -Recurse -File -Filter '*.json' | Where-Object Name -ne 'verification.json')
foreach ($file in $jsonFiles) { Get-Content -LiteralPath $file.FullName -Raw | ConvertFrom-Json | Out-Null }
$diffCheck = & git -C $repoRoot diff --check 2>&1
if ($LASTEXITCODE -ne 0) { throw "Git diff whitespace check failed: $diffCheck" }
$verification = [ordered]@{
    status='passed'; verified_UTC=[DateTime]::UtcNow.ToString('o'); external_files=$external.Count
    published_manifest_matches=@($external | Where-Object published_manifest_match -eq $true).Count
    published_SHA256SUMS_matches=@($external | Where-Object published_SHA256SUMS_match -eq $true).Count
    local_evidence=$localSources.Count; documents=$documents.Count; local_file_links_checked=$links
    JSON_parsed=$jsonFiles.Count; JMicro_parameters=$jTotal; Akebono_parameters=$aTotal
    frozen_model_source_matches=$true; git_diff_check=$true
    new_training_tokens=0; new_GPU_seconds=0
    scope='Static document/source consistency only; no runtime, quality, corpus or learned model verification.'
}
[IO.File]::WriteAllText((Join-Path $investigationRoot 'verification.json'), ($verification | ConvertTo-Json -Depth 10)+[Environment]::NewLine, $utf8)
$verification | ConvertTo-Json -Depth 10
