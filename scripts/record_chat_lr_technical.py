"""Bind actual successful verification and anchor every early GPU charge."""
from pathlib import Path
import torch
from chat_lr_contract import RUN, preflight, reference, require_ref, LIMITS
from jmicro.experiment import read_json, now
from jmicro.training import atomic_json
from run_eos_short_pilot import equal_state
from phase6_performance import finite_state, alive


if __name__ == '__main__':
    c, _, _ = preflight()
    probe = read_json(RUN / 'native_probe.json')
    resume = read_json(RUN / 'native_resume_gate.json')
    forecast = read_json(RUN / 'evaluation_forecast.json')
    assert all(r['passed'] and r['config_sha256'] == c['config_sha256'] for r in (probe, resume, forecast))
    assert probe['GPU_optimizer_updates'] == 9 and resume['GPU_optimizer_updates'] == 16
    assert probe['candidate_learning_updates'] == resume['candidate_learning_updates'] == 0
    assert probe['forecast_training_seconds'] <= LIMITS['train_S1']
    assert forecast['maximum_required_responses'] == 6132 and forecast['maximum_new_NLL_batches'] == 261
    assert forecast['forecast_evaluation_seconds'] <= LIMITS['evaluation']
    keys = ('model', 'optimizer', 'scheduler', 'rng', 'sampler', 'tokens', 'supervised_tokens',
            'body_bytes', 'token_digest', 'lineage', 'update', 'spec')
    for gate in resume['gates'].values():
        assert gate['passed'] and all(gate['checks'].values())
        states = [torch.load(require_ref(gate['checkpoint_refs'][branch]), map_location='cpu', weights_only=False)
                  for branch in ('continuous', 'resumed')]
        assert all(finite_state(state) for state in states)
        assert all(equal_state(states[0][key], states[1][key]) for key in keys)
        del states
    ledger = read_json(RUN / 'GPU_ledger.json')
    early = ledger['entries'][:3]
    assert len(early) == 3
    assert [r['category'] for r in early] == ['probe', 'resume', 'evaluation']
    assert all(r['status'] == 'complete' and not alive(r) for r in early)
    atomic_json(RUN / 'technical_milestone.json', dict(passed=True, completed_at=now(),
        config=reference(c['config_path']), config_sha256=c['config_sha256'],
        gates={name: reference(RUN / name) for name in ('native_probe.json', 'native_resume_gate.json', 'evaluation_forecast.json')},
        actual_CUDA_resume_states_equal=True, verification_GPU_updates=25, candidate_learning_updates=0,
        ledger_entries=early, source=reference(Path(__file__)), quality_evidence=False))
    print('25 actual CUDA verification updates and exact states bound; first3 charges anchored; no learning claim')
