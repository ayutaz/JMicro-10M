"""One frozen CPU replay of previously observed192 TRAIN windows for labels."""
import argparse
from collections import Counter
from datetime import datetime,timezone
import hashlib
import json
import os
from pathlib import Path
import statistics
import sys
import time
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'src'),str(ROOT/'scripts')]
import torch
from jmicro.document_progress import progress_targets
from jmicro.tokenizer import Tokenizer
from natural_context_contrast_corpus import OriginalTrainCorpusSampler


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(contract,pin):
    started = time.monotonic()
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or sha(contract) != pin:
        raise ValueError('Pinned CPU-only label feasibility contract required')
    c = json.loads(Path(contract).read_text())
    expected = dict(kind='document_progress_existing192_TRAIN_CPU_label_feasibility_v1',
        CPU_wall_ceiling_seconds=30,windows=192,batch=48,batches=4,seed=42,
        goals=dict(web=18750000,textbook=5000000,story=1250000),GPU_seconds=0,optimizer_updates=0)
    if any(type(c.get(k)) is not type(v) or c[k] != v for k,v in expected.items()):
        raise ValueError('Exact known192-window CPU scope required')
    output = ROOT/c['output']
    if output.exists() or not output.resolve().is_relative_to(ROOT/'reports/phase6'):
        raise ValueError('Fresh one-shot feasibility receipt required')
    for path,digest in c['sources'].items():
        if sha(ROOT/path) != digest:
            raise ValueError('Prepared label source differs: '+path)
    for key in ('proposal','accepted_config','old192_metadata','CPU_tests'):
        if sha(ROOT/c[key]['path']) != c[key]['sha256']:
            raise ValueError('Pinned metadata differs: '+key)
    suites = list(ET.parse(ROOT/c['CPU_tests']['path']).getroot().iter('testsuite'))
    if (sum(int(s.attrib.get('tests',0)) for s in suites) != 23
            or any(int(s.attrib.get(k,0)) for s in suites for k in ('failures','errors','skipped'))):
        raise ValueError('All23 label/head mathematical CPU checks required')
    accepted = json.loads((ROOT/c['accepted_config']['path']).read_text())
    previous = json.loads((ROOT/c['old192_metadata']['path']).read_text())
    if previous['TRAIN_windows'] != 192 or len(previous['row_metadata']) != 192:
        raise ValueError('Exactly previously observed192 original windows required')
    source = accepted['source_binding']
    pool = Path(source['pool'])
    ready = pool/('.compact-index-'+source['manifest_sha256'][:16])/'ready.json'
    codec_path = ROOT/accepted['tokenizer']
    allowed = {str(p.resolve()) for p in (pool/'manifest.json',ready,pool/'train.index.jsonl',pool/'train.bin',codec_path)}
    sensitive = (Path('/home/aihub_ubuntu/jmicro-data'),ROOT/'eval',ROOT/'artifacts',ROOT/'reports')
    reads = []
    def audit(event,args):
        if event != 'open' or not isinstance(args[0],(str,bytes)):
            return
        path = Path(os.fsdecode(args[0])).resolve()
        if any(path.is_relative_to(p) for p in sensitive):
            writing = any(flag in (args[1] or '') for flag in 'wax+')
            if path == output.resolve() and writing:
                return
            if str(path) not in allowed or writing:
                raise ValueError('Forbidden corpus/model/DEV/TEST open: '+str(path))
            reads.append(str(path))
    sys.addaudithook(audit)
    if sha(codec_path) != accepted['tokenizer_sha256']:
        raise ValueError('Original frozen Tokenizer differs')
    codec = Tokenizer(codec_path)
    sampler = OriginalTrainCorpusSampler(source['pool'],source['manifest_sha256'],codec,c['goals'],seed=42)
    if sampler.binding != source:
        raise ValueError('Accepted source identity differs; no rescan fallback')
    rows = []
    try:
        for _ in range(4):
            if time.monotonic()-started > 30:
                raise TimeoutError('Fixed30 CPU seconds exceeded')
            rows.extend(sampler.take(48))
    finally:
        sampler.handle.close()
    current = [dict(source=r['source'],original_teachers=r['original_body_tokens']+1,
        selected_gold=r['teacher_tokens'],original_body_sha256=r['full_original_body_sha256']) for r in rows]
    if current != previous['row_metadata']:
        raise ValueError('Known192 metadata differs; no changed draw or reselection')
    labels = progress_targets(rows)
    observations,values = [],[]
    totals = Counter()
    for row,label in zip(rows,labels,strict=True):
        selected = [v for t,v in zip(row['target_ids'],label,strict=True) if t != -100]
        zeros = sum(v == 0 for v in selected)
        if (zeros != row['original_EOS_targets'] or any(not 0 <= v <= 1 for v in selected)
                or any((t == -100) != (v == -1.) for t,v in zip(row['target_ids'],label,strict=True))):
            raise ValueError('Selected main/ignored/realEOS scalar labels differ')
        values.extend(selected)
        totals[row['source']] += len(selected)
        observations.append(dict(**current[len(observations)],input_start=row['input_start'],
            target_first=row['target_first'],target_end=row['target_end'],
            progress_labels=len(selected),real_EOS_zero_labels=zeros,
            minimum_progress=min(selected),maximum_progress=max(selected)))
    elapsed = time.monotonic()-started
    if (len(rows) != 192 or len(values) != previous['selected_gold_positions']
            or not statistics.pvariance(values) > 0 or elapsed > 30 or torch.cuda.is_initialized()):
        raise ValueError('Exact known labels/nonconstant target/CPU-only scope required')
    result = dict(status='known192_TRAIN_progress_label_feasibility_complete',
        observed_at=datetime.now(timezone.utc).isoformat(),contract_sha256=sha(contract),sources=c['sources'],
        existing192_metadata=c['old192_metadata'],original_source_binding=source,new_pilot_goals=c['goals'],
        known_source_body_length_selected_count_metadata_exact=True,windows=192,selected_main_gold=len(values),
        additional_scalar_progress_labels=len(values),per_source_labels=dict(totals),
        real_EOS_zero_labels=sum(r['real_EOS_zero_labels'] for r in observations),
        minimum_progress=min(values),maximum_progress=max(values),mean_progress=statistics.fmean(values),
        progress_variance=statistics.pvariance(values),row_metadata=observations,
        Python_guarded_read_paths=sorted(set(reads)),CPU_wall_seconds=elapsed,CPU_wall_ceiling_seconds=30,
        new_GPU_seconds=0,optimizer_updates=0,new_scientific_teachers=0,new_data_prepared=False,
        model_or_weights_opened=False,DEV_opened=False,TEST_opened=False,science_contract_frozen=False,
        Base_qualified=False,Base_adopted=False,full_four_item_goal_complete=False,
        limitations=['A replay of known192 selection material, not an independent corpus audit or quality proof.',
            'Old metadata lacks raw IDs, so no byte-for-byte old-input equality is claimed beyond stored source/body/length/count fields.',
            'Python open guard is not an OS sandbox and does not cover native SentencePiece reads.',
            'A nonconstant label signal is not evidence that the model can learn it or that it improves Japanese generation.'])
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','windows','selected_main_gold','real_EOS_zero_labels','progress_variance','CPU_wall_seconds')}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract',type=Path,required=True)
    parser.add_argument('--contract-sha256',required=True)
    args = parser.parse_args()
    run(args.contract,args.contract_sha256)
