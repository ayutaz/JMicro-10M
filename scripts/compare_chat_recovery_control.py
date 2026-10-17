"""Read-only numerical reproducibility check of new C0 versus historical C1."""
import json
import torch
from chat_recovery_contract import ROOT,RUN,CONFIG,preflight
from answer_learning_common import save,read_json,bound,ref,now
from jmicro.phase5 import equal_state


def main():
    target=RUN/'C0/historical_numeric_comparison.json';assert not target.exists();c,_,_=preflight(False)
    audit=read_json(RUN/'C0/training_audit.json');assert audit['passed'] and audit['config']==ref(CONFIG)
    old=read_json(ROOT/'reports/phase7/chat-answer-learning-20261017/curriculum-main-resource-v2/C1/result.json')
    current=read_json(RUN/'C0/result.json')
    a=torch.load(bound(old['checkpoint']),map_location='cpu',weights_only=False)
    b=torch.load(bound(current['checkpoint']),map_location='cpu',weights_only=False)
    checks={k:equal_state(a[k],b[k]) for k in set(a)&set(b)}
    old_history=[json.loads(line) for line in (ROOT/'reports/phase7/chat-answer-learning-20261017/curriculum-main-resource-v2/C1/metrics.jsonl').read_text().splitlines()]
    new_history=[json.loads(line) for line in (RUN/'C0/metrics.jsonl').read_text().splitlines()]
    assert len(old_history)==len(new_history)==1929
    clock_fields={'seconds','data_wait_seconds','teacher_tokens_per_second'}
    history_checks={k:all(x[k]==y[k] for x,y in zip(old_history,new_history,strict=True)) for k in old_history[0] if k not in clock_fields}
    save(target,dict(created_at=now(),config=ref(CONFIG),source=ref(__file__),historical_checkpoint=old['checkpoint'],new_checkpoint=current['checkpoint'],
        all_common_saved_fields_exact=checks,historical_only_fields=sorted(set(a)-set(b)),new_only_fields=sorted(set(b)-set(a)),
        every_non_time_history_field_exact=history_checks,history_clock_fields_excluded=sorted(clock_fields),
        independently_fresh_training_audit=ref(RUN/'C0/training_audit.json'),
        model_Adam_scheduler_RNG_exact=all(checks[k] for k in ('model','optimizer','scheduler','rng')),
        no_checkpoint_modified=True,no_GPU_or_generation=True,quality_evidence=False,not_an_independent_Base_pipeline=True))
    print(json.dumps(read_json(target),ensure_ascii=False))


if __name__=='__main__':main()
