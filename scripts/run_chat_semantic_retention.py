"""Conditional native Base DEV retention for unadopted original10B SFT.

Same native Base protocol, no disguised adopted-Base provenance and no TEST.
The copied greedy function differs only in filtering DEV before JSON parsing.
"""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import re
import signal
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json, isolated_evaluation, seed_all
from jmicro.tokenizer import SUPPRESS_IDS
from jmicro.shards import Shard
from phase6_performance import alive, identity
from chat_semantic_contract import RUN, LIMITS, GPU_stage, preflight, reference, require_ref
from evaluate_chat_semantic import checkpoint
import run_complete_text_comparison as native
from review_chat_base_retention import compare
from review_improved_base import validate_content

def safe_greedy80(model, tok, heartbeat, check, limit=80):
    cases = [json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text(encoding='utf-8').splitlines() if re.search(r'\"split\"\s*:\s*\"dev\"',line)]
    cases = [case for case in cases if case['split']=='dev']
    assert len(cases)==80
    cases=cases[:limit]
    rows = []
    with isolated_evaluation(model):
        for case in cases:
            ids, cache = [], None
            current = torch.tensor([[2,*tok.encode(case['prefix'])]], device='cuda')
            for _ in range(64):
                check()
                with torch.autocast('cuda', dtype=torch.bfloat16):
                    result = model(current, cache=cache, use_cache=True)
                cache = result.cache
                scores = result.logits[0,-1].clone()
                assert bool(torch.isfinite(scores).all())
                scores[list(SUPPRESS_IDS)] = -torch.inf
                token = int(scores.argmax())
                ids.append(token)
                if token == 3:
                    break
                current = torch.tensor([[token]], device='cuda')
            raw = tok.decode_bytes(ids)
            try:
                text, valid = raw.decode('utf-8'), True
            except UnicodeDecodeError:
                text, valid = raw.decode('utf-8', errors='replace'), False
            rows.append({'id':case['id'],'category':case['category'],'prefix':case['prefix'],
                'split':'dev','decoding':'greedy','suppressed':True,'seed':42,'generated_ids':ids,
                'text':text,'valid_utf8':valid,'role_leak':any(i in (4,5,6,7) for i in ids),
                'empty_response':not text.strip(),'stop_reason':'stop_id' if ids[-1]==3 else 'max_new_tokens',
                'repetition':bool(re.search(r'(.{2,}?)\1\1',text,flags=re.DOTALL))})
            if len(rows)%8==0:
                heartbeat('generation80', completed_cases=len(rows))
    return rows


def retention_assets():
    reference_path = ROOT / 'configs/phase6/amount_learning_comparison.json'
    plan = read_json(reference_path)
    assert plan['quality_criteria_unchanged'] and not plan['protected_test_used']
    assert plan['evaluation']['dev_documents'] == 256 and plan['evaluation']['fixed_dev_prefixes'] == 80
    assert plan['evaluation']['max_new_tokens'] == 64
    assert plan['suite_sha256'] == sha256(ROOT / 'eval/base.jsonl')
    assert sha256(Path(plan['dev_shards']) / 'manifest.json') == plan['dev_manifest_sha256']
    ev = plan['evaluation']
    assert sha256(ROOT / ev['config']) == ev['config_sha256']
    assert sha256(ROOT / ev['semantic_suite']) == ev['semantic_sha256']
    config = read_json(ROOT / ev['config'])
    assert sha256(Path(config['data']) / 'manifest.json') == ev['data_manifest_sha256']
    assert ev['tasks'] == ['semantics', 'jblimp', 'jcqa']
    dev = Shard(Path(plan['dev_shards']), 'dev')
    assert len(dev.index) >= 256
    return plan, dev, reference(reference_path)


def execute(c, tok):
    selection = read_json(RUN / 'selection.json')
    assert selection['config_sha256'] == c['config_sha256'] and selection['eligible_candidate'] == 'S1'
    assert selection['all_suites_passed'] and selection['prespecified_new_joint_improvement']
    plan, dev, assets = retention_assets()
    directory = RUN / 'retention'
    job_path = directory / 'job.json'
    if job_path.exists():
        previous = read_json(job_path)
        assert not alive(previous) and previous['config_sha256'] == c['config_sha256']
        if previous['status'] == 'complete':
            print('Completed native retention retained; review160 judgments')
            return
    binding = dict(config_sha256=c['config_sha256'], parent=c['parent'], reference_config=assets,
                   dev_manifest_sha256=plan['dev_manifest_sha256'], evaluation=plan['evaluation'],
                   suite_sha256=plan['suite_sha256'], dtype='bf16', backend='math',
                   selected_point='S1-t3', original_Base_is_unadopted=True,
                   protocol='original Base BOS/prefix/EOS3, raw EOT7 remains role leak', protected_TEST_used=False)
    stopped = [False]
    signal.signal(signal.SIGTERM, lambda *_: stopped.__setitem__(0, True))
    signal.signal(signal.SIGINT, lambda *_: stopped.__setitem__(0, True))
    job = dict(**identity(), status='starting', config_sha256=c['config_sha256'], binding=binding, started_at=now())
    atomic_json(job_path, job)
    native.RUN = directory
    native.pilot.greedy80 = safe_greedy80
    try:
        with GPU_stage('retention', 'matched_native_original10B_vs_S1t3', c['config_sha256']) as (left, stage_heartbeat):
            def check():
                if stopped[0] or left() < 8:
                    raise InterruptedError('Retention whole-section stop/budget reserve')
            def heartbeat(stage, **values):
                check()
                stage_heartbeat(stage=stage, **values)
                job.update(status='evaluating', stage=stage, heartbeat_at=now(), **values)
                atomic_json(job_path, job)
            refs = {}
            for arm, point in (('parent', 't0'), ('S1', 't3')):
                state, ref = checkpoint(c, arm, point)
                del state
                check()
                evaluation = native.evaluate(arm, dict(checkpoint=ref['path'], checkpoint_sha256=ref['sha256']),
                                             dev, tok, plan, binding, heartbeat, check, time.monotonic() + left())
                assert evaluation['checkpoint_sha256'] == ref['sha256']
                assert evaluation['body']['documents'] == 256 and len(evaluation['generation']['outputs']) == 80
                assert not evaluation['protected_test_used'] and evaluation['evaluation_RNG_isolated']
                refs[arm] = reference(directory / arm / 'evaluation/result.json')
            atomic_json(directory / 'result.json', dict(status='complete_pending_160_Base_content', binding=binding,
                                                        evaluations=refs, GPU_teacher_updates=0,
                                                        original_Base_is_unadopted=True, passed=False,
                                                        protected_TEST_used=False, completed_at=now()))
        job.update(status='complete', completed_at=now())
    except BaseException as error:
        job.update(status='failed_or_stopped', error=repr(error), ended_at=now())
        raise
    finally:
        atomic_json(job_path, job)
    print('Native Base retention evaluated; all160 content judgments remain required')


def review(c, tok, path):
    directory = RUN / 'retention'
    job, result = read_json(directory / 'job.json'), read_json(directory / 'result.json')
    assert job['status'] == 'complete' and not alive(job) and job['config_sha256'] == c['config_sha256']
    notes = read_json(path)
    assert notes['reviewer'] == 'Codex nonblind' and notes['independent_human_blind'] is False
    cases = {row['id']: row for row in (json.loads(line) for line in (ROOT / 'eval/base.jsonl').read_text().splitlines()
                                       if re.search(r'"split"\s*:\s*"dev"', line))}
    evaluations, scores = {}, {}
    for arm in ('parent', 'S1'):
        ev_path = require_ref(result['evaluations'][arm])
        evaluations[arm] = read_json(ev_path)
        assert evaluations[arm]['binding'] == result['binding']
        generation = ev_path.with_name('generation.json')
        assert notes[arm]['generation_sha256'] == sha256(generation)
        scores[arm] = validate_content(notes[arm]['notes'], evaluations[arm], tok, cases)
    comp = compare(evaluations['parent'], evaluations['S1'], scores['parent'], scores['S1'], cases)
    comp['summaries']['unadopted_original10B'] = comp['summaries'].pop('adopted_Base')
    comp['BPB']['direction'] = 'S1 minus unadopted original10B; positive is worse'
    checks = dict(target_original_Base_absolute=comp['summaries']['target']['screen_passed'],
                  original_BPB_within1percent=comp['historical_Base_BPB_within1percent'],
                  no_more_repetition=comp['failure_differences']['repetition'] <= 0,
                  no_more_empty_role_unicode=all(comp['failure_differences'][key] <= 0
                                                for key in ('empty', 'role_leak', 'unicode_failure')))
    report = dict(comp, registered_retention_checks=checks, passed=all(checks.values()),
                  result=reference(directory / 'result.json'), authored_notes=reference(path),
                  original_Base_is_unadopted=True, fullDEV_executed=False, Base_adopted=False,
                  Chat_adopted=False, protected_TEST_used=False)
    atomic_json(directory / 'retention_review.json', report)
    print(json.dumps(dict(passed=report['passed'], checks=checks)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--inspect', action='store_true')
    parser.add_argument('--notes', type=Path)
    args = parser.parse_args()
    c, tok, _ = preflight(args.config)
    retention_assets()
    if args.inspect:
        print('Native retention assets/DEV256/Base80 CPU bindings passed; GPU0')
        return
    torch.set_num_threads(2)
    torch.use_deterministic_algorithms(True)
    seed_all(42)
    if args.notes is not None:
        review(c, tok, args.notes)
    else:
        with sdpa_kernel(SDPBackend.MATH):
            execute(c, tok)


if __name__ == '__main__':
    main()


