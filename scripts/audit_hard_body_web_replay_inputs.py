"""Audit actual cached comparison inputs and immutable-parent mass, without GPU."""
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
import argparse
import json
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import alive
from run_eos_short_pilot import equal_state
import run_hard_body_web_replay_comparison as study

KEYS = ('token_digest','focus_token_digest','source_teachers','source_eos','source_input_tokens',
    'source_body_bytes','source_focus_teachers','reference_input_tokens','reference_hard_body_target_positions',
    'reference_ignored_positions','reference_digest','reference_non_EOS_teacher_probability_mass',
    'combined_student_physical_input_tokens')


def compare(left, right, expected):
    if len(left) != expected or len(right) != expected:
        raise ValueError('Every actual update required')
    for a,b in zip(left,right,strict=True):
        for key in KEYS:
            if not equal_state(a[key], b[study.control_history_key(key)]):
                raise ValueError(f'Input/teacher-mass protocol changed: update{a["update"]} {key}')
        if a['combined_hard_teacher_positions'] != a['additional_teacher_tokens']+a['reference_hard_body_target_positions']:
            raise ValueError('Gold targets cannot be hidden in probability mass')
    return dict(updates=expected, all_inputs_digests_masks_source_counters_equal=True,
        all_parent_non_EOS_probability_masses_equal=True,
        gold_body_teacher_positions=left[-1]['reference_hard_body_target_positions'],
        non_EOS_parent_probability_mass=left[-1]['reference_non_EOS_teacher_probability_mass'])


def main(probe_only):
    probe = study.probe_evidence()
    old_probe = read_json(study.MECHANISM_RUN/'probe/result.json')
    report = dict(created_at=now(), source_sha256=sha256(Path(__file__)),
        probe=study.reference(study.RUN/'probe/result.json'),
        cached_probe=study.reference(study.MECHANISM_RUN/'probe/result.json'),
        all32=compare(probe['timing']['histories'],old_probe['timing']['histories'],32),
        GPU_seconds=0, scientific_teacher_tokens=0, newly_prepared_source_tokens=0,
        limitations='Equal inputs/mass are not equal supervision: current targets are gold words, control targets are conditional soft distributions. No quality or sole-cause proof.')
    if not probe_only:
        job = read_json(study.RUN/'job.json')
        if job['status'] != 'complete' or alive(job):
            raise ValueError('Actual finished scientific process required')
        left = study.RUN/study.ARM/'training/metrics.jsonl'
        right = study.MECHANISM_RUN/study.MECHANISM_ARM/'training/metrics.jsonl'
        report['histories'] = dict(current=study.reference(left),control=study.reference(right))
        report['all3068'] = compare([json.loads(s) for s in left.read_text().splitlines()],
            [json.loads(s) for s in right.read_text().splitlines()],3068)
    target = ROOT/('reports/phase6/hard_body_web_replay_probe_input_audit.json' if probe_only else
        'reports/phase6/hard_body_web_replay_input_audit.json')
    if target.exists():
        raise ValueError('Preserve audit evidence')
    atomic_json(target,report)
    print({k:report[k] for k in ('all32','GPU_seconds')})


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    p = argparse.ArgumentParser()
    p.add_argument('--probe-only',action='store_true')
    main(p.parse_args().probe_only)
