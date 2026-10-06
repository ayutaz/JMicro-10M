"""Version only budget accounting; reuse the immutable actual v1 CUDA gate."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise ValueError('Unexpected source anchor: '+old[:60])
    return text.replace(old,new,1)


def main():
    old=ROOT/'scripts/run_source_order_condition_comparison.py'
    text=old.read_text()
    text=replace_once(text,'import argparse','import run_source_order_condition_comparison as verified_probe\nimport source_order_budget_evidence as budget_evidence\nimport argparse')
    text=replace_once(text,"RUN=ROOT/'reports/phase6/source-order-condition-comparison-20261006'","RUN=ROOT/'reports/phase6/source-order-condition-comparison-v2-20261006'\nPROBE_RUN=verified_probe.RUN/'probe'")
    text=replace_once(text,"CONFIG=ROOT/'configs/phase6/source_order_condition_comparison.json'","CONFIG=ROOT/'configs/phase6/source_order_condition_comparison_v2.json'")
    text=text.replace('RUN/\'probe/result.json\'','PROBE_RUN/\'result.json\'')
    start=text.index('SOURCES=tuple('); end=text.index('reference,check_reference',start)
    text=text[:start]+"SOURCES=tuple(dict.fromkeys(('scripts/run_source_order_condition_comparison_v2.py','scripts/run_source_order_condition_comparison_v2.ps1',\n    'scripts/review_source_order_condition_comparison_v2.py','scripts/source_order_budget_evidence.py',\n    'tests/test_source_order_budget_v2.py',*verified_probe.SOURCES)))\n"+text[end:]
    start=text.index('def prepare_probe():');end=text.index('\ndef scope(',start)
    text=text[:start]+"def prepare_probe():\n    raise ValueError('v2 reuses the completed v1 CUDA probe; do not rerun verification weights')\n\n"+text[end:]
    text=replace_once(text,'    c=read_json(path);scope(c);old,base,parent,control,ev,positive,original=source_contract()',"    if path==PROBE_CONFIG:\n        return verified_probe.inspect(path)\n    c=read_json(path);scope(c);old,base,parent,control,ev,positive,original=source_contract()")
    start=text.index('def probe_evidence():');end=text.index('\ndef estimate_training(',start)
    text=text[:start]+"def probe_evidence():\n    verified_probe.inspect(PROBE_CONFIG)\n    return verified_probe.probe_evidence()\n\n"+text[end:]
    text=replace_once(text,'    return dict(steady_step_seconds=step,teachers_per_update=teachers,estimated_updates=updates,warmup_seconds=warm,save_seconds=save,estimated_training_seconds=total),total*1.3+300+50',"    evidence=budget_evidence.inspect(); reserve=evidence['nontraining_reserve_seconds']\n    return dict(steady_step_seconds=step,teachers_per_update=teachers,estimated_updates=updates,warmup_seconds=warm,save_seconds=save,estimated_training_seconds=total,\n        measured_nontraining_reserve_seconds=reserve,nontraining_evidence_sha256=sha256(budget_evidence.PATH)),(total+reserve)*1.3+50")
    text=replace_once(text,"    c,*_=inspect(PROBE_CONFIG);c=copy.deepcopy(c);r=probe_evidence();timing,estimate=estimate_training(r)","    c,*_=inspect(PROBE_CONFIG);c=copy.deepcopy(c);r=probe_evidence();timing,estimate=estimate_training(r)\n    c['source_sha256']={p:sha256(ROOT/p) for p in SOURCES}\n    c['references'].update(nontraining_timing=reference(budget_evidence.PATH),\n        previous_budget_rejection=reference(ROOT/'reports/phase6/source_order_budget_rejection_v1.json'))\n    c['probe_reuse_policy']='Actual v1 fullstate32 checks and32 timing steps; same immutable trainer, model, parent, data, source order, quotas, losses, LR, RNG and shape. v2 changes timing estimate only. All original verification GPU is charged; weights discarded.'")
    # Executable science path differs; the trainer/evaluation bodies stay byte-identical.
    text=text.replace('scripts/run_source_order_condition_comparison.ps1 -Mode','scripts/run_source_order_condition_comparison_v2.ps1 -Mode')
    text=replace_once(text,"    path=PROBE_CONFIG if probe else CONFIG;", "    if probe: raise ValueError('Reuse v1 actual probe; v2 science only')\n    path=PROBE_CONFIG if probe else CONFIG;")
    files={'scripts/run_source_order_condition_comparison_v2.py':text}
    ps=(ROOT/'scripts/run_source_order_condition_comparison.ps1').read_text()
    ps=ps.replace('source-order-condition-','source-order-condition-v2-').replace('run_source_order_condition_comparison.py','run_source_order_condition_comparison_v2.py')
    ps=ps.replace('source-order-condition-v2-comparison-20261006','source-order-condition-comparison-v2-20261006')
    ps=ps.replace("$ErrorActionPreference='Stop'","$ErrorActionPreference='Stop'\nif($Mode -eq 'Probe'){throw 'v2 reuses completed v1 verification; Train only.'}")
    files['scripts/run_source_order_condition_comparison_v2.ps1']=ps
    review=(ROOT/'scripts/review_source_order_condition_comparison.py').read_text().replace('import run_source_order_condition_comparison as study','import run_source_order_condition_comparison_v2 as study').replace('source_order_condition_comparison_review.json','source_order_condition_comparison_v2_review.json')
    files['scripts/review_source_order_condition_comparison_v2.py']=review
    post=(ROOT/'scripts/prepare_source_order_content_review.py').read_text().replace('import run_source_order_condition_comparison as study','import run_source_order_condition_comparison_v2 as study')
    files['scripts/prepare_source_order_content_review_v2.py']=post
    for relative,value in files.items():
        path=ROOT/relative
        if path.exists() and path.read_text()!=value:
            raise ValueError('Preserve existing versioned source')
        path.write_text(value,encoding='utf-8',newline='\n')
    print('Own v2 prepared; immutable v1 files unchanged; no GPU execution')


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
