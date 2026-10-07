"""Bounded actual-parent CPU parity and prospective paired gate contract.

No CUDA, new source, quality generation, training, or adoption occurs here.
"""
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
import argparse
import gc
import hashlib
import json
from pathlib import Path
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.model import JMicroModel
from jmicro.training import atomic_json
from phase6_performance import alive, identity
from base_headwise_gate_model import ARMS, POLICY, TAG, HeadwiseGateModel

NATIVE_SHA = '298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83'
PHASE = ROOT/'reports/phase6'
PARITY = PHASE/'base_headwise_gate_parent_CPU_parity.json'
PROPOSAL = PHASE/'base_headwise_gate_proposal.json'


def reference(path):
    return dict(path=str(path), sha256=sha256(path))


def model_digest(model):
    digest = hashlib.sha256()
    for name, value in model.state_dict().items():
        digest.update(name.encode());digest.update(value.detach().numpy().tobytes())
    return digest.hexdigest()


def main():
    if PARITY.exists() or PROPOSAL.exists():
        raise ValueError('Preserve completed/interrupted gate preparation; inspect instead of rerunning')
    started = time.monotonic()
    torch.set_num_threads(2)
    if sha256(ROOT/'src/jmicro/model.py') != NATIVE_SHA:
        raise ValueError('Frozen original native model changed')
    closed_path = PHASE/'base_ademamix_comparison_completion.json'
    closed = read_json(closed_path)
    if (closed['status'] != 'AdEMAMix100M_review_complete_rejected'
            or alive(closed['actual_identity']) or closed['Base_adopted']):
        raise ValueError('Exact previous study must be rejected and actually exited')
    tests = PHASE/'base_headwise_gate_model_tests.xml'
    root = ET.parse(tests).getroot();suites = list(root.iter('testsuite'))
    if not suites or sum(int(s.get('tests',0)) for s in suites) != 15 or any(
            int(s.get(k,0)) for s in suites for k in ('errors','failures','skipped')):
        raise ValueError('Own15 actual CPU model/gradient/state checks required')
    prior = read_json(ROOT/'configs/phase6/base_ademamix_comparison.json')
    parent = prior['parent']
    if sha256(Path(parent['path'])) != parent['sha256']:
        raise ValueError('Actual original10B parent checkpoint differs')
    diagnostic_path = ROOT/'configs/phase6/base_attention_saturation_diagnostic.json'
    diagnostic = read_json(diagnostic_path)
    packet_ref = diagnostic['payload'];packet = read_json(Path(packet_ref['path']))
    if sha256(Path(packet_ref['path'])) != packet_ref['sha256'] or packet.get('TRAIN_only') is not True:
        raise ValueError('Retained immutable TRAIN-only CPU parity packet required')
    rows = packet['rows']
    if len(rows) != 24 or {row['source'] for row in rows} != {'web','textbook','story'}:
        raise ValueError('All24 retained three-source TRAIN windows required')
    state = torch.load(parent['path'], map_location='cpu', weights_only=False)
    original = JMicroModel(state['model_config']).eval()
    original.load_state_dict(state['model'],strict=True)
    del state;gc.collect()
    if sum(p.numel() for p in original.parameters()) != 10001152:
        raise ValueError('Actual original10M unique parameters required')
    initial_digest, initial_rng = model_digest(original), torch.get_rng_state().clone()
    inputs = [torch.tensor([r['input_ids']],dtype=torch.long) for r in rows]
    if any(ids.shape[1]>original.config['max_position_embeddings'] or ids.min()<0 or ids.max()>=4096 for ids in inputs):
        raise ValueError('Exact bounded original-context retained TRAIN inputs required')
    observations = []
    with torch.no_grad():
        native_logits = [original(ids,training_fast_path=True).logits for ids in inputs]
        for arm in ARMS:
            if time.monotonic()-started>30:
                raise TimeoutError('Fixed actual-parent CPU30s preparation ceiling exceeded')
            model = HeadwiseGateModel.from_native(original,arm).eval()
            checks = dict(actual_parameter_count=sum(p.numel() for p in model.parameters())==10014464,
                native_vocab_tie=model.lm_head.weight is model.model.embed_tokens.weight,
                all_gate_weights_zero=all(torch.count_nonzero(b.self_attn.gate_proj.weight)==0 for b in model.model.layers),
                original_parent_unchanged=model_digest(original)==initial_digest,
                RNG_unchanged=torch.equal(initial_rng,torch.get_rng_state()))
            measured = []
            for row,ids,expected in zip(rows,inputs,native_logits):
                actual = model(ids,training_fast_path=True).logits
                measured.append(dict(id=row['id'],source=row['source'],input_positions=ids.numel(),
                    logits_exactly_equal=torch.equal(expected,actual),
                    finite=bool(torch.isfinite(actual).all()),max_absolute_error=float((actual-expected).abs().max())))
            checks['all24_initial_logits_exactly_equal'] = all(r['logits_exactly_equal'] for r in measured)
            checks['all24_logits_finite'] = all(r['finite'] for r in measured)
            if not all(checks.values()):
                raise ValueError('Actual-parent gate conversion parity failed: '+json.dumps(checks))
            observations.append(dict(arm=arm,checks=checks,rows=measured,config=model.config))
            del model;gc.collect()
    elapsed = time.monotonic()-started
    ui = read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:
        served = json.load(response)
    if not alive(ui) or served['checkpoint_sha256'] != parent['sha256'] or served['busy']:
        raise ValueError('Actual idle original UI must remain running through CPU preparation')
    if elapsed>30:
        raise TimeoutError('Actual CPU30s preparation ceiling exceeded')
    sources = {name:sha256(ROOT/name) for name in ('scripts/base_headwise_gate_model.py',
        'scripts/prepare_base_headwise_gate.py','tests/test_base_headwise_gate_model.py','src/jmicro/model.py')}
    parity = dict(status='actual_original10B_CPU_conversion_all24_exact_no_learning',created_at=now(),
        actual_identity=identity(),parent=parent,payload=packet_ref,source_sha256=sources,CPU_seconds=elapsed,
        CPU_ceiling_seconds=30,observations=observations,original_model_unchanged=True,RNG_unchanged=True,
        optimizer_updates=0,scientific_teacher_tokens=0,quality_generations=0,GPU_seconds=0,
        UI_unchanged=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},model=served),
        Base_complete=False,Chat_started=False,quantization_started=False,protected_test_used=False)
    atomic_json(PARITY,parity)
    proposal = dict(status='paired_static_vs_query_headwise_gate_defined_CPU_validated_GPU_unstarted',
        created_at=now(),question='Can query-dependent post-SDPA output selection improve coherent Japanese continuation without sacrificing original Web prediction?',
        hypothesis='Add input-dependent nonlinearity between SDPA and output projection while retaining the parent function at initialization. Existing probability/optimizer changes have not delivered coherent generation. This is a literature-grounded adaptation hypothesis, not a diagnosed attention sink or proven remedy.',
        policy=POLICY,arms=list(ARMS),parent=parent,source_binding=prior['source_binding'],goals=prior['goals'],
        native_parameters=10001152,study_parameters_per_arm=10014464,added_parameters_per_arm=13312,
        parameter_difference_fraction=13312/10001152,
        count_scope='Both arms approximately10M and have exactly equal physical parameters; original native10,001,152 remains frozen. Static gates have zero gradients and stay zero. Not a same-inference-architecture claim.',
        initialization='Independent deep copies of same original10B weights; gate matrices zero, sigmoid1/2, o_proj doubled. No gate or residual inference decoder rescue.',
        optimizer='Both fresh all-parameter AdamW, same LR1e-5/WD.1/betas(.9,.999)/eps1e-8/globalclip1/constant schedule, seed42/batch48. Actual native parameterization is changed in both arms; same nominal LR does not mean same effective native update.',
        teacher_policy='Each exact100M original Web75M/textbook20M/story5M body+EOS teachers, OriginalTrainCorpusSampler including full metadata; original masks/draws/sequence order/fullstate. No new data, tokenization or role targets.',
        comparison='Train NEW static-half matched100M and query-dependent100M. Reused old nativeCE100M and strong staged remain qualification references; old nativeCE is not a matched reparameterized control. Account new scientific total200M separately from probe and reused100M.',
        literature=[dict(url='https://arxiv.org/html/2505.06708',scope='G1/head-specific SDPA sigmoid gate; primarily1.7B/15B fresh learning, not Japanese10M mature-weight adaptation.'),
            dict(url='https://github.com/qiuzh20/gated_attention/blob/main/modeling_qwen3.py',scope='Author implementation multiplies SDPA output by query-derived sigmoid gate before o_proj; own native implementation keeps existing cache/masks/GQA.')],
        novelty='Existing gated_shared uses scalar residual gates for a second invocation. This gate is query/head dependent inside the sole attention invocation. Closed negative saturation assay did not diagnose sinks and does not support QK restoration/softcap/sigma learning; those routes remain closed. Local registered scan found no post-SDPA query-gate learning before this implementation.',
        references=dict(previous=reference(closed_path),CPU_parity=reference(PARITY),CPU_tests=reference(tests),
            initial_CPU_fixture_failure=reference(PHASE/'base_headwise_gate_model_tests_initial.xml'),
            saturation=reference(PHASE/'base_attention_saturation_completion.json'),
            gated_shared=reference(PHASE/'gated_shared_comparison_completion.json'),
            native_control_config=reference(ROOT/'configs/phase6/base_ademamix_comparison.json')),
        source_sha256=sources,CPU_model_tests=15,probe_GPU_ceiling_seconds=180,total_GPU_ceiling_seconds=9000,
        prospective_budget_formula='For EACH arm ceil(100M*sum(all32 completed step seconds)/sum(all32 original gold)*1.3+900 evaluation/save reserve); SUM both plus actual probe must fit9000. No subset timing or old FFN/MHA cap replacement.',
        before_GPU=['Own trainer: exact all-parameter partition, partial-update refusal, typed config/arm/parent, full optimizer/scheduler/RNG/sampler/counters save/resume and original CE/mask/quotas CPU checks',
            'Own typed evaluator/runner/heartbeat/checkpoint/launcher and unchanged reviewer',
            'Own persisted CUDA4vs2+2 allstate/fullhistory and BF16 finite maximum48x1024, resident90percent limit, paired all32 timings and cumulative forecast'],
        quality='Same DEV256/common472055bytes/Japanese192-331-1119/nativegreedy64 all80 EACH/all160 individually raw-bound. Require original relative coherence+8/paired95%lower>0/EOS/rep/BPB/errors against new static and strong staged, absolute g56/coh27/appropriate27/EOS37/rep18/errors0 and historical WebBPB<=.9812859519097707. No thresholds changed.',
        completion='Both exited exact100M and all automatic evaluations/all160 content plus unchanged acceptance/archive/original idleUI/local commit, or explicit own numerical/state/resource-gate failure without science. Only a qualified candidate proceeds to independent trainedseed/fullDEV/protectedTEST/adoption.',
        failure='Close this fixed headwise/query/zero-init/doubled-o_proj/parent/source/teacher/LR recipe on failure. No elementwise/head-share/bias/gain/init/LR/parent/source/batch/backend/decoder/teacher/cap rescue or automatic extension.',
        limitations=['Mature-weight adaptation and added13,312 parameters differ from the paper setup',
            'Function-preserving conversion does not preserve native Adam dynamics; a new static matched arm is essential',
            'Repeated nonblind fixedDEV is not independent human/blind or final TEST',
            'Negative saturation marker does not diagnose a gating benefit; no capacity/improvement guarantee'],
        scientific_configuration_frozen=False,trainer_implemented=False,CUDA_verified=False,scientific_started=False,
        GPU_seconds=0,new_scientific_teacher_tokens=0,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True,
        next_action='Implement owned paired all-state trainer/typed evaluation and durable CUDA gate before any scientific training; keep parent UI running until a GPU job actually needs it.')
    atomic_json(PROPOSAL,proposal)
    print(json.dumps(dict(status=proposal['status'],CPU_seconds=elapsed,parameters=10014464,
                          all24_per_arm_exact=True,GPU_seconds=0,UI_pid=ui['pid'])))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    argparse.ArgumentParser(description=__doc__).parse_args()
    main()
