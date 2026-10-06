import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location('judge', Path(__file__).parents[1]/'scripts/base_source_semantic_judge.py')
judge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(judge)


def test_never_repair_format_or_accept_boolean_and_missing_scores():
    assert judge.parse_prediction('```json\n{}\n```') is None
    assert judge.parse_prediction('{"grammar":true,"coherence":2,"complete":2,"boilerplate":0,"reason":"x"}') is None
    assert judge.parse_prediction('{"grammar":2,"coherence":2,"complete":2,"reason":"x"}') is None


def test_false_positive_and_reject_all_cannot_qualify():
    good = dict(grammar=2, coherence=2, complete=2, boilerplate=0, reason='x')
    bad = dict(good, complete=0)
    predictions = [{'parsed':good}, {'parsed':good}, {'parsed':bad}, {'parsed':None}]
    gold = [{'usable':True}, {'usable':False}, {'usable':True}, {'usable':False}]
    stats = judge.agreement(predictions, gold, list(range(4)))
    assert (stats['true_positive'], stats['false_positive'], stats['false_negative'], stats['true_negative']) == (1, 1, 1, 1)
    assert stats['precision'] == stats['recall'] == .5
    assert stats['format_errors'] == 1
    contract = dict(minimum_accepted=1, minimum_precision=.9, minimum_recall=.5, maximum_format_errors=0)
    assert not judge.meets_gate(stats, contract)
    empty = judge.agreement([{'parsed':bad} for _ in gold], gold, list(range(4)))
    assert empty['precision'] is None and not judge.meets_gate(empty, contract)
