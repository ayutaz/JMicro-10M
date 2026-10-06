"""Read actual parent checkpoint budgets/interfaces, no forward pass or GPU."""
from pathlib import Path
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import identity,alive


def main():
    started=time.monotonic();torch.set_num_threads(2)
    cfg=read_json(ROOT/'configs/phase6/condition_relation_comparison.json')
    job=read_json(ROOT/'reports/phase6/condition-relation-comparison-20261006/job.json')
    if job['status']!='complete' or alive(job):raise ValueError('Current GPU study must be terminal')
    base=read_json(Path(cfg['original_config']['path']))
    web_ref=base['reference']['web_screen'];web=read_json(Path(web_ref['path']))
    if sha256(Path(web_ref['path']))!=web_ref['sha256']:raise ValueError('HistoricalWeb evaluation changed')
    trained_path=Path(web_ref['path']).parents[4]/'result.json'
    trained=read_json(trained_path)['arms']['web']
    if trained['checkpoint_sha256']!=web['checkpoint_sha256']:raise ValueError('Historical actual checkpoint/evaluation differ')
    original_parent=web['binding']['parent']
    refs=dict(textbook2B=cfg['parent'],originalWeb10B=dict(path=original_parent['path'],sha256=original_parent['sha256']),
        historicalWeb=dict(path=trained['checkpoint'],sha256=trained['checkpoint_sha256']))
    records={}
    for key,ref in refs.items():
        cp=Path(ref['path'])
        if sha256(cp)!=ref['sha256']:raise ValueError('Actual parent checkpoint differs')
        state=torch.load(cp,map_location='cpu',weights_only=False)
        records[key]=dict(checkpoint=ref,state_keys=sorted(state),update=state['update'],input_tokens=state['tokens'],
            supervised_tokens=state.get('supervised_tokens'),model_config=state['model_config'],
            optimizer_param_group_LRs=[g['lr'] for g in state['optimizer']['param_groups']],
            scheduler=state['scheduler'],spec=state['spec'],RNG_present='rng' in state,
            sampler_keys=sorted(state.get('sampler',{})),model_tensor_count=len(state['model']),
            optimizer_state_entries=len(state['optimizer']['state']))
        del state
    if time.monotonic()-started>30:raise TimeoutError('CPU30s metadata inspection budget exhausted')
    report=dict(status='actual_parent_budget_and_checkpoint_interface_readonly_inventory',created_at=now(),**identity(),
        records=records,reference_evaluation=web_ref,original_Web_BPB=web['body']['bpb'],original_Web_rates=web['greedy_rates'],
        original_Web_256_targets=[dict(doc_id=r['doc_id'],body_tokens=r['body_tokens'],body_bytes=r['body_bytes']) for r in web['body']['rows']],
        model_shapes_equal=records['textbook2B']['model_config']==records['historicalWeb']['model_config'],
        original10B_shape_equal=records['textbook2B']['model_config']==records['originalWeb10B']['model_config'],
        CPU_seconds=time.monotonic()-started,actual_GPU_seconds=0,scientific_teacher_tokens=0,
        protected_test_used=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        script_sha256=sha256(Path(__file__)),
        historical_training_result=dict(path=str(trained_path),sha256=sha256(trained_path)),
        initial_schema_assumption_repaired='Initial read expected checkpoint in evaluation; actual evaluator stores only SHA. Resolve path from authoritative training result and require matching SHA. No fallback checkpoint or new GPU.',
        limitations='Read-only metadata/hash evidence, not re-evaluation or matched learning-budget quality. Different historical parents also differ in data/source/order/learning amount. HistoricalWeb quality guard is not an equal-budget2B or100M causal control.')
    atomic_json(ROOT/'reports/phase6/base_parent_budget_inventory.json',report)
    print(dict(CPU_seconds=report['CPU_seconds'],model_shapes_equal=report['model_shapes_equal'],
        parents={k:dict(update=v['update'],input_tokens=v['input_tokens'],supervised_tokens=v['supervised_tokens'],LRs=v['optimizer_param_group_LRs']) for k,v in records.items()}))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
