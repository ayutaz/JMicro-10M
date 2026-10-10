"""Review diagnostic Base/SFT raw outputs without pretending Base adoption."""
import argparse
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT, read_json, sha256, write_json, now
from jmicro.chat_review import review_items, notes_template, content_review
from evaluate_chat_sft import load_dev
from chat_first_contract import resolve_diagnostic
from phase6_performance import alive


def load_evaluation(path):
    path=path.resolve()
    assert path.is_relative_to(ROOT/'reports/phase7') and path.name == 'result.json'
    ev=read_json(path);binding=ev['binding'];job=read_json(path.parent/'job.json')
    assert job['status']=='complete' and not alive(job) and job['binding']==binding
    assert 0 < job['GPU_elapsed_seconds'] <= binding['GPU_budget_seconds']
    parent=read_json(Path(job['parent_job']))
    assert parent['status']=='complete' and not alive(parent) and parent['binding']==job['parent_binding']
    assert all(parent[k]==job[k] for k in ('pid','boot_id','start_ticks'))
    for p,digest in binding['source_sha256'].items(): assert sha256(path.parent/'source'/p)==digest
    provenance=binding['diagnostic_provenance'];ref=provenance['config']
    assert sha256(Path(ref['path']))==ref['sha256']
    state,tok,current=resolve_diagnostic(Path(ref['path']),binding['stage'])
    assert current==provenance and current['checkpoint']['sha256']==binding['checkpoint_sha256']
    assert binding['implementation']==state['implementation_sha256']
    assert binding['tokenizer_sha256']==sha256(tok.path) and binding['suite_sha256']==sha256(ROOT/'eval/chat.jsonl')
    cases,_=load_dev(tok,binding['model_context'])
    return ev,review_items(ev,cases,tok,binding['model_context'])


def run(args):
    ev,items=load_evaluation(args.evaluation);digest=sha256(args.evaluation)
    if args.template:
        if args.template.exists(): raise FileExistsError('Preserve judgments')
        write_json(args.template,notes_template(digest,items))
        write_json(args.template.with_name(args.template.stem+'-items.json'),dict(evaluation_sha256=digest,items=list(items.values())))
        print('Prepared all219 actual-history responses, unscored');return
    report=content_review(ev,digest,read_json(args.notes),items)
    report.update(annotations_sha256=sha256(args.notes),checkpoint_sha256=ev['binding']['checkpoint_sha256'],
        evaluation_binding=ev['binding'],reviewed_at=now(),Base_adopted=False,purpose='chat_first_diagnostic')
    output=args.evaluation.parent/'content_review.json'
    if output.exists(): assert read_json(output)['annotations_sha256']==report['annotations_sha256']
    write_json(output,report)
    print('All219 content judgments verified; DEV screen:',report['dev_screen_passed'])


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    parser=argparse.ArgumentParser();parser.add_argument('--evaluation',type=Path,required=True)
    mode=parser.add_mutually_exclusive_group(required=True);mode.add_argument('--template',type=Path);mode.add_argument('--notes',type=Path)
    run(parser.parse_args())
