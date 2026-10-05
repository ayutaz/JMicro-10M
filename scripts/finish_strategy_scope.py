"""Portable raw evidence and actual completion for authorized roadmap1-3."""
import gzip
import hashlib
import json
from pathlib import Path
import sys
import urllib.request
import xml.etree.ElementTree as ET
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from phase6_performance import alive,identity
from run_strategy_extension import RUN,BASE,CONFIG,load_config


def finish():
    c=load_config();review=read_json(RUN/'review.json');base_review=read_json(BASE/'review.json')
    assert review['status']==base_review['status']=='verified_learning_and_content_evidence'
    assert not any(g['adopted'] for g in review['gates'].values()),'Review adoption separately before completing'
    diagnostic=ROOT/'reports/phase6/generation-transfer-20261006'
    jobs=[read_json(p) for p in (diagnostic/'job.json',BASE/'job.json',BASE/'baselines-job.json',RUN/'job.json')]
    assert all(j['status']=='complete' and not alive(j) for j in jobs)
    assert jobs[0]['scientific_teacher_tokens']==0 and jobs[0]['gpu_elapsed_seconds']<=600
    assert len(read_json(diagnostic/'review.json')['reviews'])==128
    data=Path('/home/aihub_ubuntu/jmicro-data/phase6/curriculum-strategy-20261005-v3')
    ready=read_json(data/'ready.json');content=read_json(BASE/'content-review.json')
    assert ready['splits']['train']['tokens']>=10000000 and content['documents']==64 and content['weak_documents']<=10
    tests={}
    for name in ('generation_transfer_tests.xml','curriculum_strategy_tests.xml','curriculum_strategy_bootstrap_tests.xml','strategy_extension_tests.xml'):
        path=ROOT/'reports/phase6'/name
        if not path.exists():continue
        suites=list(ET.parse(path).getroot().iter('testsuite'))
        assert all(int(s.attrib.get(k,0))==0 for s in suites for k in ('failures','errors','skipped'))
        tests[name]=dict(tests=sum(int(s.attrib.get('tests',0)) for s in suites),sha256=sha256(path))
    assert 'curriculum_strategy_tests.xml' in tests and 'strategy_extension_tests.xml' in tests
    ui=read_json(ROOT/'reports/local/webui/server.json');assert alive(ui)
    actual=identity(ui['pid'])
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=5) as response:model=json.load(response)
    assert model['checkpoint_sha256']=='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
    assert model['training_tokens']==10000007168 and not model['busy']
    sources={}
    runs=[diagnostic,BASE,RUN,ROOT/'reports/phase6/curriculum-strategy-20261005',ROOT/'reports/phase6/curriculum-strategy-20261005-v2']
    for run in runs:
        for path in sorted(run.rglob('*')):
            if path.is_file() and path.suffix in ('.json','.jsonl','.xml','.py','.ps1','.log'):
                text=path.read_text(encoding='utf-8');sources[str(path.relative_to(ROOT))]=dict(sha256=sha256(path),text=text)
    for path in (ROOT/'reports/phase6').iterdir():
        if path.is_file() and path.suffix in ('.json','.xml') and path.name.startswith(('generation_transfer_','curriculum_strategy_','strategy_extension_','strategy_architecture_')):
            sources[str(path.relative_to(ROOT))]=dict(sha256=sha256(path),text=path.read_text(encoding='utf-8'))
    for path in (data/'ready.json',data/'sample64.json',CONFIG,ROOT/'configs/phase6/curriculum_strategy.json',ROOT/'configs/phase6/generation_transfer.json'):
        if path.exists():sources[str(path)]=dict(sha256=sha256(path),text=path.read_text(encoding='utf-8'))
    bundle=ROOT/'reports/phase6/strategy_scope_evidence.json.gz'
    with gzip.open(bundle,'wt',encoding='utf-8',compresslevel=6) as stream:
        json.dump(dict(scope='Roadmap1-3 raw diagnostics, failed preparation, scientific metrics, reviews and frozen source; checkpoints/shards retained in WSL',members=sources),stream,ensure_ascii=False)
    base=read_json(BASE/'compare-result.json');result=read_json(RUN/'compare-result.json')
    report=dict(status='complete_requested_roadmap1_to3_quality_unmet',completed_at=now(),
        stage1=dict(job=jobs[0],review_sha256=sha256(diagnostic/'review.json'),scientific_teacher_tokens=0),
        stage2=dict(train_prepared_tokens=ready['splits']['train']['tokens'],dev_prepared_tokens=ready['splits']['dev']['tokens'],weak64=content['weak_documents'],ready_sha256=sha256(data/'ready.json')),
        stage3=dict(teacher_tokens_per_strategy=300000000,scientific_teacher_tokens=600000000,
            valid_input_tokens=sum(d['additional_input_tokens'] for r in (base,result) for d in r['checkpoints'].values()),
            physical_tokens=sum(d['physical_input_tokens'] for r in (base,result) for d in r['checkpoints'].values()),
            verification_teacher_tokens=base['verification_teacher_tokens']+result['verification_teacher_tokens'],
            CUDA_resume_optimizer_updates=32,gpu_seconds=review['stage3_total_GPU_seconds'],
            original100M_review_sha256=sha256(BASE/'review.json'),extension_review_sha256=sha256(RUN/'review.json'),
            all_individual_generation_reviews=320,independent_human_blind=False),
        jobs_terminal_absent=True,UI=dict(actual=actual,model=model),tests=tests,
        archive=dict(path=str(bundle.relative_to(ROOT)),sha256=sha256(bundle),members=len(sources),bytes=bundle.stat().st_size),
        decision='Both300M candidates rejected under unchanged gates; original10B UI retained; architecture experiment remains a proposal',
        old_numerical_failures72_preserved=True,stage4_started=False,Chat_started=False,protected_test_used=False,pushed=False,
        next='Stop after results/local commit. Next proposed research is realistic material/source revision with matched budget and learning-curve design; no automatic large scaling.')
    write_json(RUN/'completion.json',report);write_json(ROOT/'reports/phase6/strategy_scope_completion.json',report)
    print(json.dumps(report,ensure_ascii=False),flush=True)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);finish()
