"""One read-only, bounded native token-geometry screen before selecting training."""
import argparse
import copy
import gc
import json
import os
from pathlib import Path
import signal
import sys
import time
import xml.etree.ElementTree as ET
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import ROOT, read_json, now, sha256
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, rng_state
from phase6_performance import identity, alive
from base_kv_allocation_trainer import CEOnlyOriginalSampler
from natural_context_contrast_trainer import right_pad, right_padded_hidden, host
from natural_context_contrast_memory import configure_resident_memory
from base_token_geometry import SOURCES, token_statistics, pool_source, severe_marker

PHASE = ROOT/'reports/phase6'
CONFIG = ROOT/'configs/phase6/base_token_geometry_probe.json'
RUN = PHASE/'base-token-geometry-probe-20261007'
PROPOSAL = PHASE/'base_token_geometry_proposal.json'
COMPANION = PHASE/'base_completed_objective_studies_v3_20261007.json'
INPUTS = PHASE/'base_token_geometry_TRAIN_payload.json'
IMPLEMENTATION = ('scripts/base_token_geometry.py','scripts/probe_base_token_geometry.py',
    'scripts/probe_base_token_geometry.ps1','tests/test_base_token_geometry.py',
    'scripts/base_kv_allocation_trainer.py','scripts/natural_context_contrast_corpus.py',
    'scripts/natural_context_contrast_trainer.py','scripts/natural_context_contrast_memory.py',
    'scripts/phase6_performance.py','src/jmicro/model.py','src/jmicro/tokenizer.py','src/jmicro/training.py','uv.lock')


def ref(path):
    return dict(path=str(path),sha256=sha256(path))


def checked(reference):
    path = Path(reference['path'])
    if sha256(path) != reference['sha256']:
        raise ValueError('Frozen evidence differs: ' + path.name)
    return read_json(path)


def prepare():
    if any(p.exists() for p in (CONFIG,PROPOSAL,COMPANION,INPUTS,RUN/'job.json')):
        raise ValueError('Preserve one prospective bounded geometry study')
    started = time.monotonic()
    signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('CPU preparation30s exhausted')))
    signal.alarm(30)
    tests = PHASE/'base_token_geometry_tests.xml'
    suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites) != 4 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Four actual independent CPU math/protocol checks required')
    previous = PHASE/'base_completed_objective_studies_v2_20261007.json'
    snapshot = read_json(previous)
    if len(snapshot['conditions']) != 6:
        raise ValueError('Previous six historical studies required')
    for row in snapshot['conditions']:
        old = checked(row['completion'])
        if alive(old['actual_identity']) or old['eligible_for_final_Base_validation']:
            raise ValueError('Historical six conditions must be closed and unqualified')
    completion_path = PHASE/'base_sigsoftmax_comparison_completion.json'
    complete = read_json(completion_path)
    if (alive(complete['actual_identity']) or complete['scientific_CE_teacher_tokens'] != 100000000
            or complete['eligible_for_final_Base_validation'] or not complete['all80_individually_read']):
        raise ValueError('Actual closed sigsoftmax100M/all80 rejection required')
    review = checked(complete['review'])
    checked(complete['notes'])
    if snapshot['cached_CE'] != complete['summaries']['CE'] or snapshot['strong_staged'] != complete['summaries']['strong_staged']:
        raise ValueError('Common frozen historical controls changed')
    companion = copy.deepcopy(snapshot)
    companion.update(created_at=now(),status='seven_completed_same_gold_conditions_quality_rejected',
        previous_snapshot=ref(previous),original_gold_exposures_across_conditions=700000000,
        dataset_scope='Same matched100M stream used in seven conditions; separate auxiliary positions and linked evaluations are not new unique corpus or additional hard labels.')
    companion['conditions'].append(dict(arm='sigsoftmax',completion=ref(completion_path),
        original_gold_tokens=100000000,summaries=complete['summaries']['sigsoftmax'],
        matched_gates=review['matched_objective_quality'],GPU_seconds_including_probe=complete['total_GPU_seconds_including_probe'],
        eligible_for_final_Base_validation=False))
    old_config = ROOT/'configs/phase6/base_sigsoftmax_comparison.json'
    old = read_json(old_config)
    policy_path = ROOT/'configs/phase6/base_sigsoftmax_review.json'
    policy = read_json(policy_path)
    if policy['config_sha256'] != sha256(old_config):
        raise ValueError('Historical sigsoftmax scientific references differ')
    control = checked(old['control_CE'])
    strong = checked(policy['references']['strong_result'])['checkpoints']['source_order']
    models = dict(parent=old['parent'],
        cached_CE=dict(path=control['checkpoint'],sha256=control['checkpoint_sha256']),
        strong_staged=dict(path=strong['checkpoint'],sha256=strong['checkpoint_sha256']))
    for checkpoint in models.values():
        path = Path(checkpoint['path'])
        if sha256(path) != checkpoint['sha256']:
            raise ValueError('Frozen native weights differ')
        st = path.stat()
        checkpoint.update(size=st.st_size,mtime_ns=st.st_mtime_ns)
    tokenizer = Tokenizer(ROOT/old['tokenizer'])
    if sha256(tokenizer.path) != old['tokenizer_sha256']:
        raise ValueError('Pinned codec differs')
    b = old['source_binding']
    sampler = CEOnlyOriginalSampler(b['pool'],b['manifest_sha256'],tokenizer,
        dict(web=100000,textbook=100000,story=100000),seed=2026100703)
    if sampler.binding != b:
        raise ValueError('Accepted TRAIN stream/index identity differs; no rescan fallback')
    rows = []
    for source in SOURCES:
        selected = set()
        for _ in range(16):
            sampler._draw_document(source)
            row = sampler.pending[source][0]
            ids = row['input_ids'][:128]
            if sum(i>=8 for i in ids) < 16 or row['full_original_body_sha256'] in selected:
                continue
            selected.add(row['full_original_body_sha256'])
            rows.append(dict(source=source,split='train',source_family=row['source_family'],
                full_original_body_sha256=row['full_original_body_sha256'],index_byte_position=row['index_byte_position'],
                index_record_sha256=row['index_record_sha256'],input_ids=ids,
                diagnostic_prefix_only=True,full_original_body_tokens=row['original_body_tokens']))
            if len(selected) == 4:
                break
        if len(selected) != 4:
            raise ValueError('Fixed16 draws lack four eligible distinct original TRAIN units; no reroll')
    payload = dict(created_at=now(),sampler_seed=2026100703,rows=rows,source_binding=b,
        index_draws=sampler.draws,prepared_new_corpus_tokens=0,scientific_teacher_positions=0)
    sampler.handle.close()
    atomic_json(COMPANION,companion)
    proposal = dict(created_at=now(),status='prospective_severe_token_geometry_screen_before_GPU',
        question='Do original parent and cached CE exhibit severe similarity between distinct separated token states on the same12 original TRAIN units, motivating a single token-level separation objective?',
        references={p.name:ref(p) for p in (COMPANION,completion_path,old_config,policy_path,
            PHASE/'base_kv_allocation_proposal.json',PHASE/'base_kv_allocation_bucketed_completion.json',
            PHASE/'base_embedding_gradient_completion.json',PHASE/'base_attention_saturation_completion.json')},
        primary_sources=[dict(url='https://papers.nips.cc/paper_files/paper/2022/file/871cae8f599cb8bbfcb0f58fe1af95ad-Paper-Conference.pdf',
            role='SimCTG studies token-state similarity; its training and contrastive decoding are separate mechanisms.'),
            dict(url='https://arxiv.org/abs/2210.14140',role='Follow-up finds severe anisotropy in specific English GPT2s, not every autoregressive LM. Diagnose local model before selecting learning.')],
        novelty='No token-position geometry screen/SimCTG learning found in current sources/proposals/completions. Earlier context-suffix InfoNCE/projection, middle teacher hints, gradient sharing and confidence/output-link tests address different quantities.',
        declined_head_candidate='Do not add a head-count variant as rescue of the closed MHA4/FFN560 allocation study; its scientific training never ran due9000s budget and its failure is not a quality result.',
        models=models,source_binding=b,units_per_source=4,prefix_tokens_at_most=128,min_body_states=16,
        last_hidden='Final post-RMSNorm native decoder state; single unchanged causal forward, no vocabulary head needed',
        metrics='FP32 unit-state cosine; report all body offdiagonal and primary different input IDs at absolute separation>=4. Same word/special/nearby/diagonal pairs excluded only from primary; retain actual denominators.',
        criterion='cosine>.95 in>=25percent primary ordered pairs per source; same>=two sources in BOTH original parent and cached CE. strong staged is descriptive, cannot rescue a missing marker.',
        thresholds='Fixed conservative local feasibility screen; not a validated causal threshold, quality proxy, global isotropy metric or sufficient signal of successful training.',
        budgets=dict(CPU_preparation_cap_seconds=30,GPU_cap_seconds=120,optimizer_updates=0,new_gold_tokens=0),
        if_positive='Implement one separately frozen same-parent original100M hardCE plus token-position separation training comparison, native10M/no teacher/extra parameters, same cachedCE and full Japanese/80/retention gates, measured totalGPU4800. Training commands/probe are still absent; do not launch this prospective outline or treat a positive marker as quality.',
        if_negative='Close this severe-marker-led SimCTG branch; no threshold, subset, normalization, source, parent, layer, decoder or cap rescue; no learning or automatic geometry-loss sweep.',
        completion='Actual exited bounded read-only CUDA result/all12units on all3models; original weights/no grads/RNG/parameters unchanged; finite pair metrics/denominators and fixed decision; restore original UI/portable evidence/local commit.',
        scope='Correlated token pairs in twelve short TRAIN prefixes; not global rank/causal proof. Does not infer useful Japanese quality, data futility or10M capacity ceiling.',
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        new_GPU_seconds=0,new_scientific_teacher_tokens=0)
    atomic_json(PROPOSAL,proposal)
    atomic_json(INPUTS,payload)
    plan = dict(created_at=now(),proposal=ref(PROPOSAL),companion=ref(COMPANION),payload=ref(INPUTS),
        tests=ref(tests),models=models,source_binding=b,tokenizer=old['tokenizer'],tokenizer_sha256=old['tokenizer_sha256'],
        source_sha256={name:sha256(ROOT/name) for name in IMPLEMENTATION},GPU_cap_seconds=120,
        CPU_preparation_seconds=time.monotonic()-started,Base_complete=False,Chat_started=False,quantization_started=False)
    atomic_json(CONFIG,plan)
    signal.alarm(0)
    print(json.dumps(dict(status='token_geometry_frozen_GPU0',CPU_seconds=plan['CPU_preparation_seconds'],config_sha256=sha256(CONFIG))))


def inspect():
    plan = read_json(CONFIG)
    for key in ('proposal','companion','payload','tests'):
        checked(plan[key]) if key != 'tests' else None
        if sha256(Path(plan[key]['path'])) != plan[key]['sha256']:
            raise ValueError('Frozen reference changed')
    for name,digest in plan['source_sha256'].items():
        if sha256(ROOT/name) != digest:
            raise ValueError('Frozen geometry source changed: ' + name)
    for checkpoint in plan['models'].values():
        st = Path(checkpoint['path']).stat()
        if (st.st_size,st.st_mtime_ns) != (checkpoint['size'],checkpoint['mtime_ns']):
            raise ValueError('Previously SHA-verified native weights identity differs')
    if (RUN/'job.json').exists():
        raise ValueError('One-shot geometry run already exists; inspect actual identity, no duplicate/retry')
    return plan


def run():
    plan = inspect()
    RUN.mkdir(parents=True,exist_ok=True)
    job = dict(status='running',**identity(),started_at=now(),config_sha256=sha256(CONFIG),
        scientific_teacher_tokens=0,optimizer_updates=0,Base_complete=False,Chat_started=False,quantization_started=False)
    atomic_json(RUN/'job.json',job)
    started = None
    try:
        torch.set_num_threads(2)
        torch.use_deterministic_algorithms(True)
        memory = configure_resident_memory(2000000000)
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('Fixed geometry GPU120s exhausted')))
            signal.alarm(120)
            rows = checked(plan['payload'])['rows']
            if len(rows) != 12 or any(row['split'] != 'train' for row in rows):
                raise ValueError('Exact12 original TRAIN diagnostic units required')
            ids,_ = right_pad([row['input_ids'] for row in rows],'cuda')
            models,observations,checks = {},{},{}
            for name,checkpoint in plan['models'].items():
                state = torch.load(checkpoint['path'],map_location='cpu',weights_only=False)
                if state['model_config'].get('output_probability_link') is not None:
                    raise ValueError('Only original native plain-softmax endpoints selected')
                model = JMicroModel(state['model_config']).to('cuda').eval()
                model.load_state_dict(state['model'],strict=True)
                if sum(p.numel() for p in model.parameters()) != 10001152:
                    raise ValueError('Native10M endpoint required')
                before = rng_state()
                with torch.inference_mode(),sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                    hidden = right_padded_hidden(model,ids)
                with torch.inference_mode():
                    measurements = [token_statistics(hidden[i,:len(row['input_ids'])],ids[i,:len(row['input_ids'])])
                                    for i,row in enumerate(rows)]
                checks[name] = dict(model_eval=not model.training,no_parameter_grads=all(p.grad is None for p in model.parameters()),
                    native_count=True,model_config_unchanged=model.config==state['model_config'],
                    weights_unchanged=equal_state(host(model.state_dict()),state['model']),
                    RNG_unchanged=equal_state(before,rng_state()))
                if not all(checks[name].values()):
                    raise ValueError('Read-only native state proof failed')
                observations[name] = [dict(source=row['source'],body_sha256=row['full_original_body_sha256'],statistics=measurement)
                                      for row,measurement in zip(rows,measurements,strict=True)]
                models[name] = {source:pool_source([measurement for row,measurement in zip(rows,measurements,strict=True)
                                                   if row['source']==source]) for source in SOURCES}
                del model,state,hidden
                gc.collect()
                torch.cuda.empty_cache()
                job.update(stage=name+'-complete',heartbeat_at=now(),GPU_seconds=time.monotonic()-started)
                atomic_json(RUN/'job.json',job)
            torch.cuda.synchronize()
            elapsed = time.monotonic()-started
            if elapsed > 120:
                raise TimeoutError('Fixed geometry GPU120s exhausted')
            result = dict(status='complete',created_at=now(),actual_identity=identity(),config_sha256=sha256(CONFIG),
                GPU_seconds=elapsed,memory_policy=memory,read_only_checks=checks,models=models,observations=observations,
                decision=severe_marker(models),train_diagnostic_units=12,new_scientific_teacher_tokens=0,
                optimizer_updates=0,new_unique_corpus=0,geometry_training_implemented=False,
                Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False)
            atomic_json(RUN/'result.json',result)
            job.update(status='complete',stage='complete',ended_at=now(),GPU_seconds=elapsed)
            atomic_json(RUN/'job.json',job)
            signal.alarm(0)
            print(json.dumps(dict(status='token_geometry_readonly_complete',GPU_seconds=elapsed,severe_marker=result['decision']['passed'])))
    except BaseException as error:
        signal.alarm(0)
        job.update(status='failed',error=repr(error),ended_at=now(),GPU_seconds=time.monotonic()-started if started else 0)
        atomic_json(RUN/'job.json',job)
        raise


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser()
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--prepare',action='store_true')
    group.add_argument('--inspect',action='store_true')
    args=parser.parse_args()
    if args.prepare:
        prepare()
    elif args.inspect:
        inspect()
        print('Frozen token geometry inspected; GPU0')
    else:
        run()
