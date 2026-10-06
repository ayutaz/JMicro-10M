"""Read-only first usable prefix screen for a hypothetical frozen EOS head.

Manual choices are an optimistic diagnostic, not model-generated stopping, an
exhaustive oracle, revised primary scores or a mathematical quality bound.
"""
import hashlib
import json
import os
from pathlib import Path
import sys
import time

os.environ['CUDA_VISIBLE_DEVICES']=''
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn import functional as F
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from phase6_performance import identity
from review_eos_5b_finish import validate_rows

RAW=ROOT/'reports/phase6/story20-low-lr-10b-500m-20261005/evaluation/result/web/evaluation/generation.json'
EVALUATION=RAW.with_name('result.json')
NOTES=ROOT/'reports/phase6/stop_only_feasibility_observations.tsv'
OUTPUT=ROOT/'reports/phase6/stop_only_feasibility.json'
PARENT='d18e3e17b208237fdd5849ddea546ccfc6b6bea5f4325101577de2731bfac3d4'


def EOS_binary_loss(logits,targets,delta):
    """Full CE minus frozen conditional non-EOS CE; ignored rows stay ignored."""
    if logits.shape[:-1]!=targets.shape or delta.shape!=targets.shape or logits.shape[-1]<=3:
        raise ValueError('Aligned vocabulary logits/targets/correction required')
    active=targets.eq(3)|targets.ge(8)
    if not active.any():raise ValueError('No body/EOS labels')
    non_EOS=torch.cat((logits[...,:3],logits[...,4:]),dim=-1)
    odds=logits[...,3]-torch.logsumexp(non_EOS,dim=-1)+delta
    return F.binary_cross_entropy_with_logits(odds[active],targets[active].eq(3).to(odds.dtype))


def available_prefixes(row,tokenizer):
    result={}
    # An actual new EOS must itself fit the original64-token generation budget.
    for n in range(1,min(len(row['generated_ids']),63)+1):
        raw=tokenizer.decode_bytes(row['generated_ids'][:n])
        try:text=raw.decode('utf-8')
        except UnicodeDecodeError:continue
        result.setdefault(text.rstrip(),dict(text=text,body_tokens=n,raw_hex=raw.hex(),sha256=hashlib.sha256(raw).hexdigest()))
    return result


def main():
    started=time.monotonic();torch.set_num_threads(2)
    if OUTPUT.exists():raise ValueError('Preserve original fixed prefix screen')
    r=read_json(RAW);evaluation=read_json(EVALUATION);rows=r['outputs']
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model');validate_rows(rows,tok)
    if (evaluation['generation']!=r or evaluation['checkpoint_sha256']!=PARENT
            or r['max_new_tokens']!=64 or len(rows)!=80 or any(v['decoding']!='greedy' or not v['suppressed'] or v['split']!='dev' for v in rows)
            or evaluation['protected_test_used'] or not evaluation['evaluation_RNG_isolated']):
        raise ValueError('Original fixed actual greedy80 parent required')
    cases={json.loads(s)['id']:json.loads(s) for s in (ROOT/'eval/base.jsonl').read_text().splitlines() if json.loads(s)['split']=='dev'}
    if set(cases)!={v['id'] for v in rows} or any(v['prefix']!=cases[v['id']]['prefix'] for v in rows):
        raise ValueError('All original fixed dev prefixes required')
    notes={}
    for line in NOTES.read_text(encoding='utf-8').splitlines():
        fields=line.split('\t')
        if len(fields)!=6:raise ValueError('ID/text/grammar/relevance/coherence/rationale required')
        key,encoded_text,g,rel,coh,reason=fields;text=json.loads(encoded_text);values=[int(v) for v in (g,rel,coh)]
        if key in notes or not isinstance(text,str) or any(v not in (0,1,2) for v in values) or not reason.strip():
            raise ValueError('Unique separately scored individual choices required')
        notes[key]=dict(chosen_text=text,grammar=values[0],relevance=values[1],coherence=values[2],rationale=reason)
    if set(notes)!=set(cases):raise ValueError('All80 individual observations required')
    selected=[]
    for row in rows:
        note=notes[row['id']];prefixes=available_prefixes(row,tok);text=note['chosen_text']
        choice=prefixes.get(text) if text else None
        selected.append(dict(id=row['id'],prefix=row['prefix'],original_stop=row['stop_reason'],
            original_row_sha256=hashlib.sha256(json.dumps(row,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),
            **note,actual_token_boundary_available=choice is not None,actual_selected_prefix=choice,
            unknown_beyond_original_EOS=row['stop_reason']=='stop_id'))
    unknown=[v['id'] for v in selected if v['unknown_beyond_original_EOS']]
    successful=lambda v,k:v['actual_token_boundary_available'] and v[k]==2
    summary=dict(outputs=80,original_native_EOS=evaluation['greedy_rates']['eos'],
        original_repetition=evaluation['greedy_rates']['repetition'],
        manually_chosen_nonempty=sum(bool(v['chosen_text']) for v in selected),
        token_boundary_available=sum(v['actual_token_boundary_available'] for v in selected),
        grammar2=sum(successful(v,'grammar') for v in selected),relevance2=sum(successful(v,'relevance') for v in selected),
        coherence2=sum(successful(v,'coherence') for v in selected),
        hypothetical_complete_prefix=sum(v['actual_token_boundary_available'] and v['grammar']==2 and v['relevance']>=1 and v['coherence']>=1 for v in selected),
        unknown_after_original_EOS=unknown)
    # A prescreen, not replacement/relaxation of any original quality condition.
    marker=dict(grammar_at_least56=summary['grammar2']>=56,coherence_at_least31=summary['coherence2']>=31)
    elapsed=time.monotonic()-started
    if elapsed>60 or torch.cuda.is_initialized():raise RuntimeError('Bounded CPU-only no-inference assay required')
    result=dict(status='completed_cached_original80_first_usable_stop_prefix_screen',created_at=now(),actual_CPU_process=identity(),
        references={k:dict(path=str(p),sha256=sha256(p)) for k,p in dict(generation=RAW,evaluation=EVALUATION,observations=NOTES,
            tokenizer=ROOT/'artifacts/phase2/4096/tokenizer.model',source=Path(__file__),tests=ROOT/'reports/phase6/stop_only_feasibility_tests.xml').items()},
        parent_checkpoint_sha256=PARENT,summary=summary,rows=selected,predeclared_feasibility_marker=marker,
        marker_passed=all(marker.values()),CPU_seconds=elapsed,CPU_ceiling_seconds=60,GPU_seconds=0,forward_requests=0,
        new_scientific_teacher_tokens=0,optimizer_updates=0,new_original_corpus_tokens=0,
        mechanism='Hypothetical zero-initialized linear residual on native EOS3 logit, all native weights frozen. At any same history, non-EOS logits/order and conditional non-EOS probabilities stay unchanged; greedy body follows the original non-EOS path until stopping. Full CE head gradient equals binary EOS-vs-nonEOS CE gradient.',
        sources=['https://aclanthology.org/2020.blackboxnlp-1.26/','https://arxiv.org/abs/1903.00802'],
        limitations=['Manual first usable prefix choices are nonblind posthoc diagnostics, not learned termination, independent human evaluation, exhaustive stopping oracle or mathematical bound on grammar/meaning.',
            'A changed EOS head can extend past an original EOS; such unseen text remains unknown. This original fixed80 has no EOS, so its entire fixed64 greedy non-EOS path is already cached.',
            'Only actual token/UTF8 boundaries <=63 qualify. No token insertion, punctuation repair, altered prompts or free-running model evaluation is performed.',
            'The cited EOS work studies length extrapolation or encoder-decoder translation, not this Japanese10M head. This is a local transfer hypothesis.',
            'Failure ends this fixed stop-only feasibility route; it does not prove all termination methods, Japanese10M capacity or larger/diverse source routes impossible.'],
        next_action='If the marker fails, do not implement/train this frozen-body EOS-head-only route. Define a distinct intervention that can change body-token selection while explicitly retaining Web quality; no EOS threshold/bias/decoder or checkpoint-selection sweep. If supported, define train-only head training and an actual CUDA/budget/unchanged quality comparison before any learning.',
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True)
    atomic_json(OUTPUT,result);print(json.dumps(dict(summary=summary,marker=marker,CPU_seconds=elapsed),ensure_ascii=False))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
