"""Reuse completed Base evidence; no model forward pass or data scan."""
import codecs
import json
import math
from pathlib import Path
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import alive,identity
from analyze_condition_positive_pairs import pair_categories
import run_original_web_retention_comparison as study

RUN=ROOT/'reports/phase6/base-retention-endpoint-diagnostic-20261006'
PROPOSAL=ROOT/'reports/phase6/base_retention_endpoint_diagnostic_proposal.json'


def endpoint(data):
    decoder=codecs.getincrementaldecoder('utf-8')('strict')
    try:
        decoder.decode(data,final=False)
    except UnicodeDecodeError as error:
        return dict(kind='invalid_byte_sequence',start=error.start,end=error.end,reason=error.reason,
                    valid_prefix_bytes=error.start,trailing_bytes_hex=data[error.start:].hex())
    pending=decoder.getstate()[0]
    if pending:
        return dict(kind='unfinished_terminal_character',valid_prefix_bytes=len(data)-len(pending),
                    trailing_bytes_hex=pending.hex(),pending_bytes=len(pending))
    return dict(kind='complete_UTF8',valid_prefix_bytes=len(data),trailing_bytes_hex='',pending_bytes=0)


def paired_documents(old,new,parent):
    keys=lambda rows:[(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in rows]
    if keys(old)!=keys(new) or keys(old)!=keys(parent) or len({r['doc_id'] for r in old})!=len(old):
        raise ValueError('Identical ordered body targets required')
    if len(old)!=256 or any(r['body_bytes']<=0 or r['body_tokens']!=r['scored_body_tokens']
            or not all(math.isfinite(r[k]) for k in ('body_nll','eos_nll')) for rows in (old,new,parent) for r in rows):
        raise ValueError('All256 finite complete common-byte documents required')
    total_bytes=sum(r['body_bytes'] for r in old)
    order=sorted(range(256),key=lambda i:(old[i]['body_bytes'],old[i]['doc_id']))
    rows=[dict(doc_id=a['doc_id'],body_bytes=a['body_bytes'],body_tokens=a['body_tokens'],
        selected_Web_BPB=a['body_nll']/math.log(2)/a['body_bytes'],
        original_Web_BPB=b['body_nll']/math.log(2)/a['body_bytes'],
        parent_BPB=p['body_nll']/math.log(2)/a['body_bytes'],
        delta_nll=b['body_nll']-a['body_nll'],EOS_nll=dict(selected_Web=a['eos_nll'],original_Web=b['eos_nll'],parent=p['eos_nll']))
        for a,b,p in zip(old,new,parent,strict=True)]
    groups=[]
    for quartile in range(4):
        indices=order[64*quartile:64*(quartile+1)]
        byte_sum=sum(old[i]['body_bytes'] for i in indices)
        values={arm:sum(source[i]['body_nll'] for i in indices)/math.log(2)/byte_sum
                for arm,source in (('selected_Web',old),('original_Web',new),('parent',parent))}
        groups.append(dict(quartile=quartile+1,documents=64,body_bytes=byte_sum,
            min_document_bytes=old[indices[0]]['body_bytes'],max_document_bytes=old[indices[-1]]['body_bytes'],
            BPB=values,paired_BPB_difference=values['original_Web']-values['selected_Web'],
            global_BPB_difference_contribution=sum(rows[i]['delta_nll'] for i in indices)/math.log(2)/total_bytes,
            EOS_mean_nll={arm:sum(source[i]['eos_nll'] for i in indices)/64
                for arm,source in (('selected_Web',old),('original_Web',new),('parent',parent))}))
    delta=sum(r['delta_nll'] for r in rows)/math.log(2)/total_bytes
    if not math.isclose(delta,sum(g['global_BPB_difference_contribution'] for g in groups),abs_tol=1e-12):
        raise ValueError('Quartile contributions do not reconcile')
    return dict(documents=256,body_bytes=total_bytes,paired_BPB_difference=delta,
        original_Web_documents_improved=sum(r['delta_nll']<0 for r in rows),quartiles=groups,rows=rows,
        grouping='ascending common body bytes, stable DocID tie-break, four equal document-count groups')


def main():
    started=time.monotonic();p=read_json(PROPOSAL)
    if p['CPU_limit_seconds']!=30 or p['new_GPU_seconds'] or p['new_scientific_teacher_tokens']:
        raise ValueError('Bounded CPU-only proposal required')
    jp=RUN/'job.json'
    if jp.exists():raise ValueError('Preserve completed diagnosis; inspect job before retry')
    RUN.mkdir(parents=True,exist_ok=True)
    job=dict(status='running',**identity(),started_at=now(),proposal_sha256=sha256(PROPOSAL))
    atomic_json(jp,job)
    def check():
        if time.monotonic()-started>30:raise TimeoutError('CPU30s diagnostic budget exhausted')
    try:
        for ref in (p['result'],p['review']):study.check_reference(ref)
        c=read_json(study.CONFIG);r=read_json(Path(p['result']['path']))
        job_gpu=read_json(study.RUN/'job.json')
        study.check_reference(c['references']['control_result'])
        previous=read_json(Path(c['references']['control_result']['path']))
        if (job_gpu['status']!='complete' or alive(job_gpu) or r['config_sha256']!=sha256(study.CONFIG)
                or r['checkpoints']['control']!=previous['checkpoints']['relation']
                or r['evaluations']['control']!=previous['evaluations']['relation']
                or r['Base_adopted'] or r['protected_test_used']):
            raise ValueError('Completed unchanged Base-only study required')
        base=read_json(Path(c['original_config']['path']));tok=Tokenizer(ROOT/base['tokenizer'])
        if sha256(tok.path)!=base['tokenizer_sha256']:
            raise ValueError('Actual unchanged Tokenizer required')
        points=dict(parent=(previous['checkpoints']['parent10B'],previous['evaluations']['parent10B'],study.mature.RUN/'evaluation/parent10B/evaluation'),
            selected_Web=(r['checkpoints']['control'],r['evaluations']['control'],study.mature.RUN/'evaluation/relation/evaluation'),
            original_Web=(r['checkpoints'][study.ARM],r['evaluations'][study.ARM],study.RUN/f'evaluation/{study.ARM}/evaluation'))
        references=dict(proposal=study.reference(PROPOSAL),result=p['result'],review=p['review'],
            prior_result=c['references']['control_result'],tokenizer=study.reference(tok.path))
        endpoints,pairs={},{}
        suite=ROOT/base['evaluation']['semantic_suite']
        if sha256(suite)!=base['evaluation']['semantic_sha256']:raise ValueError('Semantic dev suite differs')
        cases={v['id']:v for v in (json.loads(line) for line in suite.read_text().splitlines()) if v['split']=='dev'}
        for arm,(record,ev,folder) in points.items():
            check();gen=read_json(folder/'generation.json')
            if gen!=ev['generation'] or len(gen['outputs'])!=80:raise ValueError('All80 bound generation required')
            entries=[]
            for row in gen['outputs']:
                data=tok.decode_bytes(row['generated_ids']);detail=endpoint(data)
                if data.decode('utf-8',errors='replace')!=row['text'] or (detail['kind']=='complete_UTF8')!=row['valid_utf8']:
                    raise ValueError('Generated IDs/bytes/text validity differs')
                entries.append(dict(id=row['id'],stop_reason=row['stop_reason'],raw_ids=row['generated_ids'],
                    raw_bytes_hex=data.hex(),raw_text=row['text'],endpoint=detail))
            endpoints[arm]=dict(outputs=80,counts={kind:sum(v['endpoint']['kind']==kind for v in entries)
                for kind in ('complete_UTF8','unfinished_terminal_character','invalid_byte_sequence')},rows=entries)
            sem=read_json(folder/'semantics.json');bound=json.loads(sem['binding']);rows=sem['rows']
            if (not sem['complete'] or sem['expected']!=192 or len(rows)!=192 or {v['id'] for v in rows}!=set(cases)
                    or len({v['id'] for v in rows})!=192 or bound['checkpoint_sha256']!=record['checkpoint_sha256']
                    or bound['binding']!=record['binding']
                    or any(any(v[k]!=cases[v['id']][k] for k in ('family','category','split','context','choices','label')) for v in rows)):
                raise ValueError('Exact192 cached semantic contexts and checkpoint required')
            pairs[arm]=pair_categories(rows)
            references[arm]=dict(generation=study.reference(folder/'generation.json'),semantics=study.reference(folder/'semantics.json'),
                checkpoint_sha256=record['checkpoint_sha256'])
        docs=paired_documents(points['selected_Web'][1]['body']['rows'],points['original_Web'][1]['body']['rows'],points['parent'][1]['body']['rows'])
        if docs['body_bytes']!=472055 or not math.isclose(docs['paired_BPB_difference'],
                points['original_Web'][1]['body']['bpb']-points['selected_Web'][1]['body']['bpb'],abs_tol=1e-12):
            raise ValueError('Original aggregate common-byte metrics differ')
        check()
        result=dict(status='actual_CPU_endpoint_paired256_and_fixeddev96_reuse_complete',created_at=now(),**identity(),
            references=references,endpoints=endpoints,paired_documents=docs,semantic_pairs=pairs,
            script_sha256=sha256(Path(__file__)),CPU_seconds=time.monotonic()-started,actual_GPU_seconds=0,
            scientific_teacher_tokens=0,protected_test_used=False,Base_adopted=False,Chat_started=False,quantization_started=False,
            frozen_scores_unchanged=True,limitations=p['limitations'])
        atomic_json(RUN/'result.json',result);atomic_json(ROOT/'reports/phase6/base_retention_endpoint_diagnostic.json',result)
        job.update(status='complete',completed_at=now(),CPU_seconds=result['CPU_seconds'],result_sha256=sha256(RUN/'result.json'))
        print(dict(CPU_seconds=result['CPU_seconds'],endpoints={a:v['counts'] for a,v in endpoints.items()},
            quartiles=docs['quartiles'],pairs={a:{k:v['both_correct'] for k,v in groups.items()} for a,groups in pairs.items()}))
    except BaseException as error:
        job.update(status='failed',error=repr(error));raise
    finally:atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
