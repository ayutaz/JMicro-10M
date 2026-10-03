"""Locate the first FP32 full/cache divergence for the fixed learned input."""
from pathlib import Path
import argparse
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.model import JMicroModel,RMSNorm,Attention,Block,MLP
from jmicro.training import implementation_hashes


def trace(export,output):
    torch.set_num_threads(2)
    requests=read_json(export/'native-float/request.json')
    request=next(row for row in requests['runs'] if row['name']=='context1024_prefill')
    ids=torch.tensor([sum(request['chunks'],[])])
    assert ids.shape==(1,1024)
    model=JMicroModel.load(export/'torch').eval()
    parameters={name:value.clone() for name,value in model.state_dict().items()}
    captures={'full':{},'cache':{}}
    mode=['full']
    handles=[]
    def capture(name):
        def hook(module,inputs,value):
            value=value[0] if isinstance(value,tuple) else value
            assert isinstance(value,torch.Tensor) and value.ndim==3
            captures[mode[0]].setdefault(name,[]).append(value.detach().clone())
        return hook
    for name,module in model.named_modules():
        if isinstance(module,(torch.nn.Linear,torch.nn.Embedding,RMSNorm,Attention,Block,MLP)):
            handles.append(module.register_forward_hook(capture(name)))
    with torch.inference_mode():
        full=model(ids).logits
        mode[0]='cache';cache=None;parts=[];position=0
        for width in (511,1,512):
            value=model(ids[:,position:position+width],cache=cache,use_cache=True)
            parts.append(value.logits);cache=value.cache;position+=width
        resumed=torch.cat(parts,1)
    for handle in handles:handle.remove()
    tolerance=read_json(ROOT/'configs/evaluation/protocol.json')['numeric_tolerances']['fp32_reference_logits']
    stages=[]
    for name,parts in captures['full'].items():
        expected=torch.cat(parts,1)
        actual=torch.cat(captures['cache'][name],1)
        assert actual.shape==expected.shape
        difference=(actual-expected).abs()
        stages.append({'module':name,'shape':list(expected.shape),'exact':torch.equal(actual,expected),
            'max_abs_error':float(difference.max()),'mean_abs_error':float(difference.mean()),
            'outside_frozen_tolerance':int((difference>tolerance['atol']+tolerance['rtol']*expected.abs()).sum())})
    assert all(torch.equal(parameters[name],value) for name,value in model.state_dict().items())
    result={'status':'diagnosis_complete','export':str(export),'native_requests_sha256':sha256(export/'native-float/request.json'),
        'checkpoint_binding':read_json(export/'binding.json'),'implementation':implementation_hashes(),
        'tracer_sha256':sha256(Path(__file__)),'tolerance_unchanged':tolerance,'stages':stages,
        'first_nonexact_stage':next(row for row in stages if not row['exact']),
        'first_outside_tolerance_stage':next((row for row in stages if row['outside_frozen_tolerance']),None),
        'final_logits_max_abs_error':float((full-resumed).abs().max()),'weights_unchanged':True,
        'scope':'One fixed FP32 CPU full1024 versus cache511+1+512, all module outputs; no environment sweep or training',
        'completed_at':now()}
    write_json(output,result)
    print(result['first_nonexact_stage']['module'],result['final_logits_max_abs_error'],flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--export',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();trace(args.export.resolve(),args.output.resolve())
