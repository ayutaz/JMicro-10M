"""Read-only final Adam clocks, scheduler and complete RNG state audit."""
import json
import torch
from two_attribute_contract import RUN,CONFIG,preflight
from answer_learning_common import save,ref,bound,read_json,now
from jmicro.phase5 import equal_state

c,_,_=preflight();initial=torch.load(bound(read_json(RUN/'initial.json')),map_location='cpu',weights_only=False)
end=torch.load(bound(read_json(RUN/'learning_complete.json')['checkpoint']),map_location='cpu',weights_only=False)
last=json.loads((RUN/'model/metrics.jsonl').read_text().splitlines()[-1]);steps={str(k):int(v['step']) for k,v in end['optimizer']['state'].items()}
checks=dict(all119_Adam_clocks=all(v==483 for v in steps.values()) and len(steps)==119,
    scheduler_epoch=end['scheduler']['last_epoch']==483,scheduler_calls=end['scheduler']['_step_count']==484,
    optimizer_LR=all(g['lr']==last['lr'] for g in end['optimizer']['param_groups']),
    scheduler_LR=all(v==last['lr'] for v in end['scheduler']['_last_lr']),
    complete_RNG_exact_initial=equal_state(end['rng'],initial['rng']),
    trained_weights_changed=not equal_state(end['model'],initial['model']),
    tied_embedding=end['model']['lm_head.weight'].data_ptr()==end['model']['model.embed_tokens.weight'].data_ptr())
assert all(checks.values()),checks
target=RUN/'final_state_extended_audit.json';assert not target.exists()
save(target,dict(created_at=now(),source=ref(__file__),config=ref(CONFIG),checks=checks,Adam_clocks=steps,
    initial=ref(RUN/'initial.json'),final=ref(RUN/'learning_complete.json'),prior_full_audit=ref(RUN/'learning_audit.json'),
    full_rng_keys=sorted(end['rng']),scheduler=end['scheduler'],quality_evidence=False))
print('Full RNG,119 Adam clocks, scheduler, learning rate and tied trained weights verified')
