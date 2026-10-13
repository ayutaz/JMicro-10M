"""Map literal reviewer-provided indices to raw-bound keys; never generate scores."""
import argparse
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import read_json, sha256
from chat_semantic_contract import RUN


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('evaluation', type=Path)
    parser.add_argument('--partial', action='store_true')
    args = parser.parse_args()
    path = args.evaluation.resolve()
    assert path.is_relative_to(RUN / 'evaluation')
    packet = read_json(path.with_name('packet.json'))
    assert packet['evaluation_sha256'] == sha256(path)
    source = path.with_name('authored_indices.tsv')
    entries = {}
    for line in source.read_text().splitlines():
        if not line.strip():
            continue
        index, grammar, relevance, context, rationale = line.split('\t', 4)
        index = int(index)
        assert index not in entries and 0 <= index < len(packet['pending'])
        assert all(int(value) in (0, 1, 2) for value in (grammar, relevance, context))
        assert len(rationale.strip()) >= 12
        entries[index] = (grammar, relevance, context, rationale)
    if args.partial:
        print(f'{len(entries)} literal authored judgments; {len(packet["pending"]) - len(entries)} remain')
        return
    assert set(entries) == set(range(len(packet['pending']))), 'All pending judgments required'
    output = path.with_name('authored_scores.tsv')
    text = ''.join('\t'.join((packet['pending'][index]['key'], *entries[index])) + '\n'
                   for index in range(len(packet['pending'])))
    if output.exists():
        assert output.read_text() == text, 'Existing authored output retained'
    else:
        output.write_text(text)
    print(f'Bound {len(entries)} literal authored judgments; no ratings inferred')


if __name__ == '__main__':
    main()
