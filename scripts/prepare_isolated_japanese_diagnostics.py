"""One export of input-only fields from stored DEV-only diagnostic results.

No mixed source/TEST/model/weights/corpus scan. Dataset payload remains WSL;
only hashes/provenance and this implementation are appropriate for Git.
"""
import hashlib
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from jmicro.evaluation_choice_boundary import COUNTS,MANIFEST_NAME,validate_rows,load_choices

SOURCES={
    'semantics':'6eb3bfa99bcb5e244cffe741e649c8fae811ab8129294b5e1e0e97adefa0ed15',
    'jblimp':'5c9710313516216466f99166c5988a2e422806bd1245c5586b391b310f5d487c',
    'jcqa':'5dc8cffefa08af297ed367bedee9899bd354740d0c2298c5e257a90fbfc69f1f'}
SOURCE=ROOT/'reports/phase6/base-parallel-residual-comparison-20261007/evaluation/sequential/evaluation'
DEST=Path('/home/aihub_ubuntu/jmicro-data/evaluation-isolated-japanese-v1')
RECEIPT=ROOT/'reports/phase6/fim-feasibility-20261015/Japanese_diagnostic_export.json'


def main():
    if DEST.exists() or RECEIPT.exists():raise ValueError('Preserve one-shot fixed diagnostic export')
    projected={};sources={}
    for task,pin in SOURCES.items():
        path=SOURCE/(task+'.json');raw=path.read_bytes()
        if hashlib.sha256(raw).hexdigest()!=pin:raise ValueError('Pinned stored diagnostic differs: '+task)
        saved=json.loads(raw)
        if saved['complete']is not True or len(saved['rows'])!=COUNTS[task]:raise ValueError('Complete fixed diagnostics required')
        if task=='semantics' and any(row['split']!='dev' for row in saved['rows']):
            raise ValueError('Stored semantic diagnostic must contain DEV only')
        rows=[dict(id=r['id'],family=r.get('family',r['id']),category=r['category'],context=r['context'],
                   choices=r['choices'],label=r['label']) for r in saved['rows']]
        validate_rows(task,rows);projected[task]=rows;sources[task]=str(path)
    DEST.mkdir(parents=True)
    manifest=dict(kind='isolated_previously_observed_Japanese_diagnostics_v1',
        project_role='dev_fixed_diagnostics',tasks={},TEST_read_for_export=False)
    for task,rows in projected.items():
        raw=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows).encode()
        name=task+'.dev.jsonl';(DEST/name).write_bytes(raw)
        manifest['tasks'][task]=dict(file=name,count=len(rows),sha256=hashlib.sha256(raw).hexdigest(),source_sha256=SOURCES[task])
    path=DEST/MANIFEST_NAME;path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    pin=hashlib.sha256(path.read_bytes()).hexdigest();audited={}
    for task in COUNTS:
        loaded,provenance=load_choices(path,pin,task)
        if loaded!=projected[task]:raise ValueError('Original input projection changed')
        audited[task]=provenance
    receipt=dict(status='fixed_diagnostic_inputs_exported_and_pinned_no_TEST_source_read',
        manifest_path=str(path),manifest_sha256=pin,tasks=manifest['tasks'],source_paths=sources,
        projections='id/family/category/context/choices/original_gold_label_only; no model scores/predictions/answers generated',
        source_roles=dict(semantics='previously observed project DEV192',jblimp='previously observed public fixed benchmark331',
                          jcqa='previously observed official DEV1119'),
        audited_reads=audited,dataset_payload_exported_to_Git=False,new_scientific_teacher_positions=0,
        new_GPU_seconds=0,new_model_quality_evaluations=0,new_TEST_prepared=False,Base_adopted=False)
    RECEIPT.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(status=receipt['status'],manifest_sha256=pin,counts=COUNTS)))


if __name__=='__main__':main()
