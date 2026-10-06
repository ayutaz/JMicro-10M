"""Repair fresh-parent bootstrap only; preserve frozen recipe and completed arm."""
import copy
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
from jmicro.curriculum_strategy import StrategyTrainer
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
import run_curriculum_strategy as runner
from phase6_performance import alive


class BootstrapStrategyTrainer(StrategyTrainer):
    def __init__(self,parent,*args,**kwargs):
        # PilotTrainer briefly validates a one-update dummy schedule before
        # PackingTrainer installs its exact-teacher schedule. Warmup is applied
        # by StrategyTrainer, so omit it ONLY during that zero-update bootstrap.
        repair=parent['update']==0 and parent['spec']['warmup']>=1
        actual_spec=copy.deepcopy(parent['spec'])
        if repair:
            parent=dict(parent,spec=dict(parent['spec'],warmup=0))
        super().__init__(parent,*args,**kwargs)
        if repair:
            self.spec['warmup']=actual_spec['warmup']
            self.lineage['parent_spec']=actual_spec
            self.lineage['bootstrap_repair']=dict(source_sha256=sha256(Path(__file__)),
                scope='dummy constructor validation only; actual200-update warmup and teacher decay unchanged')


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    c=runner.load_config();previous=read_json(runner.RUN/'job.json')
    assert previous['status']=='failed' and not alive(previous)
    assert previous['error']=="ValueError('Invalid warmup or update budget')"
    record=dict(created_at=now(),previous_job=previous,frozen_config_sha256=sha256(runner.CONFIG),
        repair_source_sha256=sha256(Path(__file__)),CPU_tests='tests/test_strategy_bootstrap.py',
        decision='Keep continuation100M+evaluation, initial-fresh checkpoint and all frozen settings. Repair zero-update dummy constructor; no retraining of completed arm.')
    write_json(runner.RUN/'bootstrap-repair.json',record)
    runner.StrategyTrainer=BootstrapStrategyTrainer
    runner.run()
