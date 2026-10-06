"""Read-only source-matching preferences; no certified negative labels or training."""
import argparse
import gc
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.japanese_evaluation import NativeLikelihood
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, implementation_hashes, gpu_lock, seed_all, rng_state, restore_rng
from phase6_performance import alive, identity
from run_eos_short_pilot import equal_state

RUN = ROOT / 'reports/phase6/condition-source-ranking-20261006'
CONFIG = ROOT / 'configs/phase6/condition_source_ranking.json'
PROPOSAL = ROOT / 'reports/phase6/condition_diversity_source_ranking_proposal.json'
STUDY = ROOT / 'reports/phase6/condition-diversity-comparison-20261006'
ARMS = ('parent2B', 'control512', 'large2048')
MODES = ('original_history', 'isolated_condition')
METRICS = ('sum_log_likelihood', 'mean_token_log_likelihood', 'mean_byte_log_likelihood')
SOURCES = ('scripts/run_condition_source_ranking.py', 'scripts/run_condition_source_ranking.ps1',
           'scripts/review_condition_source_ranking.py', 'src/jmicro/japanese_evaluation.py',
           'src/jmicro/tokenizer.py', 'scripts/phase6_performance.py', 'scripts/run_eos_short_pilot.py')


def reference(path): return dict(path=str(path), sha256=sha256(path))


def check_reference(ref):
    if sha256(Path(ref['path'])) != ref['sha256']: raise ValueError('Frozen reference differs: ' + ref['path'])


def build_cases(proposal, tokenizer):
    families, cases = [], []
    for group in ('old512_fixed64', 'new1536_fixed64'):
        refs = proposal['pilot_groups'][group]
        pilot = read_json(Path(refs['pilot']['path'])); review = read_json(Path(refs['review']['path']))
        notes = {r['id']: r for r in review['notes']}
        if (len(pilot['rows']) != 64 or len(notes) != 64 or not review['all64_read']
                or review['content_pilot_sha256'] != refs['pilot']['sha256']
                or sum(n['weak_pair'] for n in notes.values()) != refs['weak_pairs']
                or {r['id'] for r in pilot['rows']} != set(notes)):
            raise ValueError('Original fixed64 content review differs')
        for row in pilot['rows']:
            text = row['original_text']; branches = row['branches']; choices = row['choices']; family = len(families)
            if (row['split'] != 'train' or len(branches) != 2 or len(choices) != 2 or choices[0] == choices[1]
                    or hashlib.sha256(text.encode()).hexdigest() != row['decoded_body_sha256']):
                raise ValueError('Exact original train text required')
            target_ids = [tokenizer.encode(choice) for choice in choices]
            if any(not ids or any(i < 8 for i in ids) or tokenizer.decode_bytes(ids) != choice.encode()
                   for ids, choice in zip(target_ids, choices, strict=True)):
                raise ValueError('Original candidate codec differs')
            families.append(dict(index=family, group=group, source=row, content_annotation=notes[row['id']]))
            for mode in MODES:
                for label, branch in enumerate(branches):
                    start, cut, end = branch['sentence_start'], branch['cut'], branch['end']
                    if (not 0 <= start < cut < end <= len(text) or branch['prefix'] != text[:cut]
                            or branch['outcome'] != text[cut:end] or choices[label] != branch['outcome']
                            or branch['condition_sentence'] != text[start:end]):
                        raise ValueError('Original branch byte/text offsets differ')
                    prefix = text[:cut] if mode == 'original_history' else text[start:cut]
                    prefix_ids = tokenizer.encode(prefix)
                    if tokenizer.decode_bytes(prefix_ids) != prefix.encode(): raise ValueError('Raw prefix changed by codec')
                    for candidate, choice in enumerate(choices):
                        # Separate piece encoding keeps the exact SAME target IDs under all contexts.
                        # It need not equal joint SentencePiece segmentation; retain this difference.
                        ids = [2, *prefix_ids, *target_ids[candidate]]
                        if len(ids)-1 > 1024: raise ValueError('No silent context/target truncation')
                        if tokenizer.decode_bytes(ids[1:]) != (prefix+choice).encode(): raise ValueError('Exact request bytes differ')
                        case = dict(index=len(cases), family=family, group=group, id=row['id'], mode=mode,
                            source_matching_label=label, candidate=candidate, prefix=prefix, outcome=choice,
                            ids=ids, context_tokens=len(prefix_ids)+1, target_ids=target_ids[candidate],
                            target_bytes=len(choice.encode()),
                            joint_tokenization_equal=tokenizer.encode(prefix+choice) == ids[1:])
                        cases.append(case)
    return dict(families=families, cases=cases)


def scope(c):
    if (c['kind'] != 'original_train_branch_ranking_read_only' or c['GPU_budget_seconds'] != 60
            or c['optimizer_updates'] != 0 or c['scientific_teacher_tokens'] != 0 or c['new_original_tokens'] != 0
            or c['protected_test_used'] or c['Base_adopted'] or c['Chat_started'] or c['quantization_started']
            or not c['quality_criteria_unchanged'] or set(c['checkpoints']) != set(ARMS)
            or c['families'] != 128 or c['cases'] != 1024 or c['batch'] != 16
            or c['dtype'] != 'bf16' or c['backend'] != 'math' or c['primary_metric'] != METRICS[0]):
        raise ValueError('Bounded Base-only read-only scope differs')


def freeze():
    if CONFIG.exists(): inspect(); return
    started = time.monotonic(); proposal = read_json(PROPOSAL)
    for ref in (proposal['evidence'], proposal['coverage'], *proposal['checkpoints'].values()): check_reference(ref)
    for group in proposal['pilot_groups'].values():
        for name in ('pilot', 'review'): check_reference(group[name])
    job = read_json(STUDY / 'job.json'); reviewed = read_json(STUDY / 'review.json')
    if (job['status'] != 'complete' or alive(job) or reviewed['protected_test_used']
            or reviewed['result_sha256'] != sha256(STUDY / 'compare-result.json')
            or proposal['GPU_budget_seconds'] != 60 or proposal['CPU_preparation_budget_seconds'] != 30
            or proposal['optimizer_updates'] != 0 or proposal['scientific_teacher_tokens'] != 0):
        raise ValueError('Completed previous study and bounded proposal required')
    base = read_json(ROOT / 'configs/phase6/textbook_quantity_comparison.json')
    tok_path = ROOT / base['tokenizer']; tokenizer = Tokenizer(tok_path)
    if sha256(tok_path) != base['tokenizer_sha256']: raise ValueError('Pinned Tokenizer changed')
    prepared = build_cases(proposal, tokenizer)
    if len(prepared['families']) != 128 or len(prepared['cases']) != 1024: raise ValueError('Fixed128 source coverage required')
    RUN.mkdir(parents=True, exist_ok=True); atomic_json(RUN / 'cases.json', prepared)
    elapsed = time.monotonic()-started
    if elapsed > 30: raise TimeoutError('Bounded CPU preparation30s exceeded')
    refs = dict(proposal=reference(PROPOSAL), cases=reference(RUN/'cases.json'),
        reviewed_comparison=proposal['evidence'], comparison_result=reference(STUDY/'compare-result.json'),
        original_recipe=reference(ROOT/'configs/phase6/textbook_quantity_comparison.json'))
    for group, values in proposal['pilot_groups'].items():
        for key in ('pilot', 'review'): refs[group+'_'+key] = values[key]
    c = dict(kind=proposal['kind'], GPU_budget_seconds=60, CPU_preparation_seconds=elapsed,
        families=128, cases=1024, batch=16, dtype='bf16', backend='math', primary_metric=METRICS[0],
        secondary_metrics=list(METRICS[1:]), checkpoints=proposal['checkpoints'], references=refs,
        tokenizer=reference(tok_path), source_sha256={p:sha256(ROOT/p) for p in SOURCES}, implementation=implementation_hashes(),
        optimizer_updates=0, scientific_teacher_tokens=0, new_original_tokens=0, protected_test_used=False,
        Base_adopted=False, Chat_started=False, quantization_started=False, quality_criteria_unchanged=True,
        old_numerical7_preserved=True, created_at=now(),
        protocol_clarification='Existing native semantics primary is summed LL, not mean-token LL as the proposal wording claimed. Sum remains primary, means are fixed sensitivities; no Base gate changed.',
        tokenization='Unchanged raw prefix and outcome encoded separately so each candidate has common target IDs. Exact concatenated UTF8 bytes checked. joint_tokenization_equal recorded; not asserted to be original whole-document token segmentation.',
        limitations=proposal['interpretation']+' Fixed previously selected train128, one learned seed; history removal is not a minimal causal intervention; source original matching is not incompatible-negative accuracy or fluent heldout generation.')
    scope(c); atomic_json(CONFIG,c); inspect()
    print(json.dumps(dict(status='frozen_fixed128_no_GPU',CPU_seconds=elapsed,joint_segmentation_differences=sum(not r['joint_tokenization_equal'] for r in prepared['cases']))),flush=True)


def inspect():
    c=read_json(CONFIG); scope(c)
    if c['implementation'] != implementation_hashes(): raise ValueError('Core changed')
    for relative,digest in c['source_sha256'].items():
        if sha256(ROOT/relative) != digest: raise ValueError('Diagnostic source changed: '+relative)
    for ref in (*c['references'].values(),*c['checkpoints'].values(),c['tokenizer']): check_reference(ref)
    for path in (STUDY/'job.json',RUN/'job.json'):
        if path.exists() and alive(read_json(path)): raise ValueError('Actual existing diagnostic/study live; no duplicate GPU')
    prepared=read_json(RUN/'cases.json')
    if prepared != build_cases(read_json(PROPOSAL),Tokenizer(c['tokenizer']['path'])): raise ValueError('Frozen raw cases differ')
    return c,prepared


def validate_scores(scores,cases):
    if len(scores)!=len(cases): raise ValueError('Missing target scores')
    for score,case in zip(scores,cases,strict=True):
        if (score['index']!=case['index'] or score['target_ids']!=case['target_ids']
                or score['target_tokens']!=len(case['target_ids']) or score['target_bytes']!=case['target_bytes']
                or len(score['token_nll'])!=len(case['target_ids'])
                or not all(math.isfinite(n) and n>=0 for n in score['token_nll'])
                or not math.isclose(score['log_likelihood'],-sum(score['token_nll']),abs_tol=1e-10)):
            raise ValueError('Actual finite common targets/LL differ')


def metric_value(row,metric):
    ll=row['log_likelihood']
    return ll if metric==METRICS[0] else ll/row['target_tokens'] if metric==METRICS[1] else ll/row['target_bytes']


def summarize(rows,prepared,arms=ARMS):
    cases=prepared['cases']; families=prepared['families']; keyed={(r['checkpoint'],r['index']):r for r in rows}
    if len(rows)!=len(keyed) or set(keyed)!={(a,c['index']) for a in arms for c in cases}: raise ValueError('All model/case scores required')
    for arm in arms: validate_scores([keyed[(arm,c['index'])] for c in cases],cases)
    case_key={(c['family'],c['mode'],c['source_matching_label'],c['candidate']):c['index'] for c in cases}
    report={}; pair_rows=[]
    for arm in arms:
        report[arm]={}
        for mode in MODES:
            report[arm][mode]={}
            for metric in METRICS:
                pairs=[]
                for family in families:
                    margins=[]; credits=[]; winners=[]
                    for label in (0,1):
                        values=[metric_value(keyed[(arm,case_key[(family['index'],mode,label,i)])],metric) for i in (0,1)]
                        win=[i for i in (0,1) if values[i]==max(values)]; winners.append(win)
                        margins.append(values[0]-values[1]); credits.append(int(label in win)/len(win))
                    row=dict(checkpoint=arm,mode=mode,metric=metric,family=family['index'],group=family['group'],
                        id=family['source']['id'],weak=family['content_annotation']['weak_pair'],credits=credits,
                        margins_candidate0_minus1=margins,context_margin_shift=margins[0]-margins[1],
                        both_source_matches=all(x==1 for x in credits),same_unique_candidate=len(winners[0])==len(winners[1])==1 and winners[0]==winners[1],
                        any_tie=any(len(x)>1 for x in winners))
                    pairs.append(row); pair_rows.append(row)
                report[arm][mode][metric]={}
                for subset in ('all128','nonweak116','old512_fixed64','new1536_fixed64'):
                    selected=[r for r in pairs if subset=='all128' or (subset=='nonweak116' and not r['weak']) or r['group']==subset]
                    shifts=sorted(r['context_margin_shift'] for r in selected); n=len(selected)
                    report[arm][mode][metric][subset]=dict(families=n,source_matching_fraction=sum(sum(r['credits']) for r in selected)/(2*n),
                        both_source_matches=sum(r['both_source_matches'] for r in selected),
                        same_unique_candidate=sum(r['same_unique_candidate'] for r in selected),ties=sum(r['any_tie'] for r in selected),
                        aligned_context_margin_shift=sum(r['context_margin_shift']>0 for r in selected),
                        median_context_margin_shift=(shifts[(n-1)//2]+shifts[n//2])/2)
    return dict(aggregate=report,pair_rows=pair_rows)


def run():
    c,prepared=inspect(); path=RUN/'job.json'; config_sha=sha256(CONFIG); old=read_json(path) if path.exists() else {}
    if old and old['config_sha256']!=config_sha: raise ValueError('Prior diagnostic binding differs')
    if old.get('status')=='complete': print('Completed diagnostic retained; no duplicate GPU'); return
    prior=old.get('GPU_elapsed_seconds',0.); started=[None]; stopped=[False]
    job=dict(status='setup',**identity(),config_sha256=config_sha,started_at=old.get('started_at',now()),
        GPU_elapsed_seconds=prior,GPU_budget_seconds=60,optimizer_updates=0,scientific_teacher_tokens=0,protected_test_used=False,
        restart_command='scripts/run_condition_source_ranking.ps1 -Worker')
    for sig in (signal.SIGINT,signal.SIGTERM): signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]: raise InterruptedError('Interrupted; full batch scores retained')
        if started[0] is not None and prior+time.monotonic()-started[0]>60: raise TimeoutError('Cumulative diagnostic GPU60s exhausted')
    def heartbeat(**values):
        check(); job.update(heartbeat_at=now(),**values)
        if started[0] is not None: job['GPU_elapsed_seconds']=prior+time.monotonic()-started[0]
        atomic_json(path,job)
    try:
        heartbeat(stage='setup')
        for rel in (*SOURCES,*c['implementation'],CONFIG.relative_to(ROOT).as_posix()):
            dest=RUN/'source'/rel; dest.parent.mkdir(parents=True,exist_ok=True)
            if dest.exists() and dest.read_bytes()!=(ROOT/rel).read_bytes(): raise ValueError('Source snapshot differs')
            if not dest.exists(): shutil.copyfile(ROOT/rel,dest)
        torch.set_num_threads(2); seed_all(42); torch.use_deterministic_algorithms(True); all_rows=[]; checks={}
        with gpu_lock('cuda'):
            started[0]=time.monotonic()
            for arm in ARMS:
                ref=c['checkpoints'][arm]; check(); state=torch.load(ref['path'],map_location='cpu',weights_only=False)
                before_rng=rng_state(); model=JMicroModel(state['model_config']).to('cuda').eval(); model.load_state_dict(state['model'],strict=True)
                before={k:v.detach().cpu().clone() for k,v in model.state_dict().items()}
                scorer=NativeLikelihood(model,None,'cuda','bf16',c['batch']); hook=model.register_forward_pre_hook(lambda *_:check())
                with sdpa_kernel(SDPBackend.MATH):
                    for start in range(0,len(prepared['cases']),c['batch']):
                        cases=prepared['cases'][start:start+c['batch']]; output=RUN/'outputs'/arm/f'{start:04d}.json'
                        if output.exists():
                            saved=read_json(output)
                            if (saved['config_sha256']!=config_sha or saved['checkpoint_sha256']!=ref['sha256']
                                    or saved['cases_sha256']!=c['references']['cases']['sha256']): raise ValueError('Saved batch binding differs')
                            scored=saved['rows']
                        else:
                            scored=[dict(index=case['index'],**score) for case,score in zip(cases,scorer.score_encoded(cases),strict=True)]
                            validate_scores(scored,cases)
                            atomic_json(output,dict(config_sha256=config_sha,checkpoint_sha256=ref['sha256'],cases_sha256=c['references']['cases']['sha256'],rows=scored))
                        validate_scores(scored,cases); all_rows.extend(dict(checkpoint=arm,**r) for r in scored)
                        heartbeat(status='running',stage=arm,completed_requests=len(all_rows),total_requests=3072)
                    one=scorer.score_encoded(prepared['cases'][:1])[0]
                    batched=next(r for r in all_rows if r['checkpoint']==arm and r['index']==0)
                    spot=max(abs(x-y) for x,y in zip(one['token_nll'],batched['token_nll'],strict=True))
                hook.remove(); restore_rng(before_rng)
                checks[arm]=dict(weights_unchanged=all(torch.equal(before[k],v.detach().cpu()) for k,v in model.state_dict().items()),
                    RNG_restored=equal_state(before_rng,rng_state()),no_gradients=all(p.grad is None for p in model.parameters()),eval_mode=not model.training)
                if not all(checks[arm].values()): raise ValueError('Read-only invariants failed')
                checks[arm]['first_request_batched_vs_single_max_NLL_difference']=spot
                del state,model,before,scorer; gc.collect(); torch.cuda.empty_cache()
                print(json.dumps(dict(checkpoint=arm,requests=1024,GPU_seconds=job['GPU_elapsed_seconds'])),flush=True)
            summary=summarize(all_rows,prepared); torch.cuda.synchronize(); check(); elapsed=prior+time.monotonic()-started[0]
            atomic_json(RUN/'result.json',dict(status='actual_all128_train_source_pairs_3_weights_2_contexts_complete',config_sha256=config_sha,
                checks=checks,summary=summary,GPU_seconds=elapsed,evaluated_requests=3072,
                optimizer_updates=0,scientific_teacher_tokens=0,new_original_tokens=0,protected_test_used=False,
                Base_adopted=False,Chat_started=False,quantization_started=False,quality_criteria_unchanged=True,
                old_numerical7_preserved=True,limitations=c['limitations'],tokenization=c['tokenization'],completed_at=now()))
            heartbeat(status='complete',stage='complete',completed_at=now())
    except BaseException as error:
        job.update(status='failed',error=repr(error)); raise
    finally:
        if started[0] is not None: job['GPU_elapsed_seconds']=prior+time.monotonic()-started[0]
        atomic_json(path,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser(); mode=p.add_mutually_exclusive_group(); mode.add_argument('--freeze',action='store_true'); mode.add_argument('--inspect',action='store_true')
    args=p.parse_args()
    if args.freeze: freeze()
    elif args.inspect:
        c,_=inspect(); print(json.dumps(dict(status='preflight_passed',families=128,requests=3072,GPU_budget_seconds=60)))
    else: run()
