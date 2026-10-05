"""Compare isolated and original packed contexts without learning or changing gates."""
import gc
import json
from pathlib import Path
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import torch
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.japanese_evaluation import NativeLikelihood
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.training import gpu_lock
from phase6_performance import identity,alive
import run_condition_diagnostic as study


def main():
    c=study.load_config();run=study.RUN;job=read_json(run/'job.json')
    assert job['status']=='complete' and not alive(job), 'Scientific job must have exited'
    output=run/'packing-probe.json'
    if output.exists():print('Existing packing probe retained');return
    started=time.monotonic();result=dict(identity=identity(),status='running',started_at=now(),additional_learning_tokens=0,
        config_sha256=sha256(study.CONFIG),probe_sha256=sha256(Path(__file__)),arms={})
    write_json(run/'packing-probe-job.json',result)
    with gpu_lock('cuda'):
        tok=Tokenizer(ROOT/c['tokenizer'])
        for arm in ('compact','expanded'):
            detail=read_json(run/arm/'result.json');state=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False)
            assert sha256(Path(detail['checkpoint']))==detail['checkpoint_sha256']
            model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
            scorer=NativeLikelihood(model,tok,batch=8)
            directory=Path(c['pools'][arm]['pool']);stream=np.memmap(directory/'train.bin',dtype='<u2',mode='r')
            index={r['doc_id']:r for r in read_json(directory/'train.index.json')}
            isolated={r['id']:r for r in read_json(run/arm/'condition-evaluation.json')['results']['train']['rows']}
            requests=[];retained=[];skipped=[]
            for row in read_json(study.DATA/(arm+'-train-eval.json')):
                entry=index[row['id']];offset=entry['offset'];start=offset//1024*1024
                prefix=tok.encode(row['prefix']);end=offset+1+len(prefix)
                context=np.asarray(stream[start:end],dtype=np.int64).tolist()
                assert context[-len(prefix):]==prefix
                targets=[tok.encode(choice) for choice in row['choices']]
                correct=targets[row['label']]
                assert np.asarray(stream[end:end+len(correct)],dtype=np.int64).tolist()==correct
                if any(len(context)+len(target)-1>1024 for target in targets):
                    skipped.append(row['id']);continue
                retained.append(row)
                for target,choice in zip(targets,row['choices']):
                    requests.append(dict(ids=context+target,context_tokens=len(context),target_ids=target,target_bytes=len(choice.encode())))
            with sdpa_kernel(SDPBackend.MATH):scores=scorer.score_encoded(requests)
            notes=[]
            for i,row in enumerate(retained):
                ll=[scores[2*i+j]['log_likelihood'] for j in (0,1)]
                prediction=0 if ll[0]>ll[1] else 1 if ll[1]>ll[0] else None
                notes.append(dict(id=row['id'],category=row['category'],isolated_correct=isolated[row['id']]['correct'],
                    packed_correct=prediction==row['label'],isolated_expected_nll=isolated[row['id']]['expected_continuation_nll'],
                    packed_expected_nll=-ll[row['label']],target_tokens=len(requests[2*i+row['label']]['target_ids']),
                    packed_log_likelihood=ll,expected_label=row['label']))
            result['arms'][arm]=dict(checkpoint_sha256=detail['checkpoint_sha256'],retained=len(notes),boundary_crossing_skipped=skipped,
                isolated_correct=sum(r['isolated_correct'] for r in notes),packed_correct=sum(r['packed_correct'] for r in notes),
                isolated_expected_nll_per_token=sum(r['isolated_expected_nll'] for r in notes)/sum(r['target_tokens'] for r in notes),
                packed_expected_nll_per_token=sum(r['packed_expected_nll'] for r in notes)/sum(r['target_tokens'] for r in notes),
                forward_input_tokens=scorer.forward_tokens,notes=notes)
            del model,state;gc.collect();torch.cuda.empty_cache()
    result.update(status='complete',GPU_wall_seconds=time.monotonic()-started,completed_at=now(),
        interpretation='Original fixed block context vs standalone document, on same retained train targets. This detects context dependence; it does not isolate prior-document shortcuts from absolute position or all numerical differences.')
    assert result['GPU_wall_seconds']+job['gpu_elapsed_seconds']<=c['total_gpu_budget_seconds']
    write_json(output,result);write_json(run/'packing-probe-job.json',result)
    print(json.dumps({a:{k:v for k,v in d.items() if k!='notes'} for a,d in result['arms'].items()}),flush=True)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2);main()
