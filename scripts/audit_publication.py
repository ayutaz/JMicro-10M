"""Offline publication triage; outputs counts/record IDs, never matched personal values."""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import unicodedata

PATTERNS = {
    'email': r'(?<![\w.+-])[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?![\w.-])',
    'jp_phone': r'(?<![A-Za-z0-9])0[1-9]\d{0,3}[- (]?\d{1,4}[- )]?\d{3,4}(?![A-Za-z0-9])',
    'international_phone': r'(?<!\w)\+81[- (]?(?:0[- ]?)?\d{1,4}[- )]?\d{1,4}[- ]?\d{3,4}(?!\d)',
    'postal_code': r'(?:〒\s*)?(?<!\d)\d{3}[- ]\d{4}(?!\d)',
    'street_address_candidate': r'(?:北海道|東京都|大阪府|京都府|[一-龥]{2,3}県)[^\n。!?]{0,45}(?:\d{1,4}丁目|\d{1,4}番地|\d{1,4}[-−ー]\d{1,4}(?:[-−ー]\d{1,4})?)',
    'name_disclosure_context': r'(?:本名|氏名|私の名前|名前は)[^\n。!?]{0,35}',
    'birthdate_context': r'(?:生年月日|誕生日)[^\n。!?]{0,35}(?:\d{4}年|\d{1,2}月\d{1,2}日)',
    'national_id_context': r'(?:マイナンバー|個人番号|旅券番号|パスポート番号|免許証番号)[^\n。!?]{0,35}\d{6,12}',
    'card_number_candidate': r'(?<![A-Za-z0-9])(?:\d[ -]?){12,18}\d(?![A-Za-z0-9])',
    'secret_token': r'(?:hf_[A-Za-z0-9]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[A-Z0-9]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)',
    'local_user_path': r'(?:/Users/[^/\s"\']+|/home/[^/\s"\']+|[A-Za-z]:\\Users\\[^\\\s"\']+)',
    'health_disclosure_context': r'(?:私は|自分は|私は今|自分が|私は昔)[^\n。!?]{0,40}(?:病気|通院|診断|障害|うつ|癌|がん|糖尿病|持病)',
    'residence_context': r'(?:住んで|住まい|在住|居住)[^\n。!?]{0,30}',
    'age_context': r'(?<!\d)\d{1,3}(?:歳|才)(?![一-龥])',
}
REGEX = {name: re.compile(pattern) for name, pattern in PATTERNS.items()}


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def luhn(value):
    digits = [int(x) for x in value if x.isdigit()]
    if not 13 <= len(digits) <= 19 or len(set(digits)) < 3:
        return False
    return sum((x * 2 - 9 if x * 2 > 9 else x * 2) if i % 2 == 1 else x
               for i, x in enumerate(reversed(digits))) % 10 == 0


def strings(value, field=''):
    if isinstance(value, str):
        if field.endswith('_json'):
            try:
                yield from strings(json.loads(value), field)
                return
            except (ValueError, TypeError):
                pass
        yield field, value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield from strings(item, f'{field}.{key}' if field else key)
    elif isinstance(value, list):
        for i, item in enumerate(value):
            yield from strings(item, f'{field}[{i}]')


def matches(text):
    text = unicodedata.normalize('NFKC', text)
    for name, regex in REGEX.items():
        values = [m.group() for m in regex.finditer(text)]
        if name == 'jp_phone':
            values = [x for x in values if len(re.sub(r'\D', '', x)) in (10, 11)]
        if name == 'card_number_candidate':
            values = [x for x in values if luhn(x)]
        if values:
            yield name, len(values)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bundle', type=Path, default=Path('artifacts/hub-publication'))
    parser.add_argument('--output', type=Path, default=Path('reports/local/publication_scan.json'))
    args = parser.parse_args()
    bundle = args.bundle
    file_reports, findings = {}, []
    for path in sorted(p for p in bundle.rglob('*') if p.is_file()):
        relative = path.relative_to(bundle).as_posix()
        count, occurrences, records, body_records = 0, Counter(), defaultdict(set), defaultdict(set)
        source_counts, status_counts = Counter(), Counter()
        if path.suffix == '.parquet':
            import pyarrow.parquet as pq
            rows = (row for batch in pq.ParquetFile(path).iter_batches(batch_size=256) for row in batch.to_pylist())
        elif path.suffix == '.jsonl':
            rows = (json.loads(line) for line in path.open(encoding='utf-8'))
        elif path.suffix == '.json':
            rows = [json.loads(path.read_text(encoding='utf-8'))]
        elif path.suffix == '.model':
            from sentencepiece import sentencepiece_model_pb2
            from google.protobuf.json_format import MessageToDict
            proto = sentencepiece_model_pb2.ModelProto()
            proto.ParseFromString(path.read_bytes())
            rows = [MessageToDict(proto, preserving_proto_field_name=True)]
        else:
            rows = [{'text': path.read_text(encoding='utf-8')}]
        for i, row in enumerate(rows):
            count += 1
            key = row.get('doc_id', f'row:{i}') if isinstance(row, dict) else f'row:{i}'
            if isinstance(row, dict):
                source_counts[row.get('source', row.get('bucket', 'metadata'))] += 1
                status_counts[row.get('status', 'not_applicable')] += 1
            for field, text in strings(row):
                for category, n in matches(text):
                    occurrences[category] += n
                    records[category].add(key)
                    if field == 'text' or field.startswith('messages_json['):
                        body_records[category].add(key)
                    findings.append({'file':relative,'record':key,'field':field,'category':category,'occurrences':n})
        file_reports[relative] = {'sha256':digest(path),'bytes':path.stat().st_size,'rows':count,
                                  'source_counts':dict(source_counts),'status_counts':dict(status_counts),
                                  'occurrences':dict(occurrences),'records_with_candidates':{k:len(v) for k,v in records.items()},
                                  'body_records_with_candidates':{k:len(v) for k,v in body_records.items()}}
    report = {'schema_version':1,'status':'needs_context_review','method':'NFKC inspection only; regex/contact/context triage; Luhn on card candidates',
              'limitations':['No exhaustive name recognition or reidentification analysis','Candidates are not confirmed private personal information',
                             'No personal values or text snippets in this report','No guarantee that zero detected candidates means privacy-safe'],
              'patterns':PATTERNS,'files':file_reports,'findings':findings}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'files':len(file_reports),'report':str(args.output),'summary':{k:v['records_with_candidates'] for k,v in file_reports.items() if v['occurrences']}},ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
