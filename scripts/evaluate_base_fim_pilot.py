"""Checkpoint-bound DEV256/isolated80 evaluation for this prospective pilot.

No mixed semantic/Base reader, diagnostic source enumeration or TEST file.
"""
import json
from pathlib import Path

import torch
from torch.nn.attention import sdpa_kernel, SDPBackend
from base_fim_pilot_protocol import EvaluationReadGuard, validate_body, validate_raw, rates
from isolated_base_evaluation import generate_isolated_dev, validate_isolated_generation
from jmicro.evaluation_boundary import load_dev_suite
from jmicro.phase5 import equal_state
from jmicro.shards import Shard
from jmicro.readiness import evaluate_batched
from jmicro.training import atomic_json, rng_state, restore_rng
from jmicro.experiment import sha256


def evaluate(trainer,contract,record,output,heartbeat,check):
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    suite_path=Path(contract['DEV_manifest']['path']);suite_pin=contract['DEV_manifest']['sha256']
    data=Path(contract['DEV_shards']['path'])
    allowed=[suite_path,suite_path.parent/'base.dev.jsonl',data/'manifest.json',
             data/'dev.index.json',data/'dev.bin',data/'token_bytes.json']
    guard=EvaluationReadGuard([suite_path.parent.parent,data.parent.parent.parent],allowed)
    model=trainer.model;mode=model.training;before=rng_state()
    try:
        with guard,sdpa_kernel(SDPBackend.MATH):
            suite=load_dev_suite(suite_path,suite_pin)
            if sha256(data/'manifest.json')!=contract['DEV_shards']['manifest_sha256']:
                raise ValueError('Frozen DEV shard manifest differs')
            dev=Shard(data,'dev')
            if any(r['split']!='dev' for r in dev.index[:256]):raise ValueError('DEV index contains a foreign split')
            model.eval();check()
            body=evaluate_batched(model,dev,'cuda','bf16',limit=256,batch=16,
                progress=lambda done,total:(check(),heartbeat('DEV256',completed=done,total=total)))
            validate_body(body)
            generation=generate_isolated_dev(model,trainer.sampler.tokenizer,suite_path,suite_pin,heartbeat,check)
            generation.update(binding=record['binding'],checkpoint_sha256=record['checkpoint_sha256'])
            validate_isolated_generation(generation,suite_path,suite_pin)
            validate_raw(generation['outputs'],trainer.sampler.tokenizer,suite)
            atomic_json(output/'generation.json',generation)
        after=rng_state()
        if not equal_state(before,after):raise ValueError('Evaluation changed actual training RNG')
        result=dict(status='complete',checkpoint_sha256=record['checkpoint_sha256'],binding=record['binding'],
            body=body,outputs=generation['outputs'],greedy_rates=rates(generation['outputs']),
            generation_sha256=sha256(output/'generation.json'),evaluation_RNG_isolated=True,
            evaluation_read_paths=guard.paths,TEST_opened=False,legacy_mixed_suite_opened=False,
            split='dev',Base_adopted=False)
        atomic_json(output/'result.json',result)
        return result
    finally:
        model.train(mode);restore_rng(before)
