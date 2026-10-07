import sys,json
from pathlib import Path
sys.path[:0]=['src','scripts']
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from jmicro.tokenizer import Tokenizer
from review_base_output_mixture import CPU_reader,metadata_equal
from base_output_mixture_model import ARMS
p=ROOT/'configs/phase6/base_output_mixture_probe.json'
c=read_json(p)
parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
tok=Tokenizer(ROOT/c['tokenizer'])
proof=[]
for arm in ARMS:
    cp=ROOT/'reports/phase6/base-output-mixture-probe-20261007'/f'{arm}-continuous.pt'
    state=torch.load(cp,map_location='cpu',weights_only=False)
    b=c['source_binding']
    sampler=OriginalTrainCorpusSampler(b['pool'],b['manifest_sha256'],tok,c['goals'],42)
    expected=dict(parent=c['parent'],config_sha256=sha256(p),weights_role='verification_only')
    assert state['binding']==expected and state['counters']['update']==4
    trainer=CPU_reader(parent,sampler,expected,arm,state['spec'])
    trainer.validate_committed(state)
    converted=json.loads(json.dumps(state['spec']))
    assert metadata_equal(state['spec'],converted)
    converted['optimizer_recipe']['betas'][1]=.998
    assert not metadata_equal(state['spec'],converted)
    proof.append(dict(arm=arm,checkpoint_sha256=sha256(cp),actual_CUDA_update=4,allstate_CPU_read_validated=True,changed_beta_refused=True))
write_json(ROOT/'reports/phase6/base_output_mixture_CPU_reader_proof.json',dict(created_at=now(),source_sha256=sha256(Path(__file__)),config_sha256=sha256(p),actual_probe_states=proof,GPU_seconds=0,optimizer_updates=0,scientific_teacher_tokens=0,limitations='Read actual saved CUDA4 state on CPU; no CPU step, no new GPU training or quality claim.'))
print(json.dumps(proof))