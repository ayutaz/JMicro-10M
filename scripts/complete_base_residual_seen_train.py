"""Close exited six-case inference and content diagnosis without Base adoption."""
import json
import math
from pathlib import Path
import sys
import time
import urllib.request

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import alive
from run_base_residual_seen_train import RUN, CONFIG, OUTPUT, checked, ref

PHASE = ROOT / 'reports/phase6'
NOTES = PHASE / 'base_residual_seen_train_content_notes.json'
COMPLETION = PHASE / 'base_residual_seen_train_diagnostic_completion.json'


def summarize_case(row, unit, note):
    teacher, free = row['teacher'], row['free']
    gold = unit['continuation_gold_ids']
    if teacher['fed_ids'] != gold[:64] or len(teacher['steps']) != len(teacher['fed_ids']):
        raise ValueError('Only actual original gold history; no artificial EOS')
    for path in (teacher, free):
        for index, step in enumerate(path['steps']):
            target = gold[index] if index < len(gold) else None
            if step['index'] != index or step['original_gold_id'] != target or step['actual_gold_EOS'] != (target == 3):
                raise ValueError('Aligned original target positions required')
            if target is not None and not math.isfinite(step['original_gold_nll']):
                raise ValueError('Finite original-target likelihood required')
    common = min(len(teacher['steps']), len(free['steps']))
    if common <= 0:
        raise ValueError('Comparable reference positions required')
    tnll = sum(s['original_gold_nll'] for s in teacher['steps'][:common])
    fnll = sum(s['original_gold_nll'] for s in free['steps'][:common])
    first = next((i for i,(x,y) in enumerate(zip(free['fed_ids'], gold)) if x != y), None)
    eos = [s for s in teacher['steps'] if s['actual_gold_EOS']]
    return dict(id=row['id'], source=row['source'], paired_reference_positions=common,
        teacher_NLL_on_paired_positions=tnll, free_NLL_on_same_original_positions=fnll,
        teacher_mean_NLL=tnll/common, free_mean_NLL=fnll/common,
        teacher_argmax_matches=sum(s['greedy_id'] == s['original_gold_id'] for s in teacher['steps']),
        teacher_targets=len(teacher['steps']), first_token_divergence_index=first,
        divergence_is_not_in_itself_a_quality_failure=True,
        teacher_actual_gold_EOS=None if not eos else dict(probability=eos[0]['EOS_probability'], rank=eos[0]['original_gold_rank']),
        actual_EOS_in_reference_interval=bool(eos), free_stop_reason=free['stop_reason'],
        free_automatic_repetition=free['automatic_repetition'], free_content=dict(grammar=note[1], relevance=note[2], coherence=note[3], completion=note[4], rationale=note[5]))


def main():
    start = time.perf_counter()
    if COMPLETION.exists():
        raise ValueError('Preserve completed seen-TRAIN diagnostic')
    c, result, job = read_json(CONFIG), read_json(OUTPUT), read_json(RUN / 'job.json')
    if (alive(job) or job['status'] != 'complete' or not job['cumulative_GPU_ledger_closed']
            or result['actual_identity'] != {k:job[k] for k in ('pid','boot_id','start_ticks')}
            or result['config'] != ref(CONFIG) or not all(result['checks'].values())
            or not 0 < result['GPU_seconds'] == job['GPU_seconds'] <= c['GPU_budget_seconds']
            or result['scientific_teacher_tokens'] or result['optimizer_updates']):
        raise ValueError('Actual exited bounded read-only six-case GPU result required')
    prepared = checked(c['preparation'])
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name) != digest:
            raise ValueError('Frozen science source changed: '+name)
    content = read_json(NOTES)
    if (content['result_sha256'] != sha256(OUTPUT) or content['independent_human_blind'] is not False
            or content['all6_free_generated_texts_individually_read'] is not True or not content['reviewer']):
        raise ValueError('Actual all6 individual content notes required')
    rows, notes = result['results'], content['notes']
    if (len(rows) != 6 or len(notes) != 6 or [r['id'] for r in rows] != [u['id'] for u in prepared['selected']]
            or [r['id'] for r in rows] != [n[0] for n in notes]):
        raise ValueError('All six fixed units required')
    codec = Tokenizer(ROOT / read_json(ROOT/'configs/phase6/base_parallel_residual_comparison.json')['tokenizer'])
    summaries = []
    for row,unit,note in zip(rows,prepared['selected'],notes,strict=True):
        if len(note) != 6 or not all(type(n) is int and n in (0,1,2) for n in note[1:4]) or type(note[4]) is not int or note[4] not in (0,1) or len(note[5]) < 12:
            raise ValueError('Individual unchanged grammar/relevance/coherence/completion rubric required')
        if note[4] and (row['free']['stop_reason'] != 'stop_id' or note[2] < 1 or note[3] < 1):
            raise ValueError('Appropriate completion requires real stop and some coherent relevance')
        if row['prefix'] != unit['prefix'] or row['teacher']['steps'][0] != row['free']['steps'][0]:
            raise ValueError('Exact same first original prefix prediction required')
        for path in (row['teacher'],row['free']):
            raw = codec.decode_bytes(path['fed_ids'])
            try:
                text,valid = raw.decode('utf-8'),True
            except UnicodeDecodeError:
                text,valid = raw.decode('utf-8',errors='replace'),False
            if raw.hex() != path['raw_UTF8_bytes_hex'] or text != path['text'] or valid != path['valid_UTF8']:
                raise ValueError('Actual raw IDs/bytes/text required')
        summaries.append(summarize_case(row,unit,note))
    launcher = PHASE / 'base-residual-seen-train-launcher-20261008/result.json'
    launched = read_json(launcher)
    if launched['status'] != 'complete' or launched['exit_code'] != 0:
        raise ValueError('Actual durable worker completion required')
    ui = read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:
        model = json.load(response)
    if not alive(ui) or model['busy'] or model['training_tokens'] != 10000007168 or model['checkpoint_sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290':
        raise ValueError('Original actual idle10B UI restoration required')
    count = sum(s['paired_reference_positions'] for s in summaries)
    aggregated = dict(paired_original_positions=count,
        teacher_mean_NLL=sum(s['teacher_NLL_on_paired_positions'] for s in summaries)/count,
        free_mean_NLL_on_same_original_positions=sum(s['free_NLL_on_same_original_positions'] for s in summaries)/count,
        teacher_argmax_accuracy=sum(s['teacher_argmax_matches'] for s in summaries)/sum(s['teacher_targets'] for s in summaries),
        teacher_target_count=result['teacher_forced_scored_targets'], free_generated_tokens=result['free_generated_tokens'],
        free_EOS=sum(r['free']['stop_reason'] == 'stop_id' for r in rows),
        free_grammar2=sum(n[1] == 2 for n in notes), free_coherence2=sum(n[3] == 2 for n in notes),
        free_appropriate_completion=sum(n[4] for n in notes), free_automatic_repetition=sum(r['free']['automatic_repetition'] for r in rows),
        true_gold_EOS_positions_scored=sum(s['actual_EOS_in_reference_interval'] for s in summaries))
    atomic_json(COMPLETION, dict(status='exited_all6_teacher_free_diagnostic_and_content_review_complete', created_at=now(),
        result=ref(OUTPUT), config=ref(CONFIG), notes=ref(NOTES), reviewer_source=ref(Path(__file__)),
        actual_identity=result['actual_identity'], actual_process_absent_verified=True, cumulative_GPU_ledger_closed=True,
        GPU_seconds=result['GPU_seconds'], GPU_cap_seconds=180, additional_training_tokens=0, optimizer_updates=0,
        all6_generated_texts_individually_read=True, independent_human_blind=False,
        aggregated=aggregated, cases=summaries, source_preparation=c['preparation'],
        UI_restored=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')}, actual_alive=True, model=model),
        limitations='Six previously exposed units, one model and nonblind reused TRAIN content; not heldout quality or repeated memorization proof. Gold/free NLL compare the same original targets at common positions only. Natural alternative completions may diverge from that reference without being erroneous. No artificial EOS; unavailable goldEOS is null. Neither source ordering nor data quantity is causally tested.',
        original80_scores_changed=False, quality_criteria_changed=False, Base_complete=False, Base_adopted=False,
        Chat_started=False, quantization_started=False, protected_test_scored=False, CPU_seconds=time.perf_counter()-start))
    print(json.dumps(dict(aggregated=aggregated,cases=[dict(id=s['id'], teacher_gold_EOS=s['teacher_actual_gold_EOS']) for s in summaries]),ensure_ascii=False))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
