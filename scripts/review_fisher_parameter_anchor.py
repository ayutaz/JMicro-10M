"""Frozen Base selection, actual source match and all80 content; no adoption."""
import copy
import json
from pathlib import Path
import sys

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from run_eos_short_pilot import equal_state
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from fisher_parameter_anchor import tensor_digest
import review_parameter_displacement_anchor as verified
import run_fisher_parameter_anchor as study


def main():
    torch.set_num_threads(2);c=study.inspect(study.CONFIG)
    job=read_json(study.RUN/'job.json');r=read_json(study.RUN/'compare-result.json')
    if (job['status']!='complete' or alive(job) or r['GPU_seconds']!=job['GPU_elapsed_seconds']
            or r['config_sha256']!=sha256(study.CONFIG) or r['scientific_teacher_tokens']!=100000000
            or not r['all_scientific_input_streams_match'] or set(r['checkpoints'])!={'fisher_anchor'}
            or r['GPU_seconds']+c['verification_GPU_seconds']+c['field_GPU_seconds']>1800):
        raise ValueError('Actual bounded, matched full100M candidate required')
    base=read_json(Path(c['original_config']['path']));parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
    cached=read_json(study.uniform.RUN/'compare-result.json');cached_review=read_json(study.uniform.RUN/'review.json')
    if cached_review['result_sha256']!=sha256(study.uniform.RUN/'compare-result.json'):
        raise ValueError('Frozen cached review differs')
    record=r['checkpoints']['fisher_anchor'];study.check_reference(dict(path=record['checkpoint'],sha256=record['checkpoint_sha256']))
    state=torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
    history=[json.loads(s) for s in (study.RUN/'fisher_anchor/training/metrics.jsonl').read_text().splitlines()]
    # Configure the unchanged prior accounting function for the new study. Its
    # source stays immutable; the field-specific invariants are checked below.
    verified.study=study
    audit=verified.accounting(parent,state,record,history,c,'fisher_anchor')
    field=torch.load(c['field']['path'],map_location='cpu',weights_only=False)
    if (state['lineage']['field_initial_digest']!=c['field_binding']['field_tensor_digest']
            or state['spec']['field_binding']!=c['field_binding'] or field['parent']!=c['parent']
            or tensor_digest(field['field'])!=c['field_binding']['field_tensor_digest']
            or state['spec']['fisher_trainer_sha256']!=c['source_sha256']['scripts/fisher_parameter_anchor.py']
            or state['spec']['field_normalization']!='unique_global_coordinate_mean_one'):
        raise ValueError('Actual field/source/parent binding differs')
    old_record=cached['checkpoints']['parameter_anchor']
    study.check_reference(dict(path=old_record['checkpoint'],sha256=old_record['checkpoint_sha256']))
    old_state=torch.load(old_record['checkpoint'],map_location='cpu',weights_only=False)
    for key in ('sampler','token_digest','focus_token_digest','tokens','supervised_tokens','body_bytes','focus_teacher_tokens','weighted_teacher_mass','update'):
        if not equal_state(state[key],old_state[key]):raise ValueError('Cached and new100M source/teacher stream differs: '+key)
    if old_state['lineage']['parent']!=c['parent'] or old_state['lineage']['parent_scheduler']!=state['lineage']['parent_scheduler']:
        raise ValueError('Comparison parent/scheduler differs')
    summaries={};scores={}
    candidate=r['evaluations']['fisher_anchor'];control=cached['evaluations']['parameter_anchor']
    summaries['fisher_anchor'],scores['fisher_anchor']=verified.content('fisher_anchor',candidate,record,base,
        study.RUN/'evaluation/fisher_anchor/evaluation/generation.json',study.RUN/'content-notes.json')
    summaries['uniform_anchor'],scores['uniform_anchor']=verified.content('uniform_anchor',control,old_record,base,
        study.uniform.RUN/'evaluation/parameter_anchor/evaluation/generation.json',study.uniform.RUN/'parameter_anchor-content-notes.json')
    previous=read_json(ROOT/'reports/phase6/source-order-condition-comparison-v2-20261006/compare-result.json')
    strong=previous['evaluations']['source_order'];strong_record=previous['checkpoints']['source_order']
    if dict(path=strong_record['checkpoint'],sha256=strong_record['checkpoint_sha256'])!=c['strong_control']:
        raise ValueError('Fixed strong selection control differs')
    summaries['strong_staged'],scores['strong_staged']=verified.content('strong_staged',strong,strong_record,base,
        ROOT/'reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/generation.json',
        ROOT/'reports/phase6/source_order_condition_notes.json')
    if (summaries['strong_staged']['coherent']!=23 or summaries['strong_staged']['rates']['eos']!=76
            or summaries['strong_staged']['rates']['repetition']!=2):raise ValueError('Fixed strongest staged gate changed')
    comparisons={}
    for name,ev in (('uniform_anchor',control),('strong_staged',strong)):
        if ([(v['id'],v['prefix']) for v in ev['generation']['outputs']]!=[(v['id'],v['prefix']) for v in candidate['generation']['outputs']]
                or [(v['doc_id'],v['body_tokens'],v['body_bytes']) for v in ev['body']['rows']]!=[(v['doc_id'],v['body_tokens'],v['body_bytes']) for v in candidate['body']['rows']]):
            raise ValueError('Identical full common examples required')
        comparisons[name]=quality_gates(ev,candidate,scores[name],scores['fisher_anchor'],'content')
    for key in ('transfer','retention'):
        t=r[key]['fisher_anchor']
        if t['evaluated_requests']!=512 or not all(t['checks'].values()) or t['checkpoint_sha256']!=record['checkpoint_sha256']:
            raise ValueError('Complete actual read-only transfer suites required')
    summary=summaries['fisher_anchor'];rates=summary['rates']
    absolute=dict(grammar_at_least56=summary['grammar2']>=56,coherence_at_least27=summary['coherent']>=27,
        appropriate_at_least27=summary['appropriate']>=27,EOS_at_least37=rates['eos']>=37,repetition_at_most18=rates['repetition']<=18,
        no_empty_role_unicode=all(rates[k]==0 for k in ('empty','role_leak','unicode_failure')))
    study.check_reference(base['reference']['web_screen'])
    original=adoption_checks(read_json(Path(base['reference']['web_screen']['path'])),candidate)
    selection=read_json(study.PROPOSAL)['selection']
    # Predeclared selection is against the strong staged control. The uniform
    # anchor paired comparison measures the metric change and is also reported.
    eligible=comparisons['strong_staged']['passed'] and all(absolute.values()) and all(original.values())
    result=dict(status='Fisher100M_all80_content_matched_control_reviewed',created_at=now(),
        config_sha256=sha256(study.CONFIG),result_sha256=sha256(study.RUN/'compare-result.json'),
        selection=selection,summaries=summaries,accounting=audit,quality_comparisons=comparisons,
        original_Web=original,absolute_dev_screen=absolute,eligible_for_final_Base_validation=eligible,
        scientific_teacher_tokens=100000000,reused_control_teacher_tokens=100000000,
        field_model_sampled_labels=65276,verification_teacher_tokens=c['verification_teacher_tokens'],
        new_total_GPU_seconds=r['GPU_seconds']+c['verification_GPU_seconds']+c['field_GPU_seconds'],
        all80_individually_read=True,independent_human_blind=False,Base_complete=False,Base_adopted=False,
        protected_test_used=False,quality_criteria_unchanged=True,Chat_started=False,quantization_started=False,
        next_action='Qualified recipe only: independent learned seed/full dev/protected test/adoption; otherwise terminate fixed field comparison, no rescue sweep.')
    destination=study.RUN/'review.json'
    if destination.exists():raise ValueError('Preserve original Fisher review')
    atomic_json(destination,result);atomic_json(ROOT/'reports/phase6/fisher_parameter_anchor_review.json',result)
    print(dict(summaries=summaries,eligible=eligible))


if __name__=='__main__':main()
