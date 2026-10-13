"""LR-only native learning using immutable tested complete-update arithmetic."""
import argparse
import json
import signal
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jmicro.experiment import read_json, now
from jmicro.training import atomic_json, seed_all
from phase6_performance import finite_state
from chat_lr_contract import B, RUN, LIMITS, preflight, load_parent, GPU_stage, reference
import run_chat_semantic as core

# Isolated process-local paths/accounting only. The frozen trainer and sampler,
# loss, precision, resume arithmetic and serialization are not modified.
core.RUN, core.LIMITS, core.GPU_stage, core.preflight = RUN, LIMITS, GPU_stage, preflight


def probe(parent, c, tok, rows):
    path = RUN / 'native_probe.json'
    assert not path.exists(), 'Completed verification retained'
    history = []
    with GPU_stage('probe', 'changed_peak_LR', c['config_sha256']) as (left, heartbeat):
        t = core.trainer(parent, c, tok, rows, 'S1')
        torch.cuda.reset_peak_memory_stats()
        for _ in range(8):
            assert left() > 20
            history.append(t.step())
            heartbeat(completed_updates=t.update)
        assert finite_state(dict(model=t.model.state_dict(), optimizer=t.optimizer.state_dict()))
        assert t.sampler.binding == c['sampler_binding']
        rates = [row['seconds'] / row['microbatches'] for row in history[2:]]
        dry = read_json(RUN / 'S1_dry_run.json')
        forecast = max(rates) * 1.35 * dry['microbatches'] + 60.
        verification_teachers = t.supervised_tokens
        peak = torch.cuda.max_memory_allocated()
        del t
        core.release()
        t = core.trainer(parent, c, tok, rows, 'S1', 1)
        terminal = t.step()
        assert 2 <= t.supervised_tokens <= 65 and t.sampler.examples == 1
        assert finite_state(dict(model=t.model.state_dict(), optimizer=t.optimizer.state_dict()))
        verification_teachers += t.supervised_tokens
        del t
        core.release()
    report = dict(passed=forecast <= LIMITS['train_S1'], config_sha256=c['config_sha256'],
                  GPU_optimizer_updates=9, verification_Assistant_teachers=verification_teachers,
                  candidate_learning_updates=0, finite=True, history=history, terminal_budget1=terminal,
                  forecast_training_seconds=forecast, limit_seconds=LIMITS['train_S1'],
                  peak_allocated_bytes=peak, quality_evidence=False, completed_at=now())
    atomic_json(path, report)
    assert report['passed'], 'Learning forecast cannot fit fixed allocation'
    print(json.dumps({key: report[key] for key in ('passed', 'GPU_optimizer_updates', 'forecast_training_seconds')}))


def resume(parent, c, tok, rows):
    path = RUN / 'native_resume_gate.json'
    assert not path.exists(), 'Completed verification retained'
    gates = {}
    with GPU_stage('resume', 'changed_LR_exact_resume', c['config_sha256']) as (left, heartbeat):
        for tag, fixture, budget in (('full-contract', rows, B), ('epoch-and-terminal', rows[:3], 1777)):
            assert left() > 30
            gates['S1-' + tag] = core.one_resume_gate(parent, c, tok, fixture, 'S1', tag, budget)
            heartbeat(completed=list(gates))
    atomic_json(path, dict(passed=all(g['passed'] for g in gates.values()), config_sha256=c['config_sha256'],
        gates=gates, GPU_optimizer_updates=16, candidate_learning_updates=0,
        verification_Assistant_teachers=sum(g['verification_Assistant_teachers'] for g in gates.values()),
        quality_evidence=False, completed_at=now()))
    print('16 CUDA resume verification updates: all model/Adam/scheduler/RNG/sampler/counters/history equal')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--config', type=Path, required=True)
    p.add_argument('--mode', choices=('probe', 'resume', 'train'), required=True)
    p.add_argument('--arm', choices=('both', 'S1'), default='S1')
    p.add_argument('--until', type=int, choices=(1, 2, 3), default=3)
    p.add_argument('--inspect', action='store_true')
    args = p.parse_args()
    c, tok, arms = preflight(args.config)
    if args.inspect:
        print('Frozen LR-only contract, accepted TRAIN and new DEV preflight passed; GPU0')
        return
    torch.set_num_threads(2)
    torch.use_deterministic_algorithms(True)
    seed_all(42)
    assert torch.cuda.is_available() and '4090' in torch.cuda.get_device_name(0)
    stopped = [False]
    signal.signal(signal.SIGTERM, lambda *_: stopped.__setitem__(0, True))
    signal.signal(signal.SIGINT, lambda *_: stopped.__setitem__(0, True))
    parent = load_parent(c)
    if args.mode == 'probe':
        probe(parent, c, tok, arms['S1'])
    elif args.mode == 'resume':
        resume(parent, c, tok, arms['S1'])
    else:
        core.train_arm(parent, c, tok, arms['S1'], 'S1', args.until, stopped)


if __name__ == '__main__':
    main()
