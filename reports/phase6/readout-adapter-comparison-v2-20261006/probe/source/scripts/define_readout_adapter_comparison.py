"""One distinct nonlinear frozen-decoder readout policy, fixed before GPU."""
import copy
import json
import os
from pathlib import Path
import sys
import time
import xml.etree.ElementTree as ET

os.environ['CUDA_VISIBLE_DEVICES']=''
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,read_json,now
from jmicro.model import JMicroModel
from jmicro.training import atomic_json
from phase6_performance import alive
from readout_adapter_model import ReadoutAdapterModel,POLICY
from readout_adapter_trainer import KIND,READOUT_LR
import run_parameter_displacement_anchor_v3 as native

PROPOSAL=ROOT/'reports/phase6/readout_adapter_proposal.json'


def main():
    started=time.monotonic()
    if PROPOSAL.exists():raise ValueError('Preserve original readout proposal')
    c=native.inspect(native.CONFIG)
    suites=list(ET.parse(ROOT/'reports/phase6/readout_adapter_tests.xml').getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=3 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Three actual native CPU architecture/fresh readout fullstate tests required')
    references={}
    for name in ('gated_shared_comparison','fisher_parameter_anchor'):
        p=ROOT/f'reports/phase6/{name}_completion.json';r=read_json(p)
        if r['eligible_for_final_Base_validation'] or r['Base_complete']:raise ValueError('Retain actual failed alternatives')
        references[name]=native.reference(p)
    stop=ROOT/'reports/phase6/stop_only_feasibility.json';screen=read_json(stop)
    if screen['marker_passed'] or screen['GPU_seconds'] or screen['summary']['outputs']!=80:
        raise ValueError('Fixed unsupported stop-only diagnostic required, not a mathematical impossibility claim')
    references.update(stop_only_screen=native.reference(stop),CPU_tests=native.reference(ROOT/'reports/phase6/readout_adapter_tests.xml'),
        native_config=native.reference(native.CONFIG),native_result=native.reference(native.RUN/'compare-result.json'),
        native_review=native.reference(native.RUN/'review.json'),architecture_rules=native.reference(ROOT/'docs/03_architecture.md'),
        old_rank4_review=native.reference(ROOT/'reports/phase6/low_rank_base_v2_review.json'))
    old_job=read_json(native.RUN/'job.json')
    if old_job['status']!='complete' or alive(old_job):raise ValueError('Cached ordinary control must actually be terminal')
    parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
    with torch.random.fork_rng(devices=[]):
        original=JMicroModel(parent['model_config']);original.load_state_dict(parent['model']);model=ReadoutAdapterModel.from_native(original)
    count=sum(p.numel() for p in model.parameters());trainable=sum(p.numel() for p in model.parameters() if p.requires_grad)
    if (count!=10099456 or trainable!=98304 or len(list(model.named_parameters()))!=121
            or model.lm_head.weight is not model.model.embed_tokens.weight or len(model.model.layers)!=13
            or not 9500000<=count<=10100000):raise ValueError('Actual frozen native10M plus one 256-192-256 readout required')
    elapsed=time.monotonic()-started
    if elapsed>30:raise TimeoutError('CPU proposal30s exhausted')
    proposal=dict(kind=KIND,created_at=now(),parent=c['parent'],policy=POLICY,
        hypothesis='Preserve pretrained decoder features/KV and tied native vocabulary matrix, but learn one nonlinear final readout that can change non-EOS choices and stopping. Native parameters stay exact; final probabilities and Web quality are not guaranteed preserved.',
        comparison='Same mixed parent6d, full staged100M source/targets/order/seed, fixed Japanese/dev256/native greedy80 versus completed cached matched_staged_CE. Training policy is the intervention: only a new nonlinear readout with fresh Adam, versus full native inherited Adam. Not an optimizer-only or architecture-only causal comparison.',
        novelty='Old rank4 changes every attention/MLP projection and merges linear weight deltas, with different masked targets/fresh-full control. This keeps all native decoder/embedding/norm/output weights frozen and adds one nonlinear postnorm readout. It is a new representational mechanism, not a rank/module rescue of the ended rank4 recipe or a decoder bias.',
        bottleneck_width=192,bottleneck_rule='Largest multiple of64 for a bias-free256-m-256 residual inside the documented10.1M total budget: m192 adds98304; m256 would exceed budget. One fixed width, not a sweep.',
        native_unique_parameters=10001152,new_parameters=trainable,unique_parameters=count,new_parameter_tensors=2,
        trainable_names=['lm_head.down','lm_head.up'],readout_LR=READOUT_LR,readout_weight_decay=0.,
        optimizer_policy='Fresh constant-LR AdamW only for readout; same parent betas/eps. Original Adam moments/scheduler recorded as lineage but not used, original matrices receive zero optimizer updates.',
        ordinary_source_CE_teacher_tokens=100000000,teacher_goals=native.GOALS,full_conditional_setup_body_EOS=True,outcome_weight=1,
        parameter_penalty=0,KL=0,new_original_corpus_tokens=0,
        own_CUDA_probe_ceiling_seconds=120,total_new_GPU_ceiling_seconds=900,
        before_science='Own exact identity native FP32/BF16 MATH at32/1024, nonzero readout full/cache1024, frozen native119 coordinates/private RNG/tie/13KV. Own CUDA continuous4 versus2+2 allstate/history and32finite BF16/Flash timing+save atbatch32. Only if1.3training margin+300evaluation+ownprobe fits900s: implement/freeze scientific runner and100M candidate.',
        evaluation='Explicit ReadoutAdapterModel; same fixed dev256/common bytes/Japanese192-331-1119/greedy80 max64 EOS3/suppression; bridge and retention512each. All80 raw-bound individual notes and original strong-staged/absolute/historical Web gates.',
        selection=copy.deepcopy(read_json(ROOT/'reports/phase6/finite_Web_constraint_proposal.json')['selection']),
        no_rescue='No width/activation/placement/initialization/LR/weight-decay/source/mask/parent/decoder/checkpoint sweep. Cost/numeric/quality failure ends this fixed route; no automatic long extension.',
        references=references,preparation_CPU_seconds=elapsed,
        primary_sources=[dict(title='Houlsby et al. frozen pretrained network/bottleneck adapters',url='https://proceedings.mlr.press/v97/houlsby19a.html'),
            dict(title='Kumar et al. feature distortion and linear probing',url='https://arxiv.org/abs/2202.10054')],
        inference='Our single final nonlinear readout is not the exact per-layer BERT adapter protocol. Feature-distortion findings largely concern vision distribution shifts; neither cited work proves this Japanese10M recipe will improve Base.',
        limitations='Adds98304 learned weights (+0.983%); original matrices remain frozen but output distributions can drift. One learned seed/repeated dev/nonblind content. Native nonlinear config/save/cache supported; stock HF export requires a dedicated adapter, not completed. stop-only manual screen is non-exhaustive and is not a mathematical quality upper bound.',
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True,
        scientific_teacher_tokens_so_far=0,new_GPU_seconds_so_far=0)
    atomic_json(PROPOSAL,proposal);print(json.dumps(dict(status='frozen_decoder_nonlinear_readout_defined',unique_parameters=count,trainable_parameters=trainable,CPU_seconds=elapsed,GPU_seconds=0)))


if __name__=='__main__':main()
