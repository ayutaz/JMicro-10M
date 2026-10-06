"""All160 raw-bound reviews, exact learned budgets and unchanged Base gates."""
import json
from pathlib import Path
import sys
from types import SimpleNamespace
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from jmicro.model import JMicroModel
from phase6_performance import alive
from run_eos_short_pilot import equal_state
from review_parameter_displacement_anchor import content
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
import review_interleaved_outcome_order as original_accounting
import run_low_rank_base_comparison as study


def main():
    torch.set_num_threads(2);c=study.inspect(study.CONFIG)
    r=read_json(study.RUN/'compare-result.json');job=read_json(study.RUN/'job.json')
    if (job['status']!='complete' or alive(job) or r['GPU_seconds']!=job['GPU_elapsed_seconds']
            or r['GPU_seconds']+c['verification_GPU_seconds']>1800 or r['config_sha256']!=sha256(study.CONFIG)
            or r['scientific_teacher_tokens']!=183283510 or r['scientific_optimizer_updates']!=6136
            or set(r['arms'])!=set(study.ARMS)):
        raise ValueError('Both actual terminated endpoints and measured budget required')
    parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
    base=read_json(Path(c['original_config']['path']));ledger=read_json(Path(c['references']['reference_input_ledger']['path']))
    summaries={};scores={};audits={};evaluations={}
    for arm in study.ARMS:
        record=r['arms'][arm]['checkpoint'];study.check_reference(dict(path=record['checkpoint'],sha256=record['checkpoint_sha256']))
        state=torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
        history=[json.loads(s) for s in (study.RUN/arm/'training/metrics.jsonl').read_text().splitlines()]
        # The common sampler/teacher ledger audit is unchanged; only its
        # explicitly expected recipe kind is supplied for this new trainer.
        saved=original_accounting.study
        try:
            original_accounting.study=SimpleNamespace(KIND=study.KIND)
            audits[arm]=original_accounting.accounting(parent,state,record,history,ledger)
        finally:original_accounting.study=saved
        if (state['study_binding']!=study.binding(c,study.CONFIG,arm) or state['lineage']['optimizer_policy']!='fresh_Adam_both_arms'
                or state['spec']['optimizer_policy']!='fresh_Adam_both_arms' or state['native_parameters']!=10001152
                or not state['merged_for_native_evaluation'] or not r['arms'][arm]['merge']['allclose']):
            raise ValueError('Matched fresh-Adam and native merge evidence differs')
        unmerged=state['unmerged_training_model']
        if arm==study.ARMS[1]:
            if state['trainable_parameters']!=232960 or not all(torch.equal(unmerged[k],v) for k,v in parent['model'].items()):
                raise ValueError('Original frozen backbone changed')
            merged={k:v for k,v in unmerged.items() if not k.endswith(('.A','.B'))}
            names=[k[:-2] for k in unmerged if k.endswith('.A')]
            if len(names)!=91 or any(unmerged[n+'.A'].shape[0]!=4 or unmerged[n+'.B'].shape[1]!=4 for n in names):
                raise ValueError('Fixed all-projection rank-four matrices required')
            for n in names:merged[n+'.weight']=unmerged[n+'.weight']+unmerged[n+'.B']@unmerged[n+'.A']
            if not equal_state(merged,state['model']):raise ValueError('Native endpoint must equal W0+B@A')
        elif state['trainable_parameters']!=10001152 or not equal_state(unmerged,state['model']):
            raise ValueError('Actual full-model fresh control differs')
        native=JMicroModel(state['model_config']);native.load_state_dict(state['model'],strict=True)
        if sum(p.numel() for p in native.parameters())!=10001152:raise ValueError('Final model size changed')
        audits[arm].update(native_parameters=10001152,trainable_parameters=state['trainable_parameters'],
            optimizer_policy='fresh_Adam_both_arms',original_backbone_unchanged=arm==study.ARMS[1])
        evaluations[arm]=r['arms'][arm]['evaluation']
        summaries[arm],scores[arm]=content(arm,evaluations[arm],record,base,
            study.RUN/f'evaluation/{arm}/evaluation/generation.json',study.RUN/f'{arm}-content-notes.json')
        del state,native
    ref=c['references']['control_result'];saved=read_json(Path(ref['path']));strong=saved['evaluations']['source_order']
    strong_summary,strong_scores=content('historical_full_staged',strong,saved['checkpoints']['source_order'],base,
        Path(ref['path']).parent/'evaluation/source_order/evaluation/generation.json',Path(c['references']['control_notes']['path']))
    if strong_summary['coherent']!=23 or strong_summary['rates']['eos']!=76 or strong_summary['rates']['repetition']!=2:
        raise ValueError('Original strong baseline changed')
    gates={}
    historical_web=read_json(Path(base['reference']['web_screen']['path']))
    for arm in study.ARMS:
        summary=summaries[arm];rates=summary['rates']
        absolute=dict(grammar_at_least56=summary['grammar2']>=56,coherence_at_least27=summary['coherent']>=27,
            appropriate_at_least27=summary['appropriate']>=27,EOS_at_least37=rates['eos']>=37,repetition_at_most18=rates['repetition']<=18,
            no_empty_role_unicode=all(rates[k]==0 for k in ('empty','role_leak','unicode_failure')))
        relative=quality_gates(strong,evaluations[arm],strong_scores,scores[arm],'content')
        web=adoption_checks(historical_web,evaluations[arm])
        gates[arm]=dict(relative_to_unchanged_strong=relative,absolute=absolute,historical_Web=web,
            eligible_for_final_Base_validation=relative['passed'] and all(absolute.values()) and all(web.values()))
    paired=quality_gates(evaluations[study.ARMS[0]],evaluations[study.ARMS[1]],scores[study.ARMS[0]],scores[study.ARMS[1]],'content')
    eligible=[a for a in study.ARMS if gates[a]['eligible_for_final_Base_validation']]
    report=dict(status='qualified_recipe_pending_independent_learning_seed_full_dev_protected_test' if eligible else 'fixed_rank4_and_fresh_full_control_rejected',
        created_at=now(),result=study.reference(study.RUN/'compare-result.json'),config=study.reference(study.CONFIG),
        summaries=summaries,accounting=audits,gates=gates,matched_rank4_vs_full_fresh=paired,
        strong_historical_control_reused_unchanged=strong_summary,eligible_recipes=eligible,
        all160_individually_read=True,independent_human_blind=False,
        actual_science_GPU_seconds=r['GPU_seconds'],own_probe_GPU_seconds=c['verification_GPU_seconds'],
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        next_action='Only qualified recipe enters independent learned seed/full dev/protected test/adoption. Failure ends this fixed comparison without rank/module/scale/LR/source/mask/decoder/checkpoint salvage sweep.')
    destination=study.RUN/'review.json'
    if destination.exists():raise ValueError('Preserve original terminal rank-four review')
    atomic_json(destination,report);atomic_json(ROOT/'reports/phase6/low_rank_base_v2_review.json',report)
    print(json.dumps(dict(status=report['status'],summaries=summaries,eligible_recipes=eligible,matched_rank4=paired),ensure_ascii=False))


if __name__=='__main__':main()
