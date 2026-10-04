"""Bounded EOS diagnosis of the completed 2B checkpoint; execute through uv."""
import argparse
from collections import Counter
import json
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from investigate_repetition import (
    ROOT, Tokenizer, JMicroModel, Shard, SUPPRESS_IDS, torch, np,
    sdpa_kernel, SDPBackend, ending_probes, logit_stats, repetition_details,
    repeated_ngram_fraction, gpu_lock, seed_all, identity, read_json, write_json,
    sha256, now, equal_state,
)
from jmicro.training import implementation_hashes


def penalize(scores, history, penalty):
    """Sign-aware penalty on previously emitted ordinary tokens; EOS exempt."""
    scores = scores.float().clone()
    if penalty < 1:
        raise ValueError('Penalty must be >= 1')
    if penalty != 1 and history:
        ids = sorted({token for token in history if token >= 8})
        if ids:
            values = scores[ids]
            scores[ids] = torch.where(values < 0, values * penalty, values / penalty)
    scores[list(SUPPRESS_IDS)] = -torch.inf
    return scores


@torch.inference_mode()
def continuation(model, tok, case, penalty, deadline, maximum):
    ids, trace, cache = [], [], None
    current = torch.tensor([case['prompt_ids']], device='cuda')
    assert len(case['prompt_ids']) + maximum <= 1024
    for step in range(maximum):
        if time.monotonic() >= deadline:
            raise TimeoutError('Predeclared 600-second inference budget exhausted')
        with torch.autocast('cuda', dtype=torch.bfloat16):
            result = model(current, cache=cache, use_cache=True)
        cache = result.cache
        raw = result.logits[0, -1].float()
        stats = logit_stats(raw)
        scores = penalize(raw, ids, penalty)
        token = int(scores.argmax())
        trace.append({**stats, 'step': step + 1, 'selected_id': token,
                      'decoder_eos_rank': int((scores > scores[3]).sum()) + 1,
                      'eos_margin_to_selected': float(scores[3] - scores[token])})
        ids.append(token)
        if token == 3:
            break
        current = torch.tensor([[token]], device='cuda')
    raw_bytes = tok.decode_bytes(ids)
    try:
        text, valid = raw_bytes.decode('utf-8'), True
    except UnicodeDecodeError:
        text, valid = raw_bytes.decode('utf-8', errors='replace'), False
    return {'id': case['id'], 'category': case['category'], 'prefix': case['prefix'],
            'penalty': penalty, 'max_new_tokens': maximum, 'generated_ids': ids,
            'text': text, 'valid_utf8': valid, 'eos': ids[-1] == 3,
            'eos_step': len(ids) if ids[-1] == 3 else None,
            'stop_reason': 'stop_id' if ids[-1] == 3 else 'max_tokens',
            **repetition_details(text), 'trace': trace,
            'token_4gram_repeat_fraction': repeated_ngram_fraction(ids)}


@torch.inference_mode()
def precision_endings(model, shard, deadline):
    rows = []
    for doc in shard.index[:8]:
        if time.monotonic() >= deadline:
            raise TimeoutError('Inference budget exhausted')
        start, length = doc['offset'], doc['body_tokens']
        tokens = shard.tokens[max(start, start + length + 1 - 1024):start + length + 1].astype(np.int64)
        x = torch.tensor(tokens[None], device='cuda')
        with torch.autocast('cuda', dtype=torch.bfloat16):
            bf16 = model(x).logits[0, -1].float()
        fp32 = model(x).logits[0, -1].float()
        rows.append({'doc_id': doc['doc_id'], 'bf16': logit_stats(bf16),
                     'fp32': logit_stats(fp32), 'max_abs_delta': float((bf16 - fp32).abs().max()),
                     'argmax_same': int(bf16.argmax()) == int(fp32.argmax())})
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, default=ROOT / 'reports/phase6/eos_2b_plan.json')
    args = parser.parse_args()
    plan = read_json(args.plan)
    destination = ROOT / plan['destination']
    destination.mkdir(parents=True, exist_ok=True)
    if (destination / 'job.json').exists():
        raise RuntimeError('Existing diagnosis: inspect identity/results before any new run')
    job = {'status': 'running', **identity(), 'started_at': now(),
           'plan_sha256': sha256(args.plan), 'source_sha256': sha256(Path(__file__)),
           'helper_sha256': sha256(ROOT / 'scripts/investigate_repetition.py'),
           'training_updates': 0, 'stage': 'setup'}
    write_json(destination / 'job.json', job)
    started = time.monotonic()
    deadline = started + plan['inference_budget_seconds']
    try:
        seed_all(42)
        torch.set_num_threads(2)
        config = read_json(ROOT / 'configs/phase6/base_2b_10b_data.json')
        # Match the existing runner: these four hashes normalize CRLF only.
        implementation = implementation_hashes()
        for source, expected in config['source_sha256'].items():
            actual = implementation[source] if source in implementation else sha256(ROOT / source)
            assert actual == expected, source
        tok = Tokenizer(ROOT / config['tokenizer'])
        assert sha256(tok.path) == config['tokenizer_sha256']
        assert 3 not in SUPPRESS_IDS
        cases = [json.loads(line) for line in (ROOT / 'eval/base.jsonl').read_text(encoding='utf-8').splitlines()]
        cases = [case for case in cases if case['split'] == 'dev']
        assert len(cases) == 80 and sha256(ROOT / 'eval/base.jsonl') == plan['suite_sha256']
        for case in cases:
            case['prompt_ids'] = [2, *tok.encode(case['prefix'])]
        selected = [case for case in cases if case['id'] in plan['selected_ids']]
        assert [case['id'] for case in selected] == plan['selected_ids']
        assert len(selected) == 20 and set(Counter(c['category'] for c in selected).values()) == {2}
        run = ROOT / 'reports/phase6/base-2b-10bdata-20261004'
        existing = read_json(run / 'evaluation-2B/generation.json')['generation']['outputs']
        path = Path(plan['checkpoint']['path'])
        assert sha256(path) == plan['checkpoint']['sha256']
        checkpoint_stat = (path.stat().st_size, path.stat().st_mtime_ns)
        with gpu_lock('cuda'), sdpa_kernel([SDPBackend.MATH]):
            state = torch.load(path, map_location='cpu', weights_only=False)
            assert state['tokens'] == 2000027648
            assert state['implementation_sha256'] == implementation
            model = JMicroModel(state['model_config']).to('cuda')
            model.load_state_dict(state['model'], strict=True)
            model.eval()
            before = {key: value.clone() for key, value in model.state_dict().items()}
            # Only the unchanged old dev is loaded. No full new training index scan.
            dev = Shard(Path('/home/aihub_ubuntu/jmicro-data/phase6/expanded-v2/shards'), 'dev')
            endings = ending_probes(model, dev, cases, 256, deadline)
            precision = precision_endings(model, dev, deadline)
            write_json(destination / 'endings.json', {'ending_probes': endings, 'precision': precision})
            print(json.dumps({'stage': 'endings', 'eos_argmax': endings['ending_eos_argmax'],
                              'elapsed_seconds': time.monotonic() - started}), flush=True)
            outputs = []
            for penalty in plan['penalties']:
                for case in selected:
                    row = continuation(model, tok, case, penalty, deadline, plan['max_new_tokens'])
                    baseline = next(r for r in existing if r['id'] == case['id'] and r['decoding'] == 'greedy' and r['suppressed'])
                    row['first64_match_original'] = row['generated_ids'][:64] == baseline['generated_ids']
                    if penalty == 1:
                        assert row['first64_match_original'], case['id']
                    outputs.append(row)
                    write_json(destination / 'continuations.json', {'outputs': outputs})
                    job.update(stage='generation', completed_cases=len(outputs), elapsed_seconds=time.monotonic() - started)
                    write_json(destination / 'job.json', job)
                    print(json.dumps({'penalty': penalty, 'id': case['id'], 'eos_step': row['eos_step'],
                                      'repeat': row['repetition'], 'elapsed_seconds': job['elapsed_seconds']}), flush=True)
            unchanged = equal_state(before, model.state_dict())
            assert unchanged and checkpoint_stat == (path.stat().st_size, path.stat().st_mtime_ns)
        result = {'status': 'completed_bounded_eos_diagnosis', 'training_updates': 0,
                  'elapsed_seconds': time.monotonic() - started, 'model_state_unchanged': unchanged,
                  'checkpoint_stat_unchanged': True, 'plan': plan,
                  'ending_probes': endings, 'precision': precision, 'outputs': outputs}
        assert result['elapsed_seconds'] <= plan['inference_budget_seconds']
        write_json(destination / 'result.json', result)
        job.update(status='complete', stage='complete', completed_at=now(), elapsed_seconds=result['elapsed_seconds'])
    except Exception as exc:
        job.update(status='failed', error=f'{type(exc).__name__}: {exc}', finished_at=now())
        raise
    finally:
        write_json(destination / 'job.json', job)


if __name__ == '__main__':
    main()
