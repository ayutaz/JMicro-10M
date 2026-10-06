"""Actual native news source experiment and unchanged Japanese selection gates."""
import json
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from jmicro.model import JMicroModel
from phase6_performance import alive, finite_state
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from review_parameter_displacement_anchor import content
from livedoor_base_accounting import accounting
import run_livedoor_base as study


def main():
    torch.set_num_threads(2); c=study.inspect(); job=read_json(study.RUN/'job.json'); r=read_json(study.RUN/'compare-result.json')
    if (job['status'] != 'complete' or alive(job) or r['GPU_seconds'] != job['GPU_elapsed_seconds']
            or r['config_sha256'] != sha256(study.CONFIG) or r['scientific_teacher_tokens'] != study.TOTAL
            or r['reused_prefix_teacher_tokens'] != study.REUSED or r['total_teacher_tokens_from_original_parent'] != 100000000
            or r['evaluation_model_class'] != 'JMicroModel' or r['exact_same_scientific_sources_as_control']
            or set(r['checkpoints']) != {study.ARM} or r['GPU_seconds']+c['verification_GPU_seconds'] > study.CEILING):
        raise ValueError('Actual bounded native news experiment required')
    parent=torch.load(c['parent']['path'], map_location='cpu', weights_only=False); base=read_json(Path(c['original_config']['path']))
    record=r['checkpoints'][study.ARM]; study.check_reference(dict(path=record['checkpoint'], sha256=record['checkpoint_sha256']))
    state=torch.load(record['checkpoint'], map_location='cpu', weights_only=False)
    with torch.random.fork_rng(devices=[]): model=JMicroModel(state['model_config'])
    model.load_state_dict(state['model'], strict=True)
    if (not finite_state(state) or sum(p.numel() for p in model.parameters()) != 10001152
            or len(list(model.named_parameters())) != 119 or len(model.model.layers) != 13
            or model.lm_head.weight is not model.model.embed_tokens.weight
            or record['unique_parameters'] != 10001152 or record['reused_prefix_teacher_tokens'] != study.REUSED
            or state['spec']['news_trainer_sha256'] != c['old_source_sha256']['scripts/livedoor_base_trainer.py']
            or state['spec']['news_manifest_sha256'] != c['data']['news_manifest_sha256']):
        raise ValueError('Actual unchanged native architecture/source differs')
    history=[json.loads(s) for s in (study.RUN/study.ARM/'training/metrics.jsonl').read_text().splitlines()]
    audit=accounting(parent, state, record, history, study.GOALS, study.binding(c))
    matched=study.common_web_continuation(history, [json.loads(s) for s in Path(c['references']['cached_control_history']['path']).read_text().splitlines()], parent)
    if not matched or matched != record['pure_Web_continuation_matched_updates']: raise ValueError('Actual pure-Web continuation required')
    summaries={}; scores={}; candidate=r['evaluations'][study.ARM]
    summaries[study.ARM], scores[study.ARM]=content(study.ARM, candidate, record, base,
        study.RUN/f'evaluation/{study.ARM}/evaluation/generation.json', study.RUN/'content-notes.json')
    previous=read_json(Path(c['references']['cached_control_result']['path']))
    strong=previous['evaluations']['source_order']; strong_record=previous['checkpoints']['source_order']
    folder=Path(c['references']['cached_control_result']['path']).parent
    summaries['strong_staged'], scores['strong_staged']=content('strong_staged', strong, strong_record, base,
        folder/'evaluation/source_order/evaluation/generation.json', ROOT/'reports/phase6/source_order_condition_notes.json')
    if (summaries['strong_staged']['coherent'] != 23 or summaries['strong_staged']['rates']['eos'] != 76
            or summaries['strong_staged']['rates']['repetition'] != 2): raise ValueError('Frozen strong selection baseline differs')
    if ([(v['id'], v['prefix']) for v in strong['generation']['outputs']] != [(v['id'], v['prefix']) for v in candidate['generation']['outputs']]
            or [(v['doc_id'], v['body_tokens'], v['body_bytes']) for v in strong['body']['rows']] != [(v['doc_id'], v['body_tokens'], v['body_bytes']) for v in candidate['body']['rows']]):
        raise ValueError('All fixed Japanese common examples required')
    quality=quality_gates(strong, candidate, scores['strong_staged'], scores[study.ARM], 'content')
    for key in ('transfer', 'retention'):
        t=r[key][study.ARM]
        if t['evaluated_requests'] != 512 or not all(t['checks'].values()) or t['checkpoint_sha256'] != record['checkpoint_sha256']:
            raise ValueError('Complete read-only transfer score required')
    summary=summaries[study.ARM]; rates=summary['rates']
    absolute=dict(grammar_at_least56=summary['grammar2']>=56, coherence_at_least27=summary['coherent']>=27,
        appropriate_at_least27=summary['appropriate']>=27, EOS_at_least37=rates['eos']>=37, repetition_at_most18=rates['repetition']<=18,
        no_empty_role_unicode=all(rates[k]==0 for k in ('empty', 'role_leak', 'unicode_failure')))
    study.check_reference(base['reference']['web_screen']); original=adoption_checks(read_json(Path(base['reference']['web_screen']['path'])), candidate)
    eligible=quality['passed'] and all(absolute.values()) and all(original.values())
    report=dict(status='news100M_all80_content_and_native_state_reviewed', created_at=now(), config_sha256=sha256(study.CONFIG),
        result_sha256=sha256(study.RUN/'compare-result.json'), selection=read_json(study.PROPOSAL)['quality_selection'], summaries=summaries,
        quality_comparison=quality, absolute_dev_screen=absolute, original_Web=original, eligible_for_final_Base_validation=eligible,
        accounting=audit, pure_Web_continuation_matched_updates=matched, new_scientific_teacher_tokens=study.TOTAL,
        reused_prefix_teacher_tokens=study.REUSED, total_teacher_tokens_from_original_parent=100000000,
        verification_teacher_tokens=c['verification_teacher_tokens'], new_total_GPU_seconds=r['GPU_seconds']+c['verification_GPU_seconds'],
        all80_individually_read=True, independent_human_blind=False, Base_complete=False, Base_adopted=False, protected_test_used=False,
        Chat_started=False, quantization_started=False, quality_criteria_unchanged=True,
        limitations='Authored-news source/EOS/diversity replace synthetic post-Web25M; teacher counts match but inputs/updates do not. 523883 local body tokens, about47.265 repeated exposures, old Web overlap/global audit incomplete. One learned seed/nonblind repeated dev.',
        next_action='Qualified recipe only: independent learned seed/full dev/protected test/adoption. Otherwise end fixed news recipe without source/epoch/LR/decoder/checkpoint rescue.')
    destination=study.RUN/'review.json'
    if destination.exists(): raise ValueError('Preserve original news review')
    atomic_json(destination, report); atomic_json(ROOT/'reports/phase6/livedoor_base_comparison_review.json', report)
    print(dict(summaries=summaries, eligible=eligible))


if __name__ == '__main__': main()
