"""Bounded initial-vs-terminal normalization gain screen; no optimization."""
import json
from pathlib import Path
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT, now, read_json, sha256
from base_parallel_residual_model import model_from_config

PHASE = ROOT / 'reports/phase6'
PROPOSAL = PHASE / 'base_residual_norm_gain_screen_proposal.json'
OUTPUT = PHASE / 'base_residual_norm_gain_screen.json'


def main():
    started = time.perf_counter()
    if OUTPUT.exists():
        raise ValueError('Preserve completed norm gain screen')
    proposal = read_json(PROPOSAL)
    completed = read_json(PHASE / 'base_residual_seen_train_diagnostic_completion.json')
    trained = read_json(PHASE / 'base-parallel-residual-comparison-20261007/sequential/train-result.json')
    if completed['result']['sha256'] != sha256(PHASE / 'base_residual_seen_train_diagnostic.json'):
        raise ValueError('Actual previous six-case diagnostic required')
    checkpoint = Path(trained['checkpoint'])
    if sha256(checkpoint) != trained['checkpoint_sha256']:
        raise ValueError('Actual same fixed sequential2B checkpoint required')
    state = torch.load(checkpoint, map_location='cpu', weights_only=False)
    if state['counters']['supervised_tokens'] != 2000000000 or state['spec']['arm'] != 'sequential':
        raise ValueError('Actual current fresh2B state required')
    with torch.device('meta'):
        model = model_from_config(state['model_config'])
    names = [name for name,_ in model.named_parameters()]
    groups = state['optimizer']['param_groups']
    if len(groups) != 1 or len(groups[0]['params']) != len(names):
        raise ValueError('Actual single-group optimizer parameter mapping differs')
    initial = state['model_config']['norm_initial_gain']
    if initial <= 0 or initial != proposal['initial_norm_gain']:
        raise ValueError('Fixed positive initial normalization gain required')
    rows = []
    for index,name in enumerate(names):
        if not (name.endswith('layernorm.weight') or name == 'model.norm.weight'):
            continue
        value = state['model'][name].float()
        if not bool(torch.isfinite(value).all()):
            raise ValueError('Finite actual norm parameters required')
        magnitude = value.abs()
        median = float(magnitude.median())
        rows.append(dict(name=name, optimizer_parameter_id=groups[0]['params'][index],
            weight_decay=groups[0]['weight_decay'], count=value.numel(), initial_gain=initial,
            mean=float(value.mean()), absolute_median=median, absolute_mean=float(magnitude.mean()),
            rms=float(value.square().mean().sqrt()), minimum=float(value.min()), maximum=float(value.max()),
            fraction_below_quarter_initial=float((magnitude < initial*.25).float().mean()),
            norm_median_below_quarter_initial=median < initial*.25))
    block_rows = [r for r in rows if r['name'] != 'model.norm.weight']
    if len(block_rows) != 26 or len(rows) != 27:
        raise ValueError('All26 block norms and final norm required')
    small = sum(r['norm_median_below_quarter_initial'] for r in block_rows)
    screen = small >= 13
    elapsed = time.perf_counter()-started
    if elapsed > proposal['CPU_budget_seconds']:
        raise ValueError('CPU30-second screen budget exhausted')
    result = dict(status='all27_actual_norm_gain_screen_complete', created_at=now(),
        proposal_sha256=sha256(PROPOSAL), source_sha256=sha256(Path(__file__)), CPU_seconds=elapsed,
        checkpoint=dict(path=str(checkpoint), sha256=trained['checkpoint_sha256']), initial_gain=initial,
        optimizer_single_group_weight_decay=groups[0]['weight_decay'], rows=rows,
        block_norms_with_median_below_quarter_initial=small, block_norms=26,
        gain_collapse_screen_triggered=screen,
        all_norms_in_actual_decayed_optimizer_group=True,
        supports_bounded_selective_norm_decay_comparison=screen,
        root_cause_proven=False, removing_norm_decay_quality_benefit_proven=False,
        next_action=('Consider one prospectively fixed matched fresh control vs norm-decay-excluded comparison with own measured budget; no inherited-condition rescue or automatic long training.' if screen else
                    'Do not launch selective norm-decay training on this magnitude screen. Extreme block norm gain collapse is not observed; retain the failed recipe and investigate a distinct supported cause.'),
        GPU_seconds=0, scientific_teacher_tokens=0, optimizer_updates=0,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        limitations='Magnitude screen only, not a universal optimal-gain criterion or Base acceptance gate. Adjacent linear matrices can compensate norm scale. Initial gain from frozen initialization, terminal tensors from the current checkpoint; no causal weight-decay ablation, no independent learned seed or heldout-quality evidence.')
    OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(CPU_seconds=elapsed, initial_gain=initial, all_norms_decayed=True,
        block_norms_below_quarter=small, gain_collapse_screen_triggered=screen,
        median_range=[min(r['absolute_median'] for r in block_rows),max(r['absolute_median'] for r in block_rows)],
        final_norm=next(r for r in rows if r['name']=='model.norm.weight')),ensure_ascii=False))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
