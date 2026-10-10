"""Assemble explicit manual judgments; identical control reuse is byte-checked."""
import argparse
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import read_json,write_json,sha256
from jmicro.chat_review import notes_template,content_review
from review_chat_first_sft import load_evaluation


def run(path):
    ev,items=load_evaluation(path/'result.json');scored={};files={};reuse=[]
    for file in sorted(path.glob('manual-*.json')):
        files[file.name]=sha256(file)
        for key,g,r,c,reason in read_json(file)['judgments']:
            assert key in items and key not in scored
            scored[key]=dict(key=key,grammar=g,relevance=r,context=c,rationale=reason)
    for key,item in items.items():
        if key in scored or item['condition']!='unsuppressed': continue
        source=key.replace('unsuppressed-','suppressed-');other=items[source]
        if source not in scored: continue
        # Never infer equal judgments just because a headline/output looks similar.
        if (other['messages']==item['messages'] and other['response']['generated_ids']==item['response']['generated_ids']
                and other['response']['raw_bytes_hex']==item['response']['raw_bytes_hex']):
            scored[key]=dict(scored[source],key=key)
            reuse.append(dict(key=key,source=source,identical_history_token_ids_and_raw_bytes=True))
    assert set(scored)==set(items), ('Unreviewed responses',sorted(set(items)-set(scored)))
    notes=notes_template(sha256(path/'result.json'),items)
    notes.update(reviewer=dict(kind='codex_nonblind',identity='Codex / 2026-10-10 Chat-first diagnostic',
        independent_human=False,blind=False),judgments=[scored[k] for k in items],pending_all_content_judgments=False,
        manual_judgment_sources=files,identical_control_judgment_reuse=reuse)
    content_review(ev,sha256(path/'result.json'),notes,items)
    target=path/'content_notes.json'
    if target.exists() and not read_json(target).get('pending_all_content_judgments',False):
        assert read_json(target)==notes,'Preserve completed original judgments'
    else: write_json(target,notes)
    print('Assembled all219 manual judgments; identical controls:',len(reuse))


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();p.add_argument('--directory',type=Path,required=True);run(p.parse_args().directory)
