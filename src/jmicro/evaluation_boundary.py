"""Pinned DEV-only artifacts. There is deliberately no TEST-reader fallback.

The manifest contains provenance and hashes, never evaluation answers. Consumers
must pin its hash in their execution contract before loading cases.
"""
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re

MANIFEST_NAME = 'base.dev.manifest.json'
CASES_NAME = 'base.dev.jsonl'
KIND = 'isolated_base_dev_suite_v1'
FIELDS = {'kind','version','split','cases_file','cases_sha256','case_count',
    'case_identity_sha256','source_generation_sha256','source_legacy_suite_sha256',
    'TEST_read_for_export'}
CASE_FIELDS = {'id','category','prefix','split'}


def digest(raw): return hashlib.sha256(raw).hexdigest()


def identity_digest(cases):
    return digest(json.dumps(cases,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())


def require_digest(value):
    if not isinstance(value,str) or re.fullmatch(r'[0-9a-f]{64}',value) is None:
        raise ValueError('An externally pinned lowercase SHA256 is required')


def reject_symlinks(path):
    p=Path(path).absolute()
    while True:
        if p.is_symlink(): raise ValueError('Evaluation artifact paths must not contain symlinks')
        if p==p.parent: break
        p=p.parent


def validate_cases(cases):
    if not isinstance(cases,list) or len(cases)!=80:
        raise ValueError('The complete fixed80 DEV cases are required')
    ids=set()
    for case in cases:
        if not isinstance(case,dict) or set(case)!=CASE_FIELDS or case['split']!='dev':
            raise ValueError('DEV-only input cases, without generated answers, required')
        if (not isinstance(case['id'],str) or not re.fullmatch(r'base-\d{3}',case['id'])
                or case['id'] in ids or not isinstance(case['category'],str) or not case['category']
                or not isinstance(case['prefix'],str) or not case['prefix'].strip()
                or '\x00' in case['prefix'] or '\ufffd' in case['prefix']):
            raise ValueError('Unique fixed identifiers and nonempty valid DEV prefixes required')
        ids.add(case['id'])


@dataclass(frozen=True)
class DevSuite:
    cases: tuple
    manifest_sha256: str
    cases_sha256: str
    source_legacy_suite_sha256: str
    opened_paths: tuple


def load_dev_suite(manifest_path, expected_manifest_sha256):
    """Open exactly the pinned DEV manifest and its fixed DEV sibling file."""
    require_digest(expected_manifest_sha256)
    path=Path(manifest_path)
    if path.name!=MANIFEST_NAME:
        raise ValueError('Mixed suites and TEST manifests are not DEV entry points')
    reject_symlinks(path)
    raw=path.read_bytes()
    if digest(raw)!=expected_manifest_sha256:
        raise ValueError('DEV manifest differs from the frozen execution contract')
    manifest=json.loads(raw)
    if (not isinstance(manifest,dict) or set(manifest)!=FIELDS or manifest['kind']!=KIND
            or type(manifest['version']) is not int or manifest['version']!=1
            or manifest['split']!='dev' or manifest['cases_file']!=CASES_NAME
            or type(manifest['case_count']) is not int or manifest['case_count']!=80
            or manifest['TEST_read_for_export'] is not False):
        raise ValueError('Pinned DEV-only manifest schema required')
    for key in ('cases_sha256','case_identity_sha256','source_generation_sha256','source_legacy_suite_sha256'):
        require_digest(manifest[key])
    cases_path=path.parent/CASES_NAME
    reject_symlinks(cases_path)
    payload=cases_path.read_bytes()
    if digest(payload)!=manifest['cases_sha256']:
        raise ValueError('DEV case bytes differ; refuse parsing altered contents')
    cases=[json.loads(line) for line in payload.decode('utf-8').splitlines()]
    validate_cases(cases)
    if identity_digest(cases)!=manifest['case_identity_sha256']:
        raise ValueError('Fixed DEV identities/order/prefixes differ')
    return DevSuite(tuple(cases),expected_manifest_sha256,manifest['cases_sha256'],
        manifest['source_legacy_suite_sha256'],(str(path),str(cases_path)))


def validate_dev_outputs(outputs,suite):
    """Content reviewers use the same isolated cases, not the mixed legacy file."""
    if not isinstance(suite,DevSuite) or len(outputs)!=80:
        raise ValueError('Complete bound DEV output set required')
    expected={c['id']:c for c in suite.cases}
    ids=[r['id'] for r in outputs]
    if len(set(ids))!=80 or set(ids)!=set(expected):
        raise ValueError('DEV output identifiers differ')
    for row in outputs:
        case=expected[row['id']]
        if row['split']!='dev' or row['prefix']!=case['prefix'] or row['category']!=case['category']:
            raise ValueError('Actual DEV output/prefix/category/split binding differs')
    return True
