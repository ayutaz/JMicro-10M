"""CPU closeout of all96 read-only next-token LF counterfactual observations."""
import math
from pathlib import Path
import sys
import json
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import numpy as np
from jmicro.experiment import ROOT,now,read_json
from jmicro.training import atomic_json
from phase6_performance import alive
from run_base_residual_seen_train import checked,ref
from run_base_residual_boundary_counterfactual import CONFIG,OUTPUT,RUN


def complete():
    destination=ROOT/'reports/phase6/base_residual_boundary_counterfactual_completion.json'
    if destination.exists(): raise ValueError('Preserve completed boundary counterfactual')
    result=read_json(OUTPUT);c=checked(result['config'])
    if result['config']!=ref(CONFIG) or result['parent']!=c['parent']: raise ValueError('Actual fixed config/parent differs')
    job=read_json(RUN/'job.json')
    launcher=read_json(ROOT/'reports/phase6/base-residual-boundary-counterfactual-launcher-20261008/result.json')
    if (alive(job) or job['status']!='complete' or not job['cumulative_GPU_ledger_closed']
            or result['GPU_seconds']!=job['GPU_seconds'] or result['GPU_seconds']>30
            or not all(result['checks'].values()) or result['optimizer_updates'] or result['scientific_teacher_tokens']
            or launcher['status']!='complete' or launcher['exit_code'] or not launcher['UI_restore_command_succeeded']):
        raise ValueError('Actual ended process/closed30-second ledger/unchanged weights and restored launcher required')
    if [r['id'] for r in result['results']]!=[r['id'] for r in c['selected']]:
        raise ValueError('All32 fixed original units required')
    pairs=[];duplicate_checks=0
    for expected,row in zip(c['selected'],result['results'],strict=True):
        if row['population']!=expected['population'] or len(row['variants'])!=3:
            raise ValueError('Exactly three fixed contexts per unit required')
        for case,value in zip(expected['variants'],row['variants'],strict=True):
            if (any(case[k]!=value[k] for k in case) or value['LF_token_ids']!=c['LF_token_ids']
                    or value['generated_tokens'] or value['forced_EOS_tokens']
                    or not math.isfinite(value['EOS_probability']) or not 0<=value['EOS_probability']<=1
                    or type(value['EOS_rank']) is not int or value['EOS_rank']<1 or len(value['top8'])!=8):
                raise ValueError('Actual full-body context and finite next-token-only output required')
            for top in value['top8']:
                if not math.isfinite(top['probability']) or not 0<=top['probability']<=1:
                    raise ValueError('Finite top8 raw next-token event required')
        a,b,d=row['variants']
        for other in (b,d):
            if other['input_ids']==a['input_ids']:
                if any(other[k]!=a[k] for k in ('EOS_probability','EOS_rank','LF_next_token_probability','top8')):
                    raise ValueError('Repeated identical actual context prediction differs')
                duplicate_checks+=1
        pairs.append(dict(id=row['id'],population=row['population'],
            original_EOS_probability=a['EOS_probability'],original_EOS_rank=a['EOS_rank'],
            no_trailing_LF_EOS_probability=b['EOS_probability'],no_trailing_LF_EOS_rank=b['EOS_rank'],
            one_LF_EOS_probability=d['EOS_probability'],one_LF_EOS_rank=d['EOS_rank'],
            probability_difference=d['EOS_probability']-b['EOS_probability'],
            no_trailing_LF_next_LF_probability=b['LF_next_token_probability'],
            no_trailing_LF_top1_id=b['top8'][0]['id'],one_LF_top1_id=d['top8'][0]['id']))
    summaries={}
    for population in ('all','TRAIN','DEV'):
        rows=pairs if population=='all' else [r for r in pairs if r['population']==population]
        differences=[r['probability_difference'] for r in rows]
        summaries[population]=dict(units=len(rows),median_EOS_probability_difference=float(np.median(differences)),
            mean_EOS_probability_difference=float(np.mean(differences)),positive_differences=sum(v>0 for v in differences),
            median_no_trailing_LF_EOS_probability=float(np.median([r['no_trailing_LF_EOS_probability'] for r in rows])),
            median_one_LF_EOS_probability=float(np.median([r['one_LF_EOS_probability'] for r in rows])),
            no_trailing_LF_EOS_rank1=sum(r['no_trailing_LF_EOS_rank']==1 for r in rows),
            one_LF_EOS_rank1=sum(r['one_LF_EOS_rank']==1 for r in rows),
            no_trailing_LF_top1_is_LF=None if len(c['LF_token_ids'])!=1 else sum(r['no_trailing_LF_top1_id']==c['LF_token_ids'][0] for r in rows))
    screen=(summaries['all']['median_EOS_probability_difference']>.25 and summaries['all']['positive_differences']>=24)
    ui=read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=3) as response: model=json.load(response)
    if (not alive(ui) or model['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or model['training_tokens']!=10000007168 or model['busy']):
        raise ValueError('Actual idle original10B UI restoration required')
    atomic_json(destination,dict(status='complete',created_at=now(),result=ref(OUTPUT),config=ref(CONFIG),
        process_exited=True,launcher_exit_code=0,GPU_seconds=result['GPU_seconds'],GPU_cap_seconds=30,
        checks=result['checks'],all96_context_event_bindings_verified=True,
        identical_original_counterfactual_prediction_checks=duplicate_checks,paired_results=pairs,summaries=summaries,
        prespecified_strong_LF_cue_screen=screen,median_probability_difference_threshold=.25,minimum_positive_differences=24,
        restored_UI_identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},restored_UI_model=model,
        interpretation='Same-body trailing LF changes measured next-token EOS preference within these frozen weights; a positive screen establishes local marker sensitivity only. No new free-generation or Base-quality improvement measured. Original DEV/test bytes and all quality gates unchanged.',
        scientific_teacher_tokens=0,optimizer_updates=0,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,protected_test_scored=False))
    print(json.dumps(dict(status='complete',GPU_seconds=result['GPU_seconds'],strong_LF_cue_screen=screen,
                         summaries=summaries,Base_complete=False,restored_UI=ui['pid'])))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    complete()
