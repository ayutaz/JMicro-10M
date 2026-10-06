"""Bounded CPU metadata audit of exactly two documented Base checkpoints."""
from datetime import datetime, timezone
import gc
import hashlib
import json
import math
from pathlib import Path
import sys
import time
import torch

ROOT = Path(__file__).resolve().parents[1]
PROPOSAL = ROOT / 'reports/phase6/base_parent_baseline_audit_proposal.json'
OUTPUT = ROOT / 'reports/phase6/base_parent_baseline_audit.json'
REFERENCES = {}


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b''):
            digest.update(chunk)
    return digest.hexdigest()


def read(path, expected=None):
    path = Path(path); digest = sha(path)
    if expected is not None and digest != expected:
        raise ValueError(f'Fixed evidence differs: {path}')
    REFERENCES[str(path)] = digest
    return json.loads(path.read_text(encoding='utf-8'))


def metadata(state):
    groups = state['optimizer']['param_groups']
    steps = [float(s['step']) for s in state['optimizer']['state'].values()]
    if (not groups or not steps or any(not math.isfinite(g['lr']) or g['lr'] <= 0 for g in groups)
            or any(not math.isfinite(s) or s < 0 for s in steps)
            or not all(k in state for k in ('model','optimizer','scheduler','rng','sampler','spec'))):
        raise ValueError('Complete actual optimizer/scheduler/RNG/sampler state required')
    cursors = []
    def walk(row, path):
        if isinstance(row, dict):
            if {'seed','epoch','position','context','blocks'} <= set(row):
                cursors.append(dict(path=path, **{k: row[k] for k in ('seed','epoch','position','context','blocks')}))
            for key, value in row.items():
                if isinstance(value, dict):
                    walk(value, path + '/' + key)
    walk(state['sampler'], 'sampler')
    return dict(update=state['update'], input_tokens=state['tokens'], teacher_tokens=state['supervised_tokens'],
        body_bytes=state['body_bytes'], actual_optimizer_LRs=[g['lr'] for g in groups],
        saved_spec_peak_lr=state['spec']['lr'], optimizer_state_entries=len(steps),
        optimizer_step_range=[min(steps),max(steps)], scheduler=state['scheduler'],
        sampler_kind=state['sampler'].get('kind','original_block_sampler'),
        sampler_keys=sorted(state['sampler']), block_sampler_cursors=cursors,
        sampler_position=state['sampler'].get('position'), model_config=state['model_config'],
        model_tensor_count=len(state['model']), shard_manifest_sha256=state['shard_manifest_sha256'],
        implementation_sha256=state['implementation_sha256'], lineage=state.get('lineage'),
        complete_optimizer_scheduler_RNG_sampler_present=True)


def parent_references(value, path='config'):
    """Only recorded training parents; an evaluation guard is not a parent."""
    found = []
    if isinstance(value, dict):
        for key, row in value.items():
            if key == 'parent' and isinstance(row, dict) and 'sha256' in row and 'path' in row:
                found.append(dict(field=path + '/parent', checkpoint=row))
            elif key == 'parents' and isinstance(row, dict):
                for name, ref in row.items():
                    if isinstance(ref, dict) and 'sha256' in ref and 'path' in ref:
                        found.append(dict(field=path + '/parents/' + name, checkpoint=ref))
            found.extend(parent_references(row, path + '/' + key))
    elif isinstance(value, list):
        for index, row in enumerate(value):
            found.extend(parent_references(row, path + '/' + str(index)))
    return found


def main():
    started = time.perf_counter(); torch.set_num_threads(2)
    if OUTPUT.exists():
        raise ValueError('Preserve completed bounded audit')
    p = read(PROPOSAL)
    if p['CPU_limit_seconds'] != 30 or p['GPU_seconds'] or p['new_scientific_teacher_tokens'] or p['optimizer_updates']:
        raise ValueError('CPU30s/no training audit required')
    for ref in p['references'].values():
        read(ref['path'], ref['sha256'])
    inventory = read(ROOT / 'reports/phase6/base_parent_budget_inventory.json')
    guard = read(p['references']['historical_web']['path'], p['references']['historical_web']['sha256'])
    original_config = read(ROOT / 'configs/phase6/mature_base_condition_comparison.json')
    original_eval = read(ROOT / 'reports/phase6/mature-base-condition-comparison-20261006/evaluation/parent10B/evaluation/result.json')
    selected = {name:inventory['records'][name]['checkpoint'] for name in ('originalWeb10B','historicalWeb')}
    if original_eval['checkpoint_sha256'] != selected['originalWeb10B']['sha256'] or guard['checkpoint_sha256'] != selected['historicalWeb']['sha256']:
        raise ValueError('Actual two weight-bound saved evaluations required')
    states = {}
    for name, ref in selected.items():
        if time.perf_counter() - started > 30:
            raise TimeoutError('CPU30s exhausted')
        if sha(ref['path']) != ref['sha256']:
            raise ValueError('Explicit parent checkpoint SHA differs')
        REFERENCES[ref['path']] = ref['sha256']
        state = torch.load(ref['path'],map_location='cpu',weights_only=False)
        states[name] = dict(checkpoint=ref, **metadata(state))
        recorded = inventory['records'][name]
        if (states[name]['update'] != recorded['update'] or states[name]['input_tokens'] != recorded['input_tokens']
                or states[name]['teacher_tokens'] != recorded['supervised_tokens']
                or states[name]['actual_optimizer_LRs'] != recorded['optimizer_param_group_LRs']):
            raise ValueError('Recorded parent inventory does not match actual fullstate')
        del state; gc.collect()
    base, historical = states['originalWeb10B'],states['historicalWeb']
    if base['model_config'] != historical['model_config'] or base['shard_manifest_sha256'] != historical['shard_manifest_sha256']:
        raise ValueError('Same actual model shape and original Web source required')
    old_web = read(ROOT / 'configs/phase6/story20_low_lr_10b_500m.json')
    if old_web['parent']['sha256'] != base['checkpoint']['sha256'] or historical['update'] - base['update'] != old_web['updates_per_arm']:
        raise ValueError('Historical500M Web branch lineage differs')
    lr = read(p['references']['existing_lowLR_config']['path'])
    lr_review = read(p['references']['existing_lowLR_review']['path'])
    if lr['goals'] != {'web':0,'short':200000000}:
        raise ValueError('Existing lowLR recipe differs from declared evidence')
    matched = []
    registry = {}
    for path in sorted((ROOT / 'configs/phase6').glob('*.json')):
        value = read(path); registry[str(path.relative_to(ROOT))] = REFERENCES[str(path)]
        for ref in parent_references(value):
            if ref['checkpoint']['sha256'] == historical['checkpoint']['sha256']:
                matched.append(dict(config=str(path.relative_to(ROOT)), **ref))
    threshold = guard['body']['bpb'] * 1.01
    quality = {name:dict(BPB=e['body']['bpb'],greedy_rates=e['greedy_rates'],
                         original_Web_1percent_threshold=threshold, original_Web_guard_passes=e['body']['bpb']<=threshold)
               for name,e in (('originalWeb10B',original_eval),('historicalWeb',guard))}
    if [(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in original_eval['body']['rows']] != [(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in guard['body']['rows']]:
        raise ValueError('Same common-byte dev targets required')
    report = dict(status='completed_CPU_two_documented_parent_and_registered_route_audit',
        created_at=datetime.now(timezone.utc).isoformat(), CPU_seconds=time.perf_counter()-started,
        GPU_seconds=0,new_scientific_teacher_tokens=0,optimizer_updates=0,states=states,quality=quality,
        historical_Web_extra_input_tokens=historical['input_tokens']-base['input_tokens'],
        historical_Web_extra_teacher_tokens=historical['teacher_tokens']-base['teacher_tokens'],
        historical_Web_extra_updates=historical['update']-base['update'],
        existing_lowLR=dict(parents=lr['parents'],peak_lr=lr['peak_lr'],goals=lr['goals'],
            continuation_BPB=lr_review['summaries']['continuation']['BPB'],continuation_coherent=lr_review['summaries']['continuation']['coherent'],
            equivalent_to_same100M_original_Web_mixture=False),
        registered_configs=registry,historical_parent_training_matches=matched,
        historical_parent_matched_short_source_route_in_registry=bool(matched),
        references=REFERENCES,source_sha256=sha(Path(__file__)),Base_adopted=False,Base_complete=False,
        Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True,
        old_numerical7_preserved=True,
        limitations='Exactly two preselected documented checkpoints, saved evaluations and registered phase6 config parents. No new model scoring, external experiment discovery or favorable checkpoint search. No direct parent match in the registry does not prove no unregistered experiment exists. Parent states differ in Web amount/order, Adam/RNG/sampler/scheduler and actual LR; comparison of inherited routes is not a pure parent-weight or LR causal effect. Original10B failing the unchanged historical BPB guard does not invalidate other independent quality failures or justify relaxing any gate.')
    if report['CPU_seconds'] > 30:
        raise TimeoutError('CPU30s exhausted')
    OUTPUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(CPU_seconds=report['CPU_seconds'],states={n:{k:s[k] for k in ('update','input_tokens','teacher_tokens','actual_optimizer_LRs','saved_spec_peak_lr','optimizer_step_range','sampler_kind','block_sampler_cursors')} for n,s in states.items()},quality=quality,historical_parent_training_matches=matched,existing_lowLR=report['existing_lowLR']),ensure_ascii=False))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
