"""Finite cached gap synthesis and one preregistered midpoint, no GPU or corpus scan."""
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
import time
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json

CONFIG = ROOT / 'configs/phase6/weight_average_comparison.json'
RUN = ROOT / 'reports/phase6/weight-average-comparison-20261006'
GAP = ROOT / 'reports/phase6/base_intervention_gap_synthesis.json'
SOURCES = ('scripts/weight_average_checkpoint.py', 'scripts/prepare_weight_average_comparison.py',
    'scripts/run_weight_average_comparison.py', 'scripts/run_weight_average_comparison.ps1',
    'scripts/review_weight_average_comparison.py', 'tests/test_weight_average_checkpoint.py')


def reference(path):
    return dict(path=str(path), sha256=sha256(path))


def main():
    if CONFIG.exists() or GAP.exists():
        raise ValueError('Preserve frozen single midpoint and cached synthesis')
    started = time.monotonic()
    names = ('source_order_condition_comparison_v2_review.json', 'web_kl_comparison_completion.json',
        'eos_decoupled_web_kl_comparison_completion.json', 'hard_body_web_replay_comparison_completion.json',
        'context_outcome_ranking_comparison_completion.json', 'anchored_context_outcome_comparison_completion.json')
    source_names = ('narrative_condition_source_completion.json', 'natural_story_source_completion.json',
                    'translated_story_source_completion.json')
    files = [ROOT / 'reports/phase6' / name for name in (*names, *source_names)]
    if any(p.stat().st_size > 2*1024*1024 for p in files):
        raise ValueError('Finite summary metadata only; no raw/gigantic index read')
    models = {}; sources = []
    for path in files[:len(names)]:
        record = read_json(path)
        if record['Base_adopted'] or record['protected_test_used']:
            raise ValueError('Existing rejected, protected-test-unopened history required')
        for arm, summary in record['summaries'].items():
            key = summary['generation_sha256']
            value = dict(arm=arm, BPB=summary['BPB'], grammar=summary['grammar2'],
                coherence=summary['coherent'], appropriate=summary['appropriate'],
                EOS=summary['rates']['eos'], repetition=summary['rates']['repetition'],
                raw_generation_sha256=key, notes_sha256=summary['notes_sha256'], references=[])
            if key in models:
                if {k:v for k,v in models[key].items() if k not in ('arm','references')} != {k:v for k,v in value.items() if k not in ('arm','references')}:
                    raise ValueError('Repeated immutable model summary disagrees')
            else:
                models[key] = value
            models[key]['references'].append(reference(path))
    for path in files[len(names):]:
        record = read_json(path)
        if record['training_pool_accepted'] or record['GPU_seconds']:
            raise ValueError('Preserved pretraining source rejection required')
        sources.append(dict(source=path.stem, weak=record['weak_documents'],
            unresolved_expression=record['unresolved_grammar_documents'],
            unresolved_grounding=record['unresolved_grounding_documents'], reference=reference(path)))
    elapsed = time.monotonic() - started
    if elapsed > 10:
        raise TimeoutError('Bounded metadata synthesis exceeded10s')
    atomic_json(GAP, dict(status='seven_immutable_models_three_failed_sources_synthesized', created_at=now(),
        models=list(models.values()), rejected_source_routes=sources, metadata_bytes_read=sum(p.stat().st_size for p in files),
        CPU_seconds=elapsed, CPU_ceiling_seconds=10, GPU_seconds=0, scientific_teacher_tokens=0,
        conclusion='Staged CE has the best coherence/EOS/repetition in these same-parent trials but fails historical Web BPB. '
            'Web regularizers recover BPB near the historical guard while broad coherence remains poor. '
            'All three replacement-source routes fail readiness. These observations support testing a fixed parameter midpoint, '
            'not a quality guarantee, corpus-wide certification or another KL/source filter sweep.',
        old_numerical7_preserved=True, quality_criteria_unchanged=True, protected_test_used=False))
    tests = ROOT / 'reports/phase6/weight_average_tests.xml'
    suite = ET.parse(tests).getroot().find('testsuite')
    if int(suite.attrib['tests']) != 3 or any(int(suite.attrib[k]) for k in ('errors','failures','skipped')):
        raise ValueError('Three midpoint/identity/finite-state tests required')
    old_config = ROOT / 'configs/phase6/source_order_condition_comparison_v2.json'
    result_path = ROOT / 'reports/phase6/source-order-condition-comparison-v2-20261006/compare-result.json'
    old = read_json(old_config); result = read_json(result_path)
    checkpoints = {arm: {k:detail[k] for k in ('checkpoint','checkpoint_sha256','additional_supervised_tokens','source_teachers')}
                   for arm,detail in result['checkpoints'].items()}
    if set(checkpoints) != {'control','source_order'} or any(v['additional_supervised_tokens']!=100000000 for v in checkpoints.values()):
        raise ValueError('Named completed same-parent100M endpoints required')
    base_config = ROOT / 'configs/phase6/textbook_quantity_comparison.json'; base=read_json(base_config)
    evaluation_paths = (base_config, ROOT/base['evaluation']['config'], ROOT/'eval/base.jsonl',
        ROOT/'eval/japanese_semantics_v2_1.jsonl', Path(base['dev_shards'])/'manifest.json', ROOT/base['tokenizer'],
        ROOT/'scripts/run_complete_text_comparison.py', ROOT/'src/jmicro/model.py', ROOT/'src/jmicro/readiness.py',
        ROOT/'src/jmicro/japanese_evaluation.py', ROOT/'src/jmicro/tokenizer.py', ROOT/'scripts/evaluate_japanese_base.py',
        ROOT/'scripts/run_eos_short_pilot.py', ROOT/'scripts/review_matched_story_study.py',
        ROOT/'scripts/run_eos_complete_100m.py', ROOT/'uv.lock')
    references = dict(gap=reference(GAP), completed_result=reference(result_path), control_review=reference(files[0]),
        source_config=reference(old_config), source_cases=old['references']['source_cases'],
        retention_cases=old['references']['retention_cases'],
        strong_notes=reference(ROOT/'reports/phase6/source_order_condition_notes.json'),
        historical_Web_evaluation=base['reference']['web_screen'], CPU_tests=reference(tests))
    config = dict(kind='same_parent_fixed_half_weight_midpoint_research', created_at=now(),
        common_parent=old['parent'], checkpoints=checkpoints, coefficients=[.5,.5],
        arithmetic='Original FP32 tensor0.5*a+0.5*b; identical tied embedding; nonfloating buffers equal. '
            'No optimizer/scheduler/RNG/sampler/update/token counters fabricated or averaged.',
        refs=references, evaluation_refs=[reference(p) for p in evaluation_paths],
        source_sha256={p:sha256(ROOT/p) for p in SOURCES}, evaluation_base_config=str(base_config),
        strong_quality_control='source_order', evaluation_GPU_ceiling_seconds=300,
        preparation_CPU_ceiling_seconds=60, new_scientific_teacher_tokens=0, new_optimizer_updates=0,
        parameter_count=10001152, decoder='unchanged native BF16 math greedy64, EOS3 and original suppress policy',
        quality_gate='Unchanged strong relative coherence23+8/pairedCI>0/EOS>=76/repetition<=2/BPB<=1.1336128657420816*1.01; '
            'absolute grammar>=56/coherence>=27/appropriate>=27/EOS>=37/repetition<=18; historical WebBPB<=.9812859519097707 '
            'and existing stop/error guards. No criterion relaxed or stronger control replaced by mixed control.',
        evaluation='256 complete dev bodies/same bytes; Japanese192-331-1119; fixed80 all individually read/raw-bound; bridge128/retention128',
        completion_condition='One exactly50% merged endpoint, all specified read-only evaluations and80 notes, all original gates, '
            'actual PID terminal, failed costs, original UI restored and verified milestone commit. Qualified pilot only then independent '
            'learned recipe seed/full dev/protected test/adoption; notify at actual Base completion.',
        failure='Preserve result and terminate this midpoint recipe. No coefficient/endpoint/checkpoint/layer selection sweep or decoder calibration.',
        research_sources=[dict(title='Robust fine-tuning of zero-shot models',url='https://arxiv.org/abs/2109.01903',
            application='Weight interpolation can mitigate distribution shift in studied vision models; applying it to this10M Japanese Base is an unproven inference.'),
            dict(title='Model soups',url='https://arxiv.org/abs/2203.05482',
            application='Same pretrained initialization can make weight averaging useful. This experiment is one fixed pair, not a greedy hyperparameter soup.')],
        limitations='Previously reused dev, one shared learned parent/seed and correlated branches. Endpoints selected from observed tradeoff, '
            'so exploratory research rather than independent validation; equal coefficient fixed before any new midpoint scoring. '
            'Different source order is the endpoint intervention; no clean new corpus or independent seed produced.',
        quality_criteria_unchanged=True, protected_test_used=False, Base_complete=False, Base_adopted=False,
        Chat_started=False, quantization_started=False)
    atomic_json(CONFIG, config)
    print(json.dumps(dict(status='gap_synthesis_and_single_midpoint_frozen', models=len(models), sources=len(sources),
        CPU_seconds=elapsed, source_checks=True, new_GPU_seconds=0)))


if __name__=='__main__':
    main()
