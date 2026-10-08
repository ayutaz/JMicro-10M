"""CPU closeout of fixed same-stream grouping pilot; never automatic Base adoption."""
import argparse
import json
import math
from pathlib import Path
import sys
import urllib.request

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import numpy as np
import torch
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from base_gradient_accumulation_trainer import committed_group
from run_base_gradient_accumulation_pilot import CONFIG,RUN,checked,ref
from review_eos_5b_finish import validate_rows
from review_textbook_quantity_comparison import validate_notes
from run_eos_short_pilot import rate
from phase6_performance import alive

OUTPUT=ROOT/'reports/phase6/base_gradient_accumulation_pilot_completion.json'


def paired_summary(control,candidate,left,right):
    a,b=control['body'],candidate['body']
    if ([(v['doc_id'],v['body_tokens'],v['body_bytes']) for v in a['rows']]
            !=[(v['doc_id'],v['body_tokens'],v['body_bytes']) for v in b['rows']]):
        raise ValueError('Same actual256 DEV documents and byte denominators required')
    old=np.array([v['body_nll'] for v in a['rows']]);new=np.array([v['body_nll'] for v in b['rows']])
    sizes=np.array([v['body_bytes'] for v in a['rows']])
    draw=np.random.default_rng(42).integers(0,len(old),size=(10000,len(old)))
    delta=(new[draw]-old[draw]).sum(axis=1)/sizes[draw].sum(axis=1)/math.log(2)
    keys=sorted(left)
    coherent=np.array([int(right[k]['coherence']==2)-int(left[k]['coherence']==2) for k in keys])
    draw=np.random.default_rng(42).integers(0,80,size=(10000,80))
    return dict(BPB_difference=b['bpb']-a['bpb'],paired_document_BPB_difference95CI=np.quantile(delta,[.025,.975]).tolist(),
        coherence_count_difference=int(coherent.sum()),coherence_fraction_difference95CI=np.quantile(coherent[draw].mean(axis=1),[.025,.975]).tolist(),
        bootstrap_seed=42,bootstrap_samples=10000)


def main(template=False):
    if OUTPUT.exists(): raise ValueError('Preserve completed grouping pilot')
    c=read_json(CONFIG);job=read_json(RUN/'job.json');result=read_json(RUN/'result.json')
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Frozen learning source differs: '+name)
    if (alive(job) or job['status']!='complete' or not job['cumulative_GPU_ledger_closed']
            or not result['cumulative_GPU_ledger_closed'] or result['config']!=ref(CONFIG)
            or result['identity']!={k:job[k] for k in ('pid','boot_id','start_ticks')}
            or not 0<result['GPU_seconds']==job['GPU_seconds']<=c['GPU_cap_seconds']
            or result['baseline']!=c['baseline'] or result['scientific_teacher_tokens']!=94160195 or result['reused_control_teacher_tokens']!=94160195
            or not all(result['stream_checks'].values()) or not all(result['resume_gate']['checks'].values())):
        raise ValueError('Actual exited, bounded, matched original teacher pilot and CUDA gate required')
    checked(c['proposal']);base=checked(c['base_config'])
    state=torch.load(result['candidate_checkpoint']['path'],map_location='cpu',weights_only=False)
    if (sha256(Path(result['candidate_checkpoint']['path']))!=result['candidate_checkpoint']['sha256']
            or not committed_group(state) or state['grouping']['accumulation']!=4
            or state['grouping']['microbatches']!=10000 or state['counters']['update']!=2500
            or state['counters']!=result['counters']):
        raise ValueError('Exact finite2500-update/10000-microbatch candidate required')
    codec=Tokenizer(ROOT/base['tokenizer']);evaluations={};summaries={};scores={}
    cases={v['id']:v for v in (json.loads(s) for s in (ROOT/'eval/base.jsonl').read_text().splitlines()) if v['split']=='dev'}
    for arm in ('control','candidate'):
        raw=Path(result[arm+'_evaluation']['path']);ev=checked(result[arm+'_evaluation'])
        expected=result['baseline'] if arm=='control' else result['candidate_checkpoint']
        if ev['binding']!=dict(config_sha256=sha256(CONFIG),checkpoint=expected,suite_sha256=base['suite_sha256']) or not ev['RNG_unchanged']:
            raise ValueError('Exact raw evaluation/checkpoint binding required')
        rows=ev['outputs'];validate_rows(rows,codec)
        if (len(rows)!=80 or len({r['id'] for r in rows})!=80 or {r['id'] for r in rows}!=set(cases)
                or any(r['prefix']!=cases[r['id']]['prefix'] for r in rows)):
            raise ValueError('All original fixed80 prefixes required')
        body=ev['body']
        if (body['documents']!=256 or len(body['rows'])!=256 or len({v['doc_id'] for v in body['rows']})!=256
                or body['body_tokens']!=122343 or body['body_bytes']!=472055
                or any(v['body_tokens']!=v['scored_body_tokens'] or not math.isfinite(v['body_nll']) for v in body['rows'])
                or not math.isclose(body['bpb'],sum(v['body_nll'] for v in body['rows'])/math.log(2)/472055,rel_tol=1e-12)):
            raise ValueError('Full same-byte256 DEV required')
        notes_path=ROOT/f'reports/phase6/base_gradient_accumulation_{arm}_notes.json'
        if template:
            if notes_path.exists(): raise ValueError('Preserve individual content notes')
            atomic_json(notes_path,dict(reviewer='Codex nonblind; all80 require individual reading',
                independent_human_blind=False,all80_individually_read=False,generation_sha256=sha256(raw),
                notes=[[r['id'],None,None,None,None,''] for r in rows]))
            continue
        notes=read_json(notes_path)
        if notes.get('all80_individually_read') is not True: raise ValueError('All160 individual readings required')
        labels=validate_notes(rows,notes,sha256(raw));scores[arm]=labels;evaluations[arm]=ev
        summaries[arm]=dict(BPB=body['bpb'],rates=rate(rows),grammar2=sum(n['grammar']==2 for n in labels.values()),
            coherence2=sum(n['coherence']==2 for n in labels.values()),appropriate_end=sum(n['completion'] for n in labels.values()),
            notes=ref(notes_path),raw=ref(raw))
    if template:
        print('Created unscored all160 templates; no quality result');return
    old,new=summaries['control'],summaries['candidate']
    screen=dict(BPB_at_least2percent_better=new['BPB']<=.98*old['BPB'],
        **{k+'_nonworsening':new[k]>=old[k] for k in ('grammar2','coherence2','appropriate_end')},
        EOS_nonworsening=new['rates']['eos']>=old['rates']['eos'],
        repetition_nonworsening=new['rates']['repetition']<=old['rates']['repetition'],
        no_empty_role_unicode=all(new['rates'][k]==0 for k in ('empty','role_leak','unicode_failure')))
    absolute=dict(grammar_at_least56=new['grammar2']>=56,coherence_at_least27=new['coherence2']>=27,
        appropriate_at_least27=new['appropriate_end']>=27,EOS_at_least37=new['rates']['eos']>=37,
        repetition_at_most18=new['rates']['repetition']<=18,no_empty_role_unicode=screen['no_empty_role_unicode'])
    launcher=read_json(ROOT/'reports/phase6/base-gradient-accumulation-launcher-20261008/result.json')
    ui=read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=3) as response: model=json.load(response)
    if (launcher['status']!='complete' or launcher['exit_code'] or not launcher['UI_restore_command_succeeded']
            or not alive(ui) or model['busy'] or model['training_tokens']!=10000007168
            or model['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'):
        raise ValueError('Actual exited launcher and restored idle original10B UI required')
    advance=all(screen.values())
    atomic_json(OUTPUT,dict(status='same_stream_grouping_pilot_all160_review_complete',created_at=now(),result=ref(RUN/'result.json'),
        config=ref(CONFIG),reviewer_source=ref(Path(__file__)),summaries=summaries,prospective_advance_screen=screen,
        exploratory_advance_eligible=advance,fixed_grouping_pilot_closed=not advance,absolute_dev_screen=absolute,
        paired_differences=paired_summary(evaluations['control'],evaluations['candidate'],scores['control'],scores['candidate']),
        all160_individually_read=True,independent_human_blind=False,scientific_teacher_tokens=94160195,
        reused_control_teacher_tokens=94160195,verification_teacher_tokens=result['resume_gate']['verification_teacher_tokens'],
        GPU_seconds=result['GPU_seconds'],GPU_cap_seconds=c['GPU_cap_seconds'],process_exited=True,
        restored_UI_identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},restored_UI_model=model,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_scored=False,
        limits='One fresh seed42, repeated fixedDEV, nonblind160 readings. Grouping jointly changes noise/clipping/momentum/decay cadence/LR discretization. Pilot advance is not Base adoption or automatic longer training; all original retention/independent-trained-seed/fullDEV/protectedTEST/adoption gates remain pending.'))
    print(json.dumps(dict(status='pilot_review_complete',advance_screen=advance,summaries=summaries,Base_complete=False)))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--template',action='store_true')
    args=parser.parse_args();torch.set_num_threads(2);main(args.template)
