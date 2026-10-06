"""Actual matched positive/negative exposure and unchanged Japanese Base gates."""
import json
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from jmicro.model import JMicroModel
from jmicro.eos_pilot import TrainView
from phase6_performance import alive, finite_state
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from review_parameter_displacement_anchor import content
from base_preference_accounting import accounting, matched_exposure
from run_eos_short_pilot import equal_state
import run_base_preference_comparison as study


def main():
    torch.set_num_threads(2); c=study.inspect(); job=read_json(study.RUN/'job.json'); r=read_json(study.RUN/'compare-result.json')
    if (job['status']!='complete' or alive(job) or r['GPU_seconds']!=job['GPU_elapsed_seconds']
            or r['config_sha256']!=sha256(study.CONFIG) or r['scientific_positive_teacher_tokens']!=study.TOTAL
            or r['common_positive_teacher_tokens']!=study.COMMON or r['positive_teacher_tokens_per_arm']!=study.COMMON+study.PAIR
            or r['evaluation_model_class']!='JMicroModel' or set(r['checkpoints'])!={'common_Web',*study.ARMS}
            or r['GPU_seconds']+c['verification_GPU_seconds']>study.CEILING):
        raise ValueError('Actual bounded native Base preference experiment required')
    parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False); base=read_json(Path(c['original_config']['path']))
    shared_ref=r['shared_parent']; study.check_reference(shared_ref); shared=torch.load(shared_ref['path'],map_location='cpu',weights_only=False)
    study.check_reference(r['reference_cache']); cache=read_json(Path(r['reference_cache']['path']))
    if (cache['parent']!=shared_ref or cache['config_sha256']!=sha256(study.CONFIG) or not all(cache['checks'].values())
            or cache['optimizer_updates'] or cache['scientific_teacher_tokens']
            or cache['reference']['batch']!=c['pair_batch'] or cache['reference']['dtype']!='bf16'):
        raise ValueError('Readonly actual shared6M reference required')
    web=TrainView(c['original_web']['path'],c['original_web']['manifest_sha256']); pairs=study.probe.pairs(c)
    audits={}; summaries={}; scores={}; histories={}; states={}
    for arm,record in r['checkpoints'].items():
        study.check_reference(dict(path=record['checkpoint'],sha256=record['checkpoint_sha256']))
        state=torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
        with torch.random.fork_rng(devices=[]): model=JMicroModel(state['model_config'])
        model.load_state_dict(state['model'],strict=True)
        if (not finite_state(state) or sum(p.numel() for p in model.parameters())!=10001152
                or len(list(model.named_parameters()))!=119 or len(model.model.layers)!=13
                or model.lm_head.weight is not model.model.embed_tokens.weight or record['unique_parameters']!=10001152
                or state['spec']['base_preference_trainer_sha256']!=c['old_source_sha256']['scripts/base_preference_trainer.py']):
            raise ValueError('Actual unchanged native architecture/source differs')
        histories[arm]=[json.loads(v) for v in (study.RUN/arm/'training/metrics.jsonl').read_text().splitlines()]
        common=arm=='common_Web'; b=study.binding(c,arm,None if common else shared_ref,None if common else r['reference_cache'])
        audits[arm]=accounting(parent if common else shared,state,record,histories[arm],study.COMMON if common else study.PAIR,b,pairs,web.byte_lengths)
        if not common:
            if (state['spec']['coefficient']!=study.ARMS[arm] or state['spec']['beta']!=.1
                    or state['spec']['reference_digest']!=__import__('hashlib').sha256(json.dumps(cache['reference'],sort_keys=True).encode()).hexdigest()):
                raise ValueError('Actual fixed paired reference/objective differs')
            summaries[arm],scores[arm]=content(arm,r['evaluations'][arm],record,base,
                study.RUN/f'evaluation/{arm}/evaluation/generation.json',study.RUN/f'{arm}-content-notes.json')
            for key in ('transfer','retention'):
                t=r[key][arm]
                if t['evaluated_requests']!=512 or not all(t['checks'].values()) or t['checkpoint_sha256']!=record['checkpoint_sha256']:
                    raise ValueError('Complete readonly transfer score required')
            states[arm]=state
        del model
    match=matched_exposure(*(histories[a] for a in study.ARMS))
    if match!=r['matched_exposure'] or not equal_state(*(states[a]['sampler'] for a in study.ARMS)):
        raise ValueError('Exact common positive/negative source stream required')
    previous=read_json(Path(c['references']['strong_result']['path'])); strong=previous['evaluations']['source_order']; strong_record=previous['checkpoints']['source_order']
    folder=Path(c['references']['strong_result']['path']).parent
    summaries['strong_staged'],scores['strong_staged']=content('strong_staged',strong,strong_record,base,
        folder/'evaluation/source_order/evaluation/generation.json',Path(c['references']['strong_notes']['path']))
    if (summaries['strong_staged']['coherent']!=23 or summaries['strong_staged']['rates']['eos']!=76
            or summaries['strong_staged']['rates']['repetition']!=2): raise ValueError('Frozen strong selection baseline differs')
    quality={}; absolute={}; original={}; eligible={}; study.check_reference(base['reference']['web_screen'])
    for arm in study.ARMS:
        ev=r['evaluations'][arm]
        if ([(v['id'],v['prefix']) for v in strong['generation']['outputs']]!=[(v['id'],v['prefix']) for v in ev['generation']['outputs']]
                or [(v['doc_id'],v['body_tokens'],v['body_bytes']) for v in strong['body']['rows']]!=[(v['doc_id'],v['body_tokens'],v['body_bytes']) for v in ev['body']['rows']]):
            raise ValueError('All fixed Japanese/common byte examples required')
        quality[arm]=quality_gates(strong,ev,scores['strong_staged'],scores[arm],'content')
        summary=summaries[arm]; rates=summary['rates']
        absolute[arm]=dict(grammar_at_least56=summary['grammar2']>=56,coherence_at_least27=summary['coherent']>=27,
            appropriate_at_least27=summary['appropriate']>=27,EOS_at_least37=rates['eos']>=37,repetition_at_most18=rates['repetition']<=18,
            no_empty_role_unicode=all(rates[k]==0 for k in ('empty','role_leak','unicode_failure')))
        original[arm]=adoption_checks(read_json(Path(base['reference']['web_screen']['path'])),ev)
        eligible[arm]=quality[arm]['passed'] and all(absolute[arm].values()) and all(original[arm].values())
    matched_quality=quality_gates(r['evaluations']['chosen_CE'],r['evaluations']['chosen_CE_DPO'],scores['chosen_CE'],scores['chosen_CE_DPO'],'content')
    eligible['chosen_CE_DPO']=eligible['chosen_CE_DPO'] and matched_quality['passed']
    report=dict(status='Base_preference_all160_native_state_and_content_reviewed',created_at=now(),config_sha256=sha256(study.CONFIG),
        result_sha256=sha256(study.RUN/'compare-result.json'),summaries=summaries,quality_comparison=quality,matched_objective_quality=matched_quality,
        absolute_dev_screen=absolute,original_Web=original,eligible_for_final_Base_validation=eligible,accounting=audits,matched_exposure=match,
        scientific_positive_teacher_tokens=study.TOTAL,common_positive_teacher_tokens=study.COMMON,positive_teacher_tokens_per_arm=study.COMMON+study.PAIR,
        verification_teacher_tokens=c['verification_teacher_tokens'],new_total_GPU_seconds=r['GPU_seconds']+c['verification_GPU_seconds'],
        diagnostic_GPU_seconds_separate=c['diagnostic_GPU_seconds_separate'],all160_individually_read=True,independent_human_blind=False,
        Base_complete=False,Base_adopted=False,protected_test_used=False,Chat_started=False,quantization_started=False,quality_criteria_unchanged=True,
        limitations='Only56 TRAIN pairs/4565 positive positions repeatedly exposed, about438 passes; not new2M source. Original8 weak rows excluded before preference labeling. Sequence length/genre and fixed stale negatives; one learned seed/nonblind repeated dev. Earlier seven numerical failures retained.',
        next_action='Qualified fixed recipe only: independent learned seed/full dev/protected test/adoption. Otherwise end both fixed recipes; no source/beta/coefficient/epoch/LR/decoder/checkpoint rescue.')
    destination=study.RUN/'review.json'
    if destination.exists(): raise ValueError('Preserve original preference review')
    atomic_json(destination,report); atomic_json(ROOT/'reports/phase6/base_preference_comparison_review.json',report)
    print(dict(summaries=summaries,eligible=eligible))


if __name__=='__main__': main()
