$ErrorActionPreference = 'Stop'
$repoRoot = (Get-Location).Path
$relativeRoot = 'reports/investigation/documentation_plan_refresh_20261013'
$baseline = Get-Content -LiteralPath "$relativeRoot/baseline.json" -Raw -Encoding UTF8 | ConvertFrom-Json
$run = 'reports/phase7/chat-generalization-20261013'
$utf8 = [Text.UTF8Encoding]::new($false)
$checks = [Collections.Generic.List[object]]::new()
function Require([bool]$condition, [string]$message) {
    if (-not $condition) { throw $message }
}
function SHA([string]$path) {
    return (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
}
function Check([string]$requirement, [string]$evidence) {
    $checks.Add([ordered]@{ requirement=$requirement; verified=$true; evidence=$evidence })
}

Require ($baseline.documents.Count -eq 14) 'Incomplete history list'
foreach ($entry in $baseline.documents) {
    Require ((SHA $entry.history) -eq $entry.sha256) "Original bytes changed: $($entry.path)"
    $rawBlob = (git hash-object --no-filters -- $entry.history).Trim()
    $filteredBlob = (git hash-object -- $entry.history).Trim()
    Require ($LASTEXITCODE -eq 0 -and $rawBlob -eq $filteredBlob) "Git changes history bytes: $($entry.path)"
}
Check 'Preserve all original document text' '14 history files match baseline SHA256 and Git stores raw bytes'
foreach ($entry in $baseline.immutable_evidence) {
    Require ((SHA $entry.path) -eq $entry.sha256) "Frozen evidence changed: $($entry.path)"
}
Check 'Preserve frozen implementation, config and original scientific evidence' '15 immutable baseline hashes unchanged; original phase7 records retained'

$completion = Get-Content -LiteralPath "$run/completion.json" -Raw -Encoding UTF8 | ConvertFrom-Json
$progress = Get-Content -LiteralPath "$run/progress_audit.json" -Raw -Encoding UTF8 | ConvertFrom-Json
$selection = Get-Content -LiteralPath "$run/selection.json" -Raw -Encoding UTF8 | ConvertFrom-Json
$branches = Get-Content -LiteralPath "$run/conditional_branches.json" -Raw -Encoding UTF8 | ConvertFrom-Json
$training = Get-Content -LiteralPath "$run/D1/result.json" -Raw -Encoding UTF8 | ConvertFrom-Json
$NLL = Get-Content -LiteralPath "$run/NLL/D1/t3.json" -Raw -Encoding UTF8 | ConvertFrom-Json
Require ($completion.requested_four_items_complete -eq $true -and $completion.model_quality_complete -eq $false) 'Scope/quality distinction missing'
Require ($progress.reviewed_suites -eq 14 -and $progress.content_judgments -eq 3066 -and $progress.fixed_NLL_points -eq 7 -and @($progress.pending).Count -eq 0) 'Final evaluation counts differ'
Require ($training.status -eq 'learning_complete' -and $training.checkpoint.update -eq 3641 -and $training.checkpoint.Assistant_teachers -eq 1899562) 'Final learning metadata differs'
$expectedJoint = @{D0=@{new=16;old=18};D1=@{new=12;old=15}}
$expectedContext = @{D0=@{new=5;old=4};D1=@{new=3;old=1}}
foreach ($arm in @('D0','D1')) {
    foreach ($suite in @('new','old')) {
        $content = $selection.summary.$arm.$suite.content
        Require ($content.primary.joint_grammar_relevance_score2 -eq $expectedJoint[$arm][$suite]) "Final content mismatch: $arm/$suite"
        Require ($content.own_history_final24.context_score2 -eq $expectedContext[$arm][$suite]) "Final context mismatch: $arm/$suite"
    }
}
Require ($selection.eligibility.D0 -eq $false -and $selection.eligibility.D1 -eq $false -and $null -eq $selection.eligible_candidate) 'Unexpected eligible candidate'
Require ([Math]::Abs($NLL.summaries.D1_TRAIN.body_mean_NLL - 0.0011360756006468585) -lt 1e-12) 'TRAIN NLL mismatch'
Require ([Math]::Abs($NLL.summaries.new_DEV.body_mean_NLL - 4.818918347655244) -lt 1e-12) 'DEV NLL mismatch'
Check 'Use final evidence rather than intermediate pending work' 'completion/progress/training/selection/NLL establish closed full-B comparison and final counts'
Require ($branches.recovery.status -eq 'not_triggered' -and $branches.recovery.executed -eq $false) 'Recovery status mismatch'
foreach ($branch in @('retention','sampling')) {
    Require ($branches.$branch.status -eq 'skipped_no_eligible_candidate' -and $branches.$branch.executed -eq $false -and $branches.$branch.quality_unconfirmed -eq $true) "Conditional branch mismatch: $branch"
}
Require ($completion.padding.adopted -eq $false -and $completion.padding.status -eq 'completed_rejected_numerical_gate') 'Padding rejection missing'
Check 'Keep unexecuted branches unconfirmed and rejected padding unadopted' 'Original conditional_branches and completion padding outcomes'

$currentFiles = @($baseline.documents.path)
$texts = @{}
foreach ($path in $currentFiles) { $texts[$path] = [IO.File]::ReadAllText((Join-Path $repoRoot $path)) }
foreach ($path in @('README.md','docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md','docs/135_chat_problem_solution_plan.md','docs/10_next_steps.md')) {
    Require ($texts[$path] -match '2026-10-13' -and $texts[$path] -match '136' -and $texts[$path] -match '135') "Current references missing: $path"
    Require ($texts[$path] -match '停止' -and $texts[$path] -match '未採用') "Pause/unadopted status missing: $path"
    Require ($texts[$path] -notmatch '(?m)^2026-10-13.*(?:実行継続|継続実行)[:：]') "Stale active launch paragraph: $path"
}
Require ($texts['AGENTS.md'] -match 'documents and plans only' -and $texts['AGENTS.md'] -match 'does not resume') 'Current authorization boundary missing'
Require ($texts['docs/124_base_recovery_plan.md'] -match '未実行の代替経路' -and $texts['docs/124_base_recovery_plan.md'] -match '通知して止める') 'Base-only boundary missing'
Require ($texts['docs/autonomous_status.md'] -match '14評価セット・3,066' -and $texts['docs/autonomous_status.md'] -match '1,899,562') 'Final counts missing from status'
foreach ($path in @('docs/autonomous_status.md','docs/windows_handoff.md')) {
    Require ($texts[$path] -match '今回の文書更新.*(?:確認したものではない|確認していない)') "Historical liveness caveat missing: $path"
}
Check 'Unify current instructions, latest results and liveness caveats' 'README/status/roadmap/handoff/AGENTS/checklist/124 distinguish historical observations and current documentation-only scope'
$plan = $texts['docs/135_chat_problem_solution_plan.md']
Require ($plan -match '対照は最新のD1' -and $plan -match '候補を最大1件') 'Next comparison is not bounded'
Require ($plan -match '同時に変えない' -and $plan -match '10,001,152' -and $plan -match '9.5M〜10.1M') 'Fixed conditions missing'
Require ($plan -match '提案で' -and $plan -match '未実行' -and $plan -match '別の明示再開') 'Proposal/execution boundary missing'
Require ($plan -match 'TRAIN実体とQAを凍結してから' -and $plan -match '既知2suite' -and $plan -match 'protectedTESTには触れない') 'Unseen evaluation or regression separation missing'
Require ($plan -match '21セット・4,599内容判断' -and (7 * 3 * 219) -eq 4599) 'Future evaluation count differs'
Require ($plan -match '内容≥56/80' -and $plan -match '自己生成文脈≥15/24' -and $plan -match '元品質条件') 'Quality thresholds missing'
Require ($plan -match 'B=1,899,555' -and $plan -match 'seed42' -and $plan -match '累積GPU上限案は6時間' -and $plan -match '新しい提案上限') 'Teacher/resource contract proposal missing'
Require ($plan -match '独立学習seed43' -and $plan -match '人間blind' -and $plan -match '報告・停止') 'Independent confirmation or stop conditions missing'
Check 'Replace closed-run execution steps with a concrete unexecuted next plan' 'Plan135 contains data QA, control/candidate, new+2 known DEV, all outputs, original gates, proposed budgets and advancement/stop boundaries'

$linkCount = 0
$documentsToLinkCheck = $currentFiles + @('docs/133_chat_generalization_followup_plan.md','docs/134_chat_generalization_execution.md','docs/136_chat_generalization_results.md',"$relativeRoot/README.md")
foreach ($path in $documentsToLinkCheck) {
    $content = [IO.File]::ReadAllText((Join-Path $repoRoot $path))
    foreach ($match in [regex]::Matches($content, '\[[^\]]+\]\(([^)]+)\)')) {
        $target = $match.Groups[1].Value.Trim().Trim('<','>')
        if ($target -match '^(https?://|mailto:|#)') { continue }
        $target = [Uri]::UnescapeDataString(($target -split '#')[0])
        $resolved = [IO.Path]::GetFullPath((Join-Path (Split-Path (Join-Path $repoRoot $path) -Parent) $target))
        if ($resolved -eq [IO.Path]::GetFullPath((Join-Path $repoRoot "$relativeRoot/verification.json"))) { continue }
        Require (Test-Path -LiteralPath $resolved) "Missing local link in ${path}: $target"
        $linkCount += 1
    }
}
Check 'Make current navigation and evidence links usable' "$linkCount existing local links checked; verification output is created by this command"

$allowed = $currentFiles + @('.gitattributes')
$changed = @(git diff --name-only $baseline.base_commit --)
Require ($LASTEXITCODE -eq 0) 'Git changed-path query failed'
foreach ($path in $changed) {
    Require ($path -in $allowed -or $path.StartsWith("$relativeRoot/")) "Unexpected implementation/evidence change: $path"
}
git diff --check
Require ($LASTEXITCODE -eq 0) 'Document whitespace check failed'
Check 'Perform only documentation and record changes' 'Git changed paths limited to 14 current documents, evidence archive and gitattributes; no scientific source/config modifications'

$wslRoot = '\\wsl.localhost\Ubuntu\home\aihub_ubuntu\src\japanese-tiny-llm-10m'
$mirrored = foreach ($path in $currentFiles) {
    $normalized = $texts[$path].Replace("`r`n", "`n")
    $destination = Join-Path $wslRoot $path
    [IO.File]::WriteAllText($destination, $normalized, $utf8)
    $sourceBytes = $utf8.GetBytes($normalized)
    $hasher = [Security.Cryptography.SHA256]::Create()
    try { $expectedHash = [BitConverter]::ToString($hasher.ComputeHash($sourceBytes)).Replace('-', '').ToLowerInvariant() }
    finally { $hasher.Dispose() }
    Require ((SHA $destination) -eq $expectedHash) "WSL document mismatch: $path"
    [ordered]@{ path=$path; Windows_sha256=(SHA $path); WSL_LF_sha256=$expectedHash }
}
Check 'Keep WSL documentation consistent with the Windows authority' '14 document copies written with LF and SHA256 compared; no runtime or GPU command invoked'
$wslRefresh = Join-Path $wslRoot $relativeRoot
[IO.Directory]::CreateDirectory($wslRefresh) | Out-Null
$recordFiles = @(Get-ChildItem -LiteralPath (Join-Path $repoRoot $relativeRoot) -Recurse -File | Where-Object Name -ne 'verification.json')
foreach ($file in $recordFiles) {
    $relativePath = $file.FullName.Substring($repoRoot.Length + 1).Replace('\', '/')
    $destination = Join-Path $wslRoot $relativePath
    [IO.Directory]::CreateDirectory((Split-Path -Parent $destination)) | Out-Null
    Copy-Item -LiteralPath $file.FullName -Destination $destination -Force
    Require ((SHA $destination) -eq (SHA $file.FullName)) "WSL delivery record mismatch: $relativePath"
}
Check 'Preserve evidence navigation in the WSL document copy' 'History, baseline, README and static verifier mirrored byte-identically; verification mirrored after creation'
$verification = [ordered]@{
    checked_at=[DateTimeOffset]::UtcNow.ToString('o')
    objective=$baseline.objective
    observer_sha256=(SHA "$relativeRoot/verify.ps1")
    baseline_sha256=(SHA "$relativeRoot/baseline.json")
    WSL_record_files_mirrored=$recordFiles.Count + 1
    base_commit=$baseline.base_commit
    checks=@($checks.ToArray())
    previous_documents_byte_preserved=$baseline.documents.Count
    immutable_evidence_hashes_checked=$baseline.immutable_evidence.Count
    existing_local_links_checked=$linkCount
    documents=@($mirrored)
    scientific_scope_complete=$completion.requested_four_items_complete
    model_quality_complete=$completion.model_quality_complete
    next_comparison_status='proposal_only_not_executed'
    next_evaluation_suites=21
    next_content_judgments=4599
    additional_training_or_evaluation=$false
    current_UI_liveness_checked=$false
    external_push_or_publication=$false
}
$verificationText = ($verification | ConvertTo-Json -Depth 9) + "`n"
[IO.File]::WriteAllText((Join-Path $repoRoot "$relativeRoot/verification.json"), $verificationText, $utf8)
$wslRefresh = Join-Path $wslRoot $relativeRoot
[IO.Directory]::CreateDirectory($wslRefresh) | Out-Null
[IO.File]::WriteAllText((Join-Path $wslRefresh 'verification.json'), $verificationText, $utf8)
[pscustomobject]$verification | Select-Object checked_at,previous_documents_byte_preserved,immutable_evidence_hashes_checked,existing_local_links_checked,next_comparison_status,additional_training_or_evaluation | ConvertTo-Json
