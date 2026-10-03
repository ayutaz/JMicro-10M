"""Use bounded pure memoization with the unchanged independent serial auditor."""
from jmicro.corpus_state import write_json
from jmicro.feature_cache import FeatureCache


def audit_with_cache(auditor, config, raw, output, workers):
    """Replace only its feature decorator and restore it after every outcome.

    All source reconstruction, candidate loops, Jaccard scores, component/split
    checks and full token/byte round trips are executed by the original auditor.
    """
    original_decorator = auditor.lru_cache
    caches = []

    def bounded_decorator(*, maxsize):
        if maxsize != 4096:
            raise ValueError("The frozen auditor feature decorator changed")

        def decorate(load):
            cache = FeatureCache(load)
            caches.append(cache)
            return cache

        return decorate

    auditor.lru_cache = bounded_decorator
    try:
        result = auditor.audit(config, raw, output, workers)
    finally:
        auditor.lru_cache = original_decorator
    if result["status"] != "passed" or len(caches) != 1:
        raise ValueError("Independent auditor did not complete its feature stage")
    write_json(output / "audit_cache_metrics.json", {
        "status": "passed_with_unchanged_serial_audit_checks",
        "feature_cache": caches[0].info(),
        "scope": "Pure feature memoization only; no candidate or acceptance changes",
    })
    return result
