"""Own provenance for the fixed query intervention; original trainer stays frozen."""
from pathlib import Path
from jmicro.experiment import sha256
from original_web_retention_trainer import OriginalWebRetentionTrainer


class QueryBalancedTrainer(OriginalWebRetentionTrainer):
    def __init__(self, parent, pool, original_web, positive, goals, binding,
                 device='cuda', context=1024, batch=32):
        super().__init__(parent, pool, original_web, positive, goals, binding, device, context, batch)
        self.spec.update(research_kind='comparison_query_balance_same100M',
                         query_trainer_sha256=sha256(Path(__file__)))
        self.lineage.update(kind='original-Web-cursor-retained-query-balanced-fork',
            source_sampler_policy='Same original Web cursor and fresh seed42 short streams. Only172 comparison train bodies change requested property and target; same2048 IDs/order/category counts. Ordinary body+EOS CE weight1.')
