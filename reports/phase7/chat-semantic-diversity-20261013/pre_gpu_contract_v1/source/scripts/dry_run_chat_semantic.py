"""Replay candidate complete-teacher updates; reuse the bound control replay."""
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from dry_run_chat_improvement import consume
from prepare_chat_semantic_train import RUN, DATA, CONTROL, WEIGHTS


def main():
    assert not (DATA / 'dev.jsonl').exists(), 'Candidate consumption must precede new DEV'
    tok = Tokenizer(ROOT / 'artifacts/phase2/4096/tokenizer.model')
    source = ROOT / 'reports/phase7/chat-generalization-20261013/D1_dry_run.json'
    a = read_json(source)
    assert a['source_sha256'] == sha256(CONTROL / 'train.jsonl')
    historical = read_json(ROOT / 'reports/phase7/chat-generalization-20261013/D1/result.json')
    assert historical['status'] == 'learning_complete'
    assert a['updates'] == historical['checkpoint']['update'] == 3641
    assert a['Assistant_teachers'] == historical['checkpoint']['Assistant_teachers'] == 1899562
    candidate = DATA / ('train.jsonl' if (DATA / 'manifest.json').exists() else 'candidate.train.jsonl')
    b = consume(candidate, tok)
    updates = abs(b['updates'] / a['updates'] - 1)
    decay = abs(b['decay_coefficient'] / a['decay_coefficient'] - 1)
    length = sum(abs(x - y) for x, y in zip(a['length_bin_fractions'], b['length_bin_fractions'], strict=True)) / 2
    eot = abs(b['EOT_fraction'] - a['EOT_fraction'])
    mixture = max(abs(b['consumed_teacher_fractions'][key] - weight) for key, weight in WEIGHTS.items())
    checks = dict(updates_relative_difference=updates <= .05, decay_relative_difference=decay <= .001,
                  actual_length_TV=length <= .10, actual_EOT_match=eot <= .01,
                  actual_teacher_mixture=mixture <= .01,
                  final_whole_target_overshoot=all(0 <= row['final_overshoot'] <= 64 for row in (a, b)),
                  target_exposure_at_most_three=all(row['max_target_exposures'] <= 3 for row in (a, b)))
    atomic_json(RUN / 'S0_dry_run.json', dict(a, historical_reuse=dict(path=str(source), sha256=sha256(source))))
    atomic_json(RUN / 'S1_dry_run.json', b)
    result = dict(created_at=now(), status='passed' if all(checks.values()) else 'redesign_required',
                  checks=checks, update_relative_difference=updates, decay_relative_difference=decay,
                  length_TV=length, EOT_absolute_difference=eot, mixture_max_absolute_difference=mixture,
                  S0={key: value for key, value in a.items() if key not in ('rows', 'sampler_terminal')},
                  S1={key: value for key, value in b.items() if key not in ('rows', 'sampler_terminal')},
                  control_replay_source=dict(path=str(source), sha256=sha256(source)),
                  GPU_learning_updates=0, CPU_only=True, quality_evidence=False, new_DEV_read=False)
    atomic_json(RUN / 'consumption_dry_run.json', result)
    print(json.dumps(dict(status=result['status'], checks=checks, candidate_updates=b['updates'],
                          candidate_teachers=b['Assistant_teachers'], length_TV=length, EOT_difference=eot)))


if __name__ == '__main__':
    main()
