"""CPU rejection checks using copies of actual artifacts; no automatic scoring."""
import argparse
from copy import deepcopy
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, now
from jmicro.training import atomic_json
from chat_semantic_contract import RUN, preflight, reference
from complete_chat_semantic import verify_ledger, verify_selection
from audit_chat_semantic_progress import validate_nll
from evaluate_chat_semantic import nll_windows
from review_chat_semantic_observer import get_items, protocol_view


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--technical', action='store_true')
    args = parser.parse_args()
    config, tok, _ = preflight(ROOT / 'configs/phase7/chat-semantic-diversity-20261013.json')
    checks = []

    def rejected(name, function, value, mutate):
        altered = deepcopy(value)
        mutate(altered)
        try:
            function(altered)
        except (AssertionError, KeyError):
            checks.append(dict(name=name, rejected=True))
        else:
            raise AssertionError('Fabricated evidence accepted: ' + name)

    raw_path = RUN / 'evaluation/parent/t0/old/greedy/result.json'
    raw = read_json(raw_path)
    get_items(raw_path)
    new = deepcopy(raw)
    del new['requested_five_steps_complete']
    new['requested_six_steps_complete'] = False
    expected = deepcopy(new)
    expected['requested_five_steps_complete'] = False
    assert protocol_view(new) == expected and 'requested_five_steps_complete' not in new
    checks.append(dict(name='only_false_legacy_completion_alias_added_in_memory', verified=True))
    rejected('adapter_rejects_new_completion_true', protocol_view, new,
             lambda r: r.update(requested_six_steps_complete=True))
    rejected('adapter_rejects_legacy_completion_true', protocol_view, raw,
             lambda r: r.update(requested_five_steps_complete=True))
    rejected('adapter_rejects_contradictory_true_new_flag', protocol_view, raw,
             lambda r: r.update(requested_six_steps_complete=True))
    assert read_json(raw_path) == raw
    ledger = read_json(RUN / 'GPU_ledger.json')
    if args.technical:
        ledger['entries'] = read_json(RUN / 'technical_milestone.json')['ledger_entries']
        ledger['total_charged_seconds'] = sum(r['charged_seconds'] for r in ledger['entries'])
    verify_ledger(ledger, config)
    for name, mutate in (
        ('ledger_changed_early_charge', lambda r: r['entries'][0].update(charged_seconds=1.)),
        ('ledger_unregistered_config', lambda r: r['entries'][-1].update(config_sha256='0' * 64)),
        ('ledger_dropped_gate_charge', lambda r: r['entries'].pop(0)),
        ('ledger_overlapping_jobs', lambda r: r['entries'][-1].update(started_at=r['entries'][0]['started_at'])),
        ('ledger_increased_cap', lambda r: r['limits'].update(train_S1=3001.)),
        ('ledger_fabricated_total', lambda r: r.update(total_charged_seconds=0.)),
    ):
        rejected(name, lambda r: verify_ledger(r, config), ledger, mutate)
    sources = {name: reference(ROOT / 'scripts' / name) for name in
               ('check_chat_semantic_completion_gates.py', 'complete_chat_semantic.py',
                'audit_chat_semantic_progress.py', 'review_chat_semantic_observer.py')}
    output = dict(passed=True, completed_at=now(), config_sha256=config['config_sha256'],
                  checks=checks, sources=sources, stored_evidence_changed=False, new_GPU_work=False,
                  model_quality_evidence=False, all_final_requirements_tested=not args.technical)
    if not args.technical:
        selection = read_json(RUN / 'selection.json')
        progress = read_json(RUN / 'progress_audit.json')
        verify_selection(selection, progress, config)
        for name, mutate in (
            ('selection_fabricated_passing_count', lambda r: r['summary']['S1']['new']['content']['primary'].update(joint_grammar_relevance_score2=r['summary']['S1']['new']['content']['primary']['joint_grammar_relevance_score2'] + 1)),
            ('selection_false_candidate', lambda r: r.update(eligible_candidate='S0')),
            ('selection_middle_point', lambda r: r.update(point='t2')),
            ('selection_false_improvement', lambda r: r.update(new_joint_CI_lower=r['new_joint_CI_lower'] + .125)),
            ('selection_dropped_regression', lambda r: r['summary']['S1'].pop('previous')),
        ):
            rejected(name, lambda r: verify_selection(r, progress, config), selection, mutate)
        checkpoint = read_json(RUN / 'S1/checkpoints.json')['t3']
        nll = read_json(RUN / 'NLL/S1/t3.json')
        fixed = nll_windows(config, tok)
        validate_nll(nll, config, checkpoint, fixed)
        for name, mutate in (
            ('NLL_target_ID', lambda r: r['targets'][0].update(id='fabricated')),
            ('NLL_byte_denominator', lambda r: r['targets'][0].update(body_bytes=r['targets'][0]['body_bytes'] + 1)),
            ('NLL_teacher_denominator', lambda r: r['targets'][0].update(body_teachers=r['targets'][0]['body_teachers'] + 1)),
            ('NLL_nonfinite', lambda r: r['targets'][0].update(body_NLL=float('nan'))),
            ('NLL_fabricated_mean', lambda r: r['summaries']['new_DEV'].update(body_mean_NLL=r['summaries']['new_DEV']['body_mean_NLL'] + 1.)),
        ):
            rejected(name, lambda r: validate_nll(r, config, checkpoint, fixed), nll, mutate)
        output.update(actual_selection=reference(RUN / 'selection.json'),
                      actual_ledger=reference(RUN / 'GPU_ledger.json'), actual_NLL=reference(RUN / 'NLL/S1/t3.json'))
    output['CPU_checks'] = len(checks)
    atomic_json(RUN / ('technical_gate_checks.json' if args.technical else 'completion_gate_checks.json'), output)
    print(str(len(checks)) + ' targeted CPU gate checks passed; stored evidence unchanged')


if __name__ == '__main__':
    main()
