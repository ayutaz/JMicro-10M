"""One pinned foreign Japanese Base reference; no student training or adoption."""
import os
os.environ['HF_HUB_DISABLE_IMPLICIT_TOKEN'] = '1'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
import argparse
import json
from pathlib import Path
import re
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, StoppingCriteria, StoppingCriteriaList
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json, gpu_lock
from phase6_performance import identity, alive
from prepare_public_japanese_base_reference import RUN as RECOVERY, DATA

RUN = ROOT / 'reports/phase6/public-japanese-base-reference-20261007'
PLAN = RUN / 'plan.json'
SUITE = ROOT / 'eval/base.jsonl'


def load_inputs():
    recovery = read_json(RECOVERY / 'result.json')
    if alive(recovery['actual_identity']):
        raise ValueError('Recovery process must have exited')
    for row in recovery['files']:
        st = Path(row['path']).stat()
        if (st.st_size, st.st_mtime_ns) != (row['bytes'], row['mtime_ns']):
            raise ValueError('Previously hashed public model file changed')
    cases = [json.loads(line) for line in SUITE.read_text().splitlines() if line.strip()]
    cases = [row for row in cases if row['split'] == 'dev']
    if len(cases) != 80 or len({row['id'] for row in cases}) != 80:
        raise ValueError('Fixed80 DEV required')
    tokenizer = AutoTokenizer.from_pretrained(DATA, use_fast=False, local_files_only=True)
    tokenizer.do_lower_case = True
    config = read_json(DATA / 'config.json')
    if (config['bos_token_id'], config['eos_token_id']) != (tokenizer.bos_token_id, tokenizer.eos_token_id):
        raise ValueError('Official BOS/EOS mismatch')
    suppressed = sorted(set(i for i in tokenizer.all_special_ids if i < config['vocab_size']) - {tokenizer.eos_token_id})
    encoded = []
    for row in cases:
        body = tokenizer.encode(row['prefix'], add_special_tokens=False)
        if not body or any(i >= config['vocab_size'] for i in body) or len(body) + 65 > config['n_positions']:
            raise ValueError('Unusable fixed prefix')
        normalized = tokenizer.decode(body, skip_special_tokens=False, clean_up_tokenization_spaces=False)
        encoded.append(dict(**row, input_ids=[tokenizer.bos_token_id, *body],
                            normalized_prefix=normalized, normalization_changed=normalized != row['prefix'],
                            prefix_UNK_tokens=body.count(tokenizer.unk_token_id)))
    return recovery, tokenizer, encoded, suppressed


def inspect():
    if (RUN / 'job.json').exists():
        raise ValueError('Inspect actual existing process; no duplicate reference')
    recovery, tokenizer, cases, suppressed = load_inputs()
    model = AutoModelForCausalLM.from_pretrained(DATA, local_files_only=True, dtype=torch.float32, attn_implementation='eager').eval()
    if not all(torch.isfinite(p).all().item() for p in model.parameters()):
        raise ValueError('Nonfinite public parameters')
    with torch.inference_mode():
        logits = model(torch.tensor([cases[0]['input_ids']]), use_cache=False).logits
        if not torch.isfinite(logits).all().item() or logits.shape[-1] != model.config.vocab_size:
            raise ValueError('Foreign codec/logit width/finite preflight failed')
    plan = dict(created_at=now(), recovery_sha256=sha256(RECOVERY / 'result.json'),
                proposal_sha256=sha256(RECOVERY / 'proposal.json'), suite_sha256=sha256(SUITE),
                source_sha256=sha256(Path(__file__)), actual_parameters=sum(p.numel() for p in model.parameters()),
                repository=recovery['repository'], revision=recovery['revision'], max_new_tokens=64,
                GPU_limit_seconds=180, dtype='float32', attention='eager', decoding='greedy', batch=1,
                BOS=tokenizer.bos_token_id, EOS=tokenizer.eos_token_id, suppressed_ids=suppressed,
                tokenizer_class=type(tokenizer).__name__, tokenizer_do_lower_case=True,
                normalization_changed=sum(c['normalization_changed'] for c in cases),
                prefix_UNK_tokens=sum(c['prefix_UNK_tokens'] for c in cases), cases=cases,
                checks={'finite_CPU_forward': True, 'all80_DEV_only': True, 'official_codec_ids': True},
                accounting='Foreign64 tokens are not native64 tokens or equal byte/GPU budget. No BPB comparison.',
                limitations='Different parameters, architecture, codec, pretraining data/budget; benchmark contamination unknown. Reference only; no student adoption or teacher-transfer gate rescue.',
                Base_complete=False, Chat_started=False, quantization_started=False)
    RUN.mkdir(parents=True, exist_ok=True)
    if PLAN.exists():
        old = read_json(PLAN)
        if any(old[k] != v for k, v in plan.items() if k != 'created_at'):
            raise ValueError('Preserve frozen reference protocol')
    else:
        atomic_json(PLAN, plan)
    print(json.dumps({k: plan[k] for k in ('actual_parameters', 'normalization_changed', 'prefix_UNK_tokens', 'checks')}))


class Deadline(StoppingCriteria):
    def __init__(self, started, limit): self.started, self.limit = started, limit
    def __call__(self, input_ids, scores, **kwargs):
        if time.monotonic() - self.started > self.limit:
            raise TimeoutError('Frozen180s reference GPU occupancy exhausted')
        return False


def run():
    p = read_json(PLAN)
    if p['source_sha256'] != sha256(Path(__file__)) or p['suite_sha256'] != sha256(SUITE):
        raise ValueError('Frozen reference source/suite changed')
    if (RUN / 'job.json').exists():
        raise ValueError('Inspect existing job; partial reference is not full80 completion')
    recovery, tokenizer, cases, suppressed = load_inputs()
    if (sha256(RECOVERY / 'result.json') != p['recovery_sha256'] or
            sha256(RECOVERY / 'proposal.json') != p['proposal_sha256'] or cases != p['cases'] or suppressed != p['suppressed_ids']):
        raise ValueError('Frozen recovered reference/codec changed')
    job = dict(status='running', **identity(), started_at=now(), plan_sha256=sha256(PLAN), completed_cases=0)
    atomic_json(RUN / 'job.json', job)
    started = None
    try:
        with gpu_lock('cuda'):
            started = time.monotonic()
            torch.set_num_threads(2)
            torch.cuda.set_per_process_memory_fraction(.9)
            model = AutoModelForCausalLM.from_pretrained(DATA, local_files_only=True, dtype=torch.float32, attn_implementation='eager').eval().cuda()
            rows = []
            for case in cases:
                Deadline(started, p['GPU_limit_seconds'])(None, None)
                inputs = torch.tensor([case['input_ids']], device='cuda')
                with torch.inference_mode():
                    generated = model.generate(inputs, attention_mask=torch.ones_like(inputs),
                        do_sample=False, num_beams=1, max_new_tokens=64, use_cache=True,
                        bos_token_id=p['BOS'], eos_token_id=p['EOS'], pad_token_id=tokenizer.pad_token_id,
                        suppress_tokens=suppressed, stopping_criteria=StoppingCriteriaList([Deadline(started, 180)]))
                ids = generated[0, inputs.shape[1]:].tolist()
                if not ids or len(ids) > 64 or any(i < 0 or i >= model.config.vocab_size or i in suppressed for i in ids):
                    raise ValueError('Invalid actual foreign output IDs')
                stopped = ids[-1] == p['EOS']
                if p['EOS'] in ids[:-1]: raise ValueError('EOS must be terminal')
                body = ids[:-1] if stopped else ids
                raw = tokenizer.decode(ids, skip_special_tokens=False, clean_up_tokenization_spaces=False)
                text = tokenizer.decode(body, skip_special_tokens=False, clean_up_tokenization_spaces=False)
                text.encode('utf-8', errors='strict')
                row = dict(id=case['id'], family_id=case['family_id'], category=case['category'], prefix=case['prefix'],
                    input_ids=case['input_ids'], normalized_prefix=case['normalized_prefix'],
                    normalization_changed=case['normalization_changed'], prefix_UNK_tokens=case['prefix_UNK_tokens'],
                    generated_ids=ids, raw_decoded_with_EOS=raw, text=text, stopped_by='stop_id' if stopped else 'max_tokens',
                    EOS=stopped, generated_tokens=len(ids), body_tokens=len(body), characters=len(text), utf8_bytes=len(text.encode()),
                    repetition=bool(re.search(r'(.{2,}?)\1\1', text, re.DOTALL)), empty=not text.strip(),
                    unicode_failure='\ufffd' in text, role_leak=any(s in text for s in ('<|assistant|>', '<|user|>', '<|system|>')))
                rows.append(row)
                atomic_json(RUN / 'generation.partial.json', rows)
                job.update(completed_cases=len(rows), heartbeat_at=now(), GPU_occupancy_seconds=time.monotonic() - started)
                atomic_json(RUN / 'job.json', job)
            torch.cuda.synchronize()
            duration = time.monotonic() - started
            if duration > 180: raise TimeoutError('Reference GPU budget exceeded')
            atomic_json(RUN / 'generation.json', rows)
            result = dict(status='complete', actual_identity=identity(), plan_sha256=sha256(PLAN),
                generation_sha256=sha256(RUN / 'generation.json'), cases=80, GPU_occupancy_seconds=duration,
                peak_allocated_bytes=torch.cuda.max_memory_allocated(), optimizer_updates=0, student_training_tokens=0,
                Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
                content_review_pending=True, protected_test_scored=False)
            atomic_json(RUN / 'result.json', result)
            job.update(status='complete', ended_at=now(), GPU_occupancy_seconds=duration)
            atomic_json(RUN / 'job.json', job)
            print(json.dumps(result))
    except BaseException as error:
        job.update(status='failed', error=repr(error), ended_at=now(), GPU_occupancy_seconds=time.monotonic() - started if started else 0)
        atomic_json(RUN / 'job.json', job)
        raise


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser = argparse.ArgumentParser()
    parser.add_argument('--inspect', action='store_true')
    args = parser.parse_args()
    inspect() if args.inspect else run()
