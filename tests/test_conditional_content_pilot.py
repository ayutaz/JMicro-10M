import sys
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from prepare_conditional_content_pilot import select_documents


def test_fixed_source_quotas_no_duplicates_and_length_scope():
    index = SimpleNamespace(lengths=np.array([63, 64, 100, 512, 513] * 3),
                            sources=np.repeat(np.arange(3), 5))
    picked = select_documents(index, count=3, seed=17)
    assert picked == select_documents(index, count=3, seed=17)
    ids = [i for docs in picked.values() for i in docs]
    assert len(ids) == len(set(ids)) == 9
    assert all(64 <= index.lengths[i] <= 512 for i in ids)
    assert all(len(docs) == 3 and all(index.sources[i] == tag for i in docs)
               for tag, docs in enumerate(picked.values()))


def test_insufficient_source_and_expired_budget_fail_without_reroll():
    index = SimpleNamespace(lengths=np.array([100, 100]), sources=np.array([0, 1]))
    with pytest.raises(ValueError, match='Insufficient'): select_documents(index, count=1, attempts=100)
    with pytest.raises(TimeoutError): select_documents(index, count=1, deadline=0)
