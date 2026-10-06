"""Actual two-arm accounting, all160 raw content, and unchanged double controls."""
import json
import math
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive,finite_state
from run_eos_short_pilot import equal_state,rate
from review_eos_5b_finish import validate_rows
from review_textbook_quantity_comparison import validate_notes
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
import run_parameter_displacement_anchor_v3 as study


def content(arm,ev,record,base,raw,notes):
    rows=ev['generation']['outputs']
    if (ev['checkpoint_sha256']!=record['checkpoint_sha256'] or ev['binding']!=record['binding']
            or read_json(raw)!=ev['generation'] or ev['greedy_rates']!=rate(rows)
            or ev['protected_test_used'] or not ev['evaluation_RNG_isolated']):
        raise ValueError('Actual raw model evaluation binding differs: '+arm)
    validate_rows(rows,Tokenizer(ROOT/base['tokenizer']))
    cases={r['id']:r for r in (json.loads(s) for s in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    if len(rows)!=80 or {r['id'] for r in rows}!=set(cases) or any(r['prefix']!=cases[r['id']]['prefix'] for r in rows):
        raise ValueError('Complete original80 dev required')
    scores=validate_notes(rows,read_json(notes),sha256(raw));body=ev['body']
    if (body['documents']!=256 or len(body['rows'])!=256 or body['body_tokens']!=122343 or body['body_bytes']!=472055
            or any(r['body_tokens']!=r['scored_body_tokens'] or not math.isfinite(r['body_nll']) for r in body['rows'])
            or not math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/472055,rel_tol=1e-12)):
        raise ValueError('Full256 same common bytes required')
    if any(not ev['diagnostics'][k]['complete'] or ev['diagnostics'][k]['count']!=n for k,n in dict(semantics=192,jblimp=331,jcqa=1119).items()):
        raise ValueError('All Japanese diagnostics required')
    return dict(BPB=body['bpb'],rates=ev['greedy_rates'],grammar2=sum(n['grammar']==2 for n in scores.values()),
        relevance2=sum(n['relevance']==2 for n in scores.values()),coherent=sum(n['coherence']==2 for n in scores.values()),
        appropriate=sum(n['completion'] for n in scores.values()),notes_sha256=sha256(notes),generation_sha256=sha256(raw),
        Japanese={k:ev['diagnostics'][k]['primary']['accuracy']['point'] for k in ('semantics','jblimp','jcqa')}),scores


def accounting(parent,state,record,history,c,arm):
    sampler=state['sampler'];lineage=state['lineage'];spec=state['spec']
    if (not finite_state(state) or sampler['source_teachers']!=study.GOALS
            or sampler.get('source_order')!=list(study.prior.SOURCE_ORDER)
            or state['supervised_tokens']-parent['supervised_tokens']!=study.TOTAL
            or state['tokens']-parent['tokens']!=sum(sampler['source_tokens'].values())
            or state['body_bytes']-parent['body_bytes']!=sum(sampler['source_body_bytes'].values())
            or state['update']-parent['update']!=sampler['position'] or len(history)!=sampler['position']
            or [r['update'] for r in history]!=list(range(parent['update']+1,state['update']+1))
            or state['weighted_teacher_mass']!=study.TOTAL or state['focus_teacher_tokens']!=sum(sampler['source_focus_teachers'].values())
            or state['study_binding']!=study.binding(c,study.CONFIG,arm) or record['binding']!=state['study_binding']
            or record['additional_supervised_tokens']!=study.TOTAL or record['parameter_penalty_teacher_tokens']
            or spec['parameter_coefficient']!=c['coefficients'][arm] or spec['research_kind']!=study.KIND
            or spec['anchor_checkpoint']!=c['parent'] or lineage['parent']!=c['parent']
            or not lineage['no_reheat'] or not equal_state(lineage['actual_parent_sampler'],parent['sampler'])
            or not equal_state(lineage['parent_scheduler'],parent['scheduler'])
            or any(g['lr']!=.00001 for g in state['optimizer']['param_groups'])):
        raise ValueError('Completed fullstate/teacher/source/anchor accounting differs')
    digest=__import__('hashlib').sha256()
    from jmicro.model import JMicroModel
    with torch.random.fork_rng(devices=[]):model=JMicroModel(parent['model_config'])
    for k,_ in model.named_parameters():
        digest.update(k.encode());digest.update(parent['model'][k].numpy().tobytes())
    if digest.hexdigest()!=lineage['anchor_initial_digest'] or record['anchor_initial_digest']!=digest.hexdigest():
        raise ValueError('Actual anchor does not bind original unique parent parameters')
    for row in history:
        if (any(not math.isfinite(row[k]) for k in ('loss','CE_loss','parameter_penalty','gradient_norm'))
                or row['parameter_coefficient']!=c['coefficients'][arm] or row['parameter_penalty_teacher_tokens']
                or row['parameter_penalty']<0 or row['lr']!=.00001
                or not math.isclose(row['loss'],row['CE_loss']+row['parameter_penalty'],rel_tol=1e-6,abs_tol=1e-6)):
            raise ValueError('Full actual objective history differs')
    for k in ('token_digest','focus_token_digest'):
        if history[-1][k]!=state[k] or record[k]!=state[k]:raise ValueError('Terminal raw input digest differs')
    if record['sampler']!=sampler:raise ValueError('Terminal sampler record differs')
    initial=parent['sampler']['streams']['web']['sampler'];final=sampler['streams']['web']['sampler']
    if any(initial[k]!=final[k] for k in ('seed','context','blocks')):raise ValueError('Actual Web recipe differs')
    blocks=(final['epoch']-initial['epoch'])*initial['blocks']+final['position']-initial['position']
    if blocks*initial['context']!=sampler['source_tokens']['web']:raise ValueError('Actual Web cursor exposure differs')
    return dict(completed_updates=len(history),teachers=study.TOTAL,physical_input_positions=record['additional_input_tokens'],
        parameter_penalty_teacher_tokens=0,final_parameter_penalty=history[-1]['parameter_penalty'],
        actual_Web_blocks_consumed=blocks,source_teachers=sampler['source_teachers'],source_EOS=sampler['source_eos'])


def main():
    torch.set_num_threads(2);c=study.inspect(study.CONFIG);job=read_json(study.RUN/'job.json');r=read_json(study.RUN/'compare-result.json')
    if (job['status']!='complete' or alive(job) or r['config_sha256']!=sha256(study.CONFIG)
            or r['GPU_seconds']!=job['GPU_elapsed_seconds'] or r['GPU_seconds']+c['verification_GPU_seconds']>study.CEILING
            or r['scientific_teacher_tokens']!=2*study.TOTAL or not r['all_scientific_input_streams_match']
            or set(r['checkpoints'])!=set(study.ARMS) or set(r['evaluations'])!=set(study.ARMS)):
        raise ValueError('Actual terminal both100M within original cumulative ceiling required')
    parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);base=read_json(Path(c['original_config']['path']))
    summaries={};scores={};audits={};states={}
    for arm in study.ARMS:
        record=r['checkpoints'][arm];study.check_reference(dict(path=record['checkpoint'],sha256=record['checkpoint_sha256']))
        state=torch.load(record['checkpoint'],map_location='cpu',weights_only=False);states[arm]=state
        history=[json.loads(s) for s in (study.RUN/arm/'training/metrics.jsonl').read_text().splitlines()]
        audits[arm]=accounting(parent,state,record,history,c,arm)
        summaries[arm],scores[arm]=content(arm,r['evaluations'][arm],record,base,
            study.RUN/f'evaluation/{arm}/evaluation/generation.json',study.RUN/f'{arm}-content-notes.json')
        for key in ('transfer','retention'):
            t=r[key][arm]
            if t['evaluated_requests']!=512 or not all(t['checks'].values()) or t['checkpoint_sha256']!=record['checkpoint_sha256']:
                raise ValueError('Both complete actual read-only128 transfer suites required')
    a,b=[states[arm] for arm in study.ARMS]
    for k in ('sampler','token_digest','focus_token_digest','tokens','supervised_tokens','body_bytes','focus_teacher_tokens','weighted_teacher_mass','update'):
        if not equal_state(a[k],b[k]):raise ValueError('Scientific matched input stream/counters differ')
    previous=read_json(ROOT/'reports/phase6/source-order-condition-comparison-v2-20261006/compare-result.json')
    strong=previous['evaluations']['source_order'];strong_record=previous['checkpoints']['source_order']
    if dict(path=strong_record['checkpoint'],sha256=strong_record['checkpoint_sha256'])!=c['strong_control']:
        raise ValueError('Original strong staged checkpoint differs')
    summaries['strong_staged'],scores['strong_staged']=content('strong_staged',strong,strong_record,base,
        ROOT/'reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/generation.json',
        ROOT/'reports/phase6/source_order_condition_notes.json')
    if (summaries['strong_staged']['coherent']!=23 or summaries['strong_staged']['rates']['eos']!=76
            or summaries['strong_staged']['rates']['repetition']!=2):raise ValueError('Original stronger quality baseline changed')
    comparisons={}
    for name,control in [('matched_staged_CE',r['evaluations']['matched_staged_CE']),('strong_staged',strong)]:
        candidate=r['evaluations']['parameter_anchor']
        if ([(v['id'],v['prefix']) for v in control['generation']['outputs']]!=[(v['id'],v['prefix']) for v in candidate['generation']['outputs']]
                or [(v['doc_id'],v['body_tokens'],v['body_bytes']) for v in control['body']['rows']]!=[(v['doc_id'],v['body_tokens'],v['body_bytes']) for v in candidate['body']['rows']]):
            raise ValueError('Identical complete original common examples required')
        comparisons[name]=quality_gates(control,candidate,scores[name],scores['parameter_anchor'],'content')
    summary=summaries['parameter_anchor'];rates=summary['rates']
    absolute=dict(grammar_at_least56=summary['grammar2']>=56,coherence_at_least27=summary['coherent']>=27,
        appropriate_at_least27=summary['appropriate']>=27,EOS_at_least37=rates['eos']>=37,repetition_at_most18=rates['repetition']<=18,
        no_empty_role_unicode=all(rates[k]==0 for k in ('empty','role_leak','unicode_failure')))
    study.check_reference(base['reference']['web_screen'])
    original=adoption_checks(read_json(Path(base['reference']['web_screen']['path'])),r['evaluations']['parameter_anchor'])
    eligible=all(p['passed'] for p in comparisons.values()) and all(absolute.values()) and all(original.values())
    report=dict(status='both100M_all160_content_accounting_and_double_controls_reviewed',created_at=now(),
        config_sha256=sha256(study.CONFIG),result_sha256=sha256(study.RUN/'compare-result.json'),summaries=summaries,
        accounting=audits,quality_comparisons=comparisons,absolute_dev_screen=absolute,original_Web=original,
        eligible_for_final_Base_validation=eligible,scientific_teacher_tokens=2*study.TOTAL,
        actual_GPU_seconds=r['GPU_seconds'],probe_and_failed_GPU_seconds=c['verification_GPU_seconds'],
        all160_individually_read=True,independent_human_blind=False,Base_complete=False,Base_adopted=False,
        protected_test_used=False,quality_criteria_unchanged=True,Chat_started=False,quantization_started=False,
        next_action='Only qualified pilot permits independent learned recipe seed/full dev/protected test/adoption; '
            'otherwise terminate this single coefficient/anchor/source/decoder comparison without salvage sweep.')
    destination=study.RUN/'review.json'
    if destination.exists():raise ValueError('Preserve original terminal double-control review')
    atomic_json(destination,report);atomic_json(ROOT/'reports/phase6/parameter_displacement_anchor_review.json',report)
    print(dict(summaries=summaries,eligible=eligible))


if __name__=='__main__':main()
