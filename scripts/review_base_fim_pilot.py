"""Review all80 raw-bound FIM outputs; pilot success is not Base adoption."""
import argparse
import json
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from run_base_fim_pilot import CONFIG,RUN,matched,binding
from base_fim_trainer import committed_state
from base_fim_pilot_protocol import validate_body,validate_raw,notes_scores,quality,rates,DEV_PIN,TEACHERS,UPDATES
from isolated_base_evaluation import validate_isolated_generation
from jmicro.evaluation_boundary import load_dev_suite
from jmicro.experiment import sha256,now
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import alive


def review(template=False):
    c=json.loads(CONFIG.read_text());pin=sha256(CONFIG)
    for source,digest in c['sources'].items():
        if sha256(Path(__file__).resolve().parents[1]/source)!=digest:
            raise ValueError('Frozen scientific source changed: '+source)
    result=json.loads((RUN/'result.json').read_text());job=json.loads((RUN/'job.json').read_text())
    if (job['status']!='complete' or alive(job) or not job['cumulative_GPU_ledger_closed']
            or result['config_sha256']!=pin or result['binding']!=binding(pin,c)
            or job['result_sha256']!=sha256(RUN/'result.json')
            or result['scientific_teacher_positions']!=TEACHERS
            or result['GPU_occupancy_seconds']>c['scientific_GPU_cap_seconds']
            or result['total_GPU_seconds_including_probe']>3600):
        raise ValueError('Actual terminal scientific process/config/budget required')
    p=json.loads(Path(c['proposal']['path']).read_text());codec=Tokenizer(Path(__file__).resolve().parents[1]/p['tokenizer']['path'])
    suite=load_dev_suite(Path(c['DEV_manifest']['path']),DEV_PIN)
    for key in ('control_checkpoint','control_evaluation','control_notes'):
        if sha256(Path(c[key]['path']))!=c[key]['sha256']:raise ValueError('Original control evidence changed')
    record=result['training'];path=Path(record['checkpoint'])
    if sha256(path)!=record['checkpoint_sha256']:raise ValueError('Scientific checkpoint changed')
    state=torch.load(path,map_location='cpu',weights_only=False)
    control_state=torch.load(c['control_checkpoint']['path'],map_location='cpu',weights_only=False)
    checks=matched(control_state,state)
    if (not committed_state(state) or state['binding']!=result['binding'] or not all(checks.values())
            or checks!=record['matched_checks'] or state['counters']['update']!=UPDATES):
        raise ValueError('Actual terminal full state/original stream/control coupling required')
    metric_path=RUN/'metrics.jsonl';count=teachers=0;last=None
    with metric_path.open() as stream:
        for line in stream:
            row=json.loads(line);count+=1
            if row['update']!=count or not row['committed_update'] or row['CE_targets_this_update']<=0:
                raise ValueError('Each completed scientific update required')
            teachers+=row['CE_targets_this_update']
            if row['supervised_tokens']!=teachers:raise ValueError('Each actual teacher increment required')
            last=row
    if (count!=UPDATES or teachers!=TEACHERS or last['token_digest']!=state['counters']['token_digest']
            or last['FIM_counters']!=state['sampler']['FIM_counters']):
        raise ValueError('All10000 completed update records/final stream required')
    candidate=result['evaluation'];control=json.loads(Path(c['control_evaluation']['path']).read_text())
    raw_path=RUN/'evaluation/generation.json';generation=json.loads(raw_path.read_text());raw_pin=sha256(raw_path)
    validate_isolated_generation(generation,Path(c['DEV_manifest']['path']),DEV_PIN)
    if (generation['binding']!=result['binding'] or generation['checkpoint_sha256']!=record['checkpoint_sha256']
            or candidate['generation_sha256']!=raw_pin or candidate['outputs']!=generation['outputs']
            or not candidate['evaluation_RNG_isolated']):raise ValueError('Actual generation binding/RNG differs')
    for ev in (candidate,control):validate_body(ev['body']);validate_raw(ev['outputs'],codec,suite)
    body_key=lambda ev:[(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in ev['body']['rows']]
    if body_key(candidate)!=body_key(control):raise ValueError('Common DEV256 corpus differs')
    if template:
        output=RUN/'notes_template.json'
        if output.exists():raise ValueError('Do not overwrite individual review template')
        atomic_json(output,dict(generation_sha256=raw_pin,reviewer='UNSCORED',independent_human_blind=False,
            notes=[[r['id'],None,None,None,None,''] for r in candidate['outputs']]))
        print('All80 unscored template saved; not quality evidence');return
    notes=json.loads((RUN/'notes.json').read_text());old_notes=json.loads(Path(c['control_notes']['path']).read_text())
    a=notes_scores(control['outputs'],old_notes,c['control_evaluation']['sha256'])
    b=notes_scores(candidate['outputs'],notes,raw_pin)
    q=quality(control,candidate,a,b)
    summary=lambda ev,s:dict(BPB=ev['body']['bpb'],grammar2=sum(v['grammar']==2 for v in s.values()),
        coherence2=sum(v['coherence']==2 for v in s.values()),appropriate=sum(v['completion'] for v in s.values()),rates=rates(ev['outputs']))
    output=dict(status='exact_fresh_FIM_pilot_all80_reviewed',created_at=now(),config_sha256=pin,
        result_sha256=sha256(RUN/'result.json'),annotations_sha256=sha256(RUN/'notes.json'),
        matched_checks=checks,summaries=dict(control=summary(control,a),candidate=summary(candidate,b)),
        pilot_quality=q,eligible_for_measured_main_proposal=q['passed'],fixed_protocol_closed=not q['passed'],
        all80_individually_read=True,independent_human_blind=False,Base_qualified=False,Base_adopted=False,
        independent_training_completed=False,fullDEV_completed=False,fresh_TEST_prepared=False,
        next_action='Define measured full-quality main comparison only if pilot passes; this pilot cannot authorize final adoption.')
    atomic_json(RUN/'review.json',output)
    print(json.dumps(output,ensure_ascii=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--template',action='store_true');args=parser.parse_args()
    review(args.template)
