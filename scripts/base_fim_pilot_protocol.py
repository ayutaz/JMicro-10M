"""Exact fresh FIM pilot contracts; no legacy mixed evaluation readers."""
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import re
import sys

import numpy as np
from jmicro.evaluation_boundary import load_dev_suite, validate_dev_outputs, reject_symlinks

DEV_PIN='6198b43df8f4cf389e9de74c038e2e93d18665413477b27359ab352a02f69fa7'
UPDATES=10000
TEACHERS=94160195


def validate_body(body):
    rows=body['rows']
    if (body['split']!='dev' or body['documents']!=len(rows)
            or len(rows)!=256 or body['limit_documents']!=256 or body['context']!=1024
            or body['body_bytes']!=472055 or body['body_tokens']!=122343
            or len({r['doc_id'] for r in rows})!=256
            or any(r['body_tokens']!=r['scored_body_tokens'] or not math.isfinite(r['body_nll'])
                   or not math.isfinite(r['eos_nll']) for r in rows)
            or sum(r['body_bytes'] for r in rows)!=body['body_bytes']
            or sum(r['body_tokens'] for r in rows)!=body['body_tokens']
            or not math.isclose(sum(r['body_nll'] for r in rows),body['body_nll'],rel_tol=1e-12)
            or not math.isclose(body['bpb'],body['body_nll']/math.log(2)/body['body_bytes'],rel_tol=1e-12)):
        raise ValueError('Exact matched DEV256 body scope/NLL/bytes required')


def validate_raw(rows,codec,suite):
    validate_dev_outputs(rows,suite)
    for r in rows:
        ids=r['generated_ids']
        if (not 1<=len(ids)<=64 or any(type(i)is not int or not 0<=i<codec.vocab_size for i in ids)
                or r['decoding']!='greedy' or r['suppressed'] is not True or r['seed']!=42
                or any(i in (0,1,2,4,5,6,7) for i in ids)
                or 3 in ids[:-1]): raise ValueError('Exact raw native greedy64/suppression contract required')
        raw=codec.decode_bytes(ids)
        try:text,valid=raw.decode('utf-8'),True
        except UnicodeDecodeError:text,valid=raw.decode('utf-8',errors='replace'),False
        expected=dict(text=text,valid_utf8=valid,role_leak=False,empty_response=not text.strip(),
            stop_reason='stop_id' if ids[-1]==3 else 'max_new_tokens',
            repetition=bool(re.search(r'(.{2,}?)\1\1',text,flags=re.DOTALL)))
        if any(r.get(k)!=v for k,v in expected.items()):raise ValueError('Raw generation flags/text differ')
        if 'raw_utf8_hex' in r and r['raw_utf8_hex']!=raw.hex():raise ValueError('Original UTF8 bytes differ')


def rates(rows):
    return dict(outputs=len(rows),eos=sum(r['stop_reason']=='stop_id' for r in rows),
        repetition=sum(r['repetition'] for r in rows),unicode_failure=sum(not r['valid_utf8'] for r in rows),
        role_leak=sum(r['role_leak'] for r in rows),empty=sum(r['empty_response'] for r in rows),
        FIM_marker_leak=sum('[FIM_' in r['text'] for r in rows))


def notes_scores(rows,notes,pin):
    if (notes.get('generation_sha256')!=pin or notes.get('independent_human_blind') is not False
            or not isinstance(notes.get('reviewer'),str) or not notes['reviewer'].strip()):
        raise ValueError('Raw-bound individual notes and actual reviewer declaration required')
    scores={}
    for n in notes.get('notes',[]):
        if (len(n)!=6 or n[0] in scores or any(type(v)is not int or v not in (0,1,2) for v in n[1:4])
                or type(n[4])is not int or n[4] not in (0,1) or not isinstance(n[5],str)
                or len(n[5].strip())<12):raise ValueError('80 unique reasoned content notes required')
        scores[n[0]]=dict(grammar=n[1],relevance=n[2],coherence=n[3],completion=n[4],rationale=n[5])
    if len(scores)!=80 or set(scores)!={r['id'] for r in rows}:raise ValueError('All80 content notes required')
    for r in rows:
        s=scores[r['id']]
        if s['completion'] and (r['stop_reason']!='stop_id' or s['relevance']<1 or s['coherence']<1):
            raise ValueError('Appropriate completion needs actual EOS and relevant coherent content')
    return scores


def quality(control,candidate,a,b):
    if len(a)!=80 or set(a)!=set(b):raise ValueError('Paired80 scores required')
    delta=np.array([int(b[k]['coherence']==2)-int(a[k]['coherence']==2) for k in sorted(a)])
    rng=np.random.default_rng(42)
    ci=np.quantile(delta[rng.integers(0,80,size=(2000,80))].mean(axis=1),[.025,.975]).tolist()
    left,right=rates(control['outputs']),rates(candidate['outputs'])
    checks=dict(coherence_gain_at_least8=int(delta.sum())>=8,paired_CI_lower_above0=ci[0]>0,
        grammar_no_worse=sum(s['grammar']==2 for s in b.values())>=sum(s['grammar']==2 for s in a.values()),
        appropriate_no_worse=sum(s['completion'] for s in b.values())>=sum(s['completion'] for s in a.values()),
        EOS_no_worse=right['eos']>=left['eos'],repetition_no_worse=right['repetition']<=left['repetition'],
        no_empty_role_Unicode_marker=all(right[k]==0 for k in ('empty','role_leak','unicode_failure','FIM_marker_leak')),
        matched_BPB_guard=candidate['body']['bpb']<=control['body']['bpb']*1.01)
    return dict(checks=checks,passed=all(checks.values()),difference_count=int(delta.sum()),CI95=ci,
        bootstrap_seed=42,bootstrap_repetitions=2000,Base_qualified=False)


class EvaluationReadGuard:
    """Audit Python open events in sensitive eval/data roots, including NumPy.

    Not an OS sandbox; native libraries outside Python audit hooks are not
    covered. Native scoring uses known Python file reads and memmap opens.
    """
    def __init__(self,roots,allowed):
        self.roots=[Path(p).resolve() for p in roots]
        self.allowed={str(Path(p).resolve()) for p in allowed}
        for p in allowed:reject_symlinks(p)
        self.paths=[];self.active=False
        sys.addaudithook(self.audit)
    def audit(self,event,args):
        if not self.active or event!='open' or not isinstance(args[0],(str,bytes)):
            return
        p=Path(args[0].decode() if isinstance(args[0],bytes) else args[0]).resolve()
        if any(p.is_relative_to(root) for root in self.roots):
            if str(p) not in self.allowed:raise ValueError('Forbidden DEV evaluation file read: '+str(p))
            self.paths.append(str(p))
    def __enter__(self):self.active=True;return self
    def __exit__(self,*args):self.active=False
