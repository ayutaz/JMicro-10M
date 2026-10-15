"""DEV-only full-corpus/440 raw evaluation, without checkpoint qualification.

The future owned runner must qualify the main recipe and independent learned
pipeline, freeze resources, load the checkpoint and persist/review results.
This component never adopts a Base, opens TEST or changes decoding policy.
"""
import copy
from dataclasses import dataclass
import math
import os
from pathlib import Path
import sys

import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.continuation_requests import load_requests,preflight_context,validate_outputs
from jmicro.evaluation_boundary import require_digest,reject_symlinks
from jmicro.experiment import sha256
from jmicro.isolated_continuations import generate_isolated_continuations,raw_record
from jmicro.japanese_evaluation import repetition_metrics
from jmicro.phase5 import equal_state
from jmicro.readiness import evaluate_batched
from jmicro.shards import Shard
from jmicro.training import rng_state,restore_rng

PROJECT_MANIFEST = '75c7420a1434cf8a97797218b163c694a13ed838f389f09327dcc86f7164c12c'
PROJECT_TOKENIZER = 'a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'
PROJECT_COUNTS = (89416,42003934,164344743)
RAW_FIELDS = ('id','category','prefix','split','decoding','suppressed','seed','generated_ids',
    'text','valid_utf8','raw_utf8_hex','role_leak','empty_response','stop_reason','repetition')


class ReadOnlyDevGuard:
    """Python-open audit only, not an OS sandbox for native-library I/O."""
    def __init__(self,roots,allowed):
        for p in allowed:
            reject_symlinks(p)
        self.roots = tuple(Path(p).resolve() for p in roots)
        self.allowed = {str(Path(p).resolve()) for p in allowed}
        self.paths,self.active = [],False
        sys.addaudithook(self.audit)

    def audit(self,event,args):
        if not self.active or event != 'open' or not isinstance(args[0],(str,bytes)):
            return
        path = Path(os.fsdecode(args[0])).resolve()
        if any(path.is_relative_to(root) for root in self.roots):
            writing = any(c in (args[1] or '') for c in 'wax+') or bool(
                args[2] & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND))
            if writing or str(path) not in self.allowed:
                raise ValueError('Outside read-only DEV evaluation boundary: '+str(path))
            self.paths.append(str(path))

    def __enter__(self):
        self.active = True
        return self

    def __exit__(self,*args):
        self.active = False


@dataclass(frozen=True)
class DevCorpusSpec:
    directory: Path
    manifest_sha256: str
    tokenizer_sha256: str
    vocab_size: int
    documents: int
    body_tokens: int
    body_bytes: int

    def __post_init__(self):
        require_digest(self.manifest_sha256)
        require_digest(self.tokenizer_sha256)
        if any(type(v) is not int or v <= 0 for v in (
                self.vocab_size,self.documents,self.body_tokens,self.body_bytes)):
            raise ValueError('Positive exact DEV counts and vocabulary required')

    @property
    def project_identity(self):
        return (self.manifest_sha256 == PROJECT_MANIFEST and self.tokenizer_sha256 == PROJECT_TOKENIZER
            and self.vocab_size == 4096
            and (self.documents,self.body_tokens,self.body_bytes) == PROJECT_COUNTS)


def project_corpus(directory):
    return DevCorpusSpec(Path(directory),PROJECT_MANIFEST,PROJECT_TOKENIZER,4096,*PROJECT_COUNTS)


def validate_corpus(shard,spec):
    manifest = shard.manifest
    details = manifest['splits']['dev']
    if (shard.split != 'dev' or manifest['dtype'] != '<u2' or manifest['kind'] != 'web'
            or manifest['version'] != 1 or manifest['tokenizer_sha256'] != spec.tokenizer_sha256
            or manifest['vocab_size'] != spec.vocab_size or manifest['limit_per_split'] is not None
            or details['documents'] != spec.documents or len(shard.index) != spec.documents
            or details['body_bytes'] != spec.body_bytes
            or details['tokens'] != spec.body_tokens+2*spec.documents):
        raise ValueError('Pinned full DEV identity/counts differ; no subset or TEST fallback')
    seen,offset,body,bytes_ = set(),0,0,0
    for row in shard.index:
        if (row['split'] != 'dev' or row['kind'] != 'web' or not isinstance(row['doc_id'],str)
                or not row['doc_id'] or row['doc_id'] in seen or type(row['offset']) is not int
                or type(row['body_tokens']) is not int or row['body_tokens'] <= 0
                or type(row['bytes']) is not int or row['bytes'] <= 0 or row['offset'] != offset):
            raise ValueError('Unique contiguous original DEV documents required')
        seen.add(row['doc_id'])
        offset += row['body_tokens']+2
        body += row['body_tokens']
        bytes_ += row['bytes']
    if offset != details['tokens'] or body != spec.body_tokens or bytes_ != spec.body_bytes:
        raise ValueError('All original DEV documents/bytes/body tokens must be conserved')


def validate_body(body,spec,index):
    rows = body['rows']
    if (body['split'] != 'dev' or body['limit_documents'] is not None
            or body['context'] != 1024 or body['stride'] != 512 or body['batch'] != 16
            or body['documents'] != len(rows) or len(rows) != spec.documents
            or len({r['doc_id'] for r in rows}) != len(rows)
            or len(index) != len(rows)
            or any((r['doc_id'],r['body_tokens'],r['body_bytes']) !=
                   (source['doc_id'],source['body_tokens'],source['bytes'])
                   for r,source in zip(rows,index,strict=True))
            or not all(math.isfinite(body[k]) and body[k] >= 0 for k in ('body_nll','eos_nll','bpb','seconds'))
            or any(r['body_tokens'] != r['scored_body_tokens'] or r['body_tokens'] <= 0
                or r['body_bytes'] <= 0 or not math.isfinite(r['body_nll']) or r['body_nll'] < 0
                or not math.isfinite(r['eos_nll']) or r['eos_nll'] < 0 for r in rows)
            or body['body_bytes'] != sum(r['body_bytes'] for r in rows) or body['body_bytes'] != spec.body_bytes
            or body['body_tokens'] != sum(r['body_tokens'] for r in rows) or body['body_tokens'] != spec.body_tokens
            or not math.isclose(body['body_nll'],sum(r['body_nll'] for r in rows),rel_tol=1e-12,abs_tol=0.)
            or not math.isclose(body['eos_nll'],sum(r['eos_nll'] for r in rows),rel_tol=1e-12,abs_tol=0.)
            or not math.isclose(body['bpb'],body['body_nll']/math.log(2)/body['body_bytes'],rel_tol=1e-12,abs_tol=0.)):
        raise ValueError('Full DEV common-byte BPB/body-once/EOS-separate evidence required')


def validate_continuations(bundle,planned,tokenizer):
    for name,rows in (('standard400',bundle['standard']['outputs']),('long40',bundle['long']['rows'])):
        validate_outputs(rows,planned,name)
        requests = [r for r in planned if r.stage == name]
        for row,request in zip(rows,requests,strict=True):
            ids = row['generated_ids']
            if (not isinstance(ids,list) or not 0 < len(ids) <= request.max_new_tokens
                    or any(type(t) is not int or not 0 <= t < tokenizer.vocab_size for t in ids)
                    or 3 in ids[:-1]):
                raise ValueError('Complete bounded original raw token sequences required')
            expected = raw_record(request,ids,tokenizer)
            if any(row.get(k) != v for k,v in expected.items()):
                raise ValueError('Actual raw bytes/UNK/Unicode/role/stop/repetition failure must be retained')
            if name == 'long40' and not equal_state(row['metrics'],repetition_metrics(row)):
                raise ValueError('Original long-generation metrics changed')


def fixed80_comparison(standard,screen):
    current = [r for r in standard if r['decoding'] == 'greedy' and r['suppressed']]
    expected = screen['outputs']
    if (len(current) != 80 or len(expected) != 80 or len({r['id'] for r in expected}) != 80
            or [r['id'] for r in current] != [r['id'] for r in expected]):
        raise ValueError('All same-checkpoint fixed80 screen rows in original order required')
    mismatches = []
    for row,prior in zip(current,expected,strict=True):
        fields = [k for k in RAW_FIELDS if row.get(k) != prior.get(k)]
        if fields:
            mismatches.append(dict(id=row['id'],differing_fields=fields))
    return dict(passed=not mismatches,compared=80,mismatches=mismatches,
        policy='Full suite suppresses six original IDs; newer pilot additionally suppresses EOT7. Never harmonize them to hide a mismatch.')


def validate_screen(screen,planned,tokenizer):
    expected = [r for r in planned if r.stage == 'standard400' and r.decoding == 'greedy' and r.suppressed]
    rows = screen.get('outputs',[])
    if len(rows) != 80:
        raise ValueError('The complete fixed80 screen is required before full-corpus scoring')
    for row,request in zip(rows,expected,strict=True):
        ids = row.get('generated_ids',[])
        if (not isinstance(ids,list) or not 0 < len(ids) <= 64 or 3 in ids[:-1]
                or any(type(t) is not int or not 0 <= t < tokenizer.vocab_size for t in ids)):
            raise ValueError('Bounded actual raw screen token sequences required')
        raw = raw_record(request,ids,tokenizer)
        if any(row.get(k) != raw[k] for k in RAW_FIELDS):
            raise ValueError('Original fixed80 request order/raw bytes/failures must be bound before corpus scoring')


def evaluate_isolated_full_dev(model,tokenizer,spec,manifest,pin,screen,binding,check,progress,device='cuda'):
    """Return raw evidence only; caller owns qualification/lock/budget/storage.

    Synthetic fixture corpora can exercise the same component but cannot set
    project_full_corpus_scored. Screen mismatch is returned with all440 raw
    outputs, allowing the owner to save failures before refusing advancement.
    """
    if model.training or model.config['max_position_embeddings'] != 1024:
        raise ValueError('Original-context eval-mode model required before data reads')
    require_digest(pin)
    require_digest(binding['checkpoint_sha256'])
    require_digest(binding['config_sha256'])
    if screen.get('checkpoint_sha256') != binding['checkpoint_sha256'] or screen.get('max_new_tokens') != 64:
        raise ValueError('The actual same-checkpoint fixed64 screen must be bound before data reads')
    manifest = Path(manifest)
    if manifest.name != 'base.dev.manifest.json' or tokenizer.vocab_size != spec.vocab_size:
        raise ValueError('Only isolated DEV inputs and the unchanged native vocabulary are permitted')
    check()
    data = Path(spec.directory)
    allowed = [data/n for n in ('manifest.json','dev.index.json','dev.bin','token_bytes.json')]
    allowed += [manifest,manifest.parent/'base.dev.jsonl']
    guard = ReadOnlyDevGuard((data,manifest.parent),allowed)
    before,mode = rng_state(),model.training
    def before_forward(*args):
        check()
    hook = model.register_forward_pre_hook(before_forward)
    try:
        with guard,sdpa_kernel(SDPBackend.MATH):
            planned,provenance = load_requests(manifest,pin)
            preflight_context(planned,tokenizer)
            validate_screen(screen,planned,tokenizer)
            if sha256(data/'manifest.json') != spec.manifest_sha256:
                raise ValueError('Externally pinned DEV corpus manifest differs')
            shard = Shard(data,'dev')
            validate_corpus(shard,spec)
            check()
            body = evaluate_batched(model,shard,device,'bf16' if str(device).startswith('cuda') else 'fp32',
                limit=None,context=1024,batch=16,progress=lambda n,total:(check(),progress('fullDEV_body',n,total)))
            validate_body(body,spec,shard.index)
            continuation = generate_isolated_continuations(model,tokenizer,manifest,pin,check,progress,device=device)
            validate_continuations(continuation,planned,tokenizer)
            fixed = fixed80_comparison(continuation['standard']['outputs'],screen)
            check()
        if not equal_state(before,rng_state()) or model.training:
            raise ValueError('Actual global RNG/eval mode changed during full DEV evaluation')
        return dict(status='raw_full_supplied_DEV_corpus_and440_evaluation_complete',binding=copy.deepcopy(binding),
            body=body,generation=continuation['standard'],long_generation=continuation['long'],
            input_provenance=provenance,corpus_manifest_sha256=spec.manifest_sha256,
            project_full_corpus_scored=spec.project_identity,fixed80_screen_comparison=fixed,
            raw_failures={key:dict(unicode=sum(not r['valid_utf8'] for r in rows),
                empty=sum(r['empty_response'] for r in rows),role_leak=sum(r['role_leak'] for r in rows))
                for key,rows in (('standard400',continuation['standard']['outputs']),('long40',continuation['long']['rows']))},
            evaluation_read_paths=sorted(set(guard.paths)),evaluation_RNG_isolated=True,
            TEST_opened=False,legacy_mixed_suite_opened=False,additional_training_tokens=0,
            content_review_completed=False,qualification_checked=False,independent_training_checked=False,
            Base_qualified=False,Base_adopted=False,full_four_item_goal_complete=False)
    finally:
        hook.remove()
        restore_rng(before)
        model.train(mode)
