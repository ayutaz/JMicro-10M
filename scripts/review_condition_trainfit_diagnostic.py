"""Review complete original-target fitting evidence; never adopt a failed Base."""
import json
import math
from pathlib import Path
import sys
import tarfile

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import alive
import run_condition_trainfit_diagnostic as study


def main():
    c, view=study.inspect(); job=read_json(study.RUN/'job.json'); result=read_json(study.RUN/'result.json')
    if (job['status']!='complete' or alive(job) or result['config_sha256']!=sha256(study.CONFIG)
            or not 0<=result['GPU_seconds']<=job['GPU_elapsed_seconds']<=60
            or result['evaluated_documents']!=1536 or result['optimizer_updates']!=0
            or result['scientific_teacher_tokens']!=0 or result['protected_test_used']):
        raise ValueError('Actual complete bounded read-only diagnostic required')
    rows=[]
    for arm, ref in c['checkpoints'].items():
        if not all(result['checks'][arm][k] for k in ('weights_unchanged','RNG_restored','no_gradients','eval_mode')):
            raise ValueError('Read-only CUDA checks failed')
        for start in range(0,512,32):
            raw=read_json(study.RUN/'outputs'/arm/f'{start:04d}.json')
            cases=study.documents(view,start,start+32)
            if (raw['config_sha256']!=sha256(study.CONFIG) or raw['checkpoint_sha256']!=ref['sha256']
                    or len(raw['rows'])!=len(cases)):
                raise ValueError('Actual batch/checkpoint binding differs')
            for row,case in zip(raw['rows'],cases,strict=True):
                if (row['index']!=case['index'] or row['id']!=case['id']
                        or row['target_sha256']!=case['target_sha256'] or row['target_ids']!=case['ids'][1:]
                        or row['focus']!=case['focus'] or len(row['target_nll'])!=len(row['target_ids'])
                        or any(not math.isfinite(x) or x<0 for x in row['target_nll'])):
                    raise ValueError('Raw original IDs/masks/finite losses differ')
                for group in study.GROUPS:
                    selected=[nll for label,focus,nll in zip(row['target_ids'],row['focus'],row['target_nll'],strict=True)
                        if (focus if group=='focus_body' else label>=8 and not focus if group=='other_body' else label==3)]
                    kept=row['groups'][group]
                    if (kept['tokens']!=len(selected)
                            or not math.isclose(kept['nll_sum'],sum(selected),rel_tol=1e-10,abs_tol=1e-10)
                            or (not selected and kept['mean_nll'] is not None)
                            or selected and not math.isclose(kept['mean_nll'],sum(selected)/len(selected),rel_tol=1e-10,abs_tol=1e-10)):
                        raise ValueError('Saved group does not sum actual original losses')
                rows.append(dict(checkpoint=arm,**row))
    if study.summarize(rows,c)!=result['summary']: raise ValueError('Raw all512 summary differs')
    quality=read_json(study.STUDY/'review.json'); comparison=read_json(study.STUDY/'compare-result.json')
    counts={arm:comparison['checkpoints'][arm]['source_teachers']['conditional_textbook'] for arm in study.ARMS[1:]}
    report=dict(status='actual512_by3_trainfit_diagnostic_review_complete',created_at=now(),
        config_sha256=sha256(study.CONFIG),result_sha256=sha256(study.RUN/'result.json'),
        study_review_sha256=sha256(study.STUDY/'review.json'),summary=result['summary'],checks=result['checks'],
        actual_GPU_seconds=result['GPU_seconds'],GPU_occupation_seconds=job['GPU_elapsed_seconds'],
        target_documents=512,measured_checkpoint_documents=1536,optimizer_updates=0,
        scientific_teacher_tokens=0,new_original_tokens=0,protected_test_used=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,requested_five_steps_complete=False,
        actual_conditional_teacher_tokens=counts,conditional_teacher_exposures={arm:n/view.manifest['full_CE_targets'] for arm,n in counts.items()},
        heldout_content={arm:{k:quality['summaries'][arm][k] for k in ('coherent','appropriate','grammar2','rates')} for arm in study.ARMS[1:]},
        interpretation='Original positive targets fit substantially better after weight4 than ordinary CE on every504 focus-enabled document, while fixed-dev generation coherence drops15->9. This supports fitting without demonstrated transfer on these data/one seed. It does not prove the sole cause, capacity limit, independent generalization or incompatible counterfactual labels.',
        next_action='Keep weight1 and exact25M conditional/source quotas; prepare nested512->2048 original-source variety with unchanged V3 selector, fixed64 new-content gate, then measured matched comparison vs existing512 control. No automatic weight sweep/long extension/Chat.')
    atomic_json(study.RUN/'review.json',report)
    atomic_json(ROOT/'reports/phase6/condition_trainfit_diagnostic_review.json',report)
    archive=ROOT/'reports/phase6/condition-trainfit-diagnostic-20261006_evidence.tar.gz'
    if archive.exists(): raise ValueError('Evidence archive immutable; inspect existing instead')
    paths={p for p in study.RUN.rglob('*') if p.is_file() and p.suffix in ('.json','.py','.ps1','.lock')}
    paths.update((study.CONFIG,study.PROPOSAL,Path(__file__),ROOT/'reports/phase6/condition_trainfit_diagnostic_tests.xml'))
    entries=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha256(p),bytes=p.stat().st_size) for p in sorted(paths)]
    temporary=archive.with_suffix('.tmp')
    with tarfile.open(temporary,'w:gz',compresslevel=1) as stream:
        for path in sorted(paths): stream.add(path,arcname=path.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(archive)
    atomic_json(ROOT/'reports/phase6/condition_trainfit_diagnostic_evidence_manifest.json',dict(entries=entries,
        text_files=len(entries),uncompressed_bytes=sum(r['bytes'] for r in entries),
        archive=dict(path=str(archive),sha256=sha256(archive),bytes=archive.stat().st_size),checkpoint_tensors_included=False))
    print(json.dumps(dict(status=report['status'],summary=result['summary'],GPU_seconds=result['GPU_seconds'])),flush=True)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
