"""CPU-only synthesis of fixed completed evidence, with no new model scoring."""
import hashlib
import json
from pathlib import Path
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
PROPOSAL=ROOT/'reports/phase6/base_failure_route_synthesis_proposal.json'
TARGET=ROOT/'reports/phase6/base_failure_route_synthesis.json'
CONFIGS={
    'historical_parent_condition_comparison_v3_review.json':'historical_parent_condition_comparison_v3',
    'condition_query_balance_comparison_review.json':'condition_query_balance_comparison',
    'early_exposure_comparison_review.json':'early_exposure_comparison',
    'original_web_retention_comparison_review.json':'original_web_retention_comparison',
    'mature_base_condition_comparison_review.json':'mature_base_condition_comparison',
    'textbook_quantity_comparison_review.json':'textbook_quantity_comparison',
    'textbook_coverage_2b_review.json':'textbook_coverage_2b',
    'amount_learning_review.json':'amount_learning_comparison',
    'architecture_comparison_review.json':'architecture_comparison',
    'material_comparison_review.json':'material_comparison',
}


def read(path):return json.loads(path.read_text(encoding='utf-8'))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def ref(path):return dict(path=str(path),sha256=sha(path))


def summary_row(name,point,s,report,c):
    row=dict(report=name,point=point,generation_sha256=s.get('generation_sha256'),
        BPB=s.get('BPB'),grammar2=s.get('grammar2'),relevance2=s.get('relevance2'),
        coherent=s.get('coherent'),appropriate=s.get('appropriate'),rates=s.get('rates'),Japanese=s.get('Japanese'),
        prepared_tokens=s.get('prepared_tokens'),newly_scored=False,
        additional_teacher_tokens=s.get('additional_teacher_tokens'),
        stable_teacher_tokens=s.get('stable_teachers',s.get('scientific_teachers')),
        decay_teacher_tokens=s.get('decay_teachers'),
        valid_input_tokens=s.get('valid_input_tokens'),physical_tokens=s.get('physical_tokens'),
        recorded_training_step_seconds=s.get('seconds',s.get('training_step_seconds')),
        parent=c.get('parent'),parents=c.get('parents'),model_config=c.get('model_config'),
        shapes=c.get('shapes'),arms=c.get('arms'),
        config_nominal_peak_LR=c.get('peak_lr',c.get('lr')),
        actual_optimizer_LR=None,
        study_reported_eligibility=report.get('eligible_for_final_Base_validation'),
        unknown_fields_policy='Absent budget/state fields remain null; nominal config LR is not actual optimizer LR.')
    if 'exposure' in s:row['exposure']=s['exposure']
    if 'stable_exposure' in s:row['stable_exposure']=s['stable_exposure']
    return row


def distinct_generations(rows):
    known={};unknown=[]
    for row in rows:
        key=row['generation_sha256']
        if key is None:unknown.append(dict(report=row['report'],point=row['point']));continue
        signature={k:row[k] for k in ('BPB','grammar2','relevance2','coherent','appropriate','rates','Japanese')}
        if key in known and known[key]['metrics']!=signature:raise ValueError('Identical raw generation has conflicting saved metrics')
        known.setdefault(key,dict(metrics=signature,appearances=[]))['appearances'].append(dict(report=row['report'],point=row['point']))
    return dict(known=known,unknown=unknown,known_unique_count=len(known),all_rows_count=len(rows),
        note='Repeated cached control summaries are appearances of one learned checkpoint, not independent runs or new teachers. Missing hashes are unknown, not assumed unique.')


def main():
    started=time.monotonic();p=read(PROPOSAL)
    if (p['CPU_limit_seconds']!=30 or p['GPU_seconds'] or p['new_scientific_teacher_tokens'] or p['optimizer_updates']
            or p['Base_complete'] or p['Chat_started'] or p['quantization_started'] or p['protected_test_used']):raise ValueError('CPU-only fixed synthesis required')
    if TARGET.exists():raise ValueError('Preserve existing synthesis')
    reports={};refs={};configs={};rows=[]
    for name,r in p['references'].items():
        path=Path(r['path'])
        if sha(path)!=r['sha256']:raise ValueError('Fixed report SHA differs')
        report=read(path)
        if report.get('protected_test_used') or report.get('Base_adopted') or report.get('Chat_started') or report.get('quantization_started'):raise ValueError('Preserve current unqualified Base scope')
        reports[name]=report;refs[name]=r;c={}
        if name in CONFIGS:
            path=ROOT/'configs/phase6'/f'{CONFIGS[name]}.json'
            if path.exists():configs[name]=ref(path);c=read(path)
        for point,s in report.get('summaries',{}).items():rows.append(summary_row(name,point,s,report,c))
        if time.monotonic()-started>30:raise TimeoutError('CPU30s synthesis exhausted')
    if len(reports)!=13:raise ValueError('Exactly13 fixed reports required')
    indexed={(r['report'],r['point']):r for r in rows}
    get=lambda name,point:indexed[name+'.json',point]
    h=get('historical_parent_condition_comparison_v3_review','historical_parent');control=get('historical_parent_condition_comparison_v3_review','control')
    q=get('condition_query_balance_comparison_review','query_balanced')
    early=get('early_exposure_comparison_review','early8M')
    small=get('textbook_quantity_comparison_review','small-1000000000');large=get('textbook_quantity_comparison_review','large-1000000000')
    a=get('amount_learning_review','large-1000000000');b=get('amount_learning_review','large-2000000000')
    decisions=[
        dict(hypothesis='Prepared material volume alone suffices',decision='not supported as a sufficient remedy',
            evidence=dict(quantity500M_vs2B=dict(coherence=[small['coherent'],large['coherent']],BPB=[small['BPB'],large['BPB']],gates=reports['textbook_quantity_comparison_review.json'].get('quantity_comparison'))),
            limitation='This does not prove volume is irrelevant; sources, selectors and tested teacher budgets delimit the result.'),
        dict(hypothesis='More teacher exposure alone suffices',decision='learning benefits are real but do not meet Base criteria',
            evidence=dict(same500M_material1B_vs2B=dict(coherence=[a['coherent'],b['coherent']],BPB=[a['BPB'],b['BPB']])),
            limitation='No automatic extension or claim that an untested longer run must work. Existing2B-to5B completion may be linked separately; not newly measured here.'),
        dict(hypothesis='Stop original-Web short-source route earlier',decision='preselected earliest saved8.15M does not rescue quality',
            evidence=dict(coherence=[early['coherent'],control['coherent']],EOS=[early['rates']['eos'],control['rates']['eos']]),
            limitation='One nested trajectory; no further checkpoint selection by quality.'),
        dict(hypothesis='Higher historical parent Web quality solves free generation',decision='historical route rejected despite passing Web guard',
            evidence=dict(BPB=[control['BPB'],h['BPB']],coherence=[control['coherent'],h['coherent']],repetition=[control['rates']['repetition'],h['rates']['repetition']],gates=reports['historical_parent_condition_comparison_v3_review.json']['quality_comparison']),
            limitation='Parent model/Adam/RNG/scheduler/actualLR/cursor differ together; not isolated LR causality.'),
        dict(hypothesis='Balancing longest/shortest training queries rescues transfer and free text',decision='predefined intervention failed both main and secondary screens',
            evidence=dict(coherence=[control['coherent'],q['coherent']],mechanism=reports['condition_query_balance_comparison_review.json']['mechanism_screen']),
            limitation='No template/query variant sweep.'),
        dict(hypothesis='Gradient surgery is warranted',decision='predefined local conflict marker absent',
            evidence=reports['base_source_diagnostics_completion.json']['gradient_conflict_screen_supported'],limitation='Local assay is not proof of no conflict in all training.'),
        dict(hypothesis='Two tested10M shapes or source replacements settle capacity',decision='comparisons failed; capacity ceiling remains unproved',
            evidence=dict(architecture=reports['architecture_comparison_review.json']['gates'],material=reports['material_comparison_review.json']['gates']),
            limitation='Small source,300M teachers and tested architectures do not cover all10M training strategies.'),
        dict(hypothesis='Good train fit/local structured scores establish Japanese Base quality',decision='contradicted as an acceptance proxy',
            evidence=dict(historical_bridge=reports['historical_parent_condition_comparison_v3_review.json']['transfer_aggregates'],historical_free_coherence=h['coherent']),
            limitation='Shared-generator local probes are distinct from free-text consistency and protected test.'),
    ]
    result=dict(status='completed_CPU_fixed13_Base_failure_route_synthesis',references=refs,direct_config_references=configs,
        source_sha256=sha(Path(__file__)),proposal=ref(PROPOSAL),rows=rows,distinct_generations=distinct_generations(rows),hypothesis_decisions=decisions,
        conclusions=['No cited candidate is an adopted Base. Web BPB, EOS count and local structured transfer are insufficient quality proxies.',
            'Larger material and teacher budgets sometimes help but neither guarantees grammar/coherence. Historical parent route failed; do not repeat it.',
            'The remaining issue is generalization of coherent natural short prose while preserving Web quality; the completed interventions mostly adjust existing mixtures/templates or parent states.',
            'A materially different data/objective route needs an explicit novelty and feasibility check before any additional GPU training. A new arbitrary ratio/LR/template or longer-run sweep is unjustified.'],
        next_decision='Do not start GPU from this synthesis alone. Check whether a train-only, public-license, substantially diverse natural Japanese prose distillation/source route has already been tried and is feasible locally; define one finite controlled comparison only if it is new and meets source quality/retention constraints.',
        CPU_seconds=time.monotonic()-started,GPU_seconds=0,new_scientific_teacher_tokens=0,optimizer_updates=0,new_content_judgments=0,
        Base_adopted=False,Base_complete=False,Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True,
        limitations=p['limitations'])
    temp=TARGET.with_suffix('.tmp');temp.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');temp.replace(TARGET)
    print(json.dumps(dict(status=result['status'],CPU_seconds=result['CPU_seconds'],rows=len(rows),unique_known_generations=result['distinct_generations']['known_unique_count'],unknown_raw_hash_rows=len(result['distinct_generations']['unknown']))))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
