"""Same proven sampler; only new D0/D1 TRAIN consumed, no model/GPU."""
from pathlib import Path
import json
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,now
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from dry_run_chat_improvement import consume
from jmicro.chat_generalization_curriculum import WEIGHTS
from prepare_chat_generalization_train import DATA,D0,RUN


def main():
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    path=DATA/('train.jsonl' if (DATA/'manifest.json').exists() else 'candidate.train.jsonl')
    a=consume(D0/'train.jsonl',tok);b=consume(path,tok)
    countdiff=abs(b['updates']/a['updates']-1)
    decaydiff=abs(b['decay_coefficient']/a['decay_coefficient']-1)
    tv=sum(abs(x-y) for x,y in zip(a['length_bin_fractions'],b['length_bin_fractions']))/2
    eotdiff=abs(b['EOT_fraction']-a['EOT_fraction'])
    mixture=max(abs(b['consumed_teacher_fractions'][k]-v) for k,v in WEIGHTS.items())
    checks=dict(updates_relative_difference=countdiff<=.05,decay_relative_difference=decaydiff<=.001,
        actual_teacher_mixture=mixture<=.01,actual_length_TV=tv<=.10,actual_EOT_match=eotdiff<=.01,
        final_whole_target_overshoot=all(0<=x['final_overshoot']<=64 for x in (a,b)),
        target_exposure_at_most_three=all(x['max_target_exposures']<=3 for x in (a,b)))
    for name,arm in (('D0',a),('D1',b)):atomic_json(RUN/(name+'_dry_run.json'),arm)
    result=dict(created_at=now(),status='passed' if all(checks.values()) else 'redesign_required',checks=checks,
        update_relative_difference=countdiff,decay_relative_difference=decaydiff,length_TV=tv,
        EOT_absolute_difference=eotdiff,mixture_max_absolute_difference=mixture,
        D0={k:v for k,v in a.items() if k not in ('rows','sampler_terminal')},
        D1={k:v for k,v in b.items() if k not in ('rows','sampler_terminal')},
        GPU_learning_tokens=0,CPU_only=True,quality_evidence=False,new_DEV_used=False)
    atomic_json(RUN/'consumption_dry_run.json',result)
    print(json.dumps(dict(status=result['status'],checks=checks,update_difference=countdiff,
        length_TV=tv,EOT_difference=eotdiff),ensure_ascii=False))


if __name__=='__main__':main()
