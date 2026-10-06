"""Preserve failed versions; fix the inherited gate's old LR constant."""
import sys
from pathlib import Path
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parents[1]/'scripts')]
import torch
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json


def main():
    old = ROOT/'reports/phase6/historical-parent-condition-comparison-v2-20261006/probe'
    job = read_json(old/'job.json')
    states = [torch.load(old/f'resume-gate/{r}.pt',map_location='cpu',weights_only=False) for r in ('continuous','resumed')]
    teachers = sum(s['supervised_tokens']-10477786961 for s in states)
    failure = dict(status='preserved_v2_inherited_gate_wrong_LR_constant', job=dict(path=str(old/'job.json'),sha256=sha256(old/'job.json')),
        initial_parent_preservation=read_json(old/'initial-parent-preservation.json'), GPU_seconds=job['GPU_elapsed_seconds'],
        GPU_optimizer_updates=8, verification_teacher_tokens=teachers, scientific_teacher_tokens=0,
        diagnosis='All 31 state/history/finite checks passed. Old gate expected .0002 instead of actual inherited .00001. Own new gate retains all fields and strictly checks .00001.',created_at=now())
    atomic_json(ROOT/'reports/phase6/historical_parent_v2_probe_failure.json',failure)
    p=read_json(ROOT/'reports/phase6/historical_parent_condition_comparison_v2_proposal.json')
    p['references']['v2_failed_probe']=failure['job']
    p['failed_probe_GPU_seconds']+=job['GPU_elapsed_seconds']
    p['failed_probe_verification_teacher_tokens']=teachers
    p['failed_probe_optimizer_updates']=8
    p['repair']='V3 own fullstate resume gate expects actual parent LR .00001; all fields and strict equality unchanged. V1/V2 sources and failures preserved; all failed GPU charged to same900s ceiling.'
    atomic_json(ROOT/'reports/phase6/historical_parent_condition_comparison_v3_proposal.json',p)
    for path in ('scripts/run_historical_parent_condition_comparison_v2.py','scripts/run_historical_parent_condition_comparison_v2.ps1','scripts/review_historical_parent_condition_comparison_v2.py','tests/test_historical_parent_comparison_v2.py'):
        s=(ROOT/path).read_text().replace('_v2','_v3').replace('-v2-','-v3-')
        if path.endswith('comparison_v2.py') and '/run_' in path:
            s=s.replace('from phase6_performance import alive,identity','from phase6_performance import alive,identity,finite_state')
            s=s.replace('latest,reconcile,resume_gate,detail=prior.latest,prior.reconcile,prior.resume_gate,prior.detail','latest,reconcile,detail=prior.latest,prior.reconcile,prior.detail')
            start=(ROOT/'scripts/run_condition_positive_comparison.py').read_text().split('def resume_gate(',1)[1].split('\ndef detail(',1)[0]
            gate='def resume_gate('+start.replace("math.isclose(r['lr'], .0002, rel_tol=1e-10)","inherited_lr_preserved(r['lr'])")
            s=s.replace('\ndef cpu_state(value):','\ndef inherited_lr_preserved(value):\n    return math.isclose(value, .00001, rel_tol=1e-10)\n\n\n'+gate+'\n\ndef cpu_state(value):')
        if path.startswith('tests/'):
            s+='\n\ndef test_historical_inherited_LR_is_strict_and_old_control_LR_rejected():\n    assert study.inherited_lr_preserved(.00001)\n    assert not study.inherited_lr_preserved(.0002)\n    assert not study.inherited_lr_preserved(.0001)\n    assert not study.inherited_lr_preserved(float("nan"))\n'
        target=ROOT/path.replace('_v2','_v3')
        if target.exists():raise ValueError('Preserve existing version')
        target.write_text(s,encoding='utf-8',newline='\n')
    # Own postprocessor, not part of frozen scientific source.
    s=(ROOT/'scripts/prepare_query_balance_content_review.py').read_text()
    s=s.replace('import run_condition_query_balance_comparison as study','import run_historical_parent_condition_comparison_v3 as study')
    s=s.replace("    return saved,refs", """    query_notes=ROOT/'reports/phase6/condition_query_balance_notes.json'
    query_raw=ROOT/'reports/phase6/condition-query-balance-comparison-20261006/evaluation/query_balanced/evaluation/generation.json'
    raw,notes=read_json(query_raw),read_json(query_notes)
    validate_notes(raw['outputs'],notes,sha256(query_raw))
    indexed={n[0]:n for n in notes['notes']}
    for row in raw['outputs']:
        k=key(row);note=indexed[row['id']]
        if k in saved and saved[k]!=note:raise ValueError('Conflicting exact query peer notes')
        saved[k]=note
    refs.append(dict(notes=study.reference(query_notes),generation=study.reference(query_raw)))
    return saved,refs""")
    s=s.replace('condition_query_balance_notes.json','historical_parent_condition_notes.json',1) if False else s
    s=s.replace("path = ROOT / 'reports/phase6/condition_query_balance_notes.json'","path = ROOT / 'reports/phase6/historical_parent_condition_notes.json'")
    (ROOT/'scripts/prepare_historical_parent_content_review.py').write_text(s,encoding='utf-8',newline='\n')


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python required')
    main()
