"""Common-byte, model-specific codec and paired-family likelihood diagnostics."""
from collections import defaultdict
import hashlib
import json
import math

import torch
from torch.nn import functional as F
from jmicro.japanese_evaluation import encode_request, tied_prediction, clustered_ci


class HFCodec:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def encode(self, text):
        return self.tokenizer.encode(text, add_special_tokens=False)

    def decode_bytes(self, ids):
        return self.tokenizer.decode(ids, skip_special_tokens=False,
            clean_up_tokenization_spaces=False).encode('utf-8')


def hf_request(tokenizer, bos, context, choice, maximum=1024):
    row = encode_request(HFCodec(tokenizer), context, choice, maximum)
    # encode_request verifies the joint text boundary/bytes; replace only native BOS.
    row['ids'][0] = bos
    return row


def dev_cases(path):
    rows = []
    selected_bytes = []
    opaque_records = 0
    with path.open('rb') as stream:
        for raw in stream:
            if not raw.strip():
                continue
            # Reserved test records remain opaque: never JSON-decode their contents.
            if b', "split": "dev",' not in raw:
                opaque_records += 1
                continue
            row = json.loads(raw)
            if row['split'] != 'dev':
                raise ValueError('Dev-only metadata selection differs')
            rows.append(row)
            selected_bytes.append(raw)
    if len(rows) != 192:
        raise ValueError('All192 fixed dev cases required')
    families = defaultdict(list)
    for row in rows:
        families[row['family']].append(row)
    if len(families) != 96 or len({r['id'] for r in rows}) != 192:
        raise ValueError('192 unique IDs in96 paired families required')
    for cases in families.values():
        if (len(cases) != 2 or {r['label'] for r in cases} != {0, 1}
                or cases[0]['choices'] != cases[1]['choices']
                or cases[0]['context'] == cases[1]['context']):
            raise ValueError('Keep opposite labels/identical choices/different contexts in each family')
    return rows, dict(dev_bytes_sha256=hashlib.sha256(b''.join(selected_bytes)).hexdigest(),
        dev_cases=192, families=96, other_records_opaque=opaque_records,
        other_records_JSON_decoded=False)


@torch.inference_mode()
def hf_scores(model, encoded, device='cuda'):
    width = max(len(r['ids'])-1 for r in encoded)
    inputs = torch.zeros((len(encoded), width), dtype=torch.long, device=device)
    labels = torch.zeros_like(inputs)
    mask = torch.zeros_like(inputs, dtype=torch.bool)
    targets = torch.zeros_like(mask)
    for index, row in enumerate(encoded):
        count = len(row['ids'])-1
        inputs[index, :count] = torch.tensor(row['ids'][:-1], device=device)
        labels[index, :count] = torch.tensor(row['ids'][1:], device=device)
        mask[index, :count] = True
        targets[index, row['context_tokens']-1:count] = True
    logits = model(input_ids=inputs, attention_mask=mask, use_cache=False).logits
    # Only continuation positions are cast to FP32; padded/context losses never enter scores.
    selected = logits[targets].float()
    nll = F.cross_entropy(selected, labels[targets], reduction='none').double().cpu().tolist()
    greedy = selected.argmax(-1).eq(labels[targets]).cpu().tolist()
    output = []
    offset = 0
    for row in encoded:
        count = len(row['target_ids'])
        losses = nll[offset:offset+count]
        if len(losses) != count or not all(math.isfinite(v) for v in losses):
            raise ValueError('Finite complete continuation scores required')
        output.append(dict(log_likelihood=-sum(losses), token_nll=losses,
            target_tokens=count, target_ids=row['target_ids'], target_bytes=row['target_bytes'],
            is_greedy=all(greedy[offset:offset+count])))
        offset += count
    if offset != len(nll):
        raise ValueError('Continuation token accounting mismatch')
    return output


def case_scores(case, scores):
    if len(scores) != 2:
        raise ValueError('Two unchanged candidates per case required')
    primary = tied_prediction([s['log_likelihood'] for s in scores], case['label'])
    secondary = tied_prediction([s['log_likelihood']/s['target_tokens'] for s in scores], case['label'])
    byte_secondary = tied_prediction([s['log_likelihood']/s['target_bytes'] for s in scores], case['label'])
    return dict(**case, case_sha256=hashlib.sha256(json.dumps(case, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
        scores=scores, **primary, per_token_prediction=secondary, per_byte_prediction=byte_secondary)


def summary(rows):
    families = defaultdict(list)
    categories = defaultdict(list)
    for row in rows:
        families[row['family']].append(row)
        categories[row['category']].append(row)
    both = [dict(id=f, family=f, credit=float(all(r['credit'] == 1 for r in cases)))
        for f, cases in families.items()]
    return dict(cases=len(rows), accuracy=clustered_ci(rows), both_contexts_hard_correct=clustered_ci(both),
        ties=sum(r['ties'] > 1 for r in rows), categories={k:clustered_ci(v) for k,v in categories.items()},
        total_choice_tokens=sum(s['target_tokens'] for r in rows for s in r['scores']),
        total_common_choice_bytes=sum(s['target_bytes'] for r in rows for s in r['scores']),
        chance_case=.5, independent_random_both_chance=.25,
        static_candidate_preference_case_accuracy=.5, static_candidate_preference_both_correct=0)


def compare(teacher, student):
    if [r['case_sha256'] for r in teacher] != [r['case_sha256'] for r in student]:
        raise ValueError('Match every identical raw case, choice and label')
    difference = []
    discordant = []
    for t, s in zip(teacher, student, strict=True):
        if [v['target_bytes'] for v in t['scores']] != [v['target_bytes'] for v in s['scores']]:
            raise ValueError('Common continuation UTF8 bytes differ')
        difference.append(dict(id=t['id'], family=t['family'], credit=t['credit']-s['credit']))
        if t['prediction'] != s['prediction'] or t['credit'] != s['credit']:
            discordant.append(dict(id=t['id'], family=t['family'], category=t['category'], label=t['label'],
                context=t['context'], choices=t['choices'], teacher_prediction=t['prediction'],
                student_prediction=s['prediction'], teacher_credit=t['credit'], student_credit=s['credit']))
    return dict(paired_teacher_minus_student_accuracy=clustered_ci(difference),
        discordant=discordant, discordant_cases=len(discordant))
