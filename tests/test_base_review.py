import copy
import math

import pytest

from jmicro.base_review import validate_body


def body_fixture():
    rows = [dict(doc_id='a', body_bytes=10, body_tokens=3, scored_body_tokens=3,
                 body_nll=2., eos_nll=.5),
            dict(doc_id='b', body_bytes=20, body_tokens=5, scored_body_tokens=5,
                 body_nll=4., eos_nll=.7)]
    body = dict(split='dev', documents=2, rows=rows, body_bytes=30, body_tokens=8,
                body_nll=6., eos_nll=1.2, bpb=6 / (math.log(2) * 30),
                context=1024, stride=512, evaluator='batched-heldout-fp32-ce-v1')
    return body, [('a', 10, 3), ('b', 20, 5)]


def test_valid_common_byte_body():
    body, expected = body_fixture()
    assert validate_body(body, expected)


@pytest.mark.parametrize('corruption', ['reorder', 'duplicate', 'missed_teacher', 'wrong_bytes',
                                      'nonfinite', 'test_split', 'wrong_window', 'eos_in_bpb'])
def test_reject_invalid_comparison(corruption):
    body, expected = body_fixture()
    body = copy.deepcopy(body)
    if corruption == 'reorder':
        body['rows'].reverse()
    elif corruption == 'duplicate':
        body['rows'][1] = copy.deepcopy(body['rows'][0])
    elif corruption == 'missed_teacher':
        body['rows'][0]['scored_body_tokens'] -= 1
    elif corruption == 'wrong_bytes':
        body['body_bytes'] += 1
    elif corruption == 'nonfinite':
        body['rows'][0]['body_nll'] = float('nan')
    elif corruption == 'test_split':
        body['split'] = 'test'
    elif corruption == 'wrong_window':
        body['stride'] = 1024
    else:
        body['bpb'] = (body['body_nll'] + body['eos_nll']) / (math.log(2) * body['body_bytes'])
    with pytest.raises(ValueError):
        validate_body(body, expected)
