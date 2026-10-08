"""Bounded fresh-weight residual-scale measurement; no learning or GPU use."""
import copy
import math
from pathlib import Path
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src')]
import torch
from torch.nn import functional as F
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.model import JMicroModel
from jmicro.training import atomic_json

PHASE = ROOT / 'reports/phase6'
OUTPUT = PHASE / 'base_residual_initialization_measurement.json'
PREPARATION = PHASE / 'base_residual_seen_train_preparation.json'
PROPOSAL = PHASE / 'base_residual_initialization_proposal.json'


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def measure(model, rows, check):
    records = []
    for row in rows:
        check()
        model.zero_grad(set_to_none=True)
        ids = torch.tensor([row['input_ids']], dtype=torch.long)
        targets = torch.tensor(row['gold_targets'], dtype=torch.long)
        if targets.shape != ids[0].shape or int(targets.ne(-100).sum()) != row['teacher_tokens']:
            raise ValueError('Original next-token teacher alignment required')
        trace, handles = {}, []
        def capture(name):
            def hook(module, inputs, output):
                value = output[0] if isinstance(output, tuple) else output
                trace[name] = value.detach().clone()
            return hook
        handles.append(model.model.embed_tokens.register_forward_hook(capture('embedding')))
        for index, layer in enumerate(model.model.layers):
            handles.append(layer.register_forward_hook(capture(f'block-{index}')))
            handles.append(layer.self_attn.o_proj.register_forward_hook(capture(f'attention-{index}')))
            handles.append(layer.mlp.down_proj.register_forward_hook(capture(f'FFN-{index}')))
        try:
            logits = model(ids).logits[0]
            loss = F.cross_entropy(logits, targets)
            loss.backward()
        finally:
            for handle in handles:
                handle.remove()
        rms = lambda value: float(value.double().square().mean().sqrt())
        embed = trace['embedding']
        records.append(dict(id=row['id'], source=row['source'], teachers=row['teacher_tokens'],
            initial_teacher_NLL=float(loss.detach()), embedding_RMS=rms(embed),
            final_residual_RMS=rms(trace[f'block-{len(model.model.layers)-1}']),
            final_to_embedding_RMS=rms(trace[f'block-{len(model.model.layers)-1}']) / rms(embed),
            input_final_cosine=float(F.cosine_similarity(embed, trace[f'block-{len(model.model.layers)-1}'], dim=-1).mean()),
            layer_RMS=[dict(block=i, residual=rms(trace[f'block-{i}']),
                attention=rms(trace[f'attention-{i}']), FFN=rms(trace[f'FFN-{i}']))
                for i in range(len(model.model.layers))],
            gradients_RMS={name: rms(parameter.grad) for name, parameter in model.named_parameters()
                if name in ('model.embed_tokens.weight', 'model.layers.0.self_attn.o_proj.weight',
                            f'model.layers.{len(model.model.layers)-1}.self_attn.o_proj.weight')},
            finite_gradients=all(p.grad is not None and torch.isfinite(p.grad).all().item()
                                 for p in model.parameters())))
    model.zero_grad(set_to_none=True)
    return records


def main():
    if torch.cuda.is_available():
        raise ValueError('Explicit CUDA_VISIBLE_DEVICES= CPU-only execution required')
    if OUTPUT.exists():
        raise ValueError('Preserve original completed measurement; no rerun')
    started = time.monotonic()
    torch.set_num_threads(2)
    def check():
        if time.monotonic() - started > 30:
            raise TimeoutError('Fixed30-second CPU measurement cap exhausted')
    proposal = read_json(PROPOSAL)
    preparation = read_json(PREPARATION)
    if sha256(PREPARATION) != proposal['six_TRAIN_windows']['sha256']:
        raise ValueError('Prospective frozen TRAIN windows changed')
    if (len(preparation['selected']) != 6 or not preparation['all80_first_draw_trace_exact']
            or not preparation['original_next_token_alignment_verified']):
        raise ValueError('Exactly six existing actually consumed TRAIN windows required')
    config = read_json(PHASE / 'base_parallel_residual_proposal.json')['variants']['sequential']
    torch.manual_seed(42)
    control = JMicroModel(config)
    candidate = copy.deepcopy(control)
    rng = torch.get_rng_state().clone()
    scale = 1 / math.sqrt(2 * config['num_hidden_layers'])
    expected_names = {f'model.layers.{i}.{suffix}.weight' for i in range(config['num_hidden_layers'])
                      for suffix in ('self_attn.o_proj', 'mlp.down_proj')}
    with torch.no_grad():
        for name, parameter in candidate.named_parameters():
            if name in expected_names:
                parameter.mul_(scale)
    changed_names = {name for name, parameter in candidate.named_parameters()
                     if not torch.equal(parameter, dict(control.named_parameters())[name])}
    if (changed_names != expected_names or not torch.equal(rng, torch.get_rng_state())
            or candidate.lm_head.weight is not candidate.model.embed_tokens.weight
            or sum(p.numel() for p in candidate.parameters()) != 10001152):
        raise ValueError('Only26 residual-output matrices / unchanged RNG / tied10M required')
    measures = {name: measure(model, preparation['selected'], check)
                for name, model in (('control', control), ('scaled_initialization', candidate))}
    if not torch.equal(rng, torch.get_rng_state()):
        raise ValueError('Read-only deterministic comparison altered RNG')
    summary = {name: dict(mean_final_to_embedding_RMS=sum(v['final_to_embedding_RMS'] for v in rows)/len(rows),
                         mean_input_final_cosine=sum(v['input_final_cosine'] for v in rows)/len(rows),
                         teacher_weighted_initial_NLL=sum(v['teachers']*v['initial_teacher_NLL'] for v in rows)/sum(v['teachers'] for v in rows),
                         finite_gradients=all(v['finite_gradients'] for v in rows))
               for name, rows in measures.items()}
    check()
    result = dict(status='fresh_seed42_six_TRAIN_residual_scale_measurement_complete', created_at=now(),
        proposal=ref(PROPOSAL), preparation=ref(PREPARATION), script=ref(Path(__file__)),
        native_model=ref(ROOT/'src/jmicro/model.py'), model_config=config, actual_unique_parameters=10001152,
        scale=scale, scaled_output_matrices=sorted(changed_names), RNG_unchanged_after_scaling_and_measurement=True,
        measurements=measures, summaries=summary, CPU_seconds=time.monotonic()-started, CPU_cap_seconds=30,
        GPU_seconds=0, optimizer_updates=0, scientific_teacher_tokens=0, fresh_forward_backward_teacher_positions=1512,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False, protected_test_scored=False,
        limits='Six previously consumed TRAIN windows, fresh CPU FP32 weights; initial NLL/RMS/gradient measurements are not trained-model quality, instability proof, or evidence of future learning benefit. No learned weights changed or saved. Depth-scaled attention/FFN outputs jointly change initialization only; no inference-time scaling.')
    atomic_json(OUTPUT, result)
    print(dict(CPU_seconds=result['CPU_seconds'], scale=scale, summaries=summary))


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
