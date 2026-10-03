from collections import Counter

from jmicro.feature_cache import FeatureCache


def test_bounded_cache_preserves_loader_results_and_reuses_hot_group():
    loads = Counter()

    def load(key):
        loads[key] += 1
        return {f"shingle-{key}".encode()}

    cache = FeatureCache(load, max_entries=8, max_bytes=8192)
    for _ in range(3):
        for key in range(8):
            assert cache(key) == {f"shingle-{key}".encode()}
    assert sum(loads.values()) == 8
    assert cache.info()["hits"] == 16


def test_budget_and_oversize_values_do_not_change_features():
    def load(key):
        return {b"x" * (10000 if key == 99 else 20) + str(key).encode()}

    cache = FeatureCache(load, max_entries=8192, max_bytes=2048)
    for key in list(range(20)) + [99, 99] + list(range(20)):
        assert cache(key) == load(key)
        assert cache.info()["charged_bytes"] <= 2048
    assert cache.info()["evictions"] > 0
    assert cache.info()["peak_charged_bytes"] <= 2048
