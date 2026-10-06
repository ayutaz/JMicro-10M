"""Unchanged Japanese Base selection and real shared-architecture accounting."""
import copy
import json
from pathlib import Path
import sys

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive,finite_state
from run_eos_short_pilot import equal_state
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from gated_shared_model import GatedSharedModel,POLICY
from gated_shared_trainer import NATIVE_LR,GATE_LR
import review_parameter_displacement_anchor as verified
import run_gated_shared_comparison as study


def main():
    torch.set_num_threads(2);c=study.inspect();job=read_json(study.RUN/'job.json');r=read_json(study.RUN/'compare-result.json')
    if (job['status']!='complete' or alive(job) or r['GPU_seconds']!=job['GPU_elapsed_seconds']
            or r['config_sha256']!=sha256(study.CONFIG) or r['scientific_teacher_tokens']!=100000000
            or not r['all_scientific_input_streams_match'] or r['evaluation_model_class']!='GatedSharedModel'
            or set(r['checkpoints'])!={study.ARM} or r['GPU_seconds']+c['verification_GPU_seconds']>1800):
        raise ValueError('Actual bounded shared100M candidate required')
    parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);base=read_json(Path(c['original_config']['path']))
    record=r['checkpoints'][study.ARM];study.check_reference(dict(path=record['checkpoint'],sha256=record['checkpoint_sha256']))
    state=torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
    with torch.random.fork_rng(devices=[]):model=GatedSharedModel(state['model_config'])
    model.load_state_dict(state['model'],strict=True)
    if (not finite_state(state) or sum(p.numel() for p in model.parameters())!=10001165
            or len(list(model.named_parameters()))!=120 or len(model.model.layers)!=13 or model.logical_layers!=26
            or model.lm_head.weight is not model.model.embed_tokens.weight or model.config['gated_shared_reuse']!=POLICY
            or model.reuse_gates.shape!=(13,) or not torch.isfinite(model.reuse_gates).all()
            or model.reuse_gates.detach().tolist()!=record['gate_values']
            or state['spec']['gated_model_sha256']!=c['old_source_sha256']['scripts/gated_shared_model.py']
            or state['spec']['gated_trainer_sha256']!=c['old_source_sha256']['scripts/gated_shared_trainer.py']
            or state['spec']['native_unique_parameters']!=10001152 or state['spec']['new_gate_parameters']!=13
            or state['spec']['logical_layers']!=26 or state['spec']['gated_shared_reuse']!=POLICY
            or state['lineage']['parent_native_model_config']!=parent['model_config']
            or state['lineage']['new_gate_optimizer_policy']!='fresh_Adam_for_zero_gates_only'):
        raise ValueError('Actual config-reconstructed unique10M/gates/source contract differs')
    groups=state['optimizer']['param_groups']
    if (len(groups)!=3 or [g['lr'] for g in groups]!=[NATIVE_LR,NATIVE_LR,GATE_LR]
            or len(groups[-1]['params'])!=1 or groups[-1]['weight_decay']!=0
            or groups[-1]['betas']!=groups[1]['betas'] or groups[-1]['eps']!=groups[1]['eps']):
        raise ValueError('Actual native plus new-gate optimizer policy differs')
    gate_state=state['optimizer']['state'][groups[-1]['params'][0]]
    if (gate_state['exp_avg'].shape!=(13,) or gate_state['exp_avg_sq'].shape!=(13,)
            or int(gate_state['step'])!=state['sampler']['position']):
        raise ValueError('Fresh gate Adam consumed completed source updates only')
    history=[json.loads(s) for s in (study.RUN/study.ARM/'training/metrics.jsonl').read_text().splitlines()]
    if any(v['new_gate_LR']!=GATE_LR for v in history):raise ValueError('All gate LR history required')
    # Apply the unchanged native accounting contract to the two native groups;
    # the actual third gate group and its fresh moments were checked above.
    native_view=dict(state,optimizer=dict(state['optimizer'],param_groups=groups[:2]))
    verified.study=study;audit=verified.accounting(parent,native_view,record,history,c,study.ARM)
    cached=read_json(study.native.RUN/'compare-result.json');old=cached['checkpoints']['matched_staged_CE']
    study.matched_sources(record,old)
    study.check_reference(dict(path=old['checkpoint'],sha256=old['checkpoint_sha256']))
    old_state=torch.load(old['checkpoint'],map_location='cpu',weights_only=False)
    for key in ('sampler','token_digest','focus_token_digest','tokens','supervised_tokens','body_bytes','focus_teacher_tokens','weighted_teacher_mass','update'):
        if not equal_state(state[key],old_state[key]):raise ValueError('Matched actual source/teachers differs: '+key)
    if old_state['lineage']['parent']!=c['parent']:raise ValueError('Cached native same-parent control required')
    summaries={};scores={};candidate=r['evaluations'][study.ARM];control=cached['evaluations']['matched_staged_CE']
    summaries[study.ARM],scores[study.ARM]=verified.content(study.ARM,candidate,record,base,
        study.RUN/f'evaluation/{study.ARM}/evaluation/generation.json',study.RUN/'content-notes.json')
    summaries['native_CE'],scores['native_CE']=verified.content('native_CE',control,old,base,
        study.native.RUN/'evaluation/matched_staged_CE/evaluation/generation.json',study.native.RUN/'matched_staged_CE-content-notes.json')
    previous=read_json(ROOT/'reports/phase6/source-order-condition-comparison-v2-20261006/compare-result.json')
    strong=previous['evaluations']['source_order'];strong_record=previous['checkpoints']['source_order']
    if dict(path=strong_record['checkpoint'],sha256=strong_record['checkpoint_sha256'])!=c['strong_control']:
        raise ValueError('Fixed strong staged selection control differs')
    summaries['strong_staged'],scores['strong_staged']=verified.content('strong_staged',strong,strong_record,base,
        ROOT/'reports/phase6/source-order-condition-comparison-v2-20261006/evaluation/source_order/evaluation/generation.json',
        ROOT/'reports/phase6/source_order_condition_notes.json')
    if (summaries['strong_staged']['coherent']!=23 or summaries['strong_staged']['rates']['eos']!=76
            or summaries['strong_staged']['rates']['repetition']!=2):raise ValueError('Frozen selection baseline changed')
    comparisons={}
    for name,ev in (('native_CE',control),('strong_staged',strong)):
        if ([(v['id'],v['prefix']) for v in ev['generation']['outputs']]!=[(v['id'],v['prefix']) for v in candidate['generation']['outputs']]
                or [(v['doc_id'],v['body_tokens'],v['body_bytes']) for v in ev['body']['rows']]!=[(v['doc_id'],v['body_tokens'],v['body_bytes']) for v in candidate['body']['rows']]):
            raise ValueError('Complete common-byte/common-prefix examples required')
        comparisons[name]=quality_gates(ev,candidate,scores[name],scores[study.ARM],'content')
    for key in ('transfer','retention'):
        t=r[key][study.ARM]
        if t['evaluated_requests']!=512 or not all(t['checks'].values()) or t['checkpoint_sha256']!=record['checkpoint_sha256']:
            raise ValueError('Complete actual read-only transfer score required')
    summary=summaries[study.ARM];rates=summary['rates']
    absolute=dict(grammar_at_least56=summary['grammar2']>=56,coherence_at_least27=summary['coherent']>=27,
        appropriate_at_least27=summary['appropriate']>=27,EOS_at_least37=rates['eos']>=37,repetition_at_most18=rates['repetition']<=18,
        no_empty_role_unicode=all(rates[k]==0 for k in ('empty','role_leak','unicode_failure')))
    study.check_reference(base['reference']['web_screen'])
    original=adoption_checks(read_json(Path(base['reference']['web_screen']['path'])),candidate)
    eligible=comparisons['strong_staged']['passed'] and all(absolute.values()) and all(original.values())
    report=dict(status='gated_shared100M_all80_content_and_actual_architecture_reviewed',created_at=now(),
        config_sha256=sha256(study.CONFIG),result_sha256=sha256(study.RUN/'compare-result.json'),
        selection=read_json(study.PROPOSAL)['selection'],summaries=summaries,quality_comparisons=comparisons,
        absolute_dev_screen=absolute,original_Web=original,eligible_for_final_Base_validation=eligible,
        accounting=audit,gate_values=record['gate_values'],unique_parameters=10001165,unique_blocks=13,logical_invocations=26,
        native_optimizer_policy='inherited',new_gate_optimizer_policy='fresh13_only',scientific_teacher_tokens=100000000,
        reused_control_teacher_tokens=100000000,verification_teacher_tokens=c['verification_teacher_tokens'],
        new_total_GPU_seconds=r['GPU_seconds']+c['verification_GPU_seconds'],all80_individually_read=True,
        independent_human_blind=False,Base_complete=False,Base_adopted=False,protected_test_used=False,
        Chat_started=False,quantization_started=False,quality_criteria_unchanged=True,
        limitations='13 added scalar weights/new fresh gate group and more compute/KV; same native weights/Adam parent, input/target100M and evaluators. One learned seed/nonblind repeated dev. Stock HF export pending, not claimed complete.',
        next_action='Only a qualified recipe permits independent learned seed/full dev/protected test/adoption; otherwise end the fixed shared-gate recipe without LR/depth/source/decoder/checkpoint rescue.')
    destination=study.RUN/'review.json'
    if destination.exists():raise ValueError('Preserve original sharing review')
    atomic_json(destination,report);atomic_json(ROOT/'reports/phase6/gated_shared_comparison_review.json',report)
    print(dict(summaries=summaries,eligible=eligible))


if __name__=='__main__':main()
