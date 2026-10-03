"""Audit actual 500M checkpoints and compare the same dev population to 100M.

Read-only for training artifacts. Run through uv after the 500M pipeline finishes.
"""
import argparse
import json
import math
from pathlib import Path
import statistics
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jmicro.base_review import validate_body
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.phase5 import bootstrap_bpb
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import implementation_hashes
from audit_phase5 import generation_summary
from phase6_performance import alive, finite_state
from run_base import validate_config


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', type=Path, default=ROOT / 'reports/phase6/base-20261003')
    parser.add_argument('--output', type=Path, default=ROOT / 'reports/phase6/base_500m_review.json')
    args = parser.parse_args()
    run = args.run.resolve()
    config = validate_config(ROOT / 'configs/phase6/base_frozen.json')
    target = config['milestones']['500M']
    checks = {}

    def require(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise ValueError(f'500M audit failed: {name}')

    snapshots = read_json(run / 'source_sha256.json')
    require('pipeline_source_snapshots_intact', all(
        sha256(run / 'snapshot' / name) == digest for name, digest in snapshots.items()))
    checkpoints, training, states = {}, {}, {}
    for kind, directory, end, start in (
        ('stable', run / 'stable', target['stable_updates'], 0),
        ('decay', run / 'decay-500M', target['decay_end_update'], target['stable_updates'])):
        supervisor = read_json(run / f'supervisor-{kind}-500M.json')
        require(f'{kind}_supervisor_terminal', supervisor['status'] == 'complete' and
                not alive(supervisor) and not supervisor.get('worker') and supervisor['target'] == '500M')
        latest = read_json(directory / 'latest.json')
        path = Path(latest['path'])
        require(f'{kind}_checkpoint_hash_update', latest['update'] == end and sha256(path) == latest['sha256'])
        state = torch.load(path, map_location='cpu', weights_only=False)
        states[kind] = state
        record = read_json(directory / 'run.json')
        rows = [json.loads(line) for line in (directory / 'metrics.jsonl').read_text().splitlines()]
        require(f'{kind}_all_completed_updates_present', [r['update'] for r in rows] == list(range(start + 1, end + 1)))
        require(f'{kind}_finite_metrics_and_checkpoint', finite_state(state) and all(
            math.isfinite(r[key]) for r in rows for key in ('loss', 'gradient_norm', 'lr', 'seconds', 'tokens_per_second')))
        require(f'{kind}_counters_match', state['update'] == end and state['tokens'] == end * config['input_tokens_per_update'] and
                state['tokens'] == rows[-1]['tokens_seen'] == record['tokens_seen'] and
                state['supervised_tokens'] == rows[-1]['supervised_tokens'] == record['supervised_tokens'] and
                state['body_bytes'] == rows[-1]['body_bytes_seen'] == record['body_bytes_seen'] and
                state['token_digest'] == rows[-1]['token_digest'] == record['token_digest'])
        require(f'{kind}_full_resume_state_and_frozen_inputs', all(key in state for key in
                ('model', 'optimizer', 'scheduler', 'rng', 'sampler', 'supervised_tokens', 'body_bytes', 'token_digest')) and
                state['implementation_sha256'] == implementation_hashes() and
                state['shard_manifest_sha256'] == config['shard_manifest_sha256'] and
                state['spec'] == record['spec'] and state['spec']['seed'] == 42 and
                state['spec']['batch'] == 32 and state['spec']['lr'] == .002 and state['spec']['context'] == 1024)
        saved = sorted(directory.glob('checkpoint-*.pt'))
        expected_updates = sorted(set([u for u in range(start + 1, end + 1) if u % config['save_every'] == 0] + [end]))
        require(f'{kind}_all_scheduled_checkpoints_retained',
                [int(p.stem.split('-')[-1]) for p in saved] == expected_updates)
        checkpoints[kind] = dict(path=str(path), sha256=latest['sha256'], update=end,
                tokens=state['tokens'], supervised_tokens=state['supervised_tokens'],
                body_bytes=state['body_bytes'], token_digest=state['token_digest'],
                retained=[dict(path=str(p), bytes=p.stat().st_size, sha256=sha256(p)) for p in saved])
        training[kind] = dict(spec=state['spec'], metric_rows=len(rows),
                first_100_loss=statistics.mean(r['loss'] for r in rows[:100]),
                last_100_loss=statistics.mean(r['loss'] for r in rows[-100:]),
                median_tokens_per_second=statistics.median(r['tokens_per_second'] for r in rows[200:] or rows),
                update_seconds=sum(r['seconds'] for r in rows), record=record,
                supervisor=supervisor)
    stable, decay = states['stable'], states['decay']
    require('new_Base_random_initialization_and_global_budget', 'lineage' not in stable and
            stable['spec']['schedule_updates'] == config['schedule_updates'] and stable['spec']['scheduler'] == 'wsd')
    require('decay_parent_and_stable_immutable', decay['lineage']['parent_sha256'] == checkpoints['stable']['sha256'] and
            decay['lineage']['parent_update'] == target['stable_updates'] and
            decay['branch_updates'] == target['decay_updates'] and decay['branch_tokens'] == target['decay_input_tokens'] and
            training['decay']['supervisor']['parent_checkpoint_immutable'])
    summary = read_json(ROOT / 'reports/phase6/expanded_dev_baseline.json')
    baseline_path = Path(summary['raw_report']['path'])
    require('100M_raw_baseline_binding', sha256(baseline_path) == summary['raw_report']['sha256'])
    baseline = read_json(baseline_path)
    scored = read_json(run / 'evaluation-500M/full-dev.json')
    generated = read_json(run / 'evaluation-500M/generation.json')
    old_generated = read_json(ROOT / 'reports/phase6/generation_diagnostics.json')
    require('evaluation_supervisor_terminal', read_json(run / 'supervisor-evaluate-500M.json')['status'] == 'complete')
    require('evaluation_bound_to_decay_and_state_isolated', all(r['checkpoint_sha256'] == checkpoints['decay']['sha256'] and
            r['implementation'] == implementation_hashes() and r['evaluation_state_isolated'] for r in (scored, generated)))
    require('scalar_batch_frozen_tolerance', scored['scalar_batched_gpu_agreement']['bpb_abs_difference'] <=
            scored['scalar_batched_gpu_agreement']['bpb_tolerance_frozen'] == .001)
    shard = Shard(Path(config['shards']), 'dev')
    expected = [(r['doc_id'], r['bytes'], r['body_tokens']) for r in shard.index]
    require('same_full_dev_population_and_body_once', all(validate_body(r['body'], expected) for r in (baseline, scored)))
    cases = [json.loads(line) for line in (ROOT / 'eval/base.jsonl').read_text().splitlines() if line.strip()]
    cases = [r for r in cases if r['split'] == 'dev']
    tok = Tokenizer(ROOT / config['tokenizer'])
    old_rates = generation_summary(old_generated['generation'], cases, tok)
    new_rates = generation_summary(generated['generation'], cases, tok)
    require('fixed_400_generations_redecoded_and_flags_independently_checked', len(cases) == 80 and
            len(generated['generation']['outputs']) == len(old_generated['generation']['outputs']) == 400)
    require('no_1B_started', not (run / 'decay-1B').exists() and stable['update'] == target['stable_updates'])
    ci = bootstrap_bpb(baseline['body'], scored['body'], seed=42, repetitions=2000)
    require('paired_CI_finite', all(math.isfinite(v) for v in [ci['point'], *ci['ci95']]))
    regressions = [dict(condition=key, metric=metric, old=old_rates[key][metric],
                        new=new_rates[key][metric], cases=new_rates[key]['cases'])
        for key in ('greedy/suppressed=True', 'greedy/suppressed=False', 'sampling/suppressed=True')
        for metric in ('repetition', 'unicode_failure', 'role_leak', 'empty')
        if new_rates[key][metric] > old_rates[key][metric]]
    results = dict(status='passed_500M_training_and_evaluation_audit', completed_at=now(), checks=checks,
        scope='authorized steps 1–5: 500M stable, independent decay, dev comparison and reporting; stop before 1B',
        config_sha256=sha256(ROOT / 'configs/phase6/base_frozen.json'), checkpoints=checkpoints,
        training=training, evaluation=dict(baseline_bpb=baseline['body']['bpb'], new_bpb=scored['body']['bpb'],
            documents=len(expected), body_bytes=scored['body']['body_bytes'], paired_improvement_CI=ci,
            old_generation_rates=old_rates, new_generation_rates=new_rates,
            full_dev_seconds=scored['body']['seconds'], generation_seconds=generated['generation_seconds'],
            evidence={str(p): sha256(p) for p in (baseline_path, run / 'evaluation-500M/full-dev.json',
                       run / 'evaluation-500M/generation.json')}),
        quality_targets_achieved=False, human_scoring_performed=False, test_evaluated=False,
        comparison_limit='Data, training-token budget and schedule differ; not an isolated causal test of data amount.',
        CI_limit='Document sampling uncertainty for one trained checkpoint per condition; not training-seed variance.',
        generation_regressions=regressions,
        next_action='Stop before 1B. Investigate generation regressions with a defined comparison and budget before proposing continuation.'
                    if regressions else 'Stop and report; decide continuation to 1B from dev metrics and generated text.')
    write_json(args.output, results)
    lines = ['# 拡張データ500M Baseの学習・評価', '',
        f"全文dev {len(expected):,}文書: BPB {baseline['body']['bpb']:.6f} → {scored['body']['bpb']:.6f}。",
        f"改善量（100M−500M）{ci['point']:.6f}、document paired 95% CI {ci['ci95']}。",
        '', '| 生成条件 | 旧EOS | 新EOS | 旧反復 | 新反復 | 旧Unicode破綻 | 新Unicode破綻 |',
        '|---|---:|---:|---:|---:|---:|---:|']
    for key in ('greedy/suppressed=True', 'greedy/suppressed=False', 'sampling/suppressed=True'):
        old, new = old_rates[key], new_rates[key]
        values = [f"{r[k]}/{r['cases']}" for k in ('eos', 'repetition', 'unicode_failure') for r in (old, new)]
        lines.append('| ' + key + ' | ' + ' | '.join(values) + ' |')
    lines += ['', '500M stableと独立763更新decayの全state checkpointを保持。1Bは未開始。',
        '人手のblind採点・test・Chatは未実施。データ量だけの因果効果とは結論しない。',
        'BPBは改善したが、生成の退行があるため、1Bへの自動継続は採用しない。原因調査の対照・予算・終了条件を先に定義する。'
            if regressions else '追加学習は生成本文とdev結果を確認して判断する。',
        '', '## 固定devの生成例（全80件、greedy抑制あり）', '']
    for item in generated['generation']['outputs']:
        if item['decoding'] == 'greedy' and item['suppressed']:
            lines += [f"### {item['id']} / {item['category']}", '', item['prefix'], '', '```text', item['text'], '```', '']
    args.output.with_suffix('.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps(dict(status=results['status'], checks=len(checks), baseline_bpb=baseline['body']['bpb'],
                         new_bpb=scored['body']['bpb'], paired_CI=ci), ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
