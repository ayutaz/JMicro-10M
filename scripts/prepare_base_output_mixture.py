"""Prospective matched MoC/MoS and own bounded CUDA contract, CPU only."""
import json
import os
from pathlib import Path
import sys
import time
import urllib.request

os.environ['CUDA_VISIBLE_DEVICES'] = ''
sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'),
                str(Path(__file__).resolve().parent)]
import torch
from torch.nn import functional as F
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from natural_context_contrast_trainer import host
from base_output_mixture_model import ARMS, POLICY, OutputMixtureModel
from probe_base_output_mixture import CONFIG, PREPARATION, SOURCES, passed_tests, ref
from phase6_performance import alive, identity

PHASE = ROOT / 'reports/phase6'
PROPOSAL = PHASE / 'base_output_mixture_proposal.json'


def main():
    if any(p.exists() for p in (CONFIG, PREPARATION, PROPOSAL)):
        raise ValueError('Preserve one-shot mixture preparation; no setting rescue')
    old = read_json(ROOT / 'configs/phase6/base_headwise_gate_probe.json')
    ended = read_json(PHASE / 'sarashina_prose_comparison_completion.json')
    if ended['Base_complete'] or ended['paired64']['candidate_accepted']:
        raise ValueError('Latest completed rejected source evidence required')
    tests = PHASE / 'base_output_mixture_CPU_tests.xml'
    passed_tests(tests, 16)
    if sha256(ROOT / 'src/jmicro/model.py') != '298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83':
        raise ValueError('Frozen native source differs')
    pstat = Path(old['parent']['path']).stat()
    if (pstat.st_size, pstat.st_mtime_ns) != (old['parent_size'], old['parent_mtime_ns']):
        raise ValueError('Previously hash-verified native parent changed')
    source_hashes = {name: sha256(ROOT / name) for name in SOURCES}
    fields = ('parent', 'parent_size', 'parent_mtime_ns', 'source_binding', 'goals',
              'tokenizer', 'tokenizer_sha256', 'dev_shards', 'dev_manifest_sha256',
              'suite_sha256', 'evaluation', 'control_CE')
    common = {key: old[key] for key in fields}
    proposal = dict(status='new_learned_MoC_MoS_paired_contract_before_own_CUDA_or_science',
        created_at=now(), **common, arms=list(ARMS), policy=POLICY,
        rationale='Low hidden dimension constrains a single-softmax output family. Learned probability mixtures can expand it; equal-capacity context mixture isolates mixing after normalization. Rank is not established as the cause of current repetition, and prior parameter-free Sigsoftmax was rejected.',
        novelty='Registered sources have no implemented trained MoS; previous Sigsoftmax proposal explicitly excluded MoS for added parameters/compute. This learned two-context adaptation has a new matched control; no shifted/calibrated Sigsoftmax, input/output untie, or old failed checkpoint rescue.',
        control='New mixture_contexts from identical original native parent and identical physical new matrices; cached native CE is a reference, never the matched control.',
        native_parameters=10001152, study_parameters_each=10034434, added_parameters=33282,
        optimizer='fresh all-parameter AdamW lr1e-5/wd.1/betas(.9,.999)/eps1e-8/globalclip1/constant',
        scientific_original_gold_each=100000000, scientific_original_gold_total=200000000,
        batch=48, seed=42, probe_GPU_ceiling_seconds=180, total_GPU_ceiling_seconds=9000,
        forecast='ceil(100M*SUM all32 step wall seconds/SUM all32 original teachers*1.3+900) per arm; sum plus actual own probe<=9000; include data waiting and all updates, no median/cache speed claim.',
        quality='Unchanged new-matched/strong/cached/absolute/historicalWeb conjunction; all common256byte/all Japanese/all160 raw-bound individual contents. Independently trained seed/fullDEV/protectedTEST/adoption only for a qualified candidate.',
        initial_parent_gate='MoC exact initial scores; both arms initial FP32 probabilities absolute+relative tolerance1e-6/all top1 same. MoS log probabilities differ in representation from raw native scores. Initial actual CUDA CE difference<=2e-6 is arithmetic parity, not Base quality.',
        completion='Own CUDA4vs2save+2 full optimizer/scheduler/RNG/sampler/counter/history, actual48x1024 finite BF16/Flash/resident90percent and all32 timing. Discard verification weights. Only within prospective budget define/run the completed science workflow and frozen quality policy. All original gold/source/EOS/stream retained.',
        failure='Close this exact experts/rank/residual/init/priors/parent/LR/data/batch/backend/decoder/cap on failure; no tuning or automatic extension. No teacher-model or prompt rescue.',
        primary_sources=['https://arxiv.org/abs/1711.03953', 'https://github.com/zihangdai/mos',
                         'https://ojs.aaai.org/index.php/AAAI/article/view/17608'],
        limitations='Residual rank32/two components and mature-parent adaptation differ from the paper. High output rank is neither sufficient nor necessary for good perplexity/meaning. Parameters, extra output computation and optimizer dynamics are accounted for; no Japanese quality/capacity success claimed.',
        source_sha256=source_hashes, GPU_seconds=0, scientific_started=False,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        protected_test_used=False, quality_criteria_unchanged=True)
    # Freeze the recipe before measuring any new actual-parent conversion.
    write_json(PROPOSAL, proposal)
    start = time.monotonic()
    torch.set_num_threads(2)
    parent = torch.load(old['parent']['path'], map_location='cpu', weights_only=False)
    native = JMicroModel(parent['model_config']).eval()
    native.load_state_dict(parent['model'])
    original = host(native.state_dict())
    payload = PHASE / 'base_gradient_precision_payload.json'
    rows = read_json(payload)['rows'][:24]
    if len(rows) != 24:
        raise ValueError('All previously fixed24 TRAIN windows required')
    observations = []
    for arm in ARMS:
        rng = torch.get_rng_state()
        model = OutputMixtureModel.from_native(native, arm).eval()
        measurements = []
        for row in rows:
            ids = torch.tensor([row['input_ids']])
            with torch.no_grad():
                reference = native(ids).logits
                candidate = model(ids).logits
                p, q = reference.softmax(-1), candidate.softmax(-1)
            torch.testing.assert_close(p, q, atol=1e-6, rtol=1e-6)
            top1_same = torch.equal(reference.argmax(-1), candidate.argmax(-1))
            if not top1_same or not torch.isfinite(candidate).all():
                raise ValueError('Initial finite native top1/probabilities differ')
            measurements.append(dict(id=row['id'], probability_max_absolute=float((p-q).abs().max()),
                                     top1_same=True, finite=True))
        checks = dict(actual_count=sum(x.numel() for x in model.parameters()) == 10034434,
                      native_vocabulary_tie=model.lm_head.weight is model.model.embed_tokens.weight,
                      original_parent_unchanged=equal_state(original, host(native.state_dict())),
                      global_RNG_unchanged=torch.equal(rng, torch.get_rng_state()))
        if not all(checks.values()):
            raise ValueError('Actual parent/count/tie/RNG proof failed')
        observations.append(dict(arm=arm, checks=checks, rows=measurements))
    seconds = time.monotonic() - start
    if seconds > 30:
        raise TimeoutError('CPU conversion30s budget exhausted')
    ui = read_json(ROOT / 'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model', timeout=5) as response:
        api = json.load(response)
    if not alive(ui) or api['checkpoint_sha256'] != old['parent']['sha256'] or api['busy']:
        raise ValueError('Original actual idle UI required')
    prep = dict(status='new_paired_output_mixture_CPU_verified_GPU_unstarted', created_at=now(),
                policy=POLICY, CPU_tests=ref(tests), CPU_test_count=16, CPU_seconds=seconds,
                observations=observations, actual_identity=identity(), payload=ref(payload),
                source_sha256=source_hashes, proposal=ref(PROPOSAL), study_parameters_each=10034434,
                GPU_seconds=0, new_scientific_teacher_tokens=0, Base_complete=False,
                Chat_started=False, quantization_started=False,
                UI=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},
                        actual_alive=True, model=api))
    write_json(PREPARATION, prep)
    write_json(CONFIG, dict(**common, created_at=now(), preparation=ref(PREPARATION),
                proposal=ref(PROPOSAL), CPU_tests=ref(tests), payload=old['payload'],
                mixture_policy=POLICY, source_sha256=source_hashes,
                arms=list(ARMS), batch=48, seed=42,
                resource=dict(probe_GPU_cap_seconds=180,total_GPU_cap_seconds=9000,
                              warmup_updates=3,timed_updates=32),
                Base_complete=False, Chat_started=False, quantization_started=False))
    print(json.dumps(dict(status=prep['status'], CPU_tests=16, CPU_seconds=seconds,
                          parameters_each=10034434, actual_parent_windows_each=24)))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
