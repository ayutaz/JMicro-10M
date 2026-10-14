"""Create separate measured/gated workflow; preserve every old recipe and result."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def renamed(path):
    return ((ROOT/path).read_text().replace('base_confidence_penalty', 'base_document_balance')
        .replace('base-confidence-penalty', 'base-document-balance')
        .replace('ConfidencePenaltyTrainer', 'DocumentBalancedTrainer')
        .replace('confidence_penalty', 'document_balance')
        .replace('confidence_positions', 'balance_positions')
        .replace('confidence_losses', 'document_losses')
        .replace('confidence_KL_loss', 'balance_mean_inverse_length')
        .replace('prediction_entropy', 'balance_weight_ratio')
        .replace('20261007', '20261014'))


def save(path, value):
    target = ROOT/path
    if target.exists(): raise ValueError('Preserve independent workflow '+path)
    target.write_text(value)


def main():
    probe = renamed('scripts/probe_base_confidence_penalty.py')
    probe = probe.replace('tests/test_base_document_balance_trainer.py', 'tests/test_base_document_balance.py')
    probe = probe.replace("CONTROL", "CONTROL")
    start, end = probe.index('def prepare():'), probe.index('\ndef inspect():')
    probe = probe[:start]+'''def prepare():
    if CONFIG.exists(): raise ValueError('Preserve one prospective document-balance contract')
    old = read_json(ROOT/'configs/phase6/base_confidence_penalty_comparison.json')
    old_probe = read_json(ROOT/'configs/phase6/base_confidence_penalty_probe.json')
    tests = ROOT/'reports/phase6/base_document_balance_CPU_tests.xml'
    suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites) != 11 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Actual eleven analytic/state/mask CPU checks required')
    tok = Tokenizer(ROOT/old['tokenizer'])
    sampler = OriginalTrainCorpusSampler(old['source_binding']['pool'],old['source_binding']['manifest_sha256'],tok,old['goals'],42)
    if sampler.binding != old['source_binding']: raise ValueError('Accepted stream identity differs')
    rows = [row for _ in range(4) for row in sampler.take(48)]
    weights = [1/(r['original_body_tokens']+1) for r in rows for _ in range(r['teacher_tokens'])]
    mean = statistics.mean(weights)
    cv = statistics.pstdev(weights)/mean
    ratio = max(weights)/min(weights)
    diagnostic = dict(created_at=now(),TRAIN_windows=len(rows),selected_gold_positions=len(weights),
        minimum_original_teachers=min(r['original_body_tokens']+1 for r in rows),
        maximum_original_teachers=max(r['original_body_tokens']+1 for r in rows),
        weight_max_min_ratio=ratio,selected_gold_weight_CV=cv,passed=ratio>=2 and cv>=.25,
        screen='first192 accepted TRAIN windows; ratio>=2 and selected_gold_weight_CV>=.25',
        row_metadata=[dict(source=r['source'],original_teachers=r['original_body_tokens']+1,
            selected_gold=r['teacher_tokens'],original_body_sha256=r['full_original_body_sha256']) for r in rows],
        scientific_teacher_positions=0,optimizer_updates=0,GPU_seconds=0,TEST_read=False,
        limitations='Small fixed sampler diagnostic, not population audit, cause proof, model quality or uniform document draws')
    diagnostic_path=ROOT/'reports/phase6/base_document_balance_length_diagnostic.json'
    if diagnostic_path.exists(): raise ValueError('Preserve first observed CPU diagnostic')
    atomic_json(diagnostic_path,diagnostic)
    references={name:ref(ROOT/'reports/phase6'/name) for name in (
        'base_teacher_decay_2b_completion.json','base_residual_train_dev_history_completion.json',
        'base_residual_consumed_unit_provenance.json','base_confidence_penalty_comparison_completion.json')}
    proposal=dict(created_at=now(),user_resumption='6まで進めてください',question='Does inverse-original-document-length CE improve generation with the same original100M teachers?',
        recipe=RECIPE,references=references,length_diagnostic=ref(diagnostic_path),CPU_checks=ref(tests),
        native_parameters=10001152,extra_parameters=0,original_teachers=100000000,
        novelty='Full original unit weights include body and EOS equally; distinct from EOS-only weighting, genre quotas, label smoothing, confidence KL and auxiliary objectives. Mechanistic source inspection establishes token average in old trainer, not global absence of every related method.',
        limitations='Not a proven cause; index-byte draw is not uniform documents; short noisy units can gain weight; no external performance claim.',
        acceptance='Exact same stream/counters/full sampler, own CUDA finite maximum shape and full-state resume, measured frozen budget, all80 content and all unchanged matched/strong/absolute/historical gates before qualified-only independent seed/fullDEV/protectedTEST/adoption.',
        failure='Close fixed condition on data, numeric, state, budget or quality failure; no exponent, clipping, LR, parent, source, budget or seed rescue.',
        GPU_cap_seconds=4800,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(PROPOSAL,proposal)
    if not diagnostic['passed']:
        print(json.dumps(dict(status='length_diagnostic_rejected_GPU0',diagnostic=ref(diagnostic_path))))
        return
    fields=('parent','parent_size','parent_mtime_ns','source_binding','goals','tokenizer','tokenizer_sha256',
        'dev_shards','dev_manifest_sha256','suite_sha256','evaluation')
    plan=dict(**{k:old[k] for k in fields},created_at=now(),proposal=ref(PROPOSAL),CPU_tests=ref(tests),
        source_sha256={s:sha256(ROOT/s) for s in SOURCES},payload=old_probe['payload'],batch=48,seed=42,
        probe_GPU_cap_seconds=180,total_GPU_cap_seconds=4800,warmup_updates=3,timed_updates=32,
        control_CE=old['control_CE'],control_result=old['control_CE'],Base_complete=False,Chat_started=False,quantization_started=False)
    atomic_json(CONFIG,plan)
    print(json.dumps(dict(status='document_balance_probe_frozen_GPU0',length_ratio=ratio,weight_CV=cv,config_sha256=sha256(CONFIG))))

''' + probe[end:]
    probe = probe.replace('document_losses(t.model,ids,targets)',
        "document_losses(t.model,ids,targets,torch.full((48,),window['original_body_tokens']+1,device='cuda',dtype=torch.long))")
    save('scripts/probe_base_document_balance.py', probe)
    run = renamed('scripts/run_base_confidence_penalty.py')
    run = run.replace("CONTROL = ROOT/'reports/phase6/natural-context-contrast-comparison-20261014'",
        "CONTROL = ROOT/'reports/phase6/natural-context-contrast-comparison-20261007'")
    run = run.replace('confidence-loss', 'document-weighted-loss')
    save('scripts/run_base_document_balance.py', run)
    review = renamed('scripts/review_base_confidence_penalty.py')
    start = review.index('    if any(not all(math.isfinite(r[k])')
    end = review.index('    if template:', start)
    review = review[:start]+'''    if any(not all(math.isfinite(r[k]) for k in ('CE_loss','balance_mean_inverse_length','balance_weight_ratio','combined_loss','gradient_norm')) or
            not 0<r['balance_mean_inverse_length']<=.5 or r['balance_weight_ratio']<1 or r['combined_loss']<0 or
            r['document_balance']!=dict(updates=u,positions=r['supervised_tokens']) or
            r['balance_positions_this_update']!=r['CE_targets_this_update'] or r['decoder_forwards_this_update']!=1 or
            len(r['original_document_teachers'])!=r['original_windows_this_update'] or
            any(n<2 for n in r['original_document_teachers'])
            for u,r in history.items()): raise ValueError('Actual finite original-length-weighted CE history required')
''' + review[end:]
    review = review.replace('only added native confidence loss differs', 'only original-document CE contribution weighting differs')
    review = review.replace('prediction entropy regularization differs', 'original-document contribution weighting differs')
    review = review.replace('confidence-loss transition', 'document-weighted-loss transition')
    save('scripts/review_base_document_balance.py', review)
    save('tests/test_base_document_balance_run.py', renamed('tests/test_base_confidence_penalty_run.py'))
    for kind in ('probe', 'run'):
        save(f'scripts/{kind}_base_document_balance.ps1', renamed(f'scripts/{kind}_base_confidence_penalty.ps1'))
    print('Independent scripts created; no GPU work or scientific learning')


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
