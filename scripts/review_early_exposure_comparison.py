"""Raw-bound all320 content, exact completed teacher accounting and unchanged gates."""
import argparse
import json
import math
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive, finite_state
from run_eos_short_pilot import equal_state, rate
from review_eos_5b_finish import validate_rows
from review_textbook_quantity_comparison import validate_notes
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
import run_early_exposure_comparison as study

POINTS = ('final100M', study.ARM)


def notes_path(arm):
    return ROOT / 'reports/phase6/original_web_retention_notes.json' if arm == 'final100M' else ROOT / 'reports/phase6/early_exposure_notes.json'


def point(arm, base, record, ev, template=False):
    raw = study.previous.RUN / 'evaluation/original_web/evaluation/generation.json' if arm == 'final100M' else study.RUN / f'evaluation/{arm}/evaluation/generation.json'
    rows = ev['generation']['outputs']
    if (ev['binding'] != record['binding'] or ev['checkpoint_sha256'] != record['checkpoint_sha256']
            or read_json(raw) != ev['generation'] or ev['greedy_rates'] != rate(rows)
            or ev['protected_test_used'] or not ev['evaluation_RNG_isolated']):
        raise ValueError('Actual raw generation/binding required')
    validate_rows(rows, Tokenizer(ROOT / base['tokenizer']))
    cases = {r['id']:r for r in (json.loads(s) for s in (ROOT / 'eval/base.jsonl').read_text().splitlines()) if r['split'] == 'dev'}
    if len(rows) != 80 or {r['id'] for r in rows} != set(cases) or any(r['prefix'] != cases[r['id']]['prefix'] for r in rows):
        raise ValueError('Fixed originaldev80 differs')
    if template:
        path = notes_path(arm)
        if path.exists(): raise ValueError('Preserve existing notes')
        atomic_json(path, dict(reviewer='Codex nonblind; all80 individually read', independent_human_blind=False,
            generation_sha256=sha256(raw), notes=[[r['id'],None,None,None,None,''] for r in rows]))
        return
    scores = validate_notes(rows, read_json(notes_path(arm)), sha256(raw)); body = ev['body']
    if (body['documents'] != 256 or len(body['rows']) != 256 or body['body_bytes'] != 472055 or body['body_tokens'] != 122343
            or any(r['body_tokens'] != r['scored_body_tokens'] or not math.isfinite(r['body_nll']) for r in body['rows'])
            or not math.isclose(body['bpb'], sum(r['body_nll'] for r in body['rows']) / math.log(2) / 472055, rel_tol=1e-12)):
        raise ValueError('Common-byte full256 body dev required')
    if any(not ev['diagnostics'][k]['complete'] or ev['diagnostics'][k]['count'] != n for k,n in dict(semantics=192,jblimp=331,jcqa=1119).items()):
        raise ValueError('All Japanese diagnostics required')
    return dict(BPB=body['bpb'], rates=ev['greedy_rates'], grammar2=sum(v['grammar']==2 for v in scores.values()),
        relevance2=sum(v['relevance']==2 for v in scores.values()), coherent=sum(v['coherence']==2 for v in scores.values()),
        appropriate=sum(v['completion'] for v in scores.values()), generation_sha256=sha256(raw), notes_sha256=sha256(notes_path(arm)),
        Japanese={k:ev['diagnostics'][k]['primary']['accuracy']['point'] for k in ('semantics','jblimp','jcqa')},
        additional_teacher_tokens=record['additional_supervised_tokens'], independent_human_blind=False), scores


def fit_summary(rows):
    result={}
    for source in ('web','story','ordinary_textbook','conditional_textbook'):
        values=[r for r in rows if r['source']==source]
        if len(values)!=4 or {r['draw'] for r in values}!={0,1,2,3}:raise ValueError('Fixed4 source draws required')
        teachers=sum(r['teachers'] for r in values);eos=sum(r['EOS_teachers'] for r in values)
        full=sum(r['full_CE']*r['teachers'] for r in values);end=sum(r['EOS_CE']*r['EOS_teachers'] for r in values)
        result[source]=dict(full_CE=full/teachers,body_CE=(full-end)/(teachers-eos),EOS_CE=end/eos,teachers=teachers,EOS_teachers=eos)
    return result


def audit():
    c,base,previous,old,_,_=study.inspect();r=read_json(study.RUN/'compare-result.json');job=read_json(study.RUN/'job.json')
    if (job['status']!='complete' or alive(job) or r['GPU_seconds']!=job['GPU_seconds'] or r['GPU_seconds']>study.LIMIT
            or r['config_sha256']!=sha256(study.CONFIG) or r['scientific_teacher_tokens'] or r['optimizer_updates']
            or not r['RNG_restored'] or r['Base_adopted'] or r['Chat_started'] or r['quantization_started'] or r['protected_test_used']
            or set(r['evaluations'])!=set(POINTS) or r['evaluations']['final100M']!=previous['evaluations'][study.previous.ARM]
            or r['checkpoints']['final100M']!=previous['checkpoints'][study.previous.ARM]):
        raise ValueError('Terminal bounded read-only comparison required')
    state=torch.load(c['early']['checkpoint']['path'],map_location='cpu',weights_only=False)
    study.early_contract(state,c['early'])
    if not finite_state(state):raise ValueError('Saved early model/Adam must be finite')
    import itertools
    with (study.previous.RUN/'original_web/training/metrics.jsonl').open() as stream:
        history=[json.loads(line) for line in itertools.islice(stream,250)]
    if (len(history)!=250 or [v['update'] for v in history]!=list(range(305177,305427))
            or any(not math.isfinite(v['loss']) or not math.isfinite(v['gradient_norm']) or v['lr']!=.0002 for v in history)
            or history[-1]['token_digest']!=state['token_digest'] or history[-1]['focus_token_digest']!=state['focus_token_digest']
            or state['body_bytes']-state['lineage']['parent_body_bytes']!=sum(state['sampler']['source_body_bytes'].values())
            or r['checkpoints'][study.ARM]['binding']!=study.binding(c)
            or r['checkpoints'][study.ARM]['additional_supervised_tokens']!=8150782):
        raise ValueError('Actual earliest checkpoint/history identity differs')
    del state
    summaries,scores={},{}
    for arm in POINTS:summaries[arm],scores[arm]=point(arm,base,r['checkpoints'][arm],r['evaluations'][arm])
    reviewed=read_json(Path(c['references']['final_review']['path']))['summaries']['original_web']
    if summaries['final100M']!=reviewed:raise ValueError('Completed final100M content changed')
    web=read_json(Path(base['reference']['web_screen']['path']));study.check_reference(base['reference']['web_screen'])
    targets=lambda ev:[(v['doc_id'],v['body_tokens'],v['body_bytes']) for v in ev['body']['rows']]
    if any(targets(ev)!=targets(web) for ev in r['evaluations'].values()):raise ValueError('Common-byte targets differ')
    comparison=quality_gates(r['evaluations']['final100M'],r['evaluations'][study.ARM],scores['final100M'],scores[study.ARM],'content')
    s=summaries[study.ARM]
    absolute=dict(grammar_at_least56=s['grammar2']>=56,coherence_at_least27=s['coherent']>=27,appropriate_at_least27=s['appropriate']>=27,
        EOS_at_least37=s['rates']['eos']>=37,repetition_at_most18=s['rates']['repetition']<=18,
        no_empty_role_unicode=all(s['rates'][k]==0 for k in ('empty','role_leak','unicode_failure')))
    original=adoption_checks(web,r['evaluations'][study.ARM])
    for suite,key in (('bridge','transfer'),('retention','retention')):
        if set(r[key])!=set(POINTS) or r[key]['final100M']!=previous[key][study.previous.ARM]:raise ValueError('Cached final128 changed')
        t=r[key][study.ARM];case_key='source_cases' if suite=='bridge' else 'retention_cases'
        if (t['config_sha256']!=sha256(study.CONFIG) or t['checkpoint_sha256']!=c['early']['checkpoint']['sha256']
                or t['cases_sha256']!=c['references'][case_key]['sha256'] or t['evaluated_requests']!=512 or not all(t['checks'].values())
                or t['optimizer_updates'] or t['scientific_teacher_tokens'] or t['protected_test_used']):
            raise ValueError('Actual early read-only128 binding differs')
        prepared=read_json(Path(c['references'][case_key]['path']));rows=[]
        for start in range(0,512,16):
            batch=read_json(study.RUN/f'transfer/{suite}/{study.ARM}/{start:04d}.json')
            if any(batch[k]!=t[k] for k in ('config_sha256','checkpoint_sha256','cases_sha256')):raise ValueError('Raw batch differs')
            study.ranking.validate_scores(batch['rows'],prepared['cases'][start:start+16]);rows.extend(batch['rows'])
        if t['summary']!=study.summarize_transfer(rows,prepared):raise ValueError('Raw128 aggregation differs')
    fit=r['fixed_train_fit'];sample=read_json(Path(c['references']['fixed_train_samples']['path']))
    gradient=read_json(Path(c['references']['gradient_diagnostic']['path']));final_rows=[]
    for record in gradient['models']['retention100M']['records']:
        for source,loss in record['losses'].items():final_rows.append(dict(source=source,draw=record['draw'],**loss))
    if (fit['config_sha256']!=sha256(study.CONFIG) or fit['checkpoint_sha256']!=c['early']['checkpoint']['sha256']
            or fit['samples_sha256']!=c['references']['fixed_train_samples']['sha256'] or not all(fit['checks'].values())
            or fit['optimizer_updates'] or fit['scientific_teacher_tokens'] or fit['protected_test_used'] or len(fit['rows'])!=16):
        raise ValueError('Read-only fixed train assay differs')
    keyed={(v['source'],v['draw']):v for v in sample['rows']}
    for v in fit['rows']:
        if any(v[k]!=keyed[(v['source'],v['draw'])][k] for k in ('input_sha256','target_sha256','teachers','EOS_teachers')):
            raise ValueError('Same train inputs/targets required')
    early_fit,final_fit=fit_summary(fit['rows']),fit_summary(final_rows)
    if any(early_fit[s]['teachers']!=final_fit[s]['teachers'] or early_fit[s]['EOS_teachers']!=final_fit[s]['EOS_teachers'] for s in early_fit):
        raise ValueError('Same train body+EOS counts required')
    report=dict(status='earliest_saved8M_all80_and_nested100M_review_complete',created_at=now(),summaries=summaries,
        primary_comparison='early8M-vs-final100M',quality_comparison=comparison,absolute_dev_screen=absolute,original_Web=original,
        eligible_for_final_Base_validation=all(absolute.values()) and all(original.values()) and comparison['passed'],
        source_fit=dict(early8M=early_fit,final100M=final_fit),
        transfer_aggregates={a:t['summary']['aggregate'] for a,t in r['transfer'].items()},
        retention_aggregates={a:t['summary']['aggregate'] for a,t in r['retention'].items()},
        GPU_seconds=r['GPU_seconds'],new_scientific_teacher_tokens=0,optimizer_updates=0,reused_scientific_trajectory_tokens=100000000,
        result_sha256=sha256(study.RUN/'compare-result.json'),Base_adopted=False,Chat_started=False,quantization_started=False,
        protected_test_used=False,independent_human_blind=False,quality_criteria_unchanged=True,old_numerical7_preserved=True,
        limitations='One nested trajectory; earliest checkpoint chosen before its quality results. Different teacher amounts, not independent seeds. Repeated fixeddev/nonblind content. Fixed train source fit and shared-generator probes do not prove broad natural-language quality; final independent seed/full dev/test/adoption pending.')
    atomic_json(study.RUN/'review.json',report);atomic_json(ROOT/'reports/phase6/early_exposure_comparison_review.json',report)
    print(json.dumps(report,ensure_ascii=False))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2);audit()

