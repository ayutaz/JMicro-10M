"""Independently audit every completed update, CPU stream and all saved states."""
import json
import math
import torch
from two_attribute_contract import RUN,CONFIG,BUDGET,preflight
from answer_learning_common import save,ref,bound,read_json,now
from jmicro.phase5 import equal_state
from phase6_performance import finite_state

def main():
    c,tok,rows=preflight();receipt=read_json(RUN/'learning_complete.json');assert receipt['config_sha256']==c['config_sha256']
    dry=read_json(bound(c['replay']));metrics=[json.loads(l) for l in (RUN/'model/metrics.jsonl').read_text().splitlines()]
    assert len(metrics)==dry['updates']==receipt['updates'];body_bytes=0
    pairs=dict(supervised_tokens='teachers',teachers_this_update='teachers_this_update',token_digest='token_digest',microbatches='microbatches',lr='lr',
        series_tokens='series_tokens',EOT_teachers='eot_teachers',valid_input_tokens='input_tokens',physical_input_tokens='physical_tokens',
        examples='examples',removed_turns='removed_turns')
    for i,(actual,expected) in enumerate(zip(metrics,dry['history'],strict=True),1):
        assert actual['update']==expected['update']==i
        assert all(actual[k]==expected[v] for k,v in pairs.items()),i
        body_bytes+=expected['body_bytes'];assert actual['body_bytes_seen']==body_bytes
        assert all(math.isfinite(v) for v in actual.values() if isinstance(v,(int,float)))
        assert actual['padding_input_tokens']==actual['physical_input_tokens']-actual['valid_input_tokens']
    final=torch.load(bound(receipt['checkpoint']),map_location='cpu',weights_only=False)
    initial=torch.load(bound(read_json(RUN/'initial.json')),map_location='cpu',weights_only=False)
    parent=torch.load(bound(c['parent']),map_location='cpu',weights_only=False)
    checks=dict(initial_model_exact_parent=equal_state(initial['model'],parent['model']),initial_Adam_empty=not initial['optimizer']['state'],
        initial_zero_counters=all(initial[k]==0 for k in ('update','tokens','supervised_tokens','body_bytes')),
        initial_digest_zero=initial['token_digest']=='00'*32,parent_lineage_exact=final['lineage']==initial['lineage'],
        full_native_model_keys=set(final['model'])==set(parent['model']),full_final_finite=finite_state(final),
        final_sampler_exact=final['sampler']==dry['sampler_terminal'],all_metrics_CPU_exact=True,
        final_counts_exact=all(final[k]==metrics[-1][v] for k,v in dict(update='update',tokens='valid_input_tokens',supervised_tokens='supervised_tokens',body_bytes='body_bytes_seen',token_digest='token_digest').items()),
        final_implementation_exact=final['implementation_sha256']==c['implementation'],final_spec_matches=final['spec']==initial['spec'])
    assert all(checks.values()),checks
    assert BUDGET<=final['supervised_tokens']<=BUDGET+31 and len(final['optimizer']['state'])==119
    assert final['lineage']['optimizer_policy']=='fresh' and final['lineage']['base_checkpoint']==c['parent']
    intermediate=[]
    for path in sorted((RUN/'model').glob('checkpoint-*.pt')):
        s=torch.load(path,map_location='cpu',weights_only=False);assert finite_state(s) and s['implementation_sha256']==c['implementation'] and s['lineage']==initial['lineage']
        assert s['token_digest']==metrics[s['update']-1]['token_digest']
        intermediate.append(dict(checkpoint=ref(path),update=s['update'],teachers=s['supervised_tokens'],full_model_and_Adam_finite=True))
        del s
    save(RUN/'learning_audit.json',dict(created_at=now(),source=ref(__file__),config=ref(CONFIG),checks=checks,all_updates=len(metrics),
        checkpoints=intermediate,Adam_states=len(final['optimizer']['state']),model_state_tensors=len(final['model']),
        parameters=sum(v.numel() for k,v in final['model'].items() if k!='lm_head.weight'),
        final_teachers=final['supervised_tokens'],final_token_digest=final['token_digest'],metrics=ref(RUN/'model/metrics.jsonl'),
        replay=c['replay'],result=ref(RUN/'learning_complete.json'),quality_evidence=False,protected_TEST_used=False))
    print('All completed updates, CPU source clock, initial weights/fresh Adam,119 Adam states and every saved checkpoint verified')

if __name__=='__main__':main()
