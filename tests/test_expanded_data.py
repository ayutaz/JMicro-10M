from concurrent.futures import ThreadPoolExecutor
import numpy as np
from datasketch import MinHash, MinHashLSH

from jmicro.expanded_data import Union, bounded_map, permutations_for, signature


def test_fast_signature_matches_scalar_hash_and_permutation_reference():
    text = "あいうえお日本語の文章。ABC😀123"
    hashes = []
    for i in range(len(text)-4):
        value = 0
        for char in text[i:i+5]:
            value = (value*1000003+ord(char)+1) & ((1 << 64)-1)
        value ^= value >> 33
        value = (value*0xff51afd7ed558ccd) & ((1 << 64)-1)
        value ^= value >> 33
        hashes.append(value & 0xffffffff)
    a, b = permutations_for(42)
    expected = np.array([min((((h*int(x)+int(y)) & ((1 << 64)-1)) % ((1 << 61)-1)) & 0xffffffff
                              for h in set(hashes)) for x,y in zip(a,b)], dtype=np.uint64)
    np.testing.assert_array_equal(signature(text), expected)
    np.testing.assert_array_equal(signature(text), signature(text))
    assert not np.array_equal(signature(text), signature(text, 43))


def test_near_candidate_and_cluster_transitivity():
    text = "これは日本語の文章です。毎日いろいろなことを学びます。"*10
    lsh = MinHashLSH(num_perm=128, params=(32,4))
    def mh(value):
        return MinHash(num_perm=128, seed=42, hashvalues=signature(value),
                       permutations=permutations_for(42), scheme="legacy")
    lsh.insert(0, mh(text))
    assert 0 in lsh.query(mh(text+"追加文章です。"))
    groups = Union()
    for _ in range(4):
        groups.add()
    groups.union(3,2)
    groups.union(1,0)
    groups.union(2,1)
    assert [groups.find(i) for i in range(4)] == [0,0,0,0]


def test_bounded_map_preserves_record_order():
    with ThreadPoolExecutor(max_workers=2) as executor:
        assert list(bounded_map(executor, abs, iter([-3,-1,-2]), pending=2)) == [3,1,2]
