"""CPU paired-body aggregation and closed-ledger verification for context probe."""
import json
from pathlib import Path
import sys
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import numpy as np
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive
from run_base_residual_seen_train import checked,ref
from run_base_residual_original_context import CONFIG,OUTPUT,RUN


def complete():
    destination=ROOT/'reports/phase6/base_residual_original_context_completion.json'
    if destination.exists(): raise ValueError('Preserve completed context diagnostic')
    result=read_json(OUTPUT);c=checked(result['config']);prepared=checked(result['preparation']);baseline=checked(result['baseline'])
    if result['config']!=ref(CONFIG) or result['parent']!=c['parent']: raise ValueError('Fixed original2B result binding differs')
    job=read_json(RUN/'job.json');launcher=read_json(ROOT/'reports/phase6/base-residual-original-context-launcher-20261008/result.json')
    if (alive(job) or job['status']!='complete' or not job['cumulative_GPU_ledger_closed']
            or result['GPU_seconds']!=job['GPU_seconds'] or result['GPU_seconds']>60 or not all(result['checks'].values())
            or result['scientific_teacher_tokens'] or result['optimizer_updates']
            or launcher['status']!='complete' or launcher['exit_code'] or not launcher['UI_restore_command_succeeded']):
        raise ValueError('Actual exited60-second read-only process and successful launcher required')
    notes_path=ROOT/'reports/phase6/base_residual_original_context_content_notes.json'
    notes=read_json(notes_path);keyed={r['id']:r for r in notes['notes']}
    expected=[r['id'] for r in prepared['selected']]
    if (notes['raw_result_sha256']!=sha256(OUTPUT) or not notes['all14_new_continuations_individually_read']
            or not notes['all14_full_supplied_contexts_individually_read'] or len(keyed)!=16 or set(keyed)!=set(expected)
            or [r['id'] for r in result['results']]!=expected):
        raise ValueError('All16 fixed cases and raw-bound all14 new context/content readings required')
    codec=Tokenizer(ROOT/c['tokenizer']);old={r['id']:r for r in baseline['results'][:16]};pairs=[]
    for unit,row in zip(prepared['selected'],result['results'],strict=True):
        n=min(64,len(unit['continuation_gold_ids']));targets=unit['continuation_gold_ids'][:n]
        a=old[row['id']]['teacher']['steps'][:n];b=row['teacher_body']['steps']
        if (row['has_additional_context']!=unit['has_additional_context'] or len(b)!=n
                or row['teacher_body']['fed_ids']!=targets
                or [r['original_gold_id'] for r in a]!=targets or [r['original_gold_id'] for r in b]!=targets
                or any(r['actual_gold_EOS'] for r in b) or 3 in targets):
            raise ValueError('Exactly same original BODY positions, no paragraph-unit EOS required')
        if unit['has_additional_context'] and row['teacher_body']['steps'][0]!=row['free']['steps'][0]:
            raise ValueError('Same actual recovered-context teacher/free first prediction required')
        for series in (row['teacher_body'],row['free']):
            raw=codec.decode_bytes(series['fed_ids'])
            if raw.hex()!=series['raw_UTF8_bytes_hex'] or raw.decode('utf-8',errors='replace')!=series['text']:
                raise ValueError('Actual BODY/generated raw byte binding differs')
        note=keyed[row['id']]
        if (type(note['nonprogressive_repetition']) is not bool or type(note['appropriate_end']) is not bool
                or note['premise'] not in ('maintained','violated','unclear') or len(note['reason'])<12
                or (note['appropriate_end'] and row['free']['stop_reason']!='stop_id')):
            raise ValueError('Individual diagnostic note required')
        aa=sum(s['original_gold_nll'] for s in a);bb=sum(s['original_gold_nll'] for s in b)
        pairs.append(dict(id=row['id'],has_additional_context=unit['has_additional_context'],body_targets=n,
            standalone_body_NLL_sum=aa,context_body_NLL_sum=bb,standalone_body_NLL_mean=aa/n,context_body_NLL_mean=bb/n,
            mean_NLL_improvement=(aa-bb)/n,
            standalone_original_body_argmax_correct=sum(s['greedy_id']==s['original_gold_id'] for s in a),
            context_original_body_argmax_correct=sum(s['greedy_id']==s['original_gold_id'] for s in b),
            standalone_EOS=old[row['id']]['free']['stop_reason']=='stop_id',context_EOS=row['free']['stop_reason']=='stop_id',
            standalone_automatic_repetition=old[row['id']]['free']['automatic_repetition'],
            context_automatic_repetition=row['free']['automatic_repetition']))
    eligible=[r for r in pairs if r['has_additional_context']]
    values=np.array([r['mean_NLL_improvement'] for r in eligible])
    if len(eligible)>=8:
        means=np.random.default_rng(42).choice(values,size=(10000,len(values)),replace=True).mean(axis=1)
        ci=np.quantile(means,[.025,.975]).tolist()
    else: ci=[None,None]
    screen=bool(len(eligible)>=8 and float(values.mean())>.20 and ci[0]>0)
    targets=sum(r['body_targets'] for r in eligible)
    manual=notes['notes'];new_manual=[n for n in manual if n['id'] in {r['id'] for r in eligible}]
    ui=read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=3) as response: model=json.load(response)
    if (not alive(ui) or model['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or model['training_tokens']!=10000007168 or model['busy']):
        raise ValueError('Actual idle original10B UI restoration required')
    atomic_json(destination,dict(status='complete',created_at=now(),result=ref(OUTPUT),config=ref(CONFIG),notes=ref(notes_path),
        process_exited=True,launcher_exit_code=0,GPU_seconds=result['GPU_seconds'],GPU_cap_seconds=60,checks=result['checks'],
        all16_source_slices_exact=True,new_context_units=len(eligible),no_context_reused_controls=len(pairs)-len(eligible),
        paired_BODY_results=pairs,original_BODY_targets=targets,
        standalone_token_weighted_BODY_NLL=sum(r['standalone_body_NLL_sum'] for r in eligible)/targets,
        context_token_weighted_BODY_NLL=sum(r['context_body_NLL_sum'] for r in eligible)/targets,
        standalone_BODY_argmax_correct=sum(r['standalone_original_body_argmax_correct'] for r in eligible),
        context_BODY_argmax_correct=sum(r['context_original_body_argmax_correct'] for r in eligible),
        mean_document_BODY_NLL_improvement=float(values.mean()),bootstrap95CI=ci,bootstrap_seed=42,bootstrap_samples=10000,
        minimum_context_units=8,mean_improvement_threshold=.20,prespecified_context_benefit_screen=screen,
        fixed_original_context_diagnostic_closed=not screen,
        new_context_free_summary=dict(documents=len(eligible),EOS=sum(r['context_EOS'] for r in eligible),
            automatic_repetition=sum(r['context_automatic_repetition'] for r in eligible),
            manual_nonprogressive_repetition=sum(n['nonprogressive_repetition'] for n in new_manual),
            appropriate_end=sum(n['appropriate_end'] for n in new_manual),
            premise={label:sum(n['premise']==label for n in new_manual) for label in ('maintained','violated','unclear')}),
        restored_UI_identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},restored_UI_model=model,
        scientific_teacher_tokens=0,optimizer_updates=0,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,protected_test_scored=False,
        limits='Same fixed14 source-context interventions plus2 reused controls; context length and positions change together with information. A natural alternative continuation need not match the reference. No independent generalization, useful Base quality or benefit from future learning is established.'))
    print(json.dumps(dict(status='complete',new_context_units=len(eligible),GPU_seconds=result['GPU_seconds'],
        mean_BODY_NLL_improvement=float(values.mean()),bootstrap95CI=ci,context_benefit_screen=screen,
        Base_complete=False,restored_UI=ui['pid'])))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    complete()
