"""One fixed FP32 CUDA reference diagnosis using all original native logits."""
from pathlib import Path
import argparse
import os
import sys
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import torch
from torch.nn.attention import sdpa_kernel,SDPBackend
from transformers import AutoModelForCausalLM
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.training import gpu_lock,seed_all,implementation_hashes
from verify_nonorm_export import compare
from phase6_performance import identity


def verify(export,output):
    torch.set_num_threads(2)
    previous=read_json(export/'nonorm_export_parity_report.json')
    tolerance=previous['tolerance']
    request=read_json(export/'native-float/request.json')
    binding={'cpu_export_report_sha256':sha256(export/'nonorm_export_parity_report.json'),
        'native_requests_sha256':sha256(export/'native-float/request.json'),
        'implementation':implementation_hashes(),'verifier_sha256':sha256(Path(__file__)),
        'reference':'CUDA FP32 parameters/activations, math SDPA; TF32 off. Original CPU failures remain unresolved evidence.'}
    report={'status':'running','binding':binding,'tolerance':tolerance,'comparisons':{},'started_at':now(),**identity()}
    write_json(output,report)
    with gpu_lock('cuda'),sdpa_kernel([SDPBackend.MATH]):
        seed_all(42)
        torch.cuda.set_per_process_memory_fraction(.94)
        model=JMicroModel.load(export/'torch').eval().to('cuda')
        hf=AutoModelForCausalLM.from_pretrained(export/'hf',local_files_only=True,attn_implementation='eager').eval().to('cuda')
        assert all(parameter.dtype==torch.float32 for parameter in model.parameters())
        assert not torch.backends.cuda.matmul.allow_tf32
        with torch.inference_mode():
            for request_row in request['runs']:
                if not request_row['name'].endswith('_prefill'):continue
                name=request_row['name'].removesuffix('_prefill')
                ids=sum(request_row['chunks'],[])
                tensor=torch.tensor([ids],device='cuda')
                expected=model(tensor).logits
                report['comparisons'][name+'_hf_full']=compare(hf(tensor).logits,expected,tolerance)
                split=min(11,len(ids)-2) if name=='short' else 511
                own_cache=hf_cache=None
                own_parts=[];hf_parts=[];position=0
                for width in (split,1,len(ids)-split-1):
                    chunk=tensor[:,position:position+width]
                    own=model(chunk,cache=own_cache,use_cache=True)
                    ref=hf(chunk,past_key_values=hf_cache,use_cache=True)
                    own_cache=own.cache;hf_cache=ref.past_key_values
                    own_parts.append(own.logits);hf_parts.append(ref.logits);position+=width
                report['comparisons'][name+'_torch_cache']=compare(torch.cat(own_parts,1),expected,tolerance)
                report['comparisons'][name+'_hf_cache']=compare(torch.cat(hf_parts,1),expected,tolerance)
                arrays=[]
                for mode in ('prefill','cache'):
                    path=export/f'{name}_{mode}.f32'
                    array=np.fromfile(path,dtype='<f4').reshape(1,len(ids),4096)
                    arrays.append(array)
                    report['comparisons'][name+'_gguf_'+mode]=compare(torch.from_numpy(array).to('cuda'),expected,tolerance)
                report['comparisons'][name+'_gguf_cache_vs_prefill']=compare(arrays[1],arrays[0],tolerance)
    report.update(status='passed' if all(row['passed'] for row in report['comparisons'].values()) else 'failed',completed_at=now(),training_performed=False)
    write_json(output,report)
    print(report['status'],flush=True)
    assert report['status']=='passed'


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--export',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();verify(args.export.resolve(),args.output.resolve())
