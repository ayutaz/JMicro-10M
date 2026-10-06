import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from prepare_source_condition_pairs import extract_pair


def test_original_prefix_outcome_spans_preserved_without_invented_negatives():
    text = '線の描き方を説明します。先端を尖らせれば細い線が描けます。一方、丸くすれば柔らかい線が描けます。'
    pair = extract_pair(text)
    assert pair is not None and len(pair['branches']) == 2
    for branch in pair['branches']:
        assert branch['prefix'] == text[:branch['cut']]
        assert branch['outcome'] == text[branch['cut']:branch['end']]
        assert (branch['prefix'] + branch['outcome']) == text[:branch['end']]
    assert pair['choices'] == ['細い線が描けます。','柔らかい線が描けます。']


def test_no_counterfactual_rewriting_or_incomplete_outcomes():
    assert extract_pair('先端を尖らせれば細い線が描けます。') is None
    assert extract_pair('先端を尖らせれば細い線が描けますし、丸くすれば柔らかい線が描けます。') is None
    assert extract_pair('先端を尖らせれば細い線が描けます。一方、丸くすれば') is None
    assert extract_pair('先端を尖らせれば細い線が描けます。丸くすれば柔らかい線が描けます。') is None
