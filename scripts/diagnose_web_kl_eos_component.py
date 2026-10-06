"""One bounded read-only CPU pass on the preselected16 existing train windows."""
import time
START = time.monotonic()
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
import gc
import hashlib
import numpy as np
import torch
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from jmicro.model import JMicroModel
from jmicro.eos_pilot import TrainView
from historical_parent_condition_trainer import historical_web_cursor
from resident_web_window import selected_blocks
from web_kl_eos_decomposition import decompose

PROPOSAL = ROOT / 'reports/phase6/web_kl_followup_diagnostic_proposal.json'
RUN = ROOT / 'reports/phase6/web-kl-EOS-component-20261006'
SOURCES = ('scripts/diagnose_web_kl_eos_component.py','scripts/web_kl_eos_decomposition.py',
    'tests/test_web_kl_eos_decomposition.py','src/jmicro/model.py','scripts/resident_web_window.py')


def check():
    if time.monotonic() - START > 180:
        raise TimeoutError('Fixed180s CPU diagnostic budget exhausted')


def main():
    if RUN.exists():
        raise ValueError('Preserve prior diagnostic; no identical rerun')
    RUN.mkdir(parents=True)
    job = dict(status='running',started_at=now(),CPU_budget_seconds=180,GPU_seconds=0,
        optimizer_updates=0,scientific_teacher_tokens=0,protected_test_used=False,
        proposal_sha256=sha256(PROPOSAL),source_sha256={p:sha256(ROOT/p) for p in SOURCES})
    atomic_json(RUN / 'job.json', job)
    try:
        proposal = read_json(PROPOSAL)
        if proposal['CPU_budget_seconds'] != 180 or proposal['GPU_budget_seconds'] != 0 or proposal['Base_complete']:
            raise ValueError('Fixed CPU-only diagnostic scope required')
        for ref in (proposal['completion'],proposal['review'],proposal['resident_preparation'],*proposal['models'].values()):
            check()
            if sha256(Path(ref['path'])) != ref['sha256']:
                raise ValueError('Frozen diagnostic reference differs')
        prepared = read_json(Path(proposal['resident_preparation']['path']))
        cache = Path(prepared['cache_directory']); ready = read_json(cache / 'ready.json')
        if ready != prepared['cache']:
            raise ValueError('Accepted resident cache differs')
        for name,record in ready['files'].items():
            if sha256(cache/name) != record['sha256']:
                raise ValueError('Resident cache bytes differ')
        windows = np.memmap(cache/'windows.bin',mode='r',dtype='<u2',shape=(73421,1025))[:16].astype(np.int64)
        x = torch.from_numpy(windows[:, :-1].copy()); y = torch.from_numpy(windows[:, 1:].copy()); y[y == 2] = -100
        digest = hashlib.sha256(x.numpy().tobytes()+y.numpy().tobytes()).hexdigest()
        torch.set_num_threads(8); torch.use_deterministic_algorithms(True)
        probabilities = {}; model_config = None
        for name in ('parent','staged_CE','staged_CE_parent_KL'):
            check(); state = torch.load(proposal['models'][name]['path'],map_location='cpu',weights_only=False)
            if name == 'parent':
                cursor = historical_web_cursor(state)
                view = TrainView(ready['binding']['source_directory'],ready['binding']['source_manifest_sha256'])
                if cursor != ready['binding']['initial_cursor'] or not np.array_equal(
                    np.load(cache/'block_ids.npy',allow_pickle=False)[:16], selected_blocks(view,cursor,16)):
                    raise ValueError('Exact actual parent16 train window order required')
                model_config = state['model_config']
            elif state['model_config'] != model_config:
                raise ValueError('Same model architecture required')
            model = JMicroModel(state['model_config']).eval(); model.load_state_dict(state['model']); del state
            model.requires_grad_(False); logits = []
            with torch.inference_mode(), sdpa_kernel(SDPBackend.MATH):
                for index in range(16):
                    check(); output = model(x[index:index+1]).logits
                    if not torch.isfinite(output).all():
                        raise ValueError('Finite CPU FP32 logits required')
                    logits.append(output[0].clone())
                    job.update(model=name,completed_windows=index+1,CPU_elapsed_seconds=time.monotonic()-START)
                    atomic_json(RUN/'job.json',job)
            probabilities[name] = torch.stack(logits); del model,logits; gc.collect()
        results = {}
        for name in ('staged_CE','staged_CE_parent_KL'):
            check(); values = decompose(probabilities['parent'],probabilities[name],y)
            stats = {k:dict(mean=v.mean().item(),quantiles=torch.quantile(v,torch.tensor([0.,.25,.5,.75,1.],dtype=v.dtype)).tolist()) for k,v in values.items()}
            derivative = values['EOS_logit_KL_derivative']
            stats['EOS_gradient_position_counts'] = dict(positive=int((derivative>0).sum()),negative=int((derivative<0).sum()),zero=int((derivative==0).sum()))
            stats['full_KL_mean_chain_rule_absolute_error'] = abs(values['full_KL'].mean().item()-values['EOS_mass_KL'].mean().item()-values['weighted_conditional_non_EOS_KL'].mean().item())
            results[name] = stats
        check()
        report = dict(status='actual_CPU16_train_window_EOS_component_diagnostic_complete',created_at=now(),
            proposal_sha256=sha256(PROPOSAL),source_sha256=job['source_sha256'],models=proposal['models'],
            windows=16,physical_input_tokens=x.numel(),soft_body_positions=int((y>=8).sum()),ignored_special_positions=int((y<8).sum()),
            input_label_digest=digest,resident_manifest_sha256=sha256(cache/'ready.json'),
            precision=proposal['precision'],results=results,CPU_elapsed_seconds=time.monotonic()-START,
            GPU_seconds=0,optimizer_updates=0,scientific_teacher_tokens=0,newly_prepared_source_tokens=0,
            protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
            limitations=proposal['interpretation_limit'])
        atomic_json(RUN/'result.json',report)
        atomic_json(ROOT/'reports/phase6/web_kl_EOS_component_diagnostic.json',report)
        job.update(status='complete',CPU_elapsed_seconds=time.monotonic()-START,completed_at=now())
        print(report['results'],flush=True)
    except BaseException as error:
        job.update(status='failed',error=repr(error),CPU_elapsed_seconds=time.monotonic()-START); raise
    finally:
        atomic_json(RUN/'job.json',job)


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
