"""Explicit architecture comparison; completed KL/anchor failures stay failed."""
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
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.training import atomic_json
from phase6_performance import alive
from gated_shared_model import GatedSharedModel,POLICY
from gated_shared_trainer import KIND,NATIVE_LR,GATE_LR
import run_parameter_displacement_anchor_v3 as native

PROPOSAL=ROOT/'reports/phase6/gated_shared_proposal.json'


def main():
    if PROPOSAL.exists():raise ValueError('Preserve original sharing proposal')
    started=time.monotonic();c=native.inspect(native.CONFIG)
    suites=list(ET.parse(ROOT/'reports/phase6/gated_shared_tests.xml').getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=4 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Four actual architecture and native fullstate CPU tests required')
    references={}
    for name in ('web_kl_comparison','eos_decoupled_web_kl_comparison','hard_body_web_replay_comparison','anchored_context_outcome_comparison','fisher_parameter_anchor'):
        path=ROOT/f'reports/phase6/{name}_completion.json';report=read_json(path)
        if report.get('eligible_for_final_Base_validation',False) or report.get('Base_complete',False):
            raise ValueError('Preserve actually rejected retention alternatives')
        references[name]=native.reference(path)
    job=read_json(native.RUN/'job.json');result=read_json(native.RUN/'compare-result.json')
    if job['status']!='complete' or alive(job) or result['scientific_teacher_tokens']!=200000000:
        raise ValueError('Actual completed ordinary CE control required')
    references.update(native_config=native.reference(native.CONFIG),native_result=native.reference(native.RUN/'compare-result.json'),
        native_review=native.reference(native.RUN/'review.json'),CPU_tests=native.reference(ROOT/'reports/phase6/gated_shared_tests.xml'),
        architecture_rules=native.reference(ROOT/'docs/03_architecture.md'))
    parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
    with torch.random.fork_rng(devices=[]):
        model=JMicroModel(parent['model_config']);model.load_state_dict(parent['model']);shared=GatedSharedModel.from_native(model)
    parameters=sum(p.numel() for p in shared.parameters())
    if (parameters!=10001165 or len(model.model.layers)!=13 or shared.logical_layers!=26
            or shared.lm_head.weight is not shared.model.embed_tokens.weight
            or len(list(shared.named_parameters()))!=120 or not 9500000<=parameters<=10100000):
        raise ValueError('Actual unique10M/native13/logical26/tied contract required')
    elapsed=time.monotonic()-started
    if elapsed>30:raise TimeoutError('CPU proposal30s exhausted')
    proposal=dict(kind=KIND,created_at=now(),parent=c['parent'],policy=POLICY,
        hypothesis='Same unique blocks can reuse computation to improve conditional Japanese continuity without increasing the learned matrix parameter budget. Zero gates preserve the initial native function; gains are empirical, not assumed capacity proof.',
        comparison='One gated-sharing full100M candidate versus cached matched_staged_CE100M. Same native starting weights/Adam moments/scheduler/RNG, source quotas/order, input/target protocol and fixed evaluators; additional13 zero gates have fresh Adam group and fixed LR. More computation and cache are separately reported.',
        native_lr=NATIVE_LR,new_gate_lr=GATE_LR,new_gate_weight_decay=0,
        optimizer_policy='Exact native2 groups/moments inherited; append only13 zero gate coordinates as one fresh group, native LR1e-5 and new gate LR1e-4, fixed permanent floor factors. No native reset/reheat.',
        unique_parameters=parameters,native_unique_parameters=10001152,new_gate_parameters=13,
        unique_blocks=13,logical_block_invocations=26,new_unique_parameter_tensors=1,
        teacher_goals=native.GOALS,ordinary_source_CE_teacher_tokens=100000000,
        full_conditional_setup_body_EOS=True,outcome_weight=1,parameter_penalty=0,KL=0,
        preparation_CPU_seconds=elapsed,own_CUDA_probe_ceiling_seconds=120,total_new_GPU_ceiling_seconds=1800,
        before_science='Own CUDA zero-gate parent FP32/MATH and BF16/MATH native logits at32/1024, nonzero signed-gate full/cache1024; native optimizer/RNG preservation;4 continuous versus2+2 allstate/history;32timing+save and actual finite CUDA/BF16/Flash batch32. Science only when1.3margin+300evaluation and own probe fit1800s.',
        evaluation='Same fixed dev256/common bytes/Japanese192-331-1119/BOS-native greedy80 max64 EOS3/no decoder change; explicitly construct GatedSharedModel from config and strict120unique state, logical26 caches; all80 individually raw-bound content and old unchanged gates.',
        selection=copy.deepcopy(read_json(ROOT/'reports/phase6/finite_Web_constraint_proposal.json')['selection']),
        no_rescue='No gate LR/init/count/sign constraint/reuse order/depth/parent/source/mask/native LR/batch/precision/decoder/checkpoint sweep. Failed finite/quality/cost branch ends. No automatic100M extension.',
        limitations='This is architecture research to improve the unfinished Base; neither an exact replication of published models nor proof that10M capacity caused prior failures. Extra13 scalars (+0.00013%) remain in documented9.5M-10.1M range. Compute and KV memory roughly double. Native config/checkpoint supported; stock HF/Llama export needs a dedicated adapter and is not claimed complete.',
        primary_sources=[dict(title='MobileLLM immediate block-wise sharing',url='https://arxiv.org/abs/2402.14905'),
            dict(title='ReZero zero-initialized residual gates',url='https://arxiv.org/abs/2003.04887')],
        inference='Combining sharing with zero gates on only the new residual invocations is our function-preserving transfer hypothesis; published sub-billion/enwiki8 findings do not establish Japanese10M quality.',
        references=references,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        protected_test_used=False,quality_criteria_unchanged=True,scientific_teacher_tokens_so_far=0,new_GPU_seconds_so_far=0)
    atomic_json(PROPOSAL,proposal)
    print(json.dumps(dict(status='gated_sharing_defined',CPU_seconds=elapsed,unique_parameters=parameters,new_GPU_seconds=0)))


if __name__=='__main__':main()
