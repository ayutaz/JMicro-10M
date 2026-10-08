"""CPU observations only: existing selected source endings versus real EOS scores."""
from pathlib import Path
import sys
import time
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src')]
import numpy as np
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json


def main():
    started=time.monotonic()
    phase=ROOT/'reports/phase6'
    destination=phase/'base_residual_boundary_format_observation.json'
    if destination.exists(): raise ValueError('Preserve existing boundary observation')
    prepared=read_json(phase/'base_residual_train_dev_history_preparation.json')
    completed=read_json(phase/'base_residual_train_dev_history_completion.json')
    result=read_json(phase/'base_residual_train_dev_history.json')
    keyed={r['id']:r for r in result['results']}
    observations=[]
    for row in prepared['selected']:
        ending=row['full_original_body_text']
        actual=[s for s in keyed[row['id']]['teacher']['steps'] if s['actual_gold_EOS']]
        observations.append(dict(id=row['id'],population=row['population'],original_trailing_LF=ending.endswith('\n'),
            trailing_LF_count=len(ending)-len(ending.rstrip('\n')),original_tail_repr=repr(ending[-40:]),
            actual_gold_EOS_within64=bool(actual),
            gold_EOS_probability=None if not actual else actual[0]['original_gold_probability'],
            gold_EOS_rank=None if not actual else actual[0]['original_gold_rank']))
    groups={}
    for population in ('TRAIN','DEV'):
        rows=[r for r in observations if r['population']==population]
        groups[population]=dict(documents=len(rows),original_trailing_LF=sum(r['original_trailing_LF'] for r in rows),
            real_EOS_by_ending={})
        for flag in (False,True):
            selected=[r for r in rows if r['original_trailing_LF']==flag and r['actual_gold_EOS_within64']]
            probs=[r['gold_EOS_probability'] for r in selected]
            groups[population]['real_EOS_by_ending'][str(flag)]=dict(observations=len(selected),
                rank1=sum(r['gold_EOS_rank']==1 for r in selected),median_probability=None if not probs else float(np.median(probs)))
    source_names=('src/jmicro/larger_material_v3.py','src/jmicro/nested_material.py','src/jmicro/evaluation.py')
    elapsed=time.monotonic()-started
    if elapsed>30: raise TimeoutError('CPU observation30-second cap exhausted')
    atomic_json(destination,dict(status='CPU_observation_complete_counterfactual_GPU_unstarted',created_at=now(),
        CPU_seconds=elapsed,source_sha256=sha256(Path(__file__)),
        preparation_sha256=sha256(phase/'base_residual_train_dev_history_preparation.json'),
        raw_result_sha256=sha256(phase/'base_residual_train_dev_history.json'),
        completion_sha256=sha256(phase/'base_residual_train_dev_history_completion.json'),groups=groups,observations=observations,
        current_builder_source={n:sha256(ROOT/n) for n in source_names},
        builder_reading='Current material_units slices intact paragraphs through newline match.end(). whole_material temporarily strips for eligibility but returns original text/hash. canonicalize_text normalizes CR/LF and removes NUL, without stripping trailing LF. Thus preserved paragraph boundaries can differ from original whole-document endings. This reading is not an independently replayed global historic preprocessing audit.',
        causal_claim=False,
        next_action='Before learning, freeze a read-only same-body ending counterfactual: current sequential2B actual body ending, identical body with trailing LF removed, and exactly one appended LF. Measure next-token EOS probability/rank and LF preference on all32 fixed units, full original body within context. No new source draw, no generation-cap or Base-gate changes; proposed GPU30seconds. Distinguish marker sensitivity from generation coherence, never normalize DEV/test to obtain acceptance.',
        scientific_teacher_tokens=0,optimizer_updates=0,GPU_seconds=0,Base_complete=False,
        Chat_started=False,quantization_started=False))
    print(groups)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
