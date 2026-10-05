from jmicro.condition_diagnostic import make_pairs, render, summarize_choice


def test_counterfactual_targets_reverse_and_preserve_options():
    for category in ('reference','quantity','negation','time','cause'):
        for template in range(5):
            pair=[render(category,'あおい','ひなた','パン','そば',8,3,v,template) for v in (0,1)]
            assert pair[0]['choices']==pair[1]['choices']
            assert pair[0]['label']!=pair[1]['label']
            assert all(r['text']==r['prefix']+r['choices'][r['label']] for r in pair)


def test_arithmetic_labels():
    for n in range(3,13):
        for k in range(1,min(n,20-n)):
            for v in (0,1):
                row=render('quantity','あおい','なお','本','帽子',n,k,v,4)
                assert row['choices'][row['label']]==f'{n-k if v==0 else n+k}個ある。'


def test_split_names_structural_holdout_and_reproducibility():
    train=make_pairs('train',10,[0],1);dev=make_pairs('dev',10,[0,4],2)
    assert train==make_pairs('train',10,[0],1)
    assert not {r['text'] for r in train}&{r['text'] for r in dev}
    assert not any(r['structural_holdout'] for r in train)
    assert sum(r['structural_holdout'] for r in dev)==50
    assert len({r['text'] for r in dev})==100


def test_constant_answer_prior_cannot_pass_both_conditions():
    rows=make_pairs('dev',10,[0,4],2)
    for row in rows:row['correct']=row['label']==0
    result=summarize_choice(rows)
    assert result['accuracy']==.5
    assert result['both_accuracy']==0


def test_full_planned_supply_is_unique_and_terminates():
    for count,templates in ((100,[0]),(500,[0,1,2,3])):
        rows=make_pairs('train',count,templates,202610067)
        assert len(rows)==count*10
        assert len({r['text'] for r in rows})==len(rows)
