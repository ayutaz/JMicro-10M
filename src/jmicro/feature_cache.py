"""Bounded memoization of immutable corpus character-shingle sets."""
from collections import OrderedDict
import sys


class FeatureCache:
    """Cache pure feature loaders by entry count and conservative charged bytes.

    This changes no candidate or similarity calculation. Oversize values are
    returned without retention, so resource limits never remove corpus records.
    Charged bytes bound retained Python objects, not total process RSS.
    """

    def __init__(self, load, max_entries=8192, max_bytes=2 * 1024**3):
        if max_entries < 1 or max_bytes < 512:
            raise ValueError("Positive entries and at least512 charged bytes are required")
        self.load = load
        self.max_entries = max_entries
        self.max_bytes = max_bytes
        self.values = OrderedDict()
        self.charged_bytes = self.peak_bytes = 512
        self.hits = self.misses = self.evictions = 0

    def __call__(self, key):
        if key in self.values:
            self.hits += 1
            self.values.move_to_end(key)
            return self.values[key][0]
        self.misses += 1
        value = self.load(key)
        weight = sys.getsizeof(value) + sum(sys.getsizeof(item) for item in value) + 256
        if weight + 512 > self.max_bytes:
            return value
        while self.values and (len(self.values) >= self.max_entries or
                               self.charged_bytes + weight > self.max_bytes):
            _, (_, removed_weight) = self.values.popitem(last=False)
            self.charged_bytes -= removed_weight
            self.evictions += 1
        self.values[key] = value, weight
        self.charged_bytes += weight
        self.peak_bytes = max(self.peak_bytes, self.charged_bytes)
        return value

    def info(self):
        return dict(hits=self.hits, misses=self.misses, evictions=self.evictions,
                    entries=len(self.values), charged_bytes=self.charged_bytes,
                    peak_charged_bytes=self.peak_bytes, max_entries=self.max_entries,
                    max_charged_bytes=self.max_bytes)
