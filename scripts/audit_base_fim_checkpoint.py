"""Read-only forensic audit of an immutable completed FIM checkpoint/log prefix.

CPU only. No corpus, DEV, TEST, inference, GPU, training or source changes.
Allows monitoring the same running job without treating a prefix as completion.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from base_fim_trainer import committed_state
from jmicro.experiment import sha256,now


def audit(checkpoint,pin,metrics,output):
    if os.environ.get('CUDA_VISIBLE_DEVICES')!='':raise ValueError('Read-only audit requires empty CUDA_VISIBLE_DEVICES')
    if output.exists():raise ValueError('Preserve existing forensic evidence')
    if sha256(checkpoint)!=pin:raise ValueError('Pinned completed checkpoint differs')
    state=torch.load(checkpoint,map_location='cpu',weights_only=False)
    if (not committed_state(state) or state['lineage']['weights_role']!='scientific_fresh_FIM_pilot'
            or state['binding']['probe_weights_used'] is not False
            or state['binding']['learned_parent_weights_used'] is not False):
        raise ValueError('Actual committed scientific FIM state required')
    n=state['counters']['update'];teachers=0;last=None;digest=hashlib.sha256()
    with metrics.open('rb') as stream:
        for raw in stream:
            if last is not None and last['update']==n:break
            row=json.loads(raw);digest.update(raw)
            if row['update']!=(1 if last is None else last['update']+1) or not row['committed_update']:
                raise ValueError('Contiguous completed-update prefix required')
            teachers+=row['CE_targets_this_update']
            s=state['scheduler'];position=teachers
            phase=(position-s['warmup'])/(s['total']-s['warmup'])
            expected=s['peak']*position/s['warmup'] if position<=s['warmup'] else (
                s['final']+(s['peak']-s['final'])*(1+math.cos(math.pi*phase))/2)
            if (row['supervised_tokens']!=teachers or row['lr']!=expected
                    or any(not math.isfinite(row[k]) for k in ('CE_loss','gradient_norm','lr','seconds'))
                    or row['gradient_norm']<=0 or row['CE_targets_this_update']<=0):
                raise ValueError('Each actual teacher increment/LR/finite gradient required')
            if (sum(row['source_teachers'].values())!=teachers
                    or row['FIM_counters']['rows']!=row['update']*state['spec']['batch']
                    or row['FIM_counters']['marker_inputs']>row['CE_input_tokens']-teachers):
                raise ValueError('Original-source/FIM/input counts differ')
            last=row
    if n and (last is None or last['update']!=n or last['supervised_tokens']!=state['counters']['supervised_tokens']
            or last['token_digest']!=state['counters']['token_digest']
            or last['FIM_counters']!=state['sampler']['FIM_counters']):
        raise ValueError('Actual checkpoint and complete metric prefix differ')
    if sha256(checkpoint)!=pin:raise ValueError('Checkpoint changed during forensic audit')
    record=dict(status='completed_checkpoint_and_metric_prefix_CPU_audited_not_quality_evidence',
        observed_at=now(),checkpoint=dict(path=str(checkpoint),sha256=pin),
        metrics_prefix_sha256=digest.hexdigest(),completed_updates=n,original_teacher_positions=teachers,
        actual_original_teacher_scheduler_checked=True,all_model_Adam_counters_finite_committed=True,
        FIM_counters=state['sampler']['FIM_counters'],source_teachers=state['counters']['source_teachers'],
        source_EOS=state['counters']['source_EOS'],source_auditor_sha256=sha256(Path(__file__)),
        new_optimizer_updates=0,new_GPU_seconds=0,new_model_quality_evaluations=0,
        corpus_opened=False,DEV_opened=False,TEST_opened=False,Base_adopted=False)
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ('status','completed_updates','original_teacher_positions')}))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--checkpoint',type=Path,required=True)
    parser.add_argument('--sha256',required=True);parser.add_argument('--metrics',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    audit(args.checkpoint,args.sha256,args.metrics,args.output)
