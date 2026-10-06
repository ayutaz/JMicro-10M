"""Content aliases must not become independent semantic CI clusters."""
from pathlib import Path
import sys

import pytest

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from review_teacher_semantic_signal import exact_content_families


def pair(family, choices=('yes', 'no'), labels=(0, 1)):
    return [dict(id=f'{family}-{i}', family=family, context=context,
        choices=list(choices), label=labels[i], category='negation')
        for i, context in enumerate(('affirmative context', 'negative context'))]


def test_alias_ids_and_choice_order_do_not_add_clusters():
    rows = pair('original') + pair('alias', ('no', 'yes'), (1, 0))
    groups, keys, aliases = exact_content_families(rows)
    assert len(groups) == 2
    assert len(rows) == 4  # Keep every historical score and example weight.
    assert keys['original'] == keys['alias']
    assert list(aliases.values()) == [['original', 'alias']]
    changed = pair('different', labels=(1, 0))
    assert len(exact_content_families(rows + changed)[2]) == 2


def test_missing_contrast_context_is_rejected():
    with pytest.raises(ValueError, match='two distinct contexts'):
        exact_content_families(pair('incomplete')[:1])
