"""Old diagnostic reference on new endpoints, separate from fresh-dev selection."""
import gc
import json
from pathlib import Path
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.condition_diagnostic import summarize_choice
from jmicro.japanese_evaluation import NativeLikelihood
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.training import gpu_lock
from phase6_performance import identity,alive
import run_packing_study as study


def main():
    c=study.load_config();run=study.RUN;job=read_json(run/'job.json');assert job['status']=='complete' and not alive(job)
    output=run/'previous-dev-evaluation.json'
    if output.exists():print('Existing old-dev reference retained');return
    started=time.monotonic();result=dict(status='running',identity=identity(),config_sha256=sha256(study.CONFIG),
        evaluator_sha256=sha256(Path(__file__)),old_dev_sha256=c['previous_dev_sha256'],additional_learning_tokens=0,arms={},started_at=now())
    write_json(run/'previous-dev-job.json',result)
    raw=read_json(study.DATA/'previous-dev.json');assert len(raw)==100
    with gpu_lock('cuda'):
        for arm,d in read_json(run/'result.json')['checkpoints'].items():
            assert sha256(Path(d['checkpoint']))==d['checkpoint_sha256']
            state=torch.load(d['checkpoint'],map_location='cpu',weights_only=False)
            model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
            scorer=NativeLikelihood(model,Tokenizer(ROOT/c['tokenizer']),batch=16)
            with sdpa_kernel(SDPBackend.MATH):scores=scorer.score([(r['prefix'],choice) for r in raw for choice in r['choices']])
            notes=[]
            for i,row in enumerate(raw):
                values=[scores[2*i+j]['log_likelihood'] for j in (0,1)]
                pred=0 if values[0]>values[1] else 1 if values[1]>values[0] else None
                notes.append(dict(row,log_likelihood=values,prediction=pred,correct=pred==row['label']))
            result['arms'][arm]=dict(checkpoint_sha256=d['checkpoint_sha256'],summary=summarize_choice(notes),rows=notes,
                by_category={category:summarize_choice([r for r in notes if r['category']==category]) for category in ('reference','quantity','negation','time','cause')})
            del model,state;gc.collect();torch.cuda.empty_cache()
    result.update(status='complete',GPU_wall_seconds=time.monotonic()-started,completed_at=now())
    assert result['GPU_wall_seconds']+job['gpu_elapsed_seconds']<=c['total_gpu_budget_seconds']
    write_json(output,result);write_json(run/'previous-dev-job.json',result)
    print(json.dumps(dict(old_dev={a:d['summary'] for a,d in result['arms'].items()},GPU_wall_seconds=result['GPU_wall_seconds'])),flush=True)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2);main()
