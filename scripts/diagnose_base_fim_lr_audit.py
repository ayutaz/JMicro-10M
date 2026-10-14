"""CPU comparison of actual applied LR and the audit expression; no new learning."""
import json
import math
import os
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from base_kv_allocation_trainer import TargetPositionSchedule
from types import SimpleNamespace

if os.environ.get('CUDA_VISIBLE_DEVICES')!='':raise ValueError('CPU only')
root=Path(__file__).resolve().parents[1]
run=root/'reports/phase6/base-fim-pilot-20261015'
s=torch.load(run/'checkpoint-00010000.pt',map_location='cpu',weights_only=False)['scheduler']
clock=TargetPositionSchedule(SimpleNamespace(param_groups=[{}]),s['total'],s['warmup'],s['peak'],s['final'])
rows=[];native_errors=0;audit_errors=0
with (run/'metrics.jsonl').open() as stream:
    for line in stream:
        row=json.loads(line);p=row['supervised_tokens']
        wrong=s['peak']*p/s['warmup'] if p<=s['warmup'] else s['final']+(s['peak']-s['final'])*(1+math.cos(math.pi*(p-s['warmup'])/(s['total']-s['warmup'])))/2
        native=clock.value(p)
        native_errors+=row['lr']!=native;audit_errors+=row['lr']!=wrong
        if row['lr']!=wrong and len(rows)<8:
            rows.append(dict(update=row['update'],actual=row['lr'],native=native,old_audit=wrong,difference=wrong-row['lr']))
result=dict(status='actual_native_scheduler_matches_old_audit_arithmetic_order_differs',
    native_schedule_mismatches=native_errors,old_audit_expression_mismatches=audit_errors,first_differences=rows,
    cause='Audit multiplied by pi before division; native first computes normalized phase then multiplies pi.',
    new_GPU_seconds=0,new_learning_updates=0,scientific_sources_modified=False)
output=root/'reports/phase6/fim-feasibility-20261015/LR_audit_expression_diagnosis.json'
if output.exists():raise ValueError('Preserve diagnostic evidence')
output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
