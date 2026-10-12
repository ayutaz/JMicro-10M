"""Reconstruct frozen C1 consumed family shares from its exact terminal cursor."""
from collections import Counter
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from chat_improvement_contract import RUN,preflight,B


def main():
    c,_,arms=preflight(ROOT/'configs/phase7/chat-improvement-20261012.json')
    dry=read_json(RUN/'C1_dry_run.json');state=dry['sampler_terminal'];rows=arms['C1']
    assert state['binding']==c['arms']['C1']['sampler_binding'] and len(rows)==state['windows']==39655
    assert all(len(r['target_message_indices'])==1 for r in rows)
    exposure=np.full(len(rows),state['epoch'],dtype=np.int64)
    order=np.random.default_rng(np.random.SeedSequence([42,state['epoch']])).permutation(len(rows))
    exposure[order[:state['position']]]+=1
    family=Counter();category=Counter()
    for r,n in zip(rows,exposure,strict=True):
        family[r['family']]+=int(n)*r['teacher_tokens'];category[r['category']]+=int(n)*r['teacher_tokens']
    assert sum(family.values())==sum(category.values())==dry['Assistant_teachers']==B
    assert int(exposure.max())==3 and sum(exposure)==dry['EOT_teachers']
    shares={k:v/B for k,v in family.items()};maximum=max(shares.values());assert maximum<=.05
    report=dict(passed=True,config_sha256=c['config_sha256'],source_sha256=sha256(Path(__file__)),
        terminal_binding=state['binding'],actual_consumed_teacher_family_fractions=shares,max_family_fraction=maximum,
        actual_teachers=B,maximum_target_exposures=int(exposure.max()),exact_epoch_order_reconstruction=True,
        categories=dict(category),quality_evidence=False,completed_at=now())
    atomic_json(RUN/'actual_family_consumption.json',report);print(json.dumps(dict(passed=True,max_family_fraction=maximum)))

if __name__=='__main__':main()
