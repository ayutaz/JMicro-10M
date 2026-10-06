"""Create owned comparison files; never rewrite frozen historical sources."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT

CONTRACT = '''def source_contract():
    old,base,parent,_,_,positive,original=cached.source_contract()
    p=read_json(PROPOSAL)
    for ref in p['cached_control'].values():check_reference(ref)
    check_reference(p['parent']);check_reference(p['source_registry_review']);check_reference(p['CPU_sampler_tests'])
    for path,digest in p['source_sha256'].items():
        if sha256(ROOT/path)!=digest:raise ValueError('Frozen order sampler/test source differs')
    if (p['quotas']!=GOALS or p['new_scientific_teacher_tokens']!=TOTAL or p['reused_control_teacher_tokens']!=TOTAL
            or p['new_GPU_ceiling_seconds']!=CEILING or p['actual_inherited_LR']!=.00001
            or p['Base_adopted'] or p['Base_complete'] or p['Chat_started'] or p['quantization_started']
            or p['protected_test_used'] or not p['quality_criteria_unchanged'] or p['source']!=old['positive_data']
            or p['source_order']!=list(SOURCE_ORDER)):
        raise ValueError('Fixed same-parent same-teacher source-order scope required')
    expected={k:v for k,v in p['parent_actual_metadata'].items() if k!='checkpoint'}
    if parent_metadata(parent)!=expected or old['parent']!=p['parent']:
        raise ValueError('Actual same historical fullstate differs')
    job=read_json(cached.RUN/'job.json');result=read_json(cached.RUN/'compare-result.json')
    review=read_json(Path(p['cached_control']['review']['path']))
    control=result['checkpoints']['historical_parent'];ev=result['evaluations']['historical_parent']
    if (job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(cached.RUN/'compare-result.json')
            or control['additional_supervised_tokens']!=TOTAL or control['source_teachers']!=GOALS
            or control['checkpoint_sha256']!=ev['checkpoint_sha256'] or control['binding']!=ev['binding']
            or review['summaries']['historical_parent']['notes_sha256']!=p['cached_control']['notes']['sha256']
            or dict(path=control['checkpoint'],sha256=control['checkpoint_sha256'])!=p['cached_control']['checkpoint']):
        raise ValueError('Actual terminal same-parent100M mixed control required')
    return old,base,parent,control,ev,positive,original


'''

PREPARE = '''def prepare_probe():
    if PROBE_CONFIG.exists():inspect(PROBE_CONFIG);return
    old,_,_,control,_,_,_=source_contract()
    c=copy.deepcopy(read_json(cached.PROBE_CONFIG))
    c.update(research_kind=KIND,phase='probe',arms={ARM:GOALS},outcome_weights={ARM:1},
        GPU_budget_seconds=120,total_new_GPU_ceiling_seconds=CEILING,failed_probe_GPU_seconds=0,
        reused_control_checkpoint=dict(path=control['checkpoint'],sha256=control['checkpoint_sha256']),
        source_order=list(SOURCE_ORDER),created_at=now(),source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        sampler_policy='Same historical10.5B fullstate/actualLR.00001, same exact100M quotas and all four per-source streams/cursors as cached mixed control. Only order is Web then story then ordinary then conditional; no stage reset, no reheat, same all-masked Web terminal padding.')
    refs=c['references']
    refs.update(proposal=reference(PROPOSAL),control_config=reference(cached.CONFIG),
        control_result=reference(cached.RUN/'compare-result.json'),
        control_review=reference(ROOT/'reports/phase6/historical_parent_condition_comparison_v3_review.json'),
        control_notes=reference(ROOT/'reports/phase6/historical_parent_condition_notes.json'),
        control_generation=reference(cached.RUN/'evaluation/historical_parent/evaluation/generation.json'))
    scope(c);atomic_json(PROBE_CONFIG,c);inspect(PROBE_CONFIG)
    print('Same-parent source-order CUDA probe frozen; scientific learning not started',flush=True)


'''


def replace_function(source,start,end,replacement):
    a=source.index('def '+start+'(');b=source.index('def '+end+'(',a)
    return source[:a]+replacement+source[b:]


def write_new(relative,text):
    path=ROOT/relative
    if path.exists():raise ValueError('Preserve owned existing version: '+relative)
    path.write_text(text,encoding='utf-8',newline='\n')


def main():
    text=(ROOT/'scripts/run_historical_parent_condition_comparison_v3.py').read_text()
    text=text.replace('from historical_parent_condition_trainer import HistoricalParentTrainer,historical_web_cursor',
        'from source_order_condition_trainer import SourceOrderHistoricalTrainer,SOURCE_ORDER\nfrom historical_parent_condition_trainer import historical_web_cursor\nimport run_historical_parent_condition_comparison_v3 as cached')
    text=text.replace('historical-parent-condition-comparison-v3-20261006','source-order-condition-comparison-20261006')
    text=text.replace('historical_parent_condition_comparison_v3.json','source_order_condition_comparison.json')
    text=text.replace('historical_parent_condition_probe_v3.json','source_order_condition_probe.json')
    text=text.replace('historical_parent_condition_comparison_v3_proposal.json','source_order_condition_comparison_proposal.json')
    text=text.replace("ARM='historical_parent'","ARM='source_order'").replace("KIND='historical_Web_parent_inherited_condition_100M'","KIND='historical_parent_source_order_100M'")
    a=text.index('SOURCES=');b=text.index('reference,check_reference=',a)
    text=text[:a]+"SOURCES=tuple(dict.fromkeys(('scripts/run_source_order_condition_comparison.py','scripts/run_source_order_condition_comparison.ps1',\n    'scripts/review_source_order_condition_comparison.py','scripts/source_order_condition_trainer.py',\n    'tests/test_source_order_condition.py','tests/test_source_order_comparison.py',*cached.SOURCES)))\n"+text[b:]
    text=replace_function(text,'source_contract','prepare_probe',CONTRACT)
    text=replace_function(text,'prepare_probe','scope',PREPARE)
    text=text.replace("c['failed_probe_GPU_seconds']!=read_json(PROPOSAL)['failed_probe_GPU_seconds']","c['failed_probe_GPU_seconds']!=0 or c['source_order']!=list(SOURCE_ORDER)")
    text=text.replace('return HistoricalParentTrainer(', 'return SourceOrderHistoricalTrainer(')
    text=text.replace("reused=read_json(previous.RUN/'compare-result.json')","reused=read_json(cached.RUN/'compare-result.json')")
    text=text.replace("reused['transfer']['original_web']","reused['transfer']['historical_parent']").replace("reused['retention']['original_web']","reused['retention']['historical_parent']")
    text=text.replace('scripts/run_historical_parent_condition_comparison_v3.ps1','scripts/run_source_order_condition_comparison.ps1')
    text=text.replace('historical_parent100M_and_reused_original10B_route100M_complete','source_order100M_and_cached_same_parent_mixed100M_complete')
    text=text.replace('actual_historical_parent_resume_timing_complete','actual_source_order_resume_timing_complete')
    text=text.replace('measured100M_historical_parent_frozen','measured100M_source_order_frozen')
    text=text.replace('"""Historical Web fullstate route vs cached original10B route; equal100M teachers."""',
        '"""Same historical fullstate and100M streams; change cross-source order only."""')
    write_new('scripts/run_source_order_condition_comparison.py',text)
    ps=(ROOT/'scripts/run_historical_parent_condition_comparison_v3.ps1').read_text()
    ps=ps.replace('historical-parent-condition-v3-','source-order-condition-')
    ps=ps.replace('historical-parent-condition-comparison-v3-20261006','source-order-condition-comparison-20261006')
    ps=ps.replace('run_historical_parent_condition_comparison_v3','run_source_order_condition_comparison')
    ps=ps.replace('historical parent','source order').replace('Historical parent','Source order')
    write_new('scripts/run_source_order_condition_comparison.ps1',ps)
    review=(ROOT/'scripts/review_historical_parent_condition_comparison_v3.py').read_text()
    review=review.replace('import run_historical_parent_condition_comparison_v3 as study','import run_source_order_condition_comparison as study')
    review=review.replace("ROOT / 'reports/phase6/original_web_retention_notes.json'","ROOT / 'reports/phase6/historical_parent_condition_notes.json'")
    review=review.replace("ROOT / 'reports/phase6/historical_parent_condition_notes.json'\n", "ROOT / 'reports/phase6/source_order_condition_notes.json'\n")
    review=review.replace("study.previous.RUN / 'evaluation/original_web/evaluation/generation.json'","study.cached.RUN / 'evaluation/historical_parent/evaluation/generation.json'")
    review=review.replace("['summaries']['original_web']","['summaries']['historical_parent']")
    review=review.replace("study.previous.RUN / 'compare-result.json'","study.cached.RUN / 'compare-result.json'")
    review=review.replace("reused[key]['original_web']","reused[key]['historical_parent']")
    review=review.replace('historical_parent100M_all80_and_reused_original10B_route100M_reviewed','source_order100M_all80_and_cached_same_parent_mixed100M_reviewed')
    review=review.replace('historical_parent_route-vs-original10B_route','staged-source-order-vs-interleaved-same-parent-same-teachers')
    review=review.replace('historical_parent_condition_comparison_v3_review.json','source_order_condition_comparison_review.json')
    review=review.replace("    web = sampler['streams']['web']", "    if not equal_state(sampler['streams']['web'],other['streams']['web']):\n        raise ValueError('Same-parent Web terminal cursor differs')\n    for key in ('source_teachers','source_eos','source_tokens','source_body_bytes','source_focus_teachers'):\n        if sampler[key]['web']!=other[key]['web']:raise ValueError('Same-parent Web terminal accounting differs')\n    web = sampler['streams']['web']")
    review=review.replace("    return dict(short_source_cursors_and_accounting_equal=True,", "    return dict(all_four_source_cursors_and_accounting_equal=True,")
    review=review.replace("    sampler = state['sampler']", "    sampler = state['sampler']\n    if sampler.get('kind')!='same-streams-staged-source-order-v1' or sampler.get('source_order')!=list(study.SOURCE_ORDER):\n        raise ValueError('Fixed staged source ordering missing')")
    review=review.replace("            or state['spec']['historical_trainer_sha256'] != c['source_sha256']['scripts/historical_parent_condition_trainer.py']):", "            or state['spec']['historical_trainer_sha256'] != c['source_sha256']['scripts/historical_parent_condition_trainer.py']\n            or state['spec']['source_order_trainer_sha256'] != c['source_sha256']['scripts/source_order_condition_trainer.py']\n            or state['spec']['source_order'] != list(study.SOURCE_ORDER)):")
    write_new('scripts/review_source_order_condition_comparison.py',review)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python required')
    main()
