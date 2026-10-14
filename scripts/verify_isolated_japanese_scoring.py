"""One CPU-only adapter audit against stored diagnostic arithmetic.

No model or quality evaluation, TRAIN token opens, mixed reader, TEST or new
dataset. Reuses the saved2M TRAIN counts and known diagnostic input artifacts.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from jmicro.evaluation_choice_boundary import COUNTS, load_choices
from jmicro.isolated_japanese_scoring import CONTROLS, load_unigram, score_case
from jmicro.japanese_evaluation import encode_request
from jmicro.tokenizer import Tokenizer


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(contract, pin):
    started = time.monotonic()
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or sha(contract) != pin:
        raise ValueError('Pinned CPU-only audit required')
    c = json.loads(Path(contract).read_text())
    if (c['kind'] != 'isolated_fixed_Japanese_scoring_CPU_regression_v1'
            or c['CPU_wall_ceiling_seconds'] != 30 or c['GPU_seconds'] != 0
            or c['scientific_teachers'] != 0 or set(c['stored_sources']) != set(COUNTS)):
        raise ValueError('Fixed adapter audit scope differs')
    output = ROOT / c['output']
    if not output.resolve().is_relative_to(ROOT / 'reports/phase6') or output.exists():
        raise ValueError('Do not repeat or overwrite completed adapter evidence')
    for relative, digest in c['sources'].items():
        if sha(ROOT / relative) != digest:
            raise ValueError('Audit implementation differs: ' + relative)
    manifest = Path(c['manifest']['path'])
    unigram_path = ROOT / c['unigram']['path']
    tokenizer_path = ROOT / c['tokenizer']['path']
    reference_paths = {task: ROOT / c['stored_sources'][task]['path'] for task in COUNTS}
    allowed = {manifest, *(manifest.parent / (task + '.dev.jsonl') for task in COUNTS),
               unigram_path, tokenizer_path, *reference_paths.values(), output}
    allowed = {str(p.resolve()) for p in allowed}
    sensitive = [ROOT / 'eval', ROOT / 'artifacts', ROOT / 'reports', Path('/home/aihub_ubuntu/jmicro-data')]
    reads = []
    def audit(event, args):
        if event != 'open' or not isinstance(args[0], (str, bytes)):
            return
        path = Path(os.fsdecode(args[0])).resolve()
        if any(path.is_relative_to(root) for root in sensitive):
            if str(path) not in allowed:
                raise ValueError('Unexpected diagnostic audit read: ' + str(path))
            mode = args[1] or ''
            if any(flag in mode for flag in 'wax+'):
                if path != output.resolve():
                    raise ValueError('Preserve all existing input records')
            else:
                reads.append(str(path))
    sys.addaudithook(audit)
    unigram, prior = load_unigram(unigram_path, c['unigram']['sha256'])
    if sha(tokenizer_path) != c['tokenizer']['sha256']:
        raise ValueError('Fixed original Tokenizer differs')
    tokenizer = Tokenizer(tokenizer_path)
    if tokenizer.vocab_size != 4096:
        raise ValueError('Original4096 codec required')
    results = {}
    for task in COUNTS:
        cases, provenance = load_choices(manifest, c['manifest']['sha256'], task)
        path = reference_paths[task]
        if sha(path) != c['stored_sources'][task]['sha256']:
            raise ValueError('Stored known diagnostic source differs')
        stored = json.loads(path.read_text())
        if (stored['complete'] is not True or len(stored['rows']) != COUNTS[task]
                or stored['control'] != CONTROLS[task]):
            raise ValueError('Exact complete stored diagnostic controls required')
        choices_checked = 0
        for case, original in zip(cases, stored['rows']):
            if time.monotonic() - started > c['CPU_wall_ceiling_seconds']:
                raise TimeoutError('One-shot CPU audit budget exhausted')
            projection = {key: original.get(key, original['id']) if key == 'family' else original[key]
                          for key in ('id', 'family', 'category', 'context', 'choices', 'label')}
            if case != projection:
                raise ValueError('Original input-only diagnostic projection differs')
            if task == 'semantics' and original['split'] != 'dev':
                raise ValueError('Stored semantics must contain DEV only')
            likelihoods = []
            for i, choice in enumerate(case['choices']):
                encoded = encode_request(tokenizer, case['context'], choice, maximum=1024)
                ids = encoded['target_ids']
                if len(ids) != original['target_tokens'][i]:
                    raise ValueError('Original target tokenization or boundary differs')
                likelihoods.append(dict(log_likelihood=original['raw_log_likelihood'][i],
                                        target_ids=ids, target_tokens=len(ids)))
                choices_checked += 1
            rebuilt = score_case(case, likelihoods, task, unigram)
            fields = ['scores', 'raw_log_likelihood', 'target_tokens', 'token_normalized',
                      'train_sample_slor', 'unigram_scores', 'prediction', 'credit', 'ties',
                      'normalized_prediction', 'normalized_credit', 'unigram_prediction', 'unigram_credit']
            if task == 'jblimp':
                fields.append('raw_credit')
            if any(rebuilt[field] != original[field] for field in fields):
                raise ValueError('Saved count vector/SLOR/tie scoring arithmetic differs: ' + task + '/' + case['id'])
        results[task] = dict(cases_checked=len(cases), choices_checked=choices_checked,
                            exact_original_input_and_token_boundary_match=True,
                            exact_saved_unigram_and_all_scoring_fields_match=True,
                            input_provenance=provenance, original_source_sha256=c['stored_sources'][task]['sha256'])
    result = dict(status='isolated_diagnostic_scoring_CPU_regression_completed',
        created_at=datetime.now(timezone.utc).isoformat(), contract_sha256=pin, sources=c['sources'],
        tasks=results, total_cases=sum(r['cases_checked'] for r in results.values()),
        total_choices=sum(r['choices_checked'] for r in results.values()),
        unigram_provenance=prior, metadata_and_known_diagnostic_read_paths=sorted(set(reads)),
        CPU_wall_seconds=time.monotonic() - started, new_GPU_seconds=0, scientific_teachers=0,
        model_instantiated=False, new_model_quality_evaluations=0, TRAIN_token_stream_opened=False,
        legacy_mixed_reader_called=False, TEST_opened=False, dataset_prepared=False,
        independent_learning_completed=False, fullDEV_completed=False, Base_qualified=False, Base_adopted=False,
        next_action='Integrate adapter only into a separately frozen prospective qualified comparison/evaluation runner',
        limitations=['Known stored diagnostic arithmetic regression, not new model quality evidence.',
                    'Python open-hook observations do not constitute an OS sandbox; the explicitly named codec is also opened by SentencePiece.',
                    'Persistent native independent-seed/fullDEV/finalTEST orchestration and a qualified recipe remain pending.'])
    if result['CPU_wall_seconds'] > c['CPU_wall_ceiling_seconds']:
        raise TimeoutError('CPU budget exceeded; no completed receipt')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: result[key] for key in ('status', 'total_cases', 'total_choices',
                                                'CPU_wall_seconds', 'new_GPU_seconds')}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract', type=Path, required=True)
    parser.add_argument('--contract-sha256', required=True)
    args = parser.parse_args()
    run(args.contract, args.contract_sha256)
