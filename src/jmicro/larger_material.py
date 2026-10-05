"""Exact1:4 source/length/editorial-unit grouping for500M versus2B."""
from jmicro.nested_material_v2 import UnitGroups


class FourGroups(UnitGroups):
    def add(self, record):
        key = (record["source"], record["body_tokens"], record["unit_kind"])
        bucket = self.pending[key]
        bucket.append(record)
        if len(bucket) < 4:
            return None
        group = list(bucket)
        bucket.clear()
        return group, self.rng.randrange(4)
