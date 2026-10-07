"""Record CPU checks and real-parent link parity without GPU or scientific updates."""
import copy
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path
sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json, rng_state
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host, right_pad
from base_sigsoftmax_model import install_sigsoftmax, sigsoftmax_logits


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def main():
    started = time.monotonic()
    phase = ROOT / 'reports/phase6'
    output = phase / 'base_sigsoftmax_CPU_preparation_v2.json'
    if output.exists():
        raise ValueError('Preserve CPU evidence')
    proposal_path = phase / 'base_sigsoftmax_proposal.json'
    p = read_json(proposal_path)
    tests = phase / 'base_sigsoftmax_tests_v2.xml'
    suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if (sum(int(s.get('tests', 0)) for s in suites) != 14
            or any(int(s.get(k, 0)) for s in suites for k in ('errors', 'failures', 'skipped'))):
        raise ValueError('Actual14 CPU checks required')
    test_seconds = sum(float(s.get('time', 0)) for s in suites)
    previous_path = phase / 'base_sigsoftmax_CPU_preparation.json'
    previous = read_json(previous_path)
    parent_path = Path(p['parent']['path'])
    if sha256(parent_path) != p['parent']['sha256']:
        raise ValueError('Original parent changed')
    torch.set_num_threads(2)
    parent = torch.load(parent_path, map_location='cpu', weights_only=False)
    with torch.random.fork_rng(devices=[]):
        raw = JMicroModel(parent['model_config']).eval()
    raw.load_state_dict(parent['model'], strict=True)
    linked = copy.deepcopy(raw)
    before = rng_state()
    install_sigsoftmax(linked)
    tokenizer = Tokenizer(ROOT / p['tokenizer'])
    sampler = OriginalTrainCorpusSampler(p['source_binding']['pool'], p['source_binding']['manifest_sha256'],
        tokenizer, p['goals'], p['seed'])
    if sampler.binding != p['source_binding']:
        raise ValueError('Reuse accepted source binding/stat; no whole-corpus scan')
    rows = sampler.take(2)
    sequences = [r['input_ids'][:64] for r in rows]
    ids, _ = right_pad(sequences, torch.device('cpu'))
    mask = ids.ne(0)
    with torch.no_grad():
        native = raw(ids, attention_mask=mask).logits
        expected = sigsoftmax_logits(native)
        actual = linked(ids, attention_mask=mask).logits
    checks = dict(
        original_parent_weights=equal_state(parent['model'], host(linked.state_dict())),
        same_parameter_count=sum(v.numel() for v in raw.parameters()) == sum(v.numel() for v in linked.parameters()) == 10001152,
        tied_vocabulary=linked.lm_head.weight is linked.model.embed_tokens.weight,
        installing_link_preserved_RNG=equal_state(before, rng_state()),
        native_FP32_linked_logits=torch.allclose(actual[mask], expected[mask], atol=1e-6, rtol=1e-6),
        same_weight_FP32_greedy_order=torch.equal(actual[mask].argmax(-1), native[mask].argmax(-1)),
        finite_model_scores=bool(torch.isfinite(actual).all()),
        source_is_train_only=True)
    if not all(checks.values()):
        raise ValueError('Real native parent output-link parity failed: ' + str(checks))
    elapsed = time.monotonic() - started
    total = previous['total_CPU_preparation_seconds'] + test_seconds + elapsed
    if total > 30:
        raise TimeoutError('Prospective CPU30s preparation budget exceeded')
    atomic_json(output, dict(created_at=now(), status='CPU14_and_actual10M_parent_link_parity_passed_no_GPU',
        proposal=ref(proposal_path), tests=ref(tests), tests_passed=14, tests_seconds=test_seconds,
        recorder_CPU_seconds=elapsed, total_CPU_preparation_seconds=total,
        previous_CPU_preparation=ref(previous_path),
        initial_trainer=ref(phase / 'base_sigsoftmax_trainer_initial_CPU.py'),
        initial_tests=ref(phase / 'base_sigsoftmax_tests_initial_CPU.py'),
        change='Same link/math/recipe: keep finite NLL/gradient and cheap committed accounting each update; validate full weights/Adam at save/load. Added actual nonfinite serialization rejection. No scientific GPU or result-driven setting change.',
        CPU_preparation_cap_seconds=30, parent=p['parent'], real_parent_checks=checks,
        source_binding=p['source_binding'], train_diagnostic_sequences=sequences,
        diagnostic_valid_tokens=int(mask.sum()), original_weights_unchanged=True,
        source_sha256={name: sha256(ROOT / name) for name in (
            'scripts/base_sigsoftmax_model.py', 'scripts/base_sigsoftmax_trainer.py',
            'scripts/record_base_sigsoftmax_CPU_preparation.py', 'tests/test_base_sigsoftmax.py', 'src/jmicro/model.py')},
        GPU_seconds=0, scientific_gold_tokens=0, protected_test_used=False,
        GPU_workflow_implemented=False, GPU_resume_capacity_budget_proven=False,
        Japanese_quality_proven=False, Base_complete=False, Base_adopted=False,
        Chat_started=False, quantization_started=False,
        next_action='Implement typed native evaluation and durable measured CUDA/science/reviewer commands; actual GPU gate before freezing scientific100M. No proposed command execution or CPU-as-GPU claims.'))
    print('CPU14 and actual10,001,152-parameter parent link/RNG/greedy parity passed; scientificGPU0')


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
