"""Descriptive all80 failure pairing; immutable ratings, no model execution."""
from collections import Counter
import json
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, read_json, sha256

PHASE = ROOT / 'reports/phase6'
NOTES = PHASE / 'base_residual_failure_pair_notes.json'
OUTPUT = PHASE / 'base_residual_failure_pair_diagnostic.json'
STATES = {'maintained', 'violated', 'unresolved'}


def checked(reference):
    path = Path(reference['path'])
    if sha256(path) != reference['sha256']:
        raise ValueError('Immutable input differs: ' + str(path))
    return read_json(path)


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def main():
    start = time.perf_counter()
    if OUTPUT.exists():
        raise ValueError('Preserve completed descriptive diagnostic')
    policy = read_json(ROOT / 'configs/phase6/base_parallel_residual_review.json')
    review = read_json(PHASE / 'base_parallel_residual_comparison_review.json')
    completion = read_json(PHASE / 'base_parallel_residual_comparison_completion.json')
    if (not review['all160_individually_read'] or completion['eligible_for_final_Base_validation']
            or not completion['fixed_parallel_residual_condition_closed']
            or any(completion[k] for k in ('Base_complete', 'Base_adopted', 'Chat_started', 'quantization_started'))):
        raise ValueError('Actual closed failed Base-only comparison required')
    strong_result_path = Path(policy['references']['strong_result']['path'])
    strong_result = checked(policy['references']['strong_result'])
    strong_raw_path = strong_result_path.parent / 'evaluation/source_order/evaluation/generation.json'
    strong_notes_path = Path(policy['references']['strong_notes']['path'])
    strong_notes = checked(policy['references']['strong_notes'])
    seq_raw_path = ROOT / 'reports/phase6/base-parallel-residual-comparison-20261007/evaluation/sequential/evaluation/generation.json'
    seq_notes_path = PHASE / 'base_parallel_residual_sequential_notes.json'
    seq_notes = read_json(seq_notes_path)
    inputs = dict(strong_raw=ref(strong_raw_path), strong_notes=ref(strong_notes_path),
                  sequential_raw=ref(seq_raw_path), sequential_notes=ref(seq_notes_path))
    if (inputs['strong_raw']['sha256'] != policy['strong_summary']['generation_sha256']
            or inputs['sequential_notes']['sha256'] != review['notes_sha256']['sequential']):
        raise ValueError('Actual fixed all80 raw/rating lineage required')
    source_rows = dict(strong=read_json(strong_raw_path)['outputs'], sequential=read_json(seq_raw_path)['outputs'])
    source_notes = dict(strong=strong_notes, sequential=seq_notes)
    ids = [r['id'] for r in source_rows['strong']]
    if len(ids) != 80 or len(set(ids)) != 80 or ids != [r['id'] for r in source_rows['sequential']]:
        raise ValueError('Exactly aligned fixed DEV80 required')
    for arm in source_rows:
        if source_notes[arm]['generation_sha256'] != inputs[arm + '_raw']['sha256']:
            raise ValueError('Raw-bound immutable scores required')
        scores = source_notes[arm]['notes']
        if len(scores) != 80 or {n[0] for n in scores} != set(ids):
            raise ValueError('Every existing individual score required')
    annotations = read_json(NOTES)
    if (annotations['inputs'] != inputs or annotations['independent_human_blind'] is not False
            or annotations['classification_prespecified_before_outputs_read'] is not False
            or not annotations['reviewer']):
        raise ValueError('Actual raw/notes provenance and posthoc nonblind disclosure required')
    notes = annotations['notes']
    if len(notes) != 80 or [n[0] for n in notes] != ids:
        raise ValueError('Individually classified aligned all80 required')
    paired = []
    for index, note in enumerate(notes):
        if len(note) != 7:
            raise ValueError('id and two loop/premise/rationale triplets required')
        row = dict(id=note[0], prefix=source_rows['strong'][index]['prefix'], category=source_rows['strong'][index]['category'])
        for arm, offset in (('strong', 1), ('sequential', 4)):
            raw = source_rows[arm][index]
            if raw['prefix'] != row['prefix'] or raw['split'] != 'dev' or raw['decoding'] != 'greedy' or raw['seed'] != 42 or not raw['suppressed']:
                raise ValueError('Same raw fixed protocol required')
            loop, premise, rationale = note[offset:offset + 3]
            if type(loop) is not bool or premise not in STATES or not isinstance(rationale, str) or len(rationale.strip()) < 12:
                raise ValueError('Explicit individual descriptive annotation required')
            score = next(n for n in source_notes[arm]['notes'] if n[0] == note[0])
            row[arm] = dict(text=raw['text'], stop_reason=raw['stop_reason'],
                            automatic_repetition=raw['repetition'], nonprogressive_repetition=loop,
                            premise= premise, diagnostic_rationale=rationale,
                            original_scores=dict(grammar=score[1], relevance=score[2], coherence=score[3], completion=score[4]),
                            original_rationale=score[5], original_scores_changed=False)
        paired.append(row)
    summaries = {}
    for arm in source_rows:
        rows = [r[arm] for r in paired]
        cells = Counter((r['nonprogressive_repetition'], r['automatic_repetition']) for r in rows)
        summaries[arm] = dict(outputs=80,
            eos=sum(r['stop_reason'] == 'stop_id' for r in rows),
            grammar2=sum(r['original_scores']['grammar'] == 2 for r in rows),
            coherence2=sum(r['original_scores']['coherence'] == 2 for r in rows),
            appropriate=sum(r['original_scores']['completion'] for r in rows),
            premise=dict(Counter(r['premise'] for r in rows)),
            nonprogressive_repetition=sum(r['nonprogressive_repetition'] for r in rows),
            automatic_repetition=sum(r['automatic_repetition'] for r in rows),
            descriptive_manual_auto_table=[dict(nonprogressive_repetition=m, automatic_repetition=a, count=cells[m, a]) for m in (False, True) for a in (False, True)])
        expected = review['summaries']['strong_staged' if arm == 'strong' else arm]
        if (summaries[arm]['eos'], summaries[arm]['grammar2'], summaries[arm]['coherence2'], summaries[arm]['appropriate'], summaries[arm]['automatic_repetition']) != (
                expected['rates']['eos'], expected['grammar2'], expected['coherent'], expected['appropriate'], expected['rates']['repetition']):
            raise ValueError('Immutable previous quality summary changed')
    # Descriptive comparisons only: these models differ in initialization,
    # training history, source order and schedule. No causal effect is estimated.
    elapsed = time.perf_counter() - start
    if elapsed > 30:
        raise ValueError('CPU-only30-second diagnostic budget exceeded')
    result = dict(status='all80_paired_existing_generation_failures_classified', created_at=now(),
        inputs=inputs, annotation=ref(NOTES), source=ref(Path(__file__)), CPU_seconds=elapsed,
        GPU_seconds=0, generated_tokens=0, scientific_teacher_tokens=0, optimizer_updates=0,
        summaries=summaries, paired=paired, classification_definitions=annotations['definitions'],
        original_scores_changed=False, acceptance_criteria_changed=False, additional_model_evaluation=False,
        independent_human_blind=False, classification_prespecified_before_outputs_read=False,
        causal_effect_estimated=False,
        model_history=dict(strong=dict(checkpoint=strong_result['checkpoints']['source_order']['checkpoint'],
                                      tokens=strong_result['checkpoints']['source_order']['tokens'],
                                      binding=strong_result['checkpoints']['source_order']['binding']),
                           sequential=dict(original_gold=2000000000, fresh_initialization=True, training_seed=42)),
        limitations='Posthoc nonblind descriptive labels from already-reused DEV. Manual repetition is not an independent ground-truth detector benchmark. Maintained does not mean overall coherent, and unresolved does not assert a literal contradiction. Training histories differ, so this is not a causal architecture or quantity comparison. No score/gate replacement.',
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        protected_test_scored=False)
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(dict(status=result['status'], CPU_seconds=elapsed, summaries=summaries), ensure_ascii=False))


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
