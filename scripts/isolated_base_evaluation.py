"""Prospective Base DEV generation/review using only pinned isolated inputs.

Legacy frozen experiments are preserved. Never fall back to their mixed-suite
reader. This module does not read checkpoints, TRAIN, TEST or dataset shards.
"""
import re

import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.evaluation_boundary import load_dev_suite,validate_dev_outputs

SUPPRESS_IDS=(0,1,2,4,5,6,7)


@torch.inference_mode()
def generate_isolated_dev(model,tok,manifest_path,manifest_sha256,heartbeat,check,device='cuda'):
    suite=load_dev_suite(manifest_path,manifest_sha256)
    rows=[]
    with sdpa_kernel(SDPBackend.MATH):
        for case in suite.cases:
            check()
            prefix=[2]+tok.encode(case['prefix'])[-959:]
            current=torch.tensor([prefix],device=device)
            cache=None;ids=[]
            for _ in range(64):
                check()
                with torch.autocast(str(device).split(':')[0],dtype=torch.bfloat16,
                        enabled=str(device).startswith('cuda')):
                    result=model(current,cache=cache,use_cache=True)
                cache=result.cache
                scores=result.logits[0,-1].clone()
                if not bool(torch.isfinite(scores).all()): raise ValueError('Nonfinite native logits')
                scores[list(SUPPRESS_IDS)]=-torch.inf
                token=int(scores.argmax());ids.append(token)
                if token==3:break
                current=torch.tensor([[token]],device=device)
            raw=tok.decode_bytes(ids)
            try:text,valid=raw.decode('utf-8'),True
            except UnicodeDecodeError:text,valid=raw.decode('utf-8',errors='replace'),False
            rows.append(dict(id=case['id'],category=case['category'],prefix=case['prefix'],
                split='dev',decoding='greedy',suppressed=True,seed=42,generated_ids=ids,
                text=text,valid_utf8=valid,raw_utf8_hex=raw.hex(),role_leak=any(i in (4,5,6,7) for i in ids),
                empty_response=not text.strip(),stop_reason='stop_id' if ids[-1]==3 else 'max_new_tokens',
                repetition=bool(re.search(r'(.{2,}?)\1\1',text,flags=re.DOTALL))))
            if len(rows)%8==0:heartbeat('isolated-generation80',completed_cases=len(rows))
    validate_dev_outputs(rows,suite)
    return dict(outputs=rows,max_new_tokens=64,split='dev',suite_sha256=suite.cases_sha256,
        suite_manifest_sha256=suite.manifest_sha256,source_legacy_suite_sha256=suite.source_legacy_suite_sha256,
        evaluation_read_paths=list(suite.opened_paths),TEST_opened=False,TEST_parsed=False,
        legacy_mixed_suite_opened=False)


def validate_isolated_generation(generation,manifest_path,manifest_sha256):
    suite=load_dev_suite(manifest_path,manifest_sha256)
    if (generation['suite_manifest_sha256']!=suite.manifest_sha256
            or generation['suite_sha256']!=suite.cases_sha256
            or generation['source_legacy_suite_sha256']!=suite.source_legacy_suite_sha256
            or generation['split']!='dev' or generation['max_new_tokens']!=64):
        raise ValueError('Isolated DEV generation provenance differs')
    validate_dev_outputs(generation['outputs'],suite)
    if (generation.get('TEST_opened') is not False or generation.get('TEST_parsed') is not False
            or generation.get('legacy_mixed_suite_opened') is not False
            or generation['evaluation_read_paths']!=list(suite.opened_paths)):
        raise ValueError('Unexpected evaluation read boundary')
    return suite
