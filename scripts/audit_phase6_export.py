"""Inspect learned weights and exercise the precision-bound real inference CLI."""
from pathlib import Path
import argparse
import json
import subprocess
import sys
import time

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import gguf
import numpy as np
import torch
from safetensors.torch import load_file
from jmicro.experiment import ROOT,read_json,sha256,write_json,now
from jmicro.inference_precision import PROFILE
from jmicro.native_precision import validate_stable_runtime
from jmicro.training import implementation_hashes


def audit(export, output):
    torch.set_num_threads(2)
    proof = read_json(export/'nonorm_export_parity_report.json')
    binding = proof['binding']
    checks = {'all_original_numeric_and_controller_gates':proof['status']=='passed' and all(proof['checks'].values()) and
              len(proof['comparisons'])==12 and all(row['passed'] for row in proof['comparisons'].values()),
        'original_frozen_tolerance':proof['tolerance']=={'atol':1e-5,'rtol':1e-4},
        'training_core_unchanged':implementation_hashes()==binding['implementation'],
        'precision_source_bound':sha256(ROOT/'src/jmicro/inference_precision.py')==binding['inference_precision_source_sha256'],
        'verifier_source_bound':sha256(ROOT/'scripts/verify_nonorm_export.py')==binding['verifier_sha256'],
        'protocol_source_bound':sha256(ROOT/'configs/evaluation/protocol.json')==binding['protocol_sha256']}
    runtime = ROOT/'artifacts/runtime-stable-f32-v2'
    validate_stable_runtime(runtime)
    checks['runtime_receipt_and_actual_libraries_bound']=sha256(runtime/'source_receipt.json')==binding['runtime_receipt_sha256']
    checkpoint = Path(binding['checkpoint'])
    state = torch.load(checkpoint,map_location='cpu',weights_only=False)
    checks['original_learned_checkpoint_immutable']=sha256(checkpoint)==binding['checkpoint_sha256']
    own = load_file(str(export/'torch/model.safetensors'))
    hf = load_file(str(export/'hf/model.safetensors'))
    expected = {name:weight for name,weight in state['model'].items() if name!='lm_head.weight'}
    checks['all_saved_torch_learned_weights_exact']=own.keys()==expected.keys() and all(torch.equal(own[name],weight) for name,weight in expected.items())
    checks['all_saved_hf_learned_weights_exact']=hf.keys()==expected.keys() and all(torch.equal(hf[name],weight) for name,weight in expected.items())
    reader = gguf.GGUFReader(export/'model-f32.gguf')
    native_weights = {tensor.name:torch.from_numpy(np.array(tensor.data)) for tensor in reader.tensors}
    config = state['model_config']
    checks['native_profile_metadata']=reader.fields['jmicro.inference_precision'].contents()==PROFILE
    checks['all_119_tensors_fp32']=len(reader.tensors)==119 and all(tensor.tensor_type.name=='F32' for tensor in reader.tensors)
    for name,mapped in proof['weight_mapping'].items():
        weight = expected[name]
        if name.endswith(('self_attn.q_proj.weight','self_attn.k_proj.weight')):
            heads = config['num_attention_heads'] if name.endswith('q_proj.weight') else config['num_key_value_heads']
            indices = torch.arange(weight.shape[0]).reshape(heads,2,-1).transpose(1,2).flatten()
            weight = weight[indices]
        checks['physical_GGUF_weight_'+name]=torch.equal(native_weights[mapped],weight)
    checks['all_GGUF_tensors_accounted_for']=set(native_weights)==set(proof['weight_mapping'].values()) and 'output.weight' not in native_weights
    original = read_json(export.parent/'export-precise/native-float/request.json')['runs']
    current = read_json(export/'native-float/request.json')['runs']
    checks['same_original_ids_and_chunk_partitions']=[(r['name'],r['chunks']) for r in original]==[(r['name'],r['chunks']) for r in current]
    for name in ('short','context1024'):
        prefill = next(row for row in current if row['name']==name+'_prefill')
        cached = next(row for row in current if row['name']==name+'_cache')
        length = len(prefill['chunks'][0])
        arrays = [np.fromfile(row['logits_file'],dtype='<f4').reshape(1,length,4096) for row in (prefill,cached)]
        checks[name+'_physical_native_full_cache_exact']=np.array_equal(*arrays) and all(np.isfinite(a).all() for a in arrays)
    cases = []
    prompt = 'こんにちは。\n今日は　晴れ？🤔 <|assistant|> ▁'
    work = output.parent/'export-cli-evidence'
    work.mkdir(exist_ok=True,parents=True)
    messages = work/'messages.json'
    write_json(messages,[{'role':'user','text':'はい'}])
    for label,artifact,arguments,expected_id in [('learned',export,['--prompt',prompt],None),
            ('eos',export/'stop-fixture-3',['--messages',str(messages)],3),
            ('eot',export/'stop-fixture-7',['--messages',str(messages)],7)]:
        generated=[]
        for backend,relative in [('torch','torch'),('hf','hf'),('gguf','model-f32.gguf' if label=='learned' else 'model.gguf')]:
            command=[sys.executable,str(ROOT/'scripts/infer.py'),'--backend',backend,'--artifact',str(artifact/relative),
                     '--tokenizer',str(ROOT/'artifacts/phase2/4096/tokenizer.model'),*arguments,'--max-new-tokens','8']
            started=time.monotonic()
            child=subprocess.run(command,capture_output=True,text=True,timeout=120)
            assert child.returncode==0,child.stderr
            result=json.loads(child.stdout)
            generated.append(result['generated_ids'])
            checks[label+'_'+backend+'_real_cli']=bool(result['generated_ids']) and (expected_id is None or result['generated_ids']==[expected_id] and result['stop_reason']=='stop_id')
            cases.append({'case':label,'backend':backend,'command':command,'exit_code':child.returncode,
                          'seconds_including_startup':time.monotonic()-started,'result':result})
        checks[label+'_real_CLI_ids_exact']=generated[0]==generated[1]==generated[2]
    command=[sys.executable,str(ROOT/'scripts/infer.py'),'--backend','gguf','--artifact',str(export/'model-f32.gguf'),
             '--tokenizer',str(ROOT/'artifacts/phase2/4096/tokenizer.model'),'--prompt',prompt,'--max-new-tokens','8',
             '--bridge',str(ROOT/'artifacts/runtime/llama-bridge')]
    child=subprocess.run(command,capture_output=True,text=True,timeout=30)
    checks['real_cli_refuses_stock_runtime_for_precision_artifact']=child.returncode==1 and 'Stable FP32 runtime is required' in child.stderr
    checks['checkpoint_still_immutable_after_real_CLI']=sha256(checkpoint)==binding['checkpoint_sha256']
    report={'status':'passed_export_and_cli' if all(checks.values()) else 'failed','checks':checks,'cli_cases':cases,
        'stock_runtime_rejection':{'command':command,'returncode':child.returncode,'stderr':child.stderr},
        'scope':'Learned CPU FP32 precision profile and actual default CLI; stock FP32 failure retained, not a Base quality claim',
        'evidence':{str(export/'nonorm_export_parity_report.json'):sha256(export/'nonorm_export_parity_report.json')},
        'source_sha256':{name:sha256(ROOT/name) for name in ('scripts/audit_phase6_export.py','scripts/infer.py','src/jmicro/inference.py','src/jmicro/inference_precision.py')},
        'completed_at':now()}
    write_json(output,report)
    print(json.dumps({'status':report['status'],'checks':len(checks),'failed':[name for name,value in checks.items() if not value]}),flush=True)
    assert all(checks.values()),checks


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--export',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();audit(args.export.resolve(),args.output.resolve())
