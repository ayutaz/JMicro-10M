"""Bind and audit completed read-only repetition diagnostics; emit review."""
import argparse
from collections import Counter
import json
from pathlib import Path
import statistics
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.repetition_diagnosis import paired_transitions, repetition_details
from jmicro.tokenizer import Tokenizer
from investigate_repetition import CHECKPOINTS, GENERATION, binding, describe
from phase6_performance import alive


def greedy_rows(generation):
    return [r for r in generation['outputs'] if r['decoding'] == 'greedy' and r['suppressed']]


def trace_summary(rows):
    traces = [r['trace'] for r in rows]
    return {'first16_entropy_mean': statistics.mean(t['entropy_nats'] for trace in traces for t in trace[:16]),
        'last16_entropy_mean': statistics.mean(t['entropy_nats'] for trace in traces for t in trace[-16:]),
        'first16_top_probability_mean': statistics.mean(t['top_probability'] for trace in traces for t in trace[:16]),
        'last16_top_probability_mean': statistics.mean(t['top_probability'] for trace in traces for t in trace[-16:]),
        'last16_eos_probability_mean': statistics.mean(t['eos_probability'] for trace in traces for t in trace[-16:]),
        'eos_ever_argmax_before_suppression': sum(any(t['eos_is_argmax'] for t in trace) for trace in traces),
        'scope': '8 reproduced cases for old/decay; 80 cases for stable. Compare like counts only.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', type=Path, default=ROOT/'reports/phase6/repetition-diagnosis-20261003')
    parser.add_argument('--output', type=Path, default=ROOT/'reports/phase6/repetition_diagnosis_review.json')
    args = parser.parse_args()
    run = args.run
    checks = {}
    def require(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise ValueError('Diagnostic evidence audit failed: '+name)
    def verify_bound(record):
        return sha256(Path(record['path'])) == record['sha256']
    plan = read_json(ROOT/'reports/phase6/repetition_diagnosis_plan.json')
    cpu, gpu = read_json(run/'cpu.json'), read_json(run/'gpu.json')
    for phase in ('cpu', 'gpu'):
        job = read_json(run/f'job-{phase}.json')
        require(phase+'_job_terminal', job['status'] == 'complete' and not alive(job))
        require(phase+'_source_and_plan_bound', verify_bound(job['plan']) and all(sha256(ROOT/name) == digest for name,digest in job['source'].items()))
    require('GPU_within_predeclared_budget_no_training', gpu['seconds'] <= plan['budgets']['GPU_inference_seconds'] and gpu['training_updates'] == 0)
    require('cpu_and_gpu_raw_reports_bound', all(verify_bound(r) for r in [*cpu['data_reports'].values(), *gpu['records'].values(), *cpu['generation_bindings'].values()]))
    require('full_dev_eos_raw_reports_bound', all(verify_bound(r['report']) for r in cpu['full_dev_eos'].values()))
    records = {name: read_json(Path(record['path'])) for name,record in gpu['records'].items()}
    require('all_five_checkpoints_immutable', records.keys() == CHECKPOINTS.keys() and all(verify_bound(r) and r['checkpoint_unchanged'] and r['state_and_rng_unchanged'] for r in records.values()))
    datasets = {name: read_json(Path(record['path'])) for name,record in cpu['data_reports'].items()}
    for name, data in datasets.items():
        require(name+'_full_stream_checks_and_exact_sampler', data['checksummed_stream_and_index'] and verify_bound(data['manifest']) and all(r['exact_masked_count_verified'] and verify_bound(r) and r['eos_teachers'] > 0 for r in data['consumed'].values()))
        require(name+'_sample_count', len(data['sample_rows']) == data['sample_count'] == plan['budgets']['content_sample_documents_per_dataset'])
    require('old_and_decay_eight_case_generation_reproduction', all(len(records[name]['reproduction']) == plan['budgets']['exact_generation_reproduction_cases'] and all(r['identical_generated_ids'] for r in records[name]['reproduction']) for name in ('100M','decay500M')))
    require('eight_cases_each_precision_path_retained', all(len(records[name]['precision']['rows']) == 24 for name in ('100M','decay500M')))
    config = read_json(ROOT/'configs/phase6/base_frozen.json')
    tok = Tokenizer(ROOT/config['tokenizer'])
    cases = [json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines()]
    ids = [r['id'] for r in cases if r['split'] == 'dev']
    generations = {name: read_json(path)['generation'] for name,path in GENERATION.items()}
    trajectory = {'100M': greedy_rows(generations['100M']), 'decay500M': greedy_rows(generations['decay500M'])}
    for name in ('stable131M','stable328M','stable500M'):
        rows = records[name]['trajectory']
        require(name+'_80_fixed_cases_and_redecoded_flags', [r['id'] for r in rows] == ids and all(
            tok.decode_bytes(r['generated_ids']).decode(errors='replace') == r['text'] and repetition_details(r['text'])['repetition'] == r['repetition'] and r['eos'] == (r['generated_ids'][-1] == 3) and len(r['generated_ids']) <= 64 for r in rows))
        trajectory[name] = [{**r, 'decoding': 'greedy', 'suppressed': True, 'seed': 42, 'stop_reason': 'stop_id' if r['eos'] else 'max_new_tokens'} for r in rows]
    matched_ids = [[r['doc_id'] for r in records[name]['ending_probes']['endings']] for name in ('100M','stable500M','decay500M')]
    require('256_same_dev_endings_and_80_short_prefixes', matched_ids[0] == matched_ids[1] == matched_ids[2] and len(matched_ids[0]) == 256 and all(len(records[name]['ending_probes']['prefixes']) == 80 for name in ('100M','stable500M','decay500M')))
    preservation = read_json(run/'preservation.json')
    require('225_existing_source_configs_eval_lock_reports_preserved', preservation['passed'] and preservation['files'] == 225 and not preservation['mismatches'] and sha256(run/'protected-before.json') == preservation['baseline_sha256'])
    xml = ET.parse(run/'tests.xml').getroot()
    suites = [xml] if xml.tag == 'testsuite' else list(xml.iter('testsuite'))
    tests = {key: sum(int(s.get(key,0)) for s in suites) for key in ('tests','failures','errors','skipped')}
    require('tests_passed_no_skips', tests['tests'] >= 102 and not (tests['failures'] or tests['errors'] or tests['skipped']))
    eos_probes = {name: {k:v for k,v in record['ending_probes'].items() if k not in ('endings','prefixes')} for name,record in records.items() if 'ending_probes' in record}
    trajectory_summary = {name: {'outputs': len(rows), 'repetition': sum(r['repetition'] for r in rows), 'eos': sum(r['stop_reason'] == 'stop_id' for r in rows),
        'first_match_end_char_when_repetitive': describe([repetition_details(r['text'])['first_match_end_char'] for r in rows if r['repetition']])} for name,rows in trajectory.items()}
    precision = {name: records[name]['precision'] for name in ('100M','decay500M')}
    traces = {name: trace_summary(record['trajectory'] if 'trajectory' in record else [r['diagnostic'] for r in record['reproduction']]) for name,record in records.items()}
    decay_transition = paired_transitions(trajectory['stable500M'], trajectory['decay500M'])
    report = {'status': 'completed_read_only_investigation', 'completed_at': now(), 'checks': checks,
        'reviewer_source': binding(ROOT/'scripts/review_repetition_diagnosis.py'),
        'plan': binding(ROOT/'reports/phase6/repetition_diagnosis_plan.json'),
        'raw_evidence': {name: binding(run/name) for name in ('cpu.json','gpu.json','job-cpu.json','job-gpu.json','preservation.json','tests.xml')},
        'tests': tests, 'gpu_inference_seconds': gpu['seconds'], 'training_updates': 0,
        'paired_transitions': cpu['paired_transitions'], 'trajectory': trajectory_summary,
        'stable_to_decay_transitions': decay_transition,
        'data_summary': {name: {**{k:v for k,v in data.items() if k != 'sample_rows'},
            'sample_repeated_units_top10': Counter(r['repeated_unit'] for r in data['sample_rows'] if r['repetition']).most_common(10),
            'sample_repeated_units_length_at_least4': sum(r['repetition'] and len(r['repeated_unit']) >= 4 for r in data['sample_rows'])} for name,data in datasets.items()},
        'full_dev_eos': cpu['full_dev_eos'], 'matched_ending_and_prefix_probes': eos_probes,
        'generation_traces': traces, 'precision': precision,
        'findings': [
            {'conclusion': 'EOS is supervised; an EOS mask/omission or a substantial new dilution is not supported.',
             'evidence': 'Only BOS targets are masked; full BOS/EOS streams and saved sampler positions reproduce exact masked-token counters. Stable500M has1,061,096EOS teachers; decay end1,114,159. EOS teacher density is0.2127% vs0.2151% old.'},
            {'conclusion': 'True document-ending prediction improves, while short-prefix continuation rarely selects EOS.',
             'evidence': 'Full same89416 dev EOS meanNLL3.00827->2.53698; geometric mean probability4.94%->7.91%. Same256 endings EOS argmax30->35; same80 short prefixes EOS argmax0 for old/stable/decay. Final prefix mean probability0.00247%. EOS remains below top continuation during all traced greedy steps.'},
            {'conclusion': 'The expanded model already repeats heavily by131M; decay is not the source of the aggregate worsening.',
             'evidence': 'Greedy repetition69/80 at131M,70/80 at328M,70/80 at stable500M,66/80 after decay. Decay resolves8 and introduces4 repeats. Old100M versus final500M resolves6 and introduces24. Every greedy output reaches the same64-token cap.'},
            {'conclusion': 'A general increase in literal training-data repetition or document length is not observed in the measured sample/statistics.',
             'evidence': 'Full train mean body length464->469tokens; median443->448. Fixed2048doc samples each have42 regex flags, mostly punctuation/separators; none of the first detected repeated units has length>=4. Mean repeated char4gram fraction0.0911->0.0882. These sample results do not rule out rare or semantic boilerplate.'},
            {'conclusion': 'Greedy feedback and mismatch between web document endings and short generated text are supported hypotheses, not isolated training causes.',
             'evidence': 'Train is100%web/commercial_web, only0.8505% expanded train documents have<=128body tokens. Final greedy repetition66/80 vs sampled11/240. On the same8 reproduced cases, last16 top probability mean0.6524->0.8199 and entropy1.7790->0.9703; both exhibit low EOS probability. Data amount, tokens, schedule, batch and training backend changed together.'},
            {'conclusion': 'Stored generation corruption or a gross short FP32 cache error is not supported; numerical precision can still alter individual token choices.',
             'evidence': 'The same8 cases on each old/final checkpoint reproduce all generated IDs. All16 short FP32 full/cache probes satisfy originalatol1e-5+rtol1e-4. BF16 full/cache changes argmax at1 forced position per checkpoint, BF16/FP32 full changes3 old/1 final. Preserve these differences; no all-context/backend parity or exclusion of precision effects.'},
            {'conclusion': 'Do not automatically extend to1B or call this proof that dataset quantity is the main problem.',
             'evidence': 'Expanded data is roughly90times larger and teacher-forced BPB/EOS improve, while greedy short generation remains poor. First perform a fixed-checkpoint decoder comparison; consider a controlled short-text supervision comparison with a separately gated implementation.'}],
        'limitations': ['100M vs500M changes dataset exposure, token budget, batch, schedule and training backend together; no independent data-amount causal conclusion.',
            'Fixed512-character train prefixes, 2048documents each, are a sample; semantic repetition, long-tail contamination and memorized boilerplate are not excluded.',
            'Greedy80 fixed short-prefix continuations are not chat prompts or true corpus endings. BOS/EOS packing crosses document boundaries.',
            'Three stable checkpoints describe one seed trajectory, not independent repeated training experiments.',
            'Eight precision/reproduction cases cannot certify all1024-context or all decoding paths. BF16 vsFP32 is a diagnostic, not an altered acceptance gate.',
            'No test split evaluation, blind human scoring, Chat, data changes or1B training performed.'],
        'next_experiment': {
            'priority': 'First compare decoder behavior on the same checkpoint; consider matched short-text ending supervision only after this low-cost comparison, before an automatic1B extension',
            'design': 'Fork the same stable500M checkpoint twice; keep32batch/1024context/FP32+BF16/Flash/compile/fusedAdamW and identical frozen WSD branch schedule. A consumes original train; B uses a separately manifested train-only short coherent document mixture retaining true endings. Include20% short documents with body<=128tokens; no sentence truncation treated as EOS. Fix total input tokens to25M per arm; RNGseed42. Establish config/protocol and restore gates before launch.',
            'controls': 'Same starting optimizer/RNG/sampler policy and input-token budget; record supervised body/EOS tokens and bytes, no oversampling dev/test. EOS mixture effect remains a combined distribution intervention, not isolated EOS-weight causality.',
            'decoding_control': 'First compare unchanged decoding vs repetition penalty1.1 on the identical decay500M checkpoint, same80dev cases/64token ceiling and existing3sampling seeds (42/43/44,temp0.8,top_p0.9). At most640 outputs, GPU15minutes. Record EOS/repetition/Unicode/role/empty and sample20 cases for blinded human review; no blind reviewer is assumed available. Report all cases, do not replace frozen outputs. Completion is the paired report; fewer regex loops alone is not proof of better text.',
            'budget': 'Two25M-input-token branches, GPU total20minutes including generation/dev scoring; measured time cap, stop if gate fails; no launch in current scope.',
            'completion': 'Report paired repetition/EOS transitions, full dev BPB and doc-paired CI, original Unicode/role/empty flags, unchanged parent/full-state resume checks and all failures. A next-stage comparative adoption requires fewer greedy repeats without worsening sampling/Unicode/role flags and BPB degradation CI upper bound<=0.01; otherwise reject or explicitly revise hypothesis before more training. These added comparison conditions do not relax the existing frozen Base quality targets. A train-mixture branch requires a new separately implemented loader/trainer with exact resume/finite gates; preserve all frozen training code.',
            'authorization': 'Proposal only; current investigation stops after report/commit, no training launched.'}}
    write_json(args.output, report)
    print(json.dumps({'status': report['status'], 'checks': len(checks), 'trajectory': trajectory_summary, 'ending_probes': eos_probes}), flush=True)


if __name__ == '__main__':
    main()
