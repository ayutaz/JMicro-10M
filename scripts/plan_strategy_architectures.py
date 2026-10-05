"""CPU parameter counts for optional10M proposals; no learning or quality claim."""
import copy
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,now
from jmicro.model import JMicroModel


def plan():
    base=read_json(ROOT/'reports/phase5/candidate_configs.json')['100m-no-qknorm']['model_config']
    settings={'current':{},'fewer_layers_more_FFN':dict(num_hidden_layers=9,intermediate_size=1040),
        'wider_fewer_layers':dict(hidden_size=384,num_attention_heads=6,num_key_value_heads=3,num_hidden_layers=6,intermediate_size=832)}
    candidates={}
    for name,changes in settings.items():
        config=copy.deepcopy(base);config.update(changes)
        model=JMicroModel(config);count=sum(p.numel() for p in model.parameters())
        assert 9900000<=count<=10100000
        candidates[name]=dict(model_config=config,parameters=count,quality='not evaluated; CPU parameter count only')
        del model
    report=dict(status='proposal_not_launch_contract',candidates=candidates,
        comparison='Only if material evidence supports: all three fresh, same material/Tokenizer/seed and teacher budget, same schedule; CUDA stable batch/resume per new configuration; compare quality and GPU time',
        proposed_teacher_tokens_per_candidate=300000000,
        stop='At most two new architectures; no automatic experiment or claim that10M capacity is inadequate',created_at=now())
    write_json(ROOT/'reports/phase6/strategy_architecture_proposal.json',report)
    print({name:detail['parameters'] for name,detail in candidates.items()})


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);plan()
