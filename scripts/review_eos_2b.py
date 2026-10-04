"""Summarize the bounded EOS diagnosis without further GPU work; use uv."""
import json
import math
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, write_json, now, sha256
from jmicro.repetition_diagnosis import repetition_details
from jmicro.tokenizer import Tokenizer


def main():
    plan = read_json(ROOT / 'reports/phase6/eos_2b_plan.json')
    run = ROOT / plan['destination']
    job, result = read_json(run / 'job.json'), read_json(run / 'result.json')
    assert job['status'] == 'complete' and result['status'] == 'completed_bounded_eos_diagnosis'
    assert result['plan'] == plan and job['plan_sha256'] == sha256(ROOT / 'reports/phase6/eos_2b_plan.json')
    assert result['training_updates'] == 0 and result['model_state_unchanged'] and result['checkpoint_stat_unchanged']
    assert result['elapsed_seconds'] <= plan['inference_budget_seconds']
    new = result['ending_probes']
    old = read_json(ROOT / 'reports/phase6/repetition-diagnosis-20261003/gpu-decay500M.json')['ending_probes']
    assert [r['doc_id'] for r in new['endings']] == [r['doc_id'] for r in old['endings']]
    assert [r['id'] for r in new['prefixes']] == [r['id'] for r in old['prefixes']]
    full = read_json(ROOT / 'reports/phase6/base-2b-10bdata-20261004/evaluation-2B/full-dev.json')['body']
    previous_full = read_json(ROOT / 'reports/phase6/repetition-diagnosis-20261003/cpu.json')['full_dev_eos']['decay500M']
    config = read_json(ROOT / 'configs/phase6/base_2b_10b_data.json')
    train_manifest_path = Path(config['shards']) / 'manifest.json'
    assert sha256(train_manifest_path) == config['shard_manifest_sha256']
    train = read_json(train_manifest_path)['splits']['train']
    suites = ET.parse(run / 'tests.xml').getroot().iter('testsuite')
    tests = {key: 0 for key in ('tests','failures','errors','skipped')}
    for suite in suites:
        for key in tests:
            tests[key] += int(suite.attrib.get(key, 0))
    assert tests == {'tests': 3, 'failures': 0, 'errors': 0, 'skipped': 0}
    tok = Tokenizer(ROOT / 'artifacts/phase2/4096/tokenizer.model')
    comparison = {}
    details = []
    for penalty in plan['penalties']:
        rows = [r for r in result['outputs'] if r['penalty'] == penalty]
        assert [r['id'] for r in rows] == plan['selected_ids']
        assert all(r['eos'] == (r['generated_ids'][-1] == 3) for r in rows)
        if penalty == 1:
            assert all(r['first64_match_original'] for r in rows)
        repeat64 = 0
        invalid64 = 0
        for row in rows:
            raw = tok.decode_bytes(row['generated_ids'][:64])
            try:
                text = raw.decode('utf-8')
            except UnicodeDecodeError:
                invalid64 += 1
                text = raw.decode('utf-8', errors='replace')
            repeat64 += repetition_details(text)['repetition']
            details.append({key: row[key] for key in ('id', 'category', 'penalty', 'eos_step', 'stop_reason', 'repetition', 'valid_utf8', 'token_4gram_repeat_fraction')}
                           | {'generated_tokens': len(row['generated_ids']), 'first64_repetition': repetition_details(text)['repetition'],
                              'max_raw_eos_probability': max(s['eos_probability'] for s in row['trace']),
                              'minimum_raw_eos_rank': min(s['eos_rank'] for s in row['trace']),
                              'last_raw_eos_rank': row['trace'][-1]['eos_rank'],
                              'first64_match_original': row['first64_match_original']})
        comparison[str(penalty)] = {'cases': len(rows), 'eos_by_tokens': {str(n): sum(r['eos_step'] is not None and r['eos_step'] <= n for r in rows) for n in (64,128,256,512)},
            'repetition_first64': int(repeat64), 'repetition_full_output': sum(r['repetition'] for r in rows),
            'invalid_utf8_first64': invalid64, 'invalid_utf8_full_output': sum(not r['valid_utf8'] for r in rows),
            'role_token_outputs': sum(any(token in (4,5,6,7) for token in r['generated_ids']) for r in rows),
            'mean_generated_tokens': sum(len(r['generated_ids']) for r in rows) / len(rows)}
    review = {'status': 'completed_bounded_eos_investigation', 'completed_at': now(),
        'checkpoint': plan['checkpoint'], 'training_updates': 0, 'GPU_inference_seconds': result['elapsed_seconds'],
        'raw_run': str(run), 'job_identity': {key: job[key] for key in ('pid','boot_id','start_ticks')},
        'raw_evidence': {name: {'path': str(run / name), 'sha256': sha256(run / name)} for name in ('job.json','result.json','endings.json','continuations.json','run.log')},
        'plan_sha256': sha256(ROOT / 'reports/phase6/eos_2b_plan.json'),
        'teacher_endings': {'same_documents': 256, 'old500M_eos_argmax': old['ending_eos_argmax'], 'new2B_eos_argmax': new['ending_eos_argmax'],
            'old500M_mean_eos_probability': old['ending_eos_probability']['mean'], 'new2B_mean_eos_probability': new['ending_eos_probability']['mean'],
            'old500M_median_eos_rank': old['ending_eos_rank']['p50'], 'new2B_median_eos_rank': new['ending_eos_rank']['p50'],
            'old500M_prefix_mean_eos_probability': old['prefix_eos_probability']['mean'], 'new2B_prefix_mean_eos_probability': new['prefix_eos_probability']['mean'],
            'new2B_prefix_eos_argmax': new['prefix_eos_argmax']},
        'full_dev_eos_reused': {'documents': full['documents'], 'old500M_mean_eos_nll': previous_full['mean_eos_nll'],
            'new2B_mean_eos_nll': full['eos_nll'] / full['documents'],
            'old500M_geometric_eos_probability': previous_full['geometric_mean_eos_probability'],
            'new2B_geometric_eos_probability': math.exp(-full['eos_nll'] / full['documents']),
            'method': 'Existing full heldout EOS loss, not rescored. Geometric probability differs from256-ending arithmetic mean.'},
        'decoder_comparison_20_dev_cases': comparison, 'case_details': details,
        'precision_eight_true_endings': {'argmax_differences': sum(not r['argmax_same'] for r in result['precision']),
            'eos_argmax_bf16': sum(r['bf16']['eos_is_argmax'] for r in result['precision']),
            'eos_argmax_fp32': sum(r['fp32']['eos_is_argmax'] for r in result['precision']),
            'scope': 'Only8 fixed true endings; does not exclude all precision effects.'},
        'training_eos_contract': {'eos_id': 3, 'stop_ids': [3], 'eos_suppressed': False,
            'construction': '[2,*body,3] in large_corpus.tokenize_batch', 'loss_mask': 'BlockSampler masks only target2/BOS; EOS is supervised',
            'train_documents_from_existing_manifest': train['documents'], 'train_stream_tokens': train['tokens'],
            'mean_body_tokens_per_document': train['tokens'] / train['documents'] - 2,
            'eos_fraction_in_prepared_stream': train['documents'] / train['tokens'],
            'scope': 'Manifest aggregate plus unchanged source and previously accepted builder/loader evidence; not an exact count of consumed EOS teachers.'},
        'tests': {**tests,
            'xml_path': str(run / 'tests.xml'), 'xml_sha256': sha256(run / 'tests.xml')},
        'findings': [
            'EOS3 is present in the unchanged training target construction, is not masked or suppressed, and actually stops generation when selected. No stop-controller defect was found.',
            'Matched true-ending EOS argmax improves35/256 to46/256, but210/256 true endings still prefer a continuation token. Existing full-dev EOS NLL also improves.',
            'Raw greedy reproduces the saved first64 IDs for all20 cases, yet all20 repeat and fail to stop by512. The64-token cap alone does not explain failure.',
            'Penalty1.1 lowers first64 repetitions17/20 to6/20 and yields5 late EOS stops at435-491 tokens; all20 full outputs still repeat. It is not a sufficient stopping solution.',
            'The immediate mechanism is continuation tokens outranking EOS on generated trajectories, with repetitive feedback. Short-completion versus web-document training is a hypothesis; neither data size alone nor any single training factor is proven causal.'
        ],
        'next_comparison_proposal_not_started': {
            'scope': 'Two25M-token arms including decay from the same2B checkpoint in new explicit experiment forks;50M aggregate comparison budget. Preserve the completed2B weights/run.',
            'control': 'Existing web mixture, same optimizer/schedule settings as the treatment fork.',
            'treatment': '20percent of input tokens from original complete32-128-body-token train documents, remainder existing web. No EOS loss reweighting, EOS logit bias or forced termination.',
            'data': 'Use prepared12.23B train only; extract a bounded short-document pool of at least5M unique input tokens. Do not label arbitrary truncated fragments as completed documents. Keep dev/test/evaluation separate.',
            'comparison': 'Both arms: same80 greedy64 dev cases and same256 heldout scoring; reuse saved2B baseline. Track EOS, repetition, empty/roles/UTF8 and body BPB/EOS NLL. Full existing dev/400 generation only for a promising candidate.',
            'improvement_condition': 'At least8 additional EOS stops among80 at64 tokens, repetition no worse than control, no new empty/role/Unicode failures, body BPB degradation <=1percent. This is an intermediate improvement gate; original Base/Chat acceptance is unchanged.',
            'completion': 'One paired comparison, no automatic mixture/penalty sweep; report actual consumed tokens and runtime. If the gate fails, identify the next measured hypothesis before larger training.',
            'growth_after_improvement': 'Next scaling target proposed5B consumed input tokens using the already prepared12.23B pool. Freeze the fork/resume/decay budget separately after EOS comparison; no new corpus acquisition is necessary for that target.',
            'status': 'proposed_not_started'
        },
        'limits': ['Fixed64 benchmark unchanged;512 comparison is diagnostic.',
            'Penalty1.1 uses generated ordinary token history only; EOS neither boosted nor forced.',
            '20 dev cases do not establish overall quality or causal effect of data versus training quantity.',
            'New full train index/audit and old GPU runs were not repeated.'],
        'initial_setup_failure': 'CRLF-normalized hash was mistakenly compared as raw hash; fixed using existing implementation_hashes. Initial failed job preserved; no GPU generation occurred in that attempt.'}
    write_json(ROOT / 'reports/phase6/eos_2b_review.json', review)
    print(json.dumps({key: review[key] for key in ('GPU_inference_seconds', 'teacher_endings', 'full_dev_eos_reused', 'decoder_comparison_20_dev_cases', 'precision_eight_true_endings')}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
