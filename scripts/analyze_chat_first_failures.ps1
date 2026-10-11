#Requires -Version 7.0
param(
    [string]$ProjectRoot = (Split-Path -Parent $PSScriptRoot),
    [string]$OutputDirectory = 'reports/investigation/chat_improvement_20261012'
)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$ProjectRoot = (Resolve-Path -LiteralPath $ProjectRoot).Path
$sources = [ordered]@{}
function Read-Evidence([string]$Relative) {
    $path = Join-Path $ProjectRoot $Relative
    $sources[$Relative] = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
    Get-Content -LiteralPath $path -Raw -Encoding UTF8 | ConvertFrom-Json
}
function Distribution($Values) {
    $v = @($Values | Sort-Object)
    if ($v.Count -eq 0) { return $null }
    $middle = [int][math]::Floor($v.Count / 2)
    $median = if ($v.Count % 2) { [double]$v[$middle] } else { ([double]$v[$middle-1] + $v[$middle]) / 2 }
    [ordered]@{ count=$v.Count; min=$v[0]; median=$median; max=$v[-1]; mean=(@($v) | Measure-Object -Average).Average }
}
function Summarize($Rows) {
    $rowsArray = @($Rows)
    [ordered]@{
        responses=$rowsArray.Count
        grammar2=@($rowsArray | Where-Object grammar -eq 2).Count
        relevance2=@($rowsArray | Where-Object relevance -eq 2).Count
        context2=@($rowsArray | Where-Object context -eq 2).Count
        grammar2_relevance2=@($rowsArray | Where-Object { $_.grammar -eq 2 -and $_.relevance -eq 2 }).Count
        grammar2_relevance_below2=@($rowsArray | Where-Object { $_.grammar -eq 2 -and $_.relevance -lt 2 }).Count
        natural_stop=@($rowsArray | Where-Object { $_.stop_reason -in @('eot','eos') }).Count
        repetition=@($rowsArray | Where-Object repetition).Count
        nonstopping_repetition=@($rowsArray | Where-Object { $_.stop_reason -eq 'max_new_tokens' -and $_.repetition }).Count
        removed_history=@($rowsArray | Where-Object { $_.removed_turns -gt 0 }).Count
        prompt_tokens=Distribution @($rowsArray | ForEach-Object prompt_tokens)
        generated_tokens=Distribution @($rowsArray | ForEach-Object generated_tokens)
    }
}
$stages = [ordered]@{}
$allRows = @{}
foreach ($stage in @('base','epoch1','epoch2','epoch3')) {
    $leaf = "reports/phase7/chat-first-sft-20261010-$stage-chat/greedy"
    $packet = Read-Evidence "$leaf/content_notes-items.json"
    $notes = Read-Evidence "$leaf/content_notes.json"
    $review = Read-Evidence "$leaf/content_review.json"
    $null = Read-Evidence "$leaf/result.json"
    $lookup = @{}
    foreach ($j in $notes.judgments) {
        if ($lookup.ContainsKey($j.key)) { throw "Duplicate judgment: $($j.key)" }
        $lookup[$j.key] = $j
    }
    if ($packet.evaluation_sha256 -ne $notes.evaluation_sha256 -or $packet.evaluation_sha256 -ne $review.evaluation_sha256 -or
        $packet.evaluation_sha256 -ne $sources["$leaf/result.json"]) {
        throw "Mismatched evaluation binding: $stage"
    }
    $rows = @(foreach ($item in $packet.items) {
        if (-not $lookup.ContainsKey($item.key)) { throw "Missing judgment: $($item.key)" }
        $j = $lookup[$item.key]
        $final = ($null -ne $item.PSObject.Properties['final_turn']) -and $item.final_turn
        [pscustomobject][ordered]@{
            key=$item.key; id=$item.id; family_id=$item.family_id; category=$item.category
            condition=$item.condition; final_turn=$final
            grammar=$j.grammar; relevance=$j.relevance; context=$j.context; rationale=$j.rationale
            text=$item.response.text; stop_reason=$item.response.stop_reason; repetition=$item.response.repetition
            prompt_tokens=$item.response.prompt_tokens; generated_tokens=$item.response.generated_tokens
            removed_turns=$item.response.removed_turns
        }
    })
    if ($rows.Count -ne 219 -or $lookup.Count -ne 219) { throw "Unexpected response count: $stage" }
    $primary = @($rows | Where-Object condition -eq 'suppressed')
    $own = @($rows | Where-Object condition -eq 'own-history')
    $ownFinal = @($own | Where-Object final_turn)
    $summary = Summarize $primary
    if ($summary.grammar2_relevance2 -ne $review.summaries.primary.joint_grammar_relevance_score2) { throw "Primary review mismatch: $stage" }
    if ((Summarize $ownFinal).context2 -ne $review.summaries.own_history_final24.context_score2) { throw "Context review mismatch: $stage" }
    $categories = @(foreach ($group in ($primary | Group-Object category | Sort-Object Name)) {
        [ordered]@{ category=$group.Name; summary=Summarize $group.Group }
    })
    $paired = @(foreach ($row in $ownFinal) {
        $provided = @($primary | Where-Object id -eq $row.id)
        if ($provided.Count -ne 1) { throw "Expected one provided-history match for $($row.id)" }
        [ordered]@{ id=$row.id; category=$row.category; provided_context=$provided[0].context; own_context=$row.context
            provided_relevance=$provided[0].relevance; own_relevance=$row.relevance
            provided_prompt_tokens=$provided[0].prompt_tokens; own_prompt_tokens=$row.prompt_tokens }
    })
    $control = @($packet.items | Where-Object condition -eq 'unsuppressed')
    foreach ($item in $control) {
        $p = @($packet.items | Where-Object { $_.condition -eq 'suppressed' -and $_.id -eq $item.id })
        if ($p.Count -ne 1 -or $p[0].response.raw_bytes_hex -ne $item.response.raw_bytes_hex -or
            (($p[0].response.generated_ids -join ',') -ne ($item.response.generated_ids -join ',')) -or
            (($p[0].messages | ConvertTo-Json -Depth 10 -Compress) -ne ($item.messages | ConvertTo-Json -Depth 10 -Compress))) {
            throw "Control content differs: $stage / $($item.id)"
        }
    }
    $stages[$stage] = [ordered]@{ primary=$summary; primary_by_category=$categories; own_all=Summarize $own
        own_final=Summarize $ownFinal; own_final_by_category=@(foreach ($g in ($ownFinal | Group-Object category | Sort-Object Name)) {
            [ordered]@{category=$g.Name; summary=Summarize $g.Group}
        }); provided_own_pairs=$paired; control_identical=$control.Count }
    $allRows[$stage] = $rows
}
$prep = Read-Evidence 'reports/phase7/chat_pilot_preparation.json'
$result = Read-Evidence 'reports/phase7/chat-first-sft-20261010/result.json'
$null = Read-Evidence 'reports/phase7/chat-first-sft-20261010/completion.json'
$null = Read-Evidence 'reports/phase7/chat_pilot_content_notes.json'
$metricsRelative = 'reports/phase7/chat-first-sft-20261010/metrics.jsonl'
$metricsPath = Join-Path $ProjectRoot $metricsRelative
$sources[$metricsRelative] = (Get-FileHash -LiteralPath $metricsPath -Algorithm SHA256).Hash.ToLowerInvariant()
$metrics = @(Get-Content -LiteralPath $metricsPath -Encoding UTF8 | ForEach-Object { $_ | ConvertFrom-Json })
$previous = 0L
$lossRows = @(foreach ($m in $metrics) {
    $delta = [long]$m.assistant_teacher_tokens - $previous
    if ($delta -le 0 -or [double]::IsNaN($m.loss) -or [double]::IsInfinity($m.loss)) { throw 'Invalid saved loss/counter' }
    $previous = [long]$m.assistant_teacher_tokens
    [pscustomobject]@{update=$m.update; teachers=$delta; loss=$m.loss; weighted_loss=($delta * $m.loss)}
})
if ($metrics.Count -ne 3785 -or $previous -ne $result.Assistant_teacher_tokens) { throw 'Metrics result mismatch' }
$lossBlocks = @(foreach ($limits in @(@(1,1262),@(1263,2523),@(2524,3785))) {
    $block = @($lossRows | Where-Object { $_.update -ge $limits[0] -and $_.update -le $limits[1] })
    $teachers = ($block | Measure-Object teachers -Sum).Sum
    [ordered]@{first_update=$limits[0]; last_update=$limits[1]; teachers=$teachers
        teacher_weighted_observed_training_loss=(($block | Measure-Object weighted_loss -Sum).Sum / $teachers)}
})
$train = $prep.splits.train
$analysis = [ordered]@{
    schema_version=1; scope='Static reaggregation of frozen reports and saved judgments; no rescoring, corpus scan, GPU evaluation or training'
    reviewer=$notes.reviewer; independent_human=$false; source_sha256=$sources; stages=$stages
    effective_data=[ordered]@{
        train_dialogues=$train.dialogues; responses_per_pass=$train.prepared_SFT_windows
        assistant_teachers_per_pass=$train.prepared_epoch_Assistant_teachers
        mean_teacher_tokens_per_response=($train.prepared_epoch_Assistant_teachers / $train.prepared_SFT_windows)
        EOT_teacher_fraction=($train.prepared_epoch_EOT_teachers / $train.prepared_epoch_Assistant_teachers)
        history_serialization_multiplier=($train.prepared_epoch_series_tokens / $train.source_serialized_dialogue_tokens)
        train_max_teacher_length=$train.Assistant_teacher_length_max; evaluation_max_new_tokens=64
        learned_teachers=$result.Assistant_teacher_tokens; learned_EOT_teachers=$result.EOT_teachers
        physical_input_tokens=$result.physical_tokens; valid_input_tokens=$result.valid_input_tokens
        padding_input_tokens=($result.physical_tokens-$result.valid_input_tokens)
        padding_fraction=(($result.physical_tokens-$result.valid_input_tokens)/$result.physical_tokens)
        physical_tokens_per_teacher=($result.physical_tokens/$result.Assistant_teacher_tokens)
    }
    observed_training_loss=[ordered]@{updates=$metrics.Count; first_loss=$metrics[0].loss; last_loss=$metrics[-1].loss
        blocks=$lossBlocks; limitation='Measured on evolving training batches/weights, not fixed checkpoint DEV NLL; does not establish overfitting or held-out quality'}
    epoch3_content_failures=@($allRows['epoch3'] | Where-Object { $_.condition -eq 'suppressed' -and ($_.grammar -lt 2 -or $_.relevance -lt 2) })
    epoch3_own_final_context_failures=@($allRows['epoch3'] | Where-Object { $_.condition -eq 'own-history' -and $_.final_turn -and $_.context -lt 2 })
    limitations=@('876 judgments include 320 byte-identical control outputs; not 876 independent prompts',
        '24 own-history families overlap provided-history families; compare matched IDs',
        'Category counts are eight each; descriptive, nonblind and one trained seed',
        'No new TRAIN census, DEV NLL, retention, sampling, independent seed, human blind review or protected TEST')
}
$destination = Join-Path $ProjectRoot $OutputDirectory
$null = New-Item -ItemType Directory -Path $destination -Force
$analysis | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath (Join-Path $destination 'analysis.json') -Encoding utf8NoBOM
[ordered]@{status='static_analysis_complete'; output=(Join-Path $OutputDirectory 'analysis.json'); source_files=$sources.Count
    epoch3_primary=$stages.epoch3.primary; effective_data=$analysis.effective_data; training_loss=$analysis.observed_training_loss} | ConvertTo-Json -Depth 8
