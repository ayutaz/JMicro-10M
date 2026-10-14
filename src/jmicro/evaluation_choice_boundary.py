"""Pinned fixed Japanese diagnostic inputs, isolated from every TEST reader.

These are previously observed selection diagnostics, not newly unseen DEV or
sealed TEST. JBLiMP is a fixed public benchmark assigned a DEV role here.
"""
import hashlib
import json
from pathlib import Path
from jmicro.evaluation_boundary import reject_symlinks,require_digest

COUNTS={'semantics':192,'jblimp':331,'jcqa':1119}
WIDTHS={'semantics':2,'jblimp':2,'jcqa':5}
MANIFEST_NAME='japanese.dev.manifest.json'
FIELDS={'id','family','category','context','choices','label'}


def validate_rows(task,rows):
    if task not in COUNTS or len(rows)!=COUNTS[task]:raise ValueError('Exact fixed diagnostic count required')
    ids=set()
    for row in rows:
        if (set(row)!=FIELDS or any(not isinstance(row[k],str) for k in ('id','family','category','context'))
                or not row['id'] or row['id'] in ids or not row['family'] or not row['category']
                or not isinstance(row['choices'],list) or len(row['choices'])!=WIDTHS[task]
                or any(not isinstance(v,str) or not v for v in row['choices'])
                or type(row['label'])is not int or not 0<=row['label']<WIDTHS[task]):
            raise ValueError('Strict input-only diagnostic schema/IDs required')
        if any('\x00' in v or '\ufffd' in v for v in [row['context'],*row['choices']]):
            raise ValueError('Invalid diagnostic input Unicode')
        ids.add(row['id'])


def load_choices(manifest_path,pin,task):
    path=Path(manifest_path)
    if path.name!=MANIFEST_NAME or task not in COUNTS:raise ValueError('DEV-only diagnostic entry required')
    reject_symlinks(path);require_digest(pin)
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=pin:raise ValueError('Externally pinned diagnostic manifest differs')
    manifest=json.loads(raw)
    if (set(manifest)!={'kind','project_role','tasks','TEST_read_for_export'}
            or manifest['kind']!='isolated_previously_observed_Japanese_diagnostics_v1'
            or manifest['project_role']!='dev_fixed_diagnostics' or manifest['TEST_read_for_export']is not False
            or set(manifest['tasks'])!=set(COUNTS)):
        raise ValueError('Fixed diagnostic manifest schema differs')
    for name,entry in manifest['tasks'].items():
        if (set(entry)!={'file','count','sha256','source_sha256'} or entry['file']!=name+'.dev.jsonl'
                or entry['count']!=COUNTS[name]):raise ValueError('Diagnostic path/count contract differs')
        require_digest(entry['sha256']);require_digest(entry['source_sha256'])
    entry=manifest['tasks'][task];cases=path.parent/entry['file'];reject_symlinks(cases)
    raw_cases=cases.read_bytes()
    if hashlib.sha256(raw_cases).hexdigest()!=entry['sha256']:raise ValueError('Fixed diagnostic input hash differs')
    rows=[json.loads(line) for line in raw_cases.splitlines()]
    validate_rows(task,rows)
    return rows,dict(manifest_sha256=pin,cases_sha256=entry['sha256'],
        source_sha256=entry['source_sha256'],opened_paths=[str(path),str(cases)],
        role='previously_observed_fixed_diagnostics',TEST_opened=False)
