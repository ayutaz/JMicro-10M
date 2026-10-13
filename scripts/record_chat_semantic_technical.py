"""Record actual prelearning gates and the nonnumerical review metadata adapter."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, now
from jmicro.training import atomic_json
from chat_semantic_contract import RUN, preflight, reference
from complete_chat_semantic import verify_technical_gates
from phase6_performance import alive


def main():
    config, _, _ = preflight(ROOT / 'configs/phase7/chat-semantic-diversity-20261013.json')
    gates = verify_technical_gates(config)
    ledger = read_json(RUN / 'GPU_ledger.json')
    entries = ledger['entries'][:3]
    assert [row['category'] for row in entries] == ['probe', 'resume', 'evaluation']
    assert all(row['status'] == 'complete' and not alive(row) for row in entries)
    path = RUN / 'technical_milestone.json'
    report = dict(passed=True, recorded_at=now(), config_sha256=config['config_sha256'], gates=gates,
                  ledger_entries=entries, GPU_seconds=sum(row['charged_seconds'] for row in entries),
                  verification_optimizer_updates=25, candidate_learning_updates_in_gates=0,
                  historical_S0_gate_reuse_is_not_new_learning=True, quality_evidence=False,
                  required_evaluation_still_pending=True)
    if path.exists():
        prior = read_json(path)
        assert prior['ledger_entries'] == entries and prior['config_sha256'] == config['config_sha256']
    else:
        atomic_json(path, report)
    atomic_json(RUN / 'review_protocol_adapter.json', dict(recorded_at=now(),
                frozen_config_sha256=config['config_sha256'], numerical_sources_changed=False,
                raw_results_changed=False, histories_or_scores_changed=False,
                reason='Shared legacy reviewer requires requested_five_steps_complete=False; new frozen generator emits requested_six_steps_complete=False. Add false alias only in CPU memory.',
                observers={name: reference(ROOT / 'scripts' / name) for name in
                           ('review_chat_semantic_observer.py', 'compare_chat_semantic_observed.py')}))
    print('Actual25 verification updates and all-state resume audited; numerical contract unchanged')


if __name__ == '__main__':
    main()
