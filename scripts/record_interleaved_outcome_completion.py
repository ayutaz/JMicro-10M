"""Persist actual terminal fourth-cell evidence and a bounded TRAIN diagnosis."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import json
from pathlib import Path
import sys
import tarfile
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive,identity
import run_interleaved_outcome_order as study


def main():
    c=study.inspect(study.CONFIG);r=read_json(study.RUN/'compare-result.json');job=read_json(study.RUN/'job.json')
    review=read_json(study.RUN/'review.json');probe=study.probe_evidence()
    destination=ROOT/'reports/phase6/interleaved_outcome_completion.json'
    if destination.exists():raise ValueError('Preserve original actual completion')
    if (job['status']!='complete' or alive(job) or job['GPU_elapsed_seconds']!=r['GPU_seconds']
            or review['result_sha256']!=sha256(study.RUN/'compare-result.json')
            or review['eligible_for_final_Base_validation'] or review['status']!='rejected_single_order_target_fourth_cell'
            or r['scientific_teacher_tokens']!=91641755 or r['scientific_optimizer_updates']!=3068
            or r['GPU_seconds']+probe['GPU_seconds']>900 or not review['three_old_cells_reused_unchanged']):
        raise ValueError('Actually finished failed finite fourth cell required')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:ui=json.load(response)
    processes=[]
    for path in Path('/proc').glob('[0-9]*/cmdline'):
        try:args=path.read_bytes().replace(b'\0',b' ').decode('utf-8')
        except (OSError,UnicodeDecodeError):continue
        if 'scripts/webui.py --port 7860' in args and '.venv/bin/python' in args:processes.append(identity(int(path.parent.name)))
    if (len(processes)!=1 or not alive(processes[0]) or ui['busy']
            or ui['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'):
        raise ValueError('Actual original idle UI must be restored')
    audit=review['accounting'];source=audit['actual_source_accounting']
    if sum(source['teachers'].values())!=91641755 or source['teachers']['conditional_textbook']!=1641755:
        raise ValueError('Actual masked teacher source totals required')
    notes=read_json(study.RUN/'content-notes.json');summary=review['summaries']['masked_mixed']
    proposal_path=ROOT/'reports/phase6/source_gradient_attribution_proposal.json'
    if proposal_path.exists():raise ValueError('Preserve original defined diagnostic')
    proposal=dict(status='defined_read_only_TRAIN_diagnostic_not_implemented_not_launched',created_at=now(),
        trigger=study.reference(study.RUN/'review.json'),
        question='Under the frozen token-mean CE, how much does each TRAIN source and the conditional outcome/EOS contribute to the parameter gradient, and how do source gradients align?',
        motivation='Four completed cells show an order-dependent Web/generation tradeoff. Masked mixed retained WebBPB but failed completion. '
            'Conditional targets have1641755/91641755 actual teacher mass, not10percent. Count alone does not measure the gradient or prove dilution causes the quality failure.',
        fixed_checkpoints=dict(original_fullparent=c['parent'],completed_masked_mixed=dict(path=r['checkpoint']['checkpoint'],sha256=r['checkpoint']['checkpoint_sha256'])),
        fixed_inputs='First16 consecutive original mixed TRAIN batches from the frozen original parent Web cursor/seed42, context1024/batch32. '
            'Use the same windows/reference targets/conditional outcome+EOS mask as the completed fourth cell. No dev/test input or quality-based batch/CP selection.',
        groups=['web','story','ordinary_textbook','conditional_outcome_body','conditional_EOS'],
        calculation='Use the unchanged BF16/math forward in eval mode with no optimizer. Compute each group CE-sum gradient divided by the same actual nonignored teacher count. '
            'Report teacher/input counts, source CE, actual token fractions, full unique-parameter gradient norm, pairwise dot/cosine, contribution to total squared norm. '
            'Unique tied parameters count once. Report both conditional groups and their sum. Cross-check summed groups against an independently computed original token-mean CE gradient within a preregistered numeric tolerance. '
            'Zero support has zero gradient and null cosine, never an invented label/division by zero. Gradient diagnostics are not scientific training exposure.',
        read_only_requirements='No optimizer construction/step, no parameter or saved optimizer/scheduler/sampler/counter writes. '
            'Use torch.autograd.grad so parameter .grad remains absent. Isolate and restore RNG. Verify model bitwise unchanged/no gradients/eval/finite/full expected input hashes. '
            'Persist PID/boot/start/log/result and inspect existing GPU processes before start; restore original UI after completion.',
        CPU_preparation_ceiling_seconds=30,total_new_GPU_ceiling_seconds=90,teacher_tokens_learned=0,optimizer_updates=0,
        tests_required='Analytical tied-parameter group decomposition, uneven masks/teacher denominator, opposing gradients, absent-source zero support, finite rejection and immutable model/RNG checks.',
        completion='All16 matched TRAIN batches at both fixed checkpoints, decomposition checks/source counts/gradient summaries/actual terminal/UI/portable evidence and commit. '
            'No dev model reruns, sampling/content review, new learning seed, final test or adoption in this diagnostic.',
        failure='End the single diagnostic on source/checkpoint/accounting/numeric/budget failure; no batch reselection, loss coefficient, source ratio, mask/EOS weight, LR, decoder or checkpoint sweep.',
        interpretation='A local gradient observation of fixed TRAIN batches/one learned seed cannot demonstrate general quality, prove a cause or justify an automatic loss reweighting. '
            'Any later training intervention needs a separate explicit mechanism, fixed comparison, cost ceiling and unchanged quality criteria; this failed fourth cell stays rejected.',
        next_action='Implement and verify the bounded read-only TRAIN gradient attribution before any further Base training.',
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(proposal_path,proposal)
    previous=read_json(ROOT/'reports/phase6/shared_prefix_web_loss_completion.json')['related_GPU_seconds']
    report=dict(status='fourth_cell_complete_rejected_Base_unfinished',created_at=now(),result=study.reference(study.RUN/'compare-result.json'),
        review=study.reference(study.RUN/'review.json'),config=study.reference(study.CONFIG),actual_terminal_job=job,actual_process_absent=True,
        scientific_teacher_tokens=r['scientific_teacher_tokens'],scientific_optimizer_updates=r['scientific_optimizer_updates'],
        physical_input_tokens=audit['physical_input_tokens'],nominal_reference_teachers=100000000,actual_source_accounting=source,source_digests=audit['source_digests'],
        scientific_checkpoint=r['checkpoint'],all80_individually_read=True,exact_prior_raw_scores_reused=len(notes['exact_old_score_reuse']),
        new_science_GPU_seconds=r['GPU_seconds'],own_probe_GPU_seconds=probe['GPU_seconds'],new_all_GPU_seconds=r['GPU_seconds']+probe['GPU_seconds'],
        verification_optimizer_updates=48,verification_teacher_tokens=probe['verification_teacher_tokens'],verification_input_tokens=1572864,
        previous_related_GPU_seconds_preserved=previous,related_GPU_seconds=previous+r['GPU_seconds']+probe['GPU_seconds'],
        summary=summary,four_cell_analysis=review['four_cell_analysis'],original_three_cells_reused_unchanged=True,
        original_UI=dict(identity=processes[0],actual_alive_verified=True,HTTP=ui),
        limitations='Nonblind Codex content scores, one learned seed, shared data and repeated dev comparisons. '
            'Masking also changes actual teacher count/EOS fraction. The four-cell observation is not an independent human/causal or capacity-limit proof.',
        next_proposal=study.reference(proposal_path),next_action=proposal['next_action'],
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(destination,report)
    active_path=ROOT/'reports/phase6/interleaved_outcome_active_job.json'
    atomic_json(active_path,dict(status='actual_terminal_fourth_cell_rejected',actual_alive=False,observed_at=now(),actual_job=job,
        completion=study.reference(destination),restart_needed=False,Base_complete=False,Chat_started=False,quantization_started=False))
    files=[destination,active_path,proposal_path,study.CONFIG,study.PROBE_CONFIG,study.PROPOSAL,study.LEDGER,Path(__file__),
        ROOT/'scripts/record_interleaved_outcome_content.py',ROOT/'scripts/review_interleaved_outcome_order.py',ROOT/'scripts/interleaved_order_analysis.py',
        ROOT/'tests/test_interleaved_outcome_review.py',*[ROOT/p for p in study.SOURCES],
        ROOT/'reports/phase6/interleaved_outcome_tests.xml',ROOT/'reports/phase6/interleaved_outcome_review_tests.xml',
        ROOT/'reports/phase6/interleaved_outcome_review.json']
    files.extend(p for p in sorted(study.RUN.rglob('*')) if p.is_file() and p.suffix in ('.json','.jsonl','.log') and 'source' not in p.relative_to(study.RUN).parts)
    for folder in ('interleaved-outcome-order-probe-launcher-20261006','interleaved-outcome-order-train-launcher-20261006'):
        files.extend(p for p in sorted((ROOT/'reports/phase6'/folder).glob('*')) if p.is_file() and p.suffix in ('.json','.log'))
    files=list(dict.fromkeys(files));evidence={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files}
    archive=ROOT/'reports/phase6/interleaved_outcome_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve original completion archive')
    with tarfile.open(archive,'w:gz') as output:
        for p in files:output.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/'reports/phase6/interleaved_outcome_portable.json',dict(files=evidence,file_count=len(files),
        raw_bytes=sum(v['bytes'] for v in evidence.values()),archive=study.reference(archive),tensors_native_only=True))
    prefix=f'''混在順序×outcome/EOS教師の第4条件と全評価を完了、不採用（2026-10-06 JST）。Baseは未完了。完成・採用時に通知して停止し、Chat/Dialogue/SFT/量子化は開始しない。

actual{job['pid']}/boot{job['boot_id']}/start{job['start_ticks']}は実終了・不在。科学3068更新/実教師91641755/reference100M/physical100532224、source別窓・元教師・mask教師・digest/cursorは既3条件と一致。検証48更新/{probe['verification_teacher_tokens']}教師は科学と別。scienceGPU{r['GPU_seconds']:.6f}+probe{probe['GPU_seconds']:.6f}=新全{report['new_all_GPU_seconds']:.6f}秒/上限900。全256body/common472055byte・日本語192/331/1119・greedy80・bridge/retention128を完了し、全80rawに個別理由を保存（同raw8例は旧採点継承、非blind Codex/独立人手なし）。

新mask/mixedはBPB{summary['BPB']:.9f}、文法{summary['grammar2']}/関連{summary['relevance2']}/一貫性{summary['coherent']}/適切{summary['appropriate']}/EOS{summary['rates']['eos']}/反復{summary['rates']['repetition']}/Unicode-role-empty0（各80）。意味61.458%/JBLiMP77.039%/JCQA35.389%。歴史Web保持guardは通るが、strong23比一貫性-12/paired CI[-.2625,-.025]、mask/staged35比-24/CI[-.425,-.175]で内容・EOS・反復基準未達。4条件ではmixedがWeb保持、stagedが完結に優れる局所tradeoffを観測。mask効果の一貫性交互作用-5/CI[-.2,.0875]は0を含む。全旧採点/失敗/品質基準を保持し、独立seed/full dev/protected test/採用は未実施。今回比較は終了、weight/ratio/mask/source/CP/LR/decoder sweepで救済しない。

terminalのactive_job/全raw/review/会計/費用をinterleaved_outcome_completion/portable/archiveへ保存。元10B UI{processes[0]['pid']}/boot{processes[0]['boot_id']}/start{processes[0]['start_ticks']}をactual ps/HTTP親410f975d…/busy=falseで確認。関連series累積{report['related_GPU_seconds']:.6f}秒（全project費用ではない）。次はsource_gradient_attribution_proposal.jsonのread-only TRAIN勾配診断のみ。固定元親と今回終端/先頭16同TRAIN batches、5source-target groupの実token-mean CE勾配寄与/内積を測る。CPU準備30秒/新GPU全90秒/optimizer・学習教師0、実装/解析CPUtest/不変性・RNG/数値分解一致/永続PIDを先に用意する。未実装・未起動。局所勾配で原因や増量の有効性を断定せず、新学習介入は別の比較・予算を要する。Phase0–3/旧数値7失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status='Base_only_fourth_order_target_cell_complete_rejected_readonly_TRAIN_gradient_diagnostic_defined',updated_at=now(),
        interleaved_outcome_completion=study.reference(destination),interleaved_outcome_active_job=study.reference(active_path),
        source_gradient_attribution_proposal=study.reference(proposal_path),next_action=report['next_action'],
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(progress_path,progress)
    print(json.dumps(dict(status=report['status'],new_GPU_seconds=report['new_all_GPU_seconds'],related_GPU_seconds=report['related_GPU_seconds'],
        UI_pid=processes[0]['pid'],portable_files=len(files))))


if __name__=='__main__':main()
